# Release Notes for 27 January 2023

New changes to the GPS Cards API for the week ending 27th January 2023.

* [New Get Card Limits endpoint](#new-get-card-limits-endpoint)
* [Freetext fields added to Replace Card endpoint](#freetext-fields-added-to-replace-card-endpoint)

## New Get Card Limits endpoint

*Endpoint: cards/\{\{publicToken}}/balance/cardlimits*\
A new endpoint has been added that enables customers to view the limits set on a card.

You can retrieve a card's limits by making a GET request to the endpoint. For example:

```json Get Card Limits endpoint
{{base-url}}/cards/{{publicToken}}/balance/cardlimits
```

If successful, a 200 response is returned with the limits set on the card and additional information, such as the available balance. For example:

```json Get Card Limits response
{
    "availableBalance": 0,
    "maxAllowableBalance": 50000,
    "currencyCode": "GBP",
    "blockedAmount": 0,
    "cardLimits": [
        {
            "subGroup": "CASH",
            "period": 0,
            "unit": "day",
            "limit": 0,
            "frequency": 0,
            "usage": 0,
            "No": 0
        },
        {
            "subGroup": "PAY_IN",
            "period": 0,
            "unit": "day",
            "limit": 0,
            "frequency": 0,
            "usage": 0,
            "No": 0
        },
        {
            "subGroup": "PAY_OUT",
            "period": 0,
            "unit": "day",
            "limit": 0,
            "frequency": 0,
            "usage": 0,
            "No": 0
        },
        {
            "subGroup": "POS",
            "period": 4,
            "unit": "day",
            "limit": 4000,
            "frequency": 400,
            "usage": 0,
            "No": 0
        },
        {
            "subGroup": "UNLOAD",
            "period": 4,
            "unit": "day",
            "limit": 750,
            "frequency": 8,
            "usage": 0,
            "No": 0
        },
        {
            "subGroup": "LOAD",
            "period": 4,
            "unit": "day",
            "limit": 100,
            "frequency": 8,
            "usage": 0,
            "No": 0
        }
    ]
}
```

> 👍 Documentation/API Explorer
>
> * For more information on this endpoint, see [Card Limits](https://cardsapidocs.thredd.com/docs/get-card-limits)
> * To try the Get Card Limits endpoint, navigate to [Get Card Limits](https://cardsapidocs.thredd.com/reference/update-card-stip-balance) in API Explorer

## Freetext fields added to Replace Card endpoint

The free text fields (freetext1 and freetext2) have now been added to the response when using the Replace Card endpoint.

> 👍 API Explorer
>
> To try the Replace Card endpoint, navigate to [Replace Card](https://cardsapidocs.thredd.com/reference/replace-card) in API Explorer