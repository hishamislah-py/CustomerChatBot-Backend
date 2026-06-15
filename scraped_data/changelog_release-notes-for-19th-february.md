# Release Notes for 23rd February

New changes to the Thredd Cards API for the week ending 23rd February 2024.

* [New Idempotency endpoints](#new-idempotency-endpoints)
* [New Bulk Create Card endpoint](#new-bulk-create-card-endpoint)
* [New Bulk Card Status endpoint](#new-bulk-card-status-endpoint)
* [New Bulk Card Tokens endpoint](#new-bulk-card-tokens-endpoint)
* [16 digit tokens now supported](#sixteen-digit-tokens-supported)
* [Cards API updated to support leap years](#cards-api-updated-to-support-leap-years)
* [Changes to the Update Card endpoint](#changes-to-the-update-card-endpoint)
* [Card Acceptor Lists added to Update Card Control Groups endpoint](#card-acceptor-lists-added-to-update-card-control-groups-endpoint)
* [language3ds field added to multiple endpoints](#language3ds-field-added-to-multiple-endpoints)

## New Idempotency endpoints

This release includes new idempotent endpoints. Idempotency on these endpoints means that sending a request repeatedly generates the same result no matter how times it is sent.

The following endpoints support idempotency:

* (PATCH) Update Card
* (PATCH) Update Card Status
* (PATCH) Convert Card
* (PATCH) Complete Card Replacement
* (PATCH) Update 3DS Credentials
* (PATCH) Unblock CVV
* (PATCH) Update Payment Token Status

For more information on idempotency, see [What is Idempotency?](https://cardsapidocs.thredd.com/docs/what-is-idempotency)

## New Bulk Create Card endpoint

Cards API now supports the bulk creation of cards using the Bulk Create Card endpoint. This  enables you to create in bulk a number of non personalised cards (For example, creating gift cards, or rolling out new products) in a single request.

You can bulk create cards by making a POST request to the Bulk Create Cards endpoint. For example:

```json Example Bulk Create Cards Request
{
  "cardProduct": 123456,
  "quantity": 50
}
```

If successful, a 202 response is returned with a unique identifier for the cards created. This identifier can be used in the Bulk Card Requests endpoint to return endpoints created by the bulk create process. See the below for an example response.

```json Example Bulk Create Card response
{
  "id": 123456
}
```

> 👍 Information
>
> * For more information on the Bulk Create Cards endpoint, see [Bulk Create Cards](https://cardsapidocs.thredd.com/docs/bulk-create-cards) documentation.
> * To try the Bulk Create Cards endpoint, see [Create Bulk Cards](https://cardsapidocs.thredd.com/reference/create-bulk-cards) in the API Explorer.

## New Bulk Card Status endpoint

The Bulk Card Requests endpoint enables you to retrieve the current status of the bulk card creation process using the unique identifier output from a successful response.

You can retrieve bulk card requests by making a GET request to the Bulk Card Requests endpoint. See the below example endpoint, where `bulkCardRequestId=123456` is the unique identifier of the bulk create process:

```json Example Bulk Card Requests endpoint
{{base-url}}/cards/bulk?bulkCardRequestId=123456
```

If successful, a 200 response is returned with the current status of the bulk create process.

```json Example Get Bulk Card Requests response
{
    "status": "Complete"
}
```

> 👍 Information
>
> * For more information on the Bulk Card Requests endpoint, see [Bulk Create Cards](https://cardsapidocs.thredd.com/docs/bulk-create-cards) documentation.
> * To try the Bulk Card Requests endpoint, see [Get Bulk Card Requests](https://cardsapidocs.thredd.com/reference/gets-the-bulk-card-progress) in the API Explorer.

## New Get Bulk Card Tokens endpoint

The Get Bulk Tokens endpoint enables you to retrieve the public tokens created from a bulk card process using the unique identifier output from a successful Bulk Create Card response.

You can retrieve bulk card tokens by making a GET request to the Get Bulk Tokens endpoint, adding the unique Bulk Create Card identifier, the page number, and the page size to the endpoint URL.

For example if you created 20 public tokens using the Bulk Create Card endpoint, if you set the pageSize to 10 and the pageNumber to 1, the response would return the first 10 tokens created. If you wanted to see the 2nd 10, you would need to changed the pageNumber value to 2.

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

> 👍 Information
>
> * For more information on the Get Bulk Card Tokens endpoint, see [Bulk Create Cards](https://cardsapidocs.thredd.com/docs/bulk-create-cards) documentation.
> * To try the Get Bulk Card Tokens endpoint, see [Get Bulk Card Tokens](https://cardsapidocs.thredd.com/reference/gets-the-bulk-card-tokens) in the API Explorer.

## Sixteen digit tokens supported

The Cards API has been updated to support both 9 and 16 digit public tokens in endpoints.

## Cards API updated to support leap years

The Cards API has been updated to support leap years for the expiry date on cards. For example, when using the Create Card endpoint, if a card is created with the `ExpiryDate` field set to `2028-02`, then the `expiryDate `field in the response will return `2028-02-29` as 2028 is a leap year.

## Changes to the Update Card endpoint

The Update Card endpoint now no longer allows fulfilment details to be updated for a virtual card. If a fulfilment address is included in the Update Card request for a virtual card, a 422 response is returned stating that the fulfilment address should not be present for a virtual card.

## Card Acceptor Lists added to Update Card Control Groups endpoint

The fields `cardAcceptorAllowList` and `cardAcceptorDisallowList ` have been added to the Update Card Control Groups endpoint, enabling you to associate a card with a card acceptor allow list or disallow list respectively.

See the following example of the Update Card Control Groups request body with the new fields included.

```json Example Update Card Control Groups body with Card Acceptors
{
    "ControlGroups": {
        "cardAcceptorAllowList": 1,
    		"CardAcceptorDisallowList": 1 
    }
}
```

A successful response will return a HTTP 200 response code and the following response:

```json Example Update Card Control Groups response
{
    "limitsGroup": 1051,
    "usageGroup": 374,
    "recurringFeeGroup": 0,
    "webServiceFeeGroup": 0,
    "authFeeGroup": 786,
    "mccGroup": 0,
    "cardLinkageGroup": 0,
    "calendarGroup": 0,
    "fxGroup": 0,
    "paymentTokenUsageGroup": 0,
    "cardAcceptorAllowList": 1,
    "CardAcceptorDisallowList": 1 
}
```

## language3ds field added to multiple endpoints

The `language3ds` field has been added to the following endpoints:

* Create Card
* Update Card
* Retrieve Card

The `language3ds` field determines the 3DS Apata enrolment language for a card. This must be a valid BSP-47 code (for example, `en-GB`).