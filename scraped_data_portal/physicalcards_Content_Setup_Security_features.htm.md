# 5 Card Security Features

The following are features relating to the use of physical cards in card-present situations, such as at a Point of Sale (POS) terminal or ATM.

## 5.1 Signature Strip

This legacy feature is still used in some countries (where chip and PIN is not available). When the customer receives their card, they are instructed to immediately sign in the signature strip. The merchant then has the option to do a manual check to verify that the signature provided by the customer at the point of sale matches the one on the back of the card.

## 5.2 Magnetic Strip

When used in store, the cardâs magnetic strip can be swiped by a card reader. The card reader is set up with a connection to the Acquirer, and the data can be passed electronically to the scheme for real-time authorisation.

Swipe cards are still in use, but are considered legacy technology which is less secure[1 The magnetic stripe is considered less secure because it is relatively easy to skim read and clone.](#) . Some card Program Managers are no longer including magnetic strips on new cards[2  For example, Program Managers offering European only card solutions, such as VPay cards. Magstripe is mainly used in the US and is being phased out in Europe. Mastercard plan to stop using the magnetic stripe in Europe in 2024 and in the US by 2027.](#) .

You can optionally set the card usage group to disable magstripe, or alternatively use magstripe as a fallback authentication option only, if no other means of card authentication are available.

## 5.3 Chip Profile

The EMV chip is a microchip embedded on the payment card which stores card data. During an EMV terminal transaction, the chip generates a one-time unique code for each transaction. The chip profile in a card determines where and how the card can be used and how the card will interact with the card reader terminal in-store or at an ATM. Different chip profiles are provided for standard, contactless and dual interface cards.

Below are examples of some of the configuration data set on the chip profile:

* Supported cardholder authentication methods (e.g., support for PIN, signature and none)
* Language, country and currency settings
* Limits and settings to control if transactions can be approved offline
* Transaction types that can be supported (e.g., cash or purchase)
* Channels that will be supported (e.g., POS, ATM)

### 5.3.1 Setting up of Chip profiles

The Issuer (BIN sponsor) chip profiles are set up within the card scheme (payment network). All new chip profiles must go through testing and scheme certification.

An Issuer (BIN sponsor) can decide to support multiple chip profiles and assign a profile that is best suited for a particular portfolio (BIN). Typically, your Issuer (BIN sponsor) will offer a default chip profile for use on your cards. You can submit a change request to change the default chip profile.

In some cases, you may be able to use a previously certified chip, saving time to market. Speak to your card manufacturer about options.

### 5.3.2 Benefits and Options for Chip and PIN

Chip technology protects against card counterfeit fraud (card cloning). Chip & PIN technology helps to prevent fraudulent use of lost and stolen cards. When used in store, the card can be inserted into a card reader. In the majority of transactions, the cardholder needs to enter their card PIN (typically a secret 4-6 digit number known only to them).

Options on the chip determine how the card is authorised. For example: the card could approve or deny the transaction offline, or request online authorisation. For an online transaction, the data is passed electronically in real-time to the payment network for authorisation.

The chip is also used to support contactless payments. Contactless payments are a type of EMV transaction that use Near Field Contact (NFC) technology. NFC enables the payment chip to be read by a nearby card reader using a wireless process.

Chip profile data can be updated remotely when the card is used at a POS terminal or ATM.

### 5.3.3 Card Biometric Authentication

This option enables you to use biometric authentication on the card. During the card present transaction, the cardholder scans their fingerprint (without needing to enter a PIN). The card chip verifies the biometric data and when Thredd receive the transaction authorisation request, we can reset the SCA (Strong Customer Authentication) counters as required by PSD2 (the second Payment Service Directive) rules. For more information on SCA counters, see the [SCA and PSD2 Guide](https://docs.thredd.ai/PSD2_Guide.htm). For information on card data input and card authentication methods recorded in the transaction data, see the [External Host Interface (EHI) Guide > GPS\_POS\_Data Field](https://docs.thredd.ai/ehi/Content/Appendices/GPS_POS_Data.htm).

For more information on support for Card Biometric Authentication, please speak to your Thredd account manager.

#### How does Card Biometric authentication work?

Cards with biometric authentication are manufactured with an embedded fingerprint sensor. When the cardholder wants to make a payment, they place their finger on the sensor embedded in the card. The card's processor then compares the live fingerprint scan to the stored template. Biometric matching is done on the card, without transmitting the fingerprint data to any external systems.

Before the card can be used, the cardholder must first enrol their fingerprint by pressing their finger on the card's sensor, usually during an activation process. The biometric card provides a faster, more secure payment experience compared to entering a PIN, as the fingerprint verification is done with a simple touch. It also meets industry standards for on-card biometric comparison. For more information see [biometricupdate.com](https://www.biometricupdate.com/).

## 5.4 Card Verification Values

When the card is used, there are a number of card verification and security checks that can be performed at the point of sale, to validate that the card is a genuine card:

* **Card Verification Value/Code 1 (CVV1 or CVC1)** â a 3-digit number which is located on the cardâs magnetic stripe tracks 1 and 2. It is used to help prevent fake magnetic stripe transactions, but is vulnerable to copying if someone can see the original magnetic stripe data.
* **Card Verification Value/Code 2 (CVV2 or CVC2)** â a 3-digit number which is located on the card, entered by the customer in an e-commerce transaction.

## 5.5 Holographic Security Image

This is a security design on the card, which makes it difficult for the card to be counterfeited. The hologram reflects light and is three-dimensional. On Visa cards, when the card is tilted back and forth, a dove appears in the hologram and it seems to 'fly'. Mastercard cards have interlocking globes showing the continents with the word 'MasterCard' in the background.