# Appendix 7: DelegateOTPNotification Fields

Below are details of the fields in the `DelegateOTPNotification` message fields, which you receive from Thredd. For an example request and response, see [Using the Delegate SMS API](../3D_Secure_Apata/Using_Delegates_SMS_API.htm).

| Field | Description | Data type | Length | Status |
| --- | --- | --- | --- | --- |
| NotificationId | Unique identifier of the message. | String | 256 characters | Required |
| PubToken | The 9-digit Thredd public token linked to the card (must be copied from the `DelegateOTPNotification` request). | BigInt | 9 digits | Required |
| DelegateMethod | This is the method in which the program manager contacts the cardholder for approving or declining an authorisation. | String | 20 characters | Required |
| FinancialInstitutionId | The unique identifier for the financial institution. | String | 36 characters | Required |
| Language | Language setting of the card performing the transaction in [[BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)](https://en.wikipedia.org/wiki/IETF_language_tag) format, for example, en-EN (English). | String | Up to 5 characters | Optional |
| CardScheme | The card scheme (payment network) being used: *MasterCard* or *Visa*. | String | Up to 20 characters | Optional |
| Device | Details of the device of the cardholder when the transaction is initiated. | Object |  | Required |
| Channel | Device channel in which the transaction is initiated (App or Browser). | String | Up to 20 characters | Optional |
| Ip | IP address of the device used to initiate the transaction. | String | Up to 20 characters | Optional |
| Language | Language setting received from Apata of the device performing the transaction in [[BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)](https://en.wikipedia.org/wiki/IETF_language_tag) format. For example: en-EN (English). | String | Up to 5 characters | Optional |
| MerchantInfo | Provides details of the merchant requesting the authentication | Object |  | Optional |
| Id | Identifier of the merchant performing the purchase request. | String | 64 characters | Required |
| Name | The name of the merchant. | String | Up to 64 characters | Required |
| Country | Country code of the merchant. This value is in the 2-letter format (for example, US). | String | 3 characters | Optional |
| Url | The URL of the merchant's website, or the name of the merchant's app. | String | Up to 2048 characters | Required |
| ChallengePreference | The merchant's preference or requirement for challenging a transaction. For example, *challenge-requested* indicates that the merchant prefers that the transaction is challenged. | String | 100 characters | Optional |
| RedirectAppUrl | For app-based transactions only. This is the fully-qualified app URL for the merchant's app. Your authentication app uses this to redirect the cardholder back to the checkout page on the merchant app once they have been authenticated. | String | Up to 512 characters | Optional |
| TransactionInfo | Provides details of the merchant requesting the transaction. | Object |  | Optional |
| Type | Type of transaction, for example *payment* or *non-payment*. | String | Up to 20 characters | Required |
| ProtocolVersion | The version of the 3D-Secure protocol, for example, 2.2.0. For details of supported versions, see [Support for 3D Secure Versions](../3D_Secure_Apata/Additional_3D_Secure_Considerations.htm#_Support_for_3D). | String | Up to 5 characters | Required |
| Channel | The interface used for initiating the challenge. This can be an app or browser. | String | Up to 20 characters | Required |
| Token | 9-digit public token |  |  |  |
| DsTransactionId | Unique alpha-numeric transaction identifier provided by the Card Scheme's directory server. This helps to identify a transaction. | String | 36 characters | Optional |
| Date | Unix Epoch timestamp in seconds. | Int | 10 characters | Required |
| ChallengeAt | Unix Epoch timestamp in seconds of when the challenge occurred. | Int | 10 characters | Required |
| ChallengeExpiresAfter | The TTL(Time-To-Live) for the challenge. | Int | 3 characters | Required |
| ChallengeExpiry | Unix Epoch timestamp in seconds for when the challenge expires. | Int | 10 characters | Required |
| ChallengeMethod | The challenge method for authentication. For a Biometric or Out of Band session, this is *sms-otc*. | String | 20 characters | Required |
| Amount | Transaction amount in minor currency units (for example, 1000 for $10.00). | String (Numeric) | 64 characters | Required |
| Currency | Details of the currency. | Object |  | Required |
| Code | 3-digit numeric [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) currency code (e.g., EUR, USD, SGD, JPY). | String | 3 characters | Required |
| Exponent | Exponent for formatting the given ISO 4217 currency code, for example, *2*. (Most currencies have an exponent of 2, where there are two digits after the decimal point, for example: 199.99.) | String (Integer) | 1 character | Required |
| Recur | Details of recurring payments. | Object |  | Required |
| Frequency | The frequency with which the payment is repeated (in days). For example, *30* indicates that it repeats every 30 days. | String | 8 characters | Optional |
| EndRecur | The date at which the recurring payment expires in YYYY-MM-DD format. For example: *20241230* (30 December 2024). | String | 8 characters | Optional |
| Install | The number of instalments. For example, 5 indicates 5 additional payments after the first payment. | String | Up to 8 characters | Optional |
| passcode | This is the OTP (One-Time Passcode). | String | 6 characters | Required |
| Mobile number | Mobile number of the cardholder. | String | 13 characters | Required |
| MessageContent | The contents of the message containing the OTP. | String | Up to 2048 characters | Optional |

### Thredd Response

Below are details of the Thredd response to your `DelegateSCAValidation` message`:`

| Field | Description | Data type | Length | Mandatory / Optional |
| --- | --- | --- | --- | --- |
| PubToken | Thredd 9-digit Thredd public token linked to the card. | Bigint | 9 characters | Required |
| DelegateScaId | A unique identifier for each `DelegateSCANotification` request. | String | 36 characters | Required |
| PmReferenceId | Program Manager Reference ID for the Biometric/Out of Band transaction. This is defined by the Program Manager. | String | Up to 36 characters | Required |
| Status | The authentication status:   * SUCCESS â the 3DS result was received before the timeout period * TIMEOUT â the 3DS result was received after the timeout period. * ERROR - In case of any internal technical failures. * FAILURE - In case of any validation failures. | String | Up to 20 characters | Optional |
| Error |  | Object |  |  |
| ReferenceNumber | Thredd reference number for the error. Used by Thredd for referencing purposes.  Used for ERROR status only. | String | Up to 15 characters | Optional |
| Description | Short description of the error. Used by Thredd for referencing purposes.  Used for ERROR status only. | String | Up to 50 characters | Optional |

### Thredd Response

Below are details of the Thredd response to your `DelegateOTPNotification` message`:`

| Field | Description | Data type | Length | Status |
| --- | --- | --- | --- | --- |
| Response Status | The HTTP response codes to indicate whether a specific HTTP request has been successfully completed or not. | String |  | Mandatory |
| Error Message | Error message with details. | String |  | Optional |