# Create Card with Thredd Generated Card Number

You have the option to use Thredd-generated card numbers on the same account range if required. You can use the same Create Customised Card endpoint for this. Make sure that you are not specifying the customised card number (`customPan`) and its reference number (`referenceNumber`) in the request.\
See the following Create Customised Card request example, where no customised card number is included in the `customPan `field and no reference number in the `referenceNumber `field:

```json Example Create Card with Thredd Generated Card Number
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
        "LastName": "Armstrong",
        "Dob": "2002-09-26",
        "Gender": "F",
        "Mobile": "(246) 779-6344 x88395",
        "Telephone": "714.342.9465 x799",
        "Email": "Dolores_Simonis@gmail.com",
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
    "customPan": "",
    "referenceNumber": null,
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

```json Example Custom PAN response
{
    "customPan": "008185",
    "isCustomPanValid": true,
    "referenceNumber": 2053406,
    "panOptions": []
}
```