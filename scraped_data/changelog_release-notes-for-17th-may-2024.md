# Release Notes for 20th May 2024

New changes to the Thredd Cards API for the week ending 20th May 2024.

* [New field added to Retrieve Card endpoint response](#new-field-added-to-retrieve-card-endpoint-response)
* [New fields added to Get 3DS Configuration endpoint response](#new-fields-added-to-get-3ds-configuration-endpoint-response)
* [New fields added to Get Product for Program Manager endpoint response](#new-fields-added-to-get-product-for-program-manager-endpoint-response)
* [Updated field behaviour in List 3DS Credentials endpoint](#updated-field-behaviour-in-list-3ds-credentials-endpoint)
* [New validation on Load or Unload Card Endpoint](#new-validation-on-load-or-unload-card-endpoint)

## New field added to Retrieve Card endpoint response

A new field has been added to the Retrieve Card endpoint response. The `activationDate` field has been added to the cardDetails object and includes details of the time and date (in Coordinated Universal Time ‎(UTC)‎) when the card was first activated. See the below example of a successful Retrieve Card response.

```json Example Retrieve Card response
{
    "cardType": "Physical",
    "publicToken": "109725272",
    "status": "Active",
    "cardStatusCode": "00",
    "cardStatusDescription": "00 (Active)",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr. Bruce Simms",
        "maskedPan": "531610******0462",
        "startDate": "2023-10-23",
        "expiryDate": "2028-10-31",
        "clearPan": null,
        "cvv": null,
        "activationDate": "2024-05-14 08:31:33Z"
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "Bruce",
        "middleName": "Brian",
        "lastName": "Simms",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "Bsimms@email.com"
    },
    "cardProduct": {
        "scheme": "GPS TEST LUCKY No.",
        "product": 10046,
        "productShortName": "Thredd"
    },
    "controlGroups": {
        "limitsGroup": 1201,
        "usageGroup": 374,
        "recurringFeeGroup": 287,
        "webServiceFeeGroup": 236,
        "authFeeGroup": 786,
        "mccGroup": 433,
        "cardLinkageGroup": 13,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0,
        "cardAcceptorAllowList": null,
        "cardAcceptorDisallowList": null
    },
    "3DS": [],
    "designId": "THREDD",
    "childCards": [
        109096337
    ],
    "siblingCards": [],
    "address": {
        "addressLine1": "1007 Brick Lane",
        "addressLine2": "",
        "addressLine3": "",
        "city": "Leicester",
        "state": "",
        "county": "Leicestershire",
        "postCode": "LE11 2LD",
        "country": "840"
    },
    "fulfilment": {
        "addressLine1": "1007 Brick Lane",
        "addressLine2": "",
        "addressLine3": "",
        "city": "Leicester",
        "state": "",
        "county": "Leicestershire",
        "postCode": "LE11 2LD",
        "country": "840"
    },
    "freetext1": null,
    "freetext2": null,
    "isSingleUse": null,
    "isNonReloadable": null,
    "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    },
    "language3ds": null
}
```

## New fields added to Get 3DS Configuration endpoint response

Two new fields have been added to the Get 3DS Configuration endpoint. The `providerName` field describes the name of the provider (such as Apata or Cardinal). The `version` field describes the version of the provider (For example, the API version where the provider is Cardinal). See the below example of a successful Get 3DS Configuration response.

```json Example Get 3DS Configuration
{
    "provider": 4,
    "providerName": "Apata",
    "version": "Apata",
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

## New fields added to Get Product for Program Manager endpoint response

A new object (`config3dSecure`) has been added to the Get Product for Program Manager endpoint response. This object has been added to support 3DS Apata product level settings.

The below table describes each of the new fields:

| Field                           | Description                                                                                                                                                                                                                                                                                                                       |
| :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| language                        | The language applied to 3DS challenge screens displayed to the cardholder. BCP-47 is the language format that is used by Apata, for example, en-EN and fr-FR. The language content must first be set up for your card products. When this is done, your 3DS Implementation Manager will share with you the language codes to use. |
| cardProgramId                   | Unique ID configured by Apata to represent the specific card program and associated BIN ranges.                                                                                                                                                                                                                                   |
| challengeProfileId              | Unique ID configured by Apata to represent the challenge profile (default and fallback challenge options).                                                                                                                                                                                                                        |
| kbaNumberOfQuestionsToAnswer    | Number of KBA questions to answer correctly across all questions presented to the cardholder.                                                                                                                                                                                                                                     |
| kbaNumberOfIncorrectPermissable | Number of incorrect answers permissible for KBA across all questions presented to the cardholder.                                                                                                                                                                                                                                 |

See the below example of a successful Get Product for Program Manager response.

```json Example Get Product for Program Manager response
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
    "supplier3DS": "4",
    "supplier3DSName": null,
    "supplier3DSVersion": "Apata",
    "fraudManagement": 0,
    "cardDefaultIsSingleUse": null,
    "cardDefaultIsNonReloadable": null,
    "fraudNotificationMethod": 0,
    "config3dSecure": {
        "language": "en-EN",
        "apata": {
            "cardProgramId": "sudbhcfndjfncvfhgn",
            "challengeProfileId": "rshgbvbhmbhverdctgvrwe",
            "kbaNumberOfQuestionsToAnswer": 0,
            "kbaNumberOfIncorrectPermissible": 0
        }
    }
}
```

## Updated field behaviour in List 3DS Credentials endpoint

From this release, if you query a token using the List 3DS Credentials endpoint and the token does not have 3DS credentials setup for that type of credential, then a **Not Enrolled** response will be returned. See the below example.

```json Example List 3DS Credentials response
[
    {
        "type": "OTPSMS",
        "value": "8988",
        "id": 2379470,
        "credentialType": 2
    },
    {
        "type": "OTPEMAIL",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 3
    },
    {
        "type": "BIOMETRIC",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 4
    },
    {
        "type": "OUTOFBAND",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 5
    },
    {
        "type": "ALL",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 6
    },
    {
        "type": "KBA",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 7
    },
    {
        "type": "BEHAVIOURALBIOMETRIC",
        "value": "Not Enrolled",
        "id": 0,
        "credentialType": 8
    }
]
```

## New validation on Load or Unload Card Endpoint

The following changes have been made to the validation behaviour on the Load or Unload Card endpoint

* An error is returned if a transaction is less than the minimum transaction
* An error is returned if a transaction exceeds the daily limit for the card