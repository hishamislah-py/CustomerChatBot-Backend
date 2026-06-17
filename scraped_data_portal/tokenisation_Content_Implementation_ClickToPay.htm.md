# Click to Pay

Click to Pay is a service that provides customers with a frictionless online experience during checkout. Issuers can register for this service on behalf of their customers. A merchant can display details of Click to Pay-registered cards by using only the cardholderâs name and email/phone number during checkout. Thredd approves all Click to Pay tokenisation requests if Click to Pay is selected on your PSF.

Click to Pay uses the token instead of the card PAN at checkout, and avoids manual card entry for the cardholder. It also means there is a lower security risk, as the merchant never sees the cardholder's card details.

![](../Resources/Images/Click-to-pay.png)

Figure 17: Flow diagram displaying how Click to Pay works

You can enrol cardholders onto Click to Pay using the Enroll Data endpoint. This endpoint enables you to register the new cardholder, phone number, email, and card linked to their token. If you want to add additional details to a previously enrolled card, you can use the Enroll Payment Instruments endpoint. Note you must register the cardholder using the Enroll Data endpoint before you can use the Enroll Payment Instruments endpoint.

## Enroll Data

You can register a cardholder to use Click to Pay by making a POST request to the Enroll Data endpoint. For example:

[Copy](javascript:void(0);)

```
{{base-url}}/ctp/api/v1/enrolldata
```

The POST body should include the details of the customer and their publicToken. The below is an example of what the body should look like:

[Copy](javascript:void(0);)

```
{  
  "customers": [  
    {  
      "customerDetails": {  
        "billingAddress": {  
          "city": "San Francisco",  
          "state": "CA",  
          "country": "USA",  
          "postalCode": "94105",  
          "addressLine1": "1000 Market Street",  
          "addressLine2": "Building 56",  
          "addressLine3": "Suite 101"  
        },  
        "customerReferenceId": "ImACustomer",  
        "email": "jbloggs@email.com",  
        "phone": "16504005555",  
        "firstName": "John",  
        "middleName": "Robert",  
        "lastName": "Bloggs",  
        "nationalIdentifiers": [  
          {  
            "type": "PASSPORT",  
            "value": "A123456"  
          }  
        ]  
      },  
      "pubTokens": [  
        {  
          "value": "123456789"  
        }  
      ]  
    }  
  ]  
}
```

If successful, a 202 response is returned with the unique requestTraceId. See the following example of a successful response.

[Copy](javascript:void(0);)

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

