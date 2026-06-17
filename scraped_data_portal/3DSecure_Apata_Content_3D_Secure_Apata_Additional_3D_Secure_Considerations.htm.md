# 12 Additional 3D Secure Considerations

This section provides information on other aspects of the 3D Secure service.

## 12.1 Support for 3D Secure Versions

EMV 3D Secure 2.1 and 2.2 are Card Scheme (Visa/MasterCard) versions. Thredd and Apata Commerce support both versions.

Thredd and Apata support Mastercard EMV 3DS 2.1 and 2.2.

Thredd and Apata support Visa EMV 3DS 2.1 & 2.2

Visa and Mastercard discontinued support for 3DS 1.0 in October 2022.

We are awaiting finalised roll-out details of 2.3 from [EMVCo![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMVCo is a technical body which manages and evolves EMV Specifications and supporting programmes that enable card-based payment products to work together seamlessly and securely worldwide.](#). See the [EMVCo website > Enhancing the 3D Secure Specifications](https://www.emvco.com/knowledge-hub/enhancing-the-emv-3-d-secure-specifications/).

See [Appendix 1: Apata 3D Secure Rules](../Reference_Apata/Apata_3D_Secure.htm).

### 12.1.1 3D Secure 2.1

EMV 3DS 2.1 provides SCA compliance and merchant fraud liability protection. It provides support for the following features:

* Smart devices and a better customer experience.
* Enables merchants to send additional information to the issuer (BIN sponsor).
* Supports the use of dynamic authentication through Biometrics and In-app authentication methods.
* Supports issuer (BIN sponsor) exemptions through risk-based authentication ( e.g. Frictionless Flow).
* Can be used to set up merchant-initiated transactions, such as for recurring payments; the first payment requires SCA while subsequent payments can be set up as merchant-initiated transactions without requiring SCA.

### 12.1.2 3D Secure 2.2

EMV 3DS 2.2 includes all the features of 2.1, plus:

* Supports SCA exemption flags â to enable more control over SCA decisions and customer experience.
* Offers a new 3RI channel for non-payment authentication.
* Allows merchants to request SCA exemptions through their Acquirer.

For more information on EMV 3DS 2.1 and 2.2, see [EMVÂ® 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/).

## 12.2 Supported Authentication Types

Refer to the table below for details of the authentication types which Thredd supports. The `<Type>` value is the name as used in the 3D Secure web service / Cards API) and as described below:

| Type | Description |
| --- | --- |
| OTPSMS | OTP SMS authentication.  Apata generates a single-use One-Time Password (OTP). Thredd sends the OTP in a SMS text message to the cardholderâs mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate. |
| OTPEMAIL | OTP email authentication.  Apata generates a single-use One-Time Passcode (OTP). Apata sends the OTP in an email message (from the email address specified by your organisation) to the cardholderâs email address and the cardholder enters the OTP in the 3D Secure screen to authenticate. |
| KBA | The cardholder is asked to verify their identity by providing the answer to a question such as âWhat was the make of your first car?â or âWhat is the name of your first pet?  In the EU/EEA, KBA is combined with OTP SMS, to meet the two-factor requirement for Strong Customer Authentication (SCA). |
| BIOMETRIC | Biometric authentication. Apata sends a Biometric authentication request to Thredd and we forward this to your systems.  You need to verify the cardholder using your customer smart phone application, via Biometric data, such as a fingerprint scan, obtained from the cardholderâs mobile device. Your customer application manages the Biometric verification and returns a response to Thredd. |
| OUTOFBAND | In-App authentication. Apata sends the Out Of Band (OOB) authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer smart phone application, for example by asking the user to enter a username and password. Your customer application manages the verification and returns a response to Thredd. |

### 12.2.1 Other Types of authentication

For the services listed below, no card enrolment is required via Thredd web services or Cards API. These services will be available to any card that has been enrolled in 3D secure.

| Type | Description |
| --- | --- |
| RBA | Risk-Based authentication (done via Apata). Also referred to as TRA (Transaction Risk Analysis). The authentication decision (i.e., accept, reject, or challenge) is determined by the risk rules configured by the issuer (BIN sponsor). In Apata, there are a wide range of data points available to create authentication rules and risk profiles. These define how the transaction is evaluated once it reaches Apata. |
| Transaction History | During the authentication process, the cardholder is asked to identify a recent payment they made with their card. Transactions history details are taken from previous transactions where 3D Secure authentication was requested.  Please specify if you will require this authentication method when completing the 3DS Product Setup Form. |