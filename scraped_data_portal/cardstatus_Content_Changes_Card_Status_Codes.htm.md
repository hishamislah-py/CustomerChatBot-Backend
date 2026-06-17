# 2 Card Status Codes

This section describes Thredd card status codes available for use.

## 2.1 Card Status Codes (for Thredd API and Thredd Portal)

The following new card status codes are available for use when changing the status of a card to blocked, using Thredd Portal, Smart Client, or Thredd API (SOAP Web Services or REST-based Cards API).

| Code | Description | Merchant told to | Credits & refunds ? |
| --- | --- | --- | --- |
| G1 | A short-term[1  Use when you want merchants to try again.  Visa guidelines instruct merchants to attempt up to 15 retries over 30 days. (If you expect the block to last longer than this, long-term may be more appropriate.)](#) block[2  A card block will block all non-credit, Balance enquiry and tokenisation transactions. Refunds and Credits will be permitted.](#) which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. | Try again | Permitted |
| G2 | Short-term full block (all transactions are blocked). | Try again | Blocked |
| G3 | Long-term[3  Use when you donât want merchants to try again.  Visa expect that the card should not return to the '00 Approve' state at all, or at least not within 30 days.](#) block (excluding Credits and Refunds). | Do not try again | Permitted |
| G4 | Long-term full block (all transactions are blocked). | Do not try again | Blocked |

## 2.2 Card Status Codes (for Fraud Transaction Monitoring, IVR and Thredd Protect,)

The following Card Status Codes are available for use when changing the status of a card to blocked, using Fraud Transaction Monitoring, the IVR (automated Voice Recognition) Lost/Stolen card service and Thredd Protect (legacy fraud management product).

These codes are not enabled by default. To enable them on Thredd Protect, please contact Thredd Support.

| Code | Description | Merchant told to | Credits and refunds? |
| --- | --- | --- | --- |
| G5 | Fraud Transaction Monitoring/Thredd Protect: Short-term block (excluding Credits and Refunds). | Try again | Permitted |
| G6 | Fraud Transaction Monitoring/Thredd Protect: Short-term full block. | Try again | Blocked |
| G7 | Thredd Protect: Long-term block (excluding Credits and Refunds). | Do not try again | Permitted |
| G8 | Thredd Protect: Long-term full block. | Do not try again | Blocked |
| G9 | IVR Lost/Stolen block. Non-reversable status, equivalent to [status code 41](#41). | Do not try again | Not permitted (41 Lost response) |

## 2.3 Permanent Card Status Codes

Thredd card status values of '41' (Lost Card), â46â (Account Closed), â83â (Card Destroyed) and â98â (Refund given to customer) are considered permanent status values. If the card status is one of these, you should never respond to an authorisation request with an â00â (Approve)[4  The schemes may impose fines if you approve a transaction on a card that has a permanent blocked status.](#).

If you want to use non-permanent blocks, Thredd recommend you use one of the four temporary block card status codes (G1, G2, G3, G4), to make it clear that the account is temporarily blocked.  (A temporary block can always be changed to a full block, but not the other way round.)

For details, see [Full List of Thredd Card Status Codes](EHI_Response_Codes.htm#_GPS_Card_Status).

## 2.4 Full List of Thredd Card Status Codes

Below is a list of the possible card status codes. Also shown are the Visa and Mastercard response codes that will be sent for both a normal authorisation (auth) and for refund authorisation transactions. Codes âG1â to âG9â inclusive are new. For details of categories, see [Decline Response Code Categories](EHI_Response_Codes.htm#_Decline_Response_Code).

| Thredd Code | Description | Merchant told to | Mastercard Auth Response | Mastercard Refund Response | Visa Auth Response | Visa Refund Response |
| --- | --- | --- | --- | --- | --- | --- |
| 00 | Approve | n/a | 00 Approve | 00 Approve | 00 Approve | 00 Approve |
| 02 | Card not yet activated | Try again (02) | 72 Not yet activated | 02 Card not yet activated | 78 Card not activated yet | 78 Card not activated yet |
| 04 | Capture Card | Do not try again (03) | 04 Capture | 04 Capture | 04 Capture | 04 Capture |
| 05 | Do not honour | Try again (02) | 62 Restricted card | 62 Restricted card | 62 Restricted card | 62 Restricted card |
| 41 | Lost Card | Do not try again (03) | 41 Lost | 41 Lost | 41 Lost | 46 Closed account |
| 43 | Stolen Card | Do not try again (03) | 43 Stolen | 43 Stolen | 43 Stolen | 59 Suspected Fraud |
| 46 | Closed Account | Do not try again (03) | 46 Account closed | 46 Account closed | 46 Account closed | 46 Account Closed  (permanent) |
| 54 | Expired Card | Updated info required (01) | 54 expired | 54 expired | 54 expired | 54 expired |
| 59 | Suspected Fraud | Do not try again (03) | 63 Security violation  (if ATM: 57 Transaction not permitted to cardholder) | 63 Security violation | 59 Suspected fraud | 59 Suspected fraud |
| 62 | Restricted Card | Try again (02) | 62 Restricted | 62 Restricted card | 62 Restricted | 62 Restricted |
| 63 | Security Violation | Updated/additional info required (01) | 63 Security violation  (if ATM: 57 Transaction not permitted to cardholder) | 63 Security violation | 59 Suspected fraud | 59 Suspected fraud |
| 70 | Cardholder to contact Issuer | Try again (02) | 70 Cardholder contact issuer | 70 Cardholder contact issuer | 5C Transaction not supported/ blocked by issuer  (Visa do not support âcardholder contact issuerâ) | 5C Transaction not supported/blocked by issuer |
| 75 | Allowable number of PIN tries exceeded | Try again (02) | 75 Allowable number of PIN tries exceeded | 75 Allowable number of PIN tries exceeded | 75 Allowable number of PIN tries exceeded | 00 Approve |
| 83 | Card Destroyed | Do not try again (03) | 46 Account Closed | 46 Account Closed | 46 Account Closed | 46 Account Closed  (permanent) |
| 98 | Refund given to Customer | Do not try again (03) | 57 Transaction not permitted to cardholder | 58 Transaction not permitted to acquirer/ terminal. | 46 Account Closed | 46 Account Closed  (permanent) |
| 99 | Card Voided | Do not try again (03) | 57 Transaction not permitted to cardholder | 58 Transaction not permitted to acquirer/ terminal. | 46 Closed account | 46 Closed account |
| G1 (new) | Short-term debit block | Try again (02) | 62 Restricted card | 00 Approve | 78 Card not activated yet | 00 Approve |
| G2 (new) | Short-term full block | Try again (02) | 62 Restricted card | 62 Restricted card | 78 Card not activated yet | 78 Card not activated yet |
| G3 (new) | Long-term debit block | Do not try again (03) | 57 Transaction not permitted to cardholder | 00 Approve | 78 Card not activated yet | 00 Approve |
| G4 (new) | Long-term full block | Do not try again (03) | 57 Transaction not permitted to cardholder | 58 Transaction not permitted to acquirer/ terminal. | 78 Card not activated yet | 78 Card not activated yet |
| G5 (new) | Fraud Transaction Monitoring/Thredd Protect:Short-term debit block | Try again (02) | 62 Restricted card | 00 Approve | 78 Card not activated yet | 00 Approve |
| G6 (new) | Fraud Transaction Monitoring/Thredd Protect:Short-term full block | Try again (02) | 62 Restricted card | 62 Restricted card | 78 Card not activated yet | 78 Card not activated yet |
| G7 (new) | Thredd Protect:Long-term debit block | Do not try again (03) | 57 Transaction not permitted to cardholder | 00 Approve | 78 Card not activated yet | 00 Approve |
| G8 (new) | Thredd Protect:Long-term full block | Do not try again (03) | 57 Transaction not permitted to cardholder | 58 Transaction not permitted to acquirer/ terminal. | 78 Card not activated yet | 78 Card not activated yet |
| G9 (new) | IVR Lost/Stolen blocked | Do not try again (03) | 41 (Lost) | 41 (Lost) | 41 Lost | 46 Account closed |

Card Status codes â46â (Account Closed), â83â (Card Destroyed) and â98â (Refund given to customer) are considered permanent statuses.