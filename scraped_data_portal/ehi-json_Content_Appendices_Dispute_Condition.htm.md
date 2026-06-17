# 4.10 Dispute Condition

The `Dispute_Condition` field contains a code to indicate additional information to the `Reason_ID` field.

Describes the Dispute Condition for a Visa chargeback; may be used as additional information to describe chargebacks and/or representments.

The usage varies per type of message, as follows:

| MTID | Txn\_Type | Description | Details |
| --- | --- | --- | --- |
| 1240 | C | Chargeback Notification | For Visa cards: Dispute Reason for the chargeback (in addition to Reason\_ID field.) See below.  For Other cards: not defined. Will be blank. |
| 1240 | H | Chargeback Notification (Non-Credit) | For Visa cards: Dispute Reason for the chargeback (in addition to Reason\_ID field.) See below.  For Other cards: not defined. Will be blank. |
| (all other combinations) |  | (all other transactions) | Not defined. Will be blank. |

## 4.10.1 Visa Dispute\_Condition for Chargeback (Txn\_Type C and H)

In Visa network chargeback message types, the `Dispute_Condition` field provides additional information on the reason for the chargeback (in addition to details in the `Reason_ID` field). For more information, refer to the *Visa chargeback documentation*.

Visa codes are defined in the BASE2 file TC33 â*Base2 Dispute Financial Status Advice*â TCR1 record position 9-11 â*Dispute Condition*â.  This is specific to Visa chargebacks initiated on the [VROL system![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.](#). The meaning varies depending on the value of the `Reason_ID` field.

Visa do not explicitly define the codes in the BASE2 document; the table below provides the Thredd interpretaion for guidance only.

### Table of Thredd Interpretation of the VISA Codes

| Visa Reason\_ID | Visa Dispute\_Condition | Threddâs interpretation as to the Visa meaning |
| --- | --- | --- |
| 10 (Fraud) | 1 | EMV liability shift Counterfeit fraud |
| 10 (Fraud) | 2 | EMV liability shift non-counterfeit fraud |
| 10 (Fraud) | 3 | Other Fraud (Card Present Environment) |
| 10 (Fraud) | 4 | Other Fraud (Card Absent Environment) |
| 10 (Fraud) | 5 | Visa Fraud Monitoring Program |
| 10 (Fraud) | (other) | Refer to Visa |
| 11 (Authorisation) | 1 | Card Recovery Bulletin |
| 11 (Authorisation) | 2 | Declined Authorisation |
| 11 (Authorisation) | 3 | No Authorisation |
| 11 (Authorisation) | (other) | Refer to Visa |
| 12 (Processing Error) | 1 | Late Presentment |
| 12 (Processing Error) | 2 | Incorrect Transaction Code |
| 12 (Processing Error) | 3 | Incorrect Currency |
| 12 (Processing Error) | 4 | Incorrect Account Number |
| 12 (Processing Error) | 5 | Incorrect Amount |
| 12 (Processing Error) | 6 | Duplicate Processing / Paid by Other Means |
| 12 (Processing Error) | 6.1 | Not sure. Probably one of âDuplicate Processingâ, or âPaid by Other Meansâ |
| 12 (Processing Error) | 6.2 | Not sure. Probably one of âDuplicate Processingâ, or âPaid by Other Meansâ |
| 12 (Processing Error) | 7 | Invalid Data |
| 12 (Processing Error) | (other) | Refer to Visa |
| 13 (Consumer Dispute) | 1 | Merchandise/Services not as received |
| 13 (Consumer Dispute) | 2 | Cancelled Recurring |
| 13 (Consumer Dispute) | 3 | Not as Described or Defective Merchandise/services |
| 13 (Consumer Dispute) | 4 | Counterfeit Merchandise |
| 13 (Consumer Dispute) | 5 | Misrepresentation |
| 13 (Consumer Dispute) | 6 | Credit not processed |
| 13 (Consumer Dispute) | 7 | Cancelled Merchandise/services |
| 13 (Consumer Dispute) | 8 | Original Credit Transaction Not Accepted |
| 13 (Consumer Dispute) | 9 | Non-receipt of Cash or Load Transaction Value |
| 13 (Consumer Dispute) | (other) | Refer to Visa |