# 6 Implementing In App Provisioning

The following section details how to implement our in-app provisioning. There are four different types of in-app provisioning available:

* Apple Mastercard
* Apple Visa
* Google Mastercard
* Google Visa
* Samsung Visa

## Implementing Mastercard with Apple Pay

The following section describes how to implement in-app provisioning for Mastercard with Apple Pay.

### Pre-requisites

The pre-requisites for using Mastercard with Apple Pay are:

* An agreement with Apple to use Apple Pay service.
* Entitlement to access com.apple.developer.payment-pass-provisioning for your client iOS application.
* A Mastercard RSA 2048-bit Public Key to share with Thredd.
* An RSA public key for TAV generation, which you need to upload to the Key Management Portal application.

### Step One - Retrieve input data from Apple Wallet

Extend `PKAddPaymentPassViewControllerDelegate` to retrieve input data from Apple Wallet. This is where the certificate, nonce and nonce signature are provided by Apple to the Client application. Further details for objects that are required can be found on the [Apple Developer Documentation](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest).

### Step Two - Send API request to Thredd

When you have the data from Apple, use the Create Apple Wallet endpoint to send an API request to Thredd. See the following example request.

[Copy](javascript:void(0);)

```
{  
  "certificates": [  
    "MIICYDCCAgagAwIBAgIUCKCe7rVrw/SGstpLx4KPeLyRjCswCgYIKoZIzj0EAwIwaDELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRYwFAYDVQQDDA1QUFRocmVkZFN1YkNBMB4XDTI1MDIxMzE1MjAzMVoXDTM1MDIxMTE1MjAzMVowZzELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRUwEwYDVQQDDAxQUFRocmVkZExlYWYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATQE/gJiPV/b0xByi4Fbr+UZbq7W5a7NmJlkXjIvBaiL5DoJQIM1maimcEXcuGxQg5ZGa78QVxZIC2QkUTBMYuko4GOMIGLMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAPBgkqhkiG92NkBicEAgUAMB0GA1UdDgQWBBQ+D0zl7sC8vBWb/g90X1uF2xmNhDAfBgNVHSMEGDAWgBTmiALoFDbCkZEInQdscUx+10NpVDAKBggqhkjOPQQDAgNIADBFAiEAtdZ3fLs2gcidvknZQs9uDoVv6/fyf5GQ4SkeddbsYaACICYczmRL0PFSgF9O5LKDOSVnLbs9TDK1RiLEELtH6ovN",  
    "MIICYDCCAgagAwIBAgIUCKCe7rVrw/SGstpLx4KPeLyRjCswCgYIKoZIzj0EAwIwaDELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRYwFAYDVQQDDA1QUFRocmVkZFN1YkNBMB4XDTI1MDIxMzE1MjAzMVoXDTM1MDIxMTE1MjAzMVowZzELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRUwEwYDVQQDDAxQUFRocmVkZExlYWYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATQE/gJiPV/b0xByi4Fbr+UZbq7W5a7NmJlkXjIvBaiL5DoJQIM1maimcEXcuGxQg5ZGa78QVxZIC2QkUTBMYuko4GOMIGLMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAPBgkqhkiG92NkBicEAgUAMB0GA1UdDgQWBBQ+D0zl7sC8vBWb/g90X1uF2xmNhDAfBgNVHSMEGDAWgBTmiALoFDbCkZEInQdscUx+10NpVDAKBggqhkjOPQQDAgNIADBFAiEAtdZ3fLs2gcidvknZQs9uDoVv6/fyf5GQ4SkeddbsYaACICYczmRL0PFSgF9O5LKDOSVnLbs9TDK1RiLEELtH6ovN"  
  ],  
  "nonce": "c5846fb5",  
  "nonceSignature": "4061d9d63ed34825f285d953274a6c5e06ebe011bf91d79660e1f7c6f6d21427abb3a62e6352e430abff987f6ec37e5dff9f3dbe40275156d03eeb594ab191d2792f37ef13ac528a65f56165c1d753463f"  
}
```