For more information on the Enroll Data endpoint, see [Enroll Data](https://cardsapidocs.thredd.com/v2/docs/enroll-data) and [Enroll Data - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/enroll-data-field-descriptions).

## Enroll Payment Instruments

The Enroll Payment Instruments endpoint is for Visa cards only.

You can add more Click to Pay details to a card by making a POST request to the Enroll Payment Instruments endpoint. For example:

[Copy](javascript:void(0);)

```
{{base-url}}/ctp/api/v1/enrollpaymentinstruments
```

The POST body should include the details of the customer, their publicToken and their billing address. The below is an example of what the body should look like.

[Copy](javascript:void(0);)

```
{  
  "billingAddress": {  
    "city": "San Francisco",  
    "state": "CA",  
    "country": "USA",  
    "postalCode": "94105",  
    "addressLine1": "1000 Market Street",  
    "addressLine2": "Building 56",  
    "addressLine3": "Suite 101"  
  },  
  "customerReferenceId": "ImACustomer",  
  "pubTokens": [  
    {  
      "value": "123456789"  
    }  
  ]  
}
```

If successful, a 202 response is returned with the unique requestTraceId. See the following example of a successful response.

[Copy](javascript:void(0);)

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

For more information on the Enroll Payment Instruments endpoint, see [Enroll Payment Instruments](https://cardsapidocs.thredd.com/v2/docs/enroll-payment-instruments) and [Enroll Payment Instruments - Field Descriptions](https://cardsapidocs.thredd.com/v2/docs/enroll-payment-instruments-field-descriptions).

## Get Payment Instrument Information

The Get Payment Instrument Information endpoint is for Mastercard only.

The Get Payment Instrument Information endpoint enables you to return information on a payment instrument for a card enrolled onto Click to Pay. A payment instrument refers to the method or device through which a consumer can make a payment using the Click to Pay service.

You can return payment instrument information by making a GET request to the Get Payment Instrument Information endpoint, including the `customerReferenceId` and `publicToken`. For example:

```
{{base-url}}/ctp/api/v1/paymentinstrument/{customerReferenceId}/{publicToken}
```

If successful, a 200 response is returned with details of the payment instrument. For example.

```
{  
  "intent": {  
    "type": "PRODUCT_CODE",  
    "value": "CLICK_TO_PAY"  
  },  
  "paymentInstrument": {  
    "type": "CARD",  
    "cardType": "CREDIT",  
    "status": "ACTIVE",  
    "issuerName": "Bank A",  
    "nameOnCard": "John Doe",  
    "accountNumber": "4111111145551140",  
    "tokenDetails": {  
      "tokenReferenceId": "DM4MMC1US0000000a8513863213e4f1b99e4d016b4f61624"  
    },  
    "billingAddress": {  
      "city": "San Francisco",  
      "state": "CA",  
      "country": "USA",  
      "postalCode": "94105",  
      "addressLine1": "1000 Market Street",  
      "addressLine2": "Building 56",  
      "addressLine3": "Suite 101"  
    },  
    "expirationDate": "2030-01",  
    "paymentAccountReference": "5001DW4DS6FRSHVXVBC7HVP6JYAS6"  
  }  
}
```

For more information on the Get Payment Instrument Information endpoint, see [Get Payment Instrument Data](https://cardsapidocs.thredd.com//v2.0/reference/get-payment-instrument-data/) and [Get Payment Instrument Information - Field Descriptions](https://cardsapidocs.thredd.com/v2.0/docs/get-payment-instrument-information-field-descriptions).

## Manage Payment Instrument

The Manage Payment Instrument endpoint enables you to update existing payment instrument details, specifically the instruments billing address, created from the Enroll Payment Instrument endpoint.

You can manage a payment instrument by making a PUT request to the Manage Payment Instrument endpoint. For example:

```
{{base-url}}/ctp/api/v1/paymentinstrument
```

The Manage Payment Instrument request replaces the whole payment instrument object, so all fields are required in the request body. See the below example of a request:

```
{  
 "customerReferenceId": 1234,  
 "pubToken": 275797862,   
 "billingAddress": {  
    "city": "San Francisco",  
    "state": "CA",  
    "country": "USA",  
    "postalCode": 94105,  
    "addressLine1": "1000 Market Street",  
    "addressLine2": "Building 56",  
    "addressLine3": "Suite 102"  
  },  
  
}
```

If successful, a 202 response is returned with a unique `requestTraceId` when the card network is VISA, and a unique `srcCorrelationId` when the card network is Mastercard.

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

```
{  
  "srcCorrelationId": "b17b686c-4759-4ade-a3b1-6b29c61b6774"  
}
```

For more information on the Manage Payment Instrument endpoint, see [Manage Payment Instrument](https://cardsapidocs.thredd.com//v2.0/reference/manage-payment-instrument) and [Manage Payment Instrument - Field Descriptions](https://cardsapidocs.thredd.com/v2.0/docs/manage-payment-instrument-field-descriptions).

## Manage Consumer Information

The Manage Consumer Information endpoint enables you to update consumer information created from the Enroll Data endpoint.

You can update consumer information by making a PUT request to the Manage Consumer Information endpoint. For example:

```
{{base-url}}/ctp/api/v1/consumerinformation
```

The request must consist of all fields, including any fields that do not require updating. If a field is missing from the request, the request fails.

See the below example of a request body.

```
{  
  "customerDetails": {  
    "nationalIdentifiers": [  
      {  
        "type": "PASSPORT",  
        "value": "A123456"  
      }  
    ],  
    "customerReferenceId": "63421837-d597-4f0f-89e4-930c1a7b9e85",  
    "email": "alex123@hotmail.com",  
    "phone": "16504005555",  
    "firstName": "Alex",  
    "middleName": "Robert",  
    "lastName": "Miller",  
    "countryCode": "USA"  
  },  
  "cardNetwork": "Visa"  
}
```

If successful, a 202 response is returned with a unique `requestTraceId` when the card network is VISA, and a unique `srcCorrelationId` when the card network is Mastercard.

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

```
{  
  "srcCorrelationId": "b17b686c-4759-4ade-a3b1-6b29c61b6774"  
}
```

For more information on the Manage Consumer Information endpoint, see [Manage Consumer Information](https://cardsapidocs.thredd.com//v2.0/reference/manage-consumer-information) and [Manage Consumer Information - Field Descriptions](https://cardsapidocs.thredd.com/v2.0/docs/manage-consumer-information-field-descriptions).

## Delete Consumer Information

You can remove consumer information by making a DELETE request to the Delete Consumer Information endpoint

```
{{base-url}}/ctp/api/v1/consumerinformation/{customerReferenceId}
```

If successful, a 202 response is returned with a unique `requestTraceId` when the card network is VISA, and a unique `srcCorrelationId` when the card network is Mastercard.

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

```
{  
  "srcCorrelationId": "b17b686c-4759-4ade-a3b1-6b29c61b6774"  
}
```

For more information on the Delete Consumer Information endpoint, see [Delete Consumer Information.](https://cardsapidocs.thredd.com//v2.0/reference/delete-consumer-information)

## Delete Payment Instrument

You can delete a payment instrument by making a DELETE request to the Delete Payment Instrument endpoint. For example

```
{{base-url}}/ctp/api/v1/paymentinstrument/{customerReferenceId}/{publicToken}
```

If successful, a 202 response is returned with a unique `requestTraceId` when the card network is VISA, and a unique `srcCorrelationId` when the card network is Mastercard

```
{  
  "requestTraceId": "351562ba-83cf-11ee-b962-0242ac120002"  
}
```

```
{  
  "srcCorrelationId": "b17b686c-4759-4ade-a3b1-6b29c61b6774"  
}
```