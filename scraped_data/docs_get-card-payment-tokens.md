# Get Card Payment Tokens

The Get Card Payment Tokens endpoint enables you to retrieve the list of payment tokens associated with a card. You can retrieve the payment tokens by making a GET request to the Payment Tokens endpoint. For example:

```json Retrieve Card Payment Tokens endpoint
{{base-url}}/cards/{{publicToken}}/payment-tokens
```

A successful response returns an HTTP 200 response code. Below is an example response for an APPLE wallet:

```json Retrieve Card Payment Tokens response
[
    {
        "id": 6783,
        "walletId": "APPLE",
        "tokenPAN": "1321",
        "status": {
            "tokenisationStatus": {
                "code": "-",
                "description": "Invalid"
            },
            "authorisationDecision": {
                "code": "A",
                "description": "Accepted"
            },
            "authorisationStatus": {
                "code": "A",
                "description": "Accepted"
            },
            "gpsStatus": "Deactivated"
        },
        "tokenisedDate": "2024-01-01 00:00:01Z",
   		  "expiryDate": "2026-01-01",
        "tokenType": "Secure Element PAN",
        "deviceType": "Mobile phone (no further detail)",
        "deviceName": "iPhone",
        "merchantName": "TESCO Richmond",
        "activationCode": "297147"
    }
]
```

> 👍 API Explorer
>
> See the [Get a list of Card Payment Tokens](https://cardsapidocs.thredd.com/reference/get-list-of-card-payment-tokens) endpoint.