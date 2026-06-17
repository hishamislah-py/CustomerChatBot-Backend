## 10.6 Message Reason Codes

Reason Codes vary depending upon the transaction type (Domestic Maestro/MasterCard International), and the record type involved. The following tables describe all available values.

### 10.6.1 Domestic Maestro Reason Codes

The table below defines the Message Reason Codes (`<ReasonCode>`) for the UK Domestic Maestro.

| Record Type | Code | Meaning |
| --- | --- | --- |
| <CardFinancial> | 1400 | Not previously authorised |
| <CardFinancial> | 1401 | Previously approved authorization where the amount is the same |
| <CardFinancial> | 1402 | Previously approved authorization where the amount differs |
| <CardFinancial> | 1403 | Previously approved authorization where there is a partial amount and multi-clearing |
| <CardFinancial> | 1404 | Previously approved authorization where there is a partial amount and final clearing |
| <CardFee> | 7601 | Recovered card award fee for the collection of reward for a card acceptor, or financial institution employee when a card has been recovered |
| <CardFee> | 7604 | Emergency card replacement fee for the collection of fees associated with the Emergency Card Replacement |
| <CardFee> | 7777 | Merchant Funds Transfer for a transfer of funds between an acquirer and a merchantâs bank on behalf of a merchant |

### 10.6.2 Mastercard International Reason Codes

The table below defines the Message Reason Codes (`<ReasonCode>`) for MasterCard International.

