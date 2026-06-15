# Get Card Limits (Card Level)

The Get Card Limits endpoint enables you to retrieve the velocity limits associated with a specific card.

You can retrieve a card's limits by making a GET request to the endpoint. For example:

```json Example Card Limits endpoint
https://cards-iapi-limits-overrides-apigw-uat.thredd.net/get_limit
```

# Request Fields

The table below outlines the fields that can be included in the request body when calling the Get Card Limits endpoint.

| Field       | Description               | Type   | Minimum Length | Maximum Length | Mandatory |
| :---------- | :------------------------ | :----- | :------------- | :------------- | :-------- |
| token       | The card’s public token.  | Number | 9              | 16             | Yes       |
| product\_id | Unique ID of the product. | Number | 1              | 10             | Yes       |

## Example Request

Below is an example of a get card limit request.

```json Example Get Card Limits request
{
    "product_id": 1209,
    "token": 223568671
}
```

# Response Fields

If successful, a 200 response is returned with the limits set on the card and additional information. A successful response will return the following details:

## Example Response

Below is an example of a successful 200 response.

```json Example Get Card Limits response
{
    "public_token": "223344559",
    "limits_with_counter": [
        {
            "category": "Cash",
            "limits": {
                "maximumpertransaction": "70.0",
                "minimumpertransaction": "0.0",
                "dailylimit": "100.0",
                "dailyfrequency": 10,
                "accumlimit1": "100.0",
                "accumfrequency1": 100,
                "accumperiod1": 30,
                "accumlimit2": "1000.0",
                "accumfrequency2": 1000,
                "accumperiod2": 36
            },
            "counters": {
                "daily_count": 0,
                "daily_amount": 0.0,
                "accumlimit1_count": 0,
                "accumlimit1_amount": 0.0,
                "accumlimit2_count": 0,
                "accumlimit2_amount": 0.0
            },
            "subcategories": []
        },
        {
            "category": "Pos",
            "limits": {
                "maximumpertransaction": "0.2",
                "minimumpertransaction": "0.0",
                "dailylimit": "0.234",
                "dailyfrequency": 10,
                "accumlimit1": "1000.0",
                "accumfrequency1": 100,
                "accumperiod1": 30,
                "accumlimit2": "2000.0",
                "accumfrequency2": 12789,
                "accumperiod2": 365
            },
            "counters": {
                "daily_count": 0,
                "daily_amount": 0.0,
                "accumlimit1_count": 0,
                "accumlimit1_amount": 0.0,
                "accumlimit2_count": 0,
                "accumlimit2_amount": 0.0
            },
            "subcategories": [
                {
                    "subcategory": "Contactless",
                    "limits": {
                        "maximumpertransaction": "0.1",
                        "minimumpertransaction": "0.0",
                        "dailylimit": "0.1",
                        "dailyfrequency": 10,
                        "accumlimit1": "10.0",
                        "accumfrequency1": 10,
                        "accumperiod1": 10,
                        "accumlimit2": "10.0",
                        "accumfrequency2": 1000,
                        "accumperiod2": 100
                    },
                    "counters": {
                        "daily_count": 0,
                        "daily_amount": 0.0,
                        "accumlimit1_count": 0,
                        "accumlimit1_amount": 0.0,
                        "accumlimit2_count": 0,
                        "accumlimit2_amount": 0.0
                    }
                }
            ]
        },
        {
            "category": "Pay_in",
            "limits": {
                "maximumpertransaction": "10.0",
                "minimumpertransaction": "0.0",
                "dailylimit": "100.0",
                "dailyfrequency": 10,
                "accumlimit1": "1000.0",
                "accumfrequency1": 100,
                "accumperiod1": 30,
                "accumlimit2": "1000.0",
                "accumfrequency2": 1000,
                "accumperiod2": 367
            },
            "counters": {
                "daily_count": 0,
                "daily_amount": 0.0,
                "accumlimit1_count": 0,
                "accumlimit1_amount": 0.0,
                "accumlimit2_count": 0,
                "accumlimit2_amount": 0.0
            },
            "subcategories": []
        },
        {
            "category": "Pay_out",
            "limits": {
                "maximumpertransaction": "10.0",
                "minimumpertransaction": "0.0",
                "dailylimit": "100.0",
                "dailyfrequency": 10,
                "accumlimit1": "1000.0",
                "accumfrequency1": 100,
                "accumperiod1": 30,
                "accumlimit2": "1234567890.0",
                "accumfrequency2": 1000,
                "accumperiod2": 367
            },
            "counters": {
                "daily_count": 0,
                "daily_amount": 0.0,
                "accumlimit1_count": 0,
                "accumlimit1_amount": 0.0,
                "accumlimit2_count": 0,
                "accumlimit2_amount": 0.0
            },
            "subcategories": []
        }
    ]
}
```

> 📘 More Information
>
> To view this endpoint in the API Explorer, see [Get Card Limits](https://cardsapidocs.thredd.com/reference/get_limit_get_limit_get)