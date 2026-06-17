# 1.2 Level 2 and 3 Data Files

For Level 2 and 3 Reporting, Thredd can supply you with daily data reports in the XML file format. This page describes the file contents of the Level 2 and 3 reports, the file sending schedule, naming convention, and encryption/encoding requirements.

Bear in mind that if you need to keep transaction records over time, you must follow the standard business processes in your organisation for maintaining the records.

## 1.2.1 XML File Contents

Thredd can supply you with daily XML files that contain clearing data where there are relevant Level 2 and 3 data entries. The schemes provide this clearing data to Thredd in raw message form. Upon receipt, Thredd parses the data, modifies it in a standard format across all the supported schemes, and adds additional Thredd-specific data before building the Level 2 and 3 data XML files/reports. Thredd then delivers the XML files through [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). The clearing data follows the standard clearing cycles for the schemes (see [Card Scheme and Gateway Provider Considerations](#CardScheme)).

sFTP files are deleted from the Thredd sFTP server after two calendar days. They are stored on our archive server for a limited period.

## 1.2.2 Sending Schedule

Thredd can send files of generated reports at a time that meets your business requirements. You can choose the InitiationTime, ToTime and FromTime settings. The following table summarises the time settings:

| Time | Description |
| --- | --- |
| InitiationTime | The time of day you select for Thredd to start the generation of the report. |
| ToTime | The latest time threshold/end interval during the day for the timestamp transactions to be included in the report. InitiationTime is always >= to the ToTime. |
| FromTime | The earliest time threshold/start interval during the day for timestamp transactions to be included in the report. By default, FromTime = ToTime over a 24h period. |
| GenerationTime | The time needed to produce a report, spanning between InitiationTime and the time when the XML file for the report has been created. |
| TransportationTime | Disk and network time needed to copy a readily available XML file/report to the client sFTP folder. |
| DeliveryTime | The time when the XML file/report is available in the client's sFTP folder for pick-up. |

GenerationTimes and TransportationTimes determine the DeliveryTime of the report. The DeliveryTime depends on the number or volume of transactions in the file that passed from the report InitiationTime. The Initiation, From and ToTimes are selectable (FromTime = ToTime over a 24h period).

### Card Scheme and Gateway Provider Considerations

You should consider the clearing cycles for the different schemes when selecting the Level 2 and 3 XML file generation times. The following summarises the clearing cycles:

* **Mastercard** â There are six clearing cycles per day, seven days per week. After each clearing cycle, Mastercard sends Thredd clearing files, which contain the settlement data. Data from cycles 5-6 from the night before and 1-4 from current day form a compete settlement day picture for most regions. These contain all the information you need to reconcile your settlements with Mastercard.
* **Visa** â Visa provide two clearing files (Domestic and International) each day. For International visa cycles, different timings exist for some regions (For example, Australia and Hong Kong). There is a maximum file size where, for the largest clients, it is possible that more than one Domestic and/or International file will be received on the same day. Visa domestic cycles start at 9 am, while international cycles start at mid-day. The clearing cycles run seven days a week.

* **Discover** â There are three sets of files sent by Discover from Monday to Friday between 10 am and 2 pm GMT. The files include:

  + **Issuer Interchange** (main clearing file for presentments and disputes)
  + **Issuer Detail** (settlement amounts and presentment fees)
  + **Issue Disputes and Fee** (chargeback updates and fee collection records)

  There are also monthly Sysops files which hold cycle parameters and daily foreign exchange files. Discover receives the SysOps files on the last Friday of each month.

## 1.2.3 File Naming Convention

The Level 2 and 3 report files that you receive from Thredd use the following naming convention: `THRD-PPPP-L2L3-YYYYMMDDHHMM-YYYYMMDDHHMM.PX.xml`

Where:

* **THRD** â Abbreviation for Thredd.
* **PPPP** â Programme manager code or name.
* **L2L3** â The report code for Level 2 and 3 reports.
* **YYYYMMDDHHMM** â FromTime, first occurrence after report code. This includes YYYY for year (4 digits), MM for month (2 digits) and DD for day (2 digits).
* **YYYYMMDDHHMM** â ToTime, second occurrence after report code). This includes YYYY for year (4 digits), MM for month (2 digits) and DD for day (2 digits).
* **PX** - Thredd production environment used to generate the report, value of X indicating the exact environment.

#### Example

The following shows an example of files for a Level 2 and 3 report: `THRD-ABC-L2L3-202501250000-202501260000.P1.xml`

This file includes a snapshot of transactions recorded for the example ABC program manager, available on the Thredd platform. The file includes the respective statuses at the report `InitiationTime` with a timestamp between the 25th of January 2025, 00:00 and the 26th of January 2025, 00:00 on Thredd's Production 1 environment.

For details on which production environment applies to your programme, check with your Thredd implementation manager or account manager.

#### Regenerated Reports

Thredd includes \_REG in the filename of the report for regeneration. The filenames include the following naming conventions: `THRD-ABC-L2L3-YYYYMMDDHHMM-YYYYMMDDHHMM_REG.PX.xml`

The following shows an example of files for a Level 2 and 3 report: `THRD-ABC-L2L3-202501250000-202501260000_REG.P1.xml`

The regenerated report includes the same timestamp as the original report recorded for the example ABC program manager. In this case, the timestamp of the original report is between the 25th of January 2025, 00:00 and the 26th of January 2025, 00:00. The report is regenerated in the P1 production environment.

Thredd increments a number for multiple regenerations. For example, the filename is as follows for a second regeneration of the report: `THRD-ABC-L2L3-202401250000-202401260000_REG.P1(1).xml`.

## 1.2.4 Encryption and Encoding

XML files are encrypted using [PGP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Pretty Good Privacy (PGP) is an encryption system used for both sending encrypted emails and encrypting sensitive files.](#), which requires the sharing of keys. For details, contact your implementation manager.

All of the XML data files are well-formed XML (UTF-8 encoded).

As XML is case-sensitive, you should ensure that you follow the correct casing for all XML elements and attribute names when processing the XML files.