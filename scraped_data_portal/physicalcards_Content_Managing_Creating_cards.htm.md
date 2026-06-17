# 8 Creating Cards

## 8.1 Submitting Card Requests

You can use the Thredd API to create new card records. Thredd offers two types of API: SOAP Web Services or REST-based Cards API. These two options provide slightly different approaches to card creation. They also differ in the field options available with each request.

### 8.1.1 Using Thredd Web Services API (SOAP)

The Thredd Web Services API uses the SOAP protocol to send and receive messages in XML format. For common use case scenarios on how to use our web services to create and manage the cards in your program, see the [Web Services Guide > Use Case Scenarios](https://docs.thredd.ai/webservices/Content/Getting_started/User_Scenarios.htm).

For details of how to use the Card Create Web Service to create a physical card record, see the [Web Services Guide > Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm).

### 8.1.2 Using the Cards API (REST)

The Cards API use a REST-based method to send and receive messages in JSON format. For common use case scenarios on how to use our Cards API to create and manage the cards in your program, see the [Cards API Website > Recipes](https://cardsapidocs.thredd.com/recipes).

For details of how to use the Card Create API to create a physical card record, see the [Cards API Website > Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

### 8.1.3 Considerations when creating a card

There are typically three parts to creating a card:

1. Submit the create card request â Thredd returns a 9-digit Public Token, which can be used in all subsequent requests relating to the card record.
2. Activate the card â change the card status to *Active*, so that it can be used. For a physical card, the card should normally be created as inactive and only activated when the customer receives their card (you can provide your customers with an In-app option to request card activation or a phone number service to call to activate the card).
3. Load the card with a balance â update the available balance on the card, to reflect any money the customer has added to their account or loaded onto the card.

Thredd Web Services API and the Cards API provide different ways of implementing the above steps: Web services enable you to combine the above steps in a single API request or as separate requests. The Cards API split this out into three separate API requests.

When creating cards, you can use the default settings defined at a card product level, or for some fields, you can specify unique settings per card. For example, you can: change the default expiry date or change the card usage groups linked to the card.

## 8.2 Structure of a Card Record

For details of the most important attributes in a typical card record, see [Card Attributes](../Reference/Card_Attributes.htm).

## 8.3 Sending Card Records to your Card Manufacturer

When we receive your create card requests, we create a card record in the database. Multiple card records are then included in the daily card generation file that Thredd sends to your card manufacturer; the card records contain the instructions for generating the cards in your program. If required, you can request a copy of the card generation file (with sensitive card information removed for security reasons). For details, see [Working with Card Manufacturers](../Setup/Working_with_card_manufacturers.htm).

### 8.3.1 Cancelling a card order

If you need to cancel a card that has been ordered by mistake or where there is an error in the card record, please use the Thredd API (Cards Status Change web service or Card Update API) to change the card to a status that isn't 00, 02, or G1. This needs to be done before the card generation file is scheduled to be sent. For details, see the [Web Services Guide > Card Change Status](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Change_Status.htm) or the [Cards API Website > Update Card Status](https://cardsapidocs.thredd.com/docs/card-status).

After Thredd has sent the card generation file to the card manufacturer, you will need to contact your manufacturer directly to request removal of the card record. Please check with your card manufacturer for the processes, time-scales and costs around cancelling of orders.