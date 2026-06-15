# PIN Management

This section provides instructions on how to manage your cardholder's Personal Identification Number (PIN). A card's PIN is a short numerical code used to authorise Point of Sale (POS) transactions between a merchant and cardholder. This provides an additional layer of security for POS transactions.

A card's PIN is always set to a randomly allocated value as part of the Create Card API call. To find out more about creating cards, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

After card creation, the Thredd Cards API enables you to:

* Set a card's PIN to a user-defined value
* Retrieve a card's PIN to display to the user
* Unblock a card's PIN when the maximum number of attempts has been exceeded

## Setting a card's PIN

### Step 1: Identify the card's public token

Before setting a card's PIN, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

### Step 2: Set the card's PIN

After identifying the card's public token, execute a POST call to the cards *Set Card PIN* endpoint with an updated PIN in the request body. For example:

```json Example Set PIN endpoint
{{base-url}}/cards/{{publicToken}}/pin
```

The example body below sets the card PIN to 0000.

```json Example Set PIN body
{
  "cardPin": 0000
}
```

A successful response will return a 204 http code - success with no response.

> 👍 API Explorer
>
> See the [Set card PIN](https://cardsapidocs.thredd.com/reference/set-pin) endpoint for more information.

## Retrieving a card's PIN

### Step 1: Identify the card's public token

Before retrieving a card's PIN, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

### Step 2: Retrieving the card's PIN

After identifying the card's public token, execute a GET call to the **Get PIN** endpoint. For example:

```json Example Get PIN endpoint
{{base-url}}/cards/{{publicToken}}/pin
```

This request requires no body and a successful response will return a 200 http code and the card's PIN.

```json Example Get PIN response
{
    "pin": "7010"
}
```

> 👍 API Explorer
>
> See the [Get PIN](https://cardsapidocs.thredd.com/reference/get-pin) endpoint for more information.

## Retrieving a PIN Status

### Step 1: Identify the card's public token

Before retrieving a card's PIN status, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

### Step 2: Retrieving the card's PIN

After identifying the card's public token, execute a GET call to the **Get PIN Status** endpoint. For example:

```json Example Get PIN Status endpoint
{{base-url}}/cards/{{publicToken}}/pin/status
```

This request requires no body and a successful response will return a 200 http code and the status of the card's PIN.

```json Example Get PIN Status response
{
    "status": "Unblocked",
    "remainingTries": "3"
}
```

<Callout icon="👍" theme="okay">
  See the [Get PIN Status](https://cardsapidocs.thredd.com/reference/get-pin-status) endpoint for more information.
</Callout>

## Unblocking a card's PIN

### Step 1: Identify the card's public token

Before unblocking a card's PIN, identify the corresponding public token relating to the card. This is returned in the response to creating a card within the `publicToken` object.

> 📘 Note
>
> You can reset a card's PIN attempt counter at any time; it doesn't need to reach zero. Executing a successful unblock PIN request resets the PIN attempt counter back to its maximum value.

### Step 2: Unblock the card's PIN

After identifying the card's public token, execute a POST call to the Unblock PIN endpoint. For example:

```json Example Unblock Card PIN endpoint
{{base-url}}/cards/{{publicToken}}/pin/unblock
```

> 📘 Note
>
> This endpoint requires content\_type =application/json to be included in the header. If this is not included in the request then a 415 error response is returned.

The request body can include information on the details of why the card is being unblocked and who has unblocked the PIN. For example:

```json Example Unblock PIN request
{
  "description": "Unblocking blocked PIN",
  "updatedBy": "John Smith"
}
```

A successful response will return a 204 http code - success with no response.

> 👍 API Explorer
>
> See the [Unblock PIN](https://cardsapidocs.thredd.com/reference/unblock-pin) endpoint for more information.