# 1.1 Introduction

Thredd's Global Balance Reporting provides balance reports that you can receive at the local time you require, regardless of your organisation's timezone. A balance report contains details of card balances on the system in the past 24 hours. You can use the Balance report to confirm how much money is on a card according to Thredd systems (where Thredd maintain the balance), allowing you to compare the information you hold in your local card database.

Balance reports use Thredd's XML reporting system for Global Balance Reporting, which employs the Secure File Transfer Protocol (sFTP). In the reporting system, Thredd processes incoming requests from the Card Schemes (payment networks) using its real-time authorisation engine.

![](../Resources/Images/XML_reporting.png)

Figure 1: XML Reporting

## 1.1.1 Global Balance Report Details

Clients in the following EHI modes use these reports where Thredd maintains details of card balances. These include:

* Cooperative Processing (mode 2)
* Full Service Processing (mode 3)
* Gateway Processing with STIP (mode 4)

You can also use reports for balances where EHI is not being used.

Global Balance Reporting ensures that reports contain details of the balance on each card at the time of your chosen cut off and generation. Therefore, Thredd can send you the balance data whenever required.

## 1.1.2 Other Types of Reports

In addition to reports for balances, Thredd provides these other types of reports:

* **Non-Clearing Data Transaction Report**: â contains details of daily authorisations, loads and unloads, Thredd fees and other authorisation data.
* **Clearing Data Transaction Report**: â contains details of financials, interchange fees, chargebacks and other presentment data for Issuers (BIN sponsors) and Self-Issuers. For more information, see the Global Transaction Reporting Guide.

  **Legacy Balance Report**: â this report provides details of the balance on each card on each card as at midnight UK time[1 Local UK time, which is either Greenwich Mean Time (GMT) or British Summer Time (BST); For details, see: https://www.gov.uk/when-do-the-clocks-change.](#) or at a specific time when the XML is run. If you are migrating to the new Balance XML report, you may want to run this report until you are ready to switch over. Note that Thredd provides both types of reports. However, in the future, new clients will use the new balance XML report only.

* **Fee Collection Report:** â gives a summary of Scheme (VISA/Mastercard/MNE) Fees by [ICA![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Interbank Card Association Number (ICA) is a five-digit number assigned by MasterCard to a financial institution, third-party processor or other member to identify the member in the transaction.](#) and currency. You can use this report to reconcile against Mastercard/Visa/MNE Settlement summary reports. The Fee Collection Report includes transaction categories such as Interregional non-financial ATM transaction fees, fees for ATM PIN management and ATM Balance Inquiry fees. For more information, contact your Thredd Implementation Manager or Account Manager.
* **Quarterly Scheme Report:** â contains information to complete your scheme regulatory reporting for Mastercard's Quarterly Management Reports and Visa's Global Operating Certificates. Thredd provides this report to Issuers and Self-Issuers. Sent on a quarterly basis, this report includes details such as the number of live cards, cards issued, and information on card activity and status. For more information, contact your Implementation Manager or Account Manager.