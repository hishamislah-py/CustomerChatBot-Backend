# Release Notes for 2 September 2022

New changes to the GPS Cards API for the week ending 2nd September 2022.

* [Endpoints changed to spinal casing](#endpoints-changed-to-spinal-casing)
* [Publictoken added to response for endpoints](#publictoken-added-to-response-for-endpoints)
* [Get CVV Status endpoint response returns remaining tries](#get-cvv-status-endpoint-response-returns-remaining-tries)
* [New Update Payment Token Status endpoint](#new-update-payment-token-status-endpoint)
* [New Unbind Payment Token endpoint](#new-unbind-payment-token-endpoint)
* [Added Address and Fulfilment to Retrieve Card endpoint response](#added-address-and-fulfilment-to-retrieve-card-endpoint-response)

## Endpoints changed to spinal casing

The following endpoints have been changed to spinal casing for this release. This means that previous versions of endpoints will no longer work. For example, the Get Allowed Merchants endpoint used to be the following.

```json Get Allowed Merchant endpoint without spinal casing
{{base-url}}/groups/allowmerchant
```

The new endpoint is the following.

```json New Get Allowed Merchant endpoint with spinal casing
{{base-url}}/groups/allow-merchant
```

The updated list of endpoints are as follows:

* Convert Card
* Update Card Control Overrides
* Get Card Control Overrides
* Create 3DS Credentials
* List 3DS Credentials
* Update 3DS Credentials
* Delete 3DS Credentials
* Get Allowed Merchants
* Add Merchant to Allow List
* Remove Merchant from Allow List
* Get Disallowed Merchants
* Add Merchant to Disallow List
* Remove Merchant from Disallow List
* Get Customer Specific Cards

## Publictoken added to response for endpoints

The following endpoint responses now include the card's Publictoken.

* Load
* Unload
* Balance Adjustment

> 📘 Example
>
> See below for an example of the Publictoken returned in a Load Balance endpoint response.

```json Example Load Card Endpoint Response
{
    "transaction": [
        {
            "transactionType": "Load",
            "transactionId": 6153547924,
            "amount": 1000.00,
            "currencyCode": "GBP",
            "publicToken": "107690988"
        }
    ],
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 1000,
        "pendingAmount": 0,
        "availableBalance": 1000
    }
}
```

## Get CVV Status endpoint response returns remaining tries

The Get CVV Status endpoint response now returns the count for the remaining CVV tries for a card alongside the current CVV status of the card.

## New Update Payment Token Status endpoint

The Update Payment Token Status endpoint enables you to change a payment token status so that the tokens are up-to-date.

> 📘 Example
>
> See below for an example of the body for the Update Payment Token Status endpoint. Click [here](https://cardsapidocs.thredd.com/reference/update-payment-token-status-1) to test this endpoint in the API Explorer.

```json Example of Update Payment Token Status body
{
  "status": "Suspended"
   
}
```

## New Unbind Payment Token endpoint

The Unbind Payment Token endpoint enables you to remove a payment token associated with a device.

> 📘 Example
>
> See below for an example of a body used for the Unbind Payment Token endpoint. Click [here](https://cardsapidocs.thredd.com/reference/unbind-device-from-token) to test this endpoint in the API Explorer.

```json Example of Unbind Payment Token Body
{
"paymentTokenID": 123456
"deviceIndex": 4
}
```

## Added Address and Fulfilment to Retrieve Card endpoint response

The Retrieve Card endpoint has been updated so that the Address and Fulfilment details for the card are now included in the response.

> 📘 Example
>
> See below for an example of the Retrieve Card endpoint response which now includes Address and Fulfilment details.

```json Example Retrieve Card Response
{
    "cardType": "Physical",
    "publicToken": "107690988",
    "status": "Inactive",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr. Bruce Wayne",
        "maskedPan": "999999******9004",
        "pan": "9999999006089004",
        "startDate": "2022-09-01",
        "expiryDate": "2023-09-30"
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "Bruce",
        "middleName": "Batman",
        "lastName": "Wayne",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "BWayne@iambatman.com"
    },
    "cardProduct": {
        "scheme": "GPS SCHEME TEST",
        "product": 10023
    },
    "controlGroups": {
        "limitsGroup": 1051,
        "usageGroup": 374,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": 0,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0
    },
    "3DS": [],
    "designId": "PMTREST",
    "address": {
        "addressLine1": "1007",
        "addressLine2": "Mountain Drive",
        "addressLine3": "string",
        "city": "Gotham",
        "state": "",
        "county": "New Jersey",
        "postCode": "GC11 2LD",
        "country": "840"
    },
    "fulfilment": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "",
        "addressLine3": "Gothamshire",
        "city": "Gotham",
        "state": "",
        "county": "",
        "postCode": "GC11 2LD",
        "country": "840"
    }
}
```