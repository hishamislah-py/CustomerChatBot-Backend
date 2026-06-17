# 2 Parties Involved in 3D Secure

During the 3D secure authentication session, several parties are involved in exchanging data. See the example below:

![](../Resources/Images/Apata/Authentication_parties_Apata.png)

Figure 1: Flowchart of Parties involved 3D Secure

#### Cardholder

The cardholder's card must be enrolled with the relevant credentials (i.e., mobile phone number, email address, KBA questions and answers) to use the required authentication method. Thredd provides an option to auto-enrol the cards in your program, see [Card Auto Enrolment](Enrol_cards_in_3DSecure.htm#_Card_Auto_Enrolment). Alternatively, you can do this using either our SOAP-based [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#) or our REST-based [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#). See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

During the online checkout process, if the transaction does not meet the rules you have configured for [frictionless authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) When a transaction is approved without requiring any manual input from the cardholder.](#), the cardholder is presented with 3D Secure authentication screens[1  For transactions considered low risk, such as for smaller amounts, exemption rules can be configured to accept without additional authentication.](#) . They authenticate based on one of the selected options set up for their card, for example, by entering a one-time password (OTP).

#### Merchant

The merchant must support 3D Secure for an authentication session to occur. The cardholder visits the merchantâs website, and at the checkout stage, when payment is requested, in the background the merchantâs systems initiate a 3D Secure session.

Most merchants use a Payment Gateway, provided by an online payment service provider, to support their payment process. The Payment Gateway handles the connection to the Card Scheme and the 3D Secure authentication request.

#### Card Scheme (Network)

The Card Schemes (Networks such as Mastercard or Visa) receive all payment authentication requests from merchants. The card schemes maintain Directory Servers, with details of the card BIN ranges and the authentication services they are enrolled to. They check the BIN range to determine whether the card is enrolled in the 3D Secure service and the Access Control Server (ACS) used by the issuer (BIN sponsor). The authentication request is then routed to the ACS to complete the authentication.

#### Apata

Apata is Thredd's 3D Secure partner. Apata receives 3D Secure authentication requests from the Card Schemes and check their database for the 3D Secure rules you have configured in the Apata Portal for cards in this BIN range[2  Apata provides an online Admin Portal, where you can set up rules resulting in Accept, Reject or Challenge outcomes, based on parameters such as amount, merchant category, transaction type and country. For details, see Appendix 1: Apata 3D Secure Rules.](#).

If 3D Secure authentication is required, they send a request to Thredd for the types of authentication supported by the card. They provide 3D Secure Authentication screens to the cardholder. See [Configuration of 3D Secure Screens](Configuration_of_Screens.htm).

For OTP email, Apata sends the OTP to the cardholderâs email address.

#### Thredd

Thredd manages the communication with Apata and the Program Manager. During an authentication session, Thredd sends Apata a list of the authentication types for which the card is registered[3  Based on the authentication types you added to the card or, if none are added, on the default option set up in the system for your card product.](#). Apata will use these details to present the available authentication methods to the cardholder in the 3DS pop up screen.

For OTP SMS, Thredd receives the OTP from Apata and sends the OTP to the cardholderâs mobile phone. See [Appendix 2: OTP Message Templates](../Reference_Apata/OTP_Message_Templates.htm#_Appendix_2:_OTP_1).

#### Program Manager

As a Program Manager using Thredd as your Processor, you will need to sign up for the 3D Secure Service with Thredd and set up your 3D Secure rules on the Apata Portal. See [Steps in a 3D Secure Project](Steps_in_a_3D_Secure_project.htm#_Steps_in_a). You should ensure that our cardholders are enroled in the 3D-Secure service.

During the implementation phase, you can customise the 3D Secure Authentication screens displayed to cardholders during the authentication process (i.e., specify the logo and text to be displayed on these screens).

You can use either the Thredd [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#) or [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#) to enrol your cards in the 3D Secure service and request to register in Thredd the authentication types supported by the card. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm#_Using_the_Card_Enrolrement_API). An option is also available for auto-enrolment. See [Card Auto Enrolment](Enrol_cards_in_3DSecure.htm#_Card_Auto_Enrolment).

If you do not enrol the cardholder in to the 3D-Secure service, as the Program Manager, the liability may fall on you rather than the merchant who is set up with 3D-Secure in scenarios where there are chargebacks for the cardholder.