# 16 Using Delegated SMS API

The delegated SMS API enables you to receive the 3DS OTP (One-time-password) code from Thredd during the 3D Secure authentication session, allowing you to send the OTP code to the cardholder.

. Thredd provides you with a request in the `DelegatedOTPNotification` endpoint containing details of the transaction, the merchant and the OTP. You send a response back to Thredd in order to acknowledge that you received the OTP.

You must acknowledge the request as successful request with a 200 status response within a 10 second timeframe.

## Prerequisites

To use the Delegated SMS API, you must first do the following:

* Contact your Thredd Account Manager asking to use this service.
* Supply your `DelegateOTPnotification` endpoints for UAT and Production environments.
* Ensure that your firewalls allow Thredd IP addresses. See [Authorising Thredd IP Addresses](Authorising_IP_Addresses.htm).
* Nominate and share with Thredd the product you're going to test with in UAT and Production environments.
* Enrol cards with OTP SMS credentials to use the Delegated SMS API.

## Notification Signature

The verification of the notification signature is optional, though Thredd recommends that you use it.

The notifications JSON body are signed using SHA256withRSA. The signature is included in the `X-Thredd-Signature` HTTP header. You can use the public key to verify the authenticity and integrity of the notification.

The process for checking the signature is as follows:

### Step 1: Receive the Notification

You receive a JSON notification from Thredd which includes the X-Thredd-Signature header. See the following example:

[Copy](javascript:void(0);)

```
X-Thredd-Signature:  
k=I0SqfGljT-fn_oIeFAypGC66PduPP08XioSKM1ZNoEc,  
s=452ad9892d5687bd660eac27428a9301bc363f3db875f8307da25e9b0a231556
```

### Step 2: Extract the Signature Info

From the X-Thredd-Signature header, extract the key ID, designated `k` in the header (which tells you which key was used). Then extract the signature, designated `s` in the header (the actual digital signature).

### Step 3: Get the Public Key

Use the JWKS Endpoint URL to download a JSON file with the public key included. The following table describes the endpoint URLs you need for each environment.

| Environment | JWKS Endpoint URL |
| --- | --- |
| UAT | https://keystore.directory.sandbox.threddid.com/906d9a03-836e-4af0-b500-f84ef48247d3/aae5943b-f6ab-4e0a-bb7f-7ddb75c1685a/application.jwks |
| Production | https://keystore.directory.threddid.com/cf253304-8bbb-44ff-938c-89fd11e9651a/e5a5116a-2de3-4265-9d0a-c0b5bca94c34/application.jwks |

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

The JWKS Endpoint URL is publicly accessible and may need to be whitelisted on the program managerâs side, depending on your network security policies. JWKS Endpoint URLs are static and idempotent; they remain unchanged even when certificates are renewed at Threddâs side.

### Step 4: Find the Matching Key

Browse the JWKS file for the key with the same kid (key ID). This is the public key that matches the one Thredd used to sign the message.

[Copy](javascript:void(0);)

```
{  
  "keys": [  
    {  
      "kty": "RSA",  
      "use": "sig",  
      "x5c": [  
        "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"  
      ],  
      "n": "im_kob7rE8e9whraPo5Zo_QJOsH70SaAvoOxe0yt0zZZGBSOvTrYJt5ymY45STFNGO5FEC8MaBycUkbbDfL8YF-CSbkDZlp4XEs7GyI9x622RZjnPFEmvSzCN7CvIc9_IlIBTIDVZf_YkbeD_BZDltwg5HPCO3hWOHtSBXj93pZV3fMe7kvbLcFohQcP40knUHYXejr7YH9_hddEksuG-0jFrmjY-mh3DuHgA2__u0TDz6Bh2DeRCGJJWV0v0q0fiq96HBe9PU2HUO9elod8N4UQZZIOP-3rUO50S5eQZlCMzLV9Ygvp9oXjQX1vXKfb3rS-X5VYoNaVJne_HnrpiQ",  
      "e": "AQAB",  
      "kid": "I0SqfGljT-fn_oIeFAypGC66PduPP08XioSKM1ZNoEc",  
      "x5u": "https://keystore.directory.sandbox.threddid.com/906d9a03-836e-4af0-b500-f84ef48247d3/aae5943b-f6ab-4e0a-bb7f-7ddb75c1685a/ndqXpdRi_k46QLcLP7CmvJSKZx7VFfUc52J8G2kSiGc.pem",  
      "x5t#S256": "ndqXpdRi_k46QLcLP7CmvJSKZx7VFfUc52J8G2kSiGc",  
      "x5dn": "CN=aae5943b-f6ab-4e0a-bb7f-7ddb75c1685a,OU=906d9a03-836e-4af0-b500-f84ef48247d3,O=thredd,C=GB"  
    }  
  ]  
}
```

### Step 5: Verify the Signature

Use your programming languageâs library to verify the signature. Check that the signature is valid for the JSON body you received, using the public key in the JWKS JSON file.

## DelegatedOTPNotification Example Request

The following is an example `DelegatedOTPNotification` request.

[Copy](javascript:void(0);)

```
{  
    "Pubtoken": 100111111,  
    "DelegatedOtpId": "24b78815-7547-4768-b1f8-9a07ebbdaa3b",  
    "MessageVersion3DS": "1.0.2",  
    "Credential": {  
        "Id": "000000000000000000000000000002045695",  
        "Type": "OTPSMS",  
        "Text": "xxxxxxxxx6385"  
    },  
    "MerchantInfo": {  
        "AcquirerID": "1234567",  
        "MerchantID": "123456789",  
        "MerchantName": "Test Merchant",  
        "MerchantURL": "www.test.com",  
        "MerchantCategoryCode": "2468",  
        "MerchantCountryCode": "840",  
        "MerchantAppRedirectURL": "merchantScheme://appName?translD=b2385523-a66c-4907ac3c-91848e8c0067"  
    },  
    "TransactionInfo": {  
        "TransactionTimeStamp": "2021-12-17 15:48:23.2877",  
        "TransactionAmount": 1000,  
        "TransactionCurrency": "826",  
        "TransactionExponent": 2  
    },  
    "Passcode": "123456",  
    "MobileNumber": "+911234567890",  
    "MessageContent": "123456 is the One Time Password for purchase of GBP 10.00 at Test Merchant with card ending 6443 . Please use the One Time Password to complete the transaction."  
}
```

A successful response returns a 200 status.

For more information on the DelegatedOTPNotification endpoint fields, see [Appendix 6: DelegatedOTPNotification Fields](../Reference/Delegated_SMS_Fields.htm).