# Block a Lost Card

```curl cURL
curl --request PUT \
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards//status \
     --header 'accept: application/json' \
     --header 'authorization: Bearer <<apiKey>>' \
     --header 'content-type: application/*+json'
     
{
     "cardStatusCode": "41",
     "updatedBy": "John Bloggs",
     "description": "Card lost",
     "validityDate": "2023-02"
}
```

```json Response Example
{
     "cardStatusCode": "41",
     "updatedBy": "John Bloggs",
     "description": "Card lost",
     "validityDate": "2023-02"
}
```

# Get an Authentication Token



Before you can run the endpoint, you need to have a valid authentication token. The token accessesThredd systems and must be included as part of the header.

# Get the PublicToken for the Card



To update the status of a card, you need the card's unique publicToken included in the endpoint.

# Set the Card Status



The body of the request must include the new status of the card. In this example we want to block the card as the cardholder has informed us they have lost their card, so we set the cardStatusCode to 41, as that is the code for lost cards.

# Add additional information

<!-- curl@9-11 -->

There are some non-mandatory fields we can use with this endpoint to capture more information. In this example, we've added updatedBy so we can capture the actor who has performed the status change, the description of the action performed, and the date the change will be made to the card status.

# Run the Endpoint



When the body has been completed, run the endpoint. If successful, a 200 response is returned with confirmation of the change in status, as well as the date the status has been updated.