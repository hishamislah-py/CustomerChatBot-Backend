# 4.41 Visa\_STIP\_Reason\_Code

The `Visa_STIP_Reason_Code` field provides Visaâs reason codes for why an advice was generated. This information can be used to supplement the details returned in the `Message_Why` and `Response_Source_Why` fields of an advice message that originated from Visa.

The values supplied in this field are subject to change by Visa. We advise you not to configure your systems to make decisions based on this field.

Only some of the values below apply to the Thredd to Visa connection.

Definitions used below:

* Issuer - means Thredd in this scenario
* STIP â Visaâs STand-In Processing system
* Switch â the Visa Network

| Value | Action taken by Visa | Detailed reason (why action was taken) |
| --- | --- | --- |
| 9001 | STIP processed transaction | Issuer is signed off [to Visa] |
| 9002 | STIP processed transaction | Issuer was signed off by Visa |
| 9011 | STIP processed transaction | Line [from] Visa to Issuer is down |
| 9012 | STIP processed transaction | Forced STIP because of N0 (Force STIP) original response from issuer |
| 9020 | STIP processed transaction | Response from Issuer timed out |
| 9022 | STIP processed transaction | PACM (Positive Authorisation Capacity Management) - diverted |
| 9023 | STIP processed transaction | PCAS (Positive Cardholder Authorisation Service) -diverted |
| 9024 | STIP processed transaction | Transaction declined due to Visa Payment Controls (VPC) rule |
| 9025 | STIP processed transaction | Declined by Selective Acceptance Service |
| 9026 | STIP processed transaction | Transaction reviewed by the Visa Transaction Advisor Service: additional authentication required. |
| 9027 | STIP processed transaction | Declined by token provisioning service |
| 9030 | STIP processed transaction | Based on the Issuer response, the account was either listed in the ASAF via the Auto-CDB Service or updated by the ASAF Downgrade feature. |
| 9031 | STIP processed transaction | Original processed in stand-in |
| 9033 | STIP processed transaction | Declined due to active account management threshold exceeded |
| 9034 | STIP processed transaction | Unable to deliver response to Acquirer |
| 9035 | STIP processed transaction | Process recurring payment in STIP |
| 9037 | STIP processed transaction | Declined by Visa CTC (Consumer Transaction Controls) service |
| 9038 | STIP processed transaction | Merchandise return authorization processed in STIP |
| 9041 | STIP processed transaction | There was a PIN verification error |
| 9042 | STIP processed transaction | Offline PIN authentication was interrupted |
| 9045 | STIP processed transaction | Switch was unable to translate the PIN |
| 9047 | STIP processed transaction | Declined by Real-Time Decisioning (RTD) processing |
| 9048 | STIP processed transaction | There is an invalid CVV with the All Respond Option |
| 9054 | STIP processed transaction | There is an invalid CAM [EMV ARQC invalid normally] |
| 9063 | STIP processed transaction | Transaction declined, processing requirements not met. This value is set by Visa when the value in field 39 is 96 and:  â¢ Transaction required to process in-country, but the in-country Visa system is unavailable, or,  â¢ Transaction not eligible to be processed by the in-country Visa System |
| 9091 | STIP processed transaction | Dispute financial |
| 9095 | STIP processed transaction | Issuer notification of token vault provisioned or status change |
| 9050 | STIP generated advice | Source or destination does not participate in this service |
| 9061 | Switch-Detected Error | There is an internal system error or other switch-detected error condition |
| 9102 | Switch-Generated Reversal  Advice | Switch generated this 0420 reversal advice because an approval response could not be delivered to the acquirer. Visa Europe only |
| 9103 | Switch-Generated Reversal  Advice | An approval response could not be delivered to the acquirer because the issuer timed out |
| 9201 | STIP Decline Advice | Decline due to PPCS (Stop recurring payment service) |
| 9202 | STIP Decline Advice | Decline due to issuer country exclusion list |
| 9203 | STIP Decline Advice | Decline due to Office of Foreign Assets Control (OFAC) embargo |
| 9204 | STIP Decline Advice | Cashback processing error |
| 9205 | STIP Decline Advice | Invalid CAVV with Visa Verify and decline options (V and W) |
| 9206 | STIP Decline Advice | Mod-10 check failure |
| 9207 | STIP Decline Advice | Issuer does not support gambling transactions |
| 9208 | STIP Decline Advice | Declined because issuing identifier and/or routing identifier is blocked |
| 9209 | STIP Decline Advice | Declined because issuer does not support transaction type |
| 9210 | STIP Decline Advice | Declined because of issuer participation options |
| 9211 | STIP Decline Advice | Declined because acquirer does not support the service requested |
| 9212 | STIP Decline Advice | Declined due to fraud condition |
| 9213 | STIP Decline Advice | Declined because call-out to an external service timed out |
| 9214 | STIP Decline Advice | Declined because of error return from call-out to external service |
| 9215 | STIP Decline Advice | Declined because issuer blocked specific POS entry mode |
| 9218 | STIP Decline Advice | Product subtype is MB (Interoperable mobile branchless) and business application identifier is not MP or business application identifier is MP and product subtype is not MB. |
| 9219 | STIP Decline Advice | Merchant Blocking Service Decline Reason Code |
| 9302 | STIP Decline Advice | Exceeds Settlement Risk Exposure Cap. This code appears in 0120 messages |
| Any other value | Unknown | Ignore this.    **Note**: Visa may add other values at any time without prior warning, so you must ignore any values that you are not expecting. |