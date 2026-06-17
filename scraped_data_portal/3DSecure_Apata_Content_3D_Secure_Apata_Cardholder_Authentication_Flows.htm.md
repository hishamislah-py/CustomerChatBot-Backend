# 3 Cardholder Authentication Flows

This section provides a description of the message flow between parties in a 3D Secure authentication session

## 3.1 Authentication using OTP SMS

Thredd provides One Time Password (OTP) SMS for cardholder authentication. There are two types of OTP SMS authentication:

* Thredd-managed â Thredd sends the generated OTP to the cardholder's mobile on behalf of you, the Program Manager.
* Client-managed â you send the generated OTP directly to the cardholder. This method of OTP SMS authentication is useful if you want to send the OTP through your local SMS provider. This type of OTP authentication is also known as Delegated SMS.

### 3.1.1 Thredd-Managed Authentication

In Thredd-managed authentication for OTP via SMS, Thredd performs a challenge on the credentials of a cardholder, and then receives an OTP from Apata. Thredd then passes the OTP back to the customer, which they enter on their screen. You do not need to play a role in the authentication process.

![](../Resources/Images/Apata/Authentication_flow_OTP_Apata.png)

Figure 2: 3D Secure Authentication Process â Using 3D Secure and OTP

Prior to a cardholder using OTP SMS authentication, you need to set up this method on their card. You add a valid mobile phone number to use for completing the authentication (see [Using the Card Enrolment API](Using_Card_Enrolment_API.htm)).

The steps for Thredd-managed OTP SMS authentication are as follows:

