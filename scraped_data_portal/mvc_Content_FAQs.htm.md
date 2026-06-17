# General FAQs

#### Q. What options are available for setting up the MVC?

For details of setup options, see [MVC Setup Options](Configuration/Setup_Options.htm). For examples of use cases for Master Virtual Cards, see [Use Case Scenarios](Getting_Started/Use_Case_Scenarios.htm).

#### Q. Is an MVC a virtual card?

No, an MVC is a type of card record that is used for holding account balances only. You can then transfer balances to and from other types of cards. You cannot use an MVC as a virtual card or to make payments.

#### Q. Will the card balance automatically sweep back to the MVC?

No, a [Card Linkage Group![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#) is required for sweeping back the balance. For more details, check with your Implementation Manager.

#### Q. If an MVC is a separate product and on a separate BIN to the secondary cards is it possible to link the cards?

Yes it is possible to link the cards where you can share the balances, and transfer funds between the primary and secondary cards.

#### Q. Can I get a Physical MVC?

No, a physical MVC does not exist. This is because there is a flag which stops the MVC going to print.

#### Q. Does an MVC have a full PAN?

Yes, as with other types of cards, an MVC is assigned a full PAN. However, it cannot be used for payment transactions. The PAN must **never** be revealed to the MVC holder (cardholder/corporate client) . If a reference to an MVC is required, they should be provided with the MVC's 9 digit token.

#### Q. Does the MVC have a start date, an expiry date and a CVV?

Yes, as with other types of cards, the MVC is assigned a start date, an end date and a CVV. However, it cannot be used for payment transactions. The CVV must **never** be revealed to the MVC holder (cardholder/corporate client) . If a reference to an MVC is required, they should be provided with the MVC's 9 digit token.

#### Q. Should the full card details be shared with the cardholder?

No, only the 9 digit token of the MVC can be shared with the cardholder.

#### Q. Is it possible to change an MVC into another card type?

No, once the card is created as an MVC, its type cannot be changed.

#### Q. Is it possible to change an existing card to an MVC?

No, once the card is created as a physical or virtual card, its type cannot be changed to an MVC.

#### Q. Can I view reports on MVC transactions?

Yes, you can receive details of MVC loads, unloads and balance transfers. These details are provided in your transaction XML reports and External Host Interface (EHI) data. For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.aiTransaction_XML_Reporting_Guide.htm) and [External Host Interface Guide](https://docs.thredd.aiEHI_Guide.htm).

#### Q. Can an MVC allow linked cards of more than one currency?

No, an MVC can only link to cards of the same currency.