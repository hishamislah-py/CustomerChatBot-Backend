# Appendix 6: DelegatedOTPNotification Fields

Below are details of the fields in the `DelegatedOTPNotification` message fields, which you receive from Thredd. For an example request and response, see [Using Delegated SMS API](../3D_Secure/Using_Delegated_SMS_API.htm).

| Field | Description | Data type | Length | Status |
| --- | --- | --- | --- | --- |
| Pubtoken | The 9-digit Thredd public token linked to the card. | Number | 9 digits. | Required |
| DelegatedOtpId | The 36-character unique identifier of the NotifyInitiateAction request. | String | 36 characters. | Required |
| MessageVersion3DS | The 3D Secure message version (For example, 1.0.2). | String | 8 characters. | Required |
| Credential | Object that contains details on the credential. | Object |  |  |
| Id | Unique credential identifier which Thredd generates during enrolment. | String | 36 characters. | Required |
| Type | The credential type. This should be OTPSMS. | String | ENUM | Required |
| Text | The credential value. For example, when the type is OTPSMS, the value is +447654123456. | String | 254 characters. | Required |
| MerchantInfo | Object that contains details of the merchant requesting the authentication. | Object |  |  |
| AcquirerID | Identifier of the merchant acquirer. | String | 11 characters. | Optional |
| MerchantID | Identifier of the merchant performing the purchase request. | String | 35 characters. | Optional |
| MerchantName | The name of the merchant. | String | 40 characters. | Optional |
| MerchantURL | The URL of the merchant's website, or the name of the merchant's app. | String | 2048 characters. | Required |
| MerchantCategoryCode | The category code describing the type of merchant business. | String | 4 characters. | Optional |
| MerchantCountryCode | Country code of the merchant. For 3DS1 transactions this value is the 2-letter format (For example, US). For 3DS2 transactions this value is the 3-digit number format (For example, 840). | String | 3 characters . | Optional |
| MerchantAppRedirectURL | The merchantappredirecturl field is used for app-based transactions and during in-app authentication only.  The callback URL for the merchant's app. Your authentication app should use the callback URL for enabling the merchant app to redirect the cardholder back to the checkout page when they have authenticated.  If this field is empty, your app does not need to initiate a callback to the merchant's app. | String | 256 characters . | Optional |
| TransactionInfo | Provides details of the merchant requesting the transaction. | Object |  |  |
| TransactionTimeStamp | The transaction timestamp in UTC, as per the ISO 8601 UTC specification (for example, 2019-03- 21T20:55:49.000Z). | String | 24 characters. | Optional |
| TransactionAmount | The transaction amount in minor currency units (e.g., 1000 for $10.00). | Number | 48 characters. | Optional |
| TransactionCurrency | The 3-digit numeric ISO-4217 currency code. | String | 3 characters. | Optional |
| TransactionExponent | The exponent for formatting the given ISO-4217 currency code. | String | 1 character. | Optional |
| Passcode | The one time passcode (OTP) sent to the cardholder. | String | 8 characters. | Required |
| MobileNumber | The cardholder's mobile number. | String | 20 characters. | Required |
| MessageContent | The content of the message. | String | 500 characters. | Required |

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