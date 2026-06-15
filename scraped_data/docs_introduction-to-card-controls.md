# Introduction to Card Control Groups

Card control groups control what the <Glossary>Cardholder</Glossary> can do with the card, as well as the various card usage fees that they receive. You need to enter the default card control groups on your *Product Setup Form (PSF)*. Your Thredd Implementation Manager then ensures that these are configured on the system.

You can use the Update Card Control Groups API to you change the card groups assigned to the card at a later stage if needed.

The following table describes the Card Control Groups:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Group ID
      </th>

      <th>
        Group
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        0
      </td>

      <td>
        limitsGroup
      </td>

      <td>
        Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in *Smart Client*.
      </td>
    </tr>

    <tr>
      <td>
        1
      </td>

      <td>
        usageGroup
      </td>

      <td>
        Controls where a card can be used; for example,  POS or ATM.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        recurringFeeGroup
      </td>

      <td>
        Controls whether a card is charged a recurring fee, such as a monthly platform fee.
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        webServiceFeeGroup
      </td>

      <td>
        **Note:** webServiceFeeGroup is no longer available for Thredd’s REST service.
        Controls the fees charged for Web service usage. Different web services can have different fees associated with them.
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        authFeeGroup
      </td>

      <td>
        Controls the card transaction authorisation fees.
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        mccGroup
      </td>

      <td>
        Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes to define the trading category of the merchant.
      </td>
    </tr>

    <tr>
      <td>
        6
      </td>

      <td>
        cardLinkageGroup
      </td>

      <td>
        The Linkage Group set up in Smart Client controls various parameters related to linked cards. For details, check with your Implementation Manager.
      </td>
    </tr>

    <tr>
      <td>
        7
      </td>

      <td>
        calendarGroup
      </td>

      <td>
        Controls when authorisations on a card are allowed. You can use this option to control when the card can be used. For example, to prevent usage on weekends or out of hours.
      </td>
    </tr>

    <tr>
      <td>
        8
      </td>

      <td>
        fxGroup
      </td>

      <td>
        Controls the rates for FX currency conversions if the purchase currency is different from the card's currency.
      </td>
    </tr>

    <tr>
      <td>
        9
      </td>

      <td>
        paymentTokenUsageGroup
      </td>

      <td>
        Defines configuration options specific to the provisioning of a digital payment token. For details, see the *Tokenisation Guide*.
      </td>
    </tr>

    <tr>
      <td>
        10
      </td>

      <td>
        cardAcceptorAllowList
      </td>

      <td>
        Enables you to associate a card with the Card Acceptor (MerchantID) Allow list.
      </td>
    </tr>

    <tr>
      <td>
        11
      </td>

      <td>
        cardAcceptorDisallowList
      </td>

      <td>
        Enables you to associate a card with the Card Acceptor (MerchantID) Disallow list.
      </td>
    </tr>
  </tbody>
</Table>