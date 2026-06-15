# Set Card Limits (Card Level)

The Set Card limits endpoint enables you to update the velocity limits of a Thredd card.  This will override the default limits set up at a product level for your cards.

You can update the following limit categories:

* **POS** — Point Of Sales transaction limit. ( *POS-Contactless* — Contactless limit for all contactless POS transactions — is a sub-category of the POS limit category. )
* **Cash** — ATM transactions.
* **Pay-In** — Bank to Bank inward Payments. Only applicable if the client has opted for Thredd Agency Banking product.
* **Pay-Out** — Bank to Bank outward Payments. Only applicable if the client has opted for Thredd Agency Banking product.

> ❗️ Important!
>
> * When the card limits are updated using *Set Card Limits* API, then Thredd uses this updated limit during transaction validation and this limit will always override the default product limits.
> * For clients in regions where the Second Payment Directive (PSD2) Rules apply, Thredd will run additional PSD2 validation checks on the transaction, which may impact on the maximum allowed transaction limits. For more information, refer to the [PSD2 Guide](https://docs.thredd.com/PSD2_Guide.htm).

## How to set card limits

1. Retrieve the *default card product* limits by making a GET request to the Card Limits endpoint. See [Get Card Limits](https://cardsapidocs.thredd.com/docs/get-card-limits).
2. Set the card's limits by making a SET request to the *Set Card Limits* endpoint. For example:

```json Example Set Card Limits endpoint
https://cards-iapi-limits-overrides-apigw-uat.thredd.net/set_limit
```

## Request Fields

The table below lists the fields in the Set Limits request.

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>

      <th>
        Min Length
      </th>

      <th>
        Max Length
      </th>

      <th>
        Mandatory
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        public\_token
      </td>

      <td>
        The card’s public token.
      </td>

      <td>
        Number
      </td>

      <td>
        9
      </td>

      <td>
        9
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        Categories are:
        • *POS*
        • *Cash*
        • *Pay-In*
        •*Pay-Out*
      </td>

      <td>
        String
      </td>

      <td />

      <td />

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        subcategory
      </td>

      <td>
        Subcategories are:  *Contactless*
        (Applicable only for POS category)
      </td>

      <td>
        String
      </td>

      <td />

      <td />

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        maximumpertransaction
      </td>

      <td>
        The maximum allowable spend or load for each transaction.
      </td>

      <td>
        Decimal
      </td>

      <td>
        1
      </td>

      <td>
        (14,4)
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        minimumpertransaction
      </td>

      <td>
        The minimum allowable spend or load for each transaction.
      </td>

      <td>
        Decimal
      </td>

      <td>
        1
      </td>

      <td>
        (14,4)
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        dailylimit
      </td>

      <td>
        The maximum amount that can be spent or loaded within a single calendar day.
      </td>

      <td>
        Decimal
      </td>

      <td>
        1
      </td>

      <td>
        (14,4)
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        dailyfrequency
      </td>

      <td>
        The maximum number of transactions or loads permitted within a single calendar day.
      </td>

      <td>
        Integer
      </td>

      <td>
        1
      </td>

      <td>
        10
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumlimit1
      </td>

      <td>
        The first accumulated limit allowed over the accumulated period defined in *accumperiod1*.
        For example, if the accumulated limit for a POS is set at 15,000 and the accumulation period is defined as 30 days, the cardholder will be permitted to spend a maximum of 15,000 within that 30-day timeframe.
      </td>

      <td>
        Decimal
      </td>

      <td>
        1
      </td>

      <td>
        (14,4)
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumfrequency1
      </td>

      <td>
        The maximum number of transactions or loads permitted within the first accumulation period. The number of days in the accumulation period is determined by the value of *accumperiod1*.
        For example, if the accumulated frequency for POS transactions is set to 100 and the *accumperiod1* is established at 30 days, the cardholder will be limited to a maximum of 100 POS transactions within that 30-day timeframe.
      </td>

      <td>
        Integer
      </td>

      <td>
        1
      </td>

      <td>
        10
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumperiod1
      </td>

      <td>
        The first date range over which the accumulated limit applies.
        For example, if the accumulated period is configured to 30 days, the limits defined in *accumfrequency1* and *accumlimit1* will be applicable for a 30-day duration.
      </td>

      <td>
        Integer
      </td>

      <td>
        1
      </td>

      <td>
        4
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumlimit2
      </td>

      <td>
        The second accumulated limit allowed over the accumulated period defined in *accumperiod2*.
      </td>

      <td>
        Decimal
      </td>

      <td>
        1
      </td>

      <td>
        (14,4)
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumfrequency2
      </td>

      <td>
        The maximum number of transactions or loads permitted within the accumulation period. The number of days in the accumulation period is determined by the value of *accumperiod2*.
      </td>

      <td>
        Integer
      </td>

      <td>
        1
      </td>

      <td>
        10
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        accumperiod2
      </td>

      <td>
        The second date range over which the accumulated limit applies.
        For example, if the second accumulated period is configured to 365 days, the limits defined in *accumfrequency2* and *accumlimit2* will be applicable for that entire 365-day duration.
      </td>

      <td>
        Integer
      </td>

      <td>
        1
      </td>

      <td>
        4
      </td>

      <td>
        Yes
      </td>
    </tr>
  </tbody>
</Table>

> ❗️ **Note:**
>
> * “*null*” and "*0*" values are not permitted for any of the fields in the request. In cases where the cardholder wants to set the limit for their contactless transactions to 0 (effectively 'turning off' contactless transactions), you can set the limit via API to a low amount, such as 0.0001, 0.001, 0.01, etc.
> * To retrieve details of the card-specific limits for card, see [Get Card Limits (Card-specific)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific).
> * To retrieve details of the card's *product-level* limits, see [Get Card Limits (Product-level)](https://dash.readme.com/project/docs-gps/v1.0/docs/get-card-limits).

Below is an example of a Set Limit request.

```json Example Set Card Limits request
{
    "category_limits": [
        {
            "limits":
                {
                    "dailyfrequency": 10,
                    "dailylimit": 200,
                    "accumfrequency1": 100,
                    "maximumpertransaction": 100,
                    "accumlimit2": 2000,
                    "accumperiod2": 365,
                    "accumlimit1": 800,
                    "accumperiod1": 30,
                    "minimumpertransaction": 0,
                    "accumfrequency2": 300
                },
            "category":"Cash"
        },
        {
            "limits":
                {
                  "dailyfrequency": 10,
                    "dailylimit": 200,
                    "accumfrequency1": 100,
                    "maximumpertransaction": 100,
                    "accumlimit2": 2000,
                    "accumperiod2": 365,
                    "accumlimit1": 800,
                    "accumperiod1": 30,
                    "minimumpertransaction": 0,
                    "accumfrequency2": 300
                },
            "category": "Pay_in"
        },
        {
            "limits":
                {
                  "dailyfrequency": 10,
                    "dailylimit": 200,
                    "accumfrequency1": 100,
                    "maximumpertransaction": 100,
                    "accumlimit2": 2000,
                    "accumperiod2": 365,
                    "accumlimit1": 800,
                    "accumperiod1": 30,
                    "minimumpertransaction": 0,
                    "accumfrequency2": 300
                },
            "category": "Pay_out"
        },
        {
            "subcategories": [
                {
                    "limits":
                        {
                           "dailyfrequency": 10,
                           "dailylimit": 200,
                           "accumfrequency1": 100,
                           "maximumpertransaction": 100,
                           "accumlimit2": 2000,
                           "accumperiod2": 365,
                           "accumlimit1": 800,
                           "accumperiod1": 30,
                           "minimumpertransaction": 0,
                           "accumfrequency2": 300
                        },
                    "subcategory": "Contactless"
                }
            ],
            "limits":
                {
                   "dailyfrequency": 10,
                    "dailylimit": 200,
                    "accumfrequency1": 100,
                    "maximumpertransaction": 100,
                    "accumlimit2": 2000,
                    "accumperiod2": 365,
                    "accumlimit1": 800,
                    "accumperiod1": 30,
                    "minimumpertransaction": 0,
                    "accumfrequency2": 300
                },
            "category": "POS"
        }
    ],
    "public_token": 666612345
}
```

## Response Fields

If successful, a 200 response is returned. See the table below for possible response status values:

| Status code | Response Description                                                            |
| :---------- | :------------------------------------------------------------------------------ |
| 200         | Limit set successfully.                                                         |
| 401         | Please provide an auth token as part of the request.                            |
| 401         | The provided auth token is not valid. Please request a new token and try again. |
| 403         | Access to openapi documentation is forbidden in the production environment.     |

> 📘 More Information
>
> To view the endpoint in the API Explorer, see [Set Card Limits](https://cardsapidocs.thredd.com/reference/set_limit_set_limit_post).