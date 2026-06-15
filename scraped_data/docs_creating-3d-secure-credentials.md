# Managing 3D Secure Credentials

This section provides details of how to:

* [Create a 3D Secure Credential for a card](#creating-a-3d-secure-credential)
* [Update the Credentials linked to a card](#update-a-credential)
* [List 3DS Credentials](#list-3ds-credentials)
* [Delete a 3DS Credential](#delete-a-credential)
* [Get 3DS Configuration](#get-3ds-configuration)

## Creating a 3D Secure Credential

This API can be used to create a 3D Secure Authentication credential for a card.

### Step 1: Retrieve card details

Before creating the credential for a card, identify the corresponding <Glossary>Public Token</Glossary> for the card to be used.\
A card's public token is returned in the response to creating a card within the `publicToken` object.

### Step 2: Create a 3D Secure credential

After identifying the public token for the card, you can create a 3D Secure credential for the card by executing a POST request to the *Create 3DS Credential* endpoint with the corresponding credential `Type`.

```json Example Create 3DS Credentials endpoint
{{base-url}}/cards/{{publicToken}}/3ds-credentials
```

## Credential Types

You can add multiple credentials to each card that you enrol in the 3D Secure service.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Credential Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        OTPSMS
      </td>

      <td>
        During a 3D Secure session, the Access Control Server (ACS) generates a single-use One-Time Password (OTP). Thredd sends the OTP in an SMS text message to the cardholder’s mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction.
      </td>
    </tr>

    <tr>
      <td>
        OTPEMAIL
      </td>

      <td>
        During a 3D Secure session, the ACS generates a single-use One-Time Password (OTP). Thredd sends the OTP in an email message to the cardholder’s email address and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction.

        * *Note:* OTPEMAIL is currently available on Apata and is not supported on Cardinal.
      </td>
    </tr>

    <tr>
      <td>
        BIOMETRIC
      </td>

      <td>
        During a 3D Secure session, the ACS sends a biometric authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer smart phone application, via biometric data, such as a fingerprint scan or face recognition, obtained from the cardholder’s mobile device. Your customer application manages the biometric verification and returns a response to Thredd.
      </td>
    </tr>

    <tr>
      <td>
        OUTOFBAND
      </td>

      <td>
        During a 3D Secure session, the ACS sends an authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer In-App smart phone application; for example, by asking them to enter a username. Your customer application manages the verification and returns a response to Thredd.
      </td>
    </tr>

    <tr>
      <td>
        KBA
      </td>

      <td>
        You enrol the card in KBA using the 3D Secure service and provide the security question ID and answer pair. Thredd provides Cardinal or Apata with the security question to use for KBA. During the e-commerce authentication session Cardinal/Apata asks the cardholder to answer the security question and then sends a KBA authentication request to Thredd together with the cardholder’s answer. Thredd compares the answer returned by Cardinal/Apata to the answer stored in the Thredd database and then returns a response to Cardinal/Apata. KBA is typically combined with OTP SMS: the cardholder is first asked to authenticate using OTP and then via KBA.

        * *Note:* If KBA is selected as the credential type then the body must include a value in the *cardholderAnswer* field. For example,

        \{\
        "type": "KBA",\
        "value": "6",\
        "cardholderAnswer": "Ford Focus"\
        }
      </td>
    </tr>

    <tr>
      <td>
        ALL
      </td>

      <td>
        The ALL credential type is currently not available.
      </td>
    </tr>
  </tbody>
</Table>

You can find an example of Create 3DS credentials request body using the OTPSMS credential type below.

```json Example Create 3DS Credentials body
{
"type":"OTPSMS",
"value": "8988"
}
```

If successful, a 201 response will be returned with the 3DS identifier.

```json Example Create 3DS Credentials response
{
    "identifier": 2008233
}
```

### Creating a KBA 3DS Credential Type

When using the KBA credential type to create a 3DS credential for your card, the request body must include the `value `and `cardholderAnswer ` fields. The value field contains the unique identifier of the KBA question you want to use. A default set of KBA questions are set up in Smart Client. These can be modified if required. You can view the default KBA questions in the [3D Secure Guide](https://docs.thredd.com/3dsecure/Content/Reference/KBA_Questions.htm).

For example, in Smart Client the KBA ID *4*  is set to *What was the make of your first car?* by default. In the below example, the `value `field is *4* (for KBA ID 4), and the `cardholderAnswer` is *Vauxhall Corsa.*

```json Example KBA Type Create 3DS Credential body
{
  "type": "KBA",
  "value": "4",
  "cardholderAnswer": "Vauxhall Corsa"
}
```

> 👍 API Explorer
>
> See the [Create 3DS Credentials](https://cardsapidocs.thredd.com/reference/create-3ds-credentials) endpoint.

## Update a Credential

This API can be used to update a 3DS Authentication credential for a card.

### Step 1: Retrieve card details

Before updating the credential for a card, identify the corresponding Public Token for the card to be used.\
A card's public token is returned in the response to creating a card within the `publicToken` object.

### Step 2: Update a 3D Secure credential

After identifying the public token for the card, you can update or delete the 3D Secure credential for the card by executing a PUT request to the *Update 3DS Credential* endpoint with the corresponding credential `Type`.

```json Example Update 3DS Credentials endpoint
{{base-url}}/cards/{{publicToken}}/3dscredentials/{{3DSIdentifier}}
```

The body should include the new value of the 3DS credential. The below is an example of what the body should look like.

```json Example Update 3DS Credentials body
{
    "type": "EmailOTP",
    "value": "286999",
    "updatedBy": "John Bloggs"

}
```

If successful, a 204 response will be returned. You can use the List 3DS Credentials endpoint to confirm the update has been successful.

> 👍 API Explorer
>
> See the [Update 3DS Credentials](https://cardsapidocs.thredd.com/reference/update-3ds-credential) endpoint.

## List 3DS Credentials

The List 3DS Credentials endpoint allows you to retrieve the 3DS credentials associated with a card. You can retrieve the 3DS credentials by making a GET request to the endpoint. For example:

```json Example List 3DS Credentials endpoint
{{base-url}}/cards/{{publicToken}}/3dscredentials
```

A successful response will return a HTTP 200 response code and a payload that will return the details for the 3DS credentials for the card. For example:

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

A blank HTTP 200 response will be returned if there are no 3DS credentials associated with the card.

> 👍 API Explorer
>
> See the [List 3DS Credentials](https://cardsapidocs.thredd.com/reference/list-3ds-credentials) endpoint.

## Delete a Credential

The Delete 3DS Credentials endpoint allows you to remove 3DS credentials associated with a card. You can delete the credentials by making a DELETE request, with the 3DS credential id being set in the endpoint. For example:

```Text Example Delete 3DS Credential endpoint
{{base-url}}/cards/{{publicToken}}/3ds-credentials/{{3DSCredential}}
```

> 👍 API Explorer
>
> See the [Delete 3DS Credentials](https://cardsapidocs.thredd.com/reference/delete-3ds-credential) endpoint.

## Get 3DS Configuration

The Get 3DS Configuration endpoint enables customers to view a card's 3DS enrolment data from the database. This is to support customers using Apata for their 3DS provider. You can retrieve a card's 3DS configuration by making a GET request to the Get 3DS Configuration endpoint. For example:

```json Example Get 3DS Configuration endpoint
{{base-url}}/cards/{{publicToken}}/3ds-configuration
```

If successful, a HTTP 200 response will be returned. For example:

```json Example Get 3DS Configuration response
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

> 👍 API Explorer
>
> See the [Get 3DS Configuration](https://cardsapidocs.thredd.com/reference/list-card-enrollment-details) endpoint.