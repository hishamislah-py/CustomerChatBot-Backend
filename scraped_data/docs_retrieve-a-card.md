# Retrieve a Card

The Retrieve Card endpoint enables you to return details for a card based on the <Glossary>Public Token</Glossary> in the URL. A successful response includes details of the card status, the current balance, and the control groups the card is associated with.

You can retrieve card details by making a GET request to the Retrieve Card endpoint. For example:

```json Example Retrieve a Card endpoint
{{base-url}}/cards/{{publicToken}}
```

A successful response returns a HTTP 200 response code. Below is an example response:

```json Example Retrieve a Card response
{
    "cardType": "Physical",
    "publicToken": "118834053",
    "status": "Active",
    "cardStatusCode": "00",
    "cardStatusDescription": "00 (Active)",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr Johnny Bruce",
        "maskedPan": "999999******1350",
        "startDate": "2025-02-17",
        "expiryDate": "2035-01-31",
        "clearPan": null,
        "cvv": null,
        "activationDate": "2025-02-17 08:29:30Z",
        "gpsExpiryDate": "2028-02-17"
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "John",
        "middleName": "Bruce",
        "lastName": "Bloggs",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "jbloggs@email.com"
    },
    "cardProduct": {
        "scheme": "GPS SCHEME TEST",
        "product": 10023,
        "productShortName": "GPSDUMMY",
        "productName": "GPS Test REST API",
        "ehiMode": 3,
        "networkId": 0
    },
    "controlGroups": {
        "limitsGroup": 1051,
        "usageGroup": 374,
        "recurringFeeGroup": null,
        "webServiceFeeGroup": null,
        "authFeeGroup": null,
        "mccGroup": null,
        "cardLinkageGroup": 53,
        "calendarGroup": null,
        "fxGroup": null,
        "paymentTokenUsageGroup": null,
        "cardAcceptorAllowList": null,
        "cardAcceptorDisallowList": null,
        "limitedNetworkGroup": null
    },
    "3DS": [],
    "designId": "PMTREST",
    "childCards": [],
    "siblingCards": [],
    "address": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "SW11 2LD",
        "country": "826"
    },
    "fulfilment": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "SW11 2LD",
        "country": "826"
    },
    "freetext1": "Comments for the card manufacturer here",
    "freetext2": "And in this field too.",
    "isSingleUse": false,
    "isNonReloadable": false,
    "networkSharingOptOut": false,
    "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    },
    "language3ds": "en-GB",
    "programManagerID": 78,
    "programManagerCode": "PMT",
    "oobAppUrl": null,
    "isMultiFx": false,
    "isMfxPrimary": false
}
```

> 👍 API Explorer
>
> See the [Retrieve a Card](https://cardsapidocs.thredd.com/reference/retrieve-card) endpoint for more information.