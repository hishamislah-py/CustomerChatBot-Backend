# 8 Managing your Programme

This section describes how you can manage tokens on the Thredd platform and at the card scheme (network).

## 8.1 Token Lifecycle Management

Managing the status of merchant tokens and device tokens via Threddâs APIs on SOAP and REST. You can make changes to the tokenised PAN directly, or in some cases Thredd will automatically amend tokenised PANs when the linked PAN is changed.

Whenever a token is updated at Thredd we also inform the Token Service Provider so that they can update their systems, and the [Token Requestor![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The token requestor initiates the request to convert your cardholderâs Permanent Account Number (PAN) into a digital token. Token requestors can be mobile wallets (such as ApplePay) or online merchants (such as Netflix). Mastercard refer to the Token Requestor as the âWallet Providerâ.](#) can accurately reflect the status of the token to cardholders. For details, see the section [Real-time Token Status Change](../References/Realtime_token_status_change.htm#_Changing_Status).

Below is the list of supported use cases and the API services you can use to implement them.

### 8.1.1 API Use Cases

* Permanent block on payments from a lost or stolen device.   
  The cardholder has reported their device is permanently unavailable and so the payment token must be removed from the device. Used for lost, stolen or sold devices.  
  See [Update Device Tokens.](#Update)
* Temporary block on payments from a device.   
  The device has been temporarily lost or the cardholder doesnât want to allow tor use for payments (for example, phone in use by a family member or when travelling abroad).  
  See [Update Device Tokens.](#Update)
* Update Merchant Tokens  
  Prevent a merchant from using their payment token (for example, for future or recurring transactions).  
   See [Update Merchant Tokens.](#Update)
* Display payment tokens in-app.   
  Show a cardholder all their payment tokens, to manage them in the app.  
  See [View all Payment Tokens.](#Show)
* Renew a card and transfer tokens.   
  Replace a physical or virtual card and ensure continuity of service for payment tokens. Used for expired, damaged or upgraded cards.  
  See [Renew a Card.](#Renew)
* Delete a card and linked tokens.   
  Close a cardholder's account or remove card functionality from their account.  
  See [Close a Card.](#Close)
* Unbind a merchant token from a device.   
  Device binding allows a merchant token to be used with fewer authentications on a trusted device. Unbinding removes this if the device should no longer be trusted.  
  See [Unbind a merchant token from a device](#Unbind).
* Register for Click to Pay (Coming Soon)  
  Add a card into Click to Pay so that the cardholder can use their card at online merchants without typing in their card details.

### 8.1.2 Status Codes to use for Card Blocks

You should use the following Thredd status codes for temporary and permanent blocks:

* Temporary Block: "57 - Transaction not permitted to cardholder" or "62 - Restricted Card"
* Permanent Block: "46 - Account Closed" or "83 - Card Destroyed"

For details of additional card status codes, see the [Cards API Website: Card Status Codes](https://cardsapidocs.thredd.com/docs/card-status-codes).

Changing the payment token to any of the permanent block statuses deletes it irreversibly. In this case, the cardholder will need to provision a new token on their device.

### 8.1.3 Update Device Tokens

Device tokens have statuses independent to the card and will need to be updated individually.

Use cases:

* Permanent block on payments from a lost or stolen device
* Temporary block on payments from a device
* Enabling a device only

Implementation:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Identify the ID for the device token. | [Get Card Payment Token](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens) | [Payment Token Get](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |
| Update the status of the payment token. | [Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status) | [Payment Token Status Change](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Status_Change.htm) |

### 8.1.4 Update Merchant Tokens

Merchant tokens (also called *Card on File* tokens) have the same status as the card, so when the cardâs status changes all merchant tokens linked to it have their status changed.

You can also change a merchant token status individually, however the next time the card status is changed the merchant token status will be aligned to the card.

Method 1: Update the card status using the public token (merchant tokens will change in sync):

| Step | REST API | SOAP API |
| --- | --- | --- |
| Update the card status. | [Card Status](https://cardsapidocs.thredd.com/docs/card-status) | [[Update Card Status](https://docs.thredd.com/webservices/Content/Web_services_api/Update_Card_Status.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |

Method 2: Update the merchant token status directly:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Identify the ID for the device token. | [Get Card Payment Token](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens) | [Payment Token Get](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |
| Update the status of the payment token. | [Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status) | [Payment Token Status Change](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Status_Change.htm) |

### 8.1.5 View all Payment Tokens

Display payment tokens linked to a Thredd public token.

Use cases:

* Display payment tokens in-app

Implementation:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Return a list of all tokens linked to the specified public token. | [Get Card Payment Token](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens) | [Payment Token Get](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |
| Return a list of devices bound to a token.  (For use on Visa (VDEP) service only.) | [Get Card Payment Token Devices](https://cardsapidocs.thredd.com/docs/get-card-payment-token-devices) | [Token Device Management](https://docs.thredd.com/webservices/Content/Web_services_api/Token_Device_Management.htm) |

Payment tokens can also be viewed in Thredd Portal or Smart Client. Refer to the [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm) or [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).

### 8.1.6 Renew a Card (Move linked Tokens)

Renewing a card using these APIs will automatically move payment tokens from the old card to the new card. In the following circumstances the DPANs will NOT be transferred, and they will be deleted when the old card is placed in an irreversible status.

Use cases:

* Deleting a card and creating a new one
* Replacing an expiring card

Implementation:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Renew or replace the card. | [[Card Renewal and Replacement](https://cardsapidocs.thredd.com/docs/card-renewal-and-replacement)](https://cardsapidocs.thredd.com/docs/card-status) | [[[Card Renew](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Renew.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Update_Card_Status.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |
| Activate the new card. | [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) | [Card Activate](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Activate.htm) |

When a card is replaced or renewed Thredd send an API to the Token Service Provider in real-time informing them of the new PAN, CVV2 and Expiry which will then be passed to the Token Requestor.

### 8.1.7 Close a Card (Delete all linked Tokens)

Closing a card will automatically delete all payment tokens, this is the only way to delete all payment tokens at once, otherwise device tokens will need to be deleted individually.

Use cases:

* Delete a card and linked tokens

Implementation:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Close the card record. | [[[Card Status](https://cardsapidocs.thredd.com/docs/card-status)](https://cardsapidocs.thredd.com/docs/card-renewal-and-replacement)](https://cardsapidocs.thredd.com/docs/card-status) | [[[[Update Card Status](https://docs.thredd.com/webservices/Content/Web_services_api/Update_Card_Status.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Renew.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Update_Card_Status.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |

### 8.1.8 Unbind a Merchant Token from a Device

Merchants can bind a token to a device so that authentication is not required on future transactions (also referred to as a *Card on File* token). If a cardholder wants to opt out or their device is stolen, then you should unbind the device so that authentication is requested again.

Implementation:

| Step | REST API | SOAP API |
| --- | --- | --- |
| Identify the Device ID(s) linked to the payment token. | [[Get Card Payment Token Devices](https://cardsapidocs.thredd.com/docs/get-card-payment-token-devices)](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens) | [[Token Device Management](https://docs.thredd.com/webservices/Content/Web_services_api/Token_Device_Management.htm)](https://docs.thredd.com/webservices/Content/Web_services_api/Payment_Token_Get.htm) |
| Unbind the device from the merchant token. | [[Unbind Payment Token](https://cardsapidocs.thredd.com/docs/unbind-payment-token)](https://cardsapidocs.thredd.com/docs/get-card-payment-token-devices) | [Token Device Management](https://docs.thredd.com/webservices/Content/Web_services_api/Token_Device_Management.htm) |

The unbind request triggers a real-time API call to the Token Service Provider. An approval action code (000) means the request has been successful on both the Thredd and Token Service Provider platforms. A failed response means that neither platform has been updated.

### 8.1.9 Response Codes (SOAP API)

When submitting a SOAP API request to change the status of a payment token, you may receive one of the following web service responses:

| Response Code | Description |
| --- | --- |
| 000 | The status change is successful on both Thredd and Token Service Provider platforms. |
| 213 | Returned if you attempt to change to a status that is not compatible with the current status. For example, this error is returned in the following scenarios:   | Current Status | Changing to | | --- | --- | | Inactive | Anything except Active | | Active | Active | | Suspended | Suspended | | Deleted | Any status | |
| 654 | Thredd received a status change request to block a payment token that is already blocked, deleted or deactivated. |
| 951 | The status change is not successful at the card scheme and only the Thredd platform has been updated. If the first attempt at a status change is unsuccessful, Thredd recommends re-attempting the status change.  If subsequent attempts at a status change continue to be unsuccessful, contact Thredd for support. |
| 953 | Occurs when Thredd were able to process the [FPANClosed Funding PAN. The true 16-digit PAN of the card, which Mastercard/Visa converts when authorisations come through to them from Acquirers on the DPAN.](#) but not the [DPANClosed Device PAN. The PAN value set up on the cardholderâs device. This is not visible to the cardholder, but is the PAN used for the transactions as far as the merchant is concerned.](#), You should follow up with a [Payment Token Status Change](https://docs.thredd.ai/webservices/Content/Web_services_api/Payment_Token_Status_Change.htm) (`Ws_Payment_Token_StatusChange`) web service request (SOAP) or use the [Update Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status) endpoint (REST). |

### 8.1.10 Response Codes (REST API)

When submitting a REST API request to change the status of a payment token, you may receive one of the following responses:

| Response Code | Description |
| --- | --- |
| 200 | The status change is successful on both Thredd and Token Service Provider platforms.  For more information on the fields returned in the response, see the [Cards API Website: Card Tokenisation](https://cardsapidocs.thredd.com/docs/introduction-to-card-tokenization). |
| 401 | Unauthorised access request |
| 404 | Resource not found |

## 8.2 Adding and Updating your Card Art

When a token is created, the token requestor may wish to display it with the correct card art to help a cardholder identify their card.

During the tokenisation process Thredd responds to the card scheme with the card profile ID linked to the card. If no card profile ID is specified in the response from Thredd, the card scheme displays your default profile (card image artwork and terms & conditions) on the cardholderâs mobile device screen. If you only have a single card product, you can use this default card profile, without requiring further updates on your end.

### 8.2.1 Adding Card Art Profiles

During the implementation process you can set up the default card art for your programme as described in the section [Token Configuration > Thredd Configuration Options > Dynamic vs. Static Card Art](Tokenisation_Configuration.htm#_Dynamic_vs._Static).

The card art that will be used is defined when the card is created, based on what is present in the `ProductRef` field (SOAP) or `designId` field (REST). This field is used for two purposes:

* When sending instructions to card manufacturers to identify the card image file in their systems to use
* To specify which card profile the card scheme (network) should use.

As a result, it is necessary to synchronise the IDs used at the card scheme and your card manufacturer.

With Mastercard you can define the card profile ID for tokenisation and Thredd recommends that you use the same card profile ID setup with your card manufacturer for image artwork.

Visa card profile IDs are generated by Visa in their Card Metadata Management (VCMM) tool. Visa returns a 32-character profile ID. This profile ID should be populated in the `ProductRef` field (SOAP) or `designId` field (REST) when creating cards and Thredd recommends that you use the same card profile ID when configuring image artwork with your card manufacturer.

There may be situations where your card manufacturer is unable to update their identifier for image artwork to use the same identifier name for the Visa Profile ID. In these cases, please contact your Thredd implementation manager to discuss options.

### 8.2.2 Updating your Card Art

You can update the Card Art ID used for future tokenisation requests by updating the card record at Thredd. This can be done two ways:

* Raise a request to Thredd to populate the card profile IDs for the existing cards in your programme (Thredd uses a batch script to update the card profile ID linked to your card products).

* Use Thredd's API to update the profile ID for each card:

  + SOAP web services â use the *Update Cardholder Details V2* web service (`Ws_Update_Cardholder_Details_V2`). You must use the `ProductRef` field to add details of the card profile ID to be used. For details, see the [Web Services Guide > Update Cardholder Details V2](https://docs.thredd.ai/webservices/Content/Web_services_api/Update_Cardholder_Details_v2.htm).
  + REST-based Cards API â use the Update Cardholder Details endpoint. You must use the `designId` field to add details of the card profile ID to be used. For details, see the [Cards API Website > Update a Card](https://cardsapidocs.thredd.com/reference/update-card).

For payment tokens that already exist, if you wish to change the card art you must use the card scheme's online portal: [Visa Card Metadata Management (VCMM)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Online tool provided by Visa to enable card issuers to add artwork and terms & conditions for use on tokenised card images. For more information, see: https://developer.visa.com/capabilities/token-service-provisioning](#) for Visa or MDES Manager for Mastercard.

### 8.2.3 Terms and Conditions

During the tokenisation process a token requestor will display the issuer's terms and conditions for the cardholder to agree to. These are configured and updated at the card scheme's online portal: [Visa Card Metadata Management (VCMM)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Online tool provided by Visa to enable card issuers to add artwork and terms & conditions for use on tokenised card images. For more information, see: https://developer.visa.com/capabilities/token-service-provisioning](#) for Visa or MDES Manager for Mastercard.