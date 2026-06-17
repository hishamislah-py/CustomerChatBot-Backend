# 3 Setting up your Card Products

This section describes the options available for configuration of the cards in your programme. Your Implementation Manager will work with you to discuss your requirements and complete the [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#), then send this to you and your Issuer (BIN sponsor) for sign-off.

## 3.1 Programme Details

Below are examples of settings applied at a Thredd scheme level to the cards in your programme.

| Option | Description |
| --- | --- |
| Card Validity Period (in months): | Card expiry date period, which will be used to calculate the Expiry Date that is printed on the physical card (e.g., 36 months). For details, see [Calculating the Expiry Date](../Reference/Generated_Card_Elements.htm#Calculat).  **Note**: The expiry date can be amended during card creation to any date within the validity period; for more information, see [Creating Cards](../Managing/Creating_cards.htm). |
| Card Activation period | Internal expiry date, calculated from the date the card is activated (e.g., 12 months). For details, see [Calculating the Expiry Date](../Reference/Generated_Card_Elements.htm#Calculat). |
| Card Type | Type of physical card product: *Magnetic strip*, *Chip* or both. For details, see [Card Security Features](Security_features.htm). |
| Card Manufacturer (bureau) | Name of your card manufacturer. For details, see [Working with Card Manufacturers](Working_with_card_manufacturers.htm). |
| BIN | The 6-8 digit [BINClosed The Bank Identification Number (BIN) is the first six to eight numbers on a payment card, which identifies the institution that issues the card.](#) provided by your issuer. The BIN is used for the first 6-8 digits of the card's Primary Account Number (PAN). For details, see [Generating the PAN](../Reference/Generated_Card_Elements.htm#How). |
| Start Date | Expected period when your BIN will go live (in months). |
| Card product setup | The type of card products you want:   * Physical card only * Virtual card only * Ability to convert virtual card to a physical card * Both physical and virtual cards.   For more information, see the [Virtual Cards Guide > Virtual Card Setup > Summary of Virtual Card Setup Options](https://docs.thredd.ai/virtualcards/Content/Virtual_Cards_Setup/Virtual_Card_Setup.htm#Summary). |

## 3.2 Card Product Options

Your programme can consist of one or more card products. Below are examples of options that can be configured at a card product level.

| Option | Description |
| --- | --- |
| Product ID | Unique identifier of your card product (assigned by Thredd). If your programme supports multiple card products, each card product must have a unique product ID. When creating or updating cards through the Thredd Web Services API or the Cards API, you can use the product ID to link a card to a specific card product. |
| Product name | Name you assign to your card product. |
| Currency | Base or default currency of the card product. |
| Country of issue | Default country of issue. |
| Card Control Groups | Thredd offer several types of card usage groups, which control where and how the card can be used. For a list of available groups that can be set up and linked to a card product, see [Card Control Groups](#Card). |
| Card Acceptor Lists | Acceptor lists are used to control at which Merchant stores the card can be used, based on a list of *permitted* or *blocked* Merchant Category Codes (MCCs). For a list of available card acceptor lists that can be set up and linked to a card product, see [Card Acceptor Lists](#Card2). |
| Card Design ID | Each card product can have a default card design artwork associated with it. The card design artwork must be provided to your card manufacturer. |
| Image ID | Each card product can have a customised virtual card image design artwork associated with it, which can be displayed to the customer in your App. This image can be created by Thredd or you can provide your customers with your own customised version. For details, see the [Virtual Cards Guide](https://docs.thredd.ai/Virtual_Cards_Guide.htm). |
| Product type | The type of security and card profile features supported on the physical card: This can be one of the following:   * 0 â Chip and Magstripe * 1 â Magstripe Only * 2 â Chip and Contactless   For details, see [Card Security Features](Security_features.htm). |
| Card product | The type of card brand. This can be one of the following:   * MCRD â Mastercard * MAES â Maestro * VISA â Visa |

If your card programme supports multiple currency-country combinations, you will need to set up a separate card product for each combination.

## 3.3 Card Control Groups

Card Control Groups define where and how the card can be used, and provide other features to ensure card security and reduce the risks of fraud. Below is a list of the available card control groups that can be set up in the system. You can specify your card control requirements on the Thredd [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#); your Implementation Manager will set this up for you in the system.

When submitting your create card request via our Web Services or Cards API, the default card groups configured for your card product can be applied. Alternatively, you can specify which card groups to link to the card.

| Card Control Group | Description |
| --- | --- |
| Usage Group | Enable detaled configuration of how a card can be used. For more information, see [Card Usage Options](../Reference/Card_Usage_Options.htm). |
| Velocity Group | Restricts the frequency and/or amount at which the card can be loaded or unloaded, or used at a POS terminal.  For example: Â£600 daily spending limit |
| Auth Calendar Group | Controls the dates and times when cards can be used.  For example: prevent usage on Sabbath days and religious holidays. |
| MCC Group | Controls the type of merchants where the card can be used. The Merchant Category Code (MCC) is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant. For example: prevent card usage on gambling sites  For a list of MCCs, see [EHI Guide > Merchant Category Codes](https://docs.thredd.ai/ehi/Content/Appendices/Merchant_Category_Codes.htm). |
| FX Group | Controls the rates for FX currency conversions if the purchase currency is different from the card's currency. |
| Payment Token UsageGroup | Defines configuration options specific to the provisioning of a digital payment token. You can specify more than one recipient.  **Note**: Only applicable if tokenisation (digital wallets) is enabled for the card product. |

## 3.4 Card Acceptor Lists

Card Acceptor lists control the merchant stores and websites where the card can be used (based on the merchant ID, DE 042) . There are two types of lists:

| Card Acceptor List Type | Description |
| --- | --- |
| Permission List | Provides a list of merchants where a card can be used. |
| Deny List | Provides a list of merchants where a card cannot be used. |

The figure below provides an overview of how card product controls work.

![](../Resources/Images/Physical_cards/Card_Configuration_details.png "Card Configuration and Card Controls")

## 3.5 Card Production Scheduling

Card production is scheduled on a Program Manager level and applies to all cards in your programme. Below are options available for configuring how the production file is generated:

| Option | Options available |
| --- | --- |
| Schedule type | Can be sent to the **Card Manufacturer** or to the  **Card Manufacturer + Program Manager**. |
| When scheduled to run | Can be scheduled to run at a specified time on any required days of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday. |
| File format | The file can be produced in one of the following formats:   * **Full Format** â sent to the Card Manufacturer only. * **Cut Down Format**â sent to the Program Manager, with sensitive card data removed. * **Cut Down Format with Masked PAN**â sent to Program Managers who are not [PCI CompliantClosed The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major card schemes (payment networks). All Program Managers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/](#)). |
| File production limits | You can specify the following minimum thresholds which trigger the sending of the card production file:   * Minimum number of card records â that must be in the file before it is sent to the card manufacturer. * The minimum number of days â between two file creations (regardless of whether the minimum number of requests is met or not). |
| Email address | The email addresses to notify recipients that the card production file has been produced. The actual file is sent via sFTP. |