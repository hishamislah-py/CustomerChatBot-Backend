# Appendix 6: Biometric/OOB Fields

This section provides details of the fields used in Biometric/OOB message requests and responses.

## DelegateSCANotification and DelegateSCACancelNotification Message Fields

Below are details of the fields in the `DelegateSCANotification` and `DelegateSCACancelNotification` requests which Thredd sends to your systems. For more information, see [Initiating a Biometric Session.](../3D_Secure_Apata/Using_Biometric_API_Apata.htm#_Initiating_a_Biometric)

| Field | Description | Data type | Length | Status |
| --- | --- | --- | --- | --- |
| NotificationId | Unique identifier of the message notification. | String | 256 characters | Required |
| PubToken | Thredd 9-digit public token linked to the card. | BigInt | Up to 9 characters | Required |
| DelegateMethod | This is the method in which the program manager contacts the cardholder for approving or declining an authorisation. In this case, it is a push notification. | String | 20 characters | Required |
| FinancialInstitutionId | Unique identifier defined for the Program Manager in Apata. | String | 36 characters | Required |
| Language | Language setting of the device performing the transaction in [[BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)](https://en.wikipedia.org/wiki/IETF_language_tag) format, for example, en-EN (English). | String | Up to 5 characters | Optional |
| DelegateScaId | Unique alpha-numeric identifier for tracking the delegated authentication session. | String | 36 characters | Required |
| CardScheme | The card scheme (payment network) being used: *MasterCard* or *Visa*. | String | Up to 20 characters | Optional |
| CreatedMode | This field indicates how the token was enrolled into 3D-Secure through one of the following codes:  â **GA** Thredd auto-enrolment process.  â **PM** The Program Manager calling the Thredd Hyperion API Credential Call. | String | 2 characters | Optional |
| Device | Details of the device of the cardholder when the transaction is initiated. | Object |  | Required |
| Channel | Device channel in which the transaction is initiated (App or Browser). | String | Up to 20 characters | Optional |
| Ip | IP address of the device used to initiate the transaction. | String | Up to 20 characters | Optional |
| Language | Language setting of the device performing the transaction in [[BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)](https://en.wikipedia.org/wiki/IETF_language_tag) format, for example, en-EN (English). | String | Up to 5 characters | Optional |
| MerchantInfo | Provides details of the merchant requesting the authentication | Object |  | Optional |
| Id | Unique identifier of the merchant initiating the authentication request. This is assigned by the acquirer. | String | 64 characters | Required |
| Name | Merchant name. | String | Up to 64 characters | Required |
| Country | Country code of the merchant. This value is the 3-digit number format (e.g., 840). | String | Up to 3 characters | Optional |
| UrL | URL or name of the merchant's website or app. | String | Up to 2048 characters | Required |
| ChallengePreference | Challenge preference indicated by the merchant in the Authentication Request (AReq). | String | 100 characters | Optional |
| RedirectAppUrl | For app-based transactions only. This is the callback URL for the merchant's app. Your authentication app uses this to redirect the cardholder back to the checkout page on the merchant app once they have authenticated.[1 In the challenge flow, the merchant app, through the 3DS software development kit (SDK), interacts with the Access Control Server (ACS) and declares its URL, thus enabling the authentication app to call the merchant app after the OOB authentication has occurred.](#)  If this field is empty, your app does not need to initiate a callback to the merchant's app. | String | Up to 256 characters | Optional |
| TransactionInfo | Provides details of the transaction for which the authentication is being requested. | Object |  | Optional |
| Type | Type of transaction. For example: *payment* or *non-payment*. | String | Up to 20 characters | Required |
| ProtocolVersion | 3D Secure protocol version being used, for example, 2.2.0. For details of supported versions, see [Support for 3D Secure Versions](../3D_Secure_Apata/Additional_3D_Secure_Considerations.htm#_Support_for_3D). | String | Up to 5 characters | Required |
| Channel | The channel in which the transaction is initiated (App or Browser). | String | Up to 20 characters | Required |
| Token | 9-digit public token | String | 64 Characters | Required |
| DsTransactionId | Unique alpha-numeric transaction identifier provided by the Card Scheme's directory server. This helps to identify a transaction. | String | 36 characters | Optional |
| Date | Unix Epoch timestamp in seconds. | Int | 10 characters | Required |
| ChallengeAt | Unix Epoch timestamp in seconds of when challenge occurred. | Int | 10 characters | Required |
| ChallengeExpiresAfter | The TTL(Time-To-Live) for the challenge. | Int | 3 characters | Required |
| ChallengeExpiry | Unix Epoch timestamp in seconds for when the challenge expires. | Int | 10 characters | Required |
| ChallengeMethod | The Challenge method for authentication. For a Biometric or Out of Band session, this is a push-confirmation. | String | 20 characters | Required |
| Amount | Transaction amount in minor currency units (for example, 1000 for $10.00). | String (Numeric) | 64 characters | Required |
| Currency | Provides details of the currency. | Object |  | Required |
| Code | 3-digit numeric [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) currency code (e.g., EUR, USD, SGD, JPY). | String | 3 characters | Required |
| Exponent | Exponent for formatting the given ISO 4217 currency code. For example: *2*. (Most currencies have an exponent of 2, which gives two digits after the decimal point, for example: 199.99.) | String (Integer) | 1 character | Required |
| Recur | Provides details of a recurring payment that is set up. | Object |  | Optional |
| Frequency | The frequency with which the payment is repeated (in days). For example: *30* (repeats every 30 days). | String | 8 characters | Optional |
| EndRecur | The date at which the recurring payment expires, in YYYY-MM-DD format. For example: *20241230* (30 December 2024). | String | 8 characters | Optional |
| Install | The number of instalments. For example, 5 indicates 5 additional payments after the first payment. | String | Up to 8 characters | Optional |
| DelegateStatus | Status of the DelegateSCANotification request. This is set to either Active or Cancelled. | String | 10 characters | Required |

## DelegateSCAValidation Message Fields

Below are details of the fields in the `DelegateSCAValidation` message which you should use to notify Thredd of the result of the Biometric/OOB session. For more information, see [Notifying Thredd of the Result of the Biometric Session](../3D_Secure_Apata/Using_Biometric_API_Apata.htm#_Notifying_Thredd_of).

| Field | Description | Data type | Length | Status |
| --- | --- | --- | --- | --- |
| NotificationId | Unique identifier of the message notification. | String | 256 characters | Required |
| PubToken | The 9-digit Thredd public token linked to the card (must be copied from the `DelegateSCANotification` request). | BigInt | 9 digits | Required |
| DelegateScaId | The unique alpha-numeric identifier of the notification request (must be copied from the `DelegateSCANotification` request). | String | 36 characters | Required |
| PmReferenceId | Program Manager Reference identifier for the Biometric/Out of Band transaction. This is defined by the Program Manager. | String | Up to 36 characters | Optional |
| Status | One of the following status values must be returned:   * SUCCESS â the cardholder was successfully authenticated. * FAILURE â the cardholder could not be successfully authenticated. | String | Up to 20 Characters | Required |

### Thredd Response

Below are details of the Thredd response to your `DelegateSCAValidation` message`:`

| Field | Description | Data type | Length | Mandatory / Optional |
| --- | --- | --- | --- | --- |
| PubToken | Thredd 9-digit Thredd public token linked to the card. | Bigint | 9 characters | Required |
| DelegateScaId | A unique identifier for each `DelegateSCANotification` request. | String | 36 characters | Required |
| PmReferenceId | Reference identifier for the Biometric/Out of Band transaction. This is defined by the Program Manager. | String | Up to 36 characters | Required |
| Status | The authentication status:   * SUCCESS â the 3DS result was received before the timeout period * TIMEOUT â the 3DS result was received after the timeout period. * ERROR â In case of any internal technical failures. * FAILURE â In case of any validation failures. | String | Up to 20 characters | Optional |
| Error | Indicates the error object. | Object |  |  |
| ReferenceNumber | Thredd reference number for the error. Used by Thredd for referencing purposes.  Used for ERROR status only. | String | Up to 15 characters | Optional |
| Description | Short description of the error. Used by Thredd for referencing purposes.  Used for ERROR status only. | String | Up to 50 characters | Optional |