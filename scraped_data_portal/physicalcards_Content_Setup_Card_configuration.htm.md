# 4 Physical Card Customisation

This section describes some of the options available for configuring the appearance and features of your physical cards:

## 4.1 Card Appearance

The card appearance includes the card dimensions, weight and the material used in its design. It also includes the baseline artwork, such as the colours and brand logos, and any text to be printed on the card.

* **Card logos**: The Card Schemes (payment networks) have strict rules around the placement and display of their brand logos. The scheme logos typically must be included on the card. The exception to this rule is for certain types of [private-labelled![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A card which features the program managerâs card brand only (without the Visa or Mastercard logo).](#) cards, such as prepaid gift cards.
* **Your own brand and logos**: This includes any background colours, font types and colours and logo.
* **Text**: If you have any text (such as an email or contact number for card-related queries or to report lost and stolen cards), this is typically included in the card artwork.

These are standard features of the card and are the same for all the cards within your card product. If your programme has multiple card products with different card designs, you can have separate card artwork for each card product. The base artwork features are typically pre-printed in batch as base card plastics to help reduce production and printing costs. (The additional personalised elements, unique to each cardholder are then printed onto the card whenever a new card is ordered.)

Your artwork must typically be signed off by your issuer (BIN sponsor) and potentially by the Card Scheme (payment networks). If you are using standard issuer artwork designs, pre-approved by the card scheme, further approval is not required.

## 4.2 Card Physical Dimensions and Materials

The example below describes the typical payment card physical dimensions:

![](../Resources/Images/Physical_cards/Card_Example_front.png "Example of a payment card - showing dimensions")

Figure 2: Example of a payment card - showing dimensions

The standard ISO financial payment (Credit/Debit) card size in centimetres is 8.56 cm wide by 5.398 cm high. The standard payment card thickness is 0.76 mm thick. This size standard uses the ISO/IEC 7810 ID-1 format. See [Wikipedia: ISO/IEC 7810.](https://en.wikipedia.org/wiki/ISO/IEC_7810)

Adopting standard dimensions across card issuers (BIN sponsors) and countries ensures that any payment card will fit into a standard card reader terminal or ATM machine.

The weight and material of the card may differ. The majority of payment cards are made out of plastic (typically PVC) and weigh around 5 grams; some cards may be made out of metal and weigh around 17.5 grams. Please discuss your card requirements with your card manufacturer.

If the card is to be used only as a contactless card or tokenised device (such as a key ring fob), then card dimensions are less important. Please discuss your requirements with your card manufacturer.

## 4.3 Card Fields and Card Personalisation

A typical card contains dynamic fields which are printed on demand. These fields are personalised to the cardholder or to each card record and are printed or embossed onto the base card plastics (which were previously produced as part of a batch production run). The personalised fields are printed by the card manufacturer based on the card record details supplied by Thredd in the card generation file (see [Card Generation File](Working_with_card_manufacturers.htm#Card)).

The locations of fields, and whether they appear on the front or the back of the card, may vary depending on your card design; please check with your issuer (BIN sponsor) or card manufacturer for any specific requirements and restrictions that may apply. Below is an example.

![](../Resources/Images/Physical_cards/Card_elements.png "Examples of a payment card showing the elements")

Figure 3: Example of a payment card

Refer to the table below for a description of the fields and other elements on the card:

| Field | Description |
| --- | --- |
| Personalised elements - customised to the card or cardholder; printed per card record | |
| PAN | The permanent account number (PAN) is the long number (typically 16-19 digits) that is either printed or embossed on the card. Thredd generates this from the available BIN stock for your programme. This is unique to each card. For details, see [Generating the PAN](../Reference/Generated_Card_Elements.htm#How). |
| Cardholder title | Cardholder title (e.g., Mr, Mrs, Ms) based on the information you supplied in your create card request.  This field can be omitted for prepaid gift cards or certain types of corporate cards. |
| Cardholder first name | Cardholder first name based on the information you supplied in your create card request.  This field can be omitted for prepaid gift cards or certain types of corporate cards. |
| Cardholder last name | Cardholder last name based on the information you supplied in your create card request.  This field can be omitted for prepaid gift cards or certain types of corporate cards. |
| Card start date | Date the card is valid from, based on the card record defined start date. This is an optional field and may not appear on all cards. |
| Card expiry date | The card's expiry date, as calculated by Thredd according to your card product. This field is mandatory on most open loop cards (which can be used at any merchant site using the card scheme (payment network), but can be omitted on cards with restricted usage, such as prepaid gift cards and certain types of corporate cards. For details, see [Calculating the Expiry Date](../Reference/Generated_Card_Elements.htm#Calculat). |
| CVV2 (Security Code) | The three-digit security code (Card Verification Value). This is a random 3-digit code generated by Thredd. |
| Card reference | You or the printer can optionally add a text field containing a unique card or account reference. |
| QR Code | Your card manufacturer may be able to support a QR code that will be printed on the card. You can add separate values to each card using the ThreddWeb Services API. or the Cards API. |
| Card Security elements - embedded features of the card; printed in batch per card product (EMV Chip and magnetic strip profile are data added when the card is printed) | |
| Signature strip | Blank area on card where the cardholder can add their signature. See [Signature Strip](Security_features.htm#Signatur). |
| Magnetic strip | The magnetic strip is the long thin stripe on the back or front of the card, which contains data unique to the card. The card data on the magnetic strip is personalised when the card is printed. See [Magnetic Strip](Security_features.htm#Magnetic). |
| EMV Chip | Chip embedded on the card, which contains electronic data relating to the card. See [Chip Profile](Security_features.htm#Chip). |
| Card Verification Values | See [Card Verification Values](Security_features.htm#Card). |
| Security hologram | Visa and Mastercard mandate the use a holographic security logo. The hologram provides a means of protection against card forgery. The hologram is punched onto the pre-printed cards and is designed to reflect light and appear three-dimensional. |
| Card Design elements - branding elements printed on the card; pre-printed in batch per card product | |
| Scheme logo | The card scheme logo (Mastercard or Visa) is required for all scheme cards, excluding some private-labelled cards. Your card design should use approved scheme images. |
| Your brand logo | Your company name or logo can be included in your card design. |
| Your contact details | Provides your customers with details of how to get in touch, such as an email or contact number for card-related queries or to report lost and stolen cards. |