# 5.3 Physical Cards

## 5.3.1 Chip Profiles

The [EMV![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMV is a payment standard for smart payment cards, payment terminals and automated teller machines (ATMs). EMV is an acronym for "Europay, Mastercard, and Visa", the three companies which created the standard.](#) chip is a microchip embedded on the payment card which stores card data. During an EMV terminal transaction, the chip generates a one-time unique code for each transaction.

The chip profile in a card determines where and how the card can be used and how the card will interact with the card reader terminal in-store or at an ATM. Different chip profiles are provided for standard, contactless and dual interface cards.

Below are examples of some of the configuration data set on the chip profile:

* Supported cardholder authentication methods (e.g., support for PIN, signature and none)
* Language, country and currency settings
* Limits and settings to control if transactions can be approved offline
* Transaction types that can be supported (e.g., cash or purchase)
* Channels that will be supported (e.g., POS, ATM)

The issuer chip profiles are set up within the card scheme.  All new chip profiles must go through testing and scheme certification.

An issuer can decide to support multiple chip profiles and assign a profile that is best suited for a particular portfolio ([BIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first four or six numbers on a payment card, which identifies the institution that issues the card.](#)). Typically, your issuer will offer a default chip profile for use on your cards. You can submit a change request to change the default chip profile.

In some cases, you may be able to use a previously certified chip, saving time to market.  Speak to your [card manufacturer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Company that prints newly issued physical cards and sends to cardholders.](#) about options.

## 5.3.2 Card Appearance

When issuing printed cards, you can control the branding, layout and appearance of the card.

### Cards sizes

The standard credit, debit and prepaid card size is 3.37 inches (85.6mm) length Ã 2.125 inches (53.98mm) height Ã 76 mm thick. For more information, see the [ISO/IEC 7810:2003](https://www.iso.org/standard/31432.html) standard (ID-1 category).

Please check with your card manufacturer and issuer for supported print sizes.

### Scheme branding vs your own branding

Depending on the type of card being issued, the scheme may stipulate dual branding, or permit you to issue cards with your own brand:

* **Dual branding** â the card features both the scheme logo and the program managerâs card brand. Typically required for debit and credit cards.
* **Private labelled cards** â the card features the program managerâs card brand only. Used for gift cards and prepaid cards only.

### Additional text

The card may feature text such as a contact centre number to call for card queries, or legal information about the legal entity that issued the card.

## 5.3.3 Card Personalisation

Card personalisation refers to the elements of the card that are customised to each cardholder. The type of dynamic data that is printed onto the base card includes:

* **Cardholder name** â the name printed, indented or embossed on the card, based on details supplied when you submit a create request.
* **PAN** â Thredd generated Primary Account Number (typically 16-digit), based on the available BIN range provided by your issuer. This is unique to each card.
* **Valid from and Expiry date** â Thredd generated date, based on the date of the request. You can optionally specify the card expiry date.
* **CVV2/CVC2** â system generated 3-digit Card Verification Value/Card Verification Code, used in card-not-present transactions to confirm that the cardholder has the card in their possession.

You can customise the order, font size and colour of these fields.