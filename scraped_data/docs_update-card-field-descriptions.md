# Update Card - Field Descriptions

The following page details each of the fields that can be used in the request, and received in the response when using the Update Card endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when updating a card.

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
        customerReference
      </td>

      <td style={{ textAlign: "left" }}>
        An external customer reference provided in the request.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        25
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
        language3ds
      </td>

      <td style={{ textAlign: "left" }}>
        The language to apply to the 3DS challenge screens displayed to the cardholder. (In BCP-47 format. For example: en-EN,fr-FR.)

        Note: The language content must first be set up for your card products; once this is done, your 3DS Implementation Manager will share with you the language codes to use.

        Note: Default language is English. If card level value is not provided, then the product level setting will be used.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        20
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        designId
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the card visual design.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        parentCard
      </td>

      <td style={{ textAlign: "left" }}>
        Where the card is a secondary card, the public token of the primary card.
      </td>

      <td style={{ textAlign: "left" }}>
        9
      </td>

      <td style={{ textAlign: "left" }}>
        10
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
        freetext1
      </td>

      <td style={{ textAlign: "left" }}>
        A free text field to communicate details to the card manufacturer.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        A free text field to communicate details to the card manufacturer.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        updatedBy
      </td>

      <td style={{ textAlign: "left" }}>
        User who updated the card details.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        networkSharingOptOut
      </td>

      <td style={{ textAlign: "left" }}>
        Enables you specify whether the card should be opted out of the Visa Account Updater (VAU) or Automated Billing Updater (ABU), which provide merchants with account advice information.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        url
      </td>

      <td style={{ textAlign: "left" }}>
        This value is included in the Thredd Card Generation file, in the QRCode field. For example: [https://www.example.com/QRBalance/123456789](https://www.example.com/QRBalance/123456789) For details, see the [Card Generation Interface Specifications](https://docs.thredd.com/Card_Generation_Interface_Specification.htm).
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        oobAppUrl
      </td>

      <td style={{ textAlign: "left" }}>
        3DS OOBAppURL at card level.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        2048
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
        **cardHolder**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the cardholder object are used to capture information on the cardholder.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        title
      </td>

      <td style={{ textAlign: "left" }}>
        Title of the cardholder.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        5
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
        firstName
      </td>

      <td style={{ textAlign: "left" }}>
        First name of the cardholder.

        * *Note:* \*Any unpermitted characters are removed using string cleaning when submitting this field.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        middleName
      </td>

      <td style={{ textAlign: "left" }}>
        Middle name of cardholder.

        * *Note:* \*Any unpermitted characters are removed using string cleaning when submitting this field.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        lastName
      </td>

      <td style={{ textAlign: "left" }}>
        Last name of the cardholder.

        * *Note:* \*Any unpermitted characters are removed using string cleaning when submitting this field.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        dateOfBirth
      </td>

      <td style={{ textAlign: "left" }}>
        Date of Birth of the cardholder. Format YYYY-MM-DD.
      </td>

      <td style={{ textAlign: "left" }}>
        10
      </td>

      <td style={{ textAlign: "left" }}>
        10
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
        mobile
      </td>

      <td style={{ textAlign: "left" }}>
        Mobile number of cardholder.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        16
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
        email
      </td>

      <td style={{ textAlign: "left" }}>
        Email address of the cardholder.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        **address**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the address object are used to capture the cardholder's address.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        addressLine1
      </td>

      <td style={{ textAlign: "left" }}>
        First line of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        addressLine2
      </td>

      <td style={{ textAlign: "left" }}>
        Second line of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        addressLine3
      </td>

      <td style={{ textAlign: "left" }}>
        Third line of the address.
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
        city
      </td>

      <td style={{ textAlign: "left" }}>
        City name.
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
        county
      </td>

      <td style={{ textAlign: "left" }}>
        County, region or province.
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
        postCode
      </td>

      <td style={{ textAlign: "left" }}>
        Postcode / Zip code of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        16
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
        country
      </td>

      <td style={{ textAlign: "left" }}>
        Country of residence. This is represented as a 3-letter alphanumeric ISO country code (e.g. GBR for UK). See the [IBAN list of country codes](https://www.iban.com/country-codes) for a full list.
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
        state
      </td>

      <td style={{ textAlign: "left" }}>
        State of the address
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
        **fulfilment**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the fulfilment object are used to capture the cardholder's fulfilment address.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        addressLine1
      </td>

      <td style={{ textAlign: "left" }}>
        First line of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        addressLine2
      </td>

      <td style={{ textAlign: "left" }}>
        Second line of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        addressLine3
      </td>

      <td style={{ textAlign: "left" }}>
        Third line of the address.
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
        city
      </td>

      <td style={{ textAlign: "left" }}>
        City name.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        state
      </td>

      <td style={{ textAlign: "left" }}>
        State.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        county
      </td>

      <td style={{ textAlign: "left" }}>
        County, region or province.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        100
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
        postCode
      </td>

      <td style={{ textAlign: "left" }}>
        Postcode / Zip code of the address.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        16
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
        country
      </td>

      <td style={{ textAlign: "left" }}>
        Country of residence. This is represented as a 3-letter alphanumeric ISO country code (e.g. GBR for UK). See the [IBAN list of country codes](https://www.iban.com/country-codes) for a full list.
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
        nameOnCard
      </td>

      <td style={{ textAlign: "left" }}>
        The name that appears on the card. Note this is mandatory for physical card types.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        26
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        * *Yes* \*for physical cards,**No** for MVC and virtual cards.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **manufacturingDetails**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the manufacturingDetails object are used to capture the manufacturing details required for a physical card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        thermalLine1
      </td>

      <td style={{ textAlign: "left" }}>
        Free text field which can be used for transferring extra information to be printed on the card.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        120
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
        thermalLine2
      </td>

      <td style={{ textAlign: "left" }}>
        Free text field which can be used for transferring extra information to be printed on the card.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        70
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
        embossLine4
      </td>

      <td style={{ textAlign: "left" }}>
        Embossed card line 4. Actual maximum length will depend on the card design.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        27
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
        **config3dSecure**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the config3dSecure obejct are used to display values related to 3DS configuration for the card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        language3ds
      </td>

      <td style={{ textAlign: "left" }}>
        The language to apply to the 3DS challenge screens displayed to the cardholder. (In BCP-47 format. For example: en-EN,fr-FR.)

        Note: The language content must first be set up for your card products; once this is done, your 3DS Implementation Manager will share with you the language codes to use.

        Note: Default language is English. If card level value is not provided, then the product level setting will be used.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        20
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **apataConfig**
      </td>

      <td style={{ textAlign: "left" }}>
        The fields for the apataConfig object are used to display values related to the Apata 3DS configuration for the card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        cardProgramId
      </td>

      <td style={{ textAlign: "left" }}>
        Sets the card program identifier.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        255
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        challengeProfileId
      </td>

      <td style={{ textAlign: "left" }}>
        Sets the challenge profile identifier.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        255
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        kbaNumberOfQuestionsToAnswer
      </td>

      <td style={{ textAlign: "left" }}>
        Sets the KBA number of questions to answer.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        kbaNumberOfIncorrectPermissible
      </td>

      <td style={{ textAlign: "left" }}>
        Sets the KBA number of incorrect permissible
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>
  </tbody>
</Table>