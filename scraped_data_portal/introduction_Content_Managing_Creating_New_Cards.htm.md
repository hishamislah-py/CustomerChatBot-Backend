# 6.1 Creating New Cards

Creating new card records on the Thredd system is done using either our REST-based cards API or SOAP web services . For more information see:

* [REST API: Cards API website > Creating a Card](https://cardsapidocs.thredd.com//docs/create-card-2)
* [SOAP API: Web Services Guide > Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm)

The Thredd API provide flexible options for configuring the appearance and features enabled on the new card. Below are a few examples.

![](../Resources/Images/Intro_card_payments/Card_configuration.png)

Figure 19: Examples of Configurable Card Features

For details of the card configuration options available when you create a card, see the [Cards API website](https://cardsapidocs.thredd.com//) or [Web Services Guide.](https://docs.thredd.ai/Web_Services_Guide.htm)

## 6.1.1 Activating your cards

Thredd supports multiple card activation scenarios for the cards in your programme:

* If you are creating a virtual card, the card can be created in a status of active, so that it can be used immediately.
* If you are creating a physical card, then the card can be created in an initial status of inactive, and when the customer receives their card, they can activate it using an App or online (with Thredd web services/cards API), through the Thredd IVR (interactive Voice Response) system or contacting your call centre.

## 6.1.2 Printing of cards

For a physical card, instructions are sent (on a daily basis or at a customised frequency) to your card manufacturer, for printing and dispatch (either directly to the cardholder or to the designated delivery address).

Virtual cards are created with a virtual image, which you can display to your customers on your customer portal/mobile app or send to them via email.

## 6.1.3 Loading cards

You can load a balance onto the card at the time when the card is created or at any time, using the [Load/Unload](https://cardsapidocs.thredd.com//docs/loading-unloading-a-card) Cards API (REST) or [Card Load](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Load.htm) web service (SOAP) .