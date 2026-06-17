# 4.41 Visa\_ResponseInfo\_DE44

The `Visa_ResponseInfo_DE44` field contains a summary of verifications performed by the Visa system on the transaction, before it reached Thredd.  It is a useful source of additional information for Visa authorisation-related transactions.

The values supplied in this field are subject to change by Visa. We advise you not to configure your systems to make decisions based on this field.

Only some of the values below apply to the Thredd to Visa connection.

## 4.41.1 Visa\_ResponseInfo\_DE44 Positions

Each position holds the result of a verification check at Visa. The Visa system may vary on which checks it performs on which transactions.

The position is the character offset in the field; the first character is *position 1*. A space character in any position indicates the information is not provided.

In the table below,  *Issuer* indicates Thredd, *STIP* indicates the Visa [Stand-In Processing![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) system and *Switch* refers to the Visa Network.

 Only a summary of the relevant values are given below. For more information, refer to the Visa documentation.

| Position | Description | More Information |
| --- | --- | --- |
| 1 | Response Source/Reason | See [Position 1 â Response Source/Reason Code](#Position). |
| 2 | AVS result | See [AVS\_Results](AVS_Results.htm). |
| 3 | Reserved for future use | See Visa documentation |
| 4 | Reserved for future use | See Visa documentation |
| 5 | CVV/iCVV/dCVV result | Values:  Space = CVV, iCVV or dCVV was not verified  0 = CVV, iCVV or dCVV could not be verified  1 = CVV, iCVV, dCVV, or Online CAM failed verification, or Offline PIN authentication was interrupted  2 = CVV, iCVV, dCVV, or Online CAM passed verification.  3 = Transaction passed CVV, Emergency Replacement Card (ERC) service value only, which is used exclusively by the Global Customer Assistance Service (GCAS). |
| 6 - 7 | PACM diversion level | See Visa documentation |
| 8 | PACM diversion reason | See Visa documentation |
| 9 | Card Authentication Results | Values:  Space = no information  1 = EMV ARQC checked and failed verification  2 = EMV ARQC checked and passed verification |
| 10 | Reserved for future use | See Visa documentation |
| 11 | CVV2 Result | See [Position 11 â CVV2 Result Code](#Position2) |
| 12-13 | Original Response code | See Visa documentation |
| 14 | Cheque settlement code (USA only) | See Visa documentation |
| 15 | CAVV result | See [Position 15 â CAVV Result Code](#Position3) |
| 16 - 19 | Response Reason Code | See Visa documentation. (Not applicable to Thredd) |
| 20 - 23 | Last 4 digits of PAN for receipt | Holds the last four digits of the cardholder PAN, for some payment-token transactions. |
| 24 | CVM requirement for PIN-less | Values:  Space = no information  0 = No CVM required  1 = Signature prompt required |
| 25 and up | Unknown | See Visa documentation |

## 4.41.2 Position 1 â Response Source/Reason Code

This position explains who responded to the acquirer and why.  Thredd already map this into the `Response_Source` and `Response_Source_Why` fields.

In the table below,  Issuer indicates Thredd, and STIP indicates the Visa [Stand-In Processing![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) sytem.

| Value | Description |
| --- | --- |
| space | No information |
| 0 | Advice of Exception file change initiated by Global Customer Assistance Service (GCAS) or Automatic Cardholder Database Update (Auto-CDB) Service |
| 1 | Response provided by STIP because the request was timed out by Switch (ATR) or the response contained invalid data |
| 2 | Response provided by STIP because the transaction amount was below issuer limit (PCAS processing), or transaction amount is below sliding dollar limit (PACM processing), or in response to a verification request |
| 4 | Response provided by STIP because issuer was not available for processing |
| 5 | Response provided by issuer |
| 7 | Reversal message matched to the original authorization request message |
| 8 | No matching original authorization request message found. V.I.P. attempts to match reversals with originals when possible; however, 8 does not guarantee that  an original was not received |
| A | Automated Fuel Dispenser Advice |
| B | Response provided by STIP: Transaction met Visa Transaction Advisor Service criteria |
| C | Response provided by STIP for conditions not listed. See the Thredd fields `Response_Source_Why` and `Visa_STIP_Reason_Code` for why (see section [Visa\_STIP\_Reason\_Code field](Visa_STIP_Reason_Code.htm#_Ref41406658)) |
| Any other value | Unknown |

## 4.41.3 Position 11 â CVV2 Result Code

Result of Visaâs CVV2 verification.

| Value | Summary |
| --- | --- |
| space | No information |
| M | CVV2/dCVV2 match verified by issuer or Visa |
| N | CVV2/dCVV2 verified but did not match |
| P | CVV2/dCVV2 not performed due to system settings or STIP |
| S | System error (e.g., missing expiry date or CVV2) |
| U | Issuer [actual issuer, not Thredd] does not participate or lacks encryption keys |
| Any other value | Unknown |

## 4.41.4 Position 15 â CAVV Result Code

Result of Visaâs CAVV (3D-secure) verification.

| Value | CAVV result |
| --- | --- |
| space | No information |
| 0 | CAVV could not be verified or CAVV data was not provided when expected |
| 1 | CAVV failed verificationâauthentication. |
| 2 | CAVV passed verificationâauthentication. |
| 3 | CAVV passed verificationâattempted authentication.  A 3D Secure (3DS) authentication value of 07 from the Issuer Attempts Server indicates that authentication was attempted.  Issuer attempts CAVV key was used to generate the CAVV. |
| 4 | CAVV failed verificationâattempted authentication.  A 3D Secure (3DS) authentication value of 07 from the Issuer Attempts Server indicates that authentication was attempted.  Issuer attempts CAVV key was used to generate the CAVV. |
| 5 | RFU |
| 6 | CAVV not verified, issuer not participating in CAVV verification (except as noted, only Visa generates this code, issuers do not). |
| 7 | CAVV failed verificationâattempted authentication.  A 3D Secure (3DS) Authentication Results Code value of 07 from Visa Attempts Service indicates that an authentication attempt was performed.  (Visa CAVV attempts key was used to generate the CAVV) |
| 8 | CAVV passed verificationâattempted authentication  A 3D Secure (3DS) Authentication Results Code value of 07 from Visa Attempts Service indicates that an authentication attempt was performed.  (Visa CAVV attempts key was used to generate the CAVV) |
| 9 | CAVV failed verificationâattempted authentication  A 3D Secure (3DS) Authentication Results Code value of 08 from Visa Attempts Service indicates that an authentication attempt was performed when the Issuer Access Control Server (ACS) was not available.  (Visa CAVV attempts key was used to generate the CAVV) |
| A | CAVV passed verificationâattempted authentication  A 3D Secure (3DS) Authentication Results Code value of 08 from Visa Attempts Service indicates that an authentication attempt was performed when the Issuer ACS was not available.  Visa CAVV attempts key was used to generate the CAVV. |
| B | CAVV passed verificationâattempted authentication, no liability shift.  Only Visa generates this code, issuers do not. |
| C | CAVV was not verifiedâattempted authentication.  If 3D Secure (3DS) Authentication Results Code value is 07 in the CAVV and the issuer did not return a CAVV results code in the authentication response, or, if, Field 44.13 = 0 in the response message and the CAVV encryption keys do not exist in V.I.P., V.I.P.. sets the value to C in Field 44.13.  Only Visa generates this code, issuers do not. |
| D | CAVV was not verifiedâcardholder authentication.  If 3D Secure (3DS) Authentication Results code value is 00 in the CAVV and the issuer did not return a CAVV results code in the authorization response, or, if, Field 44.13 = 0 in the response message and the CAVV encryption keys do not exist in V.I.P., V.I.P. sets the value to D in Field 44.13.  Only Visa generates this code, issuers do not. |
| Any other value | Unknown |