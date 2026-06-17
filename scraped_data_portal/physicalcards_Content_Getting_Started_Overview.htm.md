# 2 Overview

This section provides an overview of how cards are set up on the Thredd system.

## 2.1 Card Programmes and Card Products

In the Thredd system, each [Program Manager![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) is associated with a card [issuer (BIN Sponsor)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme (payment network).](#) .

The Program Manager is linked to an internal Institution and internal Thredd Scheme, to reflect the regions, [BIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first six to eight numbers on a payment card, which identifies the institution that issues the card.](#) ranges, card type (physical, virtual or a combination) and [card manufacturer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd has relationships with existing card manufacturers, who we can instruct to print your cards. We use Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder.](#).

A typical card programme consists of one or more card products. The card product defines aspects of the card, such as the country of issue and base currency.

The Program Manager can define multiple card usage groups that control how and where the card can be used. The card usage group can be automatically associated with a card product and be applied to all newly created cards. Alternatively, an individual card record can be dynamically linked to card usage groups using the Thredd API (either at the time the card record is created, or afterwards).

The figure below provides further details.

![](../Resources/Images/Physical_cards/System_Hierarchy.png "System Hierarchy")

Figure 1: Thredd System Hierarchy

Your Thredd Implementation Manager will work with you to help define the requirements for your card programme and card products. Requirements are specified using a spreadsheet called the [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#). Once the requirements in the PSF have been agreed and signed off by the Program Manager and their issuer, the programme and product details are set up in the Thredd system. See [Setting up your Card Products](../Setup/Setup_card_products.htm).

## 2.2 Card Records

A physical card is represented by a unique card record in the Thredd system. You can submit create card requests using the Thredd API. See [Creating Cards](../Managing/Creating_cards.htm).

When the Thredd system receives the create card request, it checks that the details submitted are in the correct format and contain all the mandatory fields and then creates the card record. The card record will contain the unique features of the card, together with shared features of the associated card product. See [Key Attributes of a Physical Card](../Reference/Card_Attributes.htm).

Thredd returns a unique 9-digit [Public Token![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The 9-digit token is a unique reference for the PAN. This is used between and clients to remove the need for clients to hold actual PANs.](#), which can be used for any subsequent API requests against the card record.

### 2.2.1 Maintaining Card Records

You can use our Thredd Web Services API or the Cards API, together with the Thredd Public Token, to retrieve and update information about a card. For example to: activate the card, load a balance onto the card or adjust the balance, change the PIN, block and unblock the PIN, change the status of the card or update cardholder address and contact details. For details, see [Managing Cards](../Managing/Managing_cards.htm).

## 2.3 Card Manufacturers

The [card manufacturer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd has relationships with existing card manufacturers, who we can instruct to print your cards. We use Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder.](#) (card Bureau) is set up at a Thredd Scheme level. For more information, see [Working with Card Manufacturers](../Setup/Working_with_card_manufacturers.htm).

A card manufacturer is particularly relevant to physical card records, which need to be sent off for production; for virtual cards, Thredd provides an internal Thredd card manufacturer entity.

If you are using multiple card manufacturers for different card products, each will require its own Thredd scheme. If you are offering both physical and virtual cards, each will each will require its own Thredd scheme.

## 2.4 How to Configure your Cards

Your standard card configuration options are set up at the time when you first implement your card program through Thredd. Options are specified using the Thredd [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#). For more information, see [Setting up your Card Products](../Setup/Setup_card_products.htm).

There are additional customisation options available for designing the appearance and features of your physical cards. See [Physical Card Customisation](../Setup/Card_configuration.htm).

If you are also offering virtual cards, details of how to configure your virtual cards are covered in the [Virtual Cards Guide](https://docs.thredd.ai/Virtual_Cards_Guide.htm).

### 2.4.1 Card Security Features

Your physical cards can be configured with a range of embedded security features, to help protect your cardholders from the risks of fraud. See [Card Security Features](../Setup/Security_features.htm).