# 17 Using the Biometric/In-App Authentication APIs

REST-based APIs are used to initiate a Biometric or In-App OOB authentication session and to provide the result. The body of a REST-based API message is in JSON format. Three APIs are used to support Biometric/In-App authentication:

* `DelegateSCANotification` â sent by Thredd to notify you to set up an authentication session
* `DelegateSCAValidation` â as a Program Manager, you use this API to send the authentication result to Thredd.
* `DelegateSCACancelNotification` â sent by Thredd to notify you the cardholder cancelled the authentication.

## 17.1 Initiating a Biometric Session

When Thredd receives a request for Biometric/In-App authentication from Apata, Thredd uses the `DelegateSCANotification` API, to send your system a request to initiate a Biometric/In-App session. This request is sent to the `DelegateSCANotification` endpoint you specified in the 3DS Product Setup Form (see [Completing your 3DS Product Setup Form](Completing_the_PSF.htm)).

See the example below:

#### Thredd Request

```
{  
    "NotificationId": "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
    "PubToken": "123456789",  
    "DelegateMethod": "push-confirmation",  
    "FinancialInstitutionId": "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
    "Language": "en-EN",  
    "DelegateScaId": "bcd507g1-7ec8-43b4-8a07-6c5e17078967",  
    "CardScheme": "MasterCard",  
    "CreatedMode": "GA",  
    "Device": {  
        "Channel": "BROWSER",  
        "Ip": "string",  
        "Language": "en-EN"  
    },  
    "MerchantInfo": {  
        "Id": "mer-12345",  
        "Name": "Amazon",  
        "Country": "840",  
        "Url": "https://amazon.com ",  
        "ChallengePreference": "no-preference",  
        "RedirectAppUrl": "merchantScheme://appName?transID=b2385523-a66c-4907-ac3c-91848e8c0067"  
    },  
    "TransactionInfo": {  
        "Type": "payment",  
        "ProtocolVersion": "1.0.2",  
        "Channel": "app",  
        "DsTransactionId": "98315a91-e0b6-4fe0-8842-9ed82ea8ef0b",  
        "Date": "2023-08-17T10:35:32.061Z",  
        "ChallengedAt": 1650696156,  
        "ChallengeExpiresAfter": 300,  
        "ChallengeExpiry": 1650696456,  
        "ChallengeMethod": "push-confirmation",  
        "Amount": "12345",  
        "Currency": {  
            "Code": "978",  
            "Exponent": "2"  
        },  
        "Recur": {  
            "Frequency": "30",  
            "EndRecur": "20221212"  
        },  
        "Install": "5"  
    },  
    "DelegateStatus": "Active"  
}
```

