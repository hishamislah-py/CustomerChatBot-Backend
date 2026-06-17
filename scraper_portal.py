"""Web ingestion for the Thredd technical documentation portal (https://docs.thredd.ai/).

Unlike the Cards API docs (``scraper.py``, a ReadMe.io site with a clean ``.md`` export),
this portal is **MadCap Flare WebHelp**: static server-rendered ``.htm`` topic pages with
no Markdown export. Discovery is driven by a *sitemap index* (``/sitemapindex/Sitemap.xml``)
that points at ~40 per-project child sitemaps; each child lists the leaf ``Content/*.htm``
topic URLs. Each topic page is fetched, stripped of Flare chrome, and converted to Markdown
so it chunks/embeds exactly like the existing corpus.

The disk cache (``scraped_data_portal/`` + ``scrape_manifest_portal.json``) means restarts
don't re-hit the site; a re-scrape only happens on an explicit refresh. Output is a list of
LangChain ``Document`` objects with the same metadata shape as ``ThreddDocsScraper`` so the
downstream chunking / FAISS / retrieval pipeline is unchanged.
"""

import os
import re
import json
import time
import hashlib
import logging
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import List, Optional, Tuple
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from langchain_core.documents import Document

logger = logging.getLogger(__name__)

BASE_URL = "https://docs.thredd.ai"
SITEMAP_INDEX_URL = f"{BASE_URL}/sitemapindex/Sitemap.xml"
USER_AGENT = "ThreddDocsRAGBot/1.0 (+https://docs.thredd.ai)"
REQUEST_TIMEOUT = 30          # seconds
RATE_LIMIT_DELAY = 0.5        # seconds between requests (polite, sequential crawl)
CACHE_DIR = "scraped_data_portal"
MANIFEST_FILE = "scrape_manifest_portal.json"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Discard pages that are navigation/search rather than documentation content.
_SKIP_BASENAMES = {"search.htm", "default.htm"}
# Flare skin / proxy elements that carry no real content (matched on class substring).
_CHROME_CLASS_RE = re.compile(
    r"breadcrumb|MCBreadcrumbs|topic-toolbar|MCMiniTocBox|"
    r"navigation|nav-search|footer|header-content",
    re.IGNORECASE,
)


