# Get Card Payment Tokens - Field Descriptions

The following page details each of the fields received in the response when using the Get Card Payment Tokens endpoint.

## Response Fields

A successful response for the Get Card Payment Tokens endpoint will return a 200 response.

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
        id
      </td>

      <td>
        Unique payment token identifier for the Mastercard Digital Enablement Services (MDES) or Visa Digital Enablement Program (VDEP) card.
      </td>
    </tr>

    <tr>
      <td>
        walletId
      </td>

      <td>
        Unique identifier of the wallet provider this payment token is linked to (e.g., APPLE, ANDROID, SAMSUNG).
      </td>
    </tr>

    <tr>
      <td>
        walletProvider
      </td>

      <td>
        Name of the wallet provider this payment token is linked to (e.g., Apple, Android, Samsung).
      </td>
    </tr>

    <tr>
      <td>
        tokenPAN
      </td>

      <td>
        PThe funding PAN (card PAN), with only the last four digits shown.
      </td>
    </tr>

    <tr>
      <td>
        **statuses**
      </td>

      <td>
        Object that contains different statuses for the payment token.
      </td>
    </tr>

    <tr>
      <td>
        tokenisedStatus
      </td>

      <td>
        Tokenised status of this payment token: U = unknown; 0 = not tokenised; 1=tokenised.
      </td>
    </tr>

    <tr>
      <td>
        authorisationStatus
      </td>

      <td>
        Status of the authorisation to digitise this payment token:

        U = unknown

        0 = approve digitisation request

        A = approve digitisation request (with additional authentication)

        1 = decline digitisation request

        * \*Note:\*\* this is not the same as a transaction authorisation.
      </td>
    </tr>

    <tr>
      <td>
        authorisationDecision
      </td>

      <td>
        Final tokenisation decision:

        U = unknown

        0 = approve digitisation request

        A = approve digitisation request (with additional authentication).
      </td>
    </tr>

    <tr>
      <td>
        transactionStatus
      </td>

      <td>
        Status of the payment token as received from the payment token creator (normally Visa or Mastercard). After tokenisation, this is not changed by Thredd.

        A = Active

        D = Deleted (once in this status, it is normally never changed)

        I = Inactive

        N = Not Tokenised

        P = Pending

        S = Suspended

        U = Unknown

        X = Deactivated
      </td>
    </tr>

    <tr>
      <td>
        gpsStatusInfo
      </td>

      <td>
        Device status on the Thredd system. Options include:

        A = Active

        D = Deleted (once in this status, it is normally never changed)

        I = Inactive

        N = Not Tokenised

        P = Pending

        S = Suspended

        U = Unknown

        X = Deactivated
      </td>
    </tr>

    <tr>
      <td>
        **statuses**
      </td>

      <td />
    </tr>

    <tr>
      <td>
        tokenisedDate
      </td>

      <td>
        Tokenised date. Format YYYY-MM-DD.
      </td>
    </tr>

    <tr>
      <td>
        expiryDate
      </td>

      <td>
        Token expiry date. Format YYYY-MM-DD.
      </td>
    </tr>

    <tr>
      <td>
        tokenType
      </td>

      <td>
        The payment token type. For example: C (Contactless Device PAN), CF (Card on File PAN).
      </td>
    </tr>

    <tr>
      <td>
        deviceType
      </td>

      <td>
        The type of technology linked to the token. For example: F (Fob or key-fob), M (Mobile phone), P (Personal computer).
      </td>
    </tr>

    <tr>
      <td>
        deviceName
      </td>

      <td>
        Name of the cardholder assigned to the device in the wallet.
      </td>
    </tr>

    <tr>
      <td>
        merchantName
      </td>

      <td>
        The merchant name (name of the token requester). For example: Amazon, Apple Pay, Google Pay.
      </td>
    </tr>
  </tbody>
</Table>