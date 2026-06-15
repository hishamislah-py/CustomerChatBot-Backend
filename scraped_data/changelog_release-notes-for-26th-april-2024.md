# Release Notes for 26th April 2024

New changes to the Thredd Cards API for the week ending 26th April 2024.

* [New behaviour when unloading MVC cards](#new-behaviour-when-unloading-mvc-cards)
* [New fields added to Get Token Details response](#new-fields-added-to-get-token-details-response)

## New behaviour when unloading MVC cards

New optional behaviour has been added when unloading MVC cards of restricting an unload that is more than the balance of the MVC.

> 👍 Note
>
> This behaviour must be enabled before it can be used. Please contact application support via your implementations manager to discuss enabling this functionality.

For example, if the MVCs balance is £800 and the unload is for a value of £1000, then a 400 response can be returned with the below message.

```Text Example MVC Unload error response
{
Cannot unload due to insufficient fund.  
}
```

> 📘 Information
>
> For more information on MVCs, see [Master Virtual Cards](https://cardsapidocs.thredd.com/docs/master-virtual-cards).

## New fields added to Get Token Details response

New fields have been added to the response for the Get Token Details endpoint. This change expands the details returned when querying a token associated with a publicToken.

The following table describes the new fields for the Get Token Details endpoint.

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
        Wallet service provider tokenization recommendation reason codes.
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
        Which activation method was used:

        0 = none;

        1 = SMS to mobile phone;

        2 = email;

        3 = cardholder called an automated call centre;

        4 = cardholder called a human call centre;

        5 = website;

        6 = mobile application;

        7 = voice phone call
      </td>
    </tr>

    <tr>
      <td>
        activationStatus
      </td>

      <td>
        The payment token's activation status:

        Status is 'R' when Reason code  = 00\
        Status is 'T' when Reason code  = 01\
        Status is 'F' when Reason code  = 02
      </td>
    </tr>

    <tr>
      <td>
        walletId
      </td>

      <td>
        Name of the wallet provider this payment token uses (e.g., APPLE, ANDROID, SAMSON).
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
        The type of device used at the terminal.
      </td>
    </tr>

    <tr>
      <td>
        deviceName
      </td>

      <td>
        Name the cardholder assigned to the device in the wallet.
      </td>
    </tr>

    <tr>
      <td>
        merchantName
      </td>

      <td>
        The name of the merchant for the transaction.
      </td>
    </tr>
  </tbody>
</Table>

See the below example of a successful Get Token Details response.

```json Example Get Token Details response
{
    "creatorTokenReference": "DAPLMC0000239565f52605b88199440da31349c23457eeb5",
    "cardUsageGroup": "TES-CU-001 - Test CR",
    "paymentTokenUsageGroup": "CORPT-0001 - TXN_Default",
    "walletAccountScore": 5,
    "walletDeviceScore": 3,
    "walletReasons": "000000000010000000000000",
    "transactionID": 0,
    "responseCode": null,
    "transactionDate": null,
    "cardAcceptorNameLocation": "",
    "bnReference": "",
    "mtid": null,
    "ehiRequestTime": null,
    "ehiResponseTime": null,
    "activationCode": "297147",
    "activationMethod": "Email",
    "activationStatus": "",
    "id": 6783,
    "walletId": "APPLE",
    "walletProvider": "Apple",
    "tokenPAN": "1321",
    "statuses": {
        "tokenisedStatus": {
            "code": "1",
            "description": "Tokenised"
        },
        "authorisationStatus": {
            "code": "A",
            "description": "Approve with Authentication"
        },
        "authorisationDecision": {
            "code": "A",
            "description": "Approve with Authentication"
        },
        "transactionStatus": {
            "code": "A",
            "description": "Active"
        },
        "gpsStatusInfo": {
            "code": "83",
            "description": "Deactivated"
        }
    },
    "tokenisedDate": "01/17/2020 08:48:06",
    "expiryDate": "12/31/2022 00:00:00",
    "tokenType": "Secure Element PAN",
    "deviceType": "Unknown",
    "deviceName": "iPhone",
    "merchantName": null
}
```

> 📘 Information
>
> For more information on Get Payment Details, see [Get Card Payment Token Details](https://cardsapidocs.thredd.com/docs/get-card-payment-token-details).