# 1.2 Transactional Data Files

For Global Transaction Reporting, Thredd can supply you with daily transaction-related data reports in the XML file format at the time settings you require. The files are delivered to you via sFTP.

Bear in mind that if you need to keep transaction records over time, you must follow the right business processes for maintaining the records.

## 1.2.1 XML File Contents

File contents include either the Clearing Report or the Non-Clearing Report.

### Clearing Report

The Clearing Report contains all the available presentments on the Thredd platform, which have been received and processed at the InitiationTime. This is data that is used for clearing. For an example of a Clearing Report, see [Clearing Transaction Report Example.](../Reference/Clearing_Transaction_Report_Example.htm)

### Non-Clearing Report

The Non-Clearing Report contains authorisation, load, unload and fee data on the Thredd platform. This data is received and processed at the InitiationTime. For an example of a Non-Clearing Report, see [Non-Clearing Transaction Report Example.](../Reference/Non_clearing_Transaction_Report_Example.htm)

## 1.2.2 File Sending Schedule

Thredd can send files of generated reports at a time that meets your business requirements. For each report type, you can choose the InitiationTime, ToTime and FromTime settings. The following table summarises the time settings:

| Time | Description |
| --- | --- |
| InitiationTime | The time of day you select for Thredd to start the generation of an individual report. |
| ToTime | The latest time threshold/end interval during the day for the timestamp transactions to be included in the report. InitiationTime is always >= to the ToTime. |
| FromTime | The earliest time threshold/start interval during the day for timestamp transactions to be included in the report. By default, FromTime = ToTime over a 24h period. |
| GenerationTime | The time needed to produce a report, spanning between InitiationTime and the time when the XML file for the report has been created. |
| TransportationTime | Disk and network time needed to copy a readily available XML file/report to the client sFTP folder. |
| DeliveryTime | The time when the XML file/report is available in the client's sFTP folder for pick-up. |

GenerationTimes and TransportationTimes determine the DeliveryTime of the report. The DeliveryTime depends on the number or volume of transactions in the file that passed from the report InitiationTime.

By default, Thredd use the following logic for the reports:

* **Non-Clearing Report** â By default, the InitiationTime is after midnight in your selected timezone. The FromTime is 00:00 of the previous day (D-1) in relation to the InitiationTime. The ToTime is 23:59 of the previous day (D-1) in relation to the report InitiationTime.
* **Clearing Report** â The Initiation, From and ToTimes are selectable (FromTime = ToTime over a 24h period).

### Card Scheme and Gateway Provider Considerations

