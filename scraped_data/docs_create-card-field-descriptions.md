# Create Card - Field Descriptions

The following page describes each of the fields that can be used in the request, and received in the response when using the Create Card endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when creating a card.

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
        cardType
      </td>

      <td style={{ textAlign: "left" }}>
        The type of card. Select from:

        * physical
        * virtual
        * masterVirtual
      </td>

      <td style={{ textAlign: "left" }}>
        7
      </td>

      <td style={{ textAlign: "left" }}>
        13
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
        cardProduct
      </td>

      <td style={{ textAlign: "left" }}>
        The unique ID of the card product linked to the card.
      </td>

      <td style={{ textAlign: "left" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        2147483647
      </td>

      <td style={{ textAlign: "left" }}>
        int32
      </td>

      <td style={{ textAlign: "left" }}>
        Yes
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
        parentCard
      </td>

      <td style={{ textAlign: "left" }}>
        Where there is a secondary card, the public token of the primary card.
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
        expiryDate
      </td>

      <td style={{ textAlign: "left" }}>
        The Expiry Date that is embossed on the card. Format YYYY-MM.
      </td>

      <td style={{ textAlign: "left" }}>
        7
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
        freeText1
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
        freeText2
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
        nameOnCard
      </td>

      <td style={{ textAlign: "left" }}>
        The name that appears on the card. **Note**:  This is mandatory for physical card types. Leave blank for other card types.
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
        *Yes* \*for physical cards,**No** for MVC and virtual cards.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        activateNow
      </td>

      <td style={{ textAlign: "left" }}>
        If true, will set the card status as active on creation of the card. Defaults to false for a physical card. Defaults to true for a virtual card.
      </td>

      <td style={{ textAlign: "left" }}>
        0
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
        IsSingleUse
      </td>

      <td style={{ textAlign: "left" }}>
        If true, the created card is only allowed for a single spend transaction only.
      </td>

      <td style={{ textAlign: "left" }}>
        0
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
        IsNonReloadable
      </td>

      <td style={{ textAlign: "left" }}>
        If true, the card is only allowed to have a single load.
      </td>

      <td style={{ textAlign: "left" }}>
        0
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
        language3ds
      </td>

      <td style={{ textAlign: "left" }}>
        Sets the 3DS Apata Enrolment language for the card. Language must be a valid BSP-47 code. The default value is `en-GB`.
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
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        oobAppUrl
      </td>

      <td style={{ textAlign: "left" }}>
        Enables you to set the correct URL for out-of-band (OOB) authentication processes for 3DS. This is applicable for both Apata and Cardinal customers.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        2048
      </td>

      <td style={{ textAlign: "left" }}>
        URI
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
        The cardHolder object contains fields that are used to capture the details of the cardholder.
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
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        firstName
      </td>

      <td style={{ textAlign: "left" }}>
        First name of the cardholder.

        **Note:** Any unpermitted characters are removed using string cleaning when submitting this field.
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
        Yes
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        middleName
      </td>

      <td style={{ textAlign: "left" }}>
        Middle name of cardholder.

        **Note:** Any unpermitted characters are removed using string cleaning when submitting this field.
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
        lastName
      </td>

      <td style={{ textAlign: "left" }}>
        Last name of the cardholder.

        **Note:** Any unpermitted characters are removed using string cleaning when submitting this field.
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
        Mobile number of the cardholder.
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
        The address object contains fields that are used to capture the cardholder's address. Also used for the card purchaser's address details if no 'fulfilment' address field details are supplied.
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
        First line of the address. Mandatory if ‘Address’ fields are specified.
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
        state
      </td>

      <td style={{ textAlign: "left" }}>
        State.
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
        country
      </td>

      <td style={{ textAlign: "left" }}>
        Country of residence. This is represented as a 3-letter alphanumeric ISO country code (e.g. GBR for UK). See the

        [IBAN list of country codes](https://www.iban.com/country-codes)

        for a full list.
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
        **fulfilment**
      </td>

      <td style={{ textAlign: "left" }}>
        The fulfilment object contains fields that are used to capture the card purchaser's fulfilment address  — where a separate  delivery address is specified for the card manufacturer to deliver the card.
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
        addressLine1
      </td>

      <td style={{ textAlign: "left" }}>
        First line of the address. Mandatory if a fulfilment address is specified.
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
        Postcode / Zip code of the address. Mandatory if a fulfilment address is specified.
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
        Country of residence. This is represented as a 3-letter alphanumeric ISO country code (e.g. GBR for UK). See the

        [IBAN list of country codes](https://www.iban.com/country-codes)

        for a full list.
        Mandatory if a fulfilment address is specified.
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
        **virtualCardImageDetails**
      </td>

      <td style={{ textAlign: "left" }}>
        The virtualCardImageDetails object contains fields that are used to capture the Image details required for a virtual card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        virtualCardImageId
      </td>

      <td style={{ textAlign: "left" }}>
        The image ID for the virtual card.
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
        imageSize
      </td>

      <td style={{ textAlign: "left" }}>
        The image size of the virtual card as a multiple of 100%. For example, 1 is 100%, 2 is 200%.
      </td>

      <td style={{ textAlign: "left" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        int32
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **manufacturingDetails**
      </td>

      <td style={{ textAlign: "left" }}>
        The manufacturingDetails object contains fields that are used to capture the manufacturing details required for the physical card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        deliveryMethod
      </td>

      <td style={{ textAlign: "left" }}>
        The delivery method for the physical card.
      </td>

      <td style={{ textAlign: "left" }}>
        15
      </td>

      <td style={{ textAlign: "left" }}>
        21
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
        carrierType
      </td>

      <td style={{ textAlign: "left" }}>
        Carrier Product Design reference as used by the card printer.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        language
      </td>

      <td style={{ textAlign: "left" }}>
        The language used on the card.
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        2
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
        thermalLine1
      </td>

      <td style={{ textAlign: "left" }}>
        Free text field for transferring extra information to be printed on the card.
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
        Free text field for transferring extra information to be printed on the card.
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
        Embossed card line 4.
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
        vanityName
      </td>

      <td style={{ textAlign: "left" }}>
        Additional title to the card holder name (for example "Company Director").
      </td>

      <td style={{ textAlign: "left" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        32
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
        **imageDetails**
      </td>

      <td style={{ textAlign: "left" }}>
        The imageDetails object contains fields for capturing image details for a physical card.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        imageId
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the card manufacturer's image file that will be printed on the face of the card.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        logoFrontId
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the card manufacturer's logo file that will be printed on the face of the card.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        logoBackId
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the card manufacturer's logo file that will be printed on the back of the card, if supported.
      </td>

      <td style={{ textAlign: "left" }}>
        1
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
        **dynamicInterchange**
      </td>

      <td style={{ textAlign: "left" }}>
        Object that contains information for dynamic interchange, a Mastercard Wholesale Program (MWP) feature.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        feePercentage
      </td>

      <td style={{ textAlign: "left" }}>
        The interchange rate percentage of a virtual card using the Mastercard Wholesale Program (MWP).
      </td>

      <td style={{ textAlign: "left" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        2147483647
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        No
      </td>
    </tr>
  </tbody>
</Table>

## Response Fields

The following table describes fields that included in the response after successfully creating a card.

| Field             | Description                                              |
| :---------------- | :------------------------------------------------------- |
| publicToken       | The unique identifier for the card.                      |
| customerReference | The external customer reference provided in the request. |
| embossName        | The name embossed on the card.                           |
| maskedPan         | The masked PAN for the card created.                     |
| startDate         | The start date of the card.                              |
| expiryDate        | The expiry date of the card.                             |