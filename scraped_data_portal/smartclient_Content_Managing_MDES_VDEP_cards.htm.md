# 12 Managing MDES/VDEP cards

This topic explains how to use Smart Client to view information about MDES- and VDEP-enabled cards and describes the different MDES and VDEP transaction processes and processing codes.

MasterCardâs Digital Enablement Service (MDES) and Visa's Digital Enablement Programme (VDEP) deliver EMV-level security for contactless and in-app payments, allowing cardholders to pay using digital wallets. The Thredd platform supports numerous digital wallets including Google Pay, Apple Pay, Samsung Pay, Garmin Pay, Fit Bit Pay, Mont Blanc Pay and Sony Pay.

MDES and VDEP work by replacing card numbers with unique payment tokens which differ to Thredd Tokens. Tokens are placed into digital environments (a mobile wallet). During a transaction, the process maps tokens to underlying card numbers (FPAN) cryptographically and acts as a centralised hub connecting the Issuer with Digital Wallet Providers such as Apple, Google, and Samsung. This enables connected devices to make purchases in-store, in-app or online.

![Tokenisation flow](Resources/Images/Token_participants.png)

Figure 81:  Parties involved in the MDES/VDEP tokenisation flow

MDES/VDEP validates the transaction, maps from the token back to the PAN, and forwards it to the issuer for authorisation.

For more information about tokenisation (digital wallets), token provisioning and use cases, see the *Thredd Tokenisation Service Guide*.

## 12.1 Identifying MDES and VDEP-enabled Cards

