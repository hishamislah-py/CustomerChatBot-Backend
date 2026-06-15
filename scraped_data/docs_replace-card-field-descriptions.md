# Replace Card - Field Descriptions

The following page details each of the fields received in the response when using the Replace Card endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when converting a card.

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
        moveBalance
      </td>

      <td style={{ textAlign: "left" }}>
        If true then the balance will move to the new card.
      </td>

      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        moveLimitAccumulators
      </td>

      <td style={{ textAlign: "left" }}>
        If true then the limit accumulators will move to the new card.
      </td>

      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        moveChildCards
      </td>

      <td style={{ textAlign: "left" }}>
        If true then the child cards associated with the card will move to the new card.
      </td>

      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        moveExpiryDate
      </td>

      <td style={{ textAlign: "left" }}>
        If true, then move the same expiry date to the new card.
      </td>

      <td style={{ textAlign: "left" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        expiryDate
      </td>

      <td style={{ textAlign: "left" }}>
        If provided, card is set to the new Expiry Date. Otherwise default from program is used.\
        Should not be set when MoveExpiryDate is true. Format YYYY-MM.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        7
      </td>

      <td style={{ textAlign: "left" }}>
        date-time
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        freetext1
      </td>

      <td style={{ textAlign: "left" }}>
        Additional fulfilment data used for transferring extra information to the card manufacturer.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        50
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
        freetext2
      </td>

      <td style={{ textAlign: "left" }}>
        Additional fulfilment data used for transferring extra information to the card manufacturer.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        50
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

The following table describes fields that included in the response after successfully replacing a card.

| Field             | Description                                       |
| :---------------- | :------------------------------------------------ |
| publicToken       | The public token for the replaced card.           |
| customerReference | The external customer reference for the card.     |
| embossName        | The name embossed on the card.                    |
| maskedPan         | The masked PAN for the card created.              |
| startDate         | The start date of the card in yyyy-MM-dd format.  |
| expiryDate        | The expiry date of the card in yyyy-MM-dd format. |