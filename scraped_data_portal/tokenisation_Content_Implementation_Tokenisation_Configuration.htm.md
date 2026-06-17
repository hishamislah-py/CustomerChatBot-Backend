# 5 Tokenisation Configuration

This section provides details of the Thredd configuration options related to the tokenisation service.

## 5.1 Configuring Token Sub-Bin Ranges

For Program Managers implementing tokenisation on sub-BIN ranges, please note the restrictions in this section.

Visa systems can only support tokenising sub-BIN ranges split down to the 9th digit for Card on file (COF) and mobile wallet token requestors (such as ApplePay and GooglePay). If a Visa BIN is to be used for EU cross-border issuance and tokenisation, then only 10 countries can be used on that BIN before a new BIN is needed.

Mastercard and Thredd systems can support tokenisation down to the 10th digit of the sub-BIN range.

## 5.2 Card Usage Groups

If you are supporting tokenisation on your physical and virtual cards, please ensure that **Card Not Present (Manual Key Entry)** is enabled on your Card Usage Groups to allow your cards to be tokenised. You can specify this on the Thredd Product Setup Form (PSF). See the example below.

![](../Resources/Images/Card_Usage_Product_Setup_Form.png)

Figure 10: Card Usage Groups on the PSF

## 5.3 Payment Token Usage Groups

To configure your tokenisation usage groups, you need to fill in the Digital Wallet Product Set Up Form (PSF) and return to your Implementation Manager.  The key configuration options, specific to the provisioning of a payment token, are found under two groups:

* Payment Token Usage Group: these are your default settings for all Token Requestors
* Payment Token Usage Wallet Groups: these are settings for specific Token Requestors (e.g., for Android and Apple)

To enable the payment token service, you will need at least one payment token usage group, which is set as the default group at a product level. See the example below.

![](../Resources/Images/Payment_token_usage_group_psf.png)

Figure 11: Payment Token Usage Group

