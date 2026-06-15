# Release Notes for 30 September 2022

New changes to the GPS Cards API for the week ending 30th September 2022.

* [Master Virtual Card option added to Create Card endpoint](#master-virtual-card-option-added-to-create-card-endpoint)
* [Renewal support for Master Virtual Cards](#renewal-support-for-master-virtual-cards)
* [Masked PAN field added to Retrieve Card response](#masked-pan-field-added-to-retrieve-card-response)

## Master Virtual Card option added to Create Card endpoint

A Master Virtual Card option has been added to the cardType field in the Create Card endpoint. A Master Virtual Card acts as a parent card to multiple child cards and is never issued and cannot be transacted against. A Master Virtual Card Type shares the same mandatory fields as a Virtual Card when creating a card.

The below is an example body for a Create Card transaction where the Master Virtual Card type has been selected.

```json Example body for MasterVirtual Cardtype
{
     "cardHolder": {
          "title": "Mr",
          "firstName": "Jon",
          "lastName": "Smith",
          "dateOfBirth": "1963-11-22"
     },
     "address": {
          "addressLine1": "32 Eastern Lane",
          "postCode": "S11 7AA",
          "country": "GBR"
     },
     "fulfilment": {
          "addressLine1": "32 Eastern Lane",
          "postCode": "S11 7AA",
          "country": "GBR"
     },
     "virtualCardImageDetails": {
          "virtualCardImageId": "134341",
          "imageSize": 1
     },
     "cardType": "MasterVirtual",
     "cardProduct": 1234
}
'
```

A 200 response is returned with details on the MasterVirtual card created.

```json
{
    "publicToken": "103166228",
    "embossName": "Mr Jon Smith",
    "maskedPan": "999999******3433",
    "startDate": "2022-09-26",
    "expiryDate": "2023-09-30"
}
```

## Renewal support for Master Virtual Cards

The Renew Card endpoint has been updated for this release to support the renewal of master virtual cards. The renewal of a master virtual card follows the same process as when renewing a virtual card where RenewStep must be empty or not provided at all.

## Masked PAN field added to Retrieve Card response

The response to a successful Retrieve Card request has been updated in this release to include the Masked PAN field for the card.