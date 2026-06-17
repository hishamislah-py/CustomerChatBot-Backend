# 2 Transaction Processing on Discover Networks

This section provides details of transaction message processing on Discover Networks.

## 2.1 Discover Network Message Types

Discover Network messages conform to the ISO 8583 message standard. Discover uses the ISO 8583: 1993 version. See Figure 1 below.

![](../Resources/Images/MTID_format_Discover.png "MTID Format - ISO specification showing examples for Discover")

Figure 1: ISO 8583 Message Types

Thredd maps Discover message type identifiers (MTIs) back to our standard message MTIDs. For example, we map Discover 1100 messages to the Thredd standard 0100 message format.

We support the following message types:

| Discover MTI | Mapped to Thredd MTID | Message Type | Description |
| --- | --- | --- | --- |
| 1100 | 0100 | Authorisation request | Request from the acquirer to authorise a transaction (payment or refund). A response is required to approve or decline the transaction. |
| 1110 | 0110 | Authorisation response | Response from the issuer: approve or decline the transaction. |
| 1120 | 0120 | Authorisation advice | Advice from the acquirer to notify of an authorisation. The issuer responds to acknowledge the message. |
| 1130 | 0130 | Authorisation advice response | Response from the issuer to acknowledge the message. |
| 1420 | 0420 | Authorisation reversal | Advice from the acquirer to notify of an authorisation reversal. The issuer responds to acknowledge the message. |
| 1430 | 0430 | Authorisation reversal response | Response from the issuer to acknowledge the message. |
| 06 | 1240 | Financial Notification (debit, credit, financial) | Advice from the acquirer for a financial transaction such as a presentment, financial reversal or chargeback. The notification is received in the schemeâs clearing files. The type of financial message is indicated by the `Txn_Type` field. For more information, see Transaction Types. |
| 36 | 1240 | Chargeback notification | Chargeback message. The type of chargeback message is indicated by the `Txn_Type` field. For more information, see Transaction Types. |

There are additional MTIs for Discover which Thredd are not using, and which are out of scope for Phase 1.

Program Managers must use this information to update the card balance details to reflect payments that have been made or any charges on the card.

### 2.1.1 Transaction Processing

Discover data fields are mapped to Thredd's internal data elements. Thredd performs standard message validation, card usage restrictions and card security checks. The message data is normalised to provide a uniform message format that is sent to Program Managers using the External Host Interface (EHI).

For Program managers using Full Service Processing (mode 3), Thredd performs transaction matching and balance adjustments.

#### Period for receiving a response to an authorisation requests from Thredd

Thredd will wait up to two seconds for a response to an authorisation request. If no response is received the transaction will be timed out and declined.