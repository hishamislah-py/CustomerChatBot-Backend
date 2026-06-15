# Load and Unload Card for Issuer

The Load and Unload Card for Issuer endpoint enables issuers to load and unload cards for their sponsored programs.

You can load or unload a card by making a POST request to the endpoint. For example:

```json Example Load and Unload Card for Issuer endpoint
https://thredd-cg-custompan-uat.thredd.net/api/v1/cards/issuer/{publicToken}/transactions
```

> 📘 Note
>
> To use this endpoint you must have an Issuer ID linked to your Program Manager. If you do not have an Issuer ID linked, a 401 is returned.

Use this endpoint to load and unload funds onto the card for your sponsored program. See the below example requests for loading and unloading funds to a card.

```json Example Issuer Load request
{
	"transactionType": "Load",
	"amount": 10.00,
	"currencyCode": "GBP",
	"loadedBy": "System",
	"description": "Card Top up for Lunch"
}
```

```json Example Issuer Unload request
{
	"transactionType": "Unload",
	"amount": 10.00,
	"currencyCode": "GBP",
	"loadedBy": "System",
	"description": "Moving of funds"
}
```

A successful response returns a 200 response with the card's transaction and the updated balance in the response.

```json Example Issuer Load response
{
    "transaction": [
        {
            "transactionType": "Load",
            "transactionId": 6157564898,
            "amount": 10,
            "currencyCode": "GBP",
            "publicToken": "103169969"
        }
    ],
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 10,
        "pendingAmount": 0,
        "availableBalance": 10
    }
}
```

> 📘 More Information
>
> For details on the fields for this endpoint, see [Load and Unload Card for Issuer - Field Descriptions](https://cardsapidocs.thredd.com/docs/load-and-unload-bin-sponsor-field-descriptions)