class ThreddPortalScraper:
    """Discovers and fetches the Thredd technical docs portal as clean Markdown."""

    def __init__(self, base_url: str = BASE_URL, cache_dir: str = CACHE_DIR,
                 rate_limit_delay: float = RATE_LIMIT_DELAY, timeout: int = REQUEST_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.cache_dir = cache_dir
        self.rate_limit_delay = rate_limit_delay
        self.timeout = timeout
        self.manifest_path = MANIFEST_FILE

        # Session with a custom User-Agent and automatic retry/backoff on rate limits.
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        retry = Retry(
            total=3,
            backoff_factor=2,                       # 2s, 4s, 8s
            status_forcelist=[429, 500, 502, 503, 504],
            respect_retry_after_header=True,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        os.makedirs(self.cache_dir, exist_ok=True)

    # ------------------------------------------------------------------ helpers

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def content_hash(text: str) -> str:
        """MD5 of page content (mirrors the change detection used by the API-docs scraper)."""
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def _normalize_url(self, url: str) -> str:
        """Canonical form for dedup/metadata: drop fragment + query, trailing slash."""
        url = url.split("#")[0].split("?")[0].strip()
        if url.endswith("/") and len(url) > len(self.base_url) + 1:
            url = url.rstrip("/")
        return url

    def _is_doc_url(self, url: str) -> bool:
        """Keep only Flare content topics: under this site, a ``Content/...`` ``.htm`` page."""
        if not url.startswith(self.base_url):
            return False
        if not url.lower().endswith(".htm"):
            return False
        path = urlparse(url).path
        if "/Content/" not in path:
            return False
        return os.path.basename(path).lower() not in _SKIP_BASENAMES

    def _section_for(self, url: str) -> str:
        """Project slug (first path segment) as the section, e.g. 'ehi', 'tokenisation'."""
        segments = urlparse(url).path.strip("/").split("/")
        return segments[0] if segments and segments[0] else ""

    def _cache_path(self, page_url: str) -> str:
        path = urlparse(page_url).path.strip("/")
        slug = re.sub(r"[^A-Za-z0-9._-]", "_", path) or "index"
        return os.path.join(self.cache_dir, slug + ".md")

    @staticmethod
    def _is_sitemap_loc(url: str) -> bool:
        return url.lower().endswith("sitemap.xml")

    # ------------------------------------------------------------------ network

    def _fetch(self, url: str) -> Optional[requests.Response]:
        """GET a URL with timeout + session-level retry. Returns None on 404/error."""
        resp = None
        try:
            resp = self.session.get(url, timeout=self.timeout)
        except requests.RequestException as e:
            logger.warning("Request failed for %s: %s", url, e)
            return None
        finally:
            time.sleep(self.rate_limit_delay)  # politeness / rate limiting

        if resp.status_code == 404:
            logger.info("404 Not Found: %s", url)
            return None
        if not resp.ok:
            logger.warning("HTTP %s for %s", resp.status_code, url)
            return None
        return resp

    @staticmethod
    def _iter_locs(xml_bytes: bytes) -> List[str]:
        """Return every <loc> text in a sitemap or sitemap-index document."""
        locs: List[str] = []
        try:
            root = ET.fromstring(xml_bytes)
        except ET.ParseError as e:
            logger.warning("Failed to parse sitemap XML: %s", e)
            return locs
        for node in root.iter():
            if node.tag.endswith("loc") and node.text:
                locs.append(node.text.strip())
        return locs

    def discover_urls(self) -> List[dict]:
        """Return a deduped list of {url, section} for every content topic.

        Walks the sitemap *index* -> per-project child sitemaps -> leaf ``Content/*.htm``.
        """
        entries: dict = {}  # normalized_url -> {url, section}

        resp = self._fetch(SITEMAP_INDEX_URL)
        if resp is None:
            logger.warning("Could not load sitemap index %s", SITEMAP_INDEX_URL)
            return []

        child_sitemaps = [u for u in self._iter_locs(resp.content) if self._is_sitemap_loc(u)]
        logger.info("Sitemap index lists %d child sitemaps", len(child_sitemaps))

        for sitemap_url in child_sitemaps:
            child = self._fetch(sitemap_url)
            if child is None:
                continue
            for loc in self._iter_locs(child.content):
                norm = self._normalize_url(loc)
                if self._is_doc_url(norm) and norm not in entries:
                    entries[norm] = {"url": norm, "section": self._section_for(norm)}

        result = list(entries.values())
        logger.info("Discovered %d unique documentation topics", len(result))
        return result

    def fetch_page_markdown(self, page_url: str) -> Tuple[Optional[str], Optional[str]]:
        """Fetch a ``.htm`` topic and return (markdown, title). (None, None) if empty."""
        resp = self._fetch(page_url)
        if resp is None:
            return None, None
        resp.encoding = resp.encoding or "utf-8"

        soup = BeautifulSoup(resp.text, "html.parser")

        # Title: prefer the first <h1>, else <title> (drop any " | Site" suffix).
        title = None
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            title = h1.get_text(strip=True)
        elif soup.title and soup.title.get_text(strip=True):
            title = soup.title.get_text(strip=True).split("|")[0].strip()

        body = soup.body or soup
        # Strip non-content elements before converting to Markdown.
        for tag in body.find_all(["script", "style", "noscript", "nav", "header", "footer"]):
            tag.decompose()
        for tag in body.find_all(class_=_CHROME_CLASS_RE):
            tag.decompose()

        markdown = md(str(body), heading_style="ATX")
        # Collapse the runs of blank lines Flare markup tends to produce.
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

        if not markdown or len(markdown) < 20:
            return None, title
        return markdown, title

    # ------------------------------------------------------------------ documents

    @staticmethod
    def to_document(page_url: str, content: str, title: Optional[str],
                    section: Optional[str]) -> Document:
        return Document(
            page_content=content,
            metadata={
                "source": page_url,
                "source_url": page_url,
                "title": title or page_url,
                "section": section or "",
                "source_file": title or page_url,  # kept for legacy search/list code
            },
        )

    # ------------------------------------------------------------------ cache / manifest

    def load_manifest(self) -> dict:
        if os.path.exists(self.manifest_path):
            try:
                with open(self.manifest_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def save_manifest(self, manifest: dict) -> None:
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

    def _load_from_cache(self, pages: dict) -> List[Document]:
        documents = []
        for url, info in pages.items():
            # Recompute the path for the current OS rather than trusting the stored
            # ``cache_file`` (Windows backslash paths won't resolve on Linux).
            cache_file = self._cache_path(url)
            if os.path.exists(cache_file):
                try:
                    with open(cache_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    documents.append(
                        self.to_document(url, content, info.get("title"), info.get("section"))
                    )
                except OSError as e:
                    logger.warning("Failed to read cache %s: %s", cache_file, e)
        return documents

    # ------------------------------------------------------------------ orchestrator

    def scrape_all(self, force: bool = False) -> Tuple[List[Document], bool]:
        """Return (documents, changed).

        force=False: load from the disk cache when available (no network).
        force=True:  re-fetch every page, diff content hashes against the manifest.
        """
        manifest = self.load_manifest()
        pages = manifest.get("pages", {})

        # Fast path: serve from cache unless forced or the embedding model changed.
        if not force and pages and manifest.get("embedding_model") == EMBEDDING_MODEL:
            docs = self._load_from_cache(pages)
            if docs:
                logger.info("Loaded %d portal pages from cache (no network)", len(docs))
                return docs, False

        logger.info("Scraping Thredd documentation portal from %s ...", self.base_url)
        entries = self.discover_urls()
        if not entries:
            logger.warning("No URLs discovered; falling back to cache if available.")
            return self._load_from_cache(pages), False

        new_pages: dict = {}
        documents: List[Document] = []
        changed = False
        now = self._now_iso()

        for entry in entries:
            url = entry["url"]
            try:
                content, title = self.fetch_page_markdown(url)
                if not content:
                    logger.info("Skipping (no content): %s", url)
                    continue
                section = entry.get("section") or ""
                chash = self.content_hash(content)

                cache_file = self._cache_path(url)
                with open(cache_file, "w", encoding="utf-8") as f:
                    f.write(content)

                new_pages[url] = {
                    "title": title or url,
                    "section": section,
                    "content_hash": chash,
                    # Store forward-slash paths so the manifest is portable across OSes.
                    "cache_file": cache_file.replace(os.sep, "/"),
                    "fetched_at": now,
                }
                documents.append(self.to_document(url, content, title, section))

                old = pages.get(url)
                if old is None or old.get("content_hash") != chash:
                    changed = True
            except Exception as e:  # one bad page must never abort the whole run
                logger.warning("Failed to scrape %s: %s", url, e)
                continue

        if set(pages) - set(new_pages):  # pages that disappeared
            changed = True

        self.save_manifest({
            "scraped_at": now,
            "base_url": self.base_url,
            "embedding_model": EMBEDDING_MODEL,
            "pages": new_pages,
        })
        logger.info("Scraped %d portal pages (changed=%s)", len(documents), changed)
        return documents, changed


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    docs, changed = ThreddPortalScraper().scrape_all(force=True)
    print(f"\nScraped {len(docs)} pages (changed={changed}).")
    if docs:
        print("Sample metadata:", docs[0].metadata)
        print("Sample content (first 300 chars):\n", docs[0].page_content[:300])