1. The cardholder uses their card at a merchant website.
2. If the merchant is enrolled in 3D Secure, they send a request for authentication to the Card Scheme (Mastercard/Visa).
3. The Card Scheme looks up the 3D Secure service provider for your card programme and sends the authentication request to Apata.
4. Apata checks to confirm the card BIN range is enabled for 3D Secure. Based on the rules you set up in Apata for your card program (see [Appendix 1: Apata 3D Secure Rules](../Reference_Apata/Apata_3D_Secure.htm)), the outcome is Success, Fail/Reject or Challenge, with the next steps as described in the following table:

   | Outcome | What happens next? |
   | --- | --- |
   | Success | An approval response is returned to the merchant. The merchant can continue with the [authorisationClosed Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) request. |
   | Fail or Reject | An *authentication failure* or *reject* response is returned to the merchant. They can decide whether to continue to request transaction authorisation or ask the cardholder to provide an alternative payment method. |
   | Challenge | 3D Secure authentication is required, and Challenge screens are shown to the cardholder. See [Steps for a Challenge outcome](#Steps) below. |

#### Steps for a Challenge outcome

5. Apata connects to Thredd in real-time to check the types of authentication the card is registered for, which is either Biometric, OTP, SMS or KBA).
6. Thredd replies to Apata with OTP SMS as the type of authentication registered on the card (based on what you registered the card for using the [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#)/ [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#) and your product configuration at Thredd).
7. Apata generates the OTP and sends it to Thredd in real-time.
8. Apata displays the OTP entry pop-up screens to the cardholder on the merchant website or App.
9. Thredd sends the OTP to the mobile number Thredd has on record for the cardholder, via SMS.
10. The cardholder enters the OTP in the 3DS pop up screen on the merchant's website or App to complete their authentication.
11. Apata validates the OTP and sends the validation result back to the merchant.

### 3.1.2 Client-Managed Authentication

In a client-managed authentication, you pass the OTP, which Thredd sent to you, directly to the cardholder through SMS. Initially, Thredd would have validated the OTP it received from Apata. Thredd sends the OTP to you through the `DelegateOTPNotification` endpoint.

![](../Resources/Images/Apata/Authentication_flow_delegated_SMS_OTP_Apata.png)

Figure 3: Client-Managed OTP Authentication

You need to have set up the OTP SMS authentication method on the cardholder's card, and added a valid mobile phone number for completing the authentication. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

The steps for client-managed OTP SMS authentication are as follows:

1. The cardholder uses their card at a merchant website.
2. If the merchant is enrolled in 3D Secure, they send a request for authentication to the Card Scheme (Network).
3. The Card Scheme looks up the 3D Secure service provider for your card programme and sends the authentication request to Apata.
4. Apata checks to confirm the card BIN range is enabled for 3D Secure. Based on the rules you set up in Apata for your card program (see [Appendix 1: Apata 3D Secure Rules](../Reference_Apata/Apata_3D_Secure.htm)), the outcome is Success, Fail/Reject or Challenge, with the next steps as described in the following table:

   | Outcome | What happens next? |
   | --- | --- |
   | Success | An approval response is returned to the merchant. The merchant can continue with the [authorisationClosed Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) request. |
   | Fail or Reject | An *authentication failure* or *reject* response is returned to the merchant. They can decide whether to continue to request transaction authorisation or ask the cardholder to provide an alternative payment method. |
   | Challenge | 3D Secure authentication is required, and Challenge screens are shown to the cardholder. See [Steps for a Challenge outcome](#Steps) below. |

#### Steps for a Challenge outcome

5. Apata connects to Thredd in real-time to check the types of authentication the card is registered for, which include Biometric, OTP SMS or KBA).
6. Thredd replies to Apata with OTP SMS as the type of authentication registered on the card (based on what you registered the card for using the [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#)/ [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#) and your product configuration at Thredd).
7. Apata generates the OTP and sends it to Thredd in real-time.
8. Thredd validates the OTP and sends the OTP to you through the `DelegateOTPNotification` endpoint.
9. You send an acknowledgement back to Thredd
10. Thredd sends an OK response to Apata.
11. You send the OTP that you received from Thredd to the cardholder.
12. Apata renders the OTP screen.
13. The cardholder enters the OTP in the 3DS pop up screen on the merchant's website or App to complete their authentication.
14. Apata validates the OTP and sends the validation result back to the merchant.

## 3.2 Authentication using Biometrics or In-App OOB (Out of Band)

This scenario caters to both biometrics or in-app (OOB) for authentication. When a customer uses your (Program Manager)'s app, they utilise their phone's biometric details to authenticate. In OOB, the cardholder performs the transaction from the merchant's site, and uses their own authenticator app for authentication.

![](../Resources/Images/Apata/Authentication_flow_biometric_Apata.png)

Figure 4: 3D Secure Authentication Process â Using 3D Secure and Biometrics or Out of Band (OOB)

#### Authentication via Biometric or In-App OOB

Prior to using this authentication, you need to set up the BIOMETRIC or OUTOFBANDOTHER credential on the card. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

Steps 1-5 are as described previously (see [Authentication using OTP SMS](#_Authentication_using_OTP)).

6. Thredd replies to Apata with Biometric as the type of authentication (based on what you registered the card for using the API and on the default types set up for your cards).
7. Apata calls Thredd to start Biometric or Out of Band authentication.
8. Thredd sends a message to your 3D Secure service endpoint, to start authenticating using Biometrics.
9. Apata shows the Biometric screens to the cardholder. This informs the cardholder that they will need to authenticate using your smart device app.
10. Your organisation sends a push notification to your cardholder and routes them to your bank app.
11. The cardholder authenticates from the bank app (e.g., by scanning their fingerprint or face using their smart device).
12. If the customer is performing the transaction from the merchant's app, the following steps happen:

1. When the authentication session is complete, then you must return the result of the Biometric authentication to Thredd, using the `DelegateSCAValidation` API.
2. If you have received the merchant app redirect URL in the `DelegateSCANotification API` from Thredd, you can call this URL. The URL takes the customer from the banking app back to the merchant app.

13. Thredd waits for your validate response `(DelegateSCAValidation API)` and sends the results back to Apata.
14. Apata returns the results to the merchant.

## 3.3 Authentication using KBA

KBA is usually used in conjunction with OTP SMS or OTP Email (as part of two factor authentication requirements under the PSD2 rules of the European Economic Area).

The following is an overview of the cardholder authentication process during a transaction, using the 3D Secure service with Knowledge Based Authentication (KBA). The communication in this authentication happens mainly between the cardholder, Apata and Thredd.

![](../Resources/Images/Apata/Authentication_flow_KBA_Apata.png)

Figure 5: 3D Secure Authentication Process â Using 3D Secure and KBA

#### Authentication via KBA

Prior to using KBA, you need to set up the KBA credential, including the question and answer pairs to be used for the card during a KBA authentication session. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).

If using multiple questions, you must enrol all cards with a sufficient number of KBA questions to challenge the transaction. This should be the sum of the number of correct and incorrect answers permitted.

An online authentication session using KBA is typically combined with OTP SMS. The KBA authentication follows directly after successful OTP SMS authentication. See [Authentication using OTP](#_Authentication_using_OTP).

1. Apata connects to Thredd in real-time to query the types of authentication the card is registered for (e.g., OTP SMS and KBA).
2. Thredd replies with the OTP and KBA challenge profile configured for your product.
3. Apata follows the process for OTP SMS, presenting the OTP screen to the customer, who enters the OTP which Thredd sends to their mobile phone via SMS.
4. Following OTP authentication, Apata presents an additional screen to the cardholder, asking them to answer the security question(s) set up for their card.
5. The cardholder enters their answer(s).
6. Apata validates the OTP and KBA answers.
7. Apata confirms whether authentication has been successful or not.

## 3.4 What happens after successful authentication?

Once the cardholder is authenticated, the merchant can proceed with requesting [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Process that seeks approval for a payment transaction. The process starts when a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card.](#) for the transaction. (The merchant acquirer includes the 3D Secure value they receive from Apata within the transaction: `UCAF` field (For Mastercard) and the `CAVV` field 126.9 for (Visa).)

If requested, Thredd will validate the [Accountholder Authentication Value (AAV)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Unique 32-character transaction token for a Mastercard 3D Secure transaction. For Mastercard Identity Check, the AAV is named the UCAF.](#) for Mastercard programmes or the [Cardholder Authentication Verification Value (CAVV)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) For Visa Secure transactions, a CAVV is generated by the issuer's (BIN sponsor) Access Control Server (ACS). The CAVV provides evidence that cardholder authentication occurred or that the merchant attempted authentication. A CAVV is unique for each authentication transaction.](#) for Visa programmes. If you need Thredd to validate the CAVV or AAV, then please specify this when [Completing your 3DS Product Setup Form (PSF)](Completing_the_PSF.htm) by selecting YES in the `Do you require Thredd to validate the AAV/CAVV?` field.

Depending on your [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface (EHI) is a Thredd system that enables Thredd clients to receive and respond to real-time transaction data as well as financial messages.](#) mode, Thredd approves/declines the transaction or sends details to your EHI endpoint to approve or decline.

You can view details of your 3D Secure transactions in the Apata Portal. See [Searching for Transactions](../Apata_Portal/Transactions.htm#Configur).