If you want your Clearing Reports to include transactions, you need to consider the clearing cycles for these card schemes. The clearing cycles can influence the XML file sending schedule from Thredd for the Clearing Reports. For [MNE![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A US PIN debit network provider for opening access to US debit networks.](#)[1 MNE (Mastercard Networks Exchange) This is a US PIN debit network provider for opening access to US debit networks.](#) gateway transactions, the clearing cycles **do not** apply. This is because MNE sends transactions that are SMS messages, where authorisation and clearing data are in the same message. When Thredd sends to you MNE transactions data, these are included within **Non-Clearing Reports**.

The clearing cycles are summarised as follows:

* **Mastercard** â There are 6 clearing cycles per day, seven days per week. After each clearing cycle, Mastercard sends Thredd clearing files, which contain the settlement data. Data from cycles 5-6 from the night before and 1-4 from current day form a compete settlement day picture for most regions. These contain all the information you need to reconcile your settlements with Mastercard.
* **Visa** â Visa provide 2 clearing files (Domestic and International) each day. For International visa cycles, different timings exist for some regions (For example, Australia and Hong Kong). There is a maximum file size where, for the largest clients, it is possible that more than one Domestic and/or International file will be received on the same day. Visa domestic cycles start at 9 am, while international cycles start at mid-day. The clearing cycles occur for 7 days a week.
* **Discover** â Discover implement one release cycle per day.

## 1.2.3 File Naming Convention

The transaction report files that you receive from Thredd use the following naming convention:

| Type of Report | Environment | Naming Convention |
| --- | --- | --- |
| Non-Clearing Report | PX | `THRD-PPPP-NCLR-YYYYMMDDHHMM-YYYYMMDDHHMM.PX.xml` |
| Clearing Report | PX | `THRD-PPPP-CLR-YYYYMMDDHHMM-YYYYMMDDHHMM.PX.xml` |

Where:

* **THRD** â Abbreviation for Thredd.
* **PPPP** â Programme manager code or name.
* **NCLR** â Report code. NCLR is for a Non-Clearing file and CLR is for a clearing file.
* **YYYYMMDDHHMM** â FromTime, first occurrence after report code. This includes YYYY for year (4 digits), MM for month (2 digits) and DD for day (2 digits).
* **YYYYMMDDHHMM** â ToTime, second occurrence after report code). This includes YYYY for year (4 digits), MM for month (2 digits) and DD for day (2 digits).
* **PX** - Thredd production environment used to generate the report, value of X indicating the exact environment.

#### Examples

The following shows examples of files for a Non-Clearing Report and Clearing Report.

| Example | Type of Report | Description |
| --- | --- | --- |
| `THRD-ABC-NCLR-202401250000-202401260000.P1.xml` | Non-Clearing Report | This file includes a snapshot of all non-clearing transactions recorded for the ABC program manager, available on the Thredd platform. The file includes the respective statuses at the report `InitiationTime` with a timestamp between the 25th of January 2024, 00:00 and the 26th of January 2024, 00:00 on Thredd's Production 1 environment. |
| `THRD-ABC-CLR-202402151400-202402161400.P2.xml` | Clearing Report | This file includes a snapshot of all clearing transactions recorded for the ABC program manager, available on the Thredd platform. This file includes the respective statuses at the report `InitiationTime` with a timestamp between the 15th of February 2024, 14:00 and the 16th of February 2024, 14:00 on Thredd's Production 2 environment. |

For details on which production environment applies to your programme, check with your Thredd implementation manager or account manager.

#### Regenerated Reports

Thredd includes \_REG in the filename of a Non-Clearing Report or Clearing Report for regeneration. The filenames can include the following naming conventions:

* `THRD-PPPP-NCLR-YYYYMMDDHHMM-YYYYMMDDHHMM_REG.PX.xml`
* `THRD-PPPP-CLR-YYYYMMDDHHMM-YYYYMMDDHHMM_REG.PX.xml`

| Example | Type of Report | Description |
| --- | --- | --- |
| `THRD-ABC-NCLR-202501250000-202501260000_REG.P1.xml`. | Non-Clearing Report | The regenerated report includes the same timestamp as the original report recorded for the ABC program manager. In this case, the timestamp of the original report is between the 25th of January 2025, 00:00 and the 26th of January 2025, 00:00. The report is regenerated in the P1 production environment. |
| `THRD-ABC-CLR-202502151400-202502161400_REG.P2.xml`. | Clearing Report | The regenerated report includes the same timestamp as the original report recorded for the ABC program manager. In this case, the timestamp of the original report is between the 15th of February 2025, 14:00 and the 16th of February 2025, 14:00. The report is regenerated in the P2 production environment. |

Thredd increments a number for multiple regenerations. For example, the filename is as follows for a second regeneration of a Non-Clearing Report: `THRD-MCB-NCLR-202401250000-202401260000_REG.P1(1).xml`.

## 1.2.4 Encryption and Encoding

XML files are encrypted using [PGP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Pretty Good Privacy (PGP) is an encryption system used for both sending encrypted emails and encrypting sensitive files.](#), which requires the sharing of keys. For details, contact your implementation manager.

All of the XML data files are well-formed XML (UTF-8 encoded).

As XML is case-sensitive, you should ensure that you follow the correct casing for all XML elements and attribute names when processing the message.