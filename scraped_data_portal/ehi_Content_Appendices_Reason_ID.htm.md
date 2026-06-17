# 4.27 Reason\_ID

The `Reason_ID` field contains a code to indicate the reason behind this message.

This field is used to describe the reason for a chargeback, but may be used to explain the reason behind other messages. See also the `Message_Why` field.

## 4.27.1 Reason\_ID Usage

The usage varies per type of message, as follows:

| MTID | Txn\_Type | Description | Reason\_ID meaning |
| --- | --- | --- | --- |
| 0100  0120  0400  0420 | A, D, J  D, J  D  D | If message comes from Visa then:  Visaâs Message Reason Code  (otherwise blank) | Visaâs Reason for the message. See below. |
| 1240 | C | Chargeback Notification | Reason for the chargeback. See below. |
| 1240 | H | Chargeback Notification (Non-Credit) | Reason for the chargeback. See below. |
| (all other combinations) |  | (all other transactions) | Not defined. Will be blank. |

## 4.27.2 Reason\_ID for a Chargeback (Txn\_Type C and H)

In Chargeback message types, the `Reason_ID` field is the reason for the chargeback.

The code is specific to the payment network the chargeback relates to, as networks define the valid chargeback reasons, and may change them.  The table below list the reason\_ID codes. For more information on the code, refer to the following Visa/Mastercard chargeback documentation:

Mastercard codes are defined in the Mastercard GCMS IPM clearing formats manual, Field 25 (Message Reason Code), as applicable for chargeback messages.

Visa codes are defined in the BASE2 file TC33 âBase2 Dispute Financial Status Adviceâ TCR1 record position 74-75 âDispute Financial Reason Codeâ.  Since Thredd expects all customers to initiate Visa Chargebacks on the VROL system, only VROL-related chargeback reasons are listed below.  See also the `Dispute_Condition` code.

| Reason\_ID | Mastercard network meaning  (Chargeback Message Reason Code) | Visa network meaning  (Dispute Financial Reason Code) |
| --- | --- | --- |
| 10 | - | Fraud |
| 11 | - | Authorisation |
| 12 | - | Processing Error |
| 13 | - | Consumer Dispute |
| 4515 | Cardholder Denies Transaction Finalised |  |
| 4804 | Multiple Processing, Duplicate |  |
| 4807 | Warning Bulletin |  |
| 4808 | Requested/Required Authorisation not obtained |  |
| 4809 | Transaction not reconcilied |  |
| 4811 | Stale Transaction |  |
| 4812 | Account Number not on file |  |
| 4831 | Transaction Amount Differs |  |
| 4834 | Duplicate Processing |  |
| 4837 | Fraudulent Transaction, no cardholder authorisation |  |
| 4840 | Fraudulent Processing of Transaction |  |
| 4841 | Cancelled Recurring Transaction |  |
| 4842 | Late Presentment |  |
| 4846 | Correct Transaction Currency Not Provided |  |
| 4849 | Questionable Card Acceptor Activity |  |
| 4850 | Installment Transaction Dispute |  |
| 4853 | Cardholder Dispute Defective/Not as described |  |
| 4854 | Cardholder Dispute (not elsewhere classified) â USA only |  |
| 4855 | Non-receipt of merchandise |  |
| 4859 | Services not rendered |  |
| 4860 | Credit not processed |  |
| 4863 | Cardholder does not recognize â Potential Fraud |  |
| 4870 | Chip Liability Shift |  |
| 4871 | Chip/PIN Liability Shift |  |
| 4880 | Maestro Late Presentment |  |
| 4890 | Syntax Error Return |  |
| 4900 | Invalid Second Presentment (Generic) |  |
| 4901 | Required documentation not received to support second presentment |  |
| 4902 | Documentation received was illegible |  |
| 4903 | Scanning error â unrelated documents or partial scan |  |
| 4905 | Invalid Acquirer Reference Number in Second Presentment, no documentation required or provided |  |
| 4908 | Invalid Acquirer Reference Number in Second Presentment, documentation received |  |
| 4999 | Domestic Chargeback Dispute |  |

## 4.27.3 Reason\_ID for an Authorisation (Txn\_Type A, D, J)

