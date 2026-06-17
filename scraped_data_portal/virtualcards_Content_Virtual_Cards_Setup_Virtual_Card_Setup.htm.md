# 2 Virtual Card Setup

Below are details of the steps you need to complete to set up a virtual card product:

* [Decide how you want to set up your Virtual Card Product](#_Decide_setup_VCP)
* [Complete Issuer (BIN Sponsor) Forms for Virtual Cards](#_Complete_Issuer_Forms)
* [Choose how to show card details to the cardholder](#Complete)
* [Set up your Virtual Card Usage Groups](#_Set_up_VC_Groups)
* [Select How Card Details are Displayed](#Select)

Optional setup:

* [SMS Message Configuration](#_SMS_Message_Configuration)
* [Set up PGP-Encryption for Virtual Card Images](#_Set_up_PGP-Encryption)

Each of these steps is described in further detail below.

## 2.1 Overview of Steps

The following section covers the steps required to set up a virtual card product.

### 2.1.1 Decide How You Want to Set Up Your Virtual Card Product

Discuss with your Implementation Manager how you want Thredd to set up your virtual card product. Virtual and physical card settings are applied at the internal Thredd scheme level. Options available include:

* **Physical cards only** â all cards are created as physical cards.
* **Virtual cards only** â all cards are created as virtual cards.
* **Conversion of virtual cards to physical cards** â all cards are created initially as virtual cards and need to be converted to physical cards using the Thredd API. See [Converting Virtual Cards to Physical Cards](#Converti).
* **Both physical and virtual cards** â for this option you require separate internal Thredd schemes set up for both physical and virtual cards.

For more information about the Thredd setup and configuration, see [Summary of Thredd Virtual Card Setup Options](#Summary).

### 2.1.2 Complete Issuer (BIN Sponsor) Forms for Virtual Cards

To support virtual cards, your card issuer (BIN sponsor) will need to complete the relevant Mastercard or Visa card setup forms and specify virtual card creation; they will need to assign a sub-BIN range for the use of virtual cards. All card transactions on this sub-BIN range will be restricted to online usage only.

For details of which scheme forms to complete, please check with your Implementation Manager.

### 2.1.3 Choose how to show card details to the cardholder

You can obtain the virtual card details from Thredd by using your the encrypted endpoint to receive the masked PAN and then send the masked part of the PAN using Thredd SMS. If you are fully PCI compliant you can receive the full PAN in your webservices response

This solution is dependant on your level of PCI compliance and, if you have an Issuer, that your Issuer is happy to sign off full PAN in webservices.

### 2.1.4 Confirm whether you are able to display Full Card PAN

If you want to display the full PAN in the virtual image you must be [PCI Compliant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes. All customers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security](#).

To remove the need for full PCI compliance, you can use a number of options:

* You can request a virtual card image that replaces the PAN with a customer account number that you supply. When you submit a Create Card request using the Thredd API, you can then populate your customer account number: in SOAP web services, this is done using the `<CustAccount>` field; In REST-based Cards API, this is done using the `customerReference` field.
* The masked PAN (middle 6 numbers of the PAN) and the CVV could be sent to the cardholder via another means (e.g., SMS). See [SMS Message Configuration](#_SMS_Message_Configuration) .
* Thredd can display the [Thredd Public Token![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A unique 9-digit number assigned by Thredd, to represent the linked card. The public token can be used instead of the PAN for all web services API requests.](#) in place of the PAN.

* The Thredd MeaWallet service provides an alternative option for displaying full PAN and other card details to the cardholder if you are not PCI Compliant. See [MeaWallet Integration](#_MeaWallet_Integration).

### 2.1.5 Set up your Virtual Card Usage Groups

Each of your card products is linked to a default set of card usage groups in the Thredd system. The usage groups enable you to control how your virtual cards can be used.

Examples of card groups include: Velocity limits and Card Usage.

#### Velocity Limits Groups

For a virtual card product, cash limits are set zero, so the card cannot be used at a Point of Sale (POS) terminal.

#### Card Usage Groups

For a virtual card product, card use at Point of Sale (POS) terminal is disabled. The following methods of using the card are typically enabled for a virtual card:

* Card Not Present (Ecommerce)
* Card Not Present (MOTO)
* Manual Key entry transaction - Card Not present

You can decide whether to enable the following transactions:

* Card Not Present (Recurring)
* Allow Manual Key entry transaction - Cardholder Not present

The following transaction types are usually enabled for a virtual card:

* Credits / Refunds transactions
* Purchase of Goods & Services
* Credits Auth

See the example below of setup of card usage groups on the Product Setup Form:

![](../Resources/Images/Virtual Card Setup.png)

Figure 1: Card Usage Groups on the Product Setup Form

#### Include Flag for Tokenisation

If a virtual card is tokenised into a digital wallet, the token will have itâs own separate usage group which can enable usage at POS terminals. See the [Tokenisation Guide](https://docs.thredd.com/Tokenisation_Guide.htm) for more details.

## 2.2 Optional Setup

Below are additional options you can set up for your virtual cards.

### 2.2.1 SMS Message Configuration

Thredd provides a default SMS message that can be enabled at the time when you create the virtual card (using the Thredd API). If you choose to display the masked PAN then you will need to send the remaining digits via SMS

If you want to change the wording on the default SMS message, Thredd can optionally configure the dynamic field content included in the SMS message sent to the cardholder when you use the SOAP web services API to create a virtual card or renew a card image. This is set at a Program level and applies to all products under a Thredd Scheme.

For a full list of parameters that can be used, see the [Mobile Text Messaging (SMS) Guide](https://docs.thredd.com/SMS_Guide.htm).

#### Example of Default SMS

[Copy](javascript:void(0);)

```
â3 digit Security Code : %CVV% and the middle 6 digits of your Virtual Card is %PAN6%. Thank youâ 
```

Important code lines:

* `%CVV%` is the cardâs CVV
* `%PAN6%` is the middle 6 digits of the PAN.

#### Enabling SMS messages

Once set up, to enable this option in your [Create a Card](Using_the_Web_Services_API.htm#_Create_a_Card)  web service request, you must set the `<sms_required>` field in your request, to 1. The phone number to where to send the SMS is defined in the `<Mobile>` field of the Create a Card request.

Speak to your account manager regarding SMS support if using the Cards API (REST).

Thredd charge a fee for sending SMS messages. Refer to your Contract for details.

### 2.2.2 Set up PGP-Encryption for Virtual Card Images

Where Thredd provides the virtual image, we support PGP-encrypted images. Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication and is used for signing, encrypting, and decrypting graphic files to increase the security of email communications.

PGP Keys must be exchanged between the Program Manager and Thredd. Normally, we ask you to generate the PGP key and provide it to us. Separate keys are required for Thredd Test and Production environments.

Thredd use the PGP key to encrypt the virtual card image. The encrypted virtual image of the card (with details such as PAN, CVV and expiry date embossed on it) will be returned in the response to a card create or image regenerate web service request. For details, see [Using the Web Services API](Using_the_Web_Services_API.htm).

You then use your PGP key to decrypt the image.

PGP keys are required for full PAN to be returned in the `GetCardImage` data.

PGP keys currently only work in Web Services (SOAP) and do not work in the Cards API (REST).

## 2.3 Converting Virtual Cards to Physical Cards

This section is relevant to Program Managers who are converting a virtual card to a physical card. You can convert a card using either the SOAP web services (see [Converting a Virtual Card to a Physical Card)](Using_the_Web_Services_API.htm#_Converting_a_Virtual) or using the REST Cards API (see [Converting a Virtual Card to a Physical Card)](Using_Cards_API.htm#_Converting_a_Virtual).

On card convert, the virtual and physical card share the same PAN and Thredd token. Virtual and physical card share the same card record in the Thredd system, so cardholders can track their transactions on the card and view both physical card and historical virtual card transactions[1  Thredd provide an option to create a separate PAN and Thredd token on card convert. In this case, the system creates two linked card records, and both cards can continue to be used. If you want this option, we recommend you ask your implementation manager to set up separate physical and virtual card products.](#).

If you want to convert a virtual card to a physical card, you need to use the same card keys (e.g., MDK, CVK, PKI keys) as supplied by the card manufacturer for both the virtual card and physical card.

### 2.3.1 Printing of Physical Cards

When your card product is set up, it is linked to a card manufacturer (card bureau). You will need to go through the integration and testing process of setting up your physical cards via your chosen card manufacturer: get your card design approved by your Card Scheme (payment network), create test card plastics, test CHIP profiles and create live base cards for use. This needs to be done in advance, so your cards will be ready for personalisation and printing when the virtual card is converted to a physical card.

When you convert a virtual card to a physical card, the card instructions are sent to your card manufacturer, to print and despatch the card to the specified address. The cardholder can continue to use the virtual card until they have received and activated the physical card[2  For security reasons, we recommend you either set the card to an inactivate status or ensure that the card usage groups linked to the card enforce virtual only usage on the physical card until the cardholder has received and activated the card.](#).

### 2.3.2 Card CVV and Card Expiry

When converting to a physical card, you can optionally keep the same expiry date and CVV2. Note that a new expiry date and [CVV2](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Convert_to_Physical.htm) will be generated if the conversion falls in a different calendar month to the virtual card creation.

The CVV is calculated by encrypting the bank card number and the expiration date with keys, so if the expiry date for the physical and virtual card is different, the CVV will also be different.

* If using the REST-based Cards API : You can set the expiry date for the virtual card, using the `expiryDate` field in the [Create a Card](Using_Cards_API.htm#_Create_a_Card) API.  When converting a virtual to physical card, you can use the `newExpiryDate` field in the [Convert Card](Using_Cards_API.htm#_Converting_a_Virtual) API to set the expiry date.
* If using SOAP web services: You can set the expiry date for the virtual card, using the `<ExpDate>` field in the [Create a Card](Using_the_Web_Services_API.htm#_Create_a_Card) web service.  When converting a virtual to physical card, you can use the `<ExpDate>` field in the [Convert Card](Using_the_Web_Services_API.htm#_Converting_a_Virtual) web service to set the expiry date.

### 2.3.3 How to use the Card Convert API

For more information, if using SOAP web services, see [Converting a Virtual Card to a Physical Card](Using_the_Web_Services_API.htm#_Converting_a_Virtual); if using the REST Cards API, see [Converting a Virtual Card to a Physical Card.](Using_Cards_API.htm#_Converting_a_Virtual)

Thredd charge a fee for converting virtual cards to physical cards. Refer to your Contract for details.

## 2.4 Summary of Thredd Virtual Card Setup Options

The table below provides a summary of the configuration options for a virtual card product:

| Setup Option | Virtual Only | Virtual converted to Physical | Both Virtual and Physical cards offered |
| --- | --- | --- | --- |
| Thredd Scheme setup | 1 Thredd Scheme | 1 Scheme | 2 Thredd schemes required |
| Product setup | 1 Thredd Product | 1 Thredd Product | 2 Thredd products required if Virtual and Physical cards have different sub-BINs.  If Virtual and Physical cards share the same PANs, then one product is required per currency and country of issue. |
| Card Manufacturer | Not required | Required for the physical card | Required for the physical card |
| Key exchange | Required Required CVV key, optional PGP key if virtual card image is required | Required for the physical card | Required for the physical card |
| Mastercard/Visa Card validation | Not required | Required for the physical card | Required for the physical card |
| PAN | Unique per card | Virtual and physical card have the same PAN. | Unique per card |
| REST-based Cards API | Use Card Create | Use the [Create a Card](Using_Cards_API.htm#_Create_a_Card) API to create the virtual card and the [Convert Card](Using_Cards_API.htm#_Converting_a_Virtual) API to convert to a physical card[3  Cards can be set up to convert with a different PAN if required (not recommended).](#). | Use Card Create |
| SOAP Web Services API | Use Card Create | Use the [Create a Card](Using_the_Web_Services_API.htm#_Create_a_Card)  web service to create the virtual card and the [Convert Card](Using_the_Web_Services_API.htm#_Converting_a_Virtual) web service to convert to a physical card[4  Cards can be set up to convert with a different PAN if required (not recommended).](#). | Use Card Create |
| Card Activation[5  Set via Thredd API on card create or card convert.](#) | On card create | Physical card set to inactive and must be activated on delivery. When activated, the virtual card is upgraded to a physical card, so the virtual card can no longer be used. | Virtual card activated on card create  Physical card activated on delivery. |