# 18 Using the Delegated SMS API

The delegated SMS API allows you to receive the validated OTP details for the cardholder from Thredd. This allows you to set up an OTP authentication session with the cardholder. Thredd provides you with a request in the `DelegateOTPNotification` endpoint containing details of the transaction, the merchant and the OTP. You send a response back to Thredd in order to acknowledge that you received the OTP.

## 18.1 DelegateOTPNotification Request

The following is an example request.

```
{  
  "NotificationId" : "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
  "PubToken": "123456789",  
  "DelegateMethod": "otp-sms",  
  "FinancialInstitutionId": "f88458df-20ea-49b7-b890-119c2f5e8c6e",  
  "Language": "en-EN",    
  "CardScheme": "MasterCard",   
  "Device": {  
    "Channel": "BROWSER",  
    "Ip": "127.0.0.1",  
    "Language": "en-EN"  
  },  
  "MerchantInfo": {  
    "Id": "mer-12345",  
    "Name": "Amazon",  
    "Country": "840",  
    "Url": "https://amazon.com"  
    "ChallengePreference": "delegate-otp",  
    "RedirectAppUrl": "https://amazon.com"  
  },  
  "TransactionInfo": {  
    "Type": "payment",  
    "ProtocolVersion": "1.0.2",  
    "Channel": "app",  
    "Token": "a98846d1-b694-4c85-9840-64ed56bc7c70",  
    "DsTransactionId": "98315a91-e0b6-4fe0-8842-9ed82ea8ef0b",  
    "Date": 1632990584,  
    "ChallengedAt": 1650696156,  
    "ChallengeExpiresAfter": 300,  
    "ChallengeExpiry": 1650696456,  
    "ChallengeMethod": "sms-otc"  
    "Amount": "123.45",  
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
  "Passcode": "xxxxxx",  
  "MobileNumber": "+911234",  
  "MessageContent": "xxxxxx is the One Time Passcode required for completing a purchase of EUR xxxxx.xxxxx at Amazon with the last four digits of your card ending in xxxxx. Please use the One Time Passcode to complete the transaction."  
}
```

#### Your Response

Upon receipt of a request, your systems return a 200-HTTP response code (OK).

A successful response appears as follows:

```
{  
"status": "ok"  
}
```

An error response appears as follows:

```
{  
"error": "error_message"  
}
```