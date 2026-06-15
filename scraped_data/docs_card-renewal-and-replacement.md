# Card Renewal, Card Replacement & Lost Cards

This section provides information on how you can manage card renewal, replacement and lost cards for your customers using the Thredd Platform.

Thredd provides an API to enable you to renew or replace a card. This API combines the functionality of card replacement and card renewal. The replacement card will have the same balance that the original card had at the time when the replacement card is activated. Any linked cards will point to the correct card.

If you want to transfer the card balance immediately to the new card and to update any linked wallet/card payment tokens at the same time. You can then select a suitable renew option.

## Replacing Lost, Stolen or Damaged Cards

In the event your customer loses a card or reports it as stolen, we recommend the following steps:

### Step 1: Identify the lost card's public token

Identify the corresponding public token for the lost card. This is returned in the response to creating a card.

### Step 2: Update Card Status

When you have the public token, you must update the Card's status to `41` (the status for Lost Card) so it can no longer be used to transact on. See [Card Status Change](https://cardsapidocs.thredd.com/docs/card-status) for more details on card statuses.

Note that when you update the card status to lost, you need to remove the validityDate field from the request body.

### Step 3: Issue replacement Card

The Replace Card endpoint allows you to replace a card and also allows you to choose what is transferred to the new card. You can replace a card by making a POST request to the Replace Card endpoint. For example:

```json Example Replace Card endpoint
{{base-url}}/cards/{{publicToken}}/replace
```

The body can include fields that transfer details from the old card to the replacement card. The following options are available:

* **moveBalance** sets whether the balance should be transferred
* **moveLimitAccumulators** sets whether the card limits should be transferred
* **moveChildCards** sets whether any child cards should be transferred
* **moveExpiryDate** sets whether the current expiry date should be transferred
* **expiryDate** sets an expiry date on the card. This can only be used instead of the **moveExpiryDate** option.
* **freetext1** enables you to add information to the card manufacturer
* **freetext2** enables you to add further information to the card manufacturer

```json Example Replace Card body
{
     "moveBalance": true,
     "moveLimitAccumulators": true,
     "moveChildCards": false,
     "moveExpiryDate": true
}
```

If successful, a 200 response will be returned with details on the replaced card.

```json Example Replace Code response
{
    "publicToken": "103169963",
    "customerReference": "my ref 12345",
    "embossName": "Mr Jon Smith",
    "maskedPan": "999999******5974",
    "startDate": "2023-05-05",
    "expiryDate": "2025-04-30"
}
```

> 👍 API Explorer
>
> See the [Replace Card](https://cardsapidocs.thredd.com/reference/replace-card) endpoint for more information.

### Step 4: Activate replacement card

When a user has received their replacement card, it must be activated using the card status endpoint; see [Card Status Change](https://cardsapidocs.thredd.com/docs/card-status).

> 🚧 Card Activation upon replacement
>
> For virtual cards, this activate step must happen simultaneously as virtual cards are issued instantly. For physical cards, these must be user-activated when they are received.

A successful request will respond with an HTTP 201 code and the public token of the new card will be returned.

## Renewing a virtual card

In the event you want to renew a card for a customer outside of the autorenewal cycle, you can issue a renewed virtual card to your customers via an API call.

### Step 1: Identify the card's public token

Identify the public token of the card you want to renew. This is returned in the response to [creating a card](https://cardsapidocs.thredd.com/docs/create-card-2).

### Step 2: Renew Virtual card

You can renew a card by executing a card renewal request.

```json Example Renew Card endpoint
{{base-url}}/cards/{{publicToken}}/renew
```

A 204 HTTP response indicates a successful virtual card renewal with no data returned.

> 👍 API Explorer
>
> See the [Renew Card](https://cardsapidocs.thredd.com/reference/renew-card) endpoint for more information.

## Renewing a physical card

In the event you want to renew a card for a customer outside of the autorenewal cycle, you can issue a renewed physical card to your customers via an API call.

### Step 1: Identify the card's public token

Identify the public token of the card you want to renew. This is returned in the response to [creating a card](https://cardsapidocs.thredd.com/docs/create-card-2).

### Step 2: Renew Physical Card

If your card is a physical card, the process to renew it involves two steps. The first step orders a new card to be created by your card manufacturer. This is done by executing a renew API call to the card renewal API through passing `renew `in the payload.

```json Example Renew Card body
{
	"renewStep": "renew"
 }
```

This will issue an inactive replacement card to your customer whilst allowing them to continue to transact using their existing card until the renewed card arrives.

### Step 3: Migrate Physical Card

When your customer receives the card, you will need to execute a card migration call to the Renew Card endpoint in order to transition to the new card.

```json Example Migrate Card body
{
	"renewStep": "migrate"
 }
```

A 204 HTTP response indicates a successful physical card renewal and the card's new public token is returned. When a user has received their renewed card, it must be activated using the card status endpoint; see [Card Status Change](https://cardsapidocs.thredd.com/docs/card-status).

> 👍 API Explorer
>
> See the [Renew Card](https://cardsapidocs.thredd.com/reference/renew-card) endpoint for more information.

## Renew with Same Expiry

The **renewWithSameExpiry** option enables you to to replace a card (for example, if it has been damaged) with the same details it had before.

The below is an example body for a renew card where renewWithSameExpiry is used.

```json Example Renew With Same Expiry body
{
     "renewStep": "renewWithSameExpiry"
}
```

A 204 response will be returned if the call is successful. You can check the details on the renewed card by using the [Retrieve a Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card) endpoint.