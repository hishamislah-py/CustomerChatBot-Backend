# Card Status

This section provides details on card status, how to manage a card's status throughout the card's life cycle and how a card's status can be used to manage a variety of situations including when a card is lost, stolen or damaged.

By default, physical cards are issued in an *inactive* state on the Thredd  system. You can [activate a card](#step-2-activate-a-card) and manage the card throughout its lifecycle using the Update Card Status endpoint. Virtual cards are *active* by default. You can set the activateNow field to `false` in the Create Card field if you want a virtual card to be created in an inactive status.

> 📘 Note
>
> For a full list of card status codes, see [Card Status Codes](https://cardsapidocs.thredd.com/docs/card-status-codes).

## Activating a Card

Physical cards are created with an *inactive* status (unless the `activateNow` field is set to `true`), which means that the card is live, but cannot be used.  When you have created a card, you can use the card status endpoint to set the status of the card to *active*. Thredd recommends that for a physical card, the cardholder should be provided with a means to request card activation when they have received their card (for example, via your customer app or call centre).

Virtual Cards are created with an *active* status by default.

### Step 1: Retrieve Card Details

Before activating a card, you will need to identify the corresponding Public Token for the card. If you are activating a card straight after a [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2) API Call, this is returned in the response to creating a card in the `publicToken` field.

```json Example Create Card response
{
    "publicToken": "111191022",
    "customerReference": "CustNo12345A",
    "embossName": "Mr Johnny Bruce",
    "maskedPan": "531610******3644",
    "startDate": "2023-11-10",
    "expiryDate": "2028-11-30"
}
```

### Step 2: Activate a Card

After identifying the Public Token for the card, you can use it to make a PUT request to the [Update card status](https://cardsapidocs.thredd.com/reference/update-card-status) endpoint with the following payload:

```json Example Card Activation body
{
  "cardStatusCode": "00"
}
```

A successful response will return a 200 http code with the updated card status code in the response and a description of the status.

```json Example Card Activation response
{
    "status": "Active",
  	"cardStatusCode": "00",
    "updated": "2023-02-10",
    "updatedBy": "Updated by not supplied",
    "description": "Card was activated. Card Expiry Changed From 2024-02-29 To Feb 29 2024 12:00AM"
}
```

## Updating Card Status

The Update Card Status endpoint enables you to update the status of a card, such as changing the status to active from inactive.

You can update a status by making a PUT request to the endpoint. For example:

```json Example Update Card Status endpoint
{{base-url}}/cards/{{publicToken}}/status
```

The body should include  `cardStatusCode` for the card. It can also include further information, such as who made the update and the date of when the new card status is valid. For example:

```json Example Update Card Status body
{
     "status": "Active",
  	 "cardStatusCode": "00",
     "updatedBy": "John Bloggs",
     "description": "Card activated",
     "validityDate": "2023-02"
}
```

A successful response will return a HTTP 200 response code. Below is an example response:

```json Example Update Card Status response
{
    "status": "Active",
  	"cardStatusCode": "00",
    "updated": "2023-02-10",
    "updatedBy": "John Bloggs",
    "description": "Card was activated. Card Expiry Changed From 2024-02-29 To Feb 29 2024 12:00AM"
}
```

> 👍 API Explorer
>
> See the [Update card status](https://cardsapidocs.thredd.com/reference/update-card-status) endpoint.

> 📘 Note
>
> If you try to update the card status with the card's current status, a 200 response returns with a message in the description field of the response specifying that the card was already in requested status and the status is not changed. This event is not stored in the card status history.

### Status Codes for Card Blocks

Use the following Thredd status codes for card blocks:

* Temporary Block: "05 - Do Not Honour", "62 - Restricted Card"
* Permanent Block: "41 - Lost", "43 - Stolen", "83 - Card Destroyed"

## Get Card Status

You can retrieve details of the current card status by making a GET request to the [Retrieve Card Status](https://cardsapidocs.thredd.com/reference/retrieve-card-status) endpoint, with the <Glossary>Public Token</Glossary> of the card whose status you are retrieving. For example:

```json Example Retrieve Card Status endpoint
{{base-url}}/cards/{{publicToken}}/status
```

If successful, a 200 response is returned with the card status code and the description of that status.

```json Example Retrive Card Status response
{
    "status": "Active",
 	  "cardStatusCode": "00",
    "cardStatusDescription": "00 (Active)"
}
```

> 👍 API Explorer
>
> See the [Retrieve card status](https://cardsapidocs.thredd.com/reference/retrieve-card-status) endpoint.