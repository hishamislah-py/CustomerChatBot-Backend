# Bulk Create Physical Cards

> 📘 Note
>
> This endpoint is for physical cards only. Bulk creation of virtual cards will be available in a future release.

The Bulk Create Physical Cards endpoint enables you to create in bulk a number of non personalised cards (For example, creating gift cards, or rolling out new products) in a single request. Cards created by the Bulk Create Cards endpoint can be viewed in the Get Bulk Cards endpoint.

> 📘 Note
>
> A maximum of 1000 cards can be created in one request.

You can bulk create cards by making a POST request to the Bulk Create Physical Cards endpoint. For example:

```json Example Bulk Create Physical Cards endpoint
{{base-url}}/cards/bulk
```

The request body must include the unique product id that the cards are going to be created against, the quantity of cards being created, and at least the first line and postcode of the fulfilment address. The following example shows ten cards being created for the product id 10003:

```json Example Bulk Create Physical Cards body
{
  "cardProduct": 10003,
  "quantity": 10,
  "nameOnCard": "Thredd",
  "imageId": "101",
  "deliveryMethod": "StandardDelivery",
  "fulfilmentAddress": {
    "addressLine1": "32 Eastern Road",
    "city": "Sheffield",
    "county": "South Yorkshire",
    "postCode": "S11 8AA",
    "country": "GBR"
  },
}
```

If successful, a 202 response is returned with a unique bulk card generation id. This should be included in the Get Bulk Cards endpoint.

```json Example Bulk Create Physical Cards response
{
  "id": "123456"
}
```

> 👍 API Explorer
>
> For more information on the Bulk Create Physical Cards endpoint, see [Bulk Create Physical Cards](https://cardsapidocs.thredd.com/reference/create-bulk-cards) in the API Explorer.

## Get Bulk Cards Status

The Get Bulk Cards Status endpoint enables you to retrieve the current status of the bulk card creation process using the unique identifier output from a successful Bulk Create Physical Cards response.

You can retrieve bulk created cards by making a GET request to the Get Bulk Cards endpoint and adding the unique identifier to the endpoint URL. For example:

```json Example Get Bulk Cards endpoint
{{base-url}}/cards/bulk?bulkCardRequestId=123456
```

If successful, a 200 response is returned with the current status of the bulk create process.

```json Example Get Bulk Cards response
{
    "status": "Complete"
}
```

> 👍 API Explorer
>
> For more information on the Get Bulk Cards endpoint, see [Get Bulk Cards Status](https://cardsapidocs.thredd.com/reference/gets-the-bulk-card-progress) in the API Explorer.

## Get Bulk Tokens

The Get Bulk Tokens endpoint enables you to retrieve the public tokens created from a bulk card process using the unique identifier output from a successful Bulk Create Card response.

You can retrieve bulk card tokens by making a GET request to the Get Bulk Tokens endpoint, adding the unique Bulk Create Card identifier, the page number, and the page size to the endpoint URL.

For example if you created 20 public tokens using the Bulk Create Physical Cards endpoint, if you set the pageSize to 10 and the pageNumber to 1, the response would return the first 10 tokens created. If you wanted to see the 2nd 10, you would need to changed the pageNumber value to 2.

The below example shows a `bulkCardRequestId` of `24060`, a `pageNumber` of `2`, and a `pageSize` of `1`.

```json Example Get Bulk Tokens endpoint
{{base-url}}/cards/bulk/tokens?bulkCardRequestId=24060&pageNumber=2&pageSize=1
```

If successful, a 200 response is returned with the bulk created public tokens displayed, as well as the page number, page size and the total amount of tokens generated.

```json Example Get Bulk Tokens response
{
    "tokens": [
        115794151,
        123456789
    ],
    "pageNumber": 2,
    "total": 4,
    "pageSize": 2
}
```

> 👍 API Explorer
>
> For more information on the Get Bulk Tokens endpoint, see [Get Bulk Tokens](https://cardsapidocs.thredd.com/reference/gets-the-bulk-card-tokens) in the API Explorer.

## Bulk Create Card Details

You can view the details of a bulk created card by using the Retrieve Card endpoint after you have received the token from the Get Bulk Tokens endpoint. Bulk created cards will need to be activated before it can be used. You can activate a card by using the [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status-deprecated) endpoint and setting the card's status to `00`.

See below for an example bulk created card.

```json Example Bulk Created Card
{
    "cardType": "Physical",
    "publicToken": "115954570",
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
        "customerReference": "638452414641050611",
        "fullNameOnCard": "PERSONALISED",
        "maskedPan": "999999******4397",
        "startDate": "2024-03-05",
        "expiryDate": "2027-04-30",
        "clearPan": null,
        "cvv": null
    },
    "cardHolder": {
        "title": "",
        "firstName": "",
        "middleName": null,
        "lastName": "",
        "dateOfBirth": "1900-01-01",
        "mobile": "",
        "email": ""
    },
    "cardProduct": {
        "scheme": "GPS SCHEME TEST",
        "product": 10003,
        "productShortName": "GPSDUMMY"
    },
    "controlGroups": {
        "limitsGroup": 2731,
        "usageGroup": 1081,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": 0,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0,
        "cardAcceptorAllowList": null,
        "cardAcceptorDisallowList": null
    },
    "3DS": [],
    "designId": "PMTCGP",
    "childCards": [],
    "siblingCards": [],
    "address": {
        "addressLine1": "",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": null,
        "county": null,
        "postCode": "",
        "country": ""
    },
    "fulfilment": {
        "addressLine1": "",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": null,
        "county": "",
        "postCode": "",
        "country": ""
    },
    "freetext1": "",
    "freetext2": "",
    "isSingleUse": null,
    "isNonReloadable": null,
    "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    },
    "language3ds": null
}
```