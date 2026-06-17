# 3.2 Transaction Message Types

The ISO 8583 standard describes the message types to be used for financial transactions. Conformity to an ISO standard helps to ensure a consistent way to present financial transaction messages, which can be adopted across the different schemes.  In general, Mastercard, Visa and Discover Card Scheme networks follow the ISO 8583 standard, but with some discrepancies and exceptions.

When acquirers send transactions through the card scheme network, they identify the message type they are sending, using a Message Type Identifier (MTI or MTID) field. The MTID field contains a four-digit number used for all card-originated transactions, and its format is defined by ISO 8583. It identifies the version number, message class, message function and transaction originator.  See the figure below.

![](../Resources/Images/Intro_card_payments/MTID_format.png)

Figure 11: MTID Format

Thredd processes messages received from the Card Scheme networks. We provide our customers with a single and consistent message format which combines fields received from the scheme with additional Thredd enhanced information.

## 3.2.1 What are the main ISO message types?

The table below summarises the main ISO message types that are sent over card payment networks.

| MTID | Message Type | Description |
| --- | --- | --- |
| 0100 | Authorisation Request | Request from the acquirer to authorise a transaction (payment or refund). A response is required to approve or decline the transaction. |
| 0101 | Authorisation Repeat (Visa Only) | Request from the acquirer for a repeat authorisation. A response is required to approve or decline the transaction. |
| 0120 | Authorisation Advice | Advice from the acquirer to notify of an authorisation. The issuer responds to acknowledge the message. |
| 0400 | Authorisation Reversal Request | Request from the acquirer to reverse a previous authorisation. A response is required to approve or decline the transaction. |
| 0420 | Authorisation Reversal Advice | Advice from the acquirer to notify of an authorisation reversal. The issuer responds to acknowledge the message. |
| 1240 (Mastercard only) | Financial Notification | Advice from the acquirer for a financial transaction such as a presentment, financial reversal or chargeback. The notification is received in the schemeâs clearing files.  Issuers must use this information to update the card balance details to reflect payments that have been made or any charges on the card.    **Note**: Visa clearing messages are not ISO-standard compliant and therefore do not use MTIDs. |

\* A Request is a message type that requires an online authorisation response (approve or decline). An Advice is a message type that is sent for information purposes and which does not require an online authorisation response.