| Record Type | Code | Meaning |
| --- | --- | --- |
| <CardFinancial> | 1400 | Not previously authorised |
| <CardFinancial> | 1401 | Previously approved authorization where the amount is the same |
| <CardFinancial> | 1402 | Previously approved authorization where the amount differs |
| <CardFinancial> | 1403 | Previously approved authorization where there is a partial amount and multi-clearing |
| <CardFinancial> | 1404 | Previously approved authorization where there is partial amount and final clearing |
| Representments/Reversals | 2000 | General or invalid chargeback |
| Representments/Reversals | 2001 | Invalid Acquirer Reference Data on chargeback; no documentation required or provided |
| Representments/Reversals | 2002 | Non receipt of required documentation to support chargeback |
| Representments/Reversals | 2003 | Correct transaction date provided |
| Representments/Reversals | 2004 | Invalid Acquirer Reference Data on chargeback; documentation was received |
| Representments/Reversals | 2005 | Correct card acceptor location/description provided |
| Representments/Reversals | 2008 | Issuer authorised  transaction |
| Representments/Reversals | 2011 | Credit previously issued |
| Representments/Reversals | 2700 | Chargeback remedied (see corresponding documentation) |
| Representments/Reversals | 2701 | Duplicate chargeback |
| Representments/Reversals | 2702 | Past chargeback time limit |
| Representments/Reversals | 2703 | Requested transaction document provided (requires hardship variance) |
| Representments/Reversals | 2704 | Invalid merchant message text |
| Representments/Reversals | 2705 | Correct MCC provided |
| Representments/Reversals | 2706 | Authorisation advised suspicious |
| Representments/Reversals | 2707 | No authorization request required nor attempted |
| Representments/Reversals | 2708 | Account was not listed on the applicable warning bulletin as of the transaction date |
| Representments/Reversals | 2709 | Documentation received was illegible |
| Representments/Reversals | 2710 | Documentation received was invalid/incomplete |
| Representments/Reversals | 2711 | Missing documentation is being supplied  Reserved for UK domestic use |
| Representments/Reversals | 2712 | Other than required/requested documentation provided  Reserved for UK domestic use |
| Representments/Reversals | 2713 | Invalid Chargeback |
| Representments/Reversals | 2870 | Chip Liability Shift  Reserved for intra-European use only |
| Chargebacks / Reversals | 4515 | Cardholder Denies |
| Chargebacks / Reversals | 4522 | Authorisation Declined |
| Chargebacks / Reversals | 4801 | Requested transaction data was not received |
| Chargebacks / Reversals | 4802 | Requested information illegible or missing |
| Chargebacks / Reversals | 4804 | Multiple Processing, Duplicate |
| Chargebacks / Reversals | 4807 | Warning bulletin |
| Chargebacks / Reversals | 4808 | Requested/required authorization not obtained |
| Chargebacks / Reversals | 4809 | Transaction Not Reconciled |
| Chargebacks / Reversals | 4812 | Account number was not on file |
| Chargebacks / Reversals | 4831 | Transaction amount differs |
| Chargebacks / Reversals | 4834 | Duplicate processing |
| Chargebacks / Reversals | 4835 | Card not valid or expired |
| Chargebacks / Reversals | 4837 | Fraudulent transaction; no cardholder authorization |
| Chargebacks / Reversals | 4840 | Fraudulent processing of transaction |
| Chargebacks / Reversals | 4841 | Canceled recurring transaction |
| Chargebacks / Reversals | 4842 | Late presentment |
| Chargebacks / Reversals | 4846 | Correct transaction currency code was not provided |
| Chargebacks / Reversals | 4847 | Fraudulent transaction; exceeds floor limit and not authorized |
| Chargebacks / Reversals | 4849 | Questionable card acceptor activity |
| Chargebacks / Reversals | 4850 | Credit posted as purchase |
| Chargebacks / Reversals | 4853 | Cardholder Dispute Defective/Not as Described |
| Chargebacks / Reversals | 4854 | Cardholder dispute not elsewhere classified (U.S. only) |
| Chargebacks / Reversals | 4855 | Non receipt of merchandise |
| Chargebacks / Reversals | 4857 | Card-activated phone transaction |
| Chargebacks / Reversals | 4859 | Services not rendered |
| Chargebacks / Reversals | 4860 | Credit not processed |
| Chargebacks / Reversals | 4862 | Counterfeit transaction; magnetic strip POI fraud |
| Chargebacks / Reversals | 4863 | Cardholder does not recognize(potential fraud)  Not valid for domestic UK transactions |
| Chargebacks / Reversals | 4870 | Chip Liability Shift  Reserved for intra-European use |
| Chargebacks / Reversals | 4900 | General and invalid second presentment. Second Presentment did not remedy First Chargeback |
| Chargebacks / Reversals | 4901 | Required documentation not received to support prior Second Presentment |
| Chargebacks / Reversals | 4902 | Documentation received was illegible |
| Chargebacks / Reversals | 4903 | Documentation received was invalid/incomplete |
| Chargebacks / Reversals | 4905 | Invalid Acquirer Reference Data in Second Presentment. Documentation was received or was not required |
| Chargebacks / Reversals | 4906 | Missing documentation is being supplied |
| Chargebacks / Reversals | 4907 | Other than required/requested documentation provided  Reserved for UK Domestic use |
| Chargebacks /  Reversals | 4908 | Invalid Acquirer Reference Data in Second Presentment, Documentation was received. |
| Chargebacks /  Reversals | 4999 | Domestic Chargeback Dispute  Reserved for intra-European use |
| <CardFee> | 7600 | Lost/stolen telex/phone fee. This is for the collection of stolen report fee and phone or telex costs incurred for taking a lost or stolen card report |
| <CardFee> | 7601 | Recovered card award fee. This is for the collection of reward for a card acceptor or financial institution employee when a card ahs been recovered |
| <CardFee> | 7602 | Emergency cash disbursement fee. This is for the collection of fees associated with the handling of emergency cash disbursements to cardholders.  Not valid for intra-European transactions |
| <CardFee> | 7603 | Compliance ruling settlement. This is for the collection of a compliance ruling settlement amount |
| <CardFee> | 7604 | Emergency card replacement fee. This is for the collection of fees associated with the Emergency Card Replacement Service (ECR) |
| <CardFee> | 7605 | Warning bulletin handling fee-issuer originated. This is for the settlement of warning bulletin handling fees in accordance with MasterCard operating rules |
| <CardFee> | 7606 | Good faith acceptance settlement. This is for settlement of the amount of a good faith acceptance |
| <CardFee> | 7607 | Collection letter handling fee. This is for settlement of the amount of a collection letter acceptance |
| <CardFee> | 7608 | Telex authorization fee. This is for collection of fees associated with an international telex authorisation |
| <CardFee> | 7610 | Investigation fee. This is for fee collection when an investigation report has been completed by an investigating member on behalf of the requesting member. |
| <CardFee> | 7611 | Retrieval fee reversal. This is for issuer-originate, and is used to reverse a retrieval request fulfillment fee for documents never received or invalid documents.  Note: An issuer would use this code in response to receiving an invalid message from an acquirer containing code 7614, |
| <CardFee> | 7612 | Retrieval handling fee; issuer-originated. This is used to penalize an acquirer for incorrect information verified by the retrieval request document. |
| <CardFee> | 7614 | Non-MasterCom fulfillment fee settlement. This is for settlement of retrieval request fulfillment not processed through the MasterCom system |
| <CardFee> | 7616 | Warning bulletin handling fee (acquirer originated). This is for settlement of warning bulletin handling fees in accordance with MasterCard operating rules.  OR  Handling fee for second presentment of reason codes 4812 and 4835 for chip transactions where transaction certificate and DE 55 are present in the clearing message. Acquirer originated. |
| <CardFee> | 7617 | Adjustment for promotional transactions |
| <CardFee> | 7618 | Reversal of previously reimbursed State Fuel Tax. Refer to the MasterCard Government Card Service Guide.  Not valid for intra-European transactions |
| <CardFee> | 7619 | Emergency card replacement center, cash advance lockbox fee.  Not valid for intra-European transactions |
| <CardFee> | 7621 | ATM Balance Inquiry Fee |
| <CardFee> | 7622 | Handling Fee for Authorisation Related Chargebacks (4807, 4808 and 4847). This is for issuer use in a Fee Collection (Handling Fee) message after sending First Chargeback for one of the specified authorization related chargebacks.  Not valid for intra-European transactions |
| <CardFee> | 7623 | Handling Fee for Authorisation Related Chargebacks (4807, 4808 and 4847). This is for issuer use in a Fee Collection (Handling Fee) message after sending Second Presentment, which indicates that the transaction was authorized.  Not valid for intra-European transactions |
| <CardFee> | 7624 | Handling Fee for Authorisation Related Chargebacks (4807, 4808 and 4847). This is for issuer use in a Fee Collection (Handling Fee) message after sending Arbitration Chargeback for one of the specified authorization related chargebacks.  Not valid for intra-European transactions |
| <CardFee> | 7625 | PIN management Service at ATM  For intra-European use only. |
| <CardFee> | 7626 | Authorisation reversal. This is for acquirer use to advice the issuer of an authorization that needs to be reversed |
| <CardFee> | 7627 | Failure to provide a merchant advice code in a Fee Collection (Handling Fee) message. |
| <CardFee> | 7628 | Reclaim surcharge.  This is restricted to intra-European and European transaction-related services. |
| <CardFee> | 7700 | Intracurrency agreement settlement; for settlement of amounts in accordance with an intracurrency agreement between transaction originator and transaction destination parties.  Not valid for intra-European transactions |
| <CardFee> | 7500  to  7779 | Bilateral agreement settlement. This is for settlement amounts in accordance with a bilateral agreement between transaction originator and transaction destination parties. |
| <CardFee> | 7780  to  7781 | Bilateral agreement settlement. This is for settlement amounts in accordance with a bilateral agreement between transaction originator and transaction destination parties. |
| <CardFee> | 7782  to  7789 | Bilateral agreement settlement. This is for settlement amounts in accordance with a bilateral agreement between transaction originator and transaction destination parties. |
| <CardFee> | 7790  to  7799 | Bilateral agreement settlement. This is for settlement amounts in accordance with a bilateral agreement between transaction originator and transaction destination parties. |
| <CardFee> | 7800 | MCBS member settlement; for collection or payment of such things as member assessments, processed through the MasterCard Consolidated Billing System (MCSB).  Not valid for intra-European transactions. |
| <CardFee> | 7801 | MasterCard compliance case filling fee. This is for collection of a member arbitration or compliance case filling fee. |
| <CardFee> | 7802 | Interchange compliance adjustment. This is for settlement of financial amounts related to interchange compliance. |
| <CardFee> | 7803 | Interchange compliance adjustment reversal. This is for settlement of financial amounts related to the reversal of a previous interchange compliance adjustment. |
| <CardFee> | 7804 | ATM transaction settlement; for settlement of daily ATM transaction amounts. |
| <CardFee> | 7805 | ATM intracountry switch fee settlement. This is for settlement of daily ATM transaction intracountry switch fees.  Not valid for intra-European transactions. |
| <CardFee> | 7806 | ATM Network Information Control System (NICS) switch fee settlement. This is for settlement of MDS NICS Switch fees.  Not valid for intra-European transactions |
| <CardFee> | 7807 | ATM intracountry first chargeback settlement; for settlement of daily ATM transaction intracountry first chargeback amounts.  Not valid for intra-European transactions |
| <CardFee> | 7811 | Reimbursement of State Fuel Tax. Refer to the MasterCard Government Card Services Guided.  Not valid for intra-European transactions |
| <CardFee> | 7812 | Collection of return of collateral for security arrangement.  Not valid for intra-European transactions |
| <CardFee> | 7813 | Mexico IVA fees  Not valid for intra-European transactions |
| <CardFee> | 7814 | Mexico IVA Fees  Not valid for intra-European transactions |
| <CardFee> | 7815 | Mexico IVA fees.  Not valid for intra-European transactions |
| <CardFee> | 7820 | Disaster Relief Fund  Not valid for intra-European transactions |
| <CardFee> | 7821 | MCBS Emergency Borrowing Collection.  Not valid for intra-European transactions |
| <CardFee> | 7822 | Settlement Adjustment.  Not valid for intra-European transactions |
| <CardFee> | 7823 | MDS Offline Debit Settlement  Not valid for intra-European transactions  MDS feed via Settlement Account Management system (S.A.M.) |

