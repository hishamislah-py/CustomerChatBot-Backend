# Release Notes for 15th March 2024

New changes to the Thredd Cards API for the week ending 15th March 2024.

* [New fields added to Get 3DS Configuration endpoint](#new-fields-added-to-get-3ds-configuration-endpoint)
* [New fields added to Get Card Transactions endpoint](#new-fields-added-to-get-card-transactions-endpoint)
* [Max Length of imageId field in Create Card endpoint changed](#max-length-of-imageid-field-in-create-card-endpoint-changed)
* [Max Length of postcode field changed](#max-length-of-postcode-field-changed)
* [New Validation for Update Card endpoint](#new-validation-for-update-card-endpoint)
* [Bulk Card Performance Improvements](#bulk-card-performance-improvements)

## New fields added to Get 3DS Configuration endpoint

The following fields have been added to the response of the Get 3DS Configuration endpoint:

| Field                   | Description                                                                | Data Type |
| :---------------------- | :------------------------------------------------------------------------- | :-------- |
| hasBiometricCredentials | If true, confirms that biometric credentials exist for the public token.   | Boolean   |
| hasOOBCredentials       | If true, confirms that Out of Band credentials exist for the public token. | Boolean   |

The `hasBiometricCredentials `and `hasOOBCredentials `fields display in the biometric object of the response. See the below example response:

```json Example Get 3DS Configuration response
{
    "provider": 4,
    "programManager": {
        "programManagerCode": "PMT",
        "shortName": "GPSDUMMY"
    },
    "mobile": "8988",
    "email": null,
    "isActive": true,
    "status": "00",
    "has3dSecureCredentialEntry": true,
    "apataConfig": {
        "cardProgramId": "sudbhcfndjfncvfhgn",
        "challengeProfileId": "rshgbvbhmbhverdctgvrwe",
        "financialInstitutionId": "egegdfbvcvskdfng",
        "numberOfQuestionsToAnswer": 0,
        "numberIncorrectPermissible": 0,
        "language": "en-EN"
    },
    "kba": [],
    "otpSms": {
        "otpSmsTemplateFullFormat": null,
        "otpSmsTemplateDefaultFormat": null
    },
    "biometric": {
        "autoEnrol3DSBiometrics": 0,
        "autoEnrol3DSOOB": 0,
        "biometricUrl": null,
        "hasBiometricCredentials": false,
        "hasOOBCredentials": false
    }
}
```

## New fields added to Get Card Transactions endpoint

The following fields have been added to the response of the Get Card Transactions endpoint:

| Field              | Description                                                                                                                                                    | Data Type |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| payment\_token\_id | Unique identifier of the payment token, if applicable. This is used to communicate about a token without using a payment token.                                | String    |
| payment\_method    | The type of payment method. This will be either `Payment` (if the payment was made using a card), or `Wallet` (if the payment was made with a digital wallet). | String    |

See the below example of the fields included in a Get Card Transactions endpoint response.

```json Example Get Card Transactions endpoint response
[
    {
        "id": 6160502008,
        "description": "string",
        "dateTime": "2024-02-20T14:16:18.34Z",
        "lifeCycleId": null,
        "type": {
            "code": "U",
            "description": "Unload"
        },
        "status": {
            "code": "S",
            "description": "Settled"
        },
        "amount": {
            "billingValue": 50.00,
            "billingCurrency": "GBP",
            "transactionValue": 50.0000,
            "transactionCurrency": "GBP",
            "settlementAmount": 50.00,
            "settlementCurrency": "GBP",
            "actualBalance": 1950.00,
            "availableBalance": 1950.00
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
        "processingCode": "230000",
        "recordId": 0,
        "note": "API Load by ",
        "systemTraceAuditNumber": 0,
        "transactionCountry": "GBR",
        "transactionLink": 6160502008,
        "additionalDetail": null,
        "paymentTokenId": null,
        "paymentMethod": "None"
    }
  ]
```

## Max Length of imageId field in Create Card endpoint changed

The max length of the imageId field in the Create Card endpoint has changed to a limit of 16 characters. This has been done to match the behaviour of the equivalent field in SOAP.

## Max Length of postcode field changed

The max length of the postcode field has changed to a limit of 10 characters. This has been done to match the behaviour of the equivalent field in SOAP. This change affects the following endpoints:

* Create Card endpoint
* Update Card endpoint

## New Validation for Update Card endpoint

The Update Card endpoint has been updated to include new validation when hitting errors. Previously, the Update Card endpoint returned generic error messages. See below for some examples on new validation added to the endpoint.

```json Example customerReference field validation response
{
    "type": "https://tools.ietf.org/html/rfc4918#section-11.2",
    "title": "One or more validation errors occurred.",
    "status": 422,
    "traceId": "00-292943609b34d054309ec06e60151069-80a46f8038ff48a9-00",
    "errors": {
        "CustomerReference": [
            "The field CustomerReference must be a string with a maximum length of 25."
        ]
    }
}
```

```json Example dateOfBirth validation response
{
    "type": "https://tools.ietf.org/html/rfc4918#section-11.2",
    "title": "One or more validation errors occurred.",
    "status": 422,
    "traceId": "00-a643179f97eb064c72d2dbadeee83564-72def21dc9ce830d-00",
    "errors": {
        "CardHolder.DateOfBirth": [
            "The field DateOfBirth must be a date & time in the format: yyyy-MM-dd."
        ]
    }
}
```

## Bulk Card Performance Improvements

The creation of Bulk Cards has been improved in this release.