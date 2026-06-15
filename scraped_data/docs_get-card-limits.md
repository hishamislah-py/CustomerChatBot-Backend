# Get Card Limits (Product Level)

The Get Card Limits endpoint enables you to view limits associated with a card at a product level, as well as other information related to the card.

You can retrieve a card's limits by making a GET request to the endpoint. For example:

```json Example Card Limits endpoint
{{base-url}}/cards/{{publicToken}}/balance/cardlimits
```

If successful, a 200 response is returned with the limits set on the card and additional information. A successful response will return the following details:

* Available Balance
* Max Allowable Balance
* Currency Code
* Blocked Amount
* Card Limits

The Card Limits consists of multiple sub groups:

* Pay-in Limits
* Pay-out Limits
* Load Limits
* Unload Limits
* POS Limits
* Cash Limits

The below is an example of a successful 200 response.

```json Example Card Limits response
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
            "spent": 0,
            "transactionCount": 0
        },
        {
            "subGroup": "PAY_IN",
            "period": 0,
            "unit": "day",
            "limit": 0,
            "frequency": 0,
            "spent": 0,
            "transactionCount": 0
        },
        {
            "subGroup": "PAY_OUT",
            "period": 0,
            "unit": "day",
            "limit": 0,
            "frequency": 0,
            "spent": 0,
            "transactionCount": 0
        },
        {
            "subGroup": "POS",
            "period": 4,
            "unit": "day",
            "limit": 4000,
            "frequency": 400,
            "spent": 0,
            "transactionCount": 0
        },
        {
            "subGroup": "UNLOAD",
            "period": 4,
            "unit": "day",
            "limit": 750,
            "frequency": 8,
            "spent": 0,
            "transactionCount": 0
        },
        {
            "subGroup": "LOAD",
            "period": 4,
            "unit": "day",
            "limit": 100,
            "frequency": 8,
            "spent": 0,
            "transactionCount": 0
        }
    ]
}
```

Each sub group of limit (CASH, POS, PAY\_IN, PAY\_OUT, LOAD and UNLOAD) will display in a successful response. Each will display the following information.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        subGroup
      </td>

      <td>
        The type of limit.
      </td>
    </tr>

    <tr>
      <td>
        period
      </td>

      <td>
        The number of units in the time period.
      </td>
    </tr>

    <tr>
      <td>
        unit
      </td>

      <td>
        The type of period unit. This will be either:

        * Hour
        * Day
        * Month
        * Year
      </td>
    </tr>

    <tr>
      <td>
        limit
      </td>

      <td>
        The total financial amount of the limit per period.
      </td>
    </tr>

    <tr>
      <td>
        frequency
      </td>

      <td>
        The number of transactions allowed in the period.
      </td>
    </tr>

    <tr>
      <td>
        spent
      </td>

      <td>
        The current spent amount of total financial amount for the limit.
      </td>
    </tr>

    <tr>
      <td>
        transactionCount
      </td>

      <td>
        The current number of transactions in the period.
      </td>
    </tr>
  </tbody>
</Table>

> 👍 API Explorer
>
> See the [List Card Limits](https://cardsapidocs.thredd.com/reference/list-card-limits) endpoint.