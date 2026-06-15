# Card Verification Value (CVV2)

This section provides instructions on how to manage a card's Card Verification Value (CVV2). A card's CVV is the number printed on the back of the card, which is used to authorise online and Mail Order Telephone Order (MOTO) transactions between a merchant and cardholder. This provides an additional layer of security for online and MOTO transactions.

A card's CVV2 is randomly allocated as part of the Create Card API call. To find out more about creating cards, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

After card creation, the Cards API enables you to:

* Retrieve a card's CVV
* Unblock a card's CVV when the maximum number of attempts have been exceeded
* Get the card's CVV status

## Retrieve a Card's CVV

### Step 1: Identify the card's public token

Before retrieving a card's CVV, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

### Step 2: Get the card's CVV

After identifying the card's public token, execute a GET call to the *cards CVV* endpoint. For example:

```json Example Get CVV endpoint
{{base-url}}/cards/{{publicToken}}/cvv
```

A successful response will return a 200 http code with the value of the card's CVV in the response body.

```json Example Retrieve Card CVV response
{
    "cvv": "955",
    "resultStatus": "Success"
}
```

> 👍 API Explorer
>
> See the [Retrieve card CVV](https://cardsapidocs.thredd.com/reference/get-cvv) endpoint for more information.

## Unblock a Card's CVV

### Step 1: Identify the card's public token

Before retrieving a card's CVV, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

### Step 2:  Update CVV status

After identifying the card's public token, execute a PUT call to the *cards CVV* endpoint. For example:

```json Example Unblock CVV endpoint
{{base-url}}/cards/{{publicToken}}/cvv/status
```

The body should contain the status object set to 'Unblocked', as well as optional fields that describe the action and who the update was done by.

```json Example Unblock CVV body
{
  "status": "Unblocked",
  "description": "CVV unblocked on 04/11/2024",
  "updatedBy": "John Bloggs"
}
```

A successful response will return a 204 HTTP code - success no response.

> 👍 API Explorer
>
> See the [Unblock card CVV](https://cardsapidocs.thredd.com/reference/unblock-cvv) endpoint for more information.

## Get CVV Status

Use the Get CVV Status endpoint to retrieve the current status of the CVV of the card. A CVV can have have a status of:

* Unblocked
* Blocked

You can retrieve the CVV status of the card by making a GET request to the GET CVV Status endpoint. For example:

```json Example Get CVV Status Endpoint
{{base-url}}/cards/{{publicToken}}/cvv/status
```

A successful response will return a HTTP 200 response code and payload which includes the current status. For example:

```json Example Get CVV Status response
{
    "status": "Unblocked"
}
```

> 👍 API Explorer
>
> See the [Get CVV Status](https://cardsapidocs.thredd.com/reference/get-cvv-status) endpoint for more information.