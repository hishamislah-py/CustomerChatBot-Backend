# 3 EHI Response Codes

This section describes Thredd response codes and the EHI `MerchantAdvice` response field.

## 3.1 Response Codes for Refund Requests

Please ensure you update your systems to restrict use to the following response codes for approving or declining a refund transaction authorisation request.

| Code | Description |
| --- | --- |
| 00 | Approve |
| 03 | Invalid Merchant |
| 12 | Invalid transaction |
| 13 | Invalid Amount |
| 14 | Invalid PAN / no such account |
| 15 | No such issuer |
| 46 | Closed Account |
| 57 | Transaction not permitted to Cardholder  Should not be used for Mastercard or Visa Refund Declines. |
| 58 | Transaction not permitted to terminal (normally used by the acquirer)  Should also be used for Refund Declines. |
| 59 | Suspected Fraud |
| 93 | Violation of Law |

If a response code for a refund request is not one of the above, Visa will consider the response invalid, and send the transaction to their Straight Through Processing (STIP) system to respond instead.

The above response codes are currently not mandatory for Mastercard refund reporting, but we recommend your systems use them.

## 3.2 Decline Response Code Categories

Visa has grouped decline response codes into four categories[1  See Section 5.1 in the VisaNet Global Technical Letter and Implementation Guide.](#). Refer to the table below for the categories and their Mastercard equivalent.

| Category | Issuer (BIN sponsor) Action | Merchant Action | Mastercard |
| --- | --- | --- | --- |
| 1. Issuer never approves | Limit use to transactions that will never be approved. | Reattempt not permitted | Do not try again (03) |
| 2. Issuer cannot approve at this time | Use most descriptive value to indicate the decline condition | Reattempt up to 15 times over 30 days | Try Again (02) |
| 3. Data quality/ revalidate payment information | Use most descriptive value to indicate the data element requiring correction | Revalidate payment information before trying again.  Reattempt up to 15 times over 30 days. | Updated info needed (01) |
| 4. Generic response code | Limit use to transactions where no descriptive value applies. | Reattempt up to 15 times over 30 days. | n/a |

Visa will impose fines if more than 5% of declined transactions are in Visa category 4 (generic response code, highlighted in yellow).

For details of Thredd EHI response codes which are considered as generic response codes, see [EHI Response Codes Values](#_EHI_Response_Code) below.

## 3.3 EHI Response Codes Values

Below are details of the current EHI response codes. Those in Visa Category 4 (generic decline) are highlighted in yellow (if more than 5% of declines are generic, then penalty fees may be imposed).

| Code | Description | Action | Visa Category | Merchant Advice |
| --- | --- | --- | --- | --- |
| 00 | All Good | Approve | Approval | n/a |
| 01 | Refer to card issuer  Note: Not permitted for Visa transactions | Refer | 4 (generic)  (sends â05â to Visa) | Try Again (02) |
| 03 | Invalid merchant | Decline | 2 (try again) | Do not try again (03) |
| 05 | Do not honour | Decline | 4 (generic) | Try Again (02) |
| 0A | Approval with Load | Approve | Approval | n/a |
| 5C | Transaction not supported or blocked by issuer.  Visa only. | Decline | 1 (do not try again) | Do not try again (03) |
| 9G | Blocked by cardholder, contact cardholder.  Visa only. | Decline | 1 (do not try again) | Do not try again (03) |
| 10 | Partial Approval | Approve | Approval | n/a |
| 12 | Invalid transaction.  Visa only.  Do not use this response code for card-not-present (CNP) declines.  May also be used when Integrated Circuit Card (ICC) Card Verification Value (iCVV) or Card Authentication Method (CAM) authorization request cryptogram (ARQC) validation was not successful. | Decline | Decline\* | Do not try again (03) |
| 13 | Invalid amount. | Decline | 4 (generic) | Updated info needed (01) |
| 14 | Invalid card number (no such number) | Decline | 1 (do not try again),  or  3 (updated info needed) | Do not try again (03) |
| 15 | No such issuer.  Visa only. | Decline | Decline\* | Do not try again (03) |
| 33 | Expired card (Capture)  (Mastercard only) | Decline & Pickup | 4 (generic)  (Thredd sends â05â to Visa) | Do not try again (03) |
| 41 | Lost card (Capture) | Decline & Pickup | 1 (do not try again) | Do not try again (03) |
| 43 | Stolen card (Capture) | Decline & Pickup | 1 (do not try again) | Do not try again (03) |
| 46 | Closed Account | Decline | 1 (do not try again) | Do not try again (03) |
| 51 | Insufficient funds | Decline | 2 (try again) | Try again (02) |
| 54 | Expired card | Decline | 3 (updated info needed) | Updated info needed (01) |
| 55 | Incorrect PIN | Decline | 3 (updated info needed) | Updated info needed (01) |
| 57 | Transaction not permitted to cardholder.  Should not be used for Mastercard or Visa Refund Declines. You should use Response Code 58 instead.  May be used for Visa if the decline condition applies to all primary account numbers (PANs) for the same product. It cannot be used for individual PANs to generically decline a transaction. | Decline | 1 (do not try again) \* | Do not try again (03) |
| 58 | Transaction not permitted to terminal (normally used by the acquirer)  Should also be used for Refund Declines. | Decline | 4 (generic) | Do not try again (03) |
| 61 | Exceeds withdrawal amount limit | Decline | 2 (try again) | Try again (02) |
| 62 | Restricted card | Decline | 2 (try again) | Try again (02) |
| 63 | Security violation | Decline | (do not use) | Updated info needed (01) |
| 65 | Exceeds withdrawal frequency limit | Decline | 2 (try again) | Updated info needed (01) |
| 6P | Verification Data Failed | Decline | 3 (updated info needed) | Updated info needed (01) |
| 70 | Cardholder to contact issuer | Decline | 4 (generic)  (sends â05â for Visa) | Try again (02) |
| 72 | Account not yet activated | Decline | Not applicable | Try again (02) |
| 75 | Allowable number of PIN tries exceeded | Decline | 2 (try again) | Try again (02) |
| 78 | Card is not active (including created but not yet activated) | Decline | 2 (try again) | Try again (02) |
| 86 | PIN Validation not possible | Decline | 2 (try again) | Try again (02) |
| 91 | Issuer or switch is inoperative  EHI modes 1 or 2 â Thredd will decline  EHI mode 4 â Thredd to stand-in  If your system(s) are unavailable, then use â05â decline if you do not want to invoke STIP.  EHI modes 1 or 2, for Mastercard: using this code will invoke STIP at Mastercard, which may approve the transaction (depending on your STIP setup at Mastercard.) | Decline or Invoke STIP (at Thredd or Network) | 2 (try again) | Try again (02) |
| 92 | Unable to Route Transaction (to Issuer or EHI)  EHI modes 1 or 2 â Thredd will decline  EHI mode 4 â Thredd to stand-in  If your system(s) have a fatal error, then use â05â decline if you do not want to invoke STIP.  **Note**: if this is received in advices, it can indicate that Thredd failed to connect to the external host.  EHI modes 1 or 2, for Mastercard: using this code will invoke STIP at Mastercard, which may approve the transaction (depending on your STIP setup at Mastercard.) | Decline or Invoke STIP (at Thredd or Network) | 2 (try again) | Try again (02) |
| 93 | Violation of Law | Decline | 2 (try again) | Do not try again (03) |
| 96 | System Malfunction  EHI modes 1 or 2 â Thredd will decline  EHI mode 4 â Thredd to stand-in  If your system(s) have a fatal error, then use â05â decline if you do not want to invoke STIP.  EHI modes 1 or 2, for Mastercard: using this code will invoke STIP at Mastercard, which may approve the transaction (depending on your STIP setup at Mastercard.) | Decline or Invoke STIP (at Thredd or Network) | 2 (try again) | Try again (02) |
| C0 | SCA Required, card form factor | Decline | 3 (updated info needed)  (sends â1Aâ to Visa and â65â to Mastercard) | Updated info needed (01) |
| C1 | SCA Required, non-card form factor | Decline | 3 (updated info needed)  (sends â70â PIN required to Visa) | Updated info needed (01) |
| N7 | Decline for CVV2 failure | Decline | 3 (updated info needed) | Updated info needed (01) |
| (Any code not listed above) | Invalid response | If 0110 response, then Thredd will invoke STIP in EHI mode 4, otherwise will decline (05). | As per Thredd response code selected | As per Thredd response code selected |

Response code 01 is not permitted for Visa Transactions.  If 01 is sent, then Visa will discard the authorisation response and instead invoke STIP.

Response codes 12 and 15 are Visa-only codes effective from 12 April 2025. Changes to Response codes 57 are effective from 18 October 2025. If an Issuer uses these codes incorrectly, then Visa will convert the response and send it to the Acquirer as a generic response code decline.

## 3.4 EHI Field MerchantAdvice

If this field is included, then it contains a Merchant Advice Code, to tell the merchant whether to re-try the transaction on a decline. See below for possible values.

| Value | Description | Examples |
| --- | --- | --- |
| 01 | Merchant needs updated or additional information. | Expired card - merchant needs to retry after obtaining the new card expiry date.  Incorrect  CVV1/CVV2 or AVS  - merchant needs corrected data to retry |
| 02 | Merchant should re-try the transaction later | Insufficient funds (more funds may be available later). Short-term temporary card block (card will be re-enabled soon). |
| 03 | Merchant should not retry again. | Stolen card or closed account. Transactions will never be approved. |

If not included, then for declines on Mastercard cards, Thredd will set the Merchant Advice automatically based on the responseStatus provided.

This field is available on EHI version 5.0.