For more information on the fields in the request, see the [DelegateSCANotification and DelegateSCACancelNotification](../Reference_Apata/Biometric_OOB_Fields.htm#_NotifyInitiateAction_Message_Reques) message fields.

#### Your Response

Upon receipt of a request, your systems return a 200-HTTP response code (OK/success).

If Thredd does not receive the 200-HTTP response to the `DelegateSCANotification` request, Thredd does not resend the request.

When your systems receive a `DelegateSCANotification` request, you can use the Thredd oAuth server to validate the token (as an option.) This prompts the cardholder to open your Smart device customer application and authenticate themselves with the supported Biometric method (e.g., fingerprint or face recognition) or In-App method.

Thredd passes the bearer token in the header of the `DelegateSCANotification` request, as shown in the example below.

[Copy](javascript:void(0);)

```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjE5ODI3Q0E4M0NEMkNGNUUzMTAxMUVBQkQ0N0ZDNTg4RkMyRjQ3RTIiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJHWUo4cUR6U3oxNHhBUjZyMUhfRmlQd3ZSLUkifQ.eyJuYmYiOjE2MDc1MzM1NzksImV4cCI6MTYwNzU0Nzk3OSwiaXNzIjoiaHR0cHM6Ly9vYXV0aHVhdC5nbG9iYWxwcm9jZXNzaW5nLm5ldCIsImF1ZCI6WyJyZHhhcGkiLCJmaXJiaW9tZXRyaWNhcGkiXSwiY2xpZW50X2lkIjoiZmlyYmlvIiwic2NvcGUiOlsiY2xpZW50X3ZhbGlkYXRlIiwiZmlyYmlvbWV0cmljYXBpIl19.owfqYt7Rf6zHMLY2HT3j0RH7Lti05oWkp-bJ41QF1LZyqxaRMZWJAUxuRXJwIWrG2wtC0Q1KFzVPbZhpwKAwJvQTIymJFhryEvRUGTQqM61Nwu_Dnsx8H-Jpi7_0PjQk4MaAhqFv6MEgDMHvxUZ2_Q6vYj_-h2rRDunHjBvhvA55-yGLdqxeHRtNvHJQCsaVZHdLBngUpeFpWcvrbhk1SYbNlGlflYBm5aAX_YDwpWt4p_M6w7TAYJZQvc4Hi_NqAZwUOY7xOlhVD69onUmd74k6nt0ncowGgC3naWQieqcVMd3B1kCAnnYZfLlXMhSxeN_XqWtjKTK3WMavYj6vrw
```

As an option, you can also verify the token (check that it is valid and active) using the oAuth introspect API endpoint. For more details, see [Using the oAuth server.](#_OAuth)

## 17.2 Notifying Thredd of the Result of the Biometric Session

When authentication is complete, you must use the `DelegateSCAValidation` REST API to send the authentication outcome to Thredd.

The authentication session times out if Thredd does not receive your `DelegateSCAValidation` request before the `challengeExpiry` time.

#### API Endpoints

*https://uat-notifier-receiver.thredd.net:7293/api/v1/NotifierReceiver*

See the example JSON message below:

#### Your Request

```
{  
  "NotificationId" : "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
  "PubToken": "123456789",  
  "DelegateScaId": "bcd507g1-7ec8-43b4-8a07-6c5e17078967",  
  "PmReferenceId": "refId",  
  "Status": "SUCCESS",  
  "Error": null  
}
```

#### Notes

Thredd token of the card that was authenticated:

> ```
> "PubToken":"123456789",
> ```

The message also contains the result of your authentication as: SUCCESS, FAILURE, FAILWITHFEEDBACK or ERROR. For example:

```
"status: SUCCESS"
```

#### Successful Thredd Response

If the request from the client was successful, Thredd provides a response in return.

```
{  
"PubToken":"206187551",  
"DelegateScaId":"ddab0431-a615-42d7-81ab-5a6683bb5c3e",  
"PmReferenceId":"refId",  
"Status":"SUCCESS",  
"Error": {  
        "ReferenceNumber": "",  
        "Description": "",  
        "Message": ""  
    }  
}
```

When successful, the transaction proceeds to authorisation.

#### Error Handling

If there was an error in your request, for example, invalid JSON format or incorrect details, Thredd returns details of the error.

For more information on the fields in the response, see [DelegateSCAValidation Message Fields](../Reference_Apata/Biometric_OOB_Fields.htm#_NotifyValidate_Message_Fields).

#### Example Thredd Response for a Reporting Failure

If Thredd is unable to report the biometric authentication result to Apata, an error message appears similar to this:

```
{  
   "Pubtoken":"182293241",  
   "DelegateScaId":"82b44d02-71db-4d00-9b3d-9fb7c0aa5eaa",  
   "PmReferenceId":"refId",  
   "Status":"FAILWITHFEEDBACK",  
   "Error":  
   "ReferenceNumber":"504023",  
   "Description":"DelegateSca status reporting to 3DSProvider failed",  
   "Message":"DelegateSca status reporting to 3DSProvider failed"  
}
```

#### Validation Timeout

When Thredd sends the `DelegateSCANotification` message to your system, Thredd expects to receive back a `DelegateSCAValidation` response from your system before the challenge expiry time provided in the `DelegateSCANotification`.

If Thredd does not receive the `DelegateSCAValidation` response within this period, the authentication session times out. Apata then returns a Fail result to the merchant.

## 17.3 Using the Thredd oAuth server

You must authenticate against the Thredd oAuth server before you can use the 3D Secure Biometric API services. The oAuth server provides you with a username (client\_ID) and a secret password (Client\_secret) that you need to include in your API requests for accessing the Biometric/OOB API services.

You can also use the oAuth server to validate any API requests received from Thredd; Thredd provides you with another username (client\_ID) and a secret password (Client\_secret) for the token validation.

oAuth is a secure method that replaces TLS and does not require you to set up X509 certificates. There are no additional costs for using the Thredd oAuth server.

The oAuth server complies with the RFC 7662 standard. See: <https://tools.ietf.org/html/rfc7662>

To find out more, see the identity server documentation, available at: <https://identityserver4.readthedocs.io/en/latest/intro/specs.html>

#### oAuth API Endpoints

Thredd provides the following oAuth API endpoints:

* Token â you can use this to obtain a token. Whenever you use the Biometric/ OOB API, you should include this token in the Authorization header of your HTTP request.
* Introspect â you can use this to validate the token Thredd sends to your `DelegateSCANotification` endpoint (to notify you of a request to initiate a Biometric/In-App session)

Thredd oAuth endpoints for Token and Introspect are listed below:

| Environment | Endpoint |
| --- | --- |
| UAT | |  | | --- | | *https://uatists.globalprocessing.net/connect/token* | | *https://uatists.globalprocessing.net/connect/introspect* | |
| Live (Production) | |  | | --- | | *https://p1ists.globalprocessing.net/connect/token* | | *https://p1ists.globalprocessing.net/connect/introspect* | |

#### oAuth User Credentials

Check with your Thredd 3DS project manager for your **client\_id** and **client\_secret** to access the oAuth server.

#### oAuth Token Expiry

The default lifetime of the token is 4 hours (14400 seconds).

#### oAuth Token Request Example

You can retrieve an oAuth access token from the Thredd oAuth server using the private credentials (client\_id and client\_secret) provided to you by Thredd.

The following is an oAuth Token request:

[Copy](javascript:void(0);)

```
POST https://uatists.globalprocessing.net/connect/token  
Accept:    application/json  
Content-Type: application/x-www-form-urlencoded  
client_id=9d70c6bbad8ad20262828222fc0f3fdd  
&client_secret=a3d5566e8ca0d6da823eb7815c1c2b66  
&grant_type=client_credentials
```

The following is an oAuth Token response. The oAuth server returns a token, which you must include in any Biometric/OOB requests.

[Copy](javascript:void(0);)

```
200 OK  
  
{  
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhNjdmOWEzZTA1OTM0ZWZjOTUzYmY1ZjI1ZjVkMDMyIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1ODI1NDExMTYsImV4cCI6MTU4MjU0NDcxNiwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NDQzMzYiLCJhdWQiOlsiaHR0cHM6Ly9sb2NhbGhvc3Q6NDQzMzYvcmVzb3VyY2VzIiwicmR4YXBpIiwicmVsYXlhcGkiXSwiY2xpZW50X2lkIjoidmNhcyIsInNjb3BlIjpbImNsaWVudF92YWxpZGF0ZSIsInJkeGFwaSIsInJlbGF5YXBpIl19.Lh5Mp0Qa82QVMzs4ylmzbB9W9Qk4qiVcODewvOq3N1_JmspKyYyhOilVj8KxNxPjiKVYnFA2hDWtlKO16l8aL1oEkBky1h4haQuqtPWaUdNirWVDs99R1VqCh3wYmYZmNHNseJvEVIrd__HQ7kTJLGO7NkebPc_QM6rTB2qfYI9nax6JQnMrk72cDzeorwUlxSf2G6p49kpgyhNJooHfptWlRtV6JWUPUVEC7oNEfYnbfjVhSUyF5_11HHi_2r0zLhFIdPH7fSUXzl8OOOCMqUvSedaAJN6SRIEnTiE5isjIMJG3T4pymqUcc6ujm3upB9UStaBXMelp7Rom7LVqQ",  
    "expires_in": 3600,  
    "token_type": "Bearer",  
    "scope": "client_validate apataapi"  
}
```

The Thredd oAuth server supports basic HTTP status codes. See the table below:

| Status | Description |
| --- | --- |
| 200 | The request was successful. |
| 400 | The server could not understand the request due to invalid syntax. |
| 401 | The client must authenticate itself to get the requested response. |
| 403 | The client does not have access rights to the content. |
| 404 | The server cannot find the requested resource. |
| 500 | The server has encountered a situation it doesn't know how to handle. |

When obtained, your Client application must pass the access token on every request made to the Thredd Biometric/OOB service. The access token is included in the standard Authorization header of the HTTP request as shown in the following example:

[Copy](javascript:void(0);)

```
Authorization: Bearer XXXXXX_ACCESS_TOKEN_XXXXX
```

#### oAuth Introspect Example

Thredd includes a token in the header of the request sent to your `DelegateSCANotification` endpoint. As an option, you can use the Introspect endpoint to validate this token where you check that it is active.  Below are examples of an oAuth Introspect request and response.

[Copy](javascript:void(0);)

```
POST https://uatists.globalprocessing.net/connect/introspect  
Accept:    application/json  
Content-Type: application/x-www-form-urlencoded  
token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjE5ODI3Q0E4M0NEMkNGNUUzMTAxMUVBQkQ0N0ZDNTg4RkMyRjQ3RTIiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJHWUo4cUR6U3oxNHhBUjZyMUhfRmlQd3ZSLUkifQ.eyJuYmYiOjE2MDc1MzM1NzksImV4cCI6MTYwNzU0Nzk3OSwiaXNzIjoiaHR0cHM6Ly9vYXV0aHVhdC5nbG9iYWxwcm9jZXNzaW5nLm5ldCIsImF1ZCI6WyJyZHhhcGkiLCJmaXJiaW9tZXRyaWNhcGkiXSwiY2xpZW50X2lkIjoiZmlyYmlvIiwic2NvcGUiOlsiY2xpZW50X3ZhbGlkYXRlIiwiZmlyYmlvbWV0cmljYXBpIl19.owfqYt7Rf6zHMLY2HT3j0RH7Lti05oWkp-bJ41QF1LZyqxaRMZWJAUxuRXJwIWrG2wtC0Q1KFzVPbZhpwKAwJvQTIymJFhryEvRUGTQqM61Nwu_Dnsx8H-Jpi7_0PjQk4MaAhqFv6MEgDMHvxUZ2_Q6vYj_-h2rRDunHjBvhvA55-yGLdqxeHRtNvHJQCsaVZHdLBngUpeFpWcvrbhk1SYbNlGlflYBm5aAX_YDwpWt4p_M6w7TAYJZQvc4Hi_NqAZwUOY7xOlhVD69onUmd74k6nt0ncowGgC3naWQieqcVMd3B1kCAnnYZfLlXMhSxeN_XqWtjKTK3WMavYj6vrw
```

#### Response (Successful)

[Copy](javascript:void(0);)

```
{   
 "nbf":1616170152,   
 "exp":1616184602,   
 "iss":https://stsdemo.globalprocessing.net,   
 "aud":[   
  "coreapi",   
  "relayapi"   
 ],   
 "client_id":"coreapidev",   
 "active":true,   
 "scope":"coreapi"   
} 
```

#### 

#### Notes

* In the request body, the Content-Type is **application/x-www-form-urlencoded**
* `token` is the bearer token value you received in the header of a `DelegateSCANotification` request from Thredd.)
* The authorization header should be in the following format: Basic (hashed value). The hashed value needs to be `resourceid:password` and must be base64 encoded.
* The `scope` field indicates your application permissions. It is sufficient to check that the bearer token is `active`. You can also check the scope.
* If you are using .NET, recommends using the Identity Model middleware software package. For more information, see <https://identitymodel.readthedocs.io/en/latest/>
* The following setting indicates that the bearer token is active.

> [Copy](javascript:void(0);)
>
> ```
>  "active":true, 
> ```

#### Response (Failure)

[Copy](javascript:void(0);)

```
{   
"active":false   
} 
```

The following setting indicates that the bearer token is **not** active.

## 17.4 Cancelling an authentication

If a cardholder cancels an authentication, Thredd sends your system a request through the `DelegateSCACancelNotification` API.

```
{  
    "NotificationId": "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
    "PubToken": "123456789",  
    "DelegateMethod": "push-confirmation",  
    "FinancialInstitutionId": "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
    "Language": "en-EN",  
    "DelegateScaId": "bcd507g1-7ec8-43b4-8a07-6c5e17078967",  
    "CardScheme": "MasterCard",  
    "CreatedMode": "GA",  
    "Device": {  
        "Channel": "BROWSER",  
        "Ip": "string",  
        "Language": "en-EN"  
    },  
    "MerchantInfo": {  
        "Id": "mer-12345",  
        "Name": "Amazon",  
        "Country": "840",  
        "Url": "https://amazon.com   ",  
        "ChallengePreference": "no-preference",  
        "RedirectAppUrl": "merchantScheme://appName?transID=b2385523-a66c-4907-ac3c-91848e8c0067"  
    },  
    "TransactionInfo": {  
        "Type": "payment",  
        "ProtocolVersion": "1.0.2",  
        "Channel": "app",  
        "DsTransactionId": "98315a91-e0b6-4fe0-8842-9ed82ea8ef0b",  
        "Date": "2023-08-17T10:35:32.061Z",  
        "Amount": "12345",  
        "Currency": {  
            "Code": "978",  
            "Exponent": "2"  
        },  
        "Recur": {  
            "Frequency": "30",  
            "EndRecur": "20221212"  
        },  
        "Install": "5"  
    },  
    "DelegateStatus": "Cancelled"  
}
```

#### Your Response

Upon receipt of a cancellation request, your systems return a 200-HTTP response code (OK/success). If there is an error, your systems return a 400-HTTP response code.