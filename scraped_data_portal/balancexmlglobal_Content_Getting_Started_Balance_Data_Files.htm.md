# 1.2 Balance Data Files

For Global Balance Reporting, Thredd can supply you with daily Balance XML Report files using [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#), which you can receive at your required cut-off time.

Thredd deletes the sFTP files from the sFTP server after two calendar days. The files are stored on Thredd's archive server for a limited period. Bear in mind that if you need to keep transaction records over time, you must follow the right business processes for maintaining the records.

For an example of a Balance XML Report file, see [Balance XML Example.](../Reference/Balance_XML_Example.htm)

## 1.2.1 File Sending Schedule

As a Global Balance Report consists of a snapshot of the balance at any time of day, the FromTime and ToTime in the file generation schedule is the same. The generation job for the file can take up to two hours. The following table summarises the time settings:

| Time | Description |
| --- | --- |
| InitiationTime | The time of day you select for Thredd to start the generation of an individual report. |
| ToTime | The latest time threshold/end interval during the day for the timestamp transactions to be included in the report. InitiationTime is always >= to the ToTime. |
| FromTime | The earliest time threshold/start interval during the day for timestamp transactions to be included in the report. By default, FromTime = ToTime over a 24h period. |
| GenerationTime | The time needed to produce a report, spanning between InitiationTime and the time when the XML file for the report has been created. |
| TransportationTime | Disk and network time needed to copy a readily available XML file/report to the client sFTP folder. |
| DeliveryTime | The time when the XML file/report is available in the client's sFTP folder for pick-up. |

### Card Scheme Considerations

Though not essential, you can choose to run a Global Balance Report after the clearing cycles from the card schemes. Running a report after the clearing cycles considers the refund and chargeback amounts in the balances from Mastercard, Visa, and Discover transactions.

Clearing cycles do not apply to MNE (Mastercard Network Exchange) transactions. This is because MNE sends transactions that are SMS messages, where authorisation and clearing data are in the same message.

The clearing cycles are as follows:

| Scheme | Cycle Description |
| --- | --- |
| Mastercard | Mastercard has 6 clearing cycles per day, seven days per week. Mastercard sends Thredd the clearing files, which contain the settlement data.  Thredd processes all 8 cycles before generating the report with clearing data.  Data from cycles 5-8 from the night before and 1-4 from the current day provide the aggregate data of a settlement day for most regions. The cycles contain all the information you need to reconcile your settlements with Mastercard. |
| Visa | Visa provides two files, Domestic and International, each day with different timings for some regions (for example, Australia and Hong Kong).  The domestic cycle starts at 9am, while the international cycle starts at mid-day, 7 days a week. |
| Discover | Clearing occurs once per day. |

## 1.2.2 File Naming Convention

The Global Balance Report XML file uses the following naming convention:`THRD-PPPP-BAL-YYYYMMDDHHMM-YYYYMMDDHHMM.PX.xml`

Where:

* THRD = Thredd
* PPP = The 3-10 letter XML file prefix set up for your programme.
* BAL = Denotes the file as a balance.
* YYYY = Year (4 digits)
* MM = Month (2 digits)
* DD = Day (2 digits)

The two dates as `YYYYMMDDHHMM-YYYYMMDDHHMM` correspond to the From and To dates in year, month and day, which are the same. PX denotes the Production environment for the reports, where X is the value of the respective Production environment for generating reports.

For example:

`THRD-PPP-BAL-202405191300-202405191300.P1.xml`

#### Regenerated Reports

Thredd includes \_REG in the filename of a Balance Report for regeneration. The following is an example:

* `THRD-PPP-BAL-202405191300-202405191300_REG.P1.xml`

The filename of the regenerated report includes the same From and To dates as the original report.

Thredd increments a number for multiple regenerations. For example, the filename is as follows for a second regeneration of a Balance Report: `THRD-MCB-BAL-202401250000-202401260000_REG.P1(1).xml`.

For details of which production environment applies to your programme, check with your Thredd implementation manager or account manager.

## 1.2.3 Encryption and Encoding

XML files are encrypted using [Pretty Good Privacy,![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An encryption program that provides cryptographic privacy and authentication for data communication.](#) where keys are shared. For details, contact your implementation manager.

All of the XML data files are well-formed XML (UTF-8 encoded).

As XML is case-sensitive, you should follow the correct casing for all XML elements and attribute names when processing the message.