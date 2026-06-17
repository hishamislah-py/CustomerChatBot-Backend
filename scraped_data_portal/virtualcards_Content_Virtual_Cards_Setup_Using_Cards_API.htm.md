# 4 Using the Cards API (REST)

The Thredd Cards API can be used to create physical or virtual cards, regenerate virtual card images and retrieve virtual card details using our REST service. For a full description, see the [Cards API Website](https://cardsapidocs.thredd.com/). Below is a summary.

Thredd provides two alternative API for creating and managing cards: REST-based Cards API or SOAP web services. This page describes use of the REST-based Cards API. If you are using our SOAP web services, see [Using Web Services (SOAP API)](Using_the_Web_Services_API.htm).

## 4.1 Create a Card

Use the [Create Card](https://cardsapidocs.thredd.com/docs/create-card-2) API to create both virtual cards and physical cards.

See the example code snippet below: (only key fields are shown)

[Copy](javascript:void(0);)

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{  
     "cardHolder": {  
          "title": "Mr",  
          "firstName": "Jon",  
          "lastName": "Smith",  
          "dateOfBirth": "1982-11-03"  
     },  
     "address": {  
          "addressLine1": "32 Western Drive",  
          "postCode": "S25 2BZ",  
          "country": "GBR"  
     },  
     "virtualCardImageDetails": {  
          "virtualCardImageId": "4155",  
          "imageSize": 1  
     },  
     "cardType": "Virtual",  
     "cardProduct": 10005,  
     "activateNow": true,  
     "designId": "New Card Brand",  
     "customerReference": "my ref 12345",  
     "activateNow": true  
}
```

#### Response Code Snippet Example

Below is an example of the response to the create card request.

[Copy](javascript:void(0);)

```
1
2
3
4
5
6
7
8
{  
    "publicToken": "103169946",  
    "customerReference": "CustNo12345A",  
    "embossName": "Mr John Smith",  
    "maskedPan": "999999******0134",  
    "startDate": "2023-02-28",  
    "expiryDate": "2026-02-27"  
}
```

#### Notes

* `<PublicToken>` is the unique 9-digit internal Thredd token that can be used for all REST-based API queries on the card.

## 4.2 Retrieving a Card

Use the [Retrieve Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card) API to return information on a card.

See the code snippet below for an example of the response returned by the Retrieve Card endpoint.

[Copy](javascript:void(0);)

```
{  
    "cardType": "Physical",  
    "publicToken": "638050230",  
      "status": "Active",  
    "cardStatusCode": "00",  
    "cardStatusDescription": "00 (Active)",  
    "balance": {  
        "currencyCode": "GBP",  
        "cardBalance": 300.67,  
        "pendingAmount": -74,  
        "availableBalance": 226.67  
    },  
    "cardDetails": {  
        "customerReference": "CustNo12345A",  
        "fullNameOnCard": "Mr. Bruce Simms",  
        "maskedPan": "531610******0462",  
        "startDate": "2023-10-23",  
        "expiryDate": "2028-10-31",  
        "clearPan": null,  
        "cvv": null,  
        "activationDate": "2024-05-14 08:31:33Z"  
    },  
    "cardHolder": {  
        "title": "Mr",  
        "firstName": "John",  
        "middleName": "",  
        "lastName": "Smith",  
        "dateOfBirth": "1963-11-22",  
        "mobile": "",  
        "email": ""  
    },  
    "cardProduct": {  
        "scheme": "Sandbox Scheme",  
        "product": 1234,  
          "productShortName": "Sandbox",  
        "ehiMode": 1  
    },  
    "controlGroups": {  
        "limitsGroup": 1,  
        "usageGroup": 0,  
        "recurringFeeGroup": 0,  
        "webServiceFeeGroup": -1,  
        "authFeeGroup": 0,  
        "mccGroup": 0,  
        "cardLinkageGroup": 0,  
        "calendarGroup": -1,  
        "fxGroup": 0,  
        "paymentTokenUsageGroup": 0,  
          "cardAcceptorAllowList": 0,  
        "cardAcceptorDisallowList": 0  
    },  
    "3DS": [],  
    "designId": "Sandbox",  
      "childCards": [],  
    "siblingCards": [],  
    "address": {  
        "addressLine1": "32 Eastern Lane",  
        "addressLine2": "",  
        "addressLine3": "",  
        "city": "",  
        "state": "",  
        "county": "",  
        "postCode": "S11 7AA",  
        "country": "826"  
    },  
    "fulfilment": {  
        "addressLine1": "32 Eastern Lane",  
        "addressLine2": "",  
        "addressLine3": "",  
        "city": "",  
        "state": "",  
        "county": "",  
        "postCode": "S11 7AA",  
        "country": "826"  
    },  
      "freetext1": "Comments for the card manufacturer here",  
   "freetext2": "And in this field too.",  
   "IsSingleUse" : "true",  
   "IsNonReloadable" : "false",  
   "cardAcceptorIds": {  
        "allowCardAcceptors": [],  
        "disallowCardAcceptors": []  
    },  
    "language3ds": null,  
     "programManagerID": 78,  
    "programManagerCode": "PMT"  
}
```

## 4.3 Converting a Virtual Card to a Physical Card

When you convert a virtual card to a physical card it will adopt the same settings as the virtual card. The card is created with the same PAN[1  Thredd has an option to generate a different PAN on card convert; we recommend that if you require different PANs, you ask your implementation manager to set this up as separate card products. See Virtual Card Setup.](#). A new expiry date and CVV2 are generated if the conversion falls in a different calendar month to the virtual card creation. The card instructions are sent to your card manufacturer for printing and despatch to the cardholder.

Following successful conversion, any replacement or renewal cards are generated as physical cards. The cardholder can still continue to use their virtual card until the physical card is activated, after which the virtual card will stop working.

#### How to convert a card

* Prior to converting the card, you should update any cardholder details, using the [Update Card](https://cardsapidocs.thredd.com/docs/updating-a-card) API. For details, see the [Cards API Website](https://cardsapidocs.thredd.com/).
* To convert the card, you can use the [Convert Card](https://cardsapidocs.thredd.com/docs/converting-a-card) API.

See the example code snippet below: (only key fields are shown)

[Copy](javascript:void(0);)

```
{  
  "cardType": "Physical",  
  "moveExpiryDate": true  
}
```

#### Response Code Snippet Example

Below is an example of the response to the convert card request.

[Copy](javascript:void(0);)

```
{  
    "cardType": "Physical",  
    "expiryDate": "2023-05"  
}
```

### 4.3.1 Activating the Physical Card

Where a virtual card has been activated, the physical card will also be active in transit. We therefore recommend you set the status of the physical card to inactive and enforce virtual only usage until the cardholder has received their card and activated it.

You should use the Update Card Status API to activate the physical card.

### 4.3.2 Retrieve Card Details

You can retrieve card details by using the [Retrieve Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card) endpoint.

You can retrieve card details by making a GET request to the Retrieve Card endpoint. For example, {{base-url}}/cards/{{publicToken}}

A successful response will return a HTTP 200 response code. Below is an example response:

[Copy](javascript:void(0);)

```
{  
    "cardType": "Virtual",  
    "publicToken": "103170278",  
    "status": "Inactive",  
    "cardStatusCode": "02",  
    "cardStatusDescription": "02 (Inactive)",  
    "balance": {  
        "currencyCode": "GBP",  
        "cardBalance": 0,  
        "pendingAmount": 0,  
        "availableBalance": 0  
    },  
    "cardDetails": {  
        "customerReference": "my ref 12345",  
        "fullNameOnCard": "Mr Jon Smith",  
        "maskedPan": "999999******3589",  
        "startDate": "2024-03-21",  
        "expiryDate": "2034-03-31",  
        "clearPan": null,  
        "cvv": null  
    },  
    "cardHolder": {  
        "title": "Mr",  
        "firstName": "Jon",  
        "middleName": "",  
        "lastName": "Smith",  
        "dateOfBirth": "1982-11-03",  
        "mobile": "",  
        "email": ""  
    },  
    "cardProduct": {  
        "scheme": "GPS VIRTUAL SCHEME TEST",  
        "product": 10005,  
        "productShortName": "GPSDUMMY"  
    },  
    "controlGroups": {  
        "limitsGroup": 1201,  
        "usageGroup": 0,  
        "recurringFeeGroup": 0,  
        "webServiceFeeGroup": 0,  
        "authFeeGroup": 1137,  
        "mccGroup": 0,  
        "cardLinkageGroup": 0,  
        "calendarGroup": 0,  
        "fxGroup": 0,  
        "paymentTokenUsageGroup": 20,  
        "cardAcceptorAllowList": null,  
        "cardAcceptorDisallowList": null  
    },  
    "3DS": [],  
    "designId": "New Card Brand",  
    "childCards": [],  
    "siblingCards": [],  
    "address": {  
        "addressLine1": "32 Western Drive",  
        "addressLine2": "",  
        "addressLine3": "",  
        "city": "",  
        "state": "",  
        "county": "",  
        "postCode": "S25 2BZ",  
        "country": "826"  
    },  
    "fulfilment": {  
        "addressLine1": "32 Western Drive",  
        "addressLine2": "",  
        "addressLine3": "",  
        "city": "",  
        "state": "",  
        "county": "",  
        "postCode": "S25 2BZ",  
        "country": "826"  
    },  
    "freetext1": null,  
    "freetext2": null,  
    "isSingleUse": null,  
    "isNonReloadable": null,  
    "cardAcceptorIds": {  
        "allowCardAcceptors": [],  
        "disallowCardAcceptors": []  
    },  
    "language3ds": "en-GB"  
}
```