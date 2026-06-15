# Release Notes for 13th December

The following changes have been made to Cards API:

* [New Create Custom PAN Endpoints](#new-create-custom-pan-endpoints)
* [oobAppUrl Field Added to Multiple Endpoints](#oobappurl-field-added-to-multiple-endpoints)
* [Updated Card Status Behaviour](#updated-card-status-behaviour)
* [Updated Behaviour When Renewing, Updating, or Replacing Cards](#updated-behaviour-when-renewing-updating-or-replacing-cards)
* [Updated Name of Card Status](#updated-name-of-card-status)
* [Bugfix in Payment Token Updates](#bugfix-in-payment-token-updates)

## New Create Custom PAN Endpoints

Two new endpoints have been made available in this release. The Customised Card APIs provide a personalised user experience for cardholders, allowing digital banks and fintech companies to offer their users the ability to choose the last six digits of their card number.

The Customised Card functionality is supported by the following endpoints:

* The Validate Customised Card Number endpoint, which lets you validate the custom card number
* The Create Card with Customised Card Number endpoint, which allows you to create a card using the validated card number

For more information on using each of these endpoints, see [Customisable Card Number](https://cardsapidocs.thredd.com/docs/custom-cards).

### oobAppUrl Field Added to Multiple Endpoints

A new field, oobAppUrl, has been added to the Core API for this release. The field enables you to set the URL for out-of-band (OOB) authentication processes for 3DS. This is available for both Apata and Cardinal customers.

The oobAppUrl field has been added to the following endpoints:

* Create Card
* Update Card
* Get Card

See the following examples of the field included in the request of the Create Card endpoint.

```json Example Create Card request
{
    "cardType":"Physical",
    "cardProduct": 10023,
    "customerReference": "CustNo12345A",
    "activateNow": true,
    "freetext1": "Comments for the card manufacturer here",
    "freetext2": "And in this field too.",
    "nameOnCard": "Mr Johnny Bloggs",
    "isSingleUse" : "true",
    "isNonReloadable" : "false",
    "oobAppUrl": "http://www.thredd.com",
    "language3ds": "GBR",
    "cardHolder": {
        "title": "Mr.",
        "firstName": "John",
        "middleName": "Bruce",
        "lastName": "Bloggs",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "jbloggs@email.com"
    },
    "address": {
        "addressLine1": "32 Metropolis Ave",
        "addressLine2": "Mountain Drive",
        "city": "London",
        "postCode": "SW11 2LD",
        "country": "GBR"
    },
    "fulfilment": {
          "addressLine1": "32 Metropolis Ave",
          "addressLine2": "Mountain Drive",
          "city": "London",
          "postCode": "SW11 2LD",
          "country": "GBR"
     },
     "manufacturingDetails":
     {
        "deliveryMethod": 0,
        "carrierType": "Type 1",
        "language": "HU",
        "thermalLine1": "asdeoivh2neriuvnqkr",
        "thermalLine2" : "asjkfnkerjnkwe",
        "embossLine4" : "jdwncwlkejr",
        "vanityName" : "Name Mane",
             "imageDetails":
             {
                  "imageId": "An image id",
                  "logoFrontId" : "A logo ID",
                  "logoBackId": "Another logo ID"
             }
          
    
    }

}
```

## Updated Card Status Behaviour

From this release, card's with the following statuses can perform Load Card transactions using the Create Transactions endpoint.

* 04
* 05
* 41
* 43
* 46
* 59
* 63
* 70
* 98
* 99
* G1
* G2
* G3
* G4
* G5
* G6
* G7
* G8
* G9

Additionally, card's with the following statuses can now be used when Unloading, Adjusting Balance and Transferring Funds using the Create Transactions endpoint:

* 04
* 05
* 41
* 43
* 46
* 54
* 59
* 62
* 63
* 70
* 83
* 98
* 99
* G1
* G2
* G3
* G4
* G5
* G6
* G7
* G8
* G9

## Updated Behaviour When Renewing, Updating, or Replacing Cards

From this release, updates will stop being sent to Visa and Mastercard when a card is renewed, updated or replaced if the card does not have a payment token associated with it.

## Updated Name of Card Status

From this release, the description for the card status 75 has changed from "Card Pin Blocked" to "Allowable Number Of PIN Tries Exceeded".

## Bugfix in Payment Token Updates

A fix has been made in this release where, if the setting dpan\_over\_fpan is set to N, and a card's status is set to G1, then the payment token is updated when renewing a card.