## 5.2 Client Information tab

Complete the following sections on this tab:

### 5.2.1 Client Information

| Field | Description |
| --- | --- |
| Client name | Your companyâs name. The name provided here will be displayed on the Apata portal as the Financial institution name. |
| Country of residence | Your companyâs country of residence. |
| Scheme | Card scheme (Network such as Mastercard or Visa). |
| Issuer name | The name of your issuer (BIN sponsor). |
| Visa BID | Your issuerâs (BIN sponsor) Visa [Business Identifier (BID)Closed A business ID, which is unique to each Visa business customer.](#). |
| Mastercard Primary ICA Number | Your issuerâs (BIN sponsor) primary [ICAClosed The Interbank Card Association (ICA) number is a four-digit number assigned by Mastercard that identifies an issuing bank. An ICA can have multiple BINs associated with it.](#), as registered with Mastercard. |
| Mastercard Company Name (Issuer) | Your issuerâs (BIN sponsor) Company Name, as registered with Mastercard. |
| Mastercard Company ID (CID) | Your issuerâs (BIN sponsor) Company ID, as registered with Mastercard. |
| Thredd Program Manager ID | Your Thredd Program ID or code. Assigned by Thredd. |
| UAT readiness date | Date when you plan to be ready to test 3D Secure in the UAT environment. |
| Planned Go Live date | Date when you plan to launch 3D Secure for your card programme.  Please check with your Implementation Manager to confirm that this date is feasible. For steps and indicative time scales to launch a 3D Secure service, see Steps in a 3D Secure Biometric/In-app Project. |
| Do you require Thredd to validate the AAV/CAVV? | The [AAV/CAVVClosed Accountholder Authentication Value (AAV) and Cardholder Authentication Verification Value (CAVV) are cryptographic values returned by the Access Control Server (ACS) or Card Scheme to the Merchant after a successful cardholder authentication. The merchant includes this value in the authorisation message sent to the issuer.](#) is a cryptographic value which is included in the authorisation message request from the Merchant[1 The ACS generates the CAVV/AAV for a successful 3D Secure session; if Stand-In processing is enabled at the Card Scheme (for low-risk transactions), then the Scheme can step in when ACS is down and generate this value.](#) . It indicates that the 3D secure authentication session was successful. You can request that either Thredd or the Card Scheme (Mastercard or Visa) validate this value. Card Scheme validation is typically required if you want the card Scheme to provide Stand-In processing.  If YES: Thredd will validate the [AAV/CAVVClosed Accountholder Authentication Value (AAV) and Cardholder Authentication Verification Value (CAVV) are cryptographic values returned by the Access Control Server (ACS) or Card Scheme to the Merchant after a successful cardholder authentication. The merchant includes this value in the authorisation message sent to the issuer.](#). To set this up:   * Mastercard â encryption keys must be exchanged between Thredd and Apata; No action is required from the Program Manager. * Visa â encryption keys must be exchanged between Thredd and Apata. Please ensure your Client Information Questionnaire (CIQ) has the correct settings (under the **VisaSecure section > ABE1 > K01**. Select âIâ).   If NO:   * Mastercard â please ensure the BIN has been enroled with the required validation set up at Mastercard (i.e. Mastercard **On-Behalf of Services (OBS) AAV Verification Service**). * Visa â please ensure your Client Information Questionnaire (CIQ) has the correct settings (under the **VisaSecure section > ABE1 > K01**. Select âFâ orâ Vâ as appropriate). Please request for Visa to generate the CAVV key and encrypt with Thredd ZCMK (BIN: 476370, ZCMK KCV: 1CB2C9). Share the CAVV key file securely with your Thredd Implementation Manager. |
| Type of webservice to be used for 3DS enrolment | API to use for card enrolment. Options include:   * SOAP â using our traditional XML-based Thredd API. * REST â using our REST-based Cards API, supporting messages in JSON format.   For more information, see [Using the Card Enrolment API](Using_Card_Enrolment_API.htm). |
| Thredd Environment under which Program Manager is set up | Environment options include:   * PRD0 â Not currently in Cloud * PRD1 â Cloud Europe * PRD2 â Cloud Asia Pacific |

For more details, refer to the instructions in the 3DS Product Setup Form (PSF).

### 5.2.2 Required authentication methods

|  |  |
| --- | --- |
| OOB other | The cardholder receives an issuer-generated push notification to authenticate within the authenticator or mobile banking app. |
| OOB Biometrics | The cardholder receives an issuer-generated push notification to authenticate within the authenticator or mobile banking app using a biometric identifier; for example face ID or fingerprint. |
| OTP via Email | The cardholder receives a One-Time Passcode (OTP) via email. |
| OTP via SMS | The cardholder receives a One-Time Passcode (OTP) via SMS (text message). |
| KBA - Transaction history | Knowledge Based Authentication (KBA). The cardholder is presented with a Challenge screen asking them to identify a recent payment they made on the card. |
| KBA - custom question | Knowledge Based Authentication (KBA). The cardholder is presented with a Challenge screen asking them to provide the answer to a question they have previously supplied. |
| OTP via SMS + KBA | The cardholder is first requested to authenticate using OTP via SMS and then by KBA. |
| OTP via Email + KBA | The cardholder is first requested to authenticate using OTP via email and then by KBA. |

### 5.2.3 Setup options

| Field | Description |
| --- | --- |
| Default language | Default language to apply to all cardholder Challenge screens, configured at product level. |
| Other languages | List any additional languages you support. You will also need to specify which language to apply to each card product. Otherwise, the default language will be applied to all products. See [Challenge Screens > Supported Languages](Challenge_screens.htm#Supporte). |
| Default authentication | Select the default authentication type to support all BINs or sub-BIN ranges. See the drop down on the 3D Secure PSF for all available options.  This is used for the following purposes: a) to enable a card to be enroled in this type; b) to use as the default type of authentication during a real-time authentication session with Apata; c) to support auto-enrolment. |
| Fallback authentication | Select the fallback authentication type to support all sub-BIN ranges. See the drop down on the 3D Secure PSF for all available options.  This is used for two purposes: a) to enable a card to be enroled in this type; b) to use as the fallback type of authentication during a real-time authentication session with Apata, if the default type cannot be used for any reason. |
| Enable SMS OTP auto enrolment | Options are:  NO â All cards must be enroled for OTP SMS and the mobile number must be registered using either the Thredd API or the Cards API; see Using the Card Enrolment API.  YES - Initial Load â Thredd enrol the existing cards to the OTP SMS credential. Thredd use the phone number linked to the card (i.e., the phone number supplied when the card was created or updated).  YES - Continuous â Same as Initial load, however any future cards created will also have their phone numbers automatically registered for 3D Secure in the same way.  Auto-enrolment enrols all active and Live cards. It is not recommended if you wish to exclude some cardholders from enrolment. If using Continuous auto-enrolment, this may restrict your ability to unenrol cards which currently have a live status. See [Section 8.2 Card Unenrolment.](Enrol_cards_in_3DSecure.htm#Card) |
| Enable Biometric auto enrolment | Options are:   * NO â All cards must be enroled using either the Thredd API or the Cards API. * YES â Initial Load only âThis will create a biometric credential for all existing card holders which are sent to you for your reference. After initial load, auto-enrolment will be disabled and Program Manager will need to initiate the enrolment in the Thredd API or the Cards API for new card enrolments. * YES â Continuous â Same as Initial load, however auto-enrolment will remain enabled. New cards created will also have biometric credentials created in the same way. Your organisation will not need to send the Thredd API or the Cards API to enrol new cardholders.   Auto-enrolment enrols all active and Live cards. It is not recommended if you wish to exclude some cardholders from enrolment. If using Continuous auto-enrolment, this may restrict your ability to unenrol cards which currently have a live status. [See [Section 8.2 Card Unenrollmen](Enrol_cards_in_3DSecure.htm#Card)](Enrol_cards_in_3DSecure.htm#Card)[t.](Enrol_cards_in_3DSecure.htm#Card) |
| Enable Email OTP auto enrolment | Options are:   * NO â All email addresses for cards must be enroled using either the Thredd API or the Cards API. * YES â Initial Load only â This will take email addresses which are added when card is created or card details are updated. After initial load, auto-enrolment will be disabled and Program Manager will need to initiate the Thredd API or the Cards API for new card enrolments. * YES â Continuous â Same as Initial load, however auto-enrolment will remain enabled. New cards created with email addresses will also be enroled in the same way. Your organisation will not need to send the Thredd API or the Cards API to enrol new cardholders.   Auto-enrolment enrols all active and Live cards. It is not recommended if you wish to exclude some cardholders from enrolment. If using Continuous auto-enrolment, this may restrict your ability to unenrol cards which currently have a live status. See [Section 8.2 Card Unenrolment.](Enrol_cards_in_3DSecure.htm#Card) |
| Time to complete authentication | Time to complete authentication in seconds. Countdown timer will be displayed in the Challenge screen. This is customisable up to 10 minutes (600 seconds) as per EMVCo requirements. The standard is 300 seconds (5 minutes).  If a fallback method is initiated, the timer will be restarted for the new authentication method. |
| DelegateSCANotification endpoint - UAT | For Out of Band and Biometric authentication, and to access the Thredd oAuth endpoint, in the UAT environment.  Your endpoint for receiving the `DelegateSCANotification` API call to start an Out of Band or Biometric authentication.  Please only supply one endpoint for the UAT environment.  Please ensure that the provided endpoint is resolving to one or set of (maximum 5) Static IP addresses. |
| DelegateSCAValidation IP Address - UAT | For Out of Band and Biometric authentication, and to access the Thredd oAuth endpoint, in the UAT environment.  Please provide your endpoint IP addresses for connection to the UAT environment. This should be no more than 5 static IP addresses. |
| DelegateSCANotification endpoint - Production | For Out of Band and Biometric authentication only in the Production environment.  Your endpoint for receiving the `DelegateSCANotification` API call to start an Out of Band or Biometric authentication.  Please only supply one endpoint for the UAT environment, and one endpoint for the Production environment.  Please ensure that the provided endpoint is resolving to one or set of (maximum 5) Static IP addresses. |
| DelegateSCAValidation IP Address - Production | For Out of Band and Biometric authentication only in the Production environment.  Please provide your endpoint IP addresses for connection to the Production environment. This should be no more than 5 static IP addresses. |
| KBA number of questions to answer | Total number of questions which the cardholder is required to answer. |
| KBA number of correct answers required | Total number of questions which the cardholder is required to answer correctly to successfully authenticate the transaction. |
| KBA number of incorrect answers permitted | Total number of questions that the cardholder may answer incorrectly before KBA is failed. |
| Number of retries allowed for OTP (Email/SMS) | The number of times that a cardholder can request for a new OTP to be resent via SMS or Email. The standard retry is 3, however this can be increased up to 5 retries. |
| Number of attempts allowed for OTP (Email/SMS) | The number of times that a cardholder can input the wrong value and still continue the process. After this the authorisation will decline and would need to be re-attempted. |
| Number of attempts allowed for KBA authentication | The number of times that a cardholder can enter the incorrect answer for each question.  We recommend you keep this at a minimum to prevent brute force attack. |
| SMS Sender ID | Text that appears as the sender of the SMS OTP (e.g., Program Manager name or Card brand).  Can be up to 11 alphanumeric characters with no spaces.  This Sender ID will be used for all SMS services. Please make sure to match this with `SMS SENDER NAME` in the core product Setup Form. |
| Email OTP sender | The "From" email address for the email OTP (i.e., from your organisation). Apata will complete the registration to send the OTP Email to your cardholders on your organisation's behalf. An authorisation email will be initiated to the email domain administrator. Authorisation will be required via the link in the email to complete the setup.  For information on setting up EMAIL OTP, see [Appendix 2: OTP Message Templates](../Reference_Apata/OTP_Message_Templates.htm).  For information on configuring the OTP email address, see [How do we set up OTP email so that the cardholder receives an email from our email domain?](../FAQs_Apata.htm) |
| Dashboard currency | Currency to be applied to the dashboard in Apata. This will apply across your card programme. |

### 5.2.4 OTP SMS Text Support

For OTP SMS messages (sent by Thredd to the cardholderâs phone number), the SMS message is dynamic, and you can specify the text and variables to use. See [Appendix 2: OTP Message Templates](../Reference_Apata/OTP_Message_Templates.htm#_Appendix_2:_OTP_1).

Please contact your Thredd 3DS project manager to ask for these SMS options to be configured.

Language is determined by checking the current value of the cardâs `language` setting (if using [Thredd API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd API consists of web services that use SOAP and the Cards API based on REST.](#), see the [Web Services Guide >Create Card](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm); if using our [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API are REST-based API that enable you to create and manage the cards in your card programme using JSON messages.](#), see the [Cards API Website > Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2)). Below is an example of the OTP SMS message, in French:

![](../Resources/Images/Cardinal/OTP_SMS_Message_Example.png)

Figure 7: OTP SMS Message Example

A single SMS message can contain up to 140 bytes of information. The number of characters which can be included in a single SMS message depends on the type of characters the message contains. Depending on the recipient's mobile carrier and device, multiple messages may be displayed as a single message, or as a sequence of separate messages. If you are looking to avoid OTP message split into multiple parts then our recommendation is to keep it brief.

Thredd uses the default English text below if no customised message is configured (provided that the merchant shares all transactional information).

[Copy](javascript:void(0);)

```
"{{OTP}} is the One Time Passcode required for completing a purchase of {{CUR}} {{Amount}} at {{MerchantName}} with the last four digits of your card ending in {{CardNumber}}." Please use the One Time Passcode to complete the transaction.
```