# Renew a Card

```curl cURL
curl --request POST \
     --url https://cardsapi-uat.globalprocessing.net/api/v1/cards/publicToken/renew \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer <<apiKey>>' \
     --header 'Content-Type: application/*+json'
```

```json Response Example
{"success":true}
```

# Get the PublicToken for the Card

<!-- curl@2 -->

To renew a card, you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you will need to have a valid authentication token. This token is used to access Thredd systems and must be included as part of the body.

# Run the Endpoint



After the first steps have been completed, you can now run the GET request to renew the card.