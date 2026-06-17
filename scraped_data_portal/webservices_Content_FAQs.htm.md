# General FAQs

This section provides answers to frequently asked questions.

## Web Services

#### What is a WSID and why must it be unique?

Each web service request must include a unique (WSID) or Web service ID. This enables Thredd systems to ensure that all requests are unique and to prevent duplication, for example, if the same request is sent twice or more).

Your systems should always generate a unique WSID. For example, this could be a number based on the current system date and time, as long as it is unique (e.g., in the format YYYYMMDDSS).

#### What happens if the WSID is not unique?

If you try to reuse a previous WSID, this normally results in Thredd returning the following error code: *868 â Duplicate WSID in the request, deny*.

Web service transactions are archived on the Thredd systems after three days. The verification that the WID is unique therefore only extends to web service transactions made during the past three days. This is why it is important to ensure your WSID is always unique.

## Card Manufacturers

#### Which card manufacturers does Thredd support?

For a list of supported manufacturers, see [Card Manufacturers](Reference/Card_Manufacturers.htm).

## Transactions

#### What is the primary key or identifier for a transaction?

`ItemId` is the primary key or identifier for a transaction.

## Virtual and Physical Cards

#### What is the difference between a virtual and physical card?

You can use virtual cards for online transactions only. Conversely, you can use physical cards at Point of Sales terminals and ATMs. The virtual card is available for immediate use in digital format, while the physical card must be printed by a card manufacturer and sent to the cardholder.

#### How does converting a virtual card to a physical card work?

The new physical card is issued with the same card number (PAN) as the virtual card and shares the same card status.

* You can convert to a physical card with the same expiry date as the virtual card. In this case, the CVV is also be the same as the virtual card. There is no difference between the virtual and physical card apart from the virtual-physical difference. If the virtual card is active, the physical card status is also active.
* If the physical card is issued with a new expiry date, then the cardholder is not able to use their new physical card until you use the [Activate Card](Web_services_api/Card_Activate.htm) (`Ws_Activate`) web service to update the expiry date and CVV. In this case, the cardholder is able to continue to use their virtual card while waiting for printing, shipping, and delivery of the printed card. Once delivered, you can update the card record's expiry date and CVV, enabling you to use the card.

## Tokenisation Services

#### Where can I find out more about the Thredd Tokenisation (Digital Wallet) service?

