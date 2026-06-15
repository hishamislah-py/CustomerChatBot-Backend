"""Web ingestion for the Thredd Cards API documentation (https://cardsapidocs.thredd.com/).

The docs are hosted on ReadMe.io and expose a clean Markdown export of every page
(append ``.md`` to any doc URL) plus an ``llms.txt`` index of all pages. This module
discovers every doc URL, fetches the clean Markdown, caches it to disk, and returns
LangChain ``Document`` objects ready for chunking/embedding.

The disk cache (``scraped_data/`` + ``scrape_manifest.json``) means restarts don't
re-hit the site; a re-scrape only happens on an explicit refresh.
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
from langchain_core.documents import Document

logger = logging.getLogger(__name__)

BASE_URL = "https://cardsapidocs.thredd.com"
LLMS_TXT_URL = f"{BASE_URL}/llms.txt"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
USER_AGENT = "ThreddDocsRAGBot/1.0 (+https://cardsapidocs.thredd.com)"
REQUEST_TIMEOUT = 30          # seconds
RATE_LIMIT_DELAY = 0.5        # seconds between requests (polite, sequential crawl)
CACHE_DIR = "scraped_data"
MANIFEST_FILE = "scrape_manifest.json"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Matches markdown links: [Title](https://...)
_LINK_RE = re.compile(r"\[(?P<title>[^\]]+)\]\((?P<url>https?://[^\s)]+)\)")


class ThreddDocsScraper:
    """Discovers and fetches the Thredd Cards API documentation as clean Markdown."""

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
        """MD5 of page content (mirrors the file-hash change detection used for PDFs)."""
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def _normalize_url(self, url: str) -> str:
        """Canonical form for dedup/metadata: drop fragment, trailing .md, trailing slash."""
        url = url.split("#")[0].strip()
        if url.endswith(".md"):
            url = url[:-3]
        if url.endswith("/") and len(url) > len(self.base_url) + 1:
            url = url.rstrip("/")
        return url

    def _is_doc_url(self, url: str) -> bool:
        """Keep only content pages under this site (e.g. /docs/<slug>), not the home page."""
        if not url.startswith(self.base_url):
            return False
        path = urlparse(url).path.strip("/")
        return "/" in path  # has at least two path segments, e.g. docs/foo

    def _cache_path(self, page_url: str) -> str:
        path = urlparse(page_url).path.strip("/")
        slug = re.sub(r"[^A-Za-z0-9._-]", "_", path) or "index"
        return os.path.join(self.cache_dir, slug + ".md")

    @staticmethod
    def _extract_title(markdown: str, fallback_url: str) -> str:
        for line in markdown.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        slug = urlparse(fallback_url).path.strip("/").split("/")[-1]
        return slug.replace("-", " ").title() if slug else fallback_url

    @staticmethod
    def _strip_index_banner(text: str) -> str:
        """Remove the leading ReadMe 'Documentation Index' blockquote from a .md export."""
        lines = text.splitlines()
        i = 0
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        if i < len(lines) and lines[i].lstrip().startswith(">"):
            block, j = [], i
            while j < len(lines) and (lines[j].lstrip().startswith(">") or lines[j].strip() == ""):
                block.append(lines[j])
                j += 1
            blocktext = "\n".join(block).lower()
            if "llms.txt" in blocktext or "documentation index" in blocktext:
                return "\n".join(lines[j:]).strip()
        return text.strip()

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

    def discover_urls(self) -> List[dict]:
        """Return a deduped list of {url, title, section} from llms.txt (+ sitemap fallback)."""
        entries: dict = {}  # normalized_url -> {url, title, section}

        # Primary source: the llms.txt index (gives titles + section grouping).
        resp = self._fetch(LLMS_TXT_URL)
        if resp is not None:
            current_section = None
            for line in resp.text.splitlines():
                if line.startswith("## "):
                    current_section = line[3:].strip()
                    continue
                m = _LINK_RE.search(line)
                if m:
                    norm = self._normalize_url(m.group("url"))
                    if self._is_doc_url(norm) and norm not in entries:
                        entries[norm] = {"url": norm, "title": m.group("title").strip(),
                                         "section": current_section}
        else:
            logger.warning("Could not load %s", LLMS_TXT_URL)

        # Supplement with sitemap.xml for any pages missing from llms.txt.
        resp = self._fetch(SITEMAP_URL)
        if resp is not None:
            try:
                root = ET.fromstring(resp.content)
                for node in root.iter():
                    if node.tag.endswith("loc") and node.text:
                        norm = self._normalize_url(node.text.strip())
                        if self._is_doc_url(norm) and norm not in entries:
                            entries[norm] = {"url": norm, "title": None, "section": None}
            except ET.ParseError as e:
                logger.warning("Failed to parse sitemap.xml: %s", e)

        result = list(entries.values())
        logger.info("Discovered %d unique documentation URLs", len(result))
        return result

    def fetch_page_markdown(self, page_url: str) -> Optional[str]:
        """Fetch the clean Markdown export (page_url + '.md'). None if missing."""
        resp = self._fetch(page_url + ".md")
        if resp is None:
            return None
        resp.encoding = "utf-8"
        content = self._strip_index_banner(resp.text)
        return content or None

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
            # ``cache_file`` — a manifest written on Windows holds backslash paths that
            # os.path.exists() can't resolve on Linux, which would silently skip the cache.
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
                logger.info("Loaded %d documentation pages from cache (no network)", len(docs))
                return docs, False

        logger.info("Scraping Thredd Cards API documentation from %s ...", self.base_url)
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
                content = self.fetch_page_markdown(url)
                if not content:
                    logger.info("Skipping (no markdown): %s", url)
                    continue
                title = entry.get("title") or self._extract_title(content, url)
                section = entry.get("section") or ""
                chash = self.content_hash(content)

                cache_file = self._cache_path(url)
                with open(cache_file, "w", encoding="utf-8") as f:
                    f.write(content)

                new_pages[url] = {
                    "title": title,
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
        logger.info("Scraped %d documentation pages (changed=%s)", len(documents), changed)
        return documents, changed


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    docs, changed = ThreddDocsScraper().scrape_all(force=True)
    print(f"\nScraped {len(docs)} pages (changed={changed}).")
    if docs:
        print("Sample metadata:", docs[0].metadata)
