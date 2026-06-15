# Get Cardholder Details

```curl cURL
curl --request GET \
     --url https://cardsapi-uat.globalprocessing.net/api/v1/cardholder/publicToken \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer <<apiKey>>'
```

```json Response Example
{
    "title": "Mr.",
    "firstName": "John",
    "middleName": null,
    "lastName": "Smith",
    "dateOfBirth": "1982-02-25",
    "mobile": "07645123456",
    "email": "jsmith@email.com"
}
```

# Get the PublicToken for the Card

<!-- curl@2 -->

For you to get cardholder details, you need the card's unique publicToken included in the endpoint.

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you will need to have a valid authentication token. This token is used to access Thredd systems and must be included as part of the header.

# Run the Endpoint



After the body for the request has been completed and it's sent to the URL, you will receive a response. The cardholder details endpoint returns the following fields:

- Title
- First Name
- Middle Name
- Last Name
- Date of Birth
- Mobile Phone Number
- Email