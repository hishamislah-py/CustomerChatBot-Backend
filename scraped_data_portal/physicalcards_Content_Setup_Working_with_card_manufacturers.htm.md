# 6 Working with Card Manufacturers

The production of physical (printed) cards requires the services of a [card manufacturer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd has relationships with existing card manufacturers, who we can instruct to print your cards. We use Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder.](#) (Card bureau). You will need to sign a commercial agreement with one of the card manufacturers which Thredd supports. The card manufacturer is responsible for the printing of cards; they can also handle other aspects of card fulfilment, such as packaging and delivery of cards and PIN letters directly to your customers.

Thredd has existing partner relationships with over 40 card manufacturers worldwide. We provide a pre-integrated service and interface to these card manufacturers.

To use a card manufacturer not currently integrated to Thredd, please discuss with your Business Development Manager or Onboarding Manager.

For further details of working with card manufacturers, please contact your Business Development Manager.

## 6.1 Card Generation File

Thredd provides an XML file-based interface which allows card manufacturers to accept card generation files from Thredd.

You can use the Thredd Web Services API or the Cards API to submit card creation requests. Card records can be created individually or in batch.

When we receive your create card requests, we create a card record in the database. Multiple card records are then included in the daily XML file that Thredd sends to your card manufacturer; the card records contain the instructions for generating the cards in your program.

Thredd provides two version types of the card manufacturer XML file:

* **Full version** - sent to your card manufacturer, containing sensitive card details, such as PAN, CVV2, PIN and track data
* **Truncated version** - this optional version can be sent to you, for your reference. In this version, fields containing sensitive card details (such as PAN, CVV2 and track data) will be removed

The frequency of sending of the card generation XML files is configurable. Note that some manufacturers charge per file or per record included in the file; check with your card manufacturer for details.

XML files are sent to the manufacturer using Secure File Transfer Protocol (sFTP).

## 6.2 Where to find out more

* For a list of Thredd-supported card manufacturers, see the [Web Services Guide > Card Manufacturers](https://docs.thredd.ai/webservices/Content/Reference/Card_Manufacturers.htm).
* For details of the XML file format which your card manufacturer must be able to receive, see the Thredd [Card Generation Interface Specification](https://docs.thredd.ai/Card_Generation_Interface_Specification.htm).
* For examples of card generation XML files, see the [Card Generation Interface Specification > Example Files](https://docs.thredd.ai/cardgeneration/Content/Card_Generation_Interface_Specification/Example_File.htm).
* For details of how to use web service or cards API to create card records, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm) or [Cards API Website](https://cardsapidocs.thredd.com/).