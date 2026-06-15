# Creating a Card

This section provides instructions on how to create `Physical` and `Virtual` cards using the Thredd API. A card is a payment instrument that enables your customers to process transactions.

You can create three types of cards using the Thredd Cards API:

* <Glossary>Virtual Card</Glossary>
* Physical Cards
* <Glossary>Master Virtual Cards</Glossary>

The type of card you want to create is governed by what value you pass for Card Type, either `Physical`, `Virtual`, or `Master Virtual`.

> 📘 Note
>
> For more information on Master Virtual Cards, see [What is a Master Virtual Card](#what-is-a-master-virtual-card).

When you have created a card with a particular card type, you can convert it to another; for example, creating a Virtual Card and converting it to a Physical card. To find out more about converting cards, see [Converting a Card from Virtual to Physical](https://cardsapidocs.thredd.com/docs/converting-a-card).

> 📘 Please Note
>
> The fulfilment object only applies to cards that have a `Physical` `CardType` as these are posted out from your designated card manufacturer.

## Creating a card

### Prerequisites

Ensure that your Card's Product has been set up on the Thredd platform as part of implementation. Your card product ID allocates default card controls to a card as well as acts as an identifier for card design. If you are unsure of your Product ID, contact your Implementation Manager / Account Manager.

### Step 1:  Capture cardholder details

Before creating a card, ensure you have captured all the details relating to your customer.

### Step 2: Make a Card POST request

When you have captured details for your cardholder, you can make a POST /cards request. Ensure that you have the correct `cardProduct` defined in the request. Your `cardProduct` ID will be shared with you as part of the Thredd Implementation process.

```json Example Create Card endpoint
{{base-url}}/cards/
```

You can use the 'customerReference' field to store any ID you have for your customer from within your own system to act as a Foreign Key between your system and Thredd platform.

You can find examples of different Create Card payloads below:

```json Example Create Physical Card body
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

```json Example Create Virtual Card body
{
     "cardHolder": {
          "title": "Mr",
          "firstName": "Jon",
          "lastName": "Smith",
          "dateOfBirth": "1982-11-03"
     },
     "address": {
          "addressLine1": "32 Western Drive",
          "postCode": "S25 2BZ",
          "country": "GBR"
     },
     "virtualCardImageDetails": {
          "virtualCardImageId": "4155",
          "imageSize": 1
     },
     "cardType": "Virtual",
     "cardProduct": 10005,
     "designId": "New Card Brand",
     "customerReference": "my ref 12345"
}
```

```json Example Create MVC body
{
     "cardHolder": {
          "title": "Mr",
          "firstName": "Jon",
          "lastName": "Smith",
          "dateOfBirth": "1982-11-03"
     },
     "address": {
          "addressLine1": "32 Western Drive",
          "postCode": "S25 2BZ",
          "country": "GBR"
     },
    
     "virtualCardImageDetails": {
          "virtualCardImageId": "4155",
          "imageSize": 1
     },
     "cardType": "MasterVirtual",
     "cardProduct": 10005,
     "designId": "New Card Brand",
     "customerReference": "my ref 12345"
}

```

A successful response will return a 200 http code. The Thredd public token linked to the card will be returned in the response.

```json Example Create Card response
{
    "publicToken": "103169946",
    "customerReference": "CustNo12345A",
    "embossName": "Mr Johnny Bloggs",
    "maskedPan": "999999******0134",
    "startDate": "2023-02-28",
    "expiryDate": "2026-02-27"
}
```

> 👍 API Explorer
>
> See the [Create a card](https://cardsapidocs.thredd.com/reference/create-card) endpoint.

<br />

## Using the Thredd Public Token

The Thredd <Glossary>Public Token</Glossary> is a unique 9-digit number which is assigned to the card at the time of card creation. This number is for internal use on the Thredd system only, and enables you to view details of a card and manage the cards in your programme without needing to handle the full card PAN.

When you use the API to get details of a card or set details of a card, you can include the Thredd public token in your request to identify the card you want to view or update.

> 📘 Store the Thredd Public Token safely
>
> The Thredd Public Token is a primary key and must be stored safely as you will use it regularly.

## What is a Master Virtual Card

A *Master Virtual Card (MVC)* is a virtual card that is restricted to loading and unloading to a physical or virtual card and cannot be used for e-commerce or in-store transactions. An MVC is used to reflect the value of the ‘actual’ money in the Issuer's bank account. An MVC guarantees that the load is limited to the amount prefunded (i.e. loaded onto MVC) and gives the Programme Manager the ability to distribute funds immediately rather than having to wait for notification of each individual load into the Issuer Bank account.

For more information, see the [Master Virtual Cards Guide](https://docs.thredd.com/MVC_Guide.htm).

## Creating a Virtual Card for the Mastercard Wholesale Program

The Mastercard Wholesale Program (MWP) is a business-to-business (B2B) payment solution designed specifically for the travel industry to facilitate payments between travel intermediaries (such as travel agencies) and suppliers (like airlines and hotels). MWP is used with our Virtual Cards and is intended as single use and for wholesale travel programmes only.

MWP includes the Dynamic Interchange feature that enables issuers to set a predefined interchange rate when creating a virtual card using our REST API. Dynamic Interchange enables real-time rate selection without multiple BINs or API changes, helping travel and B2B programs simplify cross-border payments and maintain margin predictability.

> 📘 Note
>
> You must sign up to use your virtual cards with MWP. For more information, contact your account manager. You also need to set an MWP Product Code, which sets a default interchange for the product.

When you have signed up to use MWP, you can create a card with a valid fee percentage using the Create Card endpoint. The request must have a valid percentage in the feePercentage field. For information on the available  interchange rates, refer to the Mastercard documentation.

See the below example request:

```json Example Create Virtual Card for MWP
{
  "cardType": "Virtual",
  "cardProduct": 578,
  "cardHolder": {
    "title": "Mr",
    "firstName": "John",
    "lastName": "Smith",
    "dateOfBirth": "1963-11-22"
  },
  "address": {
    "addressLine1": "38 New Dover Road",
    "postCode": "BH12 0AL",
    "addressLine2": "Lordship Lane",
    "city": "Wallisdown",
    "country": "GBR"
  },
  "virtualCardImageDetails": {
    "virtualCardImageId": "11122",
    "imageSize": 1
  },
  "dynamicInterchange": {
    "feePercentage": 1.4
  },
}
```

> 📘 More Information
>
> * To view more information on the fields in the request and response, see [Create Card - Field Descriptions](https://cardsapidocs.thredd.com/docs/create-card-field-descriptions)
> * To view the endpoint in the API Explorer, see [Create a Card](https://cardsapidocs.thredd.com/reference/create-card).