# Get Card Payment Token Details - Field Descriptions

The following page details each of the fields received in the response when using the Get Card Payment Token Details endpoint.

## Response Fields

A successful response for the Get Card Payment Token Details endpoint will return a 200 response.

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
        The unique payment token identifier.
      </td>
    </tr>

    <tr>
      <td>
        walletId
      </td>

      <td>
        Name of the wallet provider this payment token uses (e.g., APPLE, ANDROID, SAMSUNG).
      </td>
    </tr>

    <tr>
      <td>
        walletProvider
      </td>

      <td>
        The name of the wallet provider. For example Apple or Google.
      </td>
    </tr>

    <tr>
      <td>
        tokenPAN
      </td>

      <td>
        PAN token for the card linked to the MDES or VTS card.
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
        Status of the authorisation to digitise this payment token:\
        U = unknown\
        0 = approve digitisation request\
        A = approve digitisation request (with additional authentication)\
        1 = decline digitisation request

        * \*Note:\*\* this is not the same as a transaction authorisation.
      </td>
    </tr>

    <tr>
      <td>
        authorisationDecision
      </td>

      <td>
        Final tokenisation decision:\
        U = unknown\
        0 = approve digitisation request\
        A = approve digitisation request (with additional authentication).
      </td>
    </tr>

    <tr>
      <td>
        transactionStatus
      </td>

      <td>
        Status of the payment token as received from the payment token creator (normally Visa or Mastercard). After tokenisation, this is not changed by Thredd.\
        A = Active\
        D = Deleted (once in this status, it is normally never changed)\
        I = Inactive\
        N = Not Tokenised\
        P = Pending\
        S = Suspended\
        U = Unknown\
        X = Deactivated
      </td>
    </tr>

    <tr>
      <td>
        gpsStatusInfo
      </td>

      <td>
        Device status on the Thredd system. Options include:\
        A = Active\
        D = Deleted (once in this status, it is normally never changed)\
        I = Inactive\
        N = Not Tokenised\
        P = Pending\
        S = Suspended\
        U = Unknown\
        X = Deactivated
      </td>
    </tr>

    <tr>
      <td>
        **statuses**
      </td>

      <td>
        End of the **statuses** object..
      </td>
    </tr>

    <tr>
      <td>
        tokenisedDate
      </td>

      <td>
        Date and time when tokenised, in the format: yyyy-mm-ddhhmmss.
      </td>
    </tr>

    <tr>
      <td>
        expiryDate
      </td>

      <td>
        Expiry date of the payment token.
      </td>
    </tr>

    <tr>
      <td>
        tokenType
      </td>

      <td>
        Payment token type.
      </td>
    </tr>

    <tr>
      <td>
        deviceType
      </td>

      <td>
        The type of device enabled for tokenised payments for this token.
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
        The name of the merchant that created the token.
      </td>
    </tr>

    <tr>
      <td>
        creatorTokenReference
      </td>

      <td>
        The token creator's unique reference for this payment token. (Mastercard Token Unique Reference (TUR) and Visa Token reference ID.)
      </td>
    </tr>

    <tr>
      <td>
        cardUsageGroup
      </td>

      <td>
        The card usage group the token is associated with.
      </td>
    </tr>

    <tr>
      <td>
        paymentTokenUsageGroup
      </td>

      <td>
        The payment token usage group the token is associated with.
      </td>
    </tr>

    <tr>
      <td>
        walletAccountScore
      </td>

      <td>
        Risk score for the account, received from the wallet provider during digitisation:

        1 = highest risk; 2 = higher risk; 3 = neutral; 4 = lower risk; 5 = least risk
      </td>
    </tr>

    <tr>
      <td>
        walletDeviceScore
      </td>

      <td>
        Risk score for the device received from the wallet provider during digitisation:

        1 = highest risk; 2 = higher risk; 3 = neutral; 4 = lower risk; 5 = least risk
      </td>
    </tr>

    <tr>
      <td>
        walletReasons
      </td>

      <td>
        Wallet service provider tokenization recommendation reason codes. For details, see [Wallet Tokenisation Reason Codes](https://docs.thredd.com/webservices/Content/Reference/Wallet_Tokenisation_Reason_Codes.htm)
      </td>
    </tr>

    <tr>
      <td>
        transactionID
      </td>

      <td>
        The unique identifier for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        responseCode
      </td>

      <td>
        The action code for the response.
      </td>
    </tr>

    <tr>
      <td>
        transactionDate
      </td>

      <td>
        The date and time of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        cardAcceptorNameLocation
      </td>

      <td>
        The location of the card acceptor, which can be a merchant or an ATM where the transaction occurred.
      </td>
    </tr>

    <tr>
      <td>
        bnReference
      </td>

      <td>
        The network reference.
      </td>
    </tr>

    <tr>
      <td>
        mtid
      </td>

      <td>
        The Message Type Identifier (MTID) for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        ehiRequestTime
      </td>

      <td>
        The date and time the EHI received the request.
      </td>
    </tr>

    <tr>
      <td>
        ehiResponseTime
      </td>

      <td>
        The date and time the EHI responded to the request.
      </td>
    </tr>

    <tr>
      <td>
        activationCode
      </td>

      <td>
        Activation code to be sent directly to the cardholder to activate this payment token.
      </td>
    </tr>

    <tr>
      <td>
        activationMethod
      </td>

      <td>
        Which activation method was used:\
        0 = none;\
        1 = SMS to mobile phone;\
        2 = email;\
        3 = cardholder called an automated call centre;\
        4 = cardholder called a human call centre;\
        5 = website;\
        6 = mobile application;\
        7 = voice phone call
      </td>
    </tr>

    <tr>
      <td>
        activationStatus
      </td>

      <td>
        The payment token's activation status:

        Status is 'R' when Reason code = 00\
        Status is 'T' when Reason code = 01\
        Status is 'F' when Reason code = 02
      </td>
    </tr>
  </tbody>
</Table>