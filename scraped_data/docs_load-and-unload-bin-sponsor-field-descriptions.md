# Load and Unload Card for Issuer - Field Descriptions

The following page details the fields available in the request and response when using the Load and Unload Card for Issuer endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when loading or unloading funds as an issuer.

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Field
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Minimum Length
      </th>

      <th style={{ textAlign: "left" }}>
        Maximum Length
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Mandatory
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        transactionType
      </td>

      <td style={{ textAlign: "left" }}>
        The type of transaction for the request. Select from:

        * Load for loading money onto a card
        * Unload for unloading money from a card
      </td>

      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        6
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Yes
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        amount
      </td>

      <td style={{ textAlign: "left" }}>
        The monetary amount of the transaction.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        Double
      </td>

      <td style={{ textAlign: "left" }}>
        Yes
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        currencyCode
      </td>

      <td style={{ textAlign: "left" }}>
        the currency used in the transaction.
      </td>

      <td style={{ textAlign: "left" }}>
        3
      </td>

      <td style={{ textAlign: "left" }}>
        3
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Yes
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        user
      </td>

      <td style={{ textAlign: "left" }}>
        The actor initiating the transaction request.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        description
      </td>

      <td style={{ textAlign: "left" }}>
        Free text field describing the transaction that is populated on card statement.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        1024
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>
  </tbody>
</Table>

## Response Fields

A successful response for the Load and Unload Card for Issuer endpoint returns a 200 response and details of the transaction performed, and the updated balance of the card.

| Field            | Description                                                                                    |
| :--------------- | :--------------------------------------------------------------------------------------------- |
| **transaction**  | An object that contains the details of the transaction.                                        |
| transactionType  | The type of transaction ran by the endpoint.                                                   |
| transactionId    | The unique transaction identifier for the transaction.                                         |
| amount           | The amount of the transaction.                                                                 |
| currencyCode     | The currency code of the transaction                                                           |
| publicToken      | The publicToken of the card the transaction was ran for.                                       |
| **balance**      | An object that contains the details of the updated balance for the card after the transaction. |
| currencyCode     | The currency code associated with the card.                                                    |
| cardBalance      | The current balance of the card.                                                               |
| pendingAmount    | Any pending amount associated with the card,                                                   |
| availableBalance | The available balance of the card.                                                             |