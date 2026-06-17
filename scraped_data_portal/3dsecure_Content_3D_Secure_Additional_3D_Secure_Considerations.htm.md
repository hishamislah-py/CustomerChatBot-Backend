# 12 Additional 3D Secure Considerations

This section provides information on other aspects of the 3D Secure service.

## 12.1 Support for 3D Secure Versions

EMV 3D Secure 2.1 and 2.2 are Card Scheme (payment network) versions for Visa/Mastercard and Discover, as well as smaller networks that use the Mastercard Network Exchange (MNE), such as STAR and Pulse. Thredd and Cardinal Commerce support both versions.

Thredd and Cardinal support Mastercard EMV 3DS 2.1 and 2.2.

Thredd and Cardinal are ready with Visa EMV 3DS 2.1 and 2.2

Thredd and Cardinal support ProtectBuy 3DS 2.1 and 2.2

Visa and Mastercard discontinued support for 3DS 1.0 in October 2022. 3DS 2.1 to be discontinued by card networks in September 2024.

See [Appendix 1: Cardinal 3D Secure Rules](../Reference/Cardinal_3D_Secure.htm).

### 12.1.1 3D Secure 2.1

EMV 3DS 2.1 provides SCA compliance and merchant fraud liability protection. It provides support for the following features:

* Smart devices and a better customer experience.
* Enables merchants to send additional information to the issuer (BIN sponsor).
* Supports the use of dynamic authentication through Biometrics and In-app authentication methods.
* Supports issuer (BIN sponsor) exemptions through risk-based authentication ( e.g. Frictionless Flow).
* Can be used to set up merchant-initiated transactions, such as for recurring payments; the first payment requires SCA while subsequent payments can be set up as merchant-initiated transactions without requiring SCA.

### 12.1.2 3D Secure 2.2

EMV 3DS 2.2 includes all the features of 2.1, plus:

* Supports SCA exemption flags - to enable more control over SCA decisions and customer experience.
* Offers a new 3RI channel for non-payment authentication.
* Allows merchants to request SCA exemptions through their Acquirer.

For more information on EMV 3DS 2.1 and 2.2, see the [Cardinal Commerce Website > EMVÂ® 3-D Secure v2.1 vs v2.2: What issuers need to know](https://www.cardinalcommerce.com/content-hub/industry-news/emv-3d-secure-v21-vs-v22).

## 12.2 Supported Authentication Types

Refer to the table below for details of the authentication types which Thredd supports. The `<Type>` value is the name as used in the 3D Secure Thredd API / Cards API) and as described below:

| Type | Description |
| --- | --- |
| RBA | Risk-Based authentication (done via Cardinal). The authentication decision is done based on the Cardinal ruleâs engine, which generate a risk score, based on factors such as country, IP address, merchant category, transaction type and amount.    **Note**: Cardinal automatically enrols your cards in this service. You do not need to do this via Thredd API or the Cards API. |
| OTPSMS | OTP SMS authentication.  Cardinal generates a single-use One-Time Password (OTP). Thredd sends the OTP in a SMS text message to the cardholderâs mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate. |
| BIOMETRIC | Biometric authentication. Cardinal sends a Biometric authentication request to Thredd and we forward this to your systems.  You need to verify the cardholder using your customer smart phone application, via Biometric data, such as a fingerprint scan, obtained from the cardholderâs mobile device. Your customer application manages the Biometric verification and returns a response to Thredd. |
| OUTOFBAND | In-App authentication. Cardinal sends the Out Of Band (OOB) authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer smart phone application, for example by asking the user to enter a username and password. Your customer application manages the verification and returns a response to Thredd. |
| KBA | The cardholder is asked to verify their identity by providing the answer to a question such as âWhat is your motherâs maiden name?â or âWhat is the name of your favourite pet?  KBA is combined with OTP SMS, to meet the two-factor requirement for Strong Customer Authentication (SCA). |