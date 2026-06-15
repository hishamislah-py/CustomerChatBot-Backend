# Release Notes for 24th September 2024

New changes to the Thredd Cards API coming on the 24th September. These include:

* [New Fields Added to Create Bulk Cards endpoint](#new-fields-added-to-create-bulk-cards-endpoint)
* [New Fields Added to Update Card endpoint](#new-fields-added-to-update-card-endpoint)
* [New Fields Added to the Get 3DS Configuration endpoint](#new-fields-added-to-the-get-3ds-configuration-endpoint)
* [activationCode Field Added to Get Card Payment Tokens endpoint](#activationcode-field-added-to-get-card-payment-tokens-endpoint)
* [Fault Tolerance Improved for the Update Card Status endpoint](#fault-tolerance-improved-for-the-update-card-status-endpoint)
* [Updated Retrieve Card endpoint to include Apata 3DS Credentials](#updated-retrieve-card-endpoint-to-include-apata-3ds-credentials)
* [Removed the isConfiguredGroup Field from the Get Card Acceptor endpoint](#removed-the-isconfiguredgroup-field-from-the-get-card-acceptor-endpoint)
* [Bug Fixes](#bug-fixes)

## New Fields Added to Create Bulk Cards endpoint

New fields have been added to Create Bulk Cards endpoint in this release. These have been added to support non-personalised physical cards. The new fields are described in the following table.

| Name                  | Description                                                                                                      | Mandatory |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------- |
| nameOnCard            | The name embossed on card. This name will be applied to every card created.                                      | No        |
| imageId               | The image ID used for every card created.                                                                        | No        |
| deliveryMethod        | The delivery method for every card created.                                                                      | No        |
| **fulfilmentAddress** | Object that contains the fulfilment address details.                                                             | Yes       |
| addressLine1          | First line of the address.                                                                                       | Yes       |
| addressLine2          | Second line of the address.                                                                                      | No        |
| addressLine3          | Third line of the address.                                                                                       | No        |
| city                  | The city name.                                                                                                   | No        |
| state                 | The state name.                                                                                                  | No        |
| county                | The county name.                                                                                                 | No        |
| postCode              | Postcode / Zip code of the address.                                                                              | Yes       |
| country               | Country of residence. This is represented as a 3-letter alphanumeric ISO country code (For example, GBR for UK). | No        |

See the below for an example Get Bulk Cards request with the new fields included.

```json Example Create Bulk Cards request
{
  "cardProduct": 123456,
  "quantity": 50,
  "nameOnCard": "Thredd",
  "imageId": "101",
  "deliveryMethod": "StandardDelivery",
  "fulfilmentAddress": {
    "addressLine1": "32 Eastern Road",
    "city": "Sheffield",
    "county": "South Yorkshire",
    "postCode": "S11 8AA",
    "country": "GBR"
  },
}
```

If successful, a 202 response is returned with a unique bulk card generation id. This should be included in the Get Bulk Cards endpoint.

> 📘 Information
>
> * To view the endpoint in the API Explorer, see [Create Bulk Cards](https://cardsapidocs.thredd.com/reference/create-bulk-cards).
> * To view documentation on the endpoint, see [Bulk Create Physical Cards.](https://cardsapidocs.thredd.com/docs/bulk-create-cards)

## New Fields Added to Update Card endpoint

New fields are available in the request of the Update Card endpoint. The new fields are part of the `Apata` object within the `Config3DSecure` object. The changes enables you to update the details for the Apata configuration for the card.

* ChallengeProfileId
* language3ds (Note: This has moved into the `Config3DSecure` for this release.)
* CardProgramId
* KbaNumberOfQuestionsToAnswer
* KbaNumberOfIncorrectPermissible

See the below example of the fields being included in the request:

```json Example Update Card request
{
  "customerReference": "string",
  "cardHolder": {
    "title": "string",
    "firstName": "string",
    "middleName": "string",
    "lastName": "string",
    "dateOfBirth": "string",
    "mobile": "string",
    "email": "string"
  },
  "address": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "county": "string",
    "state": "string",
    "postCode": "string",
    "country": "str"
  },
  "fulfilment": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "county": "string",
    "state": "string",
    "postCode": "string",
    "country": "str"
  },
  "designId": "MsjVO02TWhbiDt1QQWRT8_CSMARE2FxV64pMRKNQdxZaZ",
  "parentCard": "9130984553",
  "nameOnCard": "string",
  "freetext1": "string",
  "freetext2": "string",
  "language3ds": "string", 
  "Config3DSecure": {
    "language3ds" : "",
    "Apata": {      
      "cardProgramId":"wrew3245234fg3r5fsdf",
      "challengeProfileId":"wrew3245234fg3r5fsdf",
      "kbaNumberOfQuestionsToAnswer": 1,
      "kbaNumberOfIncorrectPermissible": 3
      }
    } 
}
```

<br />

## New Fields Added to the Get 3DS Configuration endpoint

New fields have been added to the Get 3DS Configuration endpoint so users can retrieve details related to Apata card level settings. The following fields have been added:

* challengeProfileId
* language
* cardProgramId
* numberOfQuestionsToAnswer
* numberOfIncorrectPermissible

The new fields are in the `apataConfig` array of the response. See the below example of the new fields included in the Get 3DS Configuration endpoint response.

```json Example Get 3DS Configuration response
{
  "provider": 0,
  "programManager": {
    "programManagerCode": "string",
    "shortName": "string"
  },
  "mobile": "string",
  "email": "string",
  "isActive": true,
  "status": "string",
  "has3dSecureCredentialEntry": true,
  "apataConfig": {
    "cardProgramId": "string",
    "challengeProfileId": "string",
    "financialInstitutionId": "string",
    "numberOfQuestionsToAnswer": 0,
    "numberIncorrectPermissible": 0,
    "language": "string"
  },
  "kba": [
    {
      "question": "string",
      "answer": "string"
    }
  ],
  "otpSms": {
    "otpSmsTemplateFullFormat": "string",
    "otpSmsTemplateDefaultFormat": "string"
  },
  "biometric": {
    "autoEnrol3DSBiometrics": 0,
    "autoEnrol3DSOOB": 0,
    "biometricUrl": "string",
    "hasBiometricCredentials": true,
    "hasOOBCredentials": true
  }
}
```

<br />

## activationCode Field Added to Get Card Payment Tokens endpoint

A new field, `activationCode`, has been added to the Get Card Payment Tokens endpoint response. The field returns the code to be sent directly to the cardholder to activate this payment token.

See the below example response with the `activationCode` included.

```json Example Get Card Payment Tokens response
[
  {
    "id": 0,
    "walletId": "string",
    "walletProvider": "string",
    "tokenPAN": "string",
    "statuses": {
      "tokenisedStatus": {
        "code": "string",
        "description": "string"
      },
      "authorisationStatus": {
        "code": "string",
        "description": "string"
      },
      "authorisationDecision": {
        "code": "string",
        "description": "string"
      },
      "transactionStatus": {
        "code": "string",
        "description": "string"
      },
      "gpsStatusInfo": {
        "code": "string",
        "description": "string"
      }
    },
    "tokenisedDate": "2024-01-01 00:00:01Z",
    "expiryDate": "2026-01-01",
    "tokenType": "Secure Element PAN",
    "deviceType": "Mobile phone (no further detail)",
    "deviceName": "iPhone",
    "merchantName": "TESCO Richmond",
    "activationCode": "297147"
  }
]
```

<br />

## Fault Tolerance Improved for the Update Card Status endpoint

Improvements to the fault tolerance of the Update Card Status have been made for this release. This includes the behaviour of the endpoint when cardStatusCode is set to 0, where an error message is now returned.

## Updated Retrieve Card endpoint to include Apata 3DS Credentials

The Retrieve Card endpoint has been updated in this release so that card's with 3DS credentials are returned in the response. See the below example.

```json Example Retrieve Card response
{
  "customerReference": "string",
  "cardHolder": {
    "title": "string",
    "firstName": "string",
    "middleName": "string",
    "lastName": "string",
    "dateOfBirth": "string",
    "mobile": "string",
    "email": "string"
  },
  "address": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "county": "string",
    "state": "string",
    "postCode": "string",
    "country": "str"
  },
  "fulfilment": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "county": "string",
    "state": "string",
    "postCode": "string",
    "country": "str"
  },
  "designId": "MsjVO02TWhbiDt1QQWRT8_CSMARE2FxV64pMRKNQdxZaZ",
  "parentCard": "9130984553",
  "nameOnCard": "string",
  "freetext1": "string",
  "freetext2": "string",
  "language3ds": "string", 
  "Config3DSecure": {
    "language3ds" : "string",
    "Apata": {      
      "cardProgramId":"wrew3245234fg3r5fsdf",
      "challengeProfileId":"wrew3245234fg3r5fsdf",
      "kbaNumberOfQuestionsToAnswer": 1,
      "kbaNumberOfIncorrectPermissible": 3
      }
    } 
}
```

<br />

## Removed the isConfiguredGroup Field from the Get Card Acceptor endpoint

From this release, the isConfiguredGroup field has been removed from the response of the Get Card Acceptor endpoint.

For more information, see [PRN-186](https://cardsapidocs.thredd.com/changelog/prn-186).

## Bug Fixes

The following fixes have been made in this release:

* Fixed an issue where, when replacing a converted card, the converted card was returning the wrong card type.
* Fixed an issue where Cards API was incorrectly using the last dpan\_over\_fpan value for a payment\_token\_usage\_id, rather than the correct value for the specific wallet\_id.