# Get a Balance Enquiry

```curl cURL
curl --request GET \
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/publicToken/balance \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <<apiKey>>'
```

```json Response Example
{
    "currencyCode": "GBP",
    "cardBalance": 0,
    "pendingAmount": 0,
    "availableBalance": 0
}
```

# Get the PublicToken for the Card

<!-- curl@2 -->

To retrieve the balance of a card, you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you need to have a valid authentication token. The token accesses Thredd systems and must be included as part of the body.

# Run the Endpoint



After the first steps have been completed, you can now run the GET to return the balance of the card. This will return four values:

- The currency code
- The card balance
- The pending amount
- The available balance

# Receive Response



When the endpoint is run, a response is provided. A successful 200 response provides details on the currency code of the card, as well as the current balance, pending amount and available balance for the card.