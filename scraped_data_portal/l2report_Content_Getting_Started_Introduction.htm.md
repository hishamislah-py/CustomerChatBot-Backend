# 1.1 Introduction

Thredd's Level 2 and 3 enhanced data reporting for commercial card customers includes specific product and services data that are associated with day-to-day transactions. The reports enable Thredd to share product and services data from the Card Schemes under the following categories:

| Category | Example Data |
| --- | --- |
| Passenger Transport | Ticket information, covering trip leg details, passenger ticket numbers, travel agency information, routing information, and service class |
| Hotels and lodging | Check-in and room dates |
| Vehicle Rental | Rental duration, vehicle class, and additional charges |
| Fuel | Fuel type, quantity, price per unit |
| Electric cars charging | Miscellaneous data for reports. Note that this is only available from Visa |

Level 2 and 3 reports provide the following benefits:

* Allows card programmes to expand their card portfolios.
* Provides data on a transaction for analytics and reporting.
* Delivers better accountability and transparency in financial operations.

## 1.1.1 Reporting Architecture

The reporting architecture include messages from the relevant Card Schemes (Payment Networks) that enter the Thredd Platform. Thredd then parses the relevant clearing messages that contain Level 2 and 3 data, whereas other clearing messages are ignored in the parsing process. Thredd then creates daily reports for sending to the Program Manager.

![](../Resources/Images/L2L3.png)

Figure 1: Enhanced Reporting for Commercial Cards

## 1.1.2 Report Structure

The daily Level 2 and 3 XML file consists of individual transactions containing data:

* that is specific to Thredd. This includes details of the transaction that the Level 2 and 3 data can link to.
* from the scheme containing Level 2 and 3 reporting data.

The basic structure of the dataset is similar across schemes. However, each individual scheme includes different data within the elements.

![](../Resources/Images/codesnippet_annotated.png)

For complete examples from the different schemes, refer to [Level 2 and 3 Report Examples](../Reference/L2-L3_Report_Example.htm#top).

## 1.1.3 Other Types of Reports

In addition to Level 2 and 3 reports, Thredd generates the:

* Clearing Data Transaction Report
* Non-Clearing Data Transaction Report
* Balance Report
* Fee Collection Report
* Quarterly Scheme Report

### Clearing Data Transaction Report

The Clearing Data Transaction Report contains details of financials, interchange fees, chargebacks and other presentment data for Issuers (BIN sponsors), Self-Issuers, and Program Managers. This report contains transactions that are linked to the Level 2 and 3 reports. For more information, see the [Global Transaction Reporting Guide.](https://docs.thredd.com/transactionxmlglobal/Content/Home_newreport.htm)

### Non-Clearing Data Transaction Report

The Non-Clearing Data Transaction Report contains details of daily authorisations, loads and unloads, Thredd fees and other authorisation data.

### Balance Report

The Balance Report is relevant where Thredd maintains details of card balances, such as in EHI modes 2,3,4 and 5 or where EHI is not being used. This report provides details of the balance on each card at the time of your chosen cut-off and generation. You can use this report to confirm how much money is on the card according to Thredd systems (where Thredd maintain the balance). You can compare this to information you hold in your local card database. Like the transaction reports, you can receive reports at the local time you require regardless of your organisation's time-zone.

### Fee Collection Report

The Fee Collection Report is a daily summary of Scheme (Mastercard/Visa/MNE/Discover) fees by ICA and currency for reconciling against the Mastercard/Visa/MNE/Discover Settlement summary reports. The report is provided to issuers and self-issuers. It includes transaction categories such as Interregional non-financial ATM transaction fees, and fees for ATM PIN management and ATM Balance Inquiry fees. For more information, contact your Thredd Implementation Manager or Account Manager.

### Quarterly Scheme Report

The Quarterly Scheme Report contains quarterly data needed to fill in/submit the quarterly scheme reports:

* **Mastercard** â Quarterly Management Reports
* **VISA** â Global Operation Certificates

The report include details such as the number of live cards, cards issued, and information on card activity and status. This report is provided to issuers and self-issuers. For more information, contact your Thredd Implementation Manager or Account Manager.

### Monthly Scheme Report

The Discover scheme send out reports on a monthly basis.