# 1 Introduction

Thredd supports the creation of two types of cards:

* Physical cards
* Virtual cards

A Virtual Card is a card that does not have any physical plastics generated and can only be used to pay for purchases online or via Mail and Telephone Order (MOTO). Virtual cards are set up at the Card Scheme (payment network) (e.g., Mastercard, Visa or Discover) with restricted usage and cannot be used at a Point of Sale (POS) terminal or for ATM withdrawals, though they can be used with digital wallets. You can define on the Thredd system further restrictions as to how and where the virtual card can be used. See [Virtual Card Setup](Virtual_Card_Setup.htm).

When a virtual card is created, it functions like a normal card record on the Thredd system, however the card record is not sent to print. This means it can be issued instantly to your customers, as there is no need to wait for physical card delivery.

To issue a virtual card all relevant card details, such as the card Primary Account Number (PAN), Expiry Date and CVV number must be delivered to the cardholder. Options for delivery include your own customer mobile app or portal, SMS, or email. The card Primary Account Number (PAN) and CVV number can be retrieved using our REST APIs. Alternatively a masked PAN

can be displayed with the middle six digits delivered by Thredd SMS.

## 1.1 Thredd Virtual and Physical Card Options

Thredd provides a number of options for setting up your virtual card program:

* Virtual Cards only
* Both Virtual and Physical Cards â set up as different products with different PANs
* Virtual Cards can be converted to physical â keeping the same PAN

Both virtual and physical cards are created using the Thredd API. At the time of submitting card creation instructions using the API, you can specify whether to create a physical or virtual card.