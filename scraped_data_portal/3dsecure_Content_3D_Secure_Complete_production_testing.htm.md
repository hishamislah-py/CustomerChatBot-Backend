# 10 Completing Pilot Production Testing

Thredd and Cardinal set up your cards in the Production environment:

* Thredd activates a single card product in the Production environment, so you can enrol a few cards for the production pilot testing.
* You provide Cardinal with your pilot cards to be enroled at the Scheme.
* Cardinal contacts the Scheme to set your pilot cards live with 3DS Cardinal.

## 10.1 Configuring Rules in Cardinal Portal Production

You can configure your rules in the live Cardinal Portal at:

<https://identifiportal.cardinalcommerce.com/home/dashboard>

You must access this link from a trust-listed IP address (as you provided on the 3D Secure PSF).

You can register the cards for the supported 3D Secure authentication types: if using the Thredd API, then use the 3D Secure RDX web service (`Ws_AddUpDelCredentials`; if using Cards API, then use the `Create 3DS Credentials` API.

Once your pilot cards are live with 3DS, the cards are then ready for use on any merchant website that supports 3D Secure. For details of merchants you may want to use for your testing, see [Appendix 5: 3D Secure Test Merchants](../Reference/3D_Secure_Test.htm#_Appendix_4:_3D).

You can put through live transactions and test the end-to-end 3D Secure authentication process.

We recommend you test the following:

* Test your main use case scenarios, based on the Policy rules you have set up in Cardinal, to trigger a Success, Fail, Reject or Challenge outcome. For example, test different amounts, merchant categories, IP addresses, countries and account types.
* Test the authentication process for all the authentication types you support:

  + Are the Authentication screens displayed correctly, with the customised text you provided?
  + If you support multiple languages, is the text displaying correctly on the Authentication screens in each language?
  + For OTP authentication, are the OTP text messages displaying the correct details and going to the correct phone numbers?
  + For Biometric/In-App authentication, is your smart device application correctly handling the authentication process and reporting the result to Thredd?
  + For KBA authentication, are the question and answer pair set up for the card being correctly validated?
* Check that once authentication is complete, the card then follows the normal payment authorisation process:

  + The payment is authorised by Thredd or your systems (depending on your [EHI![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface (EHI) is a Thredd system that enables Thredd clients to receive and respond to real-time transaction data as well as financial messages.](#) mode) and the balance on the card is adjusted accordingly.
  + You receive EHI authorisation messages and Transaction XML details for the transaction.
  + You can view details of your 3D Secure transactions in the Cardinal Portal.

Mastercard provides Test Cases for testing the 3D Secure service in different scenarios. For details, speak to your 3DS project manager. You will be notified by your issuer (BIN sponsor) if it is required for your program.

## 10.2 Rolling out to Production (Live)

Notify Thredd once you have completed your pilot testing.

Cardinal contacts the Card Scheme to set all your Sub BIN/BIN ranges live. You can confirm the full production 3DS roll out with the Scheme.

You must enrol all your live cards in 3D secure and register them for your supported authentication types (e.g., Biometrics, KBA or OTP SMS). See [Step 5: Enrol your cards in 3D Secure](Enrol_cards_in_3DSecure.htm).

If you have specified auto-enrol, Thredd will auto-enrol your cards for you.

Once your sub-BIN/BIN ranges are live with the Scheme, the card must be enroled for 3D Secure, otherwise any transactions on the card where authentication is required will fail.