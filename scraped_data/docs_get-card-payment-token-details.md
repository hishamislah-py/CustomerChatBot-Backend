# Get Card Payment Token Details

The Get Card Payment Token Details endpoint enables you to retrieve the details of a specified payment token. You can retrieve the details of the token by making a GET request to the Payment Tokens endpoint. For example:

```json Example Get Card Payment Token Details endpoint
{{base-url}}/cards/{{publicToken}}/payment-tokens/{{token-id}}
```

A successful response will return an HTTP 200 response code. Below is an example response:

```json Example Card Payment Token Details response
{
    "creatorTokenReference": "DAPLMC0000239565f52605b88199440da31349c23457eeb5",
    "cardUsageGroup": "TES-CU-001 - Test CR",
    "paymentTokenUsageGroup": "CORPT-0001 - TXN_Default",
    "walletAccountScore": 5,
    "walletDeviceScore": 3,
    "walletReasons": "000000000010000000000000",
    "transactionID": 0,
    "responseCode": null,
    "transactionDate": null,
    "cardAcceptorNameLocation": "                                        ",
    "bnReference": "",
    "mtid": null,
    "ehiRequestTime": null,
    "ehiResponseTime": null,
    "activationCode": "297147",
    "activationMethod": "Email",
    "activationStatus": "",
    "id": 6783,
    "walletId": "APPLE",
    "walletProvider": "Apple",
    "tokenPAN": "1321",
    "statuses": {
        "tokenisedStatus": {
            "code": "1",
            "description": "Tokenised"
        },
        "authorisationStatus": {
            "code": "A",
            "description": "Approve with Authentication"
        },
        "authorisationDecision": {
            "code": "A",
            "description": "Approve with Authentication"
        },
        "transactionStatus": {
            "code": "A",
            "description": "Active"
        },
        "gpsStatusInfo": {
            "code": "83",
            "description": "Deactivated"
        }
    },
    "tokenisedDate": "01/17/2020 08:48:06",
    "expiryDate": "12/31/2022 00:00:00",
    "tokenType": "Secure Element PAN",
    "deviceType": "Unknown",
    "deviceName": "iPhone",
    "merchantName": null
}
```

> 👍 API Explorer
>
> See the [Get details for a card payment token](https://cardsapidocs.thredd.com/reference/get-details-for-card-payment-token) endpoint.