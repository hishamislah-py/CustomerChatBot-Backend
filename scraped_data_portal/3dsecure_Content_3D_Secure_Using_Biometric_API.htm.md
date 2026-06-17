# 15 Using the Biometric/In-App Authentication API

REST-based API are used to initiate a Biometric or In-App OOB authentication session and provide the result. The body of the message is in JSON format. Two API are used to support Biometric/In-App authentication:

* `NotifyInitiateAction` â sent by Thredd to notify you to set up an authentication session
* `NotifyValidate` â you use this to send the authentication result to Thredd.

## 15.1 Initiating a Biometric Session

When Thredd receives a request for Biometric/In-App authentication from Cardinal, we use the `NotifyInitiateAction` API to send your system a request to initiate an authentication session. This request is sent to the `NotifyInitiateAction` endpoint you specified in the 3DS Product Setup Form (see [Completing your 3DS Product Setup Form](Completing_the_PSF.htm).

See the example below:

#### Thredd Request

[Copy](javascript:void(0);)

```
{"Pubtoken":812561666,  
"GPSInitiateActionID":"ade509f0-7ea8-43a4-8c07-6c5e17076987",  
"MessageVersion3DS":"1.0.2",  
"Credential":{  
    "Id":"000000000000000000000000000000000669",  
    "Type":"BIOMETRIC",  
    "Text":"TEST_BIOMETRIC_OTP_VALUE"  
    },  
"ChannelCreated":"GA",  
"MerchantInfo":{  
    "AcquirerID":"5555555",  
    "MerchantID":"12345678",  
    "MerchantName":"Amazon",  
    "MerchantURL":"https://www.amazon.com",  
    "MerchantCategoryCode":null,  
    "MerchantCountryCode":"UK"  
    "MerchantAppRedirectURL":"merchantScheme://appName?translD=b2385523-a66c-4907ac3c-91848e8c0067"  
    },  
"TransactionInfo":{  
    "TransactionTimeStamp":"2020-08-17T10:35:32.061Z",  
    "TransactionAmount":1000,  
    "TransactionCurrency":"826",  
    "TransactionExponent":2  
    }  
}
```

#### Notes

Thredd token of the card to authenticate:

> [Copy](javascript:void(0);)
>
> ```
> {"Pubtoken":812561666,
> ```

The last digits are the credential Id for this card `669`:

> [Copy](javascript:void(0);)
>
> ```
>     "Id":"000000000000000000000000000000000669",
> ```

Merchant and transaction details. You can optionally configure your app to confirm any of these details during the Biometric authentication:

> [Copy](javascript:void(0);)
>
> ```
>     "MerchantName":"Amazon",  
>     MerchantURL":"https://www.amazon.com",  
>     "MerchantCategoryCode":null,  
>     "MerchantCountryCode":"UK"  
>     "MerchantAppRedirectURL":"merchantScheme://appName?translD=b2385523-a66c-4907ac3c-91848e8c0067"
> ```

> [Copy](javascript:void(0);)
>
> ```
>     "TransactionTimeStamp":"2020-08-17T10:35:32.061Z",  
>     "TransactionAmount":1000,  
>     "TransactionCurrency":"826",  
>     "TransactionExponent":2
> ```

For more information on the fields in the request, see [NotifyInitiateAction Message Fields](../Reference/Biometric_OOB_Fields.htm#_NotifyInitiateAction_Message_Reques).

#### Your Response

Upon receipt of a request, your systems should return a 200-HTTP response code.

Thredd does not resend the request if the 200-HTTP response to the `NotifyInitiateAction` request is not received. The authentication session will time out if Thredd does not receive your `NotifyValidate` request. See [Validation Timeout](#_Validation_Timeout).

When your systems receive the `NotifyInitiateAction` request, you can optionally use the Thredd oAuth server to validate the token, to confirm it is from Thredd. See [Validating the Token (optional)](#_Validating_the_Token)

The customer should then be prompted to open your Smart device customer application and authenticate themselves with the supported Biometric method (e.g., fingerprint or face recognition) or In-App method.

#### Validating the Token (optional)

Thredd passes the bearer token in the header of the `NotifyInitiateAction` request, as shown in the example below.

[Copy](javascript:void(0);)

```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjE5ODI3Q0E4M0NEMkNGNUUzMTAxMUVBQkQ0N0ZDNTg4RkMyRjQ3RTIiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJHWUo4cUR6U3oxNHhBUjZyMUhfRmlQd3ZSLUkifQ.eyJuYmYiOjE2MDc1MzM1NzksImV4cCI6MTYwNzU0Nzk3OSwiaXNzIjoiaHR0cHM6Ly9vYXV0aHVhdC5nbG9iYWxwcm9jZXNzaW5nLm5ldCIsImF1ZCI6WyJyZHhhcGkiLCJmaXJiaW9tZXRyaWNhcGkiXSwiY2xpZW50X2lkIjoiZmlyYmlvIiwic2NvcGUiOlsiY2xpZW50X3ZhbGlkYXRlIiwiZmlyYmlvbWV0cmljYXBpIl19.owfqYt7Rf6zHMLY2HT3j0RH7Lti05oWkp-bJ41QF1LZyqxaRMZWJAUxuRXJwIWrG2wtC0Q1KFzVPbZhpwKAwJvQTIymJFhryEvRUGTQqM61Nwu_Dnsx8H-Jpi7_0PjQk4MaAhqFv6MEgDMHvxUZ2_Q6vYj_-h2rRDunHjBvhvA55-yGLdqxeHRtNvHJQCsaVZHdLBngUpeFpWcvrbhk1SYbNlGlflYBm5aAX_YDwpWt4p_M6w7TAYJZQvc4Hi_NqAZwUOY7xOlhVD69onUmd74k6nt0ncowGgC3naWQieqcVMd3B1kCAnnYZfLlXMhSxeN_XqWtjKTK3WMavYj6vrw
```

You can optionally verify the token (check that it is valid and active) using the oAuth introspect API endpoint. See [Using the Thredd oAuth Server](Using_Oauth.htm).

The token expires after 4 hours (14400 seconds).

## 15.2 Notifying Thredd of the Result of the Biometric Session

When authentication is complete, you must use the `NotifyValidate` REST API to send the authentication outcome to Thredd.

#### API Endpoints

UAT: *https://vcasuat.globalprocessing.net/api/v1/NotifyValidate*

Production:  
PRDZ: *https://p0ivcas.globalprocessing.net/api/v1/NotifyValidate*

PRD1: *https://p1ivcas.globalprocessing.net/api/v1/NotifyValidate*

PRD2: *https://p2ivcas.globalprocessing.net/api/v1/NotifyValidate*

See the example JSON message below:

#### Your Request

[Copy](javascript:void(0);)

```
{"Pubtoken":987654321,  
"ProgMgrCode":"ABC",  
"GPSInitiateActionID":"e459b9d8-9703-43a4-bf71-9426fc235c25",  
"PMReferenceID":"637441368856932254",  
"Status":"SUCCESS",  
"Error":null}
```

#### Notes

Thredd token of the card that was authenticated:

> [Copy](javascript:void(0);)
>
> ```
> {"Pubtoken":987654321,
> ```

The result of your authentication: SUCCESS, STEPUP, FAILURE, FAILWITHFEEDBACK or ERROR:

> [Copy](javascript:void(0);)
>
> ```
> "Status":"SUCCESS",
> ```

#### Thredd Response

[Copy](javascript:void(0);)

```
{"Pubtoken":987654321,  
"GPSInitiateActionID":"e459b9d8-9703-43a4-bf71-9426fc235c25",  
"PMReferenceID":"637441368856932254",  
"Status":"SUCCESS",  
"Error":{  
    "ReferenceNumber":"",  
    "Description":"",  
    "Message":""}  
}
```

If the cardholder authenticates successfully, you must return the status of SUCCESS. If the cardholder was unable to use the requested authentication method (e.g., Biometric/In-App) you can use the STEPUP status to trigger the fallback option configured for the card (Note that STEPUP will only work if your cards have been enroled for a fallback option, such as, OTP SMS).

For more information on the fields in the request and response, see [NotifyValidate Message Fields](../Reference/Biometric_OOB_Fields.htm#_NotifyValidate_Message_Fields).

If there was any error in your request (e.g., invalid JSON format or incorrect details), Thredd will return details of the error.

Thredd returns the result to Cardinal. For a successful authentication, the transaction proceeds to authorisation. For a failed or timed out authentication, Cardinal will show the Fail with Feedback screen.

#### Validation Timeout

When Thredd sends the `NotifyInitiateAction` message to your system, Thredd expects to receive back a `NotifyValidate` response from your system within the validation timeout period (default is 30 seconds and is configurable up to 900 seconds)[1  This period starts from when Thredd sends the NotifyInitiateAction message up to receiving the NotifyValidate.](#).

If Thredd does not receive the `NotifyValidate` response within this period, the authentication session times out. In this case, Cardinal will show the Fail with Feedback screen to the cardholder.