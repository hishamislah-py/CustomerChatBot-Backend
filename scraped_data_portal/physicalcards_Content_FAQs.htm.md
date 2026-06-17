# General FAQs

This section provides answers to frequently asked questions.

## Card Manufacturer

#### Q. Can you support a new card manufacturer?

If the card manufacturer you want to use is not on the [list of card manufacturers](https://docs.thredd.ai/webservices/Content/Reference/Card_Manufacturers.htm) supported by Thredd, please contact your Thredd Business Development Manager.

#### Q. Can I use more than one card manufacturer?

Yes. If your card programme supports special features or issues cards in different regions, you may need more than one card manufacturer, in which case we can this set up in the system. Each card manufacturer will need to be set up under a separate Thredd Scheme.

#### Q. Can I get a copy of the card generation file sent to the card manufacturer?

Yes. We can send you a copy of the card generation file (note that fields containing sensitive card details, such as Chip and Track data, will be removed).

## Supported Card Features

#### Q. What card features can the card manufacturer provide?

Most card manufacturers should support features such as CVV2, Magstrip, Chip&PIN and contactless payments. They should enable you to supply customised artwork designs for your cards. They should also be able to arrange for packaging and delivery of cards to your customers. Some card manufacturers may support additional value-added features, such as special print formats, support for biometric authentication, or special sizes and materials. Please contact your card manufacturer directly to discuss your requirements.

#### Q. Can I obtain a list of which text characters my card manufacturer will support?

Yes, you can find a list in the [Web Services Guide > String Cleaning and Approved Characters > Card Manufacturer Approved Characters](https://docs.thredd.ai/webservices/Content/Reference/String_Cleaning.htm).

## PAN Stock

#### Q. How do I request generation of new PAN stock?

New PAN stock may be required if you run out of existing PANs or your Issuer (BIN sponsor) changes the underlying BIN ranges assigned to you.

Please contact Thredd Customer Services to request additional stock or PAN stock changes.

New card requests can only be fulfilled if there is sufficient PAN stock available for your programme.

#### Q. Can Thredd delete PAN stock?

Yes, this is required if your underlying BINs change and your card PAN stock needs to be regenerated or if you close your programme with Thredd.

If changing BIN ranges requires generating new PAN stock, your existing PAN stock must first be deleted before the new PAN stock can be used.

Please contact Thredd Customer Services to request deletion of PAN stock.

## Card Expiry

#### Q: How does expiry date work for Gift cards and Flex cards?

The expiry date on the card is mandatory only if it is an [open loop card![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A card which can be used anywhere the card scheme (payment network) is accepted, without restrictions](#). It doesn't apply to gift cards or [Flex cards![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A Flex card works like a prepaid credit or debit card and can have multiple options for use, including online purchases. It can be used to pay for certain types of items, such as healthcare and medicines.](#) that have restricted usage; these types of cards do not need an expiry date displayed on the card.

#### Q: What are the Scheme rules around displaying the expiry date on the card?

Displaying the *expiry date* is only mandatory for open loop cards.

You can add optional text to clarify when the card expires (e.g., how long it will be valid from issue or activation date).

The *valid from* date is optional.

#### Q: Is it possible to set an unlimited expiry date?

No. For certain wallet accounts, such as the Master Virtual Cards (MVC), you can set this to the maximum suggested period (8 years).

#### Q: Why do Thredd Portal and Smart Client display a different expiry date to the physical card (when converted from a virtual card)?

When converting a virtual card to a physical card, the physical card is printed with the new requested expiry date, but the physical card first needs to be activated; the system will then update the expiry date in Thredd Portal and Smart Client.

## Card Balance

#### Q. What happens to the Balance and Fees on an expired card?

When a card date passes its configured validity period the card status changes to 54 (*Expired Card*) and the card can no longer be used. Two options are available for handling any remaining balance on the card:

* **Apply breakage fee on expiry is enabled** â the balance on the card is removed from the card automatically and put into an expiry transaction record.
* **Apply breakage fee on expiry is not enabled** â the balance will remain on the card. You can then do a balance adjustment or unload to remove the remaining funds. If a recurring fee has been set up then the system will continue to deduct the fee from the card until there is no balance

Fees are only applicable if you are using the Thredd Fees Module. See the [Fees Guide](https://docs.thredd.ai/Fees_Guide.htm).