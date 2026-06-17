# Appendix 5: Transaction Status

A transaction in Apata will conclude with one of the following states:

| State | Description |
| --- | --- |
| Succeeded | The transaction was approved by the ACS and the result was returned to the directory server (payment scheme) successfully. A transaction in the SUCCEEDED state may have been approved frictionlessly or the cardholder completed SCA successfully. In the event that the challenge was approved frictionlessly, the exemption field will be set. See [Exemption Values](#Exemptio). |
| Failed | The cardholder failed to complete the challenge for SCA. If the state is FAILED then the reason field will be populated by one of the following:   * CHALLENGE\_ATTEMPTS\_EXCEEDED â The number of attempts that a cardholder may perform has been exceeded. For example, the cardholder entered the OTP received over SMS incorrectly 3 times (Program Manager can set the challenge attempts to a maximum of 9 times) * CHALLENGE\_RETRIES\_EXCEEDED â The number of times that a challenge can be retried has been exceeded for the cardholder. For example, the cardholder requested that the SMS be resent too many times. |
| Error | An error occurred during the processing of the transaction. If the state is ERROR then the `errorCode` field will be set. The `errorMessage` field may also be set to provide more information on the cause of the error. See [Error Codes](#Error). |
| Timeout | The cardholder failed to complete the challenge within the allotted period of time configured (as specified in the `Time to complete authentication` field; see [Completing your 3DS Product Setup Form](../3D_Secure_Apata/Client_Information.htm#Time_to_complete_authentication)). |
| Aborted | The 3DS requestor (usually a merchant) sent an authentication request (AReq), but never followed up with a challenge request (CReq) when Apata determined that a challenge was required. |
| Cancelled | The transaction was cancelled either by the cardholder or by the 3DS requestor (usually a merchant). If the state is CANCELLED then the reason field will be set:   * CANCELLED\_VIA\_CHALLENGE\_PAGE â the cardholder selected the cancel option on the challenge page displayed in their browser or app. * CANCELLED\_OUT\_OF\_BAND â the cardholder could not complete the Biometric or Out of Band authentication. * CANCELLED\_BY\_REQUESTOR â the transaction was cancelled by the 3DS requestor (typically a merchant). This can occur when an error occurs on the merchant side for example. |
| Rejected | The ACS determined that the transaction could not proceed. This may be due to the card being blocked or TRA (Transaction Risk Analysis)  determining that the transaction is too risky. Possible reason values are:   * CARD\_DISABLED â The card has been blocked in the Apata system. * LOW\_CONFIDENCE â The risk engine determined that the transaction was too risky to continue. |

## Exemption Codes

| Value | Description |
| --- | --- |
| LOW\_VALUE\_PAYMENT | For cards issued where PSD2 applies (EEA/UK) the low value payment exemption described under PSD2 was applied. This exemption can be applied if the following conditions are met:   * The value of the payment is less than â¬50. If the transaction amount is not denoted in Euro, it will be converted to Euro using live exchange rates. * The cumulative spend of all transactions for the card since the last application of SCA cannot exceed â¬100. * The number of transactions since the last application of SCA cannot exceed 5. |
| LOW\_RISK | The transaction has been determined to be low risk using transaction risk analysis (TRA) performed by either Apataâs risk engine or a customer specified risk engine. The maximum value that may be exempted using TRA is determined by the institutionâs fraud levels. |
| WHITELISTED | The cardholder previously opted to add the merchant to their Trust List of allowed merchants. This exempts future transactions for that merchant from challenges.  SCA must be performed in order to add a merchant to the Trust List. |
| RECURRING | The transaction is a fixed, recurring payment for a particular merchant and the first payment of the recurring transaction was challenged. This allows subsequent payments for the same amount and the same merchant to be exempted from SCA. |
| ACQUIRER\_EXEMPTION | The merchant has requested an exemption from SCA as they have already applied either transaction risk analysis (TRA) or performed SCA. |
| SECURE\_CORPORATE\_PAYMENT | The transaction falls under the secure corporate payment exemption as outlined by PSD2. |
| ONE\_LEG\_TRANSACTION | The transaction has been exempted under PSD2âs one-leg transaction exemption. This exemption may be used when the acquirer is outside of the EEA. |
| MERCHANT\_INITIATED | The transaction was exempted as the request was initiated by the merchant. In this case the cardholder is not present and as a result cannot perform a challenge. |

## Decline Reasons

| Reason | Description |
| --- | --- |
| Card disabled | The card has been disabled.  Not applicable to Thredd clients. |
| Card expired | The card has expired.  Not applicable to Thredd clients. |
| Card not Enrolled | The card is not enrolled in 3D Secure authentication. |
| Challenge Attempts Exceeded | The number of Challenge attempts configured for this Challenge Method has been exceeded (e.g., entering an incorrect OTP or KBA answer too many times). |
| Challenge Retries Exceeded | The number of Challenge retries configured for this Challenge Method has been exceeded (e.g., . asking for the OTP to be resent too many times). |
| Low Confidence | The risk engine determined that the transaction was too risky to continue. |
| Required Details Missing | The transaction was missing mandatory details required for authentication. |
| Risk Engine Error | There was an error on the Apata risk engine. |

## Error Codes

Refer to the table below for a list of error codes.

| State | Description |
| --- | --- |
| ds\_error | The directory server (card scheme) returned an error when the Apata Access Control Server (ACS) attempted to report the success of the transaction. |
| client\_error | The 3DS requestor (typically a merchant) experienced an error on their side and they reported the error to the ACS. |
| validation\_error | One of the 3DS messages received by the ACS was invalid according to the 3DS protocol. |
| decoupled\_not\_supported | A decoupled transaction (valid only under 3DS 2.2+) was required, but the challenge method selected for the card does not support decoupled challenges. |
| non\_payment\_not\_supported | The ACS has been configured not to support non-payment transactions, but a non-payment transaction was received. |
| card\_not\_enrolled | The card does not exist in the Apata ACS. |
| webhook\_call\_failed | The webhook call from the Apata ACS to Thredd failed. |
| sms\_send\_failed | The sending of the SMS to the cardholder failed. |
| invalid\_config | The transaction cannot be completed due to invalid or incomplete configuration of the solution. |
| internal\_server\_error | Any error not classified above. |