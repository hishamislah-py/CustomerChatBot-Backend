# 1 Introduction

3D Secure (Three Domain Structure), also known as a cardholder authentication, is a security protocol that helps to prevent fraud in online (e-commerce) credit and debit card transactions. This security feature is supported by Visaand Mastercard, as well as smaller networks that use the Mastercard Network Exchange (MNE), such as STAR and Pulse. The feature is branded as Visa Secureand Mastercard Identity Check.

Thredd's 3D Secure partner is Apata. You can implement this service through Thredd to ensure that your cardholders are successfully enrolled and authenticated using 3D Secure.

## 1.1 About Apata

Apata is an Access Control Server (ACS) provider.

The ACS is responsible for verifying the identity of the cardholder during a 3D Secure transaction. When a merchant initiates a 3D Secure transaction, the card scheme (Mastercard or Visa) sends the transaction details to the ACS of the card issuer (BIN sponsor). The ACS then interacts with the cardholder, usually through a pop-up window, to request additional authentication information, such as a one-time passcode or biometric authentication. If the authentication is successful, the ACS (Apata) sends a response back to the merchant indicating that the transaction is successfully authenticated and can proceed to authorisation.

You can configure the rules which Apata use to make a [frictionless authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) When a transaction is approved without requiring any manual input from the cardholder.](#) approval decision, as well as the challenge rules that trigger a request for further authentication and rules that result in rejection of a transaction.

The information provided in this document refers to integrating with Apata as your 3D Secure provider. If you are integrating with Cardinal, refer to the [3D Secure (Cardinal) Guide](https://docs.thredd.ai/3D_Secure_RDX.htm).

## 1.2 Apata Features

* Authentication flows for One time Passcode (OTP), Knowledge Based Authentication (KBA), Biometric/Out of Band (OOB) authentication, Transaction History and Behavioural biometrics.
* Acquirer transaction risk analysis
* User Portal
* Dynamic linking (matching authentication to authorisation)
* Public token support to identify transaction
* Merchant trust listing â cardholder opt-in to be trusted by this merchant, so not to be challenged by this merchant
* Self-debugging
* Experimentation (A/B testing flows)

## 1.3 Authentication Methods

Thredd supports a number of authentication methods that can be used to further verify the cardholder during an online (e-commerce) card transaction made from a merchantâs website:

| Authentication Method | Description |
| --- | --- |
| **Risk based authentication (RBA)** | Risk profiles define how a transaction is evaluated once it reaches Apata. These are a combination of rules which determine the processing action (challenge, accept or reject) which should be taken based on the individual characteristics of a transaction. |
| **OTP SMS authentication** | Apata generates a single-use One-Time Passcode (OTP). Thredd sends the OTP in a SMS text message to the cardholderâs mobile phone number, and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction.  For OTP SMS authentication, Thredd offer both Thredd-managed and client-managed OTP SMS authentication. Client-managed OTP SMS authentication allows you to use a local SMS provider and send the OTP directly to the cardholder. This type of authentication is also known as *delegated SMS*. |
| **OTP Email authentication** | Apata generates a single-use One-Time Passcode (OTP). Apata sends the OTP in an email message to the cardholderâs email address and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction. |
| **Biometric authentication** | Apata sends a Biometric authentication request to Thredd and we forward this to your systems. Your cardholders will need to verify themselves with a biometric identifier (e.g., fingerprint, voiceprint, facial scan) within an authenticator app, for example your organisation's mobile banking application. Your application manages the Biometric verification and returns a response to Thredd. |
| **Out of Band (OOB) authentication** | Apata sends an authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your cardholder [In-AppClosed Purchase or activity made or available from within a particular app on a mobile device, without the need to visit a separate online site.](#) smart phone application, for example by asking them to enter a username and password. Your cardholder application manages the verification and returns a response to Thredd. |
| **Knowledge Based Authentication (KBA)** | You enrol the cardholder in KBA using the 3D Secure service and provide the security question ID(s) and answer pair(s). Thredd provides Apata with the security question and answer to use for KBA. During the e-commerce authentication session, Apata asks the cardholder to answer the security question and validates the answers. KBA is typically combined with OTP to satisfy the two-factor authentication requirement for PSD2 SCA compliance. |
| Transaction history | Another type of Knowledge based authentication. If the card is configured to use transaction history, the cardholder is asked to identify a recent payment they made with their card. (Transaction history details are taken from previous transactions where 3D Secure authentication was requested.) |

You can add multiple authentication types to each card that you enrol in the 3D Secure service.

Strong Customer Authentication (SCA) rules under the Second Payment Services Directive (PSD2) in the EU/EEA and similar regulations may not permit certain authentications on their own (e.g., OTP SMS, OTP Email or KBA). See below.

#### Strong Customer Authentication (SCA)

Strong Customer Authentication (SCA) requires a combination of two forms of customer identification at checkout. Examples include:

|  |  |  |
| --- | --- | --- |
| **Knowledge: Something they know**  (such as a password or PIN). | **Possession: Something they have**  (such as a mobile phone, card reader or other device evidenced by a One-Time Passcode). | **Inherence: Something they are**  (such as a fingerprint, face recognition or voice recognition). |

If you are supporting 3D Secure on your cards, you must be able to offer SCA to your cardholders; this is required to comply with the [Second Payment Services Directive (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#) relating to Strong Customer Authentication (SCA). These regulations apply to cards issued in the European Economic Area (EEA) and the United Kingdom.