# General FAQs

This section provides answers to frequently asked questions.

## Authentication and Biometric Regulations

#### Q. What regulations are relevant to Biometric authentication?

Biometric authentication is one of the methods for [Strong Customer Authentication![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Authentication which is a combination of two factors of identification at checkout. Examples include something they know (such as a password or PIN), something they get (such as an OTP in a mobile phone or other device) or something they are (such as their fingerprint).](#), which is covered in the following regulations:

* [PSD2 Directive![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#). For details, see <https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366_en>
* Strong Customer Authentication guidelines. For details, see: <https://www.visa.co.uk/partner-with-us/payment-technology/strong-customer-authentication.html>

#### Q What were the deadlines for implementing 3D Secure with Biometric authentication?

For cards issued within the EEA (European Economic Area), the regional Card Scheme (payment network) deadline to have Strong Consumer (2 factor) authentication in place for 3D Secure was 31st December, 2020. Each country may have applied for its own deadline extension. For UK issued cards, the deadline was March 2022.

For other regions and countries please check with your issuer (if applicable) or Card Scheme (payment network).

## The 3D Secure Service

#### Q. How does the 3DS authentication affect authorisation?

3DS authentication happens before payment authorisation. If the cardholder passes authentication, the transaction is sent to Thredd for authorisation: either Thredd or your systems authorise, depending on whether the card balance is maintained by Thredd or on your systems. (This is the following EHI modes: Gateway Processing (mode 1), Cooperative Processing (mode 2), Gateway Processing with STIP (mode 4) and Gateway Processing with STIP (mode 5).

If the cardholder does not pass 3DS authentication, the transaction will not reach Thredd for authorisation.

#### Q. What versions of 3D Secure are available and will RDX work with all of them?

There are two versions of 3D Secure: EMV 3DS 2.1 and 2.2.

The rules you set up on the Cardinal Portal apply to both EMV 3DS 2.1 and 2.2. Both versions work with all the authentication types available within RDX (OTP SMS or Biometric/In App).

For more information, see [Support for 3D Secure Versions](3D_Secure/Additional_3D_Secure_Considerations.htm#_Support_for_3D).

#### Q. Where can I find out more background information about 3D Secure?

The [EMVCo website](https://www.emvco.com/) provides detailed specifications for anyone implementing a 3D Secure project. This includes information not covered in the Thredd guides, such as authentication message flows between Issuer (BIN sponsor), ACS provider and merchant (PReq, PRes, AReq, ARes), and specific internal message fields that may be passed or validated (e.g., CAVV/ AAV).

## Starting a 3D Secure RDX Project

#### Q. What are the steps in an RDX project?

For details, see [Steps in a 3D Secure Biometric/In-app Project](3D_Secure/Steps_in_a_3D_Secure_Biometric.htm#_Steps_in_a).

#### Q. Do we need static IP addresses for oAuth calls?

The REST-based API endpoints that are used for Biometric authentication (`NotifyInitiateAction` and `NotifyValidate`) are secured with our oAuth security server (see [Using the Thredd oAuth Server](3D_Secure/Using_Oauth.htm).

* Thredd only allow incoming requests from permitted IP addresses.
* For Thredd calls to your systems, we recommend you restrict access to permitted Thredd IP addresses. See [Authorising Thredd IP Addresses](3D_Secure/Authorising_IP_Addresses.htm).

#### Q. Can we use a dynamic IP address cloud environment for REST-based API calls?

No, Thredd are unable to handle dynamic IP addresses behind the fixed DNS name.

## Testing

#### Q. How do we test Biometric authentication?

Testing can start once Cardinal has completed building your screens and your configuration is released to the Staging environment, and you have successfully set up your 3D Secure configuration options and network connection.

Thredd provides a UAT environment, where you can use Cardinalâs UAT simulator to test transactions. See [Completing Staging/UAT Testing](3D_Secure/Complete_Testing.htm).

#### Q. How do we test RDX Biometric in Production?

When you have completed testing in the UAT environment, Thredd will set up your products in the production environment and you can start pilot testing. This works as follows:

* You can use the Card Create Thredd API (`Ws_CreateCard`) to create pilot cards in the production environment. For details, refer to the Web Services Guide (SOAP).   
  If you are using our Cards API, for similar create card functionality, see the [Cards API Website](https://cardsapidocs.thredd.com/).
* Provide your 3DS project manager with the pilot card details you want them to submit to Cardinal. Cardinal will complete the Mastercard or Visa Card Scheme (payment network) forms to set your pilot cards to live on the Schemeâs directory server.
* Thredd activate your products for RDX Biometric, and you enrol your cards in 3D Secure by calling the 3D Secure RDX web service `(Ws_AddUpDelCredentials`) or the `Create 3DS Credentials` Cards API. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).
* You need to set rules in the Cardinal Portal to challenge transactions, so transactions are authenticated. See [Cardinal Configuration of RDX Biometric and Screens](3D_Secure/Configuration_of_Screens.htm).
* Once the Scheme confirms that the pilot cards are live, you can start using your pilot cards: online transactions with 3DS merchants will route through Cardinal.

#### Q. Can we use the Thredd Card Transaction System (CTS) to test a 3D Secure transaction?

No, the Thredd CTS system does not have a connect to Cardinal and cannot be used for this purposes. Note that the e-commerce transaction option on the Thredd CTS system does not include any 3D Secure authentication elements.

If you want to test your 3D Secure transactions, you can use the Cardinal Test Simulator. See [Using the Cardinal Test Simulator](3D_Secure/Complete_Testing.htm#Using).

## RDX Card Enrolment

### Using Cards API

#### Q. How can I enrol cards in 3D Secure and manage them using Cards API?

For details, see the [Cards API Website](https://cardsapidocs.thredd.com/).

### Using the Thredd API

#### Q. Which Thredd APIs do I use to enrol cards in 3D Secure?

When using the Cardinal RDX service, you only need to use a single Thredd API `(Ws_AddUpDelCredentials`) for enroling cards and for editing and deleting 3D Secure RDX records. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).

#### Q. What is the Thredd API WSDL file format and content?

The SOAP web services WSDL is available here:

<https://ws-uat.globalprocessing.net:13682/service.asmx?WSDL>

#### Q. Can I auto-enrol all cards in 3D Secure RDX?

Yes, Thredd can auto-enrol your cards. There are two options, set up per credential type: *Initial Load* and *Continuous*. For details, see [Completing your 3DS Product Setup Form](3D_Secure/Completing_the_PSF.htm).

You must ensure that both existing and new cards have the information required for 3DSecure in the Smart Client application or the new Thredd Portal, such as a mobile phone number to use for OTP authentication.

You still need to use the 3D Secure RDX Thredd API or Cards API to manage your cardholder records (e.g., to update the linked cardholder mobile phone number or delete a card from Biometric authentication).

#### Q. How can I check if a card is enroled in 3D Secure?

You can use the RDX Thredd API (`Ws_AddUpDelCredentials`) with the `Get` option provided in the `<Action>` field to return details of the cardâs Credential IDs. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).

If the card is not enroled in 3D Secure (no credentials are found), then the web service returns an action code of 437.

If you are using our Cards API, then you can use the [List 3DS Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials#list-3ds-credentials) API endpoint. If the card is not enroled in 3D Secure, then the API returns a blank 200 code response.

#### Q. How can I unenrol a card from 3D Secure?

You can remove any credentials linked to a card using the Thredd API or the Cards API with the `Delete` option specified in the `<Action>` field. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).

Thredd does not unenrol cards on behalf of Program Managers. If your card status changes to any of the following: Card destroyed, Lost card, Stolen Card, the Program Manager will need to unenrol the respective cards. They can unenrol using: `Ws_AddUpDelCredentials` (SOAP) or the 3DS Credentials API (REST).

Please check with your 3DS project manager for unenrolment restrictions if you have *continuous auto-enrolment* enabled for your cards.

#### Q. How do I add multiple authentication types to a card?

In your 3DSecure enrolment request (using `Ws_AddUpDelCredentials`) you can specify the `Add` action and include an array of `<credentials>` to enrol a card in multiple types of authentication. See the example code snippet below:

[Copy](javascript:void(0);)

```
<hyp:Action>Add</hyp:Action>  
<hyp:Credentials>  
   <hyp:Credential>  
         <hyp:ID>0</hyp:ID>  
         <hyp:Type>BIOMETRIC</hyp:Type>  
         <hyp:Value>Biometric App</hyp:Value>  
   </hyp:Credential>     
          <hyp:Credential>  
          <hyp:ID>0</hyp:ID>  
          <hyp:Type>OTPSMS</hyp:Type>  
          <hyp:Value>+5858585858588</hyp:Value>  
   </hyp:Credential>                 
 </hyp:Credentials> 
```

#### Q. How can I list what type of authentication methods are configured for a card?

You can use the 3D Secure RDX Thredd API (`Ws_AddUpDelCredentials`) and specify the `Get` Action to request the authentication methods for any enroled card.   
If you are using our Cards API, then you can use the [List 3DS Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials#list-3ds-credentials) API endpoint.

This returns a list of all the type of authentication the card is enroled in. This is displayed in the `Credentials` fields: `ID` lists the unique ID of the authentication method and `Type` list the type of authentication. `Value` lists the mobile phone number linked to the card.

You can use the `ID`, `Type` and `Value` fields in a request to update the authentication type and mobile number.

#### Q.  What is the Credential ID?

The Credential ID is a unique identifier of the type of authentication. If the same card is enroled for two different types of authentication, then each enrolment will have a unique Credential ID.

In the `Ws_AddUpDelCredentials` web service and Cards API `3ds-credentials` endpoint, this is up to 8 characters. For example: **669**  
In the `NotifyinitiateAction` web service this is 36 characters (Thredd adds leading zeros to the Credential ID as required by Cardinal). For example: 000000000000000000000000000000000**669**.

## Default and Fallback Authentication Types

#### Q. How do I choose the default and the fallback authentication types?

When you complete your 3D Secure Product Setup Form, you can specify the default and fallback authentication methods for your card product (e.g., Biometric as default with fall back as OTP SMS). See [Completing your 3DS Product Setup Form](3D_Secure/Completing_the_PSF.htm).

The supported authentication types must then be added to the card using using either Web Services or Cards API; see [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm). Alternatively, if enabled for your account, through auto-enrolment.

#### Q. When is fallback authentication used and how is it triggered?

If a cardholder cannot authenticate using your default method (e.g., Biometric or In-App), then in your `NotifyValidate` response, you should set the message `status` field to STEPUP. See [Notifying Thredd of the Result of the Biometric Session](3D_Secure/Using_Biometric_API.htm#_Notifying_Thredd_of).

This triggers the fallback solution (e.g., OTP SMS). (In the OTP SMS fallback scenario, Thredd sends the request to Cardinal, who generates the OTP and returns to Thredd for sending to the cardholder.)

#### Q. Can the cardholder be given the choice of the authentication method?

Yes, you can allow the cardholder to select the type of authentication.

During project implementation stage, you can customise the text that appears on the Cardinal Choice screen shown to cardholders: you specify this on the 3DS Product Setup Form; see [Cardinal Configuration of RDX Biometric and Screens](3D_Secure/Configuration_of_Screens.htm#_Screens_1). See the example below:

![](Resources/Images/Cardinal/FAQ_Choice_of_Authentication.png)

Figure 16: Choice Screen â where the user can select a method

To populate the options that appear on this screen, you need to register your cards for the required authentication types using using either Web Services or Cards API; see [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm). Alternatively request auto-enrolment from your 3DS project manager.

## Biometric and Out of Band (OOB) Authentication

#### Q. What does the Biometric/OOB screen look like?

The Biometric/OOB screen directs the cardholder to complete Biometric/In-App authentication through your customer smart device application. This option is triggered only if the authentication is set to Biometric and the card is enroled for Biometric. See the example below:

![](Resources/Images/Cardinal/FAQ_Biomentric.png)

Figure 17: Biometric/OOB Authentication Screen

You can specify the text that appears on this screen using the 3DS Product Setup Form; see [Cardinal Configuration of RDX Biometric and Screens](3D_Secure/Configuration_of_Screens.htm).

#### Q. How does a Biometrics/OOB session work?

Thredd can set up Biometric or OOB authentication as your default authentication type, with OTP SMS as the fallback type. If these types have been set up for your card program and the card has been enroled in these types, then the cardholder is authenticated during a session using the default type or, if the default type cannot be used for any reason, the fallback type is provided.

Alternatively, if requested during the implementation phase, Cardinal can enable the Choice screen, where the cardholder chooses their preferred authentication type during the authentication session.

For details, see [Steps in a 3D Secure Biometric/In-app Project](3D_Secure/Steps_in_a_3D_Secure_Biometric.htm#_Steps_in_a).

During an authentication session, a Biometric/OOB session works as follows:

1. If Biometric authentication is your default authentication type, Cardinal displays a message similar to the example in Figure 13.   
   Alternatively, if you have requested to have the Choice screen for your customers, then the cardholder is shown the Choice screen and selects your smart device application (i.e., Biometric/OOP) as the authentication type (See Figure 12). A screen similar to the example in Figure 13 is then displayed.
2. When the cardholder selects Continue, Cardinal sends a message to Thredd and Thredd sends you the `NotifyInitiateAction` notification. You acknowledge the message. See [Initiating a Biometric Session](3D_Secure/Using_Biometric_API.htm#_Initiating_a_Biometric).
3. Your Customer application manages the Biometric or In-App validation with the cardholder, on their smart device.
4. When completed, you return the response to Thredd, using the `NotifyValidate` API endpoint. See [Notifying Thredd of the Result of the Biometric Session](3D_Secure/Using_Biometric_API.htm#_Notifying_Thredd_of)
5. Thredd returns the response to Cardinal.

Further information on the Biometric call flow is described in the section [Cardholder Authentication Flows](3D_Secure/Cardholder_Authentication_Flows.htm).

Please discuss with your Implementation Manager before implementing OOB authentication.

#### Q. What Biometric options can we use?

This is entirely up to you, as your customer smart device application needs to implement the Biometric verification and the options you use must be supported on the end-userâs device. Examples are: Face recognition, Fingerprint and Voice recognition.

#### Q. If we do not provide a `NotifyValidate` response, will Thredd automatically use the fallback option?

No, if Thredd does not receive the response, the transaction will time out after the configured timeout period.

#### Q. Why are we receiving a *FAILWITHFEEDBACK* status in the response to our `NotifyValidate` API call?

Thredd is expecting only one `notifyvalidate` API call per authentication session. If you make more than one Notifyvalidate API call for a single authentication session, only the first request will be processed; for any subsequent requests, you will receive a FAILWITHFEEDBACK response .

#### Q. Can we convert the default authentication type from Biometric to SMS OTP for cardholders who do not have a smart device?

If Thredd implemented auto-enrolment with Biometric as the main and SMS OTP as the fallback method, you have two options:

* Use either Web Services or Cards API, with `Delete` specified in the `Action` field to remove the Biometric Credential ID for this card. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).
* During an authentication session if the cardholder is not able to authenticate using Biometric, you can respond with the status STEPUP in your `NotifyValidate` response. In this case, the OTP SMS will be triggered. See [Notifying Thredd of the Result of the Biometric Session](3D_Secure/Using_Biometric_API.htm#_Notifying_Thredd_of).

If the card has not been auto enroled, you can use either Web Services or Cards API to add the required credentials to the card. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm).

## Language Support

#### Q. Can the OTP messages be displayed in more than one language?

Yes, the dynamic OTP SMS message can be configured in a language other than English if you request this; you can only have one SMS language per card product. Please provide the translation for the OTP message. See [Appendix 2: OTP Message Templates](Reference/OTP_Message_Templates.htm#_Appendix_2:_OTP_1).

## Cardinal Portal

#### Q. How do I define and set up rules and policies for Risk Based Authentication (RBA)?

Risk Based Authentication (RBA) is an authentication method managed by Cardinal, based on their ruleâs engine.

You can use risk scores and the other data fields in the Cardinal Portal (such as transaction amount, IP address, merchant name or merchant country) in setting up the rules used by Cardinal. See [Appendix 1: Cardinal 3D Secure Rules](Reference/Cardinal_3D_Secure.htm).

The rule outcome when assessing a transaction can be:

* Success â the transaction is approved: [frictionless authentication![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) When a transaction is approved without requiring any manual input from the cardholder.](#)
* Fail/Fail with Feedback or Rejected â the transaction is declined.

+ Challenge â the cardholder is asked to verify their identity using an available authentication method.
+ Attempts â the transaction is approved as attempt without challenge. It could be triggered and identified as a risk concern to be reviewed.

For details, see [Rule Outcomes](Reference/Cardinal_3D_Secure.htm#_Rule_Outcomes).

In the first two scenarios Cardinal completes authentication of the transaction. In the Challenge scenario, one of the other supported authentication types is used (e.g., Biometric/In-App or OTP SMS).

Rules must be set up on the Cardinal Portal under both Rules 1.0 and Rules 2.0, to be applied for the 3DS transaction received from merchants enroled in 3DS 1.0,3DS 2.0, 3DS 2.1 & 3DS 2.2.

#### Q. How can I test transactions with Biometric authentication?

You can use Cardinalâs UAT simulator to test transactions. The Test Simulator can be accessed on the Cardinal Portal. See [Completing Staging/UAT Testing](3D_Secure/Complete_Testing.htm).

#### Q. How do I set up rules to pass Mastercard PSD2 Test Cases?

Mastercard provides test cases for some Program Managers to verify the 3D secure authentication process under the PSD2 rules. If you have been contacted by your issuer (BIN sponsor) to complete Mastercard PSD2 test cases, contact your 3DS project manager.

#### Q. How can I manage my PSD2 and SCA requirements and exemptions?

The Cardinal Compliance Manager app allows you to manage any PSD2 and Strong Customer Authentication (SCA) requirements and exemptions relating to cardholder authentication; Please refer to *Cardinal Compliance Manager Guide* for further information. Please check with your issuer (BIN sponsor) for any Scheme-mandated requirements relating to PSD2 and Strong Customer Authentication (SCA).

There are also a number of SCA settings you can configure with Thredd. For information on the PSD2 and SCA checks run by Thredd, see the [PSD2 and SCA Guide](https://docs.thredd.com/PSD2_Guide.htm).

## 3D Secure Fields

#### Q. Do you provide data linked to the merchant's Requestor App URL?

Yes, during an app-based transaction with authentication, if provided by the merchant, then Thredd receives data from Cardinal in an optional `RequestorAppUrl` field which indicates the merchantâs app URL. When initiating a biometric session, Thredd provides details to your systems in the `MerchantURL` field. For more information, see [Initiating a Biometric Session](3D_Secure/Using_Biometric_API.htm#_Initiating_a_Biometric).

#### Q. Who validates the CAVV or AAV, and how are these details used?

The [CAVV/AAV![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Accountholder Authentication Value (AAV) and Cardholder Authentication Verification Value (CAVV) are cryptographic values returned by the Access Control Server (ACS) or Card Scheme to the Merchant after a successful cardholder authentication. The merchant includes this value in the authorisation message sent to the issuer.](#) is a cryptographic value which is included in the authorisation message request from the Merchant[1 The ACS generates the CAVV/AAV for a successful 3D secure session; if Stand-In processing is enabled at the Card Scheme (for low-risk transactions), then the Scheme can step in when ACS is down and generate this value.](#) . It indicates that the 3D secure authentication session was successful or attempted. Merchants include this value in the authorisation request which follows after a 3D authentication session. The value is encrypted to ensure that merchant's cannot tamper with the authentication result. You can request that either Thredd or the Card Scheme (Mastercard, Visa, or Discover) validate this value. Card Scheme validation is typically required if you want the card Scheme to provide Stand-In processing. For more information, see [Completing your 3DS Product Setup Form](3D_Secure/Completing_the_PSF.htm).

If Thredd was selected to validate and the CAVV/AAV is not valid or 3D secure was not passed / not performed, then Thredd will decline the authorisation request with CAVV error. Thredd provides relevant details relating to 3D secure (e.g., method of authentication used and result) in the `GPS_POS_Data` field. For more information, see the [External Host Interface (EHI) Guide > GPS\_POS\_Data Field](https://docs.thredd.ai/Content/Appendices/GPS_POS_Data.htm).

#### Q. Do you provide details of the *acsInfoInd* Field?

No, this is a Scheme-generated optional field in the message between the ACS and the merchant server; you will not need this information. Refer to the EMVCo guides for details.

## Troubleshooting

#### Q. Why are some cardholders not receiving the OTP?

Below are possible reasons why cardholders may not receive the OTP:

* Network issue affecting the message transmission on the Thredd side
* SMS is successfully delivered to the mobile phone carrier, but has not been received: possible issue with the carrier passing it to the cardholder; this could be due to spam filtering , blocking overseas SMS messages or mobile network reception issues

#### Q. How can I unblock a card that's been blocked on the Cardinal Portal?

Depending on your risk and fraud settings in the Cardinal Portal, a card may be blocked if the cardholder enters their OTP incorrectly three times during a 3D Secure session which uses One-Time Password (OTP) authentication. You can use the Thredd PANFinder application to look up the PAN associated with the Thredd public token for the card, and then unblock the card in the Cardinal Portal, in the **Customer Services application**: use the **Unblock card** feature and enter the full PAN.

![](Resources/Images/Cardinal/Cardinal_Customer_Service.png "Unblocking a card in the Customer Services App")

Figure 18: Unblocking a card using the Customer Services App