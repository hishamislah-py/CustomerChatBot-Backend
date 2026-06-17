# General FAQs

This section provides answers to frequently asked questions. It is divided into the following sections:

* [EHI Setup](#EHI)

* [EHI Modes](#EHI2)
* [Duplicate Checking and Transaction Matching](#Duplicat)
* [EHI Cut Off Messages](#EHI3)
* [Transaction Processing](#Transact3)
* [Transaction Life Cycle](#Transact)
* [Transaction Life Cycle - Single Message Systems](#Transact2)
* [Single Message System](#Single)

#### EHI Setup and Modes

For details, refer to the [External Host Interface (EHI) Guide](https://docs.thredd.com/EHI_Guide.htm).

## Duplicate Checking and Transaction Matching

#### Q. What is duplicate checking and how can I ensure a message is unique?

EHI is designed to resend messages if a successful acknowledgement is not received by Thredd. Even if you respond with a valid acknowledgement, due to network issues, this may not be received by Thredd, in which case Thredd resends the message. This ultimately means that any message can be received through EHI more than once. You must ensure that accounts are not debited or credited multiple times due to duplicate messages.

Duplicate checking must be performed for any new message received through EHI. You can use the transaction ID (`Txn_ID`) field to check the uniqueness of a transaction in EHI.

#### Q. What is transaction matching and how should I perform this?

You are likely to receive multiple linked messages for a card payment transaction throughout its lifecycle (for example, from authorisation, through to presentment and so on). Incoming messages must be linked with each other. The main reason for linkage is to compare financial effect of new messages with previous messages and re-calculate card balances.

Matching of a received message to an earlier message is done by comparison of some key data fields. For details see [Transaction Matching](Processing/Transaction_Matching.htm).

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

For details, refer to the [Transaction XML Reporting Guide](https://docs.thredd.com/transactionxml/Content/Home.htm).

## Transaction Life-Cycle - Dual Message Systems

### Authorisations

#### Q. What are Authorisations and how do they work?

Authorisation is the stage in a transaction life-cycle where a [merchant![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.](#) requests approval for a card payment amount. If the authorisation is approved, the amount is ring-fenced on the card. Ring-fencing means that the amount is blocked and the available balance on the card is reduced by this amount.

There are different types of authorisations:

* **Pre-auth** - the merchant requests authorisation for an initial amount. This may be followed by authorisation requests for additional amounts.
* **Auth** - the merchant requests authorisation for a purchase amount. This could either be the full amount of the purchase or a partial amount.
* **Auth and Capture** - the merchant requests the authorisation and taking of the amount at the same time.

When Thredd receives the authorisation request, this is processed according to your EHI mode. In Full Service Processing (mode 3), Thredd approves or declines. In Gateway Processing (mode 1), the Program Manager approves or declines. Other modes use a combination of Thredd and Program Manager approval. Where the Program Manager maintains the card balance, they need to block the approved amount on the card and reduce the available balance.

For an approved transaction, typically the merchant then has up to 7-10 days to request settlement of the authorised amount. The time-period when a merchant needs to request settlement of the authorised amount may vary, depending on their [Merchant Category Code (MCC)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.](#) and can be up to 28 days. They can respond by:

* Sending an **authorisation reversal request** - for example, if the transaction is a duplicate or was submitted in error. When the Program Manager receives the authorisation reversal message and they hold the card balance, they should unblock the amount reserved on the card.
* Sending a **presentment request** - to take part or all of the authorised amount. When the Program Manager receives the presentment request, they should match it to the original authorisation; where they hold the card balance, they should deduct the amount from the balance on the card.

  This captured amount is transferred from the card [issuer![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.](#) to the merchant's [acquirer![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) during the settlement process. (Thredd is not involved in settlement, although we do receive copies of settlement reports.)

If no response is received from the card scheme network within the Thredd configured [hanging filter![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which waits for an approved authorisation amount to be settled. This is defined at a product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) time period, Thredd automatically issues an authorisation reversal message. When the Program Manager receives the authorisation reversal message and they hold the card balance, they should unblock the amount reserved on the card.

#### Q. What is an incremental authorisation and how do I identify it?

An incremental authorisation is an additional authorisation, following a previous transaction authorisation, which is used to request an additional amount for the same product or service purchased by the cardholder. It is commonly used by merchants in the hospitality and tourism industry, for items such as hotel bills and car rentals, where the final amount is not known at the time the original authorisation is requested.

Multiple incremental authorisations are usually linked to a single presentment.

The incremental authorisation is for an additional payment and doesn't affect any previous authorisations made on the card.

You can identify an incremental authorisation as follows:

`txn_type` = A (authorisation)

The following fields will be the same as in the original authorisation: `Token`, `Txn_CCy` and `traceid_lifecycle`

The `Network_Transaction_ID` field will be unique.

### Q. What is an ASI transaction and how do I identify it?

Account Status Inquiry (ASI) is a type of authorisation transaction, which allows a merchant to check the Card Validation Code (CVC) and, if address details are provided, to optionally use the Address Verification Service (AVS). If these checks are successful, Thredd responds to the merchant with 00 (approve). The merchant typically then submits a second authorisation transaction, with an actual transaction amount included.

(Note: for a decline, the typical response is *62 - Restricted card*)

You can identify the Authorisation Request/0100 message for an ASI transaction as follows:

* `Proc_Code` has a value of *39*.
* `Bill_Amt` has a value of zero.
* `auth_type` field has a value of V to identify account verifications
* `POS_Data_DE61` subfield 7 (POS Transaction Status), has a value of 8 (Account Status Inquiry Service (ASI))
* `Additional_Data_DE48` subelement 82 (Address Verification Service Request), has a value of 52 (AVS and Authorization Request/0100) for AVS requests (optional)
* `Additional_Data_DE48` subelement 92 (CVC 2 Value), has a CVC 2 value (optional)

### Presentments

#### Q. What are presentments and how do they work?

A presentment (settlement or clearing request) is a financial transaction where Thredd receives a request to settle an amount that was previously authorised on a card. A presentment is typically linked to a previous authorisation transaction. Thredd receives several daily batch clearing files from the card schemes, containing, amongst other records, presentments.

The majority of presentment transactions are requests for settlement of transactions authorised the previous day. However, for a normal authorisation, under current card scheme rules, merchants have up to 7-10 days to request settlement of an authorisation. For some merchant category codes (e.g., card rentals and hotels), settlement can be up to 28 days after the authorisation.

Thredd processes the presentments in the batch file, records details in the Thredd database, and sends a presentment message for each presentment, via EHI to the external host (Program Manager's system).

When you receive a presentment, you should try and match to an existing preauthorisation. Where your systems hold the card balance, you should reduce the balance by the amount of the presentment.

#### Q. Are there any cases where Thredd receives a presentment which does not have a linked previous authorisation?

Yes. In the case of [offline transactions![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by vending machines, commuting and transport networks).
The card chip and terminal determine if the offline transaction is permitted under EMV/Scheme rules; if not supported, the terminal declines the transaction. Note: Since the balance on the card balance is not authorised in real-time, there is a risk that the card may not have the amount required to cover the transaction.](#), the authorisation approval is made without Thredd and we will have no record of the transaction in the system. In this case, Thredd creates a new authorisation transaction and sends this to the Program Manager, followed by the linked presentment message.

#### Q. How is a partial presentment processed?

For a partial presentment (i.e., for part of the authorised amount), the authorised fees are partially cleared as well, with the remaining amount blocked on the card.

#### Q. What happens if a presentment is more than the amount available on the card?

The presentment always debits or credits the card balance, regardless of the existing amount. If the presentment is more than the amount held on the card, the card account would go into a negative balance.

whether negative balances are permitted on your programme will depend on the nature of the program type and the agreements with the issuer.

#### Q: How do I identify a negative card balance?

In processing modes where Thredd manages the balance (Full Service Processing - mode 3 and Cooperative Processing - mode 2) a negative balance is indicated in the `balance` and `available_balance` fields.

### Clearing Files

#### How often does Thredd process clearing files?

It is possible for Thredd to process clearing files 7 days a week. Please note, this does not change the date of settlement. If you are interested in enabling 7 day clearing file processing, please contact your account manager for more details.

#### How long does it take Thredd to process the clearing files?

It takes Thredd a few hours to process the clearing files and send notifications via EHI.

#### Q. What happens if Thredd does not receive a presentment for a previously authorised card amount?

If no presentment is received within a defined [hanging filter![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which waits for an approved authorisation amount to be settled. This is defined at a product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) period, Thredd sends a financial authorisation reversal message, via EHI, to the external host. The Program Manager should unblock any amount ring-fenced on the card, so that it is available to the cardholder.

### Credit Transactions

#### Q. Can a refund be online?

Yes. This allow acquirers to send refunds with or without authorisation. If an online refund (authorisation) is received, it will be normally followed by a presentment (financial) similar to purchase authorisation flow. Thredd recommend that you do not make the funds available to the cardholder before the financial is received.

#### Q. What is the difference between refund authorisation and reversal authorisation?

Authorisation reversals occur against authorisations that have not yet become financial (no presentment is created). Reversals are typically received on the same day. If a reversal authorisation is received for a purchase which is already cleared (i.e. the presentment is received before the authorisation reversal), it indicates a transaction processing error on the acquirer's side.

Refunds are standalone transactions that have their own lifecycle (financial message and possibly an authorisation message). Refunds might be linked with a previous purchase or they may not. Unlike reversals, there is no strict linking requirement for refunds against previous purchases (due to the independent flow, there is no need to backward balance update).