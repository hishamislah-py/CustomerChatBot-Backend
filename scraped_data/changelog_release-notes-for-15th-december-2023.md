# Release Notes for 15th December 2023

New changes to the Thredd Cards API for the week ending 15th December 2023.

* [Updated Create 3DS Credentials endpoint to support Behavioural Biometric credential type](#updated-create-3ds-credentials-endpoint-to-support-behavioural-biometric-credential-type)
* [Expiry date format updated for Get Card Image endpoint](#expiry-date-format-updated-for-get-card-image-endpoint)
* [Single Use and Non-Reloadable flags added to Get Product endpoint response](#single-use-and-non-reloadable-flags-added-to-get-product-endpoint-response)
* [Balance information added to Get Card Transactions endpoint response](#balance-information-added-to-get-card-transactions-endpoint-response)
* [Card Acceptor IDs added to Get Card endpoint response](#card-acceptor-ids-added-to-get-card-endpoint-response)
* [Validation Added to dateOfBirth field for Create Card and Update Card endpoints](#validation-added-to-dateofbirth-field-for-create-card-and-update-card-endpoints)
* [Updated field length for Name fields](#updated-field-length-for-name-fields)
* [Update Card Controls Group endpoint temporarily removed](#update-card-controls-group-endpoint-temporarily-removed)

## Updated Create 3DS Credentials endpoint to support Behavioural Biometric credential type

Behaviour biometric credential types are now supported in the Create 3DS Credentials endpoint. This type is only valid for programs using the Apata platform for their 3DS.  An error is returned in the response if the program uses a different platform for 3DS.

The following example displays a request body using the behavioural biometric type.

```json Example Create 3DS Credential body
{
  "type": "BEHAVIOURALBIOMETRIC",
  "value": "07"
}
```

If successful, a 200 response will be returned with the unique 3DS identifier. See[ Introduction to 3D Secure](https://cardsapidocs.thredd.com/docs/introduction-to-3d-secure) for more details.

## Expiry Date format updated for Get Card Image endpoint

The Expiry Date format has been updated to MM/YY in the Get Card Image endpoint. Previously, the expiry format returned was DD/MM/YY.

## Single Use and Non-Reloadable flags added to Get Product endpoint response

The fields `cardDefaultIsSingleUse` (denoting that the card can only be used once) and `cardDefaultIsNonReloadable` (denoting that the card cannot be reloaded with more money) are now returned in the Get Product response.  See the below example of the response with the fields included.

```json Example Get Product response
{
    "supportedCredentialTypesCsv": null,
    "supportedCredentialTypes": [],
    "defaultCredentialTypeId": null,
    "fallbackCredentialTypeId": null,
    "productId": 10023,
    "accountCode": "01",
    "schemeId": 644,
    "schemeName": "GPS SCHEME TEST",
    "currencyCode": "GBP",
    "groupFeeTranCode": "",
    "groupFeeMasterCode": "",
    "groupFeeWebCode": "",
    "groupMCCCode": "",
    "groupUsageCode": "PMT-CU-001",
    "ehiMode": 3,
    "supplier3DS": "2",
    "supplier3DSVersion": "RDX",
    "fraudManagement": 0,
    "cardDefaultIsSingleUse": null,
    "cardDefaultIsNonReloadable": null
}
```

## Balance information added to Get Card Transactions endpoint response

The fields `actualBalance`and `availableBalance `are now returned in the Get Card Transactions response. These fields are included in the `amount` object. See the below example of the response with the fields included.

```json Example Get Card Transactions response
[
    {
        "id": 6159718325,
        "description": "string",
        "dateTime": "2023-12-07T11:03:38.837Z",
        "lifeCycleId": null,
        "type": {
            "code": "L",
            "description": "Load"
        },
        "status": {
            "code": "S",
            "description": "Settled"
        },
        "amount": {
            "billingValue": 1000.00,
            "billingCurrency": "GBP",
            "transactionValue": 1000.0000,
            "transactionCurrency": "GBP",
            "settlementAmount": 1000.00,
            "settlementCurrency": "GBP",
            "actualBalance": 1000.00,
            "availableBalance": 1000.00
        },
        "fees": {
            "id": 0,
            "fixedFee": 0.00,
            "rateFee": 0.00,
            "fxPadding": 0.00,
            "mccPadding": 0.00
        },
        "productId": 10023,
        "cardNetwork": "MASTERCARD",
        "processingCode": "220000",
        "recordId": 0,
        "note": "API Load by ",
        "systemTraceAuditNumber": 0,
        "transactionCountry": "GBR",
        "transactionLink": 6159718325,
        "additionalDetail": null
    }
]
```

## Card Acceptor IDs added to Get Card endpoint response

A Card Acceptor object (`cardAcceptorIds`) has been added to the Get Card endpoint response. The object includes the fields `allowCardAcceptors` and `disallowCardAcceptors`. See the below example of the response with the fields included.

```json Example Get Card response
{
    "cardType": "Physical",
    "publicToken": "109725272",
    "status": "Inactive",
    "cardStatusCode": "02",
    "cardStatusDescription": "02 (Inactive)",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr. Bruce Smith",
        "maskedPan": "531610******0462",
        "startDate": "2023-10-23",
        "expiryDate": "2028-10-31",
        "clearPan": null,
        "cvv": null
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "Bruce",
        "middleName": "Brian",
        "lastName": "Smith",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "BSmith@email.com"
    },
    "cardProduct": {
        "scheme": "GPS TEST LUCKY No.",
        "product": 10046,
        "productShortName": "Thredd"
    },
    "controlGroups": {
        "limitsGroup": 1051,
        "usageGroup": 1081,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": 0,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0
    },
    "3DS": [],
    "designId": "THREDD",
    "childCards": [],
    "siblingCards": [],
    "address": {
        "addressLine1": "1007",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "GC11 2LD",
        "country": "840"
    },
    "fulfilment": {
        "addressLine1": "1007",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "GC11 2LD",
        "country": "840"
    },
    "freetext1": null,
    "freetext2": null,
    "isSingleUse": null,
    "isNonReloadable": null,
    "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    }
}
```

## Validation Added to dateOfBirth field for Create Card and Update Card endpoints

Validation has been added to the `dateOfBirth` field in the Create Card and Update Card endpoints to ensure that you cannot add a `dateOfBirth` set in the future.

## Updated field length for Name fields

The `firstName`, `middleName` and `lastName` fields have had their max length values updated in this release. This change has been made so that the length matches what is in the card generation file.

| Field        | Old Length | New Length |
| :----------- | :--------- | :--------- |
| `firstName`  | 100        | 20         |
| `middleName` | 100        | 30         |
| `lastName`   | 100        | 30         |

These changes are applicable to the following endpoints:

* [Create Card](https://cardsapidocs.thredd.com/reference/create-card)
* [Update Card](https://cardsapidocs.thredd.com/reference/update-card)

## Update Card Controls Group endpoint temporarily removed

The Update Card Control Groups endpoint has been temporarily removed from the Cards API.