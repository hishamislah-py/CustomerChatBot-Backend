# List Cards Limits - Field Descriptions (Product Level)

The following page details each of the fields received in the response when using the List Card Limits endpoint.

## Response Fields

The following table describes fields that included in the response after successfully retrieving card limits.

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
        availableBalance
      </td>

      <td>
        The available balance of the card.
      </td>
    </tr>

    <tr>
      <td>
        maxAllowableBalance
      </td>

      <td>
        Maximum allowed balance of the card.
      </td>
    </tr>

    <tr>
      <td>
        currencyCode
      </td>

      <td>
        The currency code for the card.
      </td>
    </tr>

    <tr>
      <td>
        blockedAmount
      </td>

      <td>
        Amount of funds blocked on the card account as a result of all outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2).
      </td>
    </tr>

    <tr>
      <td>
        **cardLimits**
      </td>

      <td>
        Object that contains the cards limits associated with the card.
      </td>
    </tr>

    <tr>
      <td>
        subGroup
      </td>

      <td>
        The type of limit. This will be one of the following:

        * CASH
        * PAY\_IN
        * PAY\_OUT
        * POS
        * UNLOAD
        * LOAD
      </td>
    </tr>

    <tr>
      <td>
        **daily**
      </td>

      <td>
        Object that contains the period limits.
      </td>
    </tr>

    <tr>
      <td>
        period
      </td>

      <td>
        The number of units in the period.
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
        usage
      </td>

      <td>
        The current usage of total financial amount for the limit.
      </td>
    </tr>

    <tr>
      <td>
        No
      </td>

      <td>
        The current usage of number of transactions in the period.
      </td>
    </tr>

    <tr>
      <td>
        **accumulatedPeriod1**
      </td>

      <td>
        Object that contains details around accumulated period 1, set up during the implementation process.
      </td>
    </tr>

    <tr>
      <td>
        period
      </td>

      <td>
        The length of period 1. Only used if Periodicity is set to Rolling Limits.
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
        Accumulated total value over period 1.
      </td>
    </tr>

    <tr>
      <td>
        frequency
      </td>

      <td>
        Accumulated number of transactions in period 1.
      </td>
    </tr>

    <tr>
      <td>
        spent
      </td>

      <td>
        The spend limit for period 1.
      </td>
    </tr>

    <tr>
      <td>
        transactionCount
      </td>

      <td>
        The transaction count limit for period 1.
      </td>
    </tr>

    <tr>
      <td>
        **accumulatedPeriod2**
      </td>

      <td>
        Object that contains details around accumulated period 2, set up during the implementation process.
      </td>
    </tr>

    <tr>
      <td>
        period
      </td>

      <td>
        The length of period 2. Only used if Periodicity is set to Rolling Limits.
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
        Accumulated total value over period 2.
      </td>
    </tr>

    <tr>
      <td>
        frequency
      </td>

      <td>
        Accumulated number of transactions in period 2.
      </td>
    </tr>

    <tr>
      <td>
        spent
      </td>

      <td>
        The spend limit for period 1.
      </td>
    </tr>

    <tr>
      <td>
        transactionCount
      </td>

      <td>
        The transaction count limit for period 1.
      </td>
    </tr>
  </tbody>
</Table>