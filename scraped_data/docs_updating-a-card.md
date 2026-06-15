# Updating a card

This section provides instructions on how to update card details. This supports use cases where you may want to update (also know as provisioning) cardholder details such as:

* Name
* Contact details (email and mobile)
* Address
* <Glossary>Fulfilment Address</Glossary>

## Updating Card Details

### Step 1: Capture the customer details that have changed

Before updating a card, ensure you have captured all the details from the customer that you wish to update in the Thredd system.

### Step 2: Identify the customer's card

When you have captured the details you want to change for your customer, you need to identify the public token that corresponds to the customer's card.

### Step 3: Make an update card request

When you have identified the correct public token, you can make a PATCH/cards call. Ensure you have only the fields you want to update populated. For example:

```json Example Update Card endpoint
{{base-url}}/cards/{{publicToken}}
```

> 🚧 Blank Values
>
> If you pass an empty value as part of an Update Card call, this will overwrite the value that is stored in the Thredd systems. You can use this to remove cardholder data that you no longer want stored on the Thredd platform.

Examples of different types of updates are shown below:

```json Example Update Address body
"address": {
        "addressLine1": "1008",
        "addressLine2": "Royal Way",
        "city": "London",
        "county": "Essex",
        "postCode": "RM7 2LD",
        "country": "GBR"
    },
```

```json Example Update Fulfilment body
"fulfillment": {
        "addressLine1": "32 Eastern Lane",
        "addressLine2": "Hazelford",
        "city": "Sheffield",
        "county": "South Yorkshire",
        "postCode": "S25 4HY",
        "country": "GBR"
    },
```

A successful response will return a HTTP 204 response code and the specified fields will be updated.

> 👍 API Explorer
>
> See the [Update card](https://cardsapidocs.thredd.com/reference/update-card) endpoint.

> 📘 Note
>
> Fulfilment details cannot be updated for a virtual card. If a fulfilment address is included in the Update Card request for a virtual card, a 422 response is returned stating that the fulfilment address should not be present for a virtual card.