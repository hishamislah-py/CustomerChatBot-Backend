# Use Case Scenarios

This section provides examples of common scenarios using the Thredd web services.

* [Creating a Card](#Create)
* [Using Tokens](#Using)
* [Loading a Card](#Load)
* [Running Card Enquiries](#Card)
* [Managing Cards](#Other)
* [Renewing Expiring Cards](#Renewing)
* [Updating a Card Status to Lost, Stolen or Destroyed](#Updating)
* [Replacing a Lost, Stolen or Destroyed Card](#Replacin)
* [Registering a Cardholder for 3D Secure](#3D)
* [Using MFX Wallets](#Wallets)

## Creating a Card

Thredd provides web services to create a card, which can be either a physical or a virtual card. For a virtual card, Thredd may hold the card image or you can manage the image on your side; for a physical card some extra steps are involved in generating an XML file, which is sent to the Thredd [Card Manufacturer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd instructs existing card manufacturers (that it has relationships with) to print cards. Thredd uses Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder.
Any white label test cards are typically sent to Thredd, the Program Manager and the Card Schemes (payment networks).](#) for printing and sending to your customer. See the figure below.

![](../Resources/Images/Create_card_flow.png "Create Card Call Flow")

Figure 3: Using the Card Create web service

#### Recommended API

The API to use to create a card depends on the requirements of your application. We recommend the following:

* To create a card, use the [Card Create API](../Web_services_api/Card_Create.htm): `ws_CreateCard`. The card can be issued in a state of active or inactive:

  + If issued as inactive, it must be activated using the [Card Activate API](../Web_services_api/Card_Activate.htm): `ws_Activate`. This scenario is typical for customers who sign up for a physical card via the Internet or their mobile App.
  + If issued as active, the card can be used immediately. This scenario is typical for customers who sign up for a card via a point of sale outlet or for certain types of prepaid cards which you want your customer to be able to immediately use.
* To activate a card and load an initial balance, use the [Card Activate and Load API:](../Web_services_api/Card_Activate_and_Load.htm) `ws_Activate_Load`.

#### What to look out for:

* Card status: check to confirm the card status.
* Change the status to active if required, so that a customer can start using it. You can use the [Card Activate API](../Web_services_api/Card_Activate.htm): `Ws_Activate`. Alternatively, if you provide your customers with a phone activation service, you can use the [Phone Activation API](../Web_services_api/Card_Phone_Activation.htm): `Ws_Phone_Activation`.
* If a card is reported as lost or stolen, or you need to temporarily block the card, you can change the status of the card using the [Card Change Status API](../Web_services_api/Card_Change_Status.htm): `Ws_StatusChange`. If the card is temporarily frozen, for example, it has been reported as lost and is later found, you can reactivate it using the [Card Change Status API](../Web_services_api/Card_Change_Status.htm): `Ws_StatusChange`.
* If you deactivate a card that has been reported as destroyed or stolen, for security reasons it is not possible to reactivate. You will need to issue a new card.
* Card manufacturer fields: please check with your card manufacturer for details of the fields they are expecting. For details of supported manufacturers, see [Card Manufacturers](../Reference/Card_Manufacturers.htm).
* Address fields: make sure you populate any address fields which may be used for [AWS![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An AVS check compares the billing address used in the transaction with the issuing bankâs address information on file for that cardholder. Depending on whether they match fully, partially, or not at all, the merchant can use that information in their decision on whether or not to accept or cancel the order.
  AVS is one of the most widely used fraud prevention tools in card-not-present transactions.](#) checks.

## Using Tokens

Tokens enable you to use Thredd web services without needing to store or supply the full 16-digit card primary account number (PAN). When creating a card, Thredd always returns the `<publicToken>` linked to the physical or virtual card. When making a web service request, instead of supplying the PAN, you can include the card's `<publicToken>`, together with other mandatory information.

Thredd generates two types of tokens:

* 9-digit unique random token, linked to the PAN.
* 16-digit, formed from the 3-digit identifier, plus the 9-digit token, plus the last 4 digits of the PAN.

#### Example:

PAN = 6752993874229367

9 digit token = 734602981

16-digit token = 712+734602981+9367 = 7127346029819367

Thredd web services can receive the 9 digit public token in the request and return it in the response. Some web services may respond with the 16-digit public token. This guide will clarify when this is the case.

### Using Tokens on Mobile Devices

You can use the Mastercard Digital Enablement Service (MDES) or Visa Token Service (VTS) to manage the tokens linked to a mobile device that has been bound to a card. This is a separate Mastercard or Visa `<PaymentTokenId>` linked to the digital PAN (DPAN), and should not be confused with the Thredd `<PublicToken>` linked to the card.

You can use the following web services to manage your mobile device tokens:

* [Token Device Management](../Web_services_api/Token_Device_Management.htm): `WS_Token_Device_Management`
* [Payment Token Get](../Web_services_api/Payment_Token_Get.htm): `Ws_Payment_Token_Get`
* [Payment Token Status Change](../Web_services_api/Payment_Token_Status_Change.htm): `Ws_Payment_Token_StatusChange`

## Loading a Card

The load card web services enable you to load funds onto a card. Your [EHI mode![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) For authorisation type of transactions, the External Host Interface (EHI) can operate in one of five modes:
Gateway Processing (mode 1) the External Host maintains card balances and participates in transaction authorisation by approving or declining the transaction.
Cooperative Processing (mode 2) - Thredd maintains balances and performs all types of the authorization, but the External Host can overrule in some circumstances.
Full Service Processing (mode 3) - read-only data feed from the Thredd system to the Client's system.
Gateway Processing with STIP (mode 4) - External Host maintains Balance (with Thredd stand-in).](#) determines whether Thredd holds the card balance or you hold the balance on the card. See the example below for a client with Cooperative Processing (mode 2) or Full Service Processing (mode 3), where Thredd holds the balance.

![](../Resources/Images/Load_card_flow.png "Card Load API Flow")

Figure 4: Using the Card Load web service

When using the API, you can specify the amount to load, the load source, and other load details.

#### Recommended API

The API to use to load a card depends on the requirements of your application. We recommend the following:

* To load a card without activation, use [Card Load](../Web_services_api/Card_Load.htm): `Ws_Load`
* To load and activate a card at the same time, use [Card Activate and Load](../Web_services_api/Card_Activate_and_Load.htm): `Ws_Activate_Load`
* To unload a card (debit a specified amount or the full balance), use [Card Unload](../Web_services_api/Card_Unload.htm): `Ws_UnLoad`
* To unload a card and change the card status to inactive (e.g., customer closing an account), use [Card Unload and Change Status](../Web_services_api/Card_Unload_and_Change_Status.htm): `Ws_UnLoad_StatusChange`

#### What to look out for:

* Check card status: The load will fail if the card is flagged as invalid, lost, stolen, destroyed, expired or restricted.
* The cardholder's load limits: the load will fail if the number of load attempts or load amount exceeds the daily or period limit configured for your product.
* Load source: the load will fail if you use a load source not configured for your product (if no load sources have been set up for your product, you are able to use any load source).

## Running Card Enquiries

Thredd provides web services to enable you to check the status of the card, the available balance and other card details.

![](../Resources/Images/Card_enquiry_flow.png "Check the status of a card")

Figure 5: Using the Card Enquiry web service

#### Recommended API

The API to use to run a card enquiry depends on your requirements. We recommend the following:

* To confirm the status of a card and the available balance, use [Card Enquiry](../Web_services_api/Card_Enquiry.htm): `Ws_Enquiry`. This returns both live and archived cards.
* To confirm the status of all live cards linked to a customer, use `Ws_Customer_Enquiry` or `Ws_Customer_Enquiry_V2`. See [Customer Enquiry](../Web_services_api/Card_Customer_Enquiry.htm).

## Managing Cards

Below are examples of other common web services you can use to manage your cards:

### **PIN Control**

* To set, retrieve, unblock and change the PIN associated with a card, use [Card PIN Contro](../Web_services_api/Card_PIN_Control.htm)l: `WS_PinControl`.   
  You can also use this to unblock the [CVC2![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Card Verification Value (CVV) on a credit card or debit card is a 3 digit number on VISA, MasterCard and Discover branded credit and debit cards.
  Cardholder's are typically required to enter the CVV during any online or cardholder not present transactions.
  CVV numbers are also known as CSC numbers (Card Security Code), as well as CVV2 numbers, which are the same as CVV numbers, except that they have been generated by a 2nd generation process that makes them harder to guess.](#) of a card or mobile device token.

### Change Card Groups

You can link a card to the Thredd card groups configured for your programme (e.g. [Limit Groups![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded.
You can view your current Limit Groups in Smart Client.](#), [MCC Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#), [Fee Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group which controls the card transaction authorisation fees.](#) and [Usage Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group that controls where a card can be used. For example: POS or ATM.](#)). The group determines how the card can be used and/or the types of charges that can be applied to the card.

* To change the groups linked to a card, use [Card Change Groups (single)](../Web_services_api/Card_Change_Groups.htm): `Ws_Card_Change_Groups`
* To bulk change the groups for multiple cards, use [Card Change Groups (Bulk)](../Web_services_api/Card_Change_Groups_1.htm): `Ws_Change_Groups`

#### What to look out for:

* If you change the velocity group for a card, this may prevent the customer using their card (e.g. POS daily limit for the existing group XXX-VL-XX is 500.00, but the new group for this card, XXX-VL-YY, has a POS daily limit of 250.00).
* You must use a group that has already been configured for you in Smart Client and in Thredd Portal (based on the information provided in your [Product Setup Form![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup.
  The details are used to configure your Thredd account.](#)). For any amendments or new groups, please contact your Account Manager.
* This change is at a card level and not a product level.

### Manage Card Fees

The default fees for a card are linked to the generic Thredd product for the card, as set up for your programme. Thredd offer web service to enable you to query and apply fees to a specific card.

* To apply fees to a specific card, use the [Card Apply Fees](../Web_services_api/Card_Apply_Fees.htm) API: `Ws_Generic_Fees`
* To list pending fees due on a card, use the [Card List Pending Fees](../Web_services_api/Card_List_Pending_Fees.htm) API: `Ws_List_Pending_Fees`

## Renewing Expiring Cards

We recommend you renew expiring cards as follows:

![](../Resources/Images/Renew_cards.png "Renew cards flow")

Figure 6: Renewing Expiring Cards

1. Use the [Cards Get Expiring Soon](../Web_services_api/Cards_Get_Expiring_Soon.htm) API (`Ws_Get_Card_ExpireSoon`) to return a list of cards due to expire in the next month.
2. Renew any expiring soon cards using the [Card Renew](../Web_services_api/Card_Renew.htm) API: `Ws_Renew_Card`.

You can transfer the card balance immediately to the new card and update any linked wallet/card payment tokens at the same time.

3. Thredd returns a new Thredd public token (`<PublicToken>`) to use for any further actions or queries on the renewed card.

If renewal options 0, 1 or 8 are requested, then Thredd returns the existing Thredd public token and does not create a new card record.

4. If you are replacing the card with a physical card, then you need to activate the card. See [Card Activate](../Web_services_api/Card_Activate.htm).
5. The old expiring card record will still exist in the system; any queries using the old Thredd public token will return details of the status or balance on this record.

When replacing a card, do not use the Create Card web service, with `<Replacement>` set to 1. This is a legacy option.

We recommend you renew any physical cards well in advance of their expiry date, so that the new cards can be sent to cardholders for them to activate and use. Once a card's expiry date has passed, the cardholder will no longer be able to use the old card for payment transactions.

When replacing a card, please be aware that when the new card is activated, Thredd will change the status of the old card to *62 restricted card*.

### Extending the Expiry Date

In some circumstances you may be able to extend the Thredd expiry date of a card, using the [Card Extend Expiry Date API](../Web_services_api/Card_Extend_Expiry_Date.htm): `Ws_ExtendExpiry`

## Updating a Card Status to Lost, Stolen or Destroyed

You can use the [Card Change Status](../Web_services_api/Card_Change_Status.htm) API to update the card status to lost, stolen or destroyed.

Depending on the status being changed to, this will result in either a temporary block or a permanent block on the card.

A *Lost, Stolen* or *Destroyed* status value results in a permanent block on the card. These card statuses are irreversible. This means that the cardholder can never use the card for future purchases or withdrawals. See [Status Codes](../Reference/Status_Codes.htm).

You should be aware of the potential for some types of future transactions on a lost, stolen or destroyed card, including charges on the card. For example: authorisation declines, offline authorisations, credits, refunds, reversals and chargebacks.

#### Options for cards in an irreversible status

* Before changing the card status to an irreversible status such as *Lost, Stolen* or *Destroyed*, you can update the card's expiry date to expire the card and prevent some types of future transactions and card charges. See the [Card Extend Expiry Date](../Web_services_api/Card_Extend_Expiry_Date.htm) API.
* You can issue a replacement card using the [Card Renew](../Web_services_api/Card_Renew.htm) API. Cards with irreversible status are replaced with a new PAN number. The replacement card has the same balance as the original card.
* You can update or transfer the balance on a card in an irreversible status using the [Card Balance Transfer](../Web_services_api/Card_Balance_Transfer.htm), [Card Unload](../Web_services_api/Card_Unload.htm) or [Card Balance Update](../Web_services_api/Card_Balance_Update.htm) API.

## Replacing a Lost, Stolen or Destroyed Card

You can use the [Card Renew](../Web_services_api/Card_Renew.htm) API to replace a lost, stolen or destroyed card.

## Registering a Cardholder for 3D Secure

3D Secure (3-domain structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as âVerified by Visaâ and âMastercard SecureCodeâ respectively.

Depending on the region in which you process cards, Thredd offer a choice of [Apata![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Apata provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme. See: https://apata.com/](#) or [Cardinal Commerce![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Cardinal Commerce provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme. See: https://www.cardinalcommerce.com](#) to manage 3D enrolment and authentication. We provide web services to enable you to enrol your cardholders in the 3D Secure scheme, update and delete cardholder details.

![](../Resources/Images/3DSecure_enrol_flow.png "3D Secure enrolment")

Figure 7: Using the 3D Secure cardholder enrolment web service

#### Recommended API

* To enrol a cardholder in 3D Secure, and add, edit or delete their credentials, use [3D Secure Enrol Credentials](../Web_services_api/3D_Secure_RDX_Credentials.htm) API: `Ws_AddUpDelCredentials`

* For details of additional legacy 3D Secure web services, see [3D Secure Overview](../Web_services_api/3D_Secure_Overview.htm).

For additional information on 3D Secure support, see our [3D Secure FAQs](../FAQs.htm#3D).

The use of 3D Secure can help prevent cardholder fraud. 3D secure authentication checks are only applicable to cardholders and merchants enrolled in this scheme. For details see the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) and [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm).

## Using MFX Wallets

Thredd offers web services to enable you to create and manage eWallets. The eWallet can support multiple currencies[1 Currency support is region-specific. Please check with your account manager for support in your region.](#) and can be linked to a physical card.

* To create a wallet, use the [Wallet Create](../Web_services_api/Wallet_Create.htm) API: `Ws_CreateWallet`
* To check the balance available on the wallet, use the [Wallet Balance Enquiry](../Web_services_api/Wallet_Balance_Enquiry.htm) API: `Ws_Balance_Enquiry_Wallet`
* To regenerate the wallet (e.g. for a lost or stolen card), use the [Regenerate the Wallet](../Web_services_api/Regenerate_Wallet.htm) API: `ws_RegenerateWallet`