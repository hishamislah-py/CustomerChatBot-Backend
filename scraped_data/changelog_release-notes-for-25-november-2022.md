# Release Notes for 25 November 2022

New changes to the GPS Cards API for the week ending 25 November 2022.

* [New SendSMS endpoint added](#new-sendsms-endpoint-added)
* [Freetext fields added to Retrieve Card endpoint](#freetext-fields-added-to-retrieve-card-endpoint-response)
* [Freetext fields added to Update Card and Renew Card endpoints](#freetext-fields-added-to-update-card-and-renew-card-endpoints)
* [Field changes in Create Card endpoint](#field-changes-in-create-card-endpoint)

## New SendSMS endpoint added

*Endpoint: cards/\{publicToken}/sendSMS*\
A new endpoint has been added that enables customers to send custom SMS to their clients. This is done by entering the message into the field and then using EventIDs to populate client data.

You can send an SMS to a client by making a POST request to the endpoint. For example:

```json SendSMS Example Endpoint
{{base-url}}/cards/{{publicToken}}/send-sms
```

The body can include up to three optional fields:

* **phoneNumber** enables you to select a number to send the message to if there is no phone number associated with the publicToken specified in the endpoint
* **smsText** enables you enter a message to be sent to the client, including Event IDs
* **amount** enables you to enter an amount value if the amount event ID is used in the smsText field

```json Example SendSMS Request Body
{
"phoneNumber":"07xxxxxxxxx", 
"smsText": "CVV for your card ending with %cardLast4% is %CVV%"
}
```

You will receive a 200 response if the request is successful, confirming the message has been sent to the phone number specified in either the endpoint or the body.

> 📘 Documentation
>
> For more information on the SendSMS endpoint, see [Sending SMS](https://cardsapidocs.thredd.com/docs/sending-sms).

## Freetext fields added to Retrieve Card endpoint response

The free text fields (freetext1 and freetext2) have now been added to the response when using the Retrieve Card endpoint.

```json Example Retrieve Card response 
{
    "cardType": "Virtual",
    "publicToken": "103169900",
    "status": "Inactive",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "my ref 12345",
        "fullNameOnCard": "Mr Jon Smith",
        "maskedPan": "999999******4282",
        "startDate": "2022-11-22",
        "expiryDate": "2023-11-30"
    },
    "cardHolder": {
        "title": "Mr",
        "firstName": "Jon",
        "middleName": "",
        "lastName": "Smith",
        "dateOfBirth": "1982-11-03",
        "mobile": "",
        "email": ""
    },
    "cardProduct": {
        "scheme": "GPS VIRTUAL SCHEME TEST",
        "product": 10005
    },
    "controlGroups": {
        "limitsGroup": 1201,
        "usageGroup": 0,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": 0,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 20
    },
    "3DS": [],
    "designId": "New Card Brand",
    "childCards": [],
    "address": {
        "addressLine1": "32 Western Drive",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": "",
        "county": "",
        "postCode": "S25 2BZ",
        "country": "826"
    },
    "fulfilment": {
        "addressLine1": "e43",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": "",
        "county": "",
        "postCode": "34",
        "country": "826"
    },
    "freetext1": "Text for the card manufacturer",
    "freetext2": "more text for the card manufacturer"
```

## Freetext fields added to Update Card and Renew Card endpoints

The free text fields (freetext1 and freetext2) have been added to the Update Card and Renew Card endpoints for this release, enabling customers to update the free text fields as required.

```json Example Update Card Request Body
{
    "CustomerReference": "CustNo12345A",
    "Freetext1": "Comments for the card manufacturer here",
    "Freetext2": "And in this field too.", 
    "CardHolder": {
        "Title": "Mr.",
        "FirstName": "David",
        "LastName": "Smith",
        "DateOfBirth": "1982-02-25",
        "Mobile": "07645123456",
        "Email": "Darcy@iambatman.com"
    },
    "Address": {
        "AddressLine1": "1008",
        "AddressLine2": "Royal Way",
        "AddressLine3": null,
        "City": "London",
        "County": "Essex",
        "PostCode": "RM7 2LD",
        "Country": "GBR"
    },
    "Fulfillment": {
        "AddressLine1": "1009",
        "AddressLine2": "Behind Waterfall",
        "AddressLine3": null,
        "City": "Gotham",
        "County": "New_York",
        "PostCode": "GT019TT",
        "Country": "USA"
    },
    "NameOnCard": {
        "Title": "Mr",
        "FirstName": "Dave",
        "LastName": "Smith"
    }
}
```

## Field changes in Create Card endpoint

The following fields have been changed in the Create Card endpoint so that they are no longer mandatory:

* title
* VirtualCardImageId (in the VirtualCardImageDetails nest)
* ImageSize (in the VirtualCardImageDetails nest)