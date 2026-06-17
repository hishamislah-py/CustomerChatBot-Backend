# 2 How Tokenisation Works

## 2.1 Who Participates in Tokenisation?

Tokenisation requires the following participants:

#### Cardholder

The cardholder enrols with a mobile wallet provider or registers at an online merchant website.

#### Token Requestor

The token requestor initiates the request to convert your cardholderâs [Permanent Account Number (PAN)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The cardâs 16-digit primary account number (PAN) that is typically embossed on a physical card.](#) into a digital token. Token requestors can be mobile wallets (such as ApplePay) or online merchants (such as Netflix). Mastercard refer to the Token Requestor as the âWallet Providerâ.

#### Token Service Provider (TSP)

The Token Service Provider is the party that generates the token and securely maps the PAN to a token. This is the Visa ([VDEP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Visa Digital Enablement Programme. Also called the Visa Tokenisation Service (VTS).](#)) or Mastercard ([MDES![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The MasterCard Digital Enablement Service (MDES) is a data interchange platform for generating and managing secure digital payment tokens. It enables devices such as smartphones, smart watches, as well as merchants, to create a tokenised version of a Mastercard, which is specific to that device or merchant. Then the device/merchant can use the tokenised version of the card to perform transactions. The tokenised version of the card appears as just a normal Mastercard card number to the merchant and acquirer, and Mastercard will map the transactions onto the original cardholder Mastercard.](#)) systems that run the token service.

#### Issuer Host

The issuer host is Thredd, who receives the tokenisation request from Visa or Mastercard and decides on whether to approve or decline. During the implementation phase of the project, the issuer/Program Manager and Thredd work together to set up and create the token service.

![](../Resources/Images/Token_participants.png "Participants in the tokenisation process")

Figure 2: Participants in the Tokenisation Ecosystem

The Token Service Provider (Visa/Mastercard) receives token requests from the Token Requestor and sends them to Thredd for authorisation. There is no direct connection between Thredd and the Token Requestor during tokenisation and Thredd does not have the capability to act as a Token Requestor.

When using mobile wallet token requestors (such as Apple and Android), the [Program Manager![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) (Thredd customer) requires a separate commercial agreement with each of the three parties involved in tokenisation.

For online merchant tokenisation (i.e., for online payments), the card issuer does not need to have an existing relationship with the merchant.

## 2.2 Token Provisioning

Token provisioning is the act of creating and activating a digital token. The digital token is sometimes referred to as the [DPAN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Device PAN. The PAN value set up on the cardholderâs device. This is not visible to the cardholder, but is the PAN used for the transactions as far as the merchant is concerned.](#), and is the same length as a normal 16-digit card financial PAN ([FPAN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Funding PAN. The true 16-digit PAN of the card, which Mastercard/Visa converts when authorisations come through to them from Acquirers on the DPAN.](#)).

This process must be completed first before the token can be used in transactions.

### 2.2.1 Token Provisioning Steps

Figure 3 provides a high-level overview of the token provisioning flow.

![](../Resources/Images/Token_Provisioning_Flow_without_Authentication.png "Token provisioning flow without authenticate")

Figure 3: Token Provisioning Flow without Authentication

1. The cardholder enrols their card with a token requestor (either an online merchant or a mobile Wallet provider).
2. The token requestor requests a new token from the token service provider (Visa/Mastercard).
3. The token service provider creates the payment token (DPAN), containing [EMV![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMV is a payment standard for smart payment cards, payment terminals and automated teller machines (ATMs). EMV is an acronym for "Europay, Mastercard, and Visa", the three companies which created the standard.](#) and other card data, to replace the cardholderâs FPAN.   
   The token service provider sends a [Token Activation Request (TAR)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Tokenisation Authorisation Request messages enable the issuer to provide a real-time decision as to whether the token service provider (MDES/VDEP) can digitise a card and designate a token on their behalf.](#) to the issuer host (Thredd).
4. Thredd decides if token activation can continue, based on the [Thredd Configuration Options](../Implementation/Tokenisation_Configuration.htm#_GPS_Configuration_Options) set up for your programme. (See [Token Authorisation Options](#_Token_Authorisation_Options) below.)
5. With Thredd approval the token service provider (Visa/Mastercard) activates the new payment token and sends the newly created token to the token requestor.
6. For an Online Merchant payment token, the token is stored for use on their website. For a Mobile Wallet payment token, it is installed on the phone for mobile [Near Field Communication (NFC)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Near Field Communication (NFC) is a technology that enables a device, such as a mobile phone or payment ring, to transmit data to a Point of Sale (POS) terminal, enabling contactless payments.](#) use.

### 2.2.2 Token Authorisation Options

When Thredd returns a decision on the token request there are three options:

* Approve â token is active for use
* Approve with Authentication â additional authentication is required before the approved token can be used
* Decline â token is not approved.

The Thredd response code in the response triggers three different provisioning flows:

| Thredd Response | Response Code | Provisioning Flow (Token Terminology) |
| --- | --- | --- |
| Approve | 00 | Green Flow |
| Approve with Authentication | 85 | Yellow Flow |
| Decline | 05 | Red Flow |

Each of these provisioning flows is described below.

### 2.2.3 Approve (Green Flow)

When Thredd receives the token activation request (TAR) and we approve, if cardholder authentication is not required, Thredd sends an approve message to the token service provider to create the token without further authentication[1  Note that in some circumstances it possible for a Program Manager or issuer to set up rules on Mastercard or Visa to ignore or overrule the Thredd response to a TAR. Please contact the card schemes for details.](#).

Cardholder authentication is not required in the following circumstances:

* Authentication has already been performed (i.e., token is being push-provisioned; see [Push Provisioning](#_Push_Provisioning))
* For an online merchant
* Based on the configuration for your Wallet Usage Group; see [Payment Token Usage Groups](../Implementation/Tokenisation_Configuration.htm#_Payment_Token_Usage)

Your Thredd Wallet Usage Group configuration is used to determine the appropriate flow to trigger[2  Your Wallet Usage Group can be viewed in Smart Client. If the token requestor is ApplePay, they populate the request with a score (Wallet device score and Wallet account score), which can be used to determine if further cardholder authentication is required. See Thredd Configuration Options.](#). Most Thredd Program Managers implement the approve with authentication flow.

### 2.2.4 Approve with Authentication (Yellow Flow)

When Thredd receives the token activation request (TAR) and we approve, if cardholder authentication is required, we send an approve with authentication message to the token service provider to create the token with cardholder authentication.

Cardholder authentication is only needed by mobile wallet token requestors (such as Apple and Android), where the cardholder is present at the time the card is being tokenised.

To authenticate a cardholder during token provisioning, the cardholder is provided with a One-Time Password (OTP) generated by the token service provider (Visa/Mastercard). The cardholder enters the OTP value into their mobile app for validation.

The Program Manager decides what delivery options are available to the cardholder for the OTP. These options can include:

* SMS text message to mobile phone
* Push notification/in-app notification
* Email
* Call centre (an operator reads out the passcode to the cardholder to enter; the passcode is available on [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your account on the Thredd Platform.](#), via Thredd Web Services or the Thredd[External Host Interface (EHI)](../Implementation/Tokenisation_Configuration.htm#_External_host_interface) and will expire after a limited period, such as 2 hours).

Thredd currently only sends the OTP via SMS text message directly to the cardholderâs mobile phone. For all other OTP methods, you will need to deliver the OTP to the cardholder. The OTP is always sent via EHI, even if Thredd also sends an SMS direct to the cardholder. The OTP can be viewed in Smart Client or retrieved via Web services.

Figure 4 below describes the Approve with Authentication (Yellow) flow.

![](../Resources/Images/Cardholder_Authentication_During_Token_Provisioning.png)

Figure 4: Cardholder Authentication During Token Provisioning

This flow commences after the token has been generated, but further user authentication is required before it can be used:

1. Thredd sends an 85 (approve with authentication) response to the token service provider (Visa/Mastercard). The response contains a list of cardholder verification methods (CVMs), based on the configuration of your Wallet Usage Group for your cards.
2. The token service provider sends a list of available cardholder verification methods to the cardholder.
3. The cardholder selects one of the verification methods shown on their mobile phone wallet application.
4. The Token Service Provider receives the method selection and sends the one-time password (OTP) to Thredd.
5. Thredd always sends the OTP over the External Host Interface (EHI) to the Program Manager.
6. If the cardholder selected the SMS option and you have requested that Thredd send the message on your behalf, then Thredd sends the OTP to the cardholder via SMS.   
   For other cardholder verification methods or where you have opted to send the SMS, the cardholder receives the OTP from your systems[3  You must provide Thredd with the SMS text message to send to the customer. This message can contain dynamic fields. For details, check with your Implementation Manager. Thredd always sends the SMS to the phone number linked to the card on our systems (note that this may not be the same as the device which is being tokenised).](#).
7. The cardholder enters the OTP on their mobile device.
8. The token service provider validates the OTP.

Figure 4 above has been simplified to show the overall process. Token provisioning with authentication requires several messages between the card schemes (networks) that are a mixture of BASE I (ISO 8583) messages (for Visa and Mastercard) and APIs (for Visa only).

### 2.2.5 Decline (Red Flow)

When Thredd receives the token activation request (TAR) and we decline, we send a decline message to the Token Service Provider. This ends the token flow. The token requestor must request a new token.

### 2.2.6 Orange Flow

Orange Flow is for token requests from Apple that indicate if the request is high risk. Apple mandate that these requests must be authenticated using secure authentication methods or be declined. The Secure authentication methods are:

* In-App authentication where the application is tenured
* A call centre where additional fraud analysis is performed

Orange Flow is set up during implementation, where you select the options on the PSF. Contact Implementations to discuss the best option for you.

In the event of a provisioning request being marked as Orange Flow, Thredd will return any of the above authentication methods that you have configured on the Payment Token Usage Wallet.

In-App authentication cannot be returned if the provisioning requests started as In-App push provisioning. This is an Apple rule designed to stop a fraudulent actor with access to your app using it to start the flow and then authenticate themselves through the same channel.

Customers can choose to support secure authentication methods or to decline all requests flagged as Orange Flow. Apple recommend supporting secure authentication methods, however if you are not able to do this we have kept the possibility of declining all requests (In this scenario speak to Apple about getting your use case approved).

## 2.3 In-App Push Provisioning

In-App Push Provisioning enables a cardholder to request a token for their device directly from the Programme Manager's mobile app, removing the need to manually enter the PAN details into the mobile wallet Token Requestor's app.

The cardholder must be logged into their account on their Programme Manager mobile app to be able to authenticate.

Since it originates from inside the mobile app, the Program Manager can pre-authenticate the cardholder through entry to their mobile app before a request for a token is sent to the Token Service Provider (Such as Visa or Mastercard). For information on the requirements for authenticating a cardholder during push provisioning, discuss with your mobile wallet Token Requestor.

Push provisioning requires you to share sensitive card data with the Token Service Provider using the mobile wallet Token Requestor. This data needs to be encrypted to standards of both the Token Service Provider and the mobile wallet Token Requestor. Thredd's role is to provide an encrypted payload that can be returned to your mobile app and passed into the relevant mobile wallet app.

Thredd provides an integrated solution through our In-App Provisioning endpoints to ensure that non [PCI Compliance![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major card schemes. All Program Managers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/](#) Level 1 customers can retrieve the PAN from the Thredd platform.

This integration enables you to retrieve the PAN and CVV from the Thredd platform. The data is encrypted and sent to the cardholderâs mobile phone application to pass to the token requestor and then to the token service provider (Visa/Mastercard).

Thredd's In-App Provisioning solution is also available to customers that are PCI compliant. Contact your Implementations Manager to ask about using this.

Figure 5 below describes the In-App Provisioning process.

![](../Resources/Images/In-App_Push_Provisioning.png)

Figure 5: Integration for In-App Provisioning

1. The cardholder confirms the card to be added to their mobile phone application for your service.
2. Your mobile phone app requests encrypted card data for In-App Provisioning from the token requestor (e.g., Apple or Android).
3. The token requestor returns the data.
4. Your mobile app sends data to your server.
5. Using a valid REST API authorisation token, your server calls either the Thredd Apple, Google Wallet, or Samsung Pay endpoint.
6. Thredd creates an encrypted payload and returns it to your server.
7. The server sends the encrypted data to the mobile phone app.
8. The encrypted data is passed to the token requestor from the phone app.
9. The token requestor initiates provisioning with the Token Service Provider, which decrypts the card data and starts the [token provisioning flow](#_Token_Provisioning_Flow).

## 2.4 Token Requestors

The token requestor initiates the request to convert your cardholderâs PAN into a token. There are two types of token requestors:

* Mobile Wallet Token Requestors â such as Apple and Android, who provide a token service via a smartphone or other mobile device that enables the cardholder to use their device for point of sale (POS) transactions
* Online Merchant Token Requestors â who tokenise a payment card for use in repeat or recurring payments on their website (such as Netflix, Dominoâs and PayPal). These are referred to by Card on File (COF) Token Requestors[4  Card on File (COF) is also referred to by Mastercard as MDES for Merchants.](#).

As a Thredd customer, most of your implementation in a tokenisation service project will be focused on the Mobile Wallet Token Requestors, with whom you need to integrate directly.

You will also need to enable online merchant Token Requestors. You do not require a pre-existing relationship with the merchant. Since merchants replace the live PAN with a token, you do not need to store the PAN. The merchant sends only the token to the Token Service Provider who maps it back to the real PAN before sending to Thredd. This is done to improve card data security.

## 2.5 Visa Cloud Token Framework â Online Merchant Device Binding

Mandatory for Visa only. Not applicable to Mastercard.

In October 2020, Visa launched the Visa Cloud Token Framework (CTF). This product is a precursor to supporting the [EMVCo![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Organisation that facilitates worldwide interoperability and acceptance of secure payment transactions. Created by EuroPay, Mastercard and Visa.](#) Secure Remote Commerce (SRC) functionality[5  Precursor to Visa Secure EMVCo data.](#) . SRC aims to introduce a common e-checkout experience that cardholders will trust, called Click to Pay.

CTF allows online Merchant Token Requestors to bind their previously created [Card On File (COF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card on File token request created by an online merchant.](#) tokens with devices which they can authenticate belongs to their customer. The device binding process allows merchants to directly authenticate that the cardholder owns the device they are paying from.

#### How does it work?

The Online Merchant Token Requestors creates a [COF token![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card on File token request created by an online merchant.](#) through the standard [Token Provisioning flow](#_Token_Provisioning_Flow) (Green flow, without Authentication).

The token can then be bound to a device if the Online Merchant Requestor sends a follow up request to do so. During binding, the Online Merchant Token Requestors usually requires cardholder authentication, by sending an OTP to the cardholder.  This cannot be done by in-app notification through an app (this is against the Visa rules and OTP standard).  Methods such as SMS are still valid.

When Thredd approves a device binding, the merchant can initiate authentication of the device at any stage. This means you may receive OTP messages (Activation Code Notifications) at any time over EHI and not just immediately following a TAR or Device Binding Request. These OTP messages must be sent to the cardholder. If configured, Thredd sends these via SMS on your behalf.

### 2.5.1 Binding an existing COF Token to a Device

Note that this is relevant to Visa only.

![](../Resources/Images/Device_Binding_Flow.png)

Figure 6: Device Binding Flow

1. The cardholder makes a purchase on their device.
2. The merchant identifies a new device on an existing Card on File ([COF![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card on File token request created by an online merchant.](#)) token.
3. The merchant submits a device binding request.
4. The Token Service Provider (Visa/Mastercard) forwards the device binding request to Thredd.
5. Thredd provides a decision on the device binding request: Approve or Decline.
6. With approval, the merchant records the device binding for future purchases.

Cardholder authentication is not required in the following circumstances:

* Authentication has already been performed (i.e., token is being push-provisioned; see [Push Provisioning](#_Push_Provisioning))
* For an online merchant
* Based on the configuration for your Wallet Usage Group; see [Payment Token Usage Groups](../Implementation/Tokenisation_Configuration.htm#_Payment_Token_Usage)

Your Thredd Wallet Usage Group configuration is used to determine the appropriate flow to trigger[6  Your Wallet Usage Group can be viewed in Smart Client. If the token requestor is ApplePay, they populate the request with a score (Wallet device score and Wallet account score), which can be used to determine if further cardholder authentication is required. See Thredd Configuration Options.](#). Most Thredd Program Managers implement the approve with authentication flow.

## 2.6 Token Requestors

The token requestor initiates the request to convert your cardholderâs PAN into a token. There are two types of token requestors:

* Mobile Wallet Token Requestors â such as Apple and Android, who provide a token service via a smartphone or other mobile device that enables the cardholder to use their device for point of sale (POS) transactions
* Online Merchant Token Requestors â who tokenise a payment card so that the token can be used for repeat payments or recurring payments on their website (e.g., such as Netflix, Dominoâs and PayPal). These are referred to by Card on File (COF) Token Requestors[7  Card on File (COF) is also referred to by Mastercard as MDES for Merchants.](#).

As a Thredd customer, most of your implementation in a tokenisation service project will be focused on the Mobile Wallet Token Requestors, with whom you need to integrate directly.

You will also need to enable online merchant Token Requestors. You do not require a pre-existing relationship with the merchant. Since merchants replace the live PAN with a token, you do not need to store the PAN. The merchant sends only the token to the Token Service Provider who maps it back to the real PAN before sending to Thredd. This is done to improve card data security.

## 2.7 Visa Cloud Token Framework â Online Merchant Device Binding

Mandatory for Visa only. Not applicable to Mastercard.

The device binding process allows merchants to directly authenticate that the cardholder owns the device they are paying from. The Online Merchant Token Requestor creates a [COF token![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card on File token request created by an online merchant.](#) through the standard [Token Provisioning flow](#_Token_Provisioning_Flow), which can then be bound to a device. During binding, the Online Merchant Token Requestor usually requires cardholder authentication, by sending an OTP to the cardholder. This cannot be done by push notification through an app (this is against the Visa rules and OTP standard).  Methods such as SMS are still valid.

When Thredd approves a device binding, the merchant can initiate authentication of the device at any stage. This means you may receive OTP messages (Activation Code Notifications) at any time over EHI and not just immediately following a TAR or Device Binding Request. These OTP messages must be sent to the cardholder. If configured, Thredd sends these via SMS on your behalf.

### 2.7.1 Binding an existing COF Token to a Device

Note that this is relevant to Visa only.

![](../Resources/Images/Device_Binding_Flow.png)

Figure 7: Device Binding Flow

1. The cardholder makes a purchase on their device.
2. The merchant identifies a new device on an existing Card on File ([COF![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card on File token request created by an online merchant.](#)) token.
3. The merchant submits a device binding request.
4. The Token Service Provider (Visa/Mastercard) forwards the device binding request to Thredd.
5. Thredd provides a decision on the device binding request: Approve or Decline.
6. With approval, the merchant records the device binding for future purchases.