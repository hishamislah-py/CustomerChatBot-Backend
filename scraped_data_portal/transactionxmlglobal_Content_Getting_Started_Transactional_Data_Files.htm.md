# 4.11 Transactional Data Files

Thredd can supply you with daily Transaction XML files. Transaction XML files are delivered to you via [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#).

sFTP files are deleted from the Thredd sFTP server after two calendar days. They are stored on our archive server for a limited period.

## 4.11.1 Sending of Files

Transactional data files are created every day (excluding UK Public Holidays). When we have received the settlement information from the card scheme, we send this to you. For UK issuers, this is in the afternoon, between 2:30-5pm, UK time[1 Local UK time, which is either Greenwich Mean Time (GMT) or British Summer Time (BST). For details, see: https://www.gov.uk/when-do-the-clocks-change.](#). For issuers in other regions, the timings may vary.

### Mastercard Cycles

Mastercard has 6 cycles clearing cycles per day, seven days per week. After each clearing cycle, Mastercard sends us clearing files, which contain the settlement data.

We wait until we process all 8 cycles before generating the transaction XML report. We send you a single daily file.

Data from cycles 5-8 from the night before and 1-4 from current day form a compete settlement day picture for most regions. These contain all the information you need to reconcile your settlements with Mastercard.

#### Asia-Pacific

For Asia-Pacific clients we process cycles 2-8 for the previous day and cycle 1 from the current day, and include them in the daily transaction XML report.

### Visa Cycles

Visa provide 2 files (Domestic and International) each day with different timings for some regions (For example, Australia and Hong Kong). There is a maximum filesize so for the largest clients it is possible that more than one Domestic and/or International file will be received on the same day.. [2 Visa Domestic cycle at 9am and International cycle at mid-day, 7 days a week.](#)

After processing, we will create the transaction XML file and send to you.

### Discover Cycles

Discover provide 3 sets of files from Monday to Friday between 10 am and 2 pm GMT which include:

* **Issuer Interchange** (main clearing file for presentments and disputes)
* **Issuer Detail** (settlement amounts and presentment fees)
* **Issue Disputes and Fee** (chargeback updates and fee collection records)
* There are also monthly Sysops files, that hold cycle parameters, and the daily foreign exchange files. Discover receives the SysOps files on the last Friday of each month.

## 4.11.2 File Contents

The daily transaction XML file contains:

* All [presentments![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). Also known as Clearing.](#) that have a settlement date of this day (D)
* Any presentments that have a settlement date of day D-1 and arrived too late for the previous day's XML generation
* All non-presentment transactions for day D-1.

## 4.11.3 File Format and Encryption

For an example of a transaction XML file, see [Transaction XML Example.](../Reference/Transaction_XML_Example.htm)

### File Naming Convention

The transaction XML files use the following naming convention:

#### On-Premise Customers (P0)

`GPS-PPPtxnexpYYYYMMDD.xml`

#### Thredd Cloud (P1 and P2)

`GPS-PPPtxnexpYYYYMMDD.Pn.xml`

Where:

* PPP= The 3-10 letter XML file prefix set up for your programme.
* YYYY= year (4 digits)
* MM = month (2 digits)
* DD = day (2 digits)
* Pn = production environment (2 digits), such as P1 and P2. (Not applicable to customers in our UK data centre production environment)

For example:

`GPS-NWCtxnexp20230130.P1.xml`

The production environment variable is relevant to customers in one of our AWS Cloud-based production environments (P1 and P2) and does not apply to exisiting customers in our UK data centre production environment (P0). For details of which production environment applies to your programme, please check with your Thredd implementation manager or account manager.

### Encryption

XML files are encrypted using [PGP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Pretty Good Privacy (PGP) is an encryption system used for both sending encrypted emails and encrypting sensitive files.](#), which requires sharing of keys. For details, contact your implementation manager.

### Encoding / Type

Transaction XML data files are well-formed XML (UTF-8 encoded).

XML is case-sensitive, ensure you follow the correct casing for all XML elements and attribute names when processing the message.