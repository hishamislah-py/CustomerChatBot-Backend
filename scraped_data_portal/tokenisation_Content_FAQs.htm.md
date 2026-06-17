# Frequently Asked Questions

#### Q. What is the role of Thredd in the tokenisation process?

Thredd are the issuing host and so approve or decline the tokenisation requests. Thredd plays an important role in connecting your program to the Token Service Providers (Mastercard/Visa), configuring the service and providing your systems with messages to support the tokenisation service. See [Who Participates in Tokenisation?](Getting_Started/How_Tokenisation_Works.htm#_Who_Participates_in)

#### Q. How do we start a project?

A project needs to be opened with the Token Service Providers (Visa/Mastercard) and with Thredd.  Please discuss with your Account Manager.

#### Q. At what point does Thredd get involved?

Thredd needs to be involved when the Visa/Mastercard project is started, as we need to provide details in the documentation about the Thredd setup. See [Implementing a Tokenisation Project](Implementation/Implementing_Tokenisation.htm#_Implementing_a_Tokenisation).

#### Q. What do we need to do as a Program Manager?

Essentially, you are the owner of the project and need to manage all parties involved in the setup of the service (Mobile wallet token requestors, token service providers and Thredd). See [Implementing a Tokenisation Project](Implementation/Implementing_Tokenisation.htm#_Implementing_a_Tokenisation).

#### Q. How long does a project take?

To add tokenisation to an existing product typically takes approximately 3 months. This depends on many external factors and delays may occur in the live testing with Token Requestors.

#### Q. Why do we need EHI?

EHI is used to retrieve the One Time Passcode (OTP) used in authentication. This needs to be sent to the cardholder quickly and so cannot be sent via any reports. If you choose not to use EHI, you will only be able to use the Thredd SMS option to send the OTP to the cardholder. See [External Host Interface (EHI)](Implementation/Tokenisation_Configuration.htm#_External_host_interface).

#### Q. What is in-app provisioning?

In-app provisioning (also known as push provisioning) is a provisioning request originating from your mobile app so the cardholder does not have to enter their card details. This means that you can pre-authenticate the cardholder and choose to not authenticate when the provisioning request reaches Thredd. During In-App provisioning the cardholder will not enter their PAN and instead an encrypted payload must be sent to Apple to confirm the card details. When the In-App Provisioning API is called Thredd generate this payload using the cardholder details we have and the wallet inputs you provide, before returning it in the API response.

For more information, see [Implementing In App Provisioning](Implementation/Implementing_In_App_Provisioning.htm).

#### Q. Are there any API calls we need to make?

Yes. See below:

| Using Web Services (SOAP) | Using Cards API (REST) |
| --- | --- |
| * `Ws_CreateCard` â create card * `Ws_Activate` â activate card * `Ws_Update_Cardholder_Details_V2` â update card * `Ws_Payment_Token_Get` â get the payment token * `Ws_Token_Device_Management` â manage the token device * `Ws_Payment_Token_StatusChange` â change the status of the payment token   For more information, refer to the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm). | * [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) â create card * [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status)  â change card status to *active* * [Update a Card](https://cardsapidocs.thredd.com/reference/update-card) â update card * [Get Card Payment Token](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens)  â get the payment token * [Get Card Payment Token Devices](https://cardsapidocs.thredd.com/docs/get-card-payment-token-devices) â manage the token device * [Update Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status) â change the status of the payment token   For more information, see the [Cards API Website](https://cardsapidocs.thredd.com/). |

#### Q. Do we need to develop an app?

If you wish to support Mobile Wallet Token requestors, then an app is required. Please discuss with your chosen Token Requestors. You do not need an app for Online Merchant Token Requestors.

#### Q. On the PSF what does âoverride enabled/disabledâ mean, what does it do?

This option on the Payment Setup Form (PSF) means that Thredd will override any logic that would send an authentication request to the cardholder when we detect that push provisioning has been carried out. Since the cardholder has already been authenticated during push provisioning, Thredd does not need to request further authentication.

This must be enabled to pass Apple testing and is a good cardholder journey for other token requestors. See [Thredd Configuration Options](Implementation/Tokenisation_Configuration.htm#_GPS_Configuration_Options).

#### Q. What is the difference between VTS and VDEP?

They both refer to the same service. VTS is the Visa Token Service and VDEP is the Visa Digital Enablement Programme. You are required to sign a VDEP agreement with Visa when starting a new Visa Token Service integration.

Since VTS is also an abbreviation for the Visa Test Simulator (VTS), we use the term VDEP to avoid confusion.

#### Q. Whatâs the difference between a Token and a Payment Token?

Thredd refer to the 9-digit public token for use on Thredd systems as the Token or Public Token and the digitised tokens from the schemes is called a Payment Token.

#### Q. Whatâs the difference between a Token Requestor and a Wallet Provider?

These are used interchangeably between the schemes however Visa will more often use Token Requestor and Mastercard use Token requestor. Because the Mastercard Digital Enablement Service (MDES) was integrated first at Thredd you will often see references to token requestor.

#### Q. What is the difference between an FPAN and a DPAN?

These are Apple terms to specify which PAN is being discussed as following tokenisation there are two PANs for one card. The FPAN is the Funding PAN and refers to the original PAN on the card and the DPAN is the Device PAN and refers to the PAN personalised onto the device.

#### Q. Does Thredd know the DPAN?

Yes. Thredd receives and stores the DPAN during the provisioning process and validates it during subsequent transactions on that DPAN. IF Thredd does not receive the DPAN then it will decline transactions.