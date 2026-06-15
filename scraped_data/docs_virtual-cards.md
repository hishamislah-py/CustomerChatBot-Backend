# Virtual Cards

A Virtual Card is a card that does not have any physical plastics generated and can only be used to pay for purchases online or via Mail and Telephone Order (MOTO). Virtual cards are set up at the Card Scheme (payment network) with restricted usage and cannot be used at a Point of Sale (POS) terminal or for ATM withdrawals. You can define on the Thredd system further restrictions as to how and where the virtual card can be used.

When a virtual card is created, it functions like a normal card record on the Thredd system, however the card record is not sent to print. This means it can be issued instantly to your customers, as there is no need to wait for physical card delivery. All relevant card details, such as the card Primary Account Number (PAN), the Expiry Date and the CVV number can be displayed on the virtual card image or delivered by different means, such as: SMS, email, or through your own Customer mobile app or Customer Portal.

## Virtual Cards and Tokenisation

It is possible to provide Virtual cards only, which are available for immediate use, without the need for any physical card. Virtual cards that have been tokenised (see [Tokenisation](https://docs.thredd.com/More_Information/Tokenisation.htm)) can also be used at POS and contactless-enabled ATMs.

## Virtual Card Image Design

If you are using the Thredd system to generate a virtual card image and you want to customise the appearance of the background image and dynamic text elements, please complete the Virtual Card Image tab on your Thredd Product Setup Form (PSF). Alternatively, you can generate the virtual card image on your own systems, using the details returned in the Thredd response to a Create Card request.

See the example of a customised virtual card image below.

<Image title="Virtual_Cards.png" alt="Figure: Example of a Virtual Card Image" align="center" src="https://files.readme.io/21315cb-Virtual_Cards.png">
  Figure: Example of a Virtual Card Image
</Image>

For more information, see the [Virtual Cards Guide](https://docs.thredd.com/Virtual_Cards_Guide.htm).

## Converting a Virtual Card to a Physical Card

When you convert a virtual card to a physical card it will adopt the same settings as the virtual card. The card is created with the same PAN. A new expiry date and CVV2 are generated if the conversion falls in a different calendar month to the virtual card creation.

The card instructions are sent to your card manufacturer for printing and despatch to the cardholder.

Following successful conversion, any replacement or renewal cards are generated as physical cards. The cardholder can still continue to use their virtual card until the physical card is activated, after which the virtual card will stop working.

> 👍 Documentation
>
> For more information on Virtual Cards, refer to the [Virtual Cards Guide](https://docs.thredd.com/virtualcards/Content/Home.htm)