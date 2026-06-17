# 10 Completing Pilot Production Testing

Thredd set up your cards in the Production environment:

* Thredd activates a single card product in the Production environment, so you can manually enrol a few cards for the production pilot testing.
* Thredd releases your 3D Secure configuration in the live environment.
* Your issuer (BIN sponsor) enrols your pilot cards at the card scheme.

## 10.1 Viewing Risk Profiles in Apata Portal Production

You can view your rules in the live Apata Portal at:

<https://portal.apata.io/>

You can register the cards for the supported 3D Secure authentication types: if using the Thredd API, then use the 3D Secure Web service (`Ws_AddUpDelCredentials`; if using Cards API, then use the `Create 3DS Credentials` API.

Once your pilot cards are live with 3DS, the cards are then ready for use on any merchant website that supports 3D Secure. For details of merchants you may want to use for your testing, see [Appendix 4: 3D Secure Test Merchants](../Reference_Apata/3D_Secure_Test.htm).

You can put through live transactions and test the end-to-end 3D Secure authentication process.

We recommend you test the following:

* Test your main use case scenarios, based on the Risk Profile rules set up in Apata to trigger an Accept,Reject or Challenge outcome. For example, test different amounts, merchant categories, IP addresses, countries and transaction types. For more informaiton, see [Managing Authentication Rules](../Apata_Portal/Authentication.htm).
* Test the authentication process for all the authentication types you support:

  + Are the Authentication screens displayed correctly, with the customised text you provided?
  + If you support multiple languages, is the text displaying correctly on the Authentication screens in each language?
  + For OTP authentication, are the OTP text or OTP email messages displaying the correct details and going to the correct phone numbers?
  + For Biometric/In-App authentication, is your smart device application correctly handling the authentication process and reporting the result to Thredd?
  + For KBA authentication, are the question and answer pairs set up for the card being correctly validated?
* Check that once authentication is complete, the card then follows the normal payment authorisation process:

  + The payment is authorised by Thredd or your systems (depending on your [EHI![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface (EHI) is a Thredd system that enables Thredd clients to receive and respond to real-time transaction data as well as financial messages.](#) mode) and the balance on the card is adjusted accordingly.
  + You receive EHI authorisation messages and Transaction XML details for the transaction.
  + You can view details of your 3D Secure transactions in the Apata Portal.

Mastercard provides mandatory Test Cases for testing the 3D Secure service in different scenarios, which will need to be completed. For details, speak to your issuer (BIN sponsor) or card scheme.

## 10.2 Rolling out to Production (Live)

Notify Thredd once you have completed your pilot testing.

If self-issuing, you must enroll your remaining card ranges at the card scheme. If not self-issuing, your Issuer (BIN sponsor) will do this. (This can also be done in one go when enrolling pilot card ranges.)

You must enrol all your live cards in 3D secure and register them for your supported authentication types (e.g., OTP SMS, OTP email, Biometrics or KBA). See [Step 5: Enrol your cards in 3D Secure](Enrol_cards_in_3DSecure.htm).

If you have specified auto-enrol, Thredd will auto-enrol your cards for you.

Please ensure all cards are enrolled with the relevant credentials for the required authentication methods before the card ranges are live at the card scheme.