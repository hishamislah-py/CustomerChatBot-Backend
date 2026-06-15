# Release Notes for 28 October 2022

New changes to the GPS Cards API for the week ending 28 October 2022.

* [Update Card endpoint updated to support Master Virtual Cards](#update-card-endpoint-updated-to-support-master-virtual-cards)
* [Automatic Web Service Fees added to endpoints](#automatic-web-service-fees-added-to-endpoints)

## Update Card endpoint updated to support Master Virtual Cards

The Update Card endpoint has been updated to support the Master Virtual Card cardtype.

> 👍 Documentation
>
> For more details on updating a card, see [Updating a Card](https://cardsapidocs.thredd.com/docs/updating-a-card)

## Automatic Web Service Fees added to endpoints

The following endpoints have been updated in this release so that program managers can automatically charge customers on using the service. When the request is successful and the specific condition for the endpoint has been met, a new fee transaction for the card will be created.

> 📘 Note
>
> Automatic web service fees should be completed on the Web Services Fees tab of the customer PSF. For more details, see the [Fees Guide](https://developer.globalprocessing.com/fees/Content/Fee_Setup_and_Configuration/Completing_your_PSF.htm).

The below table details each of the available endpoints, the conditions required for a fee to be charged to the card, and the FeeType.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Endpoint
      </th>

      <th>
        Condition
      </th>

      <th>
        FeeType
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        POST /cards
      </td>

      <td>
        CardType is Virtual
      </td>

      <td>
        VirtualCardIssuingFee
      </td>
    </tr>

    <tr>
      <td>
        POST /cards
      </td>

      <td>
        CardType is Physical
      </td>

      <td>
        PhysicalCardIssuingFee
      </td>
    </tr>

    <tr>
      <td>
        PUT /cards/\{publicToken}/status
      </td>

      <td>
        Status is “Active” and Card is Parent Card
      </td>

      <td>
        ParentCardActivationFee
      </td>
    </tr>

    <tr>
      <td>
        PUT /cards/\[publicToken}/status
      </td>

      <td>
        Status is “Active” and Card is Parent Card
      </td>

      <td>
        ChildCardActivationFee
      </td>
    </tr>

    <tr>
      <td>
        POST /cards/\{publicToken}/pin
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        GET /cards/\{publicToken}/pin/status
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        POST /cards/\{publicToken}/pin/unblock
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        GET /cards/\{publicToken}/cvv
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        GET /cards/\{publicToken}/cvv/status
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        PUT /cards/\{publicToken}/cvv/status
      </td>

      <td>
        N/A
      </td>

      <td>
        PINCVVServiceFee
      </td>
    </tr>

    <tr>
      <td>
        POST /cards/\{publicToken}/renew
      </td>

      <td>
        N/A
      </td>

      <td>
        CardReplacementFee
      </td>
    </tr>

    <tr>
      <td>
        POST /cards/\{publicToken}/replace
      </td>

      <td>
        RenewStep is empty or RenewState is Renew or RenewStep is RenewWithSameExpiry
      </td>

      <td>
        CardReplacementFee
      </td>
    </tr>

    <tr>
      <td>
        POST  /cards/\{public Token}/cardType
      </td>

      <td>
        CardType is Physical
      </td>

      <td>
        CardConversionFee
      </td>
    </tr>
  </tbody>
</Table>

> 👍 Documentation
>
> For more details on Web Service Fees, see [Web Service Fees](https://cardsapidocs.thredd.com/docs/web-service-fees)