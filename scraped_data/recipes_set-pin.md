# Set PIN

```curl cURL
curl --request POST \
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/publicToken/pin \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <<apiKey>>' \
     --header 'content-type: application/*+json'

{
    "CardPin": "1234"
}
```

```json Response Example
{"success":true}
```

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you need to have a valid authentication token. The token accesses Thredd systems and must be included as part of the header.

# Get the PublicToken for the Card

<!-- curl@2 -->

To set the PIN of a card, you need the card's unique publicToken included in the endpoint.

# Set the Card PIN

<!-- curl@7-9 -->

Set the new PIN for the card in the CardPin field of the body.

# Run the Endpoint



Run the endpoint when the details for the PIN are set. If successful, a 204 response is returned.