# 23 Searching for Transactions

The Transactions menu on the [Apata Portal Dashboard](Apata_dashboard.htm#Apata_Portal_Dashboard) enables you to search for transactions.

1. To search for a transaction, select Transactions from the left-hand menu.

   [![](../Resources/Images/Apata/transactions.png "Transactions screen")](../Resources/Images/Apata/transactions.png)

   Figure 32: Search for Transactions
2. Enter the details you'd like to search on and click Search.

Refer to the table below for further details of search options.

| Option | Description |
| --- | --- |
| Transaction ID | Search by Apata's ACS unique ID for the transaction. |
| DS Transaction ID | Unique transaction ID as provided by the directory server of the card scheme (payment network). |
| BIN | The Bank Identification Number (BIN) of the card (first 8 digits). |
| Card ID | Apata configured ID for the card that performed the transaction. |
| Include Deleted Cards | Not applicable to Thredd clients. |
| Was Challenged | Check this option to include transactions where the cardholder was challenged. |
| Was Frictionless | Check this option to include transactions where the cardholder was not challenged (frictionless authentication). |
| Merchant | You can specify the name of the merchant to search for transactions linked to a specific merchant. |
| Date | Specify the start and end date range to search for transactions within a specific period. |
| State | Search by transaction status. Options include: Succeeded, Aborted, Failed, Error, Rejected, Timeout and Cancelled. For details see [Appendix 6: Transaction Status](../Reference_Apata/Transaction_Status.htm). |
| Reason | Search by decline reason. For details see [Appendix 6: Transaction Status > Decline Reasons](../Reference_Apata/Transaction_Status.htm#Decline). |
| Error Code | Search by transaction error code. For details see [Appendix 6: Transaction Status > Error Codes](../Reference_Apata/Transaction_Status.htm#Error). |
| Exemptions | Search by permitted acquirer exemptions. For details see [Appendix 6: Transaction Status > Exemptions](../Reference_Apata/Transaction_Status.htm#Exemptio). |
| Protocol Version | Search by 3D Secure protocol version. Options include: *1.0.2*, *2.1.0* and *2.2.0*.  version 1.0.2 was discontinued in Oct 2022. |
| Device Channel | Search by the channel used during the authentication session. Options include: *App*, *Browser* and *Requestor Initiated*. |

## 23.1 Viewing Transactions

The Transactions screen lists all transactions that match your search criteria. See the example below.

![](../Resources/Images/Apata/Viewing_Transactions.png "Viewing Transactions")

Figure 33: Viewing Transactions

If the Merchant Simulator option has been enabled for your organisation, you can use the Transaction Simulation toggle button (which will appear at the top-right of the Transactions page) to view simulated transactions. See [Viewing Simulated Transactions](Merchant_Simulator.htm#Viewing).

* To view details of a specific transaction, click the ![](../Resources/Images/Apata/View_details.png "View details button") button. See the example below.

![](../Resources/Images/Apata/transaction_details.png "Viewing a Transaction's Details")

Figure 34: Viewing a Transaction's Details

### Viewing Cardholder Interaction Status

* To view details of the system interaction with the cardholder during the 3D Secure session, mouse-hover over the relevant icons: Was Challenged, Was Frictionless, Was Presented Choice, Did Make Choice and Did Whitelist. If any of these conditions occurred, the status is indicates as *true*.

### Viewing Details of Message Types

* To view details of the message types that have been sent during the 3D Secure session between the Card Scheme (payment network), the [ACS![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A system used to manage the 3D Secure authentication service for the issuer (BIN sponsor). During an authentication session, the ACS communicates with the Card Scheme and Thredd systems, and may also interact with the cardholder, by providing Challenge screens.](#) (Apata) and the cardholder's browser, in the right-hand pane of the screen, click the expand button next to the relevant message type.

For example, to view the Challenge HTML message sent to the cardholder, click the ![](../Resources/Images/Apata/down_arrow.png)icon in the  Challenge Html row.   
This displays a copy of the Challenge screen that was shown to the cardholder:

[![](../Resources/Images/Apata/Challenge_html.png "Example of Challenge HTML Message")](../Resources/Images/Apata/Challenge_html.png)

Figure 35: Example of the Challenge HTML Screen