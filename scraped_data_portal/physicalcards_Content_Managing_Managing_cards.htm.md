# 9 Managing Cards

This section provides an overview of some of the Thredd API (SOAP Web Services API or REST-based Cards API) functionality that can be used to manage the cards in your programme. For a details of the full functionality available , see the [Web Services Guide (SOAP)](https://docs.thredd.ai/Web_Services_Guide.htm) or the [Cards API Website (REST)](https://cardsapidocs.thredd.com/).

## 9.1 Initial Actions

### 9.1.1 Activating the Card

If the card is issued as inactive, it must be activated. This is typical for customers who sign up for a physical card via the Internet or their mobile App and who need to activate the physical card after it is delivered.

* On Web Services (SOAP), use [Card Activate](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Activate.htm).
* On Cards API (REST), use [Card Status.](https://cardsapidocs.thredd.com/docs/card-status)

### 9.1.2 Loading the Card

Where Thredd maintains the card balance on your behalf or has a copy of the balance, you can use the following web services or cards API to update the Thredd-held card balance:

* On Web Services (SOAP), to load a card without activation, use [Card Load](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Load.htm). To load and activate a card at the same time, use [Card Activate and Load](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Activate_and_Load.htm).
* On Cards API (REST) use [Load or Unload a Card](https://cardsapidocs.thredd.com/docs/loading-unloading-a-card#loading-or-unloading-a-card)

### 9.1.3 Applying Fees for Card Services

This service is available to Program Managers using the Thredd fees module (available where Thredd maintains details of the balance on the card). You can apply a fee for specified activities on the card, such as when your customer applies for a new card, or loads the card with money. For more information, see the [Fees Guide](https://docs.thredd.ai/Fees_Guide.htm).

## 9.2 Updating Cards

### 9.2.1 Managing the PIN

To set, retrieve, unblock and change the PIN associated with a card:

* On Web Services (SOAP), use [Card PIN Control](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_PIN_Control.htm).
* On Cards API (REST), use [Set PIN](https://cardsapidocs.thredd.com/docs/card-personal-identification-number-pin).

### 9.2.2 Changing Card Status

* On Web Services (SOAP), use [Card Change Status](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Change_Status.htm).
* On Cards API (REST), use [Card Status.](https://cardsapidocs.thredd.com/docs/card-status)

### 9.2.3 Updating Cardholder Details

To change the cardholder details linked to a card:

* On Web Services (SOAP), use [Update Cardholder Details](https://docs.thredd.ai/webservices/Content/Web_services_api/Update_Cardholder_Details_v1.htm).
* On Cards API (REST), use [Update Card](https://cardsapidocs.thredd.com/docs/updating-cardholder-details).

## 9.3 Viewing Card Transactions

Thredd provides a number of systems to enable you to generate test card transactions, view transactions on a card, and view both payment authorisation and financial messages relating to the card transactions in your program:

* **Card Transaction System (CTS)** â enables you to test your systemâs integration before you move into a production environment by running built-in tests to simulate different types of transactions (e.g., Point of Sale terminal, ATM, E-Commerce and refund). For details, see the [Card Transaction System Guide](https://docs.thredd.ai/Card_Transaction_System_Guide.htm).
* **Smart Client** â the legacy user interface for managing your cards and transactions on the Thredd systems. Using Smart Client, you can display details about card activity, transaction type, and customer interaction, and drill down into the details of specific transactions. For details, see the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).
* **Thredd Portal** â the new user interface for managing your cards and transactions on the Thredd systems. Using Thredd Portal, you can display details about card activity, transaction type, and customer interaction, and drill down into the details of specific transactions. For details, see the [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm).
* **External Host Interface** â a Thredd system which sends real-time payment authorisation requests and other types of financial messages to your systems. For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).
* **Transaction Reports** â an XML report containing details of daily transactions. For details, see the [Transaction XML Reporting Guide](https://docs.thredd.ai/Transaction_XML_Reporting_Guide.htm).