### 10.6.3 Visa Dispute Reason Codes

The table below lists relevant Dispute (Chargeback/reversal) reason codes received in the Visa Clearing message. Thredd maps some Visa dispute reason codes to their Mastercard equivalents. For more information on Visa Clearing message reason codes, please refer to the VisaNet Base II Message Specifications available at <https://www.visaonline.com/>.

| Record Type | Code | Meaning |
| --- | --- | --- |
| Chargebacks / Reversals | 10 | Fraud:  10.1. EMV Liability Shift Counterfeit Fraud  10.2. EMV Liability Shift Non-Counterfeit Fraud  10.3. Other Fraud: Card-Present Environment / Condition  10.4. Other Fraud: Card-absent Environment / Condition  10.5. Visa Fraud Monitoring Program |
| Chargebacks / Reversals | 11 | Authorisation:  11.1. Card Recovery Bulletin  11.2. Declined Authorisation  11.3. No Authorisation |
| Chargebacks / Reversals | 12 | Processing errors:  12.1. Late Presentment  12.2. Incorrect Transaction Code  12.3. Incorrect Currency  12.4. Incorrect Account Number  12.5. Incorrect Amount  12.6.1. Duplicate Processing  12.6.2. Paid by Other Means  12.7. Invalid Data |
| Chargebacks / Reversals | 13 | Consumer disputes:  13.1. Merchandise / Services Not Received  13.2. Cancelled Recurring Transaction  13.3. Not as Described or Defective Merchandise / Services  13.4. Counterfeit Merchandise  13.5. Misrepresentation  13.6. Credit Not Processed  13.7. Cancelled Merchandise / Services  13.8. Original Credit Transaction Not Accepted  13.9. Non-Receipt of Cash or Load Transaction Value at ATM |

The following website provides some useful descriptions on the above Visa Dispute codes: <https://chargebacks911.com/chargeback-reason-codes/visa/>