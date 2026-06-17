# 5.2 Virtual Cards

A virtual card is a card that does not have any physical cards generated and can only be used to pay for purchases online (e-commerce) or via Mail and Telephone Order (MOTO). Virtual cards are set up at the Card Scheme (Mastercard or Visa) with restricted usage and cannot be used at a Point of Sale (POS) terminal or for ATM withdrawals. You can define on the Thredd system further restrictions as to how and where the virtual card can be used.

When a virtual card is created, it functions like a normal card record on the Thredd system, however the card record is not sent to print. This means it can be issued instantly to your customers, as there is no need to wait for physical card delivery. All relevant card details, such as the card Primary Account Number (PAN), the Expiry Date and the CVV2 number can be displayed on the virtual card image or delivered by different means, such as: SMS, email, or through your own Customer mobile app or Customer Portal.

## 5.2.1 Virtual Cards and Tokenisation

It is possible to provide virtual cards only, which are available for immediate use, without the need for any physical card. Virtual cards that have been tokenised via the Mastercard Digital Enablement Service (MDES) or Visa Digital Enablement Platform (VDEP) can also be used at POS and contactless-enabled ATMs. See [Tokenisation](https://docs.thredd.ai/More_Information/Tokenisation.htm).

## 5.2.2 Virtual Card Image Design

If you are using the Thredd system to generate a virtual card image you can customise the appearance of the background image and dynamic text elements. Alternatively, you can generate the virtual card image on your own systems, using the details returned in the Thredd response to a Create Card request. See the example below.

![](../Resources/Images/Intro_card_payments/Example_card_1.png)

Figure 17: Virtual Card Configuration

We can return full PAN if you are [PCI-DSS compliant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes. All customers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security](#), else the middle 6 digits of the PAN will be masked.

For more information, see the [Virtual Cards Guide](https://docs.thredd.ai/Virtual_Cards_Guide.htm).