To identify whether a card has any MDES/VDEP payment-tokens on it, see [Viewing Payment Tokens.](Viewing_Card_Details.htm#Viewing2)

To identify whether a transaction is on an MDES/VDEP payment token, see the device information in the bottom left of the **View Transaction Details** screen. See [Locating Device Token Data](#Locating)

To identify a transaction from Visa/Mastercard used to create a new payment-token, see [About the processing codes](#About), and look for processing codes: â330000â (Tokenisation Authorisation Request), â340000â (Activation Code (to activate a new payment-token) Notification), and â350000â (Tokenisation Complete Notification).

## 12.2 About the Transaction Process

This section describes the main MDES and VDEP transaction processes and processing codes you will see within Smart Client. For a detailed description of these, see the *Thredd Tokenisation Service Guide*.

### 12.2.1 VDEP transaction process

The main VDEP transaction processing codes are identified using the codes 33, 36 and 35 (which do not always follow in order):

* Token Authentication Request (TAR) â 330000
* Token Event Notification (TEN) â 360000
* Tokenisation Complete Notification (TCN) â 350000

  ![](Resources/Images/Managing_MDES_VDEP_cards_1.png)

  Figure 82:  Tokenisation Complete Notification ,Token Event Notification, and Token Authentication in the View Transactions screen

### 12.2.2 MDES transaction process

The main MDES transaction processing codes are identified using the codes 33, 34, 35 and 36 (which do not always follow in order). For example, the following shows the stages involved in registering a device via Apple Pay:

* Token Authentication Request (TAR) â 330000
* Activation Code Notification (ACN) â 340000
* Tokenisation Complete Notification (TCN) â 350000
* Debit goods and services (000000 â AVS Check)

  ![](Resources/Images/Managing_MDES_VDEP_cards_2.png)

  Figure 83:  Debit (goods and services), Tokenisation Complete Notification , and Token Authentication in the View Transactions screen

### 12.2.3 About the processing codes

#### Token Authentication Request (TAR) â 330000

The Tokenisation Authentication Request (TAR) allows Thredd to provide a realtime decision as to whether the token service provider (MDES/VDEP) can digitize a card and designate a token on their behalf.

![](Resources/Images/Managing_MDES_VDEP_cards_3.png)

Figure 84:  Card activation notification in realtime on a mobile device.

![](Resources/Images/Managing_MDES_VDEP_cards_4_1191x26.png)

Figure 85: Token Authentication in the View Transactions screen

#### Activation Code Notification (ACN) â 340000

This is received by Thredd from Mastercard and contains the Activation Code Notification (ACN) message. This signals Thredd to provide the cardholder with an authentication code as a second means of Authentication. Depending on setup, these Activation codes are sent via SMS by Thredd, or provided via EHI message to indicate One Time Passcode (OTP).

![](Resources/Images/Managing_MDES_VDEP_cards_5_1296x20.png)

Figure 86: Activation Code Notification in the View Transactions screen

#### Tokenisation Complete Notification (TCN) â 350000

This the final step in the digitisation process to confirm the setup of the token was successful.

![](Resources/Images/Managing_MDES_VDEP_cards_6.png)

Figure 87:  Card ready for use notification on a mobile device.

This message, constructed in a similar format to the previous MDES/VDEP messages, contains all the details of the tokenisation (digital wallets) including, but not limited to:

![](Resources/Images/Managing_MDES_VDEP_cards_7_1323x18.png)

Figure 88: Tokenisation Complete Notification in the View Transactions screen

#### Token Event Notification (TEN) â 360000

This notification is part of the post-digitisation flow, this informs the issuer of unsuccessful Activation Code entry attempts and subsequent invalidation of an Activation Code or when a token is suspended, resumed or deactivated.

## 12.3 Finding MDES/VDEP Data on Smart Client

A payment token, also known as a DPAN (or Device PAN), is a new digital PAN created by Mastercard or Visa and placed on a device which is then linked to the original issuer PAN. A DPAN is the byproduct of Tokenisation Completion (TCN) which Thredd references as the `<Payment_Token>`.

### 12.3.1 Locating Device Token Data

To find information about the device token in Smart Client:

1. Select an Authorisation in the **View Transactions** screen and right-click.
2. Select **More details** > **View Transaction Details** to display the **Transaction Details** screen.

   ![](Resources/Images/MDES_VDEP_TXN_Details_no_PAN_506x390.png)

   Figure 89:  Device Token field on the View Transactions screen
3. Expand the arrow next to **Device Token** (bottom left). Device token details are displayed.

   Depending on how your product is set up, the status of the physical/virtual card is taken into consideration during the authorisation process. For example, the card status may be ignored, or if the card status is anything other than 00 (All Good), the authorisation is declined.

### 12.3.2 Locating MDES/VDEP Device Status

Using Smart Client, you can identify how many devices a token has been registered to and the status of the wallet on each of those devices. You can also update the status of the token.

To find information about the device status:

1. Select an Authorisation in the **View Transactions** screen, right-click and select **More details** > **Card Details, inc Fees**.
2. **Form Factor** shows the type of device being used for the wallet (for example, a mobile phone, tablet, or watch).
3. The colour indicates whether the device is active, inactive, or not tokenised (cancellation). The colours are explained in the key at the bottom of the screen.

   ![](Resources/Images/MDES_VDEP_payment_tokens_616x387.png)

   Figure 90:  Device Tokens in the Card Master screen
4. Double-click a green entry to open the Payment Token. Information like the following is shown:

   ![](Resources/Images/Locating_MDES_VDEP.JPG)

   Figure 91:  Payment Token screen
5. Update the token status if necessary.

## 12.4 MDES/VDEP EHI Considerations

MDES messages are also sent through the Thredd Authorisation system and are processed as transactions and sent through EHI (External Host Interface). The attributes remain unchanged, such as:

* MTID = 0100
* Txn\_Type = A
* Transaction Amount = 00

For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.com/EHI_Guide.htm).

## 12.5 Using MDES/VDEP API

Thredd offers a number of APIs relating to MDES/VDEP:

| Using SOAP Web Services API | Using the REST-based Cards API |
| --- | --- |
| * [Payment Token Status Change](https://docs.thredd.ai/webservices/Content/Web_services_api/Payment_Token_Status_Change.htm) â use this to change the status of an MDES and VDEP Payment Token Card. * [Payment Token Get](https://docs.thredd.ai/webservices/Content/Web_services_api/Payment_Token_Get.htm) â use this to get the details for MDES Payment Token Cards.   For more information, see the [Web Services Guide](https://docs.thredd.com/Web_Services_Guide.htm). | * [Update Payment Token Status](https://cardsapidocs.thredd.com/docs/update-payment-token-status) â use this to change the status of an MDES and VDEP Payment Token Card. * [Get Card Payment Token](https://cardsapidocs.thredd.com/docs/get-card-payment-tokens) â use this to get the details for MDES Payment Token Cards.   For more information, see the [Cards API Website](https://cardsapidocs.thredd.com/). |