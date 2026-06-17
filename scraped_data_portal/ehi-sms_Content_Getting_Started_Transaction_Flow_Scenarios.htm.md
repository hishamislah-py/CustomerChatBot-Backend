# 1.7 Transaction Flow Scenarios - Dual Message Systems

This section provides examples of typical transaction flows with Message Transaction IDs (MTIDs) for Dual Message systems. This provides a flavour of the type of messages you can expect to receive from the Thredd system.

The examples below are for customers using the [Dual Message system](Single_vs_Dual_Message.htm) (which provides separate messages for the [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) and clearing stages). For customers receiving messages from [Single Message systems](Single_vs_Dual_Message.htm) (which combine the authorisation and clearing stages of a payment transaction into a single message), see [Transaction Flow Scenarios - Single Message Systems](Transaction_Flow_Single_Message_System.htm).

## 1.7.1 Authorisations

Authorisation is the stage in a transaction life-cycle where a [merchant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.](#) requests approval for a card payment amount. If the authorisation is approved, the amount is ring-fenced on the card. Typically, the merchant then has 7-10 days to request the transfer of the authorised funds (although this can be up to 28 days for certain merchant category codes). For additional information see  [What are Authorisations and how do they work](../FAQs.htm#Q.)?

### Authorisation with Approve

The following scenario illustrates a typical approve journey for EHI modes 1, 2 and 4 (Gateway and Cooperative Processing).

![](../Resources/Images/Auth_flow.png "Authorisation transaction flow - Approve")

Figure 12: Authorisation Flow - Approve

1. The scheme sends an 0100 authorisation request to Thredd.
2. Thredd carries out validation checks and sends the request to the external host (Program Manager).
3. The Program Manager approves the request.
4. The Program Manager blocks the approved amount (including fees) on the card and reduces the available balance.
5. The Program Manager returns an approved response:

   *<Responsestatus>00</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>*.\*
6. Thredd responds to the scheme with an 0110 message (with response status 00 indicating an approval).

\* Responsestatus = 00 indicates the request is approved; Acknowledgement = 1 informs Thredd that the message was received and Thredd does not need to resend.

#### Partial Amount Approval

[Partial amount approval![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Some acquirers support a partial amount approval for Debit or Prepaid payment authorisation requests. The issuer can respond with an approval amount less than the requested amount. The cardholder then needs to pay the remainder using another form of tender.](#) is allowed for authorisation requests that have a [response code](../Appendices/Response_Code.htm) status of 10 and where `Thredd_POS_Capability` position 1 (partial approval support indicator) is 1. This feature is available for all EHI modes. You can use the `Bill_Amt_Approved` field to return the partially approved amount. See [GetTransaction Message Fields: Bill\_Amt\_Approved](../Requirements/GetTransaction_Message.htm#Bill_Amt_Approved).

### Authorisation Resulting in a Decline

The following scenario illustrates a typical decline journey for EHI modes 1, 2 and 4 (Gateway and Cooperative Processing).

![](../Resources/Images/auth_flow_decline.png "Authorisation transaction flow - decline")

Figure 13: Authorisation Flow - Decline

1. The scheme sends an 0100 authorisation request to Thredd.
2. Thredd carries out validation checks and sends the request to the external host (Program Manager).
3. The Program Manager declines the request.
4. The Program Manager returns a declined response, for example:

   *<Responsestatus>05</Responsestatus> and <Acknowledgement>1</Acknowledgement>*.\*
5. Thredd responds to the scheme with an 0110 message (with an appropriate response status, e.g. 05, indicating a decline).

\* Responsestatus = 05 indicates Do not honour. You can return any suitable decline response code. See [Response Codes](../Appendices/Response_Code.htm).

Acknowledgement = 1 informs Thredd that the message was received and Thredd does not need to resend.

### Authorisation Reversal (network)

This type of transaction occurs when the merchant, [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) or card scheme requests a reversal of the original authorisation. This should result in the amount previously ring-fenced on the card being unblocked.

![](../Resources/Images/auth_reversal_network.png "Authorisation reversal flow - Network")

Figure 14: Authorisation Reversal Flow

1. The scheme sends an 0400 authorisation reversal request to Thredd.
2. Thredd sends the request to the external host (Program Manager).
3. Thredd responds to the scheme with an 0410 message.
4. The Program Manager matches the reversal message to the original authorisation message. See [Transaction Matching](../Requirements/Transaction_Matching.htm).  
   The Program Manager unblocks the authorised amount and updates the cardholder's available balance.
5. The Program Manager acknowledges the message: *`acknowledgement`= 1.*

### Authorisation Reversal (non-network)

If no presentment (request to settle the amount previously authorised) is received within the Thredd [hanging filter![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) period, Thredd automatically reverses the authorisation.

![](../Resources/Images/auth_reversal_flow.png "Authorisation reversal transaction flow")

Figure 15: Authorisation Reversal Flow

1. If no presentment is received within the time period set by the [hanging filter![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#), EHI sends a financial reversal message to the external host (Program Manager).
2. The Program Manager matches the reversal message to the original authorisation. See [Transaction Matching](../Requirements/Transaction_Matching.htm).   
   The Program Manager unblocks the authorised amount and updates the cardholder's available balance.
3. The Program Manager acknowledges the message: *`acknowledgement`= 1.*

### Incremental Authorisation

An incremental authorisation is an additional authorisation, following a previous transaction authorisation, which is used to request an additional amount for the same product or service purchased by the cardholder. See [What is an incremental authorisation and how do I identify it?](../FAQs.htm#Q.3)

![](../Resources/Images/Auth_incremental.png "Incremental Authorisation transaction flow")

Figure 16: Incremental Authorisation Reversal Flow

* A request for the first authorisation is received, and follows the steps of a normal authorisation. See [Authorisation with Approve](#Authoris2).
* When you receive the incremental authorisation (`auth_type` = P or 0), where you maintain the card balance and approve, you should block the additional amount.
* If you receive the final authorisation (`auth_type` = F), where you maintain the card balance and approve, you should revise the amount blocked on the card based on the final amount.

You will receive a single financial presentment, which includes the sum of all incremental authorisations.

### AFD Authorisations

Automated Fuel Dispensers (AFD) are unattended terminals at fuel stations that allow cardholders to purchase fuel without requiring an attendant. Authorisations from AFDs work slightly differently to other types of authorisations. The initial amount authorised may be followed by an authorisation completion advice for either a higher or a lower amount. In EHI modes where you maintain the card balance, you should return an authorisation decision (approve or decline) and then update the blocked amount on the card, to reflect the new authorised amount.

AFD transactions (MCC 5542) are blocked by default on the Thredd platform. This will result in an automatic decline for AFD authorisations. To enable AFD transactions, contact your account manager or implementation manager.

![](../Resources/Images/auth_flow_afds.png "AFD Authorisation and Settlement Flow")

Figure 17: AFD Authorisation and Settlement Flow

The general AFD process described in this section may differ, depending on the fuel dispenser.

#### Scenario 1: Maximum preauthorisation example

**Step 1: Authorisation Request**

1. The cardholder inserts or taps their card at an Automated Fuel Dispenser (AFD).
2. The AFD requests either a pre-set fixed preauthorisation amount or a maximum preauthorisation amount (e.g., 100.00 GBP).
3. The Acquirer sends an authorisation request message. The message may contain a partial authorisation indicator, which allows a partial approval response from the issuer to be returned.
4. Thredd or the Program Manager approves or declines the preauthorisation amount. An approval will either be for the full requested amount or, if the issuer supports partial authorisation, an amount based on the cardholderâs available funds if less than the amount of the authorisation request.
5. If approved, then Thredd or the Program Manager blocks the approved amount on the card and reduces the available balance (e.g., by 100 GBP).

**Step 2: Authorisation Confirmation Advice**

1. The fuel is dispensed and costs 90 GBP. The AFD confirms the amount with the Acquirer. The Acquirer sends a completion advice for 90 GBP to Thredd.
2. Thredd or the Program Manager deducts this amount (90 GBP) from the card's actual balance.
3. Thredd generates a partial authorisation reversal for -10 GBP (`Txn_Type` = D, Credit) linked to the original preauthorisation (reducing the full authorised amount from 100 GBP to 90 GBP).

**Step 3: Settlement and Reconciliation**

1. Thredd or the Program Manager receives the clearing file and matches the financial transaction (presentment) to the original authorisation.
2. Thredd or the Program Manager removes the authorisation amount of 90 GBP. The card now has an authorisation for 90 GBP and a financial message of 90 GBP.

#### Scenario 2: Nominal preauthorisation example

**Step 1: Authorisation Request**

1. The cardholder inserts or taps their card at an Automated Fuel Dispenser (AFD).
2. The AFD requests an authorisation for a nominal amount (e.g., 1.00 USD).
3. The Acquirer sends a preauthorisation request message, indicating that the actual maximum amount expected is higher (e.g., 100 USD chargeback protection amount).
4. Thredd or the Program Manager approves or declines the preauthorisation, treating the nominal amount request as a request for the maximum predetermined amount (e.g., 100 USD) to hold funds for the transaction, even though the request amount is 1 USD. Thredd/The Program Manager may partially approve an amount based on available funds (e.g., approving 50 USD out of 100 USD if the account balance is limited).
5. The authorisation response sent back to the merchant reflects the approved amount, which may be less than the maximum or nominal amount requested, indicating a partial approval if applicable.

**Step 2: Authorisation Confirmation Advice**

1. The fuel is dispensed and costs 90 USD. The AFD confirms the amount with the Acquirer. The Acquirer sends a completion advice for 90 USD to Thredd.
2. Thredd or the Program Manager deducts this amount (90 USD) from the card's actual balance.
3. Thredd generates a partial authorisation reversal for -10 USD (`Txn_Type` = D, Credit) linked to the original preauthorisation (reducing the full authorised amount from 100 USD to 90 USD).

**Step 3: Settlement and Reconciliation**

1. Thredd or the Program Manager receives the clearing file and matches the financial transaction (presentment) to the original authorisation.
2. Thredd or the Program Manager removes the authorisation amount of 90 GBP. The card now has an authorisation for 90 USD and a financial message of 90 USD.

#### US AFD Authorisations

For non-commercial cards issued by Thredd clients in the US and used in the US, the AFD limits are as follows:

* Initial Authorised amount = 1 USD
* Amount blocked on the card = 175 USD

After the cardholder has fuelled, e.g., 75 USD, we take this amount and unblock the remaining 100 USD on the card.

### Refund

A refund transaction occurs when a merchant refunds money to the cardholder, typically relating to a previously processed transaction. The merchant/acquirer submits a request for a partial or a full refund of a previously paid amount. This is typically processed as an 0100 Authorisation request for a negative billed amount, with the DE3 processing code of  *20*. This 2-digit code is displayed in the Thredd (`Proc_Code`) transaction field.

It is not recommended to update the available balance until the linked financial notification is received. You must make information about any pending refund transactions available to cardholders.

## 1.7.2 Financials

Thredd receives batch [clearing![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.](#) files containing financial transactions (presentments) for authorisations that need settlement. Typically the authorisations happened the previous day. Thredd processes the clearing files and sends a separate notification via EHI for each presentment transaction. For additional information see  [What are Presentments and how do they work?](../FAQs.htm#Q.2)

### First Presentment

First presentment occurs when the merchant sends a request to take either part or all of the amount previously authorised on the card[1 You should be aware that in some cases it is possible for merchants to submit a presentment for more than the authorised amount. This is permitted for certain Merchant Category Codes (MCC), but it may also indicate a fraudulent transaction.](#) . This can happen at the same time as the authorisation request or in some cases it can be much later. The Program Manager should attempt to match the presentment to the original authorisation request.

![](../Resources/Images/presentment_flow.png "Presentment transaction flow")

Figure 18: Presenment Flow

1. The scheme sends a batch clearing file to Thredd.
2. Thredd processes the file and sends a notification message per presentment, via EHI, to the external host (Program Manager).
3. The Program Manager matches the presentment to the original authorisation. See [Transaction Matching](../Requirements/Transaction_Matching.htm).
4. The Program Manager unblocks the pending amount and reduces the cardholder's available balance.
5. The Program Manager acknowledges the message: *`acknowledgement`= 1.*

### First Presentment for an Offline Transaction

In an [offline transaction![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card is not checked in realtime, there is a risk that the card may not have the amount required to cover the transaction.](#), Thredd has not received a previous authorisation transaction, so when a financial presentment message is received from the card schemes, we are unable to match to an 0100 authorisation transaction. In this case, Thredd creates a new authorisation transaction and sends this to the Program Manager, followed by the linked presentment message.

![](../Resources/Images/Offline_presentment_flow.png "Offline transaction Presentment flow")

Figure 19: Offline Transaction - Presentment Flow

1. The scheme sends a batch clearing file to Thredd.
2. Thredd carries out validation checks. Since this is an offline transaction, Thredd will not be able to match to an existing 0100 authorisation.
3. Thredd creates an Unmatched [Authorisation Advice Notification](../Requirements/Transaction_Matching.htm#Authorisation_Advice_Notification) and sends it the external host (Program Manager).
4. Thredd sends a presentment notification to the Program Manager.
5. The Program Manager processes the financial notification (matching it to the Unmatched Authorisation Advice Notification).
6. The Program Manager reduces the cardholder's available balance by the amount of the presentment.
7. The Program Manager acknowledges the authorisation message: *`acknowledgement`= 1.*
8. The Program Manager returns a financial notification acknowledgement:*`acknowledgement`= 1.*

### Incremental Presentment

An incremental presentment may occur when a merchant requests an authorisation for a specific amount, but then submits multiple presentments for different partial amounts. An incremental presentment has one authorisation and multiple presentment files. The final presentment total usually equals the total of the original authorised amount. For more information, see [What are incremental presentments and how do I handle them?](../FAQs.htm#Q.4)

### Financial Reversal

A financial reversal occurs when the acquirer cancels all or part of a prior transaction (which may be a purchase, refund, cashback, cash, PIN change, or any other transaction type).

For example, if the acquirer has already taken the funds and are aware of a processing error (e.g., double charging), they can submit an 1240 Financial Reversal. You must return any deducted amounts back to the card.

For a financial reversal, if the card has subsequently been lost, stolen or replaced, then the card record will be in a blocked and inactive/archived status, and you will not be able to update the card status or process transactions on the card. You should have a process in place to provide the reversed funds to your customer (e.g., move money to another account belonging to your customer).

## 1.7.3 Chargebacks

A [chargeback![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.](#) is a mechanism available to cardholders who dispute a transaction on the card and want part or all of a card payment returned. The chargeback is always issued by the card issuer or Program Manager. The creation of chargebacks is outside of the EHI flow; you can create a chargeback using either the Visa or Mastercard online Dispute Management portals or the Thredd [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#). For more information, refer to the *Thredd Chargeback Guide*.

### Chargeback and Second Presentment

A chargeback can only be created for a transaction that has a linked presentment. The Program Manager or card issuer creates the chargeback request, which is sent to the card scheme (Visa or Mastercard). This triggers the process described below.

![](../Resources/Images/Chargeback_flow.png "Chargeback transaction flow")

Figure 20: Chargeback Transaction Flow

1. Thredd receives a chargeback notification from the card scheme (Visa or Mastercard).
2. Thredd sends the chargeback notification message to the external host (Program Manager).
3. The Program Manager returns a chargeback notification acknowledgement.
4. If the merchant or acquirer accepts the chargeback, no further EHI messages are sent. (The Program Manager receives additional transaction notifications via the card scheme's dispute management portal or via Smart Client.)
5. If the merchant or acquirer does not accept the chargeback, Thredd receives a second presentment notification from the card scheme.
6. Thredd sends the second presentment notification message to the Program Manager.
7. The Program Manager returns a notification acknowledgement.

When a chargeback is raised, you should always return the disputed amount to the cardholder within the time period prescribed by the card scheme and issuer regulations relevant to your region.