You then need to set up a payment token usage wallet group for each Token Requestor. See the example in [Figure 12](#Payment2) below.

Note that all [COF Token Requestors![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Online Merchant Token Requestors are referred to as Card on File (COF) Token Requestors. These are merchants who tokenise a payment card so that the token can be used for repeat payments or recurring payments on their website.](#) are grouped into one payment token usage wallet group for ease of configuration.

![](../Resources/Images/Payment_token_usage_wallet_group_psf.png)

Figure 12: Payment Token Wallet Usage Group

For details of the fields in the Digital Wallet Product Set Up Form, see [Thredd Configuration Options](#_GPS_Configuration_Options).

## 5.4 Thredd Configuration Options

The following table describes the available tokenisation service configuration options.

Settings in the Payment Token Usage Group apply for all Token Requestors, while settings in the Payment Token Wallet apply to individual Token Requestors (for example, Wallet Decision Auth).

Online Merchant Token Requestors are provided as a single group (called MRCHTOKEN), so you cannot set different token logic for individual online merchant token requestors.[1  MRCHTOKEN is also referred to as M4M (by Mastercard) and Card on File (by Visa).](#)

| Parameter | Function | Suggestions |
| --- | --- | --- |
| General Options | | |
| Group Usage | The default usage group that should be assigned to the wallet.  (set at Payment Token Usage Group level) | If you want any different functionality for transactions on payment tokens than your existing physical or virtual cards, then specify a different usage group here to be used just for tokens. (For example, to prevent payment tokens to be used for ATMs with NFC enabled, or tokens to be used overseas.) |
| Artwork | The reference that Thredd should return to Visa/Mastercard for T&Cs and card art. | For Static card art: Leave blank (for Visa) or add a Mastercard reference.  For Dynamic card art: Leave blank. |
| Dynamic | Whether the artwork is dynamic  For details, see [Dynamic vs. Static Card Art](#_Dynamic_vs._Static) | If dynamic, select Yes. When you send Thredd a create card request (using the Thredd API) Thredd will pass the contents of the `ProductRef` field (SOAP web services) or the `designId` field (REST-based Cards API) to Visa/Mastercard. |
| Options for responding to a TAR request | | |
| Default Decision | The default response that Thredd should provide when a TAR arrives. | Set to approve if you have scenarios where you want to approve a TAR without authentication.[2 Not applicable for Push Provisioning. Please see the setting for âOverride approve-with-auth to Approve for in app provisioningâ for further information on how to correctly set up push provisioning for Wallet Provider testing](#)  If you always want to authenticate the cardholder then set to authenticate.  Set to decline if you are setting up a decline-only group. These groups are used to prevent individual cardholders from using the token service. |
| CVV2 Missing | The response code that Thredd should return if the [CVV2Closed The Card Verification Value (CVV) on a credit card or debit card is a 3 digit number on VISA, MasterCard and Discover branded credit and debit cards. Cardholder's are typically required to enter the CVV during any online or cardholder not present transactions. CVV numbers are also known as CSC numbers (Card Security Code), as well as CVV2 numbers, which are the same as CVV numbers, except that they have been generated by a 2nd generation process that makes them harder to guess.](#) is missing from the TAR. | For Mobile Wallet tokenisation, set to approve or authenticate depending on your risk appetite.  For the [MRCHTOKENClosed Thredd name for the Wallet Provider group, representing Online Merchant Token Requestors. Also referred to as M4M (by Mastercard) and Card on File (by Visa).](#) wallet provider, this should be set to approve.  Online merchant token activation requests must not decline for missing CVV2. |
| AVS Missing | The response code that Thredd returns if address data is missing from the TAR. | For Online Merchant tokenisation, this should be set to approve.  For Mobile Wallet tokenisation, set to approve or authenticate depending on your risk appetite. |
| Wallet Decision Auth | The action Thredd should take if the incoming TAR from the token requestor recommends authenticate cardholder. | Set to approve or authenticate depending on your risk appetite. |
| Wallet Decision Decline | The action Thredd should take if the incoming TAR from the token requestor recommends decline. | Set to Approve, Authenticate or Decline depending on your risk appetite and the cardholder journey requirements. |
| Wallet and Device Scoring | | |
| Wallet Device Score Default | The default score that Thredd should assign if there is no device score on the incoming TAR. | These scores are often missing (since many Token requestors do not provide a score).  The default is 3, but you can set a higher or lower threshold, depending on your risk appetite. See [Wallet Device and Account Scoring](#_Wallet_and_Device). |
| Wallet Account Score Default | The default score that Thredd should assign if there is no account score on the incoming TAR. | These scores are often missing if the Token requestor is not Apple.  The default is 3, but you can set a higher or lower threshold, depending on your risk appetite. |
| Wallet Device Score Max Auth | The maximum device score required to trigger the Authenticate flow.  Device scores are between 1 and 5. | The default is 3, but you can set a higher or lower threshold, depending on your risk appetite. See [Wallet Device and Account Scoring](#_Wallet_and_Device). |
| Wallet Device Score Max Decline | The maximum device score required to trigger a Decline. Device scores are between 1 and 5. | Default is set to 1.  Note that during internal pilots if you are adding and removing cards multiple times from Apple, the score may get low enough to cause declines. |
| Wallet Account Score Max Auth | The maximum wallet score to trigger the Authenticate flow. Wallet scores are between 1 and 5. | Usually set to 3 but you can set higher or lower threshold depending on your risk appetite. |
| Wallet account Score Max Decline | The maximum device score to trigger a Decline.  Device scores are between 1 and 5. | Usually set to 1.  However, during internal pilots if you are adding and removing cards multiple times from Apple the score may get low enough to cause declines. |
| Token frequency and overrides | | |
| Min. Tokens to Auth | The number of tokens permitted before Thredd requests authentication.  (set at Payment Token Usage Group level) | The number of existing tokens is specified in the incoming TAR request from the Token Service Provider. |
| Min. Tokens to Decline | The number of tokens permitted before Thredd declines further requests.  (set at Payment Token Usage Group level only) | The number of existing tokens is specified in the incoming TAR request from the Token Service Provider. |
| Override-with-auth to Approve for in-app provisioning | Thredd can identify TARs where push provisioning has been used.  In these requests the cardholder has already been authenticated so this option allows you to prevent a request for further authentication to be sent. | Always set Override Enabled for a better customer journey. If it is not enabled the cardholders will often need to authenticate twice.  The override is required to pass Apple testing. |
| Default Wallet Provider Authentication | This relates to authentication on the payment token/DPAN. [PSD2Closed Payment Service Directive 2. PSD2 is an EU Directive which sets requirements for firms that provide payment services. It aims to improve consumer protection, make payments safer and more secure, and drive down the costs of payment services.](#) requires cardholder authentication when:   * The transaction amount is over 50 EUR \* * The cumulative non-SCA value exceeds 150 EUR\* * More than five consecutive non-SCA transactions have been processed   \* The amount/value is configurable per client and currency    **Note**: The Wallet provider should always handle the authentication and update the [countersClosed A counter under the PSD2 rules is used to track the number of transactions and cumulative amount before the cardholder is requested to authenticate using Strong Customer Authentication (SCA): for example, via PIN for a card or via 3D Secure authentication for an online transaction.](#). | Options include:   * **Authenticated** â the payment token/wallet always does implicit cardholder authentication for each transaction performed on it. * **Not authenticated** â no implicit cardholder authentication happens for transactions. (If PSD2 is enabled, then Thredd will track both contactless and e-commerce [countersClosed A counter under the PSD2 rules is used to track the number of transactions and cumulative amount before the cardholder is requested to authenticate using Strong Customer Authentication (SCA): for example, via PIN for a card or via 3D Secure authentication for an online transaction.](#), and will request SCA if these limits are exceeded.) (This option can be set for an online merchant.) * **Do not apply PSD counters** â the payment token/wallet does the PSD2 checking, and Thredd should not do any PSD2 checking for transactions. (This option should always be set for Mastercard. It is also recommended for Visa.)[3 For Mastercard, Thredd do not receive the full authentication data to support this option. We also highly   recommend you do not enable for Visa as this may lead to a poor customer journey (where the token is declined   and the terminal prompts to insert a card).](#)     **Note**: PSD2 counters for physical cards is not affected by this setting. SCA counters for physical cards are a separate configuration parameter. |
| Options for cardholder authentication and token activation | | |
| Activate: Call Centre Tel Number | The number to call if you want cardholders to be able to telephone a call centre to activate their payment token. | Leave blank for no call centre, otherwise enter the phone number that Thredd should return to the token service provider. If you need different call centre numbers for different groups of cardholders, please set up a Payment Token Usage group for each number.    **Note**: Your call centre staff can view the One-time passcode (OTP) required for activation in Smart Client. The OTP is also available via EHI or Thredd API. |
| Activate: Mobile App Reference | The name that the Wallet provider refers to your app as, and is displayed to the cardholder. | The name of the client that appears in the Apple or Google Pay app. This depends on your app build. Leave blank for no mobile app, otherwise enter the reference that Thredd returns to the token service provider. |
| App Source Address | The identifier that the network can use to tell the Wallet which app to send the cardholder to for verification. | * **For Apple Wallet**: Use the Adam ID of your app in the format of a string of 10 numbers. This must match the Adam ID added in MDES Manager. It can also be found by copying the numbers at the end of the clients app's App Store URL. For example, if the URL is https://apps.apple.com/app/id1195168544, the Adam ID is 1195168544. * **For Google Wallet**: Use the package name of the issuer's mobile app which is added in MDES Manager. For example: com.mybank.bankingap |
| Activate: Website URL | URL cardholders use to retrieve an OTP. | Enter the website URL you want cardholders to go to for their OTP. |
| Activate Email | Whether to activate email as an OTP delivery option | This option is required if you want email to be returned to the cardholder as an option for authentication; note that Thredd will not send the email directly to the cardholder and your systems will need to implement this:  you can retrieve the OTP from EHI and handle with your own messaging and branding.  If you are interested in Thredd sending emails directly, please raise with your Account Manager. |
| Activate SMS | Whether to activate SMS as an OTP delivery option. | If you want to send your own SMS, then enable this parameter, but do not configure a message. |
| Activate Call-back | Whether to activate call-back as an OTP delivery option | Thredd does not handle call-backs directly with a cardholder. If you want to provide this option, then your systems will need to retrieve the OTP from EHI and call your cardholder directly. |
| Token complete notification options | | |
| Notify SMS | Whether you want Thredd to confirm via SMS to a cardholder that tokenisation is complete | Enable if required. |

For Thredd to return an Approve response code for a TAR (Green flow), all checks based on configuration and card must be approved. If only one check returns an authentication decision, then Thredd will request authentication (yellow flow)[4  Excludes authentication for push-provisioned token requests, which only allow approve or decline responses.](#); if only one check triggers a decline then Thredd will decline (red flow).

### 5.4.1 Enabling Different Configuration Options per Card

Thredd provide the option to create multiple [Payment Token Usage Wallet Groups](#_Card_Usage_Groups) and have different authentication options at a card level for different cards or card products. The Thredd Implementation Team set up these usage groups.

Below are some examples of why multiple Payment Token Wallet Usage Groups are used:

* To prevent individual cards from being tokenised, you can set up a âdecline onlyâ group (often done for fraud purposes).
* To set up different notification options such as different call centre numbers or to exclude SMS options from some clients.
* To set up different usage roles for tokenised cards, for example exclude MOTO payments or magnetic stripe card payments.
* To have different limits on the numbers of tokens that can be created before authentication and/or decline responses are sent.

#### How to change a cardâs usage group

All token service products have a default Payment Token Usage Group. To change a cardâs usage group using the Thredd API:

| Using Web Services (SOAP) | Using Cards API (REST) |
| --- | --- |
| * When creating the card, use the `Ws_CreateCard` or when changing a cardâs usage group at a later time, use the `Ws_Change_Groups` web service. * Enter the unique identifier into the `<PaymentTokenUsageGroup>` field.   For more information, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm). | * When creating the card, using the [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) endpoint, the default usage groups for the card product are linked to the card * You can use the [Update Card Controls Group](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) endpoint to change the cardâs usage group   For more information, see the [Cards API Website > Managing Card Control Groups](https://cardsapidocs.thredd.com/docs/card-controls). |

It is also possible to change a cardâs usage group using Thredd Portal or Smart Client. For more information, see the [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm), or the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).

### 5.4.2 Dynamic vs. Static Card Art

There are two options to configure the card art that is displayed to the cardholder at the time of tokenisation:

* Static - the same artwork for the whole account range.
* Dynamic - artwork can vary at card level.

Configuration of artwork differs slightly between Visa and Mastercard.

#### Visa Configuration

You will need to configure your static card art per account range on the Visa Cardholder Metadata Manager (VCMM) online portal.

* To configure dynamic artwork, you must upload your card art options to VCMM against a `ProfileID`. The `ProfileID` is always 32 characters long.
* When you create a card using the Thredd API, you must enter this Profile ID into the `ProductRef` field (SOAP [Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm) web service) or the `designId` field (REST [Create Card](https://cardsapidocs.thredd.com/docs/create-card-2) API).

#### Mastercard Configuration

Upload your artwork to the MDES Manager. Use the same product reference for your artwork as is used by your Card Manufacturer.

For static artwork, Thredd take the reference from your payment token wallet usage group. For dynamic artwork, Thredd take the reference from the `ProductRef` field (SOAP) or `designId` field (REST).

the card art reference (`ProductRef` field for SOAP web services or `designId` field for REST-based Cards API) should be the same for both Visa/Mastercard and your Card Manufacturer.

### 5.4.3 Wallet Device and Account Scores

These scores are returned from [Mobile Wallet Token Requestors![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A token requestor connected to a mobile device.](#) such as Apple Pay, to reflect how trustworthy they consider the account and device. Scores are between 1-5. The higher the score, the more reliable the account or device is considered to be. 1 = least trusted, and 5 = most trustworthy.

You can use this score to determine how you want Thredd to respond to the Token Activation Request (TAR).

#### Example Thredd Settings

What is the maximum number which triggers approve with authentication (yellow flow)?  
Wallet Device Score Max Auth = 3

What is the maximum number which triggers a decline (red flow)?  
Wallet Device Score Max Decline = 1

If a device score of 4 is received, then Thredd approves.  If a device score of 3 is received, then Thredd approves with authentication. If a device score of 1 is received, then Thredd declines.

### 5.4.4 Default Device and Account Scores

Some wallet providers do not return any device or account scores. In this case, you can configure Thredd to assign a default score that can be used in the Token Activation Request to determine how you want Thredd to respond to the Token Activation Request.

### 5.4.5 Device Binding Logic

[Device binding requests](../Getting_Started/How_Tokenisation_Works.htm#_Visa_Cloud_Token) follow a specific logic based on Visaâs best practice and mandates regarding how Thredd can process them so these settings cannot be changed. The processing flow is dependent on the reason code as follows:

* 3740 (Device binding request) â Always requests authentication
* 3749 (Device binding with FIDO intent) â Always requests authentication
* 3760 (Device binding â implicit green flow) â Always approval

Currently, Thredd device binding requests use the same authorisation logic as the Online Merchant token activation requests. If you want different authorisation logic between Online Merchant Token requests and Device Binding Requests, please raise with your Account Manager.

### 5.4.6 DPAN over FPAN Status

DPAN over FPAN status is an optional setting that specifies how Thredd should treat the Digital PAN (DPAN) and Financial PAN (FPAN) statuses during DPAN transactions:

* If DPAN over FPAN status is ENABLED â Thredd will check the DPAN status during a token transaction and disregard the underlying FPAN status
* If DPAN over FPAN status is DISABLED â Thredd will check BOTH the FPAN and DPAN statuses during token transactions

The default setting is disabled. To enable this setting, please raise a change request or speak to your Thredd Implementation Manager.

We recommend that DPAN over FPAN status should not be enabled for [Card on File token requestors![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Online Merchant Token Requestors are referred to as Card on File (COF) Token Requestors. These are merchants who tokenise a payment card so that the token can be used for repeat payments or recurring payments on their website.](#). This should only be used for device-based tokens through wallet providers such as Apple and Android.

#### Changing the Token Status

The interaction between the card status and the payment token status depends on the type of payment token.

| Payment Token Type | Authorisation Behaviour | Card Status Change |
| --- | --- | --- |
| Wallet (for example, Apple Wallet or Google Wallet). | Authorisation response is determined by the status of the Wallet token being used. | Wallet token status is independent from the card status. |

You can use the following Thredd APIs to change the status of your cards:

| Using Web Services (SOAP) | Using Cards API (REST) |
| --- | --- |
| * `Ws_StatusChange` â changes the status of a card (the FPAN status) * `Ws_PaymentToken_StatusChange` â changes the status of a digital payment token (the DPAN status)   Note that the card status is changed in both web services using the `<NewStatCode>` field. For more information, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm). | * [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) - changes the status of a card (the FPAN status) * [Update Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status)  â changes the status of a digital payment token (the DPAN status)   For more information, see the [Cards API Website](https://cardsapidocs.thredd.com/). |

#### Impact on token transactions

If the DPAN over FPAN setting is enabled, then you must separately set the statuses of both the FPAN and DPAN using the Thredd API. See [Changing the FPAN and DPAN status](#Changing).

If the DPAN over FPAN setting is disabled, then the DPAN status can be overridden in an authorisation by the FPAN status (as set using the Thredd API).  This allows you to control the status used for authorisation using a single API.

Do not use status code 41 if temporarily blocking a DPAN, since the Card Schemes (Networks) treat this as a permanent status. We recommend you use status code G1 instead, as this status is reversible.

## 5.5 Exchange of Keys

### 5.5.1 Visa Keys

Visa and Thredd exchange the following keys as part of the Visa Token service project. A set of Visa keys are unique per Bank Identification Number ([BIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first four or six numbers on a payment card, which identifies the institution that issues the card.](#)).

* Master Derivation Key (MDK) â used to validate chip cards. This key is per [BIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first four or six numbers on a payment card, which identifies the institution that issues the card.](#) and this process is the same as the key exchange for Visa STIP processing. Sharing the existing MDK with Visa is optional, as they can create a new one for tokenisation. Thredd can support either option.
* XPay Shared Secret (or HMAC key) â this is used by Visa to validate Visa inbound APIs that are sent by Thredd. This is shared per issuer via the Visa Developer Portal.
* XPay API Key â this is added to the URL by Thredd for Lifecycle Maintenance (outbound) APIs. This is shared per issuer via the Visa Developer Portal.
* JWE/JWS certificates â Private/Public key pairs used to sign or encrypt sensitive data within the APIs. The public certificates of these keys will be shared between Thredd and Visa during the implementation project.
* Key Identifier (KID) â Visa provides Thredd with the Key Identifier (KID) they assign to the Thredd JWE for Visa outbound APIs.
* Push Provisioning Shared Secret (or HMAC key) â this is used by Visa to validate Visa inbound payloads that are sent by Thredd. This is shared per issuer via the Visa Developer Portal.
* Push Provisioning API Key â this is added to the URL by Thredd for Push Provisioning payloads.  This is shared per issuer via the Visa Developer Portal.
* Apple Web Services Key (WSDK) â This is used by Visa to validate Visa inbound payloads that are sent by Thredd. This key is already configured at Thredd and so does not need to be requested in a VTS project.

### 5.5.2 Mastercard Keys

The following keys are exchanged between Mastercard and Thredd.

* RSA Public key for TAV requests (Apple and Google) - This key is already configured at Thredd and so does not need to be requested in an MDES project
* RSA 2048-bit Public Key (Google) - A separate key is needed for each issuer who is onboarded. Mastercard need to share this with Thredd via the key management team email

## 5.6 Event Notifications

During token provisioning and status updates, Thredd receive multiple messages from the network. These can be sent to you through two routes: Webhooks or External Host Interface (EHI). The table below explains the events we can notify you about.

| Message Type | EHI Processing Code | Webhook Event Code | Function | Usage |
| --- | --- | --- | --- | --- |
| Token Activation Request (TAR) | 330000 | 106 | Request for a new token. | Counting token requests for reporting to the wallets.  Identifying Orange flow requests (Webhooks only). |
| Activation Code Notification (ACN) | 340000 | 107 | Contains the OTP delivery message. | Client delivery of the OTP through a secure channel. |
| Token Complete Notification (TCN) | 350000 | 108 | Token created. | Counting successful token requests for reporting to the wallets.  Confirm that the network has finished the tokenisation flow. |
| Token Event Notification (TEN) | 360000 | 109 | Token event notification (including activation). | Logging the status of a token to give cardholder correct options and information in the mobile app or website. |
| TLCM Failure Notification (Webhooks only) |  | 110 | Thredd was unable to update MDES or VTS with a DPANs new status. | Retrying any status changes that were not successfully processed by the Token Service Provider. |

### 5.6.1 Webhooks

To receive tokenisation event notifications using Webhooks you can self-serve by using our Webhooks APIs. Using Webhooks, you can opt in to the message types that you want to receive.

You can utilise its REST API to create and update webhook endpoints, and specifying desired events for notification for the endpoints. Additionally, clients can retrieve historical or missed events on demand, update their details, and manage event subscriptions. Webhooks provide a robust platform for efficient event-driven interactions, retrieving notification details, subscribing to events, and re-sending notifications.

The advantage of webhooks is that there is no persistent open connection to the system where you need to keep filtering for events that you are interested in. It is an asynchronous mechanism where you wait for the system to notify you. The HTTP payload will contain the details of the event.

Before using webhooks, you will need to setup a URL that can listen for any alerts. Contact the Thredd Application Support Team for help with this as your IP address must be whitelisted first. When the URL has been set up correctly, it must be registered using the Create Webhook endpoint.

For details of the Webhook message fields related to tokenisation, see Introduction to [Tokenisation Event Notifications](https://cardsapidocs.thredd.com/v2.0/docs/introduction-to-tokenisation-event-notifications#/).

### 5.6.2 EHI

You can receive tokenisation messages using Thredd's External Host Interface (EHI). To do so, in your Product Setup Form (PSF), tick the option to enable TAR transaction types. This sends all available token event notifications through the EHI (TAR, ACN, TCN, TEN). For more information, see the [EHI Guides](https://docs.thredd.com/EHI_Guides.htm).

For details of the EHI message fields related to tokenisation see [EHI Tokenisation Fields](../References/EHI_Tokenisation.htm).