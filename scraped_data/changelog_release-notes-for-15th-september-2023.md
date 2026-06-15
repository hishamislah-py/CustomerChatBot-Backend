# Release Notes for 15 September 2023

New changes to the Thredd Cards API for the week ending 12th September 2023.

## Virtual card can no longer be created with fulfilment object included in the request body

A 422 error will now be returned if the fulfilment object is included in the request body when creating a virtual card for the Create Card endpoint. Previously a virtual card could be created with fulfilment details associated with it, which is not required for virtual cards.

## manufacturingDetails object now optional in Create Card endpoint

The manufacturingDetails object in the Create Card endpoint is now optional. This is done by setting the object to `null `in the request body. See the below example:

```json Example Create Card request body with null manufacturingDetails
{
    "CardType":"Physical",
    "CardProduct": 10023,
    "CustomerReference": "CustNo12345A",
    "ActivateNow": true,
    "Freetext1": "Comments for the card manufacturer here",
    "Freetext2": "And in this field too.", 
    "CardHolder": {
        "Title": "Mr.",
        "FirstName": "John",
        "MiddleName": "Bruce",
        "LastName": "Bloggs",
        "DateOfBirth": "1982-02-19",
        "Mobile": "07755123456",
        "Email": "jbloggs@email.com"
    },
    "nameOnCard": {
        "title": "Mr",
        "firstName": "Johnny",
        "lastName": "Bloggs"
     },
    "Address": {
        "AddressLine1": "32 Metropolis Ave",
        "AddressLine2": "Mountain Drive",
        "City": "London",
        "PostCode": "SW11 2LD",
        "Country": "GBR"
    },
    "fulfilment": {
          "AddressLine1": "32 Metropolis Ave",
          "AddressLine2": "Mountain Drive",
          "City": "London",
          "PostCode": "SW11 2LD",
          "Country": "GBR"
     },
     "ManufacturingDetails": Null,
     

}
```

> 🚧 Note
>
> If the manufacturingDetails object is not set to null, then the cardManufacturer, deliveryMethod and carrierType fields will be mandatory for creating a physical card.

## Apostrophe now allowed in name fields

The following fields can now include an apostrophe:

* `firstName`, `middleName `and `lastName `in the cardHolder object in the Create Card endpoint
* `firstName `and `lastName `in the nameOnCard object in the Create Card endpoint
* `firstName`, `middleName `and `lastName `in the Cardholder object in the Update Card endpoint
* `firstName `and `lastName `in the nameOnCard object in the Update Card endpoint

## middleName now optional in Update Card endpoint

The Update Card endpoint has been updated so that the middleName field is now optional.