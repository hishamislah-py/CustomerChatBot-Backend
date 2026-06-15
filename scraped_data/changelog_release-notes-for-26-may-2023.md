# Release Notes for 26 May 2023

New changes to the Thredd Cards API for the week ending 26th May 2023.

* [ActivateNow field added to Create Card endpoint](#activatenow-field-added-to-create-card-endpoint)
* [Examples added to Postman Collection](#examples-added-to-postman-collection)
* [Update STIP Balance endpoint temporarily removed](#update-stip-balance-endpoint-temporarily-removed)

## ActivateNow field added to Create Card endpoint

The ActivateNow field has been added to the Create Card endpoint, enabling users to activate a card in the process of creating a card. This is an optional field and the default value, where the field is not included in the body, is **false**.

See below for an example Create Card body with the ActivateNow field included and set to **true**.

```json Example Create Card body with ActivateNow field
{
    "CardType":"Physical",
    "CardProduct": 10030,
    "CustomerReference": "CustNo12345A",
    "ActivateNow": true,
    "CardHolder": {
        "Title": "Mr.",
        "FirstName": "Bruce",
        "MiddleName": "Graham",
        "LastName": "Smith",
        "DateOfBirth": "1982-02-19",
        "Mobile": "07755123456",
        "Email": "BSmith@email.com"
    },
    "Address": {
        "AddressLine1": "1007",
        "AddressLine2": "Mountain Drive",
        "AddressLine3": "string",
        "City": "Derby",
        "County": "Derbyshire",
        "PostCode": "DE1 4PP",
        "Country": "GBR"
    },
    "fulfilment": {
          "addressLine1": "32 Metropolis Ave",
          "city": "Derby",
          "country": "GBR",
          "county": "Derbyshire",
          "PostCode": "DE1 4PP"
     },
     "ManufacturingDetails":
     {
       "CardManufacturer": "AB Note",
        "DeliveryMethod": 0,
        "CarrierType": "Type 1",
        "Quantity": 1,
        "Language": "HU",
        "ThermalLine1": "asdeoivh2neriuvnqkr",
        "ThermalLine2" : "asjkfnkerjnkwe",
        "EmbossLine4" : "jdwncwlkejr",
        "VanityName" : "Name Mane",
             "ImageDetails":
             {
                  "ImageId": "An image id",
                  "LogoFrontId" : "A logo ID",
                  "LogoBackId": "Another logo ID"
             },
    "nameOnCard": {
        "title": "Mr",
        "firstName": "Bruce",
        "lastName": "Smith"
     }
     
    
    }

}
```

> 👍 Documentation/API Explorer
>
> * For more information on the Create Card endpoint, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).
> * To try the Create Card endpoint, see [Create Card](https://cardsapidocs.thredd.com/reference/create-card) in API Explorer.
> * To view more details on the fields available for the Create Card endpoint, see [Create Card - Field Descriptions](https://cardsapidocs.thredd.com/docs/create-card-field-descriptions).

## Examples added to Postman Collection

Example bodies and responses have been added to the UAT Postman Collection.

<Image align="center" className="border" border={true} src="https://files.readme.io/ab99492-PostmanExample.png" />

> 👍 Postman Collection
>
> You can download the latest version of the Postman Collection from the [API Explorer](https://cardsapidocs.thredd.com/reference/introduction-1).

## Update STIP Balance endpoint temporarily removed

The Update STIP Balance endpoint has been temporarily removed from the Cards API.