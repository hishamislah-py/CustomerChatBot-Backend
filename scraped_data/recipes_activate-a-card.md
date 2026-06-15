# Activate a Card

```curl cURL
curl --request PUT \
     --url https://sandbox.globalprocessing.com/sandbox/api/v1/cards/publicToken/status \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <<apiKey>>' \
     --header 'content-type: application/*+json'
     
{
     "cardStatusCode": "00",
     "updatedBy": "John Bloggs",
     "description": "Card activated",
     "validityDate": "2023-02"
}
```

```json Response Example
{
    "cardStatusCode": "00",
    "updated": "2023-02-10",
    "updatedBy": "John Bloggs",
    "description": "Card activated"
}
```

# Get the PublicToken for the Card

<!-- curl@2 -->

To update the status of a card, you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you will need to have a valid authentication token. This token is used to access Thredd systems and must be included as part of the header.

# Set the Card Status

<!-- curl@8 -->

Use the Update Card Status endpoint to change the status of a card. The body of the request must include the new status of the card. In this example we want to activate the card, so we set the cardStatusCode field to 00.

# Add additional information

<!-- curl@9-11 -->

There are some non-mandatory fields we can use with this endpoint to capture more information. In this example, we've added updatedBy and description so we can capture the actor who has performed the activation and what we've changed, as well as the date the card will become active.

# Run the Endpoint



When the body has been completed, run the endpoint. If successful, a 200 response is returned with confirmation of the change in status, as well as the date the status has been updated.