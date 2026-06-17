# 5 Completing your 3DS Product Setup Form

The Cardinal Commerce RDX service is provided through Thredd, so you do not need to have a direct relationship with Cardinal. Thredd will provide Cardinal with instructions and set up your service.

Before we can start a project with Cardinal, you must complete the Thredd 3DS [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#), which specifies your 3D Secure requirements. This form consists of three tabs:

* [Client Information](#_Client_Information)
* [Cardinal Access](#Cardinal)
* [Supported Languages](#_Language_Support)

Each of these tabs is described in further detail below.

## 5.1 Client Information

Complete the following details on this tab:

| Field | Description |
| --- | --- |
| Client Information | |
| Client name | Your companyâs name. |
| Legal Name | Your companyâs legal name. |
| Country of residence | Your companyâs country of residence. |
| Card Scheme | The payment network for your BIN. Thredd supports cards enabled for use on Visa, Mastercard and Discover payment networks. |
| Visa BID | Your issuerâs (BIN sponsor) Visa [Business Identifier (BID)Closed A business ID, which is unique to each Visa business customer.](#). |
| Mastercard Primary ICA Number | Your issuerâs (BIN sponsor) primary [ICAClosed The Interbank Card Association (ICA) number is a four-digit number assigned by Mastercard that identifies an issuing bank. An ICA can have multiple BINs associated with it.](#), as registered with Mastercard. |
| Mastercard Company Name (Issuer) | Your issuerâs (BIN sponsor) Company Name, as registered with Mastercard. |
| Mastercard Company ID (CID) | Your issuerâs (BIN sponsor) Company ID, as registered with Mastercard. |
| Thredd Program Manager ID | Your Thredd Program ID or code |
| Default language | The default language for the 3D Secure screens. |
| Other languages | List any additional languages you support. See [Language Support](#_Language_Support). |
| SMS Sender ID | The text that appears as the name of the sender of the SMS OTP for validation. This can be up to 11 alphanumeric characters with no spaces. |
| Are you self-issuing? | Whether your organisation is set up as an issuer (BIN sponsor). Select YES or NO. |
| Issuer (BIN sponsor) name | The name of your issuer (BIN sponsor). |
| Is Compliance Manager required? | The Compliance Manager is a Cardinal application which provides tools to identify transactions that require [Strong Customer Authentication (SCA)Closed Authentication which is a combination of two factors of identification at checkout. Examples include something they know (such as a password or PIN), something they get (such as an OTP in a mobile phone or other device) or something they are (such as their fingerprint).](#), and enables you to configure rules for handling these transactions. This option is mainly relevant to Issuers (BIN sponsors) in the European Economic Area (EEA) and in other regions who want to conform to the [Second Payment Services Directive (PSD2)Closed PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#). See [Creating Rules in Compliance Manager](../Reference/Cardinal_3D_Secure.htm#Setting).  In the [Cardinal Access](#Cardinal) tab of the 3DS PSF, please specify the users who you want to be set up with access to Compliance Manager.  For training on how to use Compliance Manager, please contact your 3D Secure project manager. |
| Customer Support number | The Customer Support phone number, including the country code, for cardholders to contact. |
| Issuer regulator country | The regulatory country of your [Issuer (BIN sponsor)Closed Financial organisation and card scheme member, licensed by the scheme to issue cards and process transactions using the schemeâs network.](#). |
| Are you PCI Compliant? | Select YES or NO. If your organisation is not [PCI compliantClosed The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes (payment networks). All merchants who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security](#), this affects the type of card information, such as PAN, which your systems are allowed to process and store. |
| Do you have an existing ACS Provider? | Whether you currently have a different provider of 3D Secure services/ a different [Access Control Server (ACS)Closed A system used to manage the 3D Secure authentication service for the issuer (BIN sponsor). During an authentication session, the ACS communicates with the Card Scheme and Thredd systems, and may also interact with the cardholder, by providing Challenge screens.](#). Select YES or NO. |
| Have you been assigned full BIN range? Or sub BIN | If you are using a full BIN Range for your programme, select YES, else select NO. |
| Planned Go Live date | When do you plan to launch your card programme?  Please check with your Implementation Manager to confirm that this date is feasible. For steps and indicative time scales to launch a 3D Secure service, see [Steps in a 3D Secure Biometric/In-app Project.](Steps_in_a_3D_Secure_Biometric.htm) |
| Thredd Environment under which Program Manager is built | Indicate your current production environment. For example:   * **PRD1** â European Cloud production environment * **PRD2** â Asia-Pacific Cloud production environment |
| Do you require Thredd to validate the AAV/CAVV? | The [AAV/CAVVClosed Accountholder Authentication Value (AAV) and Cardholder Authentication Verification Value (CAVV) are cryptographic values returned by the Access Control Server (ACS) or Card Scheme to the Merchant after a successful cardholder authentication. The merchant includes this value in the authorisation message sent to the issuer.](#) is a cryptographic value which is included in the authorisation message request from the Merchant[1 The ACS generates the CAVV/AAV for a successful 3D secure session; if Stand-In processing is enabled at the Card SCheme (for low-risk transactions), then the Scheme can step in when ACS is down and generate this value.](#) . It indicates that the 3D secure authentication session was successful. You can request that either Thredd or the Card Scheme (Mastercard, Visa, or Discover) validate this value. Card Scheme validation is typically required if you want the card Scheme to provide Stand-In processing.  If YES: Thredd will validate the [AAV/CAVVClosed Accountholder Authentication Value (AAV) and Cardholder Authentication Verification Value (CAVV) are cryptographic values returned by the Access Control Server (ACS) or Card Scheme to the Merchant after a successful cardholder authentication. The merchant includes this value in the authorisation message sent to the issuer.](#). To set this up:   * Mastercard â keys must be exchanged between Thredd and Cardinal; No action is required from the Program Manager. * Visa â keys must be exchange between Thredd and Cardinal. Please ensure your Client Information Questionnaire (CIQ) has the correct settings (under the **VisaSecure section > ABE1 > K01**. Select âIâ). * Discover â keys must be exchanged between Thredd and Cardinal. Please ensure you have informed your Discover Implementation Manager that Thredd will validate the CAVV.   If NO:   * Mastercard â please ensure the BIN has been enroled with the required validation set up at Mastercard (i.e. Mastercard **On-Behalf of Services (OBS) AAV Verification Service**). * Visa â please ensure your Client Information Questionnaire (CIQ) has the correct settings (under the **VisaSecure section > ABE1 > K01**. Select âFâ orâ Vâ as appropriate). Please request Visa to generate the CAVV key and encrypt with Cardinal ZCMK (BIN = 763641 and ZCMK KCV = 89CEE0). Share the CAVV key file securely with your Thredd Implementation Manager. * Discover â Discover will validate the CAVV. Please request for Discover to generate the CAVV key and share it to Cardinal. |
| Setup Options (provide details for Test and Production separately) | |
| Default authentication | Select the default authentication type to support all sub-BIN ranges. Options are:   * Biometric * SMS OTP * KBA * OUTOFBAND * ALL[2  ALL includes Biometric and OTP, but not KBA. If Thredd returns ALL, then during the online transaction the cardholder is shown a screen showing all available options and can select their preferred authentication method.](#)   This is used for the following purposes: a) to enable a card to be enroled in this type; b) to use as the default type of authentication during a real-time authentication session with Cardinal; c) to support auto-enrolment.  **Note**: Please discuss with your Implementation Manager before implementing OOB authentication. |
| Fallback authentication | Select the fallback authentication type to support all sub-BIN ranges. Options are:   * SMS OTP * KBA * OUTOFBAND * ALL * None   This is used for two purposes: a) to enable a card to be enroled in this type; b) to use as the fallback type of authentication during a real-time authentication session with Cardinal, if the default type cannot be used for any reason. |
| Biometric validation timeout | The period (in seconds) you have to respond to a request for Biometric validation before the system times out[3  The request for validation is sent using the NotifyInitiateAction API to the NotifyInitiateAction endpoint you specify for this service. See Initiating a Biometric Session.](#). The maximum is 900 seconds.  This is the time from when we notify you to start authentication, up to your validation response. |
| Out of Band validation timeout | The period (in seconds) you have to respond to a request for Out of Band validation before the system times out. The maximum is 900 seconds.  This is the time from when we notify you to start authentication, up to your validation response. |
| NotifyInitiateAction endpoint | The endpoint Thredd should use to send you the Biometric validation request. (Implemented using the (`NotifyInitiateAction` API. See [Initiating a Biometric Session](Using_Biometric_API.htm#_Initiating_a_Biometric)    **Note**: Your endpoint (in both production and UAT) must resolve to a single or set of static IP addresses. |
| oAuth and NotifyValidate IP Addresses | Provide details of the IP addresses you want Thredd to allow to use the Thredd oAuth server and NotifyValidate endpoint. |
| Do you need Introspection credentials? (Optional) | Select Yes or No. If you select Yes, Thredd will generate the credentials that will be used to validate the Token. |
| Enable SMS OTP auto enrolment | Options are:  NOâ All cards must be enroled for OTP SMS and the mobile number must be registered using either Web Services or Cards API; see [Using the Card Enrolment API.](Using_Card_Enrolment_API.htm)  YES - Initial Load â Thredd enrol the existing cards to the OTP SMS credential. Thredd use the phone number linked to the card (i.e., the phone number supplied when the card was created or updated).  YES - Continuous â Same as Initial load, however any future cards created will also have their phone numbers automatically registered for 3D Secure in the same way.  Auto-enrolment enrols all live and active cards. It is not recommended if you wish to exclude some cardholders from enrolment. If using Continuous auto-enrolment, this may restrict your ability to unenrol cards which have been previously enroled and which currently have a live status. SeeSection 8.2 Card Unenrolment. |
| Enable Biometric auto enrolment | Options are:  NOâ All cards must be enroled for Biometric using either Web Services or Cards API; see [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).  YES - Initial Load â Thredd creates a Biometric credential for all existing cardholders.  YES - Continuous â Same as Initial load, however any future cards created will also have Biometric credentials created the same way.  Auto-enrolment enrols all live and active cards. It is not recommended if you wish to exclude some cardholders from enrolment. If using Continuous auto-enrolment, this may restrict your ability to unenrol cards which have been previously enroled and which currently have a live status. See Section 8.2 Card Unenrolment.Enrol\_cards\_in\_3DSecure.htm |
| **KBA Setup Options (provide details for Test and Production separately)** | |
| KBA questions | Enter the KBA questions you want to include. For each KBA question, indicate if required. You can also provide questions in other languages. See [KBA Language Support](#KBA). Thredd will provide you with details of the unique KBA `ID` linked to each question. You will need to use the relevant KBA `ID` when enroling the card for KBA. For more information, see [Appendix 4: KBA Questions](../Reference/KBA_Questions.htm). |
| **Bin Ranges Low** and **Bin Ranges High** | |
| Provide the whole range (14, 16, or 19 digit) of the Sub-BIN or BIN. If you do not own the whole BIN, please provide the SUB-BIN range. | |
| **UAT testing cards /UAT product ID** | |
| Provide the staging cards and their product ID you want to use for staging testing. | |
| **Pilot testing cards /Production product ID** | |
| Provide the pilot cards and their product ID you want to use for production testing. | |

For more details, refer to the instructions in the 3DS Product Setup Form (PSF).

## 5.2 Cardinal Access

Please provide Thredd with a list of IP addresses you want to allow to access the Cardinal Portal. See [How to Access the Cardinal Portal](Complete_Testing.htm#_How_to_Access).

For security reasons we can only set up permission lists for client-owned static Office IP addresses; employees working remotely will need to connect securely to their office IP address. Any attempt to access Cardinal from a non-registered IP address will result in the page not being displayed.

Please provide details of the administrator users who need to access the Cardinal Portal. Thredd can set up role-based access for your users to the following Cardinal Portal applications: Customer Service Application, Rules Application, Reporting Application and Admin Application.

Any users Thredd set up with Admin level rights with full access to all Cardinal applications on the Cardinal Portal will be able to create access for additional users.

For more details, refer to the instructions in the [3DS Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#).

## 5.3 Supported Languages

Please select the languages you want to support. You must specify a default language. You can specify additional languages and provide the translated text you want to use for each language.

Cardinal identifies the language in which to display the Authentication screens based on the cardholderâs web browser language settings (e.g., English, French).

If the cardholder uses a language that has not been configured in Cardinal (i.e., is not provided in the PSF) then Cardinal will show the screens in the default language.

The screen text limit is 350 characters.

### 5.3.1 KBA Language Support

If you support more than one language, you can provide translations for the Thredd questions in different languages. This is set up per card product. Questions defined in a different language will automatically generate new KBA Question IDs. See [Appendix 4: KBA Questions](../Reference/KBA_Questions.htm).

Thredd cannot use a different language to what is configured as the language with Cardinal for your BIN/sub-BINs.

### 5.3.2 OTP SMS Text Support

For OTP SMS messages (sent by Thredd to the cardholderâs phone number), the SMS message is dynamic, and you can specify the text and variables to use. See [Appendix 2: OTP Message Templates](../Reference/OTP_Message_Templates.htm#_Appendix_2:_OTP_1).

Please contact your Thredd 3DS project manager to ask for these SMS options to be configured.

Language is determined by checking the current value of the cardâs `language` setting (if using [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#), see the [Web Services Guide >Create Card](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm); if using our [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#), see the [Cards API Website > Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2)). Below is an example of the OTP SMS message, in French:

![](../Resources/Images/Cardinal/OTP_SMS_Message_Example.png)

Figure 7: OTP SMS Message Example

The text length limit for the Thredd SMS message is 36 characters. If you pass this limit, the message will be split into two messages.