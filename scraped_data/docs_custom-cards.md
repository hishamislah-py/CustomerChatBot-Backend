# Customisable Card Number

> 🚧 Important
>
> To use the Custom PAN endpoints, unique Client Secret and Client IDs need to be used when authenticating your token. Contact Thredd Application Support for more information.

The Customised Card APIs provide a personalised user experience for cardholders, allowing digital banks and fintech companies to offer their users the ability to choose the last six digits of their card number.

The Customised Card functionality is supported by the following endpoints:

* The Validate Customised Card Number endpoint, which lets you validate the custom card number
* The Create Card with Customised Card Number endpoint, which allows you to  create a card using the validated card number

> 📘 Note
>
> You can also create a customised card with a Thredd-Generated Card Number. See  [Create Card with Thredd-Generated Card Number](https://cardsapidocs.thredd.com/docs/create-card-with-thredd-generated-card-number).

## Validate Customised Card Number

The Validate Customised Card Number endpoint enables you to confirm whether the customised card number you want to use for a card is valid. As part of the request, you need to send additional custom PAN option in the `panOptions` object in the case that the first customised card number is invalid.

You can validate the customised card number option by making a POST request to the endpoint. For example:

```json Example Validate Custom PAN endpoint
https://thredd-cg-custompan-uat.thredd.net/api/v1/card/custom-pan
```

See the following example Validate Custom PAN request.

```json Example Validate Custom PAN request
{
  "productId": 443,
  "customPan": "008185",
  "panOptions": [
    {
      "id": 1,
      "pan": "78965"
    },
    {
      "id": 2,
      "pan": "78765"
    }
  ]
}

```

If successful, a 200 response is returned with confirmation on whether the customised card number is valid. If it is valid, the `isCustomPanValid` field returns true and that customised card number can be used when creating a card. See the below example of a successful response.

```json Example Validate Custom PAN response
{
    "customPan": "008185",
    "isCustomPanValid": true,
    "referenceNumber": 2053406,
    "panOptions": []
}

```

<br />

> 📘 Information
>
> * For information on the fields in the request and response for this endpoint, see [Validate Custom PAN - Field Descriptions](https://cardsapidocs.thredd.com/docs/validate-custom-pan-field-descriptions).
> * To see this endpoint in the API Explorer, see [Validate Custom PAN](https://cardsapidocs.thredd.com/reference/post_api-v1-card-custom-pan).

## Create Card with Customisable Card Number

When you have validated the customised card number, you can create a card with that card number using the Create Card with the Customised Card Number endpoint.

You can create a card with a customised card number by making a POST request to the endpoint. For example:

```json Create Card with Custom PAN endpoint
https://thredd-cg-custompan-uat.thredd.net/api/v1/card/create
```

See the following example Create Card with customised card number request, where the validated customised card number is included in the `customPan` field:

> 📘 Note
>
> If the customised card number and reference number are not present in the request, a random card number will be generated and assigned to the customer. See [Create Card with Thredd Generated Card Number](https://cardsapidocs.thredd.com/docs/create-card-with-thredd-generated-card-number) for more information.

```json Example Create Card with Customised Card Number
{
    "productReference": "",
    "customerAccount": "",
    "expiryDate": "",
    "accessCode": "",
    "coBrand": "",
    "fulfil1": "",
    "fulfil2": "",
    "cardName": "",
    "singleUse": false,
    "nonReloadable": false,
    "CardHolder": {
        "Title": "Mrs.",
        "FirstName": "Francis",
        "LastName": "Bloggs",
        "Dob": "2002-09-26",
        "Gender": "F",
        "Mobile": "07912123456",
        "Telephone": "",
        "Email": "fbloggs@gmail.com",
        "Address": {
            "AddressLine1": "21156",
            "AddressLine2": "Northwest",
            "AddressLine3": "6469 Ullrich Street",
            "City": "North Erichhaven",
            "PostCode": "74494-8786",
            "Country": "826"
        },
        "DeliveryAddress": {
            "AddressLine1": "21156",
            "AddressLine2": "Northwest",
            "AddressLine3": "6469 Ullrich Street",
            "City": "North Erichhaven",
            "County": "Cambridgeshire",
            "PostCode": "74494-8786",
            "Country": "826"
        }
    },
    "Groups": {
        "Limit": "",
        "Mcc": "",
        "Usage": "",
        "AuthorisationFee": "",
        "ScheduledFee": "",
        "WebserviceFee": "",
        "LimitedNetwork": "",
        "CardLinkage": "",
        "AuthorisationCalendar": "",
        "ForeignExchange": "",
        "Whitelist": "",
        "Blacklist": ""
    },
    "customPan": "008185",
    "referenceNumber": 2053406,
    "productId": 443,
    "ManufacturerDetails": {
        "DeliveryMethod": "",
        "DeliveryCode": "suywmq",
        "LanguageCode": "EN",
        "CarrierType": "suywmq",
        "VanityName": "suywmq",
        "Url": "https://natalia.net",
        "CardPhysicalLayout": {
            "ImageId": "suywmq",
            "EmbossLine4": "suywmq",
            "ThermalLine1": "suywmq",
            "ThermalLine2": "suywmq",
            "LogoFrontId": "suywmq",
            "LogoBackId": "suywmq"
        }
    }
}
```

If successful, a 200 response is returned.

```json Example Create Card with Customisable Card Number  response
{
    "messageId": "c012a5c5-7665-41f5-b317-6a59dadabba7"
}
```

The response includes the *messageId*, which is used to link to the Event Delivery Service (EDS) that communicates the public token and masked PAN to the customer. You should store the *messageId* on the customer's app. For more information on the EDS, see [Introduction to Webhooks](https://cardsapidocs.thredd.com/docs/introduction-to-webhooks) and [Webhook Event Codes](https://cardsapidocs.thredd.com/docs/webhook-event-codes).

> 📘 Information
>
> * For information on the fields in the request and response for this endpoint, see [Create Card with Customisable Card Number - Field Descriptions](https://cardsapidocs.thredd.com/docs/create-card-with-custom-pan-field-descriptions).
> * To see this endpoint in the API Explorer, see [Create Custom PAN](https://cardsapidocs.thredd.com/reference/create-custom-pan-1).

<br />