For detailed information on setting up and integrating the Thredd Tokenisation (Digital Wallet) service, see the [Tokenisation Service Guide](https://docs.thredd.ai/Tokenisation_Guide.htm).

#### How can I send an activation code to the cardholder's phone number?

If you want to use the SMS activation code service to send an Activation Code Notification (ACN) to the cardholder, you must include the mobile phone number of the cardholder when creating the card: first use the [Card Create](Web_services_api/Card_Create.htm) web service to create the card and then use the [Card Activate](Web_services_api/Card_Activate.htm) web service to activate the card via SMS.

#### How do I send a confirmation SMS to the cardholder upon successful token activation in Apple Pay?

Thredd can configure your product so that your end customers receive an SMS notification after successfully activating their Apple Pay token. You must ensure that you provide the cardholder's mobile number when creating the card.

Thredd receives a Tokenization Complete Notification (TCN) from Apple Pay if the activation is successful. Thredd does not receive notifications for unsuccessful activations.

#### How can I retrieve the DPAN?

You can use the `ws_Payment_Token_Get` web service to get the DPAN for a card. See [Payment Token Get](Web_services_api/Payment_Token_Get.htm).

The DPAN is returned in the `<Payment_Token >` field as a masked value.

#### Do I need to be PCI compliant to support MDES/VDEP?

Both Apple and Google mandate Push Provisioning, which requires handling the full [PAN![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A payment card number (PAN), primary account number, or simply a card number, is the card identifier found on payment cards, such as credit cards and debit cards, as well as stored-value cards, gift cards and other similar cards.](#). To support MDES/VDEP integration on Android Pay or Apple Pay, you must either be [PCI DSS Compliant![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes (payment networks).
All Program Managers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/](#) or be using Thredd's In-App push provisioning service. For more information, see the [Cards API Website: Introduction to In-App Provisioning](https://cardsapidocs.thredd.com/v2.0/docs/introduction-to-in-app-provisioning).

## 3D Secure

#### Where can I find out more about the Thredd 3D Secure service?

For detailed information on setting up and integrating the Thredd 3D Secure service, see the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) or [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm).

#### How do we enrol cardholders in 3DS?

You can use `Ws_AddUpDelCredentials` to enrol cardholders. See [3D Secure Credentials](Web_services_api/3D_Secure_RDX_Credentials.htm).

The same web service is used to add, update and delete credentials for SMS One Time Password (OTP) and Biometric authentication methods.

The mobile number must be correct (in the format +44 7566789123) to allow the One Time Password to be sent to your cardholder.

#### Which service do you use to provide 3D Secure?

Depending on the region in which you operate, Thredd offers a choice of 3D secure providers. [Cardinal Commerce![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Cardinal Commerce provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme. See: https://www.cardinalcommerce.com](#) manages 3D secure enrolment and authentication. Cardinal provider includes two types of interfaces:

* Real-time Data Exchange (RDX): enables updates in real-time. Thredd use this interface.
* Batch file interface: legacy interface which is updated hourly (at 20 minutes past the hour). Available as a legacy service only.

#### What type of credentials are used to authenticate a 3D Secure transaction?

Thredd's 3D Secure service providers offer the following methods of cardholder authentication:

| Thredd Option | Name | Description |
| --- | --- | --- |
| 1 | RBA | Risk Based Authentication. Cardinal applies a risk score to determine whether to automatically accept or reject the transaction. You can configure the risk scores elements for your programme using Cardinal's Risk Portal (Check with your Account Manager for details of how to access this portal). |
| 2 | OTPSMS | One-time password via SMS. Thredd sends the OTP request to the cardholder's registered phone number when a message from Cardinal is received. The cardholder then enters the OTP to authenticate on the merchant's website. |
| 3 | OTPEMAIL | One-time password via email.  **Note**: OTPEMAIL is only available for 3DS Apata. For more information, see the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm). |
| 4 | BIOMETRIC | Uses some for of user biometric to authenticate, such as a fingerprint or facial recognition on the device. Thredd sends the authentication request to your systems, using the endpoint set up for your Programme. Your systems must handle the authentication. |
| 5 | OUTOFBAND | Managed outside of the Thredd authentication flow, where the cardholder has to authenticate via a key FOB or other token device.  **Note**: OUTOFBAND is currently not available. |
| 6 | CHOICE | This option allows the cardholder to choose their preferred authentication method. Note that this option must be set up in the Thredd system instead of via web services. |
| 7 | KBA | Knowledge-based Authentication. Authentication is based on something only the cardholder knows, for example, the answer to the question '*What was your first pet's name?*') |

For details,refer to the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) or [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm).

#### How are 3D Secure transactions authenticated?

When a cardholder uses their card at the website of a merchant who is enrolled on the 3D Secure scheme, the merchant initiates a 3D authentication call. Thredd's 3D Secure provider (Apata or Cardinal) receives the request. Authentication is handled based on the authentication credential type set up for the card:

* **RBA** â Thredd's 3D Secure provider authorise or decline the transaction based on the risk score settings configured in their portal. The cardholder does not need to enter credentials to authenticate.
* **OTPSMS** â Thredd sends a One-Time Password (OTP) request to the cardholder's registered phone number when we receive a message from Thredd's 3D Secure provider . The cardholder then enters the OTP to authenticate on the merchant's website.
* **BIOMETRIC** â Thredd sends the authentication request to your systems, using the endpoint set up for your Programme. Your systems must handle the authentication.
* **OUTOFBAND** â Thredd sends the authentication request to your systems, using the endpoint set up for your Programme. Your systems must handle the authentication.

OUTOFBAND is currently not available.

* **KBA** â Thredd sends the authentication request to your systems, using the endpoint set up for your Programme. Your systems must handle the authentication.

For details,refer to the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) or [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm).

You can use `Ws_AddUpDelCredentials` to configure the cardholder's authentication credential type. See [3D Secure Credentials](Web_services_api/3D_Secure_RDX_Credentials.htm).

#### We have tried an e-commerce transaction and it was approved without using 3DS, why?

Not all merchants are set up to use 3DS and not all merchants choose to use it for every e-commerce transaction.

#### What happens when a user enters an incorrect OTP? Do they get a set number of retries?

The user is allowed three attempts to enter an OTP, after which the card will be blocked for any online transaction through a merchant enrolled in 3DS.

#### Do OTPs have an expiry time after they are generated? If so, how long are they valid for?

Yes, they are valid until the merchant's site times out for the purchase.

#### Can users request a new OTP to be sent? If so, are there limits, or can we apply limits, per transaction?

Yes, there is an ability to request a new OTP during the online transaction.