For more information on this endpoint, see [Apple In-App Push Provisioning](https://cardsapidocs.thredd.com/v2/docs/request-apple-payload) and [Apple In-App Push Provisioning - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/request-apple-payload-field-descriptions).

### Step Three - Receive API response from Thredd

If the API request is successful, a 200 response is returned. See the following example.

[Copy](javascript:void(0);)

```
{  
  "encryptedPassData":"ew0KICAiTmFtZSI6ICIiLA0KICAiTm9uY2UiOiAiIiwNCiAgIk5vbmNlU2lnbmF0dXJlIjogIiIsDQogICJQcmltYXJ5QWNjb3VudE51bWJlclByZWZpeCI6ICIiLA0KICAiRW5jcnlwdGVkUHJpbWFyeUFjY291bnROdW1iZXIiOiB7DQogICAgIkVuY3J5cHRlZFBheWxvYWQiOiB7DQogICAgICAiUHVibGljS2V5RmluZ2VyUHJpbnQiOiAiIiwNCiAgICAgICJFbmNyeXB0ZWRLZXkiOiAiIiwNCiAgICAgICJPYWVwSGFzaGluZ0FsZ29yaXRobSI6ICIiLA0KICAgICAgIkl2IjogIiIsDQogICAgICAiRW5jcnlwdGVkRGF0YSI6ICIiDQogICAgfQ0KICB9LA0KICAiTmV0d29ya05hbWUiOiAiTWFzdGVyY2FyZCIsDQogICJQcm9kdWN0VHlwZSI6ICJERUZBVUxUX01BU1RFUkNBUkQiLA0KICAiVmVyc2lvbiI6ICIxIg0KfQ==",  
  "activationData":"ew0KICAiVmVyc2lvbiI6ICI0IiwNCiAgIktleUFsaWFzIjogIiIsDQogICJTaWduYXR1cmVBbGdvcml0aG0iOiAiUlNBLVNIQTI1NiIsDQogICJJbmNsdWRlZEZpZWxkc0luT3JkZXIiOiAiZGF0YVZhbGlkVW50aWxUaW1lc3RhbXB8YWNjb3VudE51bWJlcnxhY2NvdW50RXhwaXJ5IiwNCiAgIkRhdGFWYWxpZFVudGlsVGltZXN0YW1wIjogIiIsDQogICJTaWduYXR1cmUiOiAiIg0KfQ==",  
  "ephemeralPublicKey":"MzkzMDAwMDA="  
}
```

### Step Four - Send output data to Apple Wallet

To provision payments passes (cards) in your app, Thredd clients must initialise and invoke the `PKAddPaymentPassViewController` with a `PKAddPaymentPassRequestConfigurationobject`.

## Implementing Visa with Apple Pay

The following section describes how to implement in-app provisioning for Visa with Apple Pay.

### Pre-requisites

The pre-requisites for using Apple Pay with Visa are:

* An agreement with Apple to use the Apple Pay service.
* Your client iOS application requires com.apple.developer.payment-pass-provisioning entitlement.
* To exchange the Web Services key (WSDK) with Visa.

### Step One - Retrieve input data from Apple Wallet

Extend `PKAddPaymentPassViewControllerDelegate`. This is where the certificate, nonce and nonce signature are provided by Apple to the Client application. Further details for objects that are required can be found on the [Apple Developer Documentation](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest).

### Step Two - Send API request to Thredd

When you have the data from Apple, use the Create Apple Wallet endpoint to send an API request to Thredd. See the following example request.

[Copy](javascript:void(0);)

```
{  
  "certificates": [  
    "MIICYDCCAgagAwIBAgIUCKCe7rVrw/SGstpLx4KPeLyRjCswCgYIKoZIzj0EAwIwaDELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRYwFAYDVQQDDA1QUFRocmVkZFN1YkNBMB4XDTI1MDIxMzE1MjAzMVoXDTM1MDIxMTE1MjAzMVowZzELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRUwEwYDVQQDDAxQUFRocmVkZExlYWYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATQE/gJiPV/b0xByi4Fbr+UZbq7W5a7NmJlkXjIvBaiL5DoJQIM1maimcEXcuGxQg5ZGa78QVxZIC2QkUTBMYuko4GOMIGLMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAPBgkqhkiG92NkBicEAgUAMB0GA1UdDgQWBBQ+D0zl7sC8vBWb/g90X1uF2xmNhDAfBgNVHSMEGDAWgBTmiALoFDbCkZEInQdscUx+10NpVDAKBggqhkjOPQQDAgNIADBFAiEAtdZ3fLs2gcidvknZQs9uDoVv6/fyf5GQ4SkeddbsYaACICYczmRL0PFSgF9O5LKDOSVnLbs9TDK1RiLEELtH6ovN",  
    "MIICYDCCAgagAwIBAgIUCKCe7rVrw/SGstpLx4KPeLyRjCswCgYIKoZIzj0EAwIwaDELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRYwFAYDVQQDDA1QUFRocmVkZFN1YkNBMB4XDTI1MDIxMzE1MjAzMVoXDTM1MDIxMTE1MjAzMVowZzELMAkGA1UEBhMCVUsxDjAMBgNVBAgMBVN0YXRlMQ8wDQYDVQQHDAZMb25kb24xDzANBgNVBAoMBlRocmVkZDEPMA0GA1UECwwGVGhyZWRkMRUwEwYDVQQDDAxQUFRocmVkZExlYWYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATQE/gJiPV/b0xByi4Fbr+UZbq7W5a7NmJlkXjIvBaiL5DoJQIM1maimcEXcuGxQg5ZGa78QVxZIC2QkUTBMYuko4GOMIGLMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAPBgkqhkiG92NkBicEAgUAMB0GA1UdDgQWBBQ+D0zl7sC8vBWb/g90X1uF2xmNhDAfBgNVHSMEGDAWgBTmiALoFDbCkZEInQdscUx+10NpVDAKBggqhkjOPQQDAgNIADBFAiEAtdZ3fLs2gcidvknZQs9uDoVv6/fyf5GQ4SkeddbsYaACICYczmRL0PFSgF9O5LKDOSVnLbs9TDK1RiLEELtH6ovN"  
  ],  
  "nonce": "c5846fb5",  
  "nonceSignature": "4061d9d63ed34825f285d953274a6c5e06ebe011bf91d79660e1f7c6f6d21427abb3a62e6352e430abff987f6ec37e5dff9f3dbe40275156d03eeb594ab191d2792f37ef13ac528a65f56165c1d753463f"  
}
```

For more information on this endpoint, see [Apple In-App Push Provisioning](https://cardsapidocs.thredd.com/v2/docs/request-apple-payload) and [Apple In-App Push Provisioning - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/request-apple-payload-field-descriptions).

### Step Three - Receive API response from Thredd

If the API request is successful, a 200 response is returned. See the following example.

[Copy](javascript:void(0);)

```
{  
  "encryptedPassData":"ew0KICAiTmFtZSI6ICIiLA0KICAiTm9uY2UiOiAiIiwNCiAgIk5vbmNlU2lnbmF0dXJlIjogIiIsDQogICJQcmltYXJ5QWNjb3VudE51bWJlclByZWZpeCI6ICIiLA0KICAiRW5jcnlwdGVkUHJpbWFyeUFjY291bnROdW1iZXIiOiB7DQogICAgIkVuY3J5cHRlZFBheWxvYWQiOiB7DQogICAgICAiUHVibGljS2V5RmluZ2VyUHJpbnQiOiAiIiwNCiAgICAgICJFbmNyeXB0ZWRLZXkiOiAiIiwNCiAgICAgICJPYWVwSGFzaGluZ0FsZ29yaXRobSI6ICIiLA0KICAgICAgIkl2IjogIiIsDQogICAgICAiRW5jcnlwdGVkRGF0YSI6ICIiDQogICAgfQ0KICB9LA0KICAiTmV0d29ya05hbWUiOiAiTWFzdGVyY2FyZCIsDQogICJQcm9kdWN0VHlwZSI6ICJERUZBVUxUX01BU1RFUkNBUkQiLA0KICAiVmVyc2lvbiI6ICIxIg0KfQ==",  
  "activationData":"ew0KICAiVmVyc2lvbiI6ICI0IiwNCiAgIktleUFsaWFzIjogIiIsDQogICJTaWduYXR1cmVBbGdvcml0aG0iOiAiUlNBLVNIQTI1NiIsDQogICJJbmNsdWRlZEZpZWxkc0luT3JkZXIiOiAiZGF0YVZhbGlkVW50aWxUaW1lc3RhbXB8YWNjb3VudE51bWJlcnxhY2NvdW50RXhwaXJ5IiwNCiAgIkRhdGFWYWxpZFVudGlsVGltZXN0YW1wIjogIiIsDQogICJTaWduYXR1cmUiOiAiIg0KfQ==",  
  "ephemeralPublicKey":"MzkzMDAwMDA="  
}
```

### Step Four - Send output data to Apple Wallet

To provision payment passes (cards) in your app, Thredd clients must initialise and invoke the `PKAddPaymentPassViewController` with a `PKAddPaymentPassRequestConfigurationobject`.

## Implementing Mastercard with Google Pay

The following section describes how to implement in-app provisioning for Mastercard with Google Pay.

### Pre-requisites

The pre-requisites for using Mastercard with Google Pay are:

* An agreement with Google which grants permission to use the Google Push Provisioning API, and permits you to share all required data elements.
* Your apps must be added to the allow list for Google's Push Provisioning. See [API - Push Provisioning API Access](https://developers.google.com/pay/issuers/apis/push-provisioning/android/allowlist) for more information.

  You must sign up and request access to view Google's documentation.
* Integrate the **Add to Google Pay** button into your mobile app.
* Obtain the Mastercard RSA 2048-bit Public Key and share with Thredd.
* Upload an RSA public key for TAV generation into the Key Management Portal application

### Step One - Send API request to Thredd

When you have the data from Google, use the endpoint to send an API request to Thredd. Note if the billing object is left blank then the address associated with the publicToken for the card will be used instead.

[Copy](javascript:void(0);)

```
{  
"billing": {  
    "line1": "32 Eastern Drive",  
    "line2": "Thurcroft",  
    "city": "Sheffield",  
    "countrySubdivision": "South Yorkshire",  
    "postalCode": "S25 1AA",  
    "country": "GBR"  
  }  
}
```

For more information on this endpoint, see [Google In-App Push Provisioning](https://cardsapidocs.thredd.com/v2/docs/request-google-payload) and [Google In-App Push Provisioning - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/request-google-payload-field-descriptions).

### Step Two - Receive API response from Thredd

If the API request is successful, a 200 response is returned. See the following example.

[Copy](javascript:void(0);)

```
{  
  "opaquePaymentCard": "string",  
  "last4digits": "string",  
  "name": "string",  
  "network": "Mastercard",  
  "address": {  
    "line1": "string",  
    "line2": "string",  
    "city": "string",  
    "countrySubdivision": "string",  
    "postalCode": "string",  
    "country": "yIa"  
  }  
}
```

### Step Three - Send API response to Google Push Provisioning API

After receiving a successful response, the information should be shared with Google using their Push Provisioning API.

## Implementing Visa with Google Pay

The following section describes how to implement in-app provisioning for Visa with Google Pay.

### Pre-requisites

The pre-requisites for using Visa with Google Pay are:

* An agreement with Google which grants permission to use the Google Push Provisioning API, and permits you to share all required data elements.
* Your apps must be added to the allow list for Google's Push Provisioning. See [API - Push Provisioning API Access](https://developers.google.com/pay/issuers/apis/push-provisioning/android/allowlist) for more information.

  You must sign up and request access to view Google's documentation.
* Integrate the **Add to Google Pay** button into your mobile app.
* Exchange API Key with Visa and share with Thredd.
* Exchange shared secret with Visa and share with Thredd.

### Step One - Send API request to Thredd

When you have the data from Google, use the endpoint to send an API request to Thredd. See the following example request.

[Copy](javascript:void(0);)

```
{  
  "clientWalletProvider": "string",  
  "clientWalletAccountID": "string",  
  "clientDeviceID": "string",  
  "clientAppID": "string",  
  "billing": {  
    "line1": "string",  
    "line2": "string",  
    "city": "string",  
    "countrySubdivision": "string",  
    "postalCode": "string",  
    "country": "gQc"  
  }  
}
```

For more information on this endpoint, see [Google In-App Push Provisioning](https://cardsapidocs.thredd.com/v2/docs/request-google-payload) and [Google In-App Push Provisioning - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/request-google-payload-field-descriptions).

### Step Two - Receive API response from Thredd

If the API request is successful, a 200 response is returned. See the following example.

[Copy](javascript:void(0);)

```
{  
  "opaquePaymentCard": "string",  
  "last4digits": "string",  
  "name": "string",  
  "network": "Mastercard",  
  "address": {  
    "line1": "string",  
    "line2": "string",  
    "city": "string",  
    "countrySubdivision": "string",  
    "postalCode": "string",  
    "country": "yIa"  
  }  
}
```

### Step Three - Send API response to Google Push Provisioning API

After receiving a successful response, the information should be shared with Google using their Push Provisioning API.

## Implementing Visa with Samsung Pay

The following section describes how to implement in-app provisioning for Visa with Samsung Pay. This is similar to implementing Google pay for Visa, with some differences to the pre-requisites.

### Pre-requisites

The pre-requisites for using Visa with Samsung Pay are:

* An agreement with Samsung which grants permission to use the Samsung Push Provisioning API, and permits you to share all required data elements.
* Integrate the **Add to Samsung Pay** button into your mobile app.
* Exchange API Key with Visa and share with Thredd.
* Exchange shared secret with Visa and share with Thredd.

### Step One - Send API request to Thredd

When you have the data from Samsung, use the endpoint to send an API request to Thredd. See the following example request.

[Copy](javascript:void(0);)

```
{  
  "clientWalletProvider": "string",  
  "clientWalletAccountID": "string",  
  "clientDeviceID": "string",  
  "clientAppID": "string",  
  "billing": {  
    "line1": "string",  
    "line2": "string",  
    "city": "string",  
    "countrySubdivision": "string",  
    "postalCode": "string",  
    "country": "gQc"  
  }  
}
```

For more information on this endpoint, see [Samsung In-App Push Provisioning](https://cardsapidocs.thredd.com/v2/docs/samsung-in-app-push-provisioning) and [Samsung In-App Push Provisioning - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/samsung-in-app-push-provisioning-field-descriptions/).

### Step Two - Receive API response from Thredd

If the API request is successful, a 200 response is returned. See the following example.

[Copy](javascript:void(0);)

```
{  
  "opaquePaymentCard": "string",  
  "last4digits": "string",  
  "name": "string",  
  "network": "Visa",  
  "address": {  
    "line1": "string",  
    "line2": "string",  
    "city": "string",  
    "countrySubdivision": "string",  
    "postalCode": "string",  
    "country": "yIa"  
  }  
}
```

### Step Three - Send API response to Samsung Push Provisioning API

After receiving a successful response, the information should be shared with Samsung using their Push Provisioning API.