In authorisation-related messages (`Txn_Types`: A, D or J) if Thredd receives the transaction from Visa, then the Visa Message Reason code is included, if available.

Thredd maps important Visa Message Reasons to the Thredd field `Message_Why`. This field is provided for additional information. Thredd does not recommend you process this, but you can store for information if desired.

| Reason Code | Used for | Description |
| --- | --- | --- |
| 2104 | Acquirer generated 0120 (USA only) | Acquirer Advice. No 0100 was sent |
| 2501 | Reversal messages | Transaction voided by customer |
| 2502 | Reversal messages | Transaction not completed |
| 2503 | Reversal messages | No confirmation from Point of Sale (POS) terminal |
| 2504 | Reversal messages | Partial dispense by ATM or POS partial reversal |
| 3700 | Payment token related messages | Token create |
| 3701 | Payment token related messages | Token deactivate |
| 3702 | Payment token related messages | Token suspend |
| 3703 | Payment token related messages | Token resume |
| 3711 | Payment token related messages | Device provisioning result |
| 3712 | Payment token related messages | One Time Password (OTP) verification result |
| 3713 | Payment token related messages | Call Centre activation |
| 3714 | Payment token related messages | Mobile Banking App activation |
| 3715 | Payment token related messages | Replenishment confirmation of limited-use keys |
| 3716 | Payment token related messages | Token expiry update |
| 3717 | Payment token related messages | 3DS browser activation |
| 3720 | Payment token related messages | PAN expiry update |
| 3721 | Payment token related messages | PAN update |
| 3730 | Payment token related messages | Device provisioning update results |
| 3740 | Payment token related messages | Device binding |
| 3741 | Payment token related messages | Device binding results |
| 3742 | Payment token related messages | One Time Password (OTP) verification results â device binding |
| 3743 | Payment token related messages | Call centre step up â device binding |
| 3744 | Payment token related messages | Mobile banking app step up â device binding |
| 3745 | Payment token related messages | Device binding removed |
| 3748 | Payment token related messages | 3DS browser setup - device binding |
| 3749 | Payment token related messages | Device binding with FIDO intent. |
| 3751 | Payment token related messages | Cardholder verification results |
| 3752 | Payment token related messages | OTP verification result - cardholder verification |
| 3753 | Payment token related messages | Call center step up - cardholder verification |
| 3754 | Payment token related messages | Mobile banking app step up - cardholder verification |
| 3755 | Payment token related messages | 3DS browser setup - cardholder verification |
| 3760 | Payment token related messages | Device binding Green Flow |
| 3900 | Merchant initiated transactions | Incremental authorization |
| 3901 | Merchant initiated transactions | Resubmission |
| 3902 | Merchant initiated transactions | Delayed charges |
| 3903 | Merchant initiated transactions | Reauthorization |
| 3904 | Merchant initiated transactions | No show |
| 5206 | Deferred authorisation | Deferred Authorisation |
| 5400 | Fee collection/funds disbursement transactions | Preauthorisation |
| 5401 | Fee collection/funds disbursement transactions | Purchase |
| 5402 | Fee collection/funds disbursement transactions | [Original Credit Transaction (OCT)Closed Card Scheme transaction to credit funds to a card account. It can be used to send or "push" funds to an eligible card account, resulting in a real-time credit of funds to the cardholder's account.](#) |
| 5403 | Fee collection/funds disbursement transactions | [Account Funding Transaction (AFT)Closed Card Scheme transaction to debit funds from a card account. It is used to "pull" funds from a card account in order to fund a real-time "push" OCT to a different account, which can be either the cardholder's or another person's account.](#) |
| 5404 | Fee collection/funds disbursement transactions | Bill Pay |
| 5405 | Fee collection/funds disbursement transactions | Preauthorisation Completion |
| 5406 | Fee collection/funds disbursement transactions | Reversal |
| 5407 | Fee collection/funds disbursement transactions | Chargeback |
| 5408 | Fee collection/funds disbursement transactions | Representment |
| 5409 | Fee collection/funds disbursement transactions | Adjustment |
| Any other value | Unknown | Unknown.  Visa may add extra codes at any time. |