# 3 Cardholder Authentication Flows

This section provides a description of the message flow between parties in an authentication session.

## 3.1 Authentication using Non-Delegated OTP

[Figure 1](#3D3) provides an overview of the cardholder authentication process during a transaction, using the Cardinal 3D Secure service with Non-Delegated One Time Password (OTP) authentication.

![](../Resources/Images/Cardinal/Authentication_flow_OTP.png)

Figure 2: 3D Secure Authentication Process â Using RDX and Non-Delegated OTP

Prior to using OTP, you need to set up the OTP credential on the card. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

1. The cardholder uses their card at a merchant website.
2. If the merchant is enroled in 3D Secure, they send a request for authentication to the Card Scheme (Mastercard/Visa/Discover).
3. The Card Scheme looks up the 3D Secure service provider and sends the authentication request to Cardinal.
4. Cardinal checks to confirm the card BIN range is enabled for 3D Secure. Based on the rules you set up in Cardinal for your card program, the outcome is Success, Fail/Reject or Challenge. (See [Appendix 1: Cardinal 3D Secure Rules](../Reference/Cardinal_3D_Secure.htm))

   1. For a Success outcome, an approval response is returned to the merchant. They can continue with the transaction [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) process.
   2. For a Fail/Reject outcome, an authentication failure/reject response is returned to the merchant. They can decide whether to continue or ask the cardholder to provide an alternative payment method.
   3. For a challenge outcome, 3D Secure authentication is required. See the steps below.

#### Steps for a Challenge outcome

5. Cardinal connects to Thredd in real-time to query the types of authentication the card is registered for (e.g., Biometric, OTP SMS or KBA).
6. Thredd replies to Cardinal with the OTP as the type of authentication registered on the card (based on what you registered the card for using the [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#)/ [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#) and on the default types set up for your cards)[1  Thredd configure the sub-BIN range to a default main authentication method and a fallback method. See Setup Options in Client Information.](#).
7. Cardinal generates the OTP and sends it to Thredd in real-time.
8. Cardinal displays the OTP screens to the cardholder.
9. Thredd sends the OTP to the cardholderâs mobile number.
10. The cardholder enters the OTP to complete their authentication.
11. Cardinal validates the OTP and sends the result back to the merchant.

## 3.2 Authentication using Delegated OTP

[Figure 2](#3D3) provides an overview of the cardholder authentication process during a transaction, using the Cardinal 3D Secure service with Delegated One Time Password (OTP) authentication. For Delegated OTP, you pass the OTP, which Thredd sent to you, directly to the cardholder through SMS. Initially, Thredd would have validated the OTP it received from Cardinal. Thredd sends the OTP to you through the DelegatedOTPNotification endpoint.

![](../Resources/Images/Cardinal/Delegated_OTP.png)

Figure 3: 3D Secure Authentication Process â Using RDX and Delegated OTP

You need to have set up the OTP SMS authentication method on the cardholder's card, and added a valid mobile phone number for completing the authentication.

The steps for client-managed OTP SMS authentication are as follows:

1. The cardholder uses their card at a merchant website.
2. If the merchant is enrolled in 3D Secure, they send a request for authentication to the Card Scheme (Network).
3. The Card Scheme looks up the 3D Secure service provider for your card programme and sends the authentication request to Cardinal.
4. Cardinal checks to confirm the card BIN range is enabled for 3D Secure. Based on the rules you set up in Cardinal for your card program, the outcome is Success, Fail/Reject or Challenge, with the next steps as described in the following table:

   | Outcome | What happens next? |
   | --- | --- |
   | Success | An approval response is returned to the merchant. The merchant can continue with the [authorisationClosed Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) request. |
   | Fail or Reject | An *authentication failure* or *reject* response is returned to the merchant. They can decide whether to continue to request transaction authorisation or ask the cardholder to provide an alternative payment method. |
   | Challenge | 3D Secure authentication is required, and Challenge screens are shown to the cardholder. See [Steps for a Challenge outcome](#Steps) below. |

#### Steps for a Challenge outcome

5. Cardinal connects to Thredd in real-time to check the types of authentication the card is registered for, which include Biometric, OTP SMS or KBA).
6. Thredd replies to Cardinal with OTP SMS as the type of authentication registered on the card (based on what you registered the card for using the [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#)/ [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#) and your product configuration at Thredd).
7. Cardinal generates the OTP and sends it to Thredd in real-time.
8. Send OTP to Program Manager.
9. You send an acknowledgement back to Thredd.
10. Thredd sends an OK response to Cardinal.
11. You send the OTP that you received from Thredd to the cardholder.
12. Cardinal renders the OTP screen.
13. The cardholder enters the OTP in the 3DS pop up screen on the merchant's website or App to complete their authentication.
14. Cardinal validates the OTP and sends the validation result back to the merchant.

## 3.3 Authentication using Biometrics or In-App OOB

[Figure 3](#3D) provides an overview of the cardholder authentication process during a transaction, using the Cardinal 3D Secure service with Biometric authentication.

![](../Resources/Images/Cardinal/Authentication_flow_biometric.png)

Figure 4: 3D Secure Authentication Process â Using RDX and Biometrics

#### Authentication via Biometric or In-App OOB

Prior to using KBA, you need to set up the BIOMETRIC credential on the card. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

Steps 1-5 are as described previously.

6. Thredd replies to Cardinal with Biometric as the type of authentication (based on what you registered the card for using the API and on the default types set up for your cards)[2 Thredd configure the sub-BIN range to a default main authentication method and a fallback method. See Setup Options in Client Information.](#).
7. Cardinal calls Thredd to start the Biometric authentication.
8. Thredd sends a message to your RDX service endpoint, to start authenticating using Biometric. Note that Program Managers must respond to Threddâs `NotifyInitiateAction` API request (200 OK) within 5 seconds as Cardinal is expecting Thredd to respond within 5 seconds. The architecture allows occasional longer running transactions of up to 10 seconds; however, the average response time should be significantly lower.(See [Initiating a Biometric Session)](Using_Biometric_API.htm#_Initiating_a_Biometric)
9. Cardinal shows the Biometric screens to the cardholder. This informs the cardholder that they will need to authenticate using your smart device app.
10. You connect to your cardholder via your Biometric or In-App customer smart device application.
11. The cardholder authenticates using your smart phone app (e.g., by scanning their fingerprint or face using their smart device)
12. When the authentication session is complete, then:

* Your app must return the result of the Biometric authentication to Thredd (validate response using the `NotifyValidate` API).
* Your app should call the merchant's app (using the `MerchantAppRedirectURL` field value obtained from the Thredd `NotifyInitiateAction` API request) to enable the merchant app to redirect the cardholder back to the checkout page.

13. Cardinal sends a validate request to Thredd.
14. Thredd waits for your validate response (`NotifyValidate` API) and sends the results back to Cardinal.
15. Cardinal returns the results to the merchant.

## 3.4 Authentication using KBA

[Figure 4](#3D2) provides an overview of the cardholder authentication process during a transaction, using the Cardinal 3D Secure service with Knowledge Based Authentication (KBA).

![](../Resources/Images/Cardinal/Authentication_flow_KBA.png)

Figure 5: 3D Secure Authentication Process â Using RDX and KBA

#### Authentication via KBA

Prior to using KBA, you need to set up the KBA credential, including the question and answer pair to be used for the card during a KBA authentication session. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

An online authentication session using KBA is typically combined with OTP SMS; the KBA authentication follows directly after the OTP SMS authentication. See [Authentication using OTP](#_Authentication_using_OTP).

1. Cardinal connects to Thredd in real-time to query the types of authentication the card is registered for (e.g., OTP SMS and KBA).
2. Thredd replies to Cardinal with the OTP and KBA authentication types. For KBA, Thredd includes the security question to present to the cardholder.
3. Cardinal follows the process for OTP SMS, presenting the OTP screen to the customer, who enters the OTP which Thredd sends to their mobile phone.
4. Following OTP authentication, Cardinal presents an additional screen to the cardholder, asking them to answer the security question set up for their card.
5. The cardholder enters their answer.
6. Cardinal validates the OTP and sends the OTP validation result to Thredd, together with the KBA answer.
7. Thredd compares the answer returned from Cardinal to the answer stored in the Thredd database[3  When Thredd receives the answer from Cardinal it is immediately encrypted using a hashing algorithm and compared to the hashed answer value stored in the Thredd database.](#). Thredd sends the combined OTP and KBA validation results back to Cardinal.
8. Cardinal returns the results to the merchant.

## 3.5 What happens after authentication?

When the cardholder is authenticated, the merchant can proceed with requesting [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) for the transaction. (The merchant acquirer includes the 3DS secure value they receive from Cardinal within the transaction: `UCAF` field (For Mastercard), the `CAVV` field 126.9 for (Visa), and Field 122 of the authorisation message for Discover/Diners.)

If requested, then Thredd will validate the AAV (Mastercard) or CAVV (Visa). If you need Thredd to validate the CAVV or AAV, then please specify this when [Completing your 3DS Product Setup Form (PSF)](Completing_the_PSF.htm) by selecting YES in the `Do you require Thredd to validate the AAV/CAVV?` field.

Depending on your [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface (EHI) is a Thredd system that enables Thredd clients to receive and respond to real-time transaction data as well as financial messages.](#) mode, Thredd approves/declines the transaction or sends to your EHI endpoint to approve or decline.

You can view details of your 3D Secure transactions in the Cardinal Portal. See [Configuring Rules in Cardinal Portal Production](Complete_production_testing.htm#Configur).