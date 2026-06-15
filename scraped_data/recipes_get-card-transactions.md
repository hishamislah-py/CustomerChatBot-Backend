# Get Card Transactions

```curl cURL
curl --request GET \
     --url 'https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/248396758/transactions?fromDate=20220830&toDate=20220921'
     --header 'accept: application/json' \
     --header 'authorization: Bearer <<apiKey>>'
```

```json Response Example
[
  {
    "id": 6151349769,
    "description": "TransactionType",
    "dateTime": "2022-09-21T08:45:11.587Z",
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
      "billingValue": 200,
      "billingCurrency": "GBP",
      "transactionValue": 200,
      "transactionCurrency": "GBP"
    },
    "fees": {
      "id": 0,
      "fixedFee": 0,
      "rateFee": 0,
      "fxPadding": 0,
      "mccPadding": 0
    },
    "productId": 1234,
    "cardNetwork": "MASTERCARD",
    "processingCode": "230000",
    "recordId": 0,
    "note": "API Load by ",
    "systemTraceAuditNumber": 0,
    "transactionCountry": "GBR",
    "transactionLink": 6151349769,
    "additionalDetail": null
  },
  {
    "id": 6151349768,
    "description": "TransactionType",
    "dateTime": "2022-09-21T08:44:53.43Z",
    "lifeCycleId": null,
    "type": {
      "code": "L",
      "description": "Load"
    },
    "status": {
      "code": "S",
      "description": "Settled"
    },
    "amount": {
      "billingValue": 500.67,
      "billingCurrency": "GBP",
      "transactionValue": 500.67,
      "transactionCurrency": "GBP"
    },
    "fees": {
      "id": 0,
      "fixedFee": 0,
      "rateFee": 0,
      "fxPadding": 0,
      "mccPadding": 0
    },
    "productId": 1234,
    "cardNetwork": "MASTERCARD",
    "processingCode": "220000",
    "recordId": 0,
    "note": "API Load by ",
    "systemTraceAuditNumber": 0,
    "transactionCountry": "GBR",
    "transactionLink": 6151349768,
    "additionalDetail": null
  }
]
```

# Get the PublicToken for the Card

<!-- curl@2 -->

To get a card's transactions you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you need to have a valid authentication token. The token accesses Thredd systems and must be included as part of the header.

# Add dates to the URL

<!-- curl@2 -->

The Get Card Transactions endpoint works by returning all transactions for a card between two nominated dates. These dates must be included in the endpoint URL. 

In this example, the dates are added to the end of the URL and specify that transactions between the 30th August 2022 and 21st September 2022 should be returned by the endpoint.

# Run the Endpoint



After the other steps have been completed, run the endpoint. If successful, a 200 response will be returned with the details of all transaction between the specified dates.

In this example, the response has returned two distinct transactions. The latest (which appears first) is £200 being unloaded from the card. The second is £500.67 being loaded onto the card. Both of these transactions include further details on the transaction, such as any fees that are associated with them, as well as their unique transaction id.