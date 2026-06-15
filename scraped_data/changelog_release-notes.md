# Release Notes for 17 February 2023

New changes to the GPS Cards API for the week ending 17th February 2023.

* [Changes to Status Codes](#changes-to-status-codes)
* [New fields added to Retrieve Card Details endpoint](#new-fields-added-to-retrieve-card-details-endpoint)

## Changes to Status Codes

Changes have been made to how Status Codes are used in this release so that statuses are the same across all GPS instances. Previously, Cards API used unique card statuses that were formatted as text. Statuses have now been changed to display as a two-digit alphanumeric code.

The following status codes are now available when updating and retrieving a card status:

* **00** indicates Active status
* **04** indicates Card Capture status
* **05** indicates Do Not Honour status
* **41** indicates Lost Card status
* **43** indicates Stolen Card status
* **46** indicates Closed Account status
* **54** indicates Expired Card status
* **57** indicates Transaction not permitted to cardholder status
* **59** indicates Suspected Fraud status
* **62** indicates Restricted Card status
* **63** indicates Security Violation status
* **70** indicates Cardholder to contact issuer status
* **83** indicates Card Destroyed status
* **98** indicates Refund given to customer status
* **99** indicates Card Voided status
* **G1**, used for a short-term block on all transactions (excluding credits and refunds)
* **G2**, used for a short-term block for all transactions
* **G3**, used for a long-term block on all transactions (excluding credits and refunds)
* **G4**, used for a long-term block on all transactions

The following status codes are now available when viewing card statuses that are changed by other products:

* **G5**, changed by GPS Protect, and used for a short-term block on all transactions (excluding credits and refunds)
* **G6**, changed by GPS Protect, and used for a short-term block on all transactions
* **G7**, changed by GPS Protect and used for a long-term block on all transactions (excluding credits and refunds)
* **G8**, changed by GPS Protect and used for a long-term block on all transactions
* **G9**, changed by IVR and used for a Lost/Stolen block on all transactions (irreversible status)

> 👍 Documentation
>
> * For more information on card statuses, see [Card Status Change](https://cardsapidocs.thredd.com/docs/card-status)

## New fields added to Retrieve Card Details endpoint

Two new fields have been added to the Retrieve Card Details endpoint, replacing the Status field that detailed the Card Status previously.

* **cardStatusCode** holds the two-digit card status code
* **cardStatusDescription** holds the code two-digit code and a description of what the code does

> 👍 Documentation/API Explorer
>
> * For more information on this endpoint, see [Retrieve a Card](https://cardsapidocs.thredd.com/docs/retrieve-a-card)
> * To try the Retrieve a Card endpoint, navigate to [Retrieve a Card](https://cardsapidocs.thredd.com/reference/retrieve-card) in API Explorer