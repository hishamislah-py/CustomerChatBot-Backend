# Release Notes for the 27th February

The following changes have been made to Cards API:

* [NetworkSharingOptOut added to Retrieve and Update Card endpoints](#new-field-added-to-create-retrieve-and-update-card-endpoints)
* [New Field added to Update 3DS Credentials endpoint](#new-field-added-to-update-3ds-credentials-endpoint)
* [New Validation added to Load Unload Card for Issuer endpoint](#new-validation-added-to-load-unload-card-for-issuer-endpoint)

## NetworkSharingOptOut added to Retrieve and Update Card endpoints

The `NetworkSharingOptOut` enables you to specify whether the card should be opted out of the Visa Account Updater (VAU) or Mastercard's Automated Billing Updater (ABU), which provide merchants with account advice information. `NetworkSharingOptOut` is a Boolean field. If true, the card will be omitted from Visa Account Updater (VAU) or Automated Billing Updater (ABU). By default, when a card is created, the `NetworkSharingOptOut` is set to `false`.

The following example shows the NetworkSharingOptOut field in an Update Card request.

```json Example Update Card request
{
    "CustomerReference": "CustNo12345A",
    "NetworkSharingOptOut": false,
    "CardHolder": {
        "Title": "Mr.",
        "FirstName": "David",
        "LastName": "Smith",
        "DateOfBirth": "1982-02-25",
        "Mobile": "07645123456",
        "Email": "dsmith@email.com"
    },
    "Address": {
        "AddressLine1": "1008",
        "AddressLine2": "Royal Way",
        "AddressLine3": null,
        "City": "London",
        "County": "Essex",
        "PostCode": "RM7 2LD",
        "Country": "GBR"
    }
}
```

The following example shows the NetworkSharingOptOut field in the response of the Retrieve Card endpoint.

```json Example Retrieve Card response
{
    "cardType": "Physical",
    "publicToken": "118834053",
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
        "fullNameOnCard": "Mr Johnny Bruce",
        "maskedPan": "999999******1350",
        "startDate": "2025-02-17",
        "expiryDate": "2035-01-31",
        "clearPan": null,
        "cvv": null,
        "activationDate": "2025-02-17 08:29:30Z",
        "gpsExpiryDate": "2028-02-17"
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "John",
        "middleName": "Bruce",
        "lastName": "Bloggs",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "jbloggs@email.com"
    },
    "cardProduct": {
        "scheme": "GPS SCHEME TEST",
        "product": 10023,
        "productShortName": "GPSDUMMY",
        "productName": "GPS Test REST API",
        "ehiMode": 3,
        "networkId": 0
    },
    "controlGroups": {
        "limitsGroup": 1051,
        "usageGroup": 374,
        "recurringFeeGroup": null,
        "webServiceFeeGroup": null,
        "authFeeGroup": null,
        "mccGroup": null,
        "cardLinkageGroup": 53,
        "calendarGroup": null,
        "fxGroup": null,
        "paymentTokenUsageGroup": null,
        "cardAcceptorAllowList": null,
        "cardAcceptorDisallowList": null,
        "limitedNetworkGroup": null
    },
    "3DS": [],
    "designId": "PMTREST",
    "childCards": [],
    "siblingCards": [],
    "address": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "SW11 2LD",
        "country": "826"
    },
    "fulfilment": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "Mountain Drive",
        "addressLine3": "",
        "city": "London",
        "state": "",
        "county": "",
        "postCode": "SW11 2LD",
        "country": "826"
    },
    "freetext1": "Comments for the card manufacturer here",
    "freetext2": "And in this field too.",
    "isSingleUse": false,
    "isNonReloadable": false,
    "networkSharingOptOut": false,
    "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    },
    "language3ds": "en-GB",
    "programManagerID": 78,
    "programManagerCode": "PMT",
    "oobAppUrl": null,
    "isMultiFx": false,
    "isMfxPrimary": false
}
```

> 📘 More Information
>
> For more information on these endpoints, see:
>
> * [Retrieve a Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card)
> * [Updating a card](https://cardsapidocs.thredd.com/docs/updating-a-card)

## New Field added to Update 3DS Credentials endpoint

A new field, UpdatedBy, has been added to the Update 3DS Credentials endpoint in this release. This enables users to specify who has updated the 3DS credentials for a card.

The following example shows the UpdatedBy field in an Update 3DS Credentials request.

```json Example Update 3DS Credentials request
{
    "type": "EmailOTP",
    "value": "286999",
    "updatedBy": "John Bloggs"

}
```

> 📘 More Information
>
> For more information on the Update 3DS Credentials endpoint, see [Managing 3D Secure Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials).

## New Validation added to Load Unload Card for Issuer endpoint

We have included additional validation to the Load/Unload Card for Issuer endpoint in this release. This validation will prevent users from loading or unloading funds onto a child card. If you attempt to loads funds onto a child card, Thredd returns a 422 response stating that the endpoint does not support creating child card transactions