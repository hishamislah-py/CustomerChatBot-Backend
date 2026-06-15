# Load a Card

```curl cURL
curl --request POST \
     --url https://cardsapi-uat.globalprocessing.net/cards/publicToken/transactions \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer <<apiKey>>' \
     --header 'Content-Type: application/json'
     
    {
"TransactionType": "Load",
"Amount": 1000.00,
"CurrencyCode": "GBP",
"LoadedBy": "string",
"Description": "string"
}
```

```json Response Example
{
    "transaction": [
        {
            "transactionType": "Load",
            "transactionId": 6153125591,
            "amount": 1000.00,
            "currencyCode": "GBP"
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

# Get the PublicToken for the Card

<!-- curl@2 -->

To load a card, you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you need a valid authentication token. This token is used to access Thredd systems and must be included as part of the header.

# Enter the Mandatory Details

<!-- curl@8-10 -->

You need to include the load details of the load amount in the body.

- TransactionType must be set to "Load" when loading money onto a card.
- Amount is the value of the transaction that you want to load onto the card.
- CurrencyCode is the 3-digit currency code used for the transaction.

# Enter the Non-Mandatory Details

<!-- curl@11-12 -->

LoadedBy and Description are not required fields for this endpoint. LoadedBy indicates the user initiating the transaction, and description is what will be visible to the cardholder on their card statement.

# Run the Endpoint



After the other steps have been completed, run the endpoint. 

The Output gives a response that is split into two. The first, transaction, details the current transaction and includes a unique transactionID for the load onto the card.

The balance section will display the current balance of the card inclusive of the transaction just made.