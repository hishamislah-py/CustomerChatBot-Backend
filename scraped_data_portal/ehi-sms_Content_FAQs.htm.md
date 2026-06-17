# General FAQs

This section provides answers to frequently asked questions. It is divided into the following sections:

* [EHI Setup](#EHI)

* [EHI Modes](#EHI2)
* [Duplicate Checking and Transaction Matching](#Duplicat)
* [EHI Cut Off Messages](#EHI3)
* [Transaction Processing](#Transact3)
* [Transaction Lifecycle](#Transact)
* [Transaction Life](#Transact2)c[ycle - Single Message Systems](#Transact2)
* [Single Message System](#Single)

## EHI Setup

#### Q. How do I change my EHI configuration?

Please discuss changes with your implementation manager or account manager.

#### Q. Can I use a private IP in the Test Environment?

A private IP is used internally within your own network and will require a secure connection for EHI to access. In the test environment Thredd recommends the EHI connection resolves to a public IP.

In the test environment Thredd recommends the EHI connection resolves to a public IP using Thredd's Secure Connectivity framework. However, you can use a private IP internally within your own network, which also uses the Thredd's Secure Connectivity framework. For more information, see the [Connecting to Thredd Guide](https://docs.thredd.ai/Connecting_to_Thredd_Guide.htm).

## EHI Setup and Modes

#### Q. Which EHI mode should I choose?

Thredd offers four EHI setup options (modes), which are configured when your account is set up on the Thredd platform.

You should select your EHI mode based on how you want the balance on the cards in your programme to be held and how you want to handle payment authorisation transactions:

* Gateway Processing (mode 1) is used where you want full to control the card balance and authorisation process
* Cooperative Processing (mode 2) offers flexible scenarios where Thredd maintains the balance and performs authorisation, but you can override an approval decision.
* Full Service Processing (mode 3) is used where you want Thredd to control the card balance and authorisation process
* Gateway Processing with STIP (mode 4) is similar to Gateway Processing (mode 1), but offers Thredd Stand-in processing if your systems are unavailable.

For more information, see [EHI Operating Modes](Getting_Started/EHI_operating_modes.htm).

#### Q. Can I be on more than one EHI mode?

You can only choose one EHI mode per product.

#### Q. Can I change my EHI mode?

Yes. The following are typical reasons why you may decide to change your EHI mode at a later stage:

* You started using Full Service Processing (mode 3) for convenience and to launch your service quickly, but later decide to maintain your own card balance ledger and payment authorisation process. In this case, you could switch to Gateway Processing (mode 1) or Gateway Processing with STIP (mode 4).
* You started using Gateway Processing (mode 1), but have been experiencing persistent processing issues and timeouts on your end, so decide to switch to one of the EHI options that provide Thredd stand-in processing (STIP) when your systems are unavailable. For example: Gateway Processing with STIP (mode 4).

For more information, see [EHI Operating Modes](Getting_Started/EHI_operating_modes.htm).

#### Q. How do I change my EHI mode?

To change your EHI mode, please contact your Account Manager.

Your Account Manager will need to fully assess and cost any changes to your EHI mode.

Changing your EHI mode may require changes to the way in which Thredd and your external host systems maintain the card balance and respond to authorisation requests. It may also require other EHI configuration changes and testing.

## Duplicate Checking and Transaction Matching

#### Q. What is duplicate checking and how can I ensure a message is unique?

EHI is designed to resend messages if a successful acknowledgement is not received by Thredd. Even if you respond with a valid acknowledgement, due to network issues, this may not be received by Thredd, in which case Thredd resends the message. This ultimately means that any message can be received through EHI more than once. You must ensure that accounts are not debited or credited multiple times due to duplicate messages.

Duplicate checking must be performed for any new message received through EHI. You can use the transaction ID (`Txn_ID`) field to check the uniqueness of a transaction in EHI.

#### Q. What is transaction matching and how should I perform this?

You are likely to receive multiple linked messages for a card payment transaction throughout its lifecycle (for example, from authorisation, through to presentment and so on). Incoming messages must be linked with each other. The main reason for linkage is to compare financial effect of new messages with previous messages and re-calculate card balances.

Matching of a received message to an earlier message is done by comparison of some key data fields. For details see [Transaction Matching](Requirements/Transaction_Matching.htm).

#### Q. What fields should I use for transaction matching?

You can use the following fields to match your transactions:

1. `traceID_lifecyle` - this is the primary identifier to match a message to a previous transaction.
2. `authcode` and `date`- can be used to match where you cannot find a match using `traceID_lifecyle`

## EHI Cut Off Messages

#### Q. What are Cut Off messages and what are they used for?

The EHI cut off message is an optional service, which provides a summary of messages sent to the External host in the last X hours (where X is configurable). This is set at product level and sent every X hours to the specified URL you provided.

The cut off message enables you to check all the messages that Thredd has sent to and received from the external host and to identify where any messages were not received/acknowledged (e.g., because of a network connection issue or timeout). It is an important aid to transaction reconciliation and troubleshooting.

The cut off message structure is different to the normal EHI transaction message structure, so Thredd recommends you use a different URL for your cut off messages.

#### Q. How do the timings on EHI Cut off messages work?

EHI starts sending the cut off message at the end of the cut-off period that was applied to a product.

For example if you select a cut off period of every 6 hours, if added to a product at 1 am, EHI will start sending at 7 am.

Cut of times often vary per product as they can be added to different products at different times.

#### Q. What happens if there is no data within the cut off period?

If there is no data, then zero is sent as a count at the end of the cut-off period.

## Transaction Processing

#### Q: What are processing codes and how can I identity them?

The processing code (`Proc_Code`) is a 6 digit field made up of a 2 character transaction code identifying the type of payment, a 2 character source account type code and a 2 character destination account type code. The (`Proc_Code`) is based on information obtained from the card scheme networks as well as Thredd's own systems. You can use the processing code to apply processing rules to the transaction (for example, to restrict card usage or charge fees based on the type of transaction. For details, see [Processing Codes](Appendices/Processing_Codes.htm).

#### Q: What is the difference between Card Scheme Stand In Processing (STIP) and Thredd STIP?

Scheme STIP is configured on the Card Scheme network:

* The Scheme makes the authorisation decision when the Issuer Processor (Thredd) is unavailable or does not respond in time.

* STIP is enabled only up to a maximum predefined Stand-in authorisation amount
* Configured on the Scheme's systems at BIN level

Thredd STIP is configured on Thredd systems:

* Thredd make the authorisation decision when the Program Manager's external host system is unavailable or does not respond in time.
* Allows flexible STIP authorisation amounts, within the limit set for the product
* Configured on Thredd systems at Product level

#### Q: How does Mastercard STIP work?

A Mastercard STIP allows Mastercard to complete a transaction when the systems for the Issuer or Thredd are unavailable. Each transaction where Mastercard has processed on Thredd or the Issuer's behalf is followed by an Authorisation Advice message (MTID: 0120), indicating the outcome of the transaction, for example, Accepted or Declined.

#### Q. How are fees applied and reported for declined transactions?

When a transaction is declined, the system applies a pre-configured decline fee. This fee is processed and reported in EHI messages as follows:

* The *Fixed Fee* and *Rate Fee* are set to 0.
* The *Note* field is updated to include details of both the *Fixed Fee* and *Rate Fee*.
* If a *Decline Fee* is defined for the specific card product:

  + This fee is deducted from the card balance.
  + The deducted amount is populated in the *Fixed fee* field in the EHI message.

  This will be the only fee that is applied to the card for a declined transaction.

Applicable if you are using the Thredd Fees module to apply fees to transactions. See [Fees Guide > Completing your PSF: Decline Fees](https://docs.thredd.com/fees/Content/Fee_Setup_and_Configuration/Completing_your_PSF.htm#Decline_Fee).

## Transaction Lifecycle

### Authorisations

#### Q. What are Authorisations and how do they work?

Authorisation is the stage in a transaction life-cycle where a [merchant![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.](#) requests approval for a card payment amount. If the authorisation is approved, the amount is ring-fenced on the card. Ring-fencing means that the amount is blocked and the available balance on the card is reduced by this amount.

There are different types of authorisations:

* **Pre-auth** - the merchant requests authorisation for an initial amount. This may be followed by authorisation requests for additional amounts.
* **Auth** - the merchant requests authorisation for a purchase amount. This could either be the full amount of the purchase or a partial amount.
* **Auth and Capture** - the merchant requests the authorisation and taking of the amount at the same time.

When Thredd receives the authorisation request, this is processed according to your EHI mode. In Full Service Processing (mode 3), Thredd approves or declines. In Gateway Processing (mode 1), the Program Manager approves or declines. Other modes use a combination of Thredd and Program Manager approval. Where the Program Manager maintains the card balance, they need to block the approved amount on the card and reduce the available balance. See [EHI Operating Modes](Getting_Started/EHI_operating_modes.htm).

For an approved transaction, typically the merchant then has up to 7-10 days to request settlement of the authorised amount. The time-period when a merchant needs to request settlement of the authorised amount may vary, depending on their [Merchant Category Code (MCC)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.](#) and can be up to 28 days. They can respond by:

* Sending an **authorisation reversal request** - for example, if the transaction is a duplicate or was submitted in error. When the Program Manager receives the authorisation reversal message and they hold the card balance, they should unblock the amount reserved on the card.
* Sending a **presentment request** - to take part or all of the authorised amount. When the Program Manager receives the presentment request, they should match it to the original authorisation; where they hold the card balance, they should deduct the amount from the balance on the card.

  This captured amount is transferred from the card [issuer![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.](#) to the merchant's [acquirer![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) during the settlement process. (Thredd is not involved in settlement, although we do receive copies of settlement reports.)

If no response is received from the card scheme network within the Thredd configured [hanging filter![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) time period, Thredd automatically issues an authorisation reversal message. When the Program Manager receives the authorisation reversal message and they hold the card balance, they should unblock the amount reserved on the card.

For more information, see [Transaction Flow Scenarios](Getting_Started/Transaction_Flow_Scenarios.htm).

#### Q. What is an incremental authorisation and how do I identify it?

An incremental authorisation is an additional authorisation, following a previous transaction authorisation, which is used to request an additional amount for the same product or service purchased by the cardholder. It is commonly used by merchants in the hospitality and tourism industry, for items such as hotel bills and car rentals, where the final amount is not known at the time the original authorisation is requested.

Multiple incremental authorisations are usually linked to a single presentment.

The incremental authorisation is for an additional payment and doesn't affect any previous authorisations made on the card.

You can identify an incremental authorisation as follows:

* `txn_type` = A (authorisation)
* In `Message_Why`, the `Response_Source_Why` value = 56 (for Visa) and will be blank for Mastercard. See [Response\_Source\_Why and Message\_Why](Appendices/Response_Source_Why_and_Message_Why.htm#top).
* `auth_type` = 0 or P (used for both preauths and incremental auths)
* The following fields are the same as in the original authorisation: `Token`, `Txn_CCy` and `traceid_lifecycle`
* The `Network_Transaction_ID` field will be unique.

Other ways you can use to identify incremental authorisations:

* For Mastercard, you can use the `Traceid_Original` field. Positions 1-9 will have the same value as the original authorisation.

  The same `Traceid_Original` value can also appear in subscription payments and recurring payment scenarios. You should exclude these non-incremental cases, which can be identified where position 1 of `GPS_POS_Data`  is equal to 4.
* For Visa, `Reason_ID` = 3900 (incremental auth for Visa).

  In some instances, this field may be blank, so you should not rely on it.

#### Q. What is an ASI transaction and how do I identify it?

Account Status Inquiry (ASI) is a type of authorisation transaction, supported by Mastercard, which allows a merchant to check the Card Validation Code (CVC) and, if address details are provided, to optionally use the Address Verification Service (AVS). If these checks are successful, Thredd responds to the merchant with 00 (approve). The merchant typically then submits a second authorisation transaction, with an actual transaction amount included.

(Note: for a decline, the typical response is *62 - Restricted card*)

You can identify the Authorisation Request/0100 message for an ASI transaction as follows:

* `Proc_Code` has a value of *39*.
* `Bill_Amt` has a value of zero.
* `auth_type` field has a value of V to identify account verifications
* `POS_Data_DE61` subfield 7 (POS Transaction Status), has a value of 8 (Account Status Inquiry Service (ASI))
* `Additional_Data_DE48` subelement 82 (Address Verification Service Request), has a value of 52 (AVS and Authorization Request/0100) for AVS requests (optional)
* `Additional_Data_DE48` subelement 92 (CVC 2 Value), has a CVC 2 value (optional)

#### Q. What is the MerchantAdvice field and how is it used?

The `MerchantAdvice` field contains a Merchant Advice Code (MAC), which provides the merchant with some further information about the decline, which they can use to decide what to do next: whether to obtain updated details from the cardholder, re-try the transaction later or not attempt any further transactions on the card.

* Where Thredd manages the authorisation response on your behalf ([Full Service Processing](Getting_Started/EHI_operating_modes.htm)), the system returns an appropriate advice to the merchant in the authorisation response. This advice code is based on the card status and available funds.
* Where your systems manage the authorisation response ([Gateway or Cooperative Processing](Getting_Started/EHI_operating_modes.htm)), you can optionally return one of the advice codes listed in the description of the `MerchantAdvice` field. See [GetTransaction Message Fields](Requirements/GetTransaction_Message.htm): [MerchantAdvice](Requirements/GetTransaction_Message.htm#MerchantAdvice).

When declining a transaction and returning a Merchant Advice Code value of â03â (Merchant should not retry again), you must not approve any future transactions on this card. This advice code is reserved for lost, stolen or destroyed cards that are permanently blocked.

Be aware that Mastercard could impose issuer fines for transactions that are authorised on a PAN where previously a Merchant Advice Code value of â03â (Merchant should not retry again) was returned to the merchant.

#### Q. What is an offline transaction and how do I handle it?

In an [offline transaction![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card is not checked in realtime, there is a risk that the card may not have the amount required to cover the transaction.](#), Thredd has not received a previous authorisation transaction from the card network. In this case you will not receive any authorisation request message. See the [Presentments](#Presentm) section below for details of how to handle a presentment message for an offline transaction.

#### Q. What is the traceid\_lifecycle field and how is it constructed?

This is a unique transaction lifecycle identifier which can be used to track a transaction across its lifecycle, enabling linking of authorisations and financial messages relating to the same transaction.

The `traceid_lifecycle` is a concatenation of: *network\_id + "-" + date\_yyyymmdd + "-" + a unique identifier*

For details of how this is constructed for different networks, see the following table:

| Card Scheme (Network) | network\_id | date\_yyyymmdd | Unique identifier | Example |
| --- | --- | --- | --- | --- |
| Mastercard Banknet | BNET | Banknet trace date from DE15 that corresponds to the Banknet serial number (from DE63). | The traceid from field 63 (or equivalent from field 48.63, e.g., for incremental authorisations) | "BNET-20181231-MCC1234XY" |
| Visa Base I | VIS1 | Date from inside the Visa Transaction ID | The Base field 62.2 Visa Transaction Id. For details, see Visa's Base II documentation. | "VIS1-20180331-918090604354364" |
| VDEP/Visa-Tokenisation-System API call | VDEP | No date.  The  `traceid_lifecycle` format is: "*VDEP" + 1 space + X-REQUEST-ID"* | The 36-character X-REQUEST-ID from VDEP API incoming HTTP header field. | "VDEP 90bc1da9-4f7e-491d-ba3b-1e0d70c1b601" |

### Presentments

#### Q. What are presentments and how do they work?

A presentment (settlement or clearing request) is a financial transaction where Thredd receives a request to settle an amount that was previously authorised on a card. A presentment is typically linked to a previous authorisation transaction. Thredd receives several daily batch clearing files from the card schemes, containing, amongst other records, presentments.

The majority of presentment transactions are requests for settlement of transactions authorised the previous day. However, for a normal authorisation, under current card scheme rules, merchants have up to 7-10 days to request settlement of an authorisation. For some merchant category codes (e.g., card rentals and hotels), settlement can be up to 28 days after the authorisation.

Thredd processes the presentments in the batch file, records details in the Thredd database, and sends a presentment message for each presentment, via EHI to the external host (Program Manager's system).

When you receive a presentment, you should try and match to an existing preauthorisation. Where your systems hold the card balance, you should reduce the balance by the amount of the presentment.

#### Q. Are there any cases where Thredd receives a presentment which does not have a linked previous authorisation?

Yes. In the case of [offline transactions![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card is not checked in realtime, there is a risk that the card may not have the amount required to cover the transaction.](#), the authorisation approval is made without Thredd and we will have no record of the transaction in the system. In this case, Thredd creates a new authorisation transaction and sends this to the Program Manager, followed by the linked presentment message. For more information, see [First Presenment for an Offline Transaction](Getting_Started/Transaction_Flow_Scenarios.htm#First).

#### Q. What are incremental presentments and how do I handle them?

An incremental presentment may occur when a merchant requests an authorisation for a specific amount, but then submits multiple presentments for different partial amounts. So, an incremental presentment has one authorisation and multiple presentment files. The final presentment total usually equals the total of the original authorised amount.

An incremental presentment can be identified in a GetTransaction financial message if the `multi_part_txn` field = 1. Additional fields provide information on the sequence and number of expected partial presentments: `multi_part_txn`, `multi_part_txn_final`, `multi_part_number` and `multi_part_count` (Visa only). See [GetTransaction Message Fields](Requirements/GetTransaction_Message.htm).

When you receive an incremental presentment, you should only unblock the amount stated and not the full amount previously authorised. When you have received the final presentment, you can calculate the total and unblock any amount left on the original authorisation.

A presentment must be correctly flagged by the acquirer in order for Thredd to identify it as an incremental presentment. This option is specific to Visa and some acquirers may not report this information.

#### Q. How is a partial presentment processed?

For a partial presentment (i.e., for part of the authorised amount), the authorised fees are partially cleared as well, with the remaining amount blocked on the card.

#### Q. What happens if a presentment is more than the amount available on the card?

The presentment always debits or credits the card balance, regardless of the existing amount. If the presentment is more than the amount held on the card, the card account would go into a negative balance.

whether negative balances are permitted on your programme will depend on the nature of the program type and the agreements with the issuer.

#### Q: How do I identify a negative card balance?

In processing modes where Thredd manages the balance (Full Service Processing - mode 3 and Cooperative Processing - mode 2) a negative balance is indicated in the `balance` and `available_balance` fields.

### Clearing Files

#### Q. How often do Thredd receive clearing files from the schemes?

Mastercard send 8 clearing files per day, seven days a week. Visa send 2 clearing files per day.

#### How often does Thredd process clearing files?

It is possible for Thredd to process clearing files 7 days a week. Please note, this does not change the date of settlement. If you are interested in enabling 7 day clearing file processing, please contact your account manager for more details.

#### How long does it take Thredd to process the clearing files?

It takes Thredd a few hours to process the clearing files and send notifications via EHI.

#### Q. What happens if Thredd does not receive a presentment for a previously authorised card amount?

If no presentment is received within a defined [hanging filter![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) period, Thredd sends a financial authorisation reversal message, via EHI, to the external host. The Program Manager should unblock any amount ring-fenced on the card, so that it is available to the cardholder.

### Credit Transactions

#### Q. Can a refund be online?

Yes. Visa and Mastercard allow acquirers to send refunds with or without authorisation. If an online refund (authorisation) is received, it will be normally followed by a presentment (financial) similar to purchase authorisation flow. Thredd recommend that you do not make the funds available to the cardholder before the financial is received.

#### Q. What is the difference between refund authorisation and reversal authorisation?

Authorisation reversals occur against authorisations that have not yet become financial (no presentment is created). Reversals are typically received on the same day. If a reversal authorisation is received for a purchase which is already cleared (i.e. the presentment is received before the authorisation reversal), it indicates a transaction processing error on the acquirer's side.

Refunds are standalone transactions that have their own lifecycle (financial message and possibly an authorisation message). Refunds might be linked with a previous purchase or they may not. Unlike reversals, there is no strict linking requirement for refunds against previous purchases (due to the independent flow, there is no need to backward balance update).

#### Q. What is the difference between Refunds and Fund Transfers (Original Credits)?

Refunds are common way of returning funds to customers relating to a previous card transaction. Thredd recommends that you only transfer the refund to the cardholder after you have received the financial message confirming the refund.

Original credits are fund transfer transactions from one entity to another and are not linked to a previous transaction. Visa Fast Funds and Mastercard Money Send are examples. Unlike refunds, most of the Fund Transfer transactions should be funded to the target card within 30 minutes of authorisation. This needs a careful approach to detect the appropriate fund transfers and credit the cards in 30 minutes and not credit the cards again when financials are received. (Please check with your Visa / Mastercard representative to confirm the funding requirements for your region/country).

### Network Fees

#### Q. How are Acquirer fees applied and reported?

Acquirer fees do not affect the cardholder balance at Thredd and are passed as data only, requiring program managers to handle fees separately. This fee data is provided in the EHI field `Amt_Tran_Fee_DE28`.

#### Q. How are Acquirer ATM fees applied and reported?

Acquirer fees for ATM balance inquiries, PIN changes and cash withdrawals are sent in the EHI field `Amt_Tran_Fee_DE28` and are not included in the `Bill_Amt` used for card limit checks. See the example below, showing a cash withdrawal of 100 GBP and an Acquirer ATM fee of 1.5 GBP.

[Copy](javascript:void(0);)

```
<GetTransaction  
            xmlns="http://tempuri.org/">  
            <Acquirer_id_DE32>0852729540</Acquirer_id_DE32>  
            <ActBal>884.9800</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28>D00015000</Amt_Tran_Fee_DE28>  
            <Auth_Code_DE38>129833</Auth_Code_DE38>  
            <Avl_Bal>660.7800</Avl_Bal>  
            <Bill_Amt>-100.0000</Bill_Amt>  
            <Bill_Ccy>826</Bill_Ccy>  
            <BlkAmt>-100.0000</BlkAmt>
```

During transaction authorisation for an ATM withdrawal, for EHI modes (e.g., Full Service Processing) where Thredd controls the card balance, the authorisation approval is made only for the amount in the `Bill_Amt` field. If there is a sufficient balance held on the card, the request will be approved.

#### Q. Does Thredd provide an option to deduct Issuer transaction-related fees from a card?

This applies to EHI modes (e.g., Cooperative Processing and Full Service Processing) where Thredd controls the card balance.

You can use the Thredd Fees module to deduct Issuer fees (e.g., ATM withdrawals and balance inquiries) from the card at the time of the transaction authorisation.

If there is sufficient balance on the card, the fee will be deducted from the card's available balance.

If there is insufficient balance on the card and you have enabled *Partial Fees*, then Thredd will deduct a part of the fee amount and create a Pending Fee Record. If you have not enabled Partial Fees, the transaction will be declined.

For other EHI modes (e.g. Gateway Processing) where Thredd does not control the card balance, the Issuer fees must be calculated and sent in the relevant EHI fields to the External Host.

For more information, see the [Fees Guide](https://docs.thredd.com/Fees_Guide.htm).

## Transaction Lifecycle - Single Message Systems

#### Q. How does the transaction life cycle differ in Single Message Systems?

Single Message Systems do not provide a separate authorisation and clearing (presentment) stage. Instead, the Card Scheme sends a single online financial request, in realtime, for approval. This is the equivalent to an authorisation request, the main difference is that instead of placing a block on the amount, you change the balance immediately.

There can be multi-message scenarios in Single Message systems. Depending on the single message network you participate, following cases may happen:

* **Preauthorization\Completion:** In this scenario, a 0100 might be coming as a preauthorization, which is later finalized by an online 0220 completion message.
* **Incremental authorization\Completion:** This is a life cycle case where multiple 0100 preauthorizations are cleared with a final online 0220 completion message
* **Authorization\Multi completion:** A 0100 preauthorization might be cleared by multiple online 0220 completion messages
* **Financial Request\Financial Reversal:** 0200 message followed by 0420 message.
* **Financial Request\Financial Reversal:** 0220 message followed by 0420 message.
* **Financial Request\Financial Advice:** An Adjustment (0220) follows a previous Financial Request (0200).

Contact your Account Manager to confirm which of these cases apply to your implementation.

#### Q. What is an Online Financial Request?

This is a realtime financial request to approve a payment transaction. Your systems should respond with approve or deny and adjust the card balance accordingly.

#### Q. What is an Online Financial Advice?

This is a realtime financial message to advise you of a payment transaction. Your systems should respond with an acknowledgement and adjust the card balance accordingly (you cannot approve or deny an advice message). An example of an online financial advice is where the Card Scheme did not receive a response to an online financial request and performed [Stand In Processing (STIP)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#).

#### Q. What is an Online Financial Reversal?

This is a realtime financial request to reverse a previous online financial transaction. Your systems should respond with approve and adjust the card balance.

## Single Message Systems

#### Q. What is Mastercard Network Exchange?

This is a processing network for US issuers, where messages are processed based on Single Message standards. This network enables one stop integration for the US Local Debit Networks such as STAR, PULSE and NYCE.

#### Q. Which regions support Single Message Systems?

This standard is more common in regions such as the US and parts of the Asia Pacific. Please check with your Card Scheme representative or Implementation Manager for details. Note that it is possible for the Scheme in your region to operate a mixed approach that supports both Single and Dual Message System formats.