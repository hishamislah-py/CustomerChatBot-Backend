# 4.38 Trans\_Link Field

The `Trans_Link` field is a string between 0-19 digits, the length and value of which depends on the type of transaction as described in the table below.

| Transaction Description | Type | Other Criteria | Trans\_Link Content | Trans\_link Examples |
| --- | --- | --- | --- | --- |
| Dummy authorisation  (Created from unmatched First Presentment) | A | Description begins â*OFFLINE*â, MTID 1240 (Mastercard) or 5, 6 or 7 (Visa) | 19 digits:  â1â + *date* + *digit locator* + *Acquirer BIN*  Where:  â¢ â1â â is the offline transaction indicator  â¢ *date (yymmdd )* â is the 6 digit acquirer process date from the Acquirer Reference Number (ARN)  â¢ *Digit locator*â is the last 6 digits of ARN  â¢ *Acquirer BIN*â is the 6 digit acquiring BIN/ID from ARN  **Note**: Ensure it does not match other normal values. | 1230310339532446366  1230310321639446366  1230311008318483857 |
| Most normal authorisation requests and advices | A, J | MTID 0100, 0101, 0120 | 18 digits:  *date* (*yymmdd* ) + *6 digit STAN* + *6 digit Acquirer ID*  **Note**: the 0120 advice and 0100 request should have the same `trans_Link` values. | 230311604412007460 |
| Most normal authorisation reversals | D | MTID 0400, 0420 | 18 digits:  *date (YYMMDD*) + *6 digit OrigSTAN* + *6 digit Acquirer ID*  Where:  *OrigSTAN* comes from DE90.2 and contains the same STAN (DE11) as the original being reversed.  **Note**: 0400 and 0420 reversals should have same `trans_Link` values as the original authorisation request or advice. |  |
| Some declined authorisations | A | Some declined MTID 01xx with Acquirer ID present | 16 digits:  *date (YYMM)* + *6 digit STAN* + *6 digit Acquirer ID* | 2302994754416361  2302134370016901 |
| Visa 0620 TCN or TEN | J | MTID 0620 with no Acquirer ID present  (These are always `ProcessingCode` 35xxxx or 36xxxx, from Visa) | 12 digits:  *date (YYMMDD)* + *6 digit STAN* | 230225030928  230225005491 |
| Recurring Fees,  Activation Fees | P | Meets both of these criteria:  `ProcessingCode` ends with '999'  ProcessingCode indicates Recurring or Activation Fees | Fixed value of '0' | 0  0  0 |
| Fees related to Balance Transfers or Loads | P | Meets both of these criteria:  `ProcessingCode` ends with '999' (A Fee)  `ProcessingCode` indicates Balance Transfer Fees or Load Fees | Transaction ID of the related Balance Transfer or Load | 12659871933  12659347510 |
| First Presentments that matches a prior authorisation | P | Meets both of these criteria:  `ProcessingCode` does not end with '999' (not a Fee)  Matched to an authorisation | Set to the `trans_Link` value of the original authorisation | 230310784631401134  230309725008494605  230308638653443973 |
| First presentment with no matching auth (and not a refund) | P | Meets both of these criteria:  `ProcessingCode` does not begin with '20' and does not end with '999' (Not a Refund, not a Fee)  No matching authorisation | 19 digits:  â1â + *date* + *digit locator* + *Acquirer BIN*  Where:  â¢ â1â â is the offline transaction indicator  â¢ *date (yymmdd )* â is the 6 digit acquirer process date from the Acquirer Reference Number (ARN)  â¢ *Digit locator* â is the last 6 digits of ARN  â¢ *Acquirer BIN* â is the 6 digit acquiring BIN/ID from ARN  **Note**: ARN is the unique Acquirer Reference Number received in the clearing message. | 1230310339532446366  1230310321639446366 |
| First Presentment of a refund, with no matching auth, but a matching non-refund first presentment | P | Meets both of these criteria:  `ProcessingCode` begins with '20' (Refund)  No matching authorisation, but a matching non-refund first presentment | Set to the `trans_link` of the matching first presentment. |  |
| First Presentment of a refund, with no matching authorisation, and no matching non-refund first presentment | P | Meets both of these criteria:  `ProcessingCode` begins with '20' (Refund)  No matching authorisation, and no matching non-refund first presentment | 18 digits:  *transaction date ("YYMMDDmssxxx")* + *last 6 digits of DE031 ARN* | 230218621277522576  230218621287522584  230218621297522592 |
| Chargeback | H, C |  | Set to the `trans_Link` value of the matching Presentment. | 221023402304009260  1230108385918520914 |
| Financial Reversal (received in clearing file), and matches a previous financial | E | Matching financial found | Set to the `trans_Link` value of the matching Presentment. | 1230310299729410157 |
| Financial Reversal (received in clearing file), but no matching financial found | E | No matching financial found | 18 digits: *YYMMDDmssxxx* + *last 6 digits of ARN*. | 230311243300809653 |
| Second Presentment, matching a chargeback | N | Matching chargeback found | Set to the `trans_Link` value of the matching chargeback. | 221023402304009260  1230108385918520914 |
| Second Presentment, but related chargeback not found | N | No matching chargeback found | 18 digits: *YYMMDDmssxxx* + *last 6 digits of ARN*. | 230307223653154848  230303431430593766 |
| Balance Adjustment (debit) | B | `ProcessingCode`='190000' | Transaction ID value of this transaction. | 12613916745 |
| Balance Update from EHI response, net debit | B | `ProcessingCode` begins with '60' | Transaction ID value of the related transaction that caused this Balance Adjustment.  (Due to new Balance Update information being sent back in an EHI response message to an online authorisation.) | 12613979001 |
| Balance Update from Web Service call, net debit | B | `ProcessingCode` begins with '61' | Set to empty string. | *Empty string* |
| Balance Update from EHI response, net credit | B | `ProcessingCode` begins with '65' | Transaction ID value of the related transaction that caused this Balance Adjustment.  (Due to new Balance Update information being sent back in an EHI response message to an online authorisation.) | 12613917117 |
| Balance Update from Web Service call, net credit | B | `ProcessingCode` begins with '66' | Set to empty string. | *Empty string* |
| Payment Transaction | G |  | Transaction ID value of this transaction. | 12613921478  12668419405 |
| Load, relating to a prior Unload | L | Relates to a prior Unload | Transaction ID value of the related unload. | 12639991950  12668158805 |
| Load (not related to an Unload) | L | Unrelated to a prior Unload | Transaction ID value of this transaction. | 12613916737 |
| Unload, relating to a prior Load | U | Relates to a prior Load | Transaction ID of the related load. | 12672545523 |
| Unload (not related to an Load) | U | Unrelated to a prior Load | Transaction ID value of this transaction. | 12613916878 |

## Matching the Trans\_Link to a Previous Transaction

Refer to the table below for a summary of how to match the `Trans_Link` value in the current transaction to the value in a previous transaction.

| Current Transaction Type | How it matches to a previous transaction |
| --- | --- |
| Authorisation Advices (TxnType âJ') and Authorisation Reversals (TxnType 'Dâ | Has the same value as the original Authorisation Request it relates to (if any). |
| Presentments (TxnType 'P') | Has the same value as the original Authorisation Request or Advice it relates to. |
| Chargebacks (TxnType âC' or âHâ) | Has the same value as original Presentment (TxnType âPâ or 'Nâ). |
| Balance Adjustments (TxnType 'B') | Has the same value as the related transaction. |
| For Loads (TxnType 'L') | Has the same value as the prior related Unload. |
| Unloads (TxnType 'U') | Has the same value as the prior related Load. |