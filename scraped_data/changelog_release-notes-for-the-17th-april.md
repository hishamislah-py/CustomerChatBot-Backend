# Release Notes for the 17th April

The following change has been made to Cards API:

* [Url Field added to Multiple Endpoints](#url-field-added-to-multiple-endpoints)
* [Unblock PIN and Unblock CVV Endpoints Updated to Work for all Card Statuses](#unblock-pin-and-unblock-cvv-endpoints-updated-to-work-for-all-card-statuses)
* [Added dynamicInterchange object in Create Card endpoint](#added-dynamicinterchange-object-in-create-card-endpoint)

## Url Field added to Multiple Endpoints

The Url field has been added to the following endpoints, enabling you to add a QR code to a card:

* Create Card
* Update Card
* Retrieve Card

See the following example of the field included in a Create Card request.

```json Example Create Card request
{
  "cardType": "Physical",
  "cardProduct": 578,
  "designId": "New Card Brand",
  "url": "Example QR Code UR",
  "customerReference": "my ref 12345",
  "activateNow": true,
  "cardHolder": {
    "title": "Mr",
    "firstName": "John",
    "lastName": "Smith",
    "dateOfBirth": "1963-11-22",
    "mobile": "07471234567",
    "email": "john.smith@example.com"
  },
  "address": {
    "addressLine1": "38 New Dover Road",
    "addressLine2": "Lordship Lane",
    "city": "Wallisdown",
    "postCode": "BH12 0AL",
    "country": "GBR"
  },
  "manufacturingDetails": {
    "deliveryMethod": "StandardDelivery",
    "carrierType": "CarrierType",
    "imageDetails": {
      "imageId": "12345"
    }
  }
}
```

This value is included in the Thredd Card Generation file, in the `<QRCode>` field. For example: [https://www.example.com/QRBalance/123456789](https://www.example.com/QRBalance/123456789). For details, see the [Card Generation Interface Specifications](https://docs.thredd.com/Card_Generation_Interface_Specification.htm).

> 📘 More Information
>
> For more information on these endpoints, see:
>
> * [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2)
> * [Retrieve a Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card)
> * [Updating a card](https://cardsapidocs.thredd.com/docs/updating-a-card)

## Unblock PIN and Unblock CVV Endpoints Updated to Work for all Card Statuses

A card's PIN and CVV can now be updated regardless of the card's status, aligning with the behaviour found in Smart Client. Previously only cards with an Active status could have their PIN or CVV unblocked.

> 📘 More Information
>
> For more information on these endpoints, see:
>
> * [PIN Management](https://cardsapidocs.thredd.com/docs/card-personal-identification-number-pin)
> * [Card Verification Value (CVV2)](https://cardsapidocs.thredd.com/docs/card-verification-value-cvv)

## Added dynamicInterchange object in Create Card endpoint

A new object, `dynamicInterchange`, has been added to the Create Card endpoint in this release. This relates to upcoming new functionality and can be ignored for now. Further information on this functionality will be available in due course.