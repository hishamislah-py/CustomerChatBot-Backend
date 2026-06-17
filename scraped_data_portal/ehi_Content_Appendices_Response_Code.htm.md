# 4.28 Response Status Values

The table below lists the response status codes that you can return in a response to a payment authorisation request through EHI. See [Get Transaction Message field: Responsestatus](../Requirements/GetTransaction_Message.htm#Responsestatus).

For details of `<Resp_Code_DE39>` response codes that the Card Scheme (Network) sends to Thredd, see [Response\_Code\_DE39 Values](Resp_Code_DE39_Codes.htm). For card status codes, see [Card Status Codes.](Card_Status_Codes.htm)

| Response Code | Description | Action |
| --- | --- | --- |
| 00 | All good. | Approve |
| 01 | Refer to card issuer.  **Note**: Not permitted for Visa transactions. | Refer |
| 03 | Invalid merchant. | Decline |
| 05 | Do not honour. | Decline |
| 0A | Approval with Load. | Approve |
| 5C | Transaction not supported or blocked by issuer.  **Note**: For Visa transactions only. | Decline |
| 9G | Blocked by cardholder, contact cardholder.  **Note**: For Visa transactions only. | Decline |
| 10 | Partial approval.  This is permitted only if `GPS_POS_Capability` position 1 (partial approval supported) is â1â (POS supports partial approval) | Approve |
| 12 | Invalid transaction.  May also be used when Integrated Circuit Card (ICC) Card Verification Value (iCVV) or Card Authentication Method (CAM) authorization request cryptogram (ARQC) validation was not successful.  **Note**: For Visa transactions only. | Decline |
| 13 | Invalid amount | Decline |
| 14 | Invalid card number (no such number) | Decline |
| 15 | No such issuer.  **Note**: For Visa transactions only. | Decline |
| 33 | Expired card (Capture). | Decline and *Pickup* card |
| 41 | Lost card (Capture). | Decline and *Pickup* card |
| 43 | Stolen card (Capture). | Decline and *Pickup* card |
| 46 | Account closed and no further authorisation requests will be approved. | Decline |
| 51 | Insufficient funds. | Decline |
| 54 | Expired card. | Decline |
| 55 | Incorrect PIN. | Decline |
| 57 | Transaction not permitted to cardholder.  May be used if the decline condition applies to all primary account numbers (PANs) for the same product. It cannot be used for individual PANs to generically decline a transaction.  **Note**: For Visa transactions only. | Decline |
| 58 | Transaction not permitted to terminal. | Decline |
| 59 | Suspected fraud. | Decline |
| 61 | Exceeds withdrawal amount limit. | Decline |
| 62 | Restricted card (e.g. card invalid in region or country). | Decline |
| 63 | Security violation. | Decline |
| 65 | Exceeds withdrawal frequency limit. | Decline |
| 6P | Verification Data Failed. Applies to cardholder, card, and other verification data. Includes both:  â¢ Provided verification data is invalid  â¢ Required verification data is missing  **Note**: if a more specific code exists (e.g. â55â if PIN incorrect), then use that. | Decline |
| 70 | Cardholder to contact issuer.  **Note**: only for Mastercard transactions. | Decline |
| 72 | Account not yet activated.  **Note**: only for Mastercard transactions. | Decline |
| 75 | Allowable number of PIN tries exceeded. | Decline |
| 78 | Card is not active (including created but not yet activated). | Decline |
| 91 | Issuer or switch is inoperative.  â¢ Gateway and Cooperative Processing (modes 1 or 2) â Thredd will decline  â¢ Gateway Processing with STIP (mode 4) â Thredd to stand-in  If your systems are unavailable, then use â05â decline if you do not want to invoke STIP.  **Note**: Gateway and Cooperative Processing (modes 1 or 2), for Mastercard: using this code will invoke STIP at the Mastercard, which may approve the transaction (depending on your STIP setup at Mastercard.) | Decline or Invoke STIP (at Thredd or Network) |
| 92 | Unable to Route Transaction (to Issuer or EHI).  â¢ Gateway Processing (modes 1 or 2) â Thredd will decline  â¢ Gateway Processing with STIP (mode 4) â Thredd to stand-in  If your systems have a fatal error, then use â05â decline if you to not want to invoke STIP.  If this received in advices, it can indicate that Thredd failed to connect to EHI.  Gateway and Cooperative Processing (modes 1 or 2), for Mastercard: using this code will invoke STIP at Mastercard, which may approve the transaction (depending on your STIP setup at Mastercard.) | Decline or Invoke STIP (at Thredd or Network) |
| 93 | Violation of law. (Transaction is illegal or against regulations in this jurisdiction.)  **Note**: Visa use only. For Mastercard Thredd suggest using value 57 instead. | Decline |
| 96 | System malfunction.  â¢ Gateway or Cooperative Processing (modes 1 or 2) â Thredd will decline  â¢ Gateway Processing with STIP (mode 4) â Thredd to stand-in  If your systems have a fatal error, then use â05â decline if you to not want to invoke STIP.  **Note**: Gateway or Cooperative Processing (modes 1 or 2): using this code will invoke Card Scheme STIP at Mastercard or Visa, which may approve the transaction (depending on your STIP setup). | Decline or Invoke STIP (at Thredd or Network) |
| C0 | [Strong Customer Authentication (SCA)Closed When the cardholder is authenticated during a payment transaction using a combination of at least two of the following authentication methods: Knowledge (Something the cardholder knows, such as a password), Possession (Something the cardholder has access to, such as a phone number or email account) and Biometrics (such as a fingerprint, face or voice) Under the Payment Service Directive 2 (PSD2), strong customer authentication is required on all cardholder-initiated transactions when both the card issuer and acquirer are within the European Economic Area (EEA).](#) required, card form factor. | Decline (reattempt with SCA) |
| C1 | SCA required, non-card form factor. | Decline (reattempt with SCA) |
| N7 | Decline for CVV2 failure. | Decline |
| R0 | Merchant level one-time stop payment to be used for VSPS-eligible (Visa Stop Payment Service) transactions (recurring, instalment, and credential-on-file). | Stop this payment. |
| R1 | Used when a cardholder requests to stop all VSPS-eligible (Visa Stop Payment Service) transactions (recurring, instalment, and credential-on-file) payments against a single merchant.  This is a Category 1 response code, meaning the issuer will never approve the transaction and further attempts are not permitted. | Stop all future payments for a single merchant. |
| R3 | Used when a cardholder requests to stop all VSPS-eligible (Visa Stop Payment Service) payments (recurring, instalment, and credential-on-file) against all merchants.  This is a Category 1 response code, meaning the issuer will never approve the transaction and further attempts are not permitted. | Stop all future payments for all merchants. |
| Z5 | Valid account but verification amount not verified correctly.  This is an account verification response that relates to an expected amount. Visa only. | Decline |
| (any code not in the above list) | Invalid response. | If 0110 response, then Thredd will invoke STIP in EHI mode 4, otherwise will decline (05). |

##### Notes:

* Response code â01â is not permitted for Visa Transactions.  If â01â is sent, then Visa will discard the authorisation response and instead invoke STIP.
* Response codes 12 and 15 are Visa-only codes effective from 12 April 2025.
* Response Code 57 (Transaction not permitted to cardholder) cannot be used for individual PANs to generically decline a transaction. It can still be used if the decline condition applies to all PANs for the same product. This change is effective from 18 October 2025.
* Response codes 04, 07, 14, 41, 43, and 46 are only used for listing permanently closed or invalid accounts.
* If an Issuer uses the 12, 15 or 57 response codes incorrectly, then Visa will convert the response and send it to the Acquirer as a generic response code decline.