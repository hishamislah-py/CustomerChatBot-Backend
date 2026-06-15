# List Card Transactions

This section provides instructions on how you can retrieve transactions from a specific time range for a given card. This can be useful in generating card statements for your customers.

## Listing Card Transactions

### Step 1: Retrieve card details

Identify the corresponding <Glossary>Public Token</Glossary> for the card to be used.\
A card's public token is returned in the response to creating a card within the `publicToken` object.

### Step 2: Retrieve card transactions

After identifying the public token for the card, you can list the transactions linked to the card using the *List card transaction(s)* endpoint. You can define the start and end date period over which to return transactions by using the `dateFrom` and `dateTo` headers to define the date range you want returned from the API. See the below example that will return transactions between the 1st January 2021 and the 31st December 2022.

```json Example List Card Transactions endpoint
{{base-url}}/cards/{{publicToken}}/transactions?fromDate=20210101&toDate=20221231
```

If successful, a 200 response will be returned with details of the transactions between the dates specified. See below for an example response:

```json Example List Card Transactions response
[
    {
        "id": 6160502008,
        "description": "string",
        "dateTime": "2024-02-20T14:16:18.34Z",
        "lifeCycleId": null,
        "type": {
            "code": "U",
            "description": "Unload"
        },
        "status": {
            "code": "S",
            "description": "Settled"
        },
        "amount": {
            "billingValue": 50.00,
            "billingCurrency": "GBP",
            "transactionValue": 50.0000,
            "transactionCurrency": "GBP",
            "settlementAmount": 50.00,
            "settlementCurrency": "GBP",
            "actualBalance": 1950.00,
            "availableBalance": 1950.00
        },
        "fees": {
            "id": 0,
            "fixedFee": 0.00,
            "rateFee": 0.00,
            "fxPadding": 0.00,
            "mccPadding": 0.00
        },
        "productId": 10023,
        "cardNetwork": "MASTERCARD",
        "processingCode": "230000",
        "recordId": 0,
        "note": "API Load by ",
        "systemTraceAuditNumber": 0,
        "transactionCountry": "GBR",
        "transactionLink": 6160502008,
        "additionalDetail": null,
        "paymentTokenId": null,
        "paymentMethod": "None",
        "ehiMode": 3
    }
  ]
```

> 👍 API Explorer
>
> See the [List card transaction(s)](https://cardsapidocs.thredd.com/reference/get-card-transactions) endpoint.