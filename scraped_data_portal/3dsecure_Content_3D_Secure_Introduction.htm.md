# 1 Introduction

3D Secure (Three Domain Structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa, Mastercard and Discover, as well as smaller networks that use the Mastercard Network Exchange (MNE), such as STAR and Pulse. The feature is branded as Visa Secure, Mastercard Identity Check and Discover ProtectBuy respectively.

Thredd use Cardinal Commerce as our 3D Secure service provider. Cardinal provides a real-time 3D Secure enrolment and authentication service called Realtime Data eXchange (RDX). You can implement this service through Thredd to ensure that your cardholders are successfully enrolled and authenticated using 3D Secure.

You can configure the rules which Cardinal use to make a [frictionless authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) When a transaction is approved without requiring any manual input from the cardholder.](#) approval decision, as well as the challenge rules that trigger a request for further authentication.

You can view demos and more information about the authentication process on the Cardinal demo website: [Cardinal Commerce Demo Library](https://www.cardinalcommerce.com/)

The information provided in this document refers to integrating with Cardinal as your 3D Secure provider. If you are integrating with Apata, refer to the [3D Secure (Apata) Guide](https://docs.thredd.ai/3D_Secure_Apata.htm).

## 1.1 Authentication Types

Thredd supports a number of methods or types of authentication that can be used to further verify the cardholder during an online transaction made from a merchantâs website. These authentication types include:

* **Risk based authentication (RBA)**. The authentication decision is done based on Cardinal rules, which generate a risk score that determines whether to approve or decline the transaction. This process is managed by Cardinal.
* **OTP SMS authentication**. Cardinal generates a single-use One-Time Password (OTP). Thredd sends the OTP in a SMS text message to the cardholderâs mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction.
* **Biometric authentication**. Cardinal sends a Biometric authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer smart phone application, via Biometric data, such as a fingerprint scan or face recognition, obtained from the cardholderâs mobile device. Your customer application manages the Biometric verification and returns a response to Thredd.
* **Out of Band (OOB) authentication**. Cardinal sends an authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer [In-App![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Purchase or activity made or available from within a particular app on a mobile device, without the need to visit a separate online site.](#) smart phone application, for example by asking them to enter a username and password. Your customer application manages the verification and returns a response to Thredd.

* **Knowledge Based Authentication (KBA)**. You enrol the card in KBA using the 3D Secure RDX service and provide the security question ID and answer pair. Thredd provides Cardinal with the security question to use for KBA. During the e-commerce authentication session Cardinal asks the cardholder to answer the security question and then sends a KBA authentication request to Thredd together with the cardholderâs answer. Thredd compares the answer returned by Cardinal to the answer stored in the Thredd database and then returns a response to Cardinal. KBA is typically combined with OTP SMS: the cardholder is first asked to authenticate using OTP and then via KBA.

You can add multiple authentication types to each card that you enrol in the 3D Secure RDX service.

#### Two-factor authentication

Biometric, In-App [Out-of-band (OOB)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A type of two-factor authentication that requires a secondary verification method through a separate communication channel. Both Biometric and In-App authentication methods are out of band.](#) authentication and KBA are types of two-factor authentication that requires a secondary verification method through a separate communication channel[1  Since Cardinal provide the primary communication channel (3D Secure screens shown to the user), the authentication session must provide a secondary channel for authentication (e.g., via your Smart device application screens).](#). If Biometrics is being used for authentication, this secondary verification is obtained via Biometric data[2  Behavioural Biometrics (based on analysis of patterns of user activity such as mouse activity, keystroke movement, touch screen behaviour and device movement) is another form of 2-factor authentication, which is in the Thredd/Cardinal development roadmap.](#). If In-App OOB is being used, the secondary verification is obtained via your customer In-App application. If Knowledge-Based Authentication (KBA) is used, secondary verification is obtained via a security question combined with a One Time Password (OTP) to authenticate the cardholder.

Biometric, In-App OOB authentication and KBA are considered to be a form of Strong Customer Authentication (SCA).

#### Strong Customer Authentication (SCA)

Strong Customer Authentication (SCA) requires a combination of two forms of customer identification at checkout. Examples include:

|  |  |  |
| --- | --- | --- |
| **Knowledge: Something they know**  (such as a password or PIN). | **Possession: Something they have**  (such as a mobile phone, card reader or other device evidenced by a One-Time Password). | **Inherence: Something they are**  (such as a fingerprint, face recognition or voice recognition). |

If you are supporting 3D Secure on your cards, you must be able to offer strong customer authentication (SCA) to your cardholders; this is required to comply with the [Second Payment Services Directive (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#) relating to strong consumer authentication (SCA). These regulations apply to cards issued in the European Economic Area (EEA) and the United Kingdom.

SCA has been in place since **March 2022** for UK issued cards, and across most of the EEA from January **1st, 2021**.