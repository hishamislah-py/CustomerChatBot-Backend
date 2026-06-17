# 1.8 Transaction Flow Scenarios - Single Message Systems

This section provides examples of typical transaction flows with Message Transaction IDs (MTIDs) for Single Message systems. This provides a flavour of the type of messages you can expect to receive from the Thredd system.

Single Message System does **not** apply to you, unless you have configured your BINs to support single message system at the card scheme.

For customers using the Dual Message system (which provides separate messages for the [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) and clearing stages), see [Transaction Flow Scenarios - Dual Message Systems](Transaction_Flow_Scenarios.htm).

## 1.8.1 Online Financial Requests

Thredd receives online financial requests depending on your product implementation (based on region/country, and routing options). An online financial request is similar to regular authorization messages (0100), but the financial effect is immediate. Unlike authorisations, where you apply a block to a card balance, online financial messages reduce the card balance instantly.

### Online Financial Request with Approve

The following scenario illustrates a typical approve journey for EHI modes 1, 2 and 4 (Gateway and Cooperative Processing).

![](../Resources/Images/Financial_Auth_with_approval_sms.png "Authorisation transaction flow - Approve")

Figure 21: Financial Authorisation Flow - Approve

1. The scheme sends an 0200 online financial request to Thredd.
2. Thredd carries out validation checks and sends the request to the external host (Program Manager).
3. The Program Manager approves the financial request.
4. The Program Manager debits the final approved amount (including fees) on the card and reduces the available balance.
5. The Program Manager returns an approved response:

   *<Responsestatus>00</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>*.\*
6. Thredd responds to the scheme with an 0210 message (with response status 00 indicating an approval).

\* Responsestatus = 00 indicates the request is approved; Acknowledgement = 1 informs Thredd that the message was received and Thredd does not need to resend.

### Online Financial Request Resulting in a Decline

The following scenario illustrates a typical decline journey for EHI modes 1, 2 and 4 (Gateway and Cooperative Processing).

![](../Resources/Images/Financial_Auth_with_decline_sms.png "Authorisation transaction flow - decline")

Figure 22: Financial Authorisation Flow - Decline

1. The scheme sends an 0200 online financial request to Thredd.
2. Thredd carries out validation checks and sends the request to the external host (Program Manager).
3. The Program Manager declines the request.
4. The Program Manager returns a declined response, for example:

   *<Responsestatus>05</Responsestatus> and <Acknowledgement>1</Acknowledgement>*.\*
5. Thredd responds to the scheme with an 0210 message (with an appropriate response status, e.g. 05, indicating a decline).

\* Responsestatus = 05 indicates Do not honour. You can return any suitable decline response code. See [Response Codes](../Appendices/Response_Code.htm).

Acknowledgement = 1 informs Thredd that the message was received and Thredd does not need to resend.

### Online Financial Reversal

This type of transaction occurs when the merchant, [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) or card scheme requests a reversal of the original online financial request. This should result in a card balance adjustment to load back the amount previously deducted from the card.

![](../Resources/Images/Financial_Auth_with_reversal_sms.png "Authorisation reversal transaction flow")

Figure 23: Authorisation Reversal Flow

1. The original 0200 online financial request message is approved by the Program Manager.
2. The scheme later sends an 0420 online financial reversal request to Thredd.
3. Thredd responds to the scheme with an 0430 message.
4. Thredd sends the request to the external host (Program Manager).
5. The Program Manager matches the reversal message to the original 0200 financial message. See [Transaction Matching](../Requirements/Transaction_Matching.htm).  
   The Program Manager returns an acknowledment to Thredd and updates the cardholder's available balance.

### Online Financial Advice

The online financial advice message contains a transaction detail that is already approved or declined on card scheme and acquirer level. That means that an online financial message cannot be declined. It is important to check the `Resp_Code_DE39` field in the incoming 0220 message, as it can indicate a decline. A non-blank and non-00 value in this field means the financial transaction is declined at network level. In this case, there's no need to update the balance of a card. An approval online financial advice (`Resp_Code_DE39` blank or "00") can be cancelled using the dispute mechanisms enabled for the specific Single Message Network.

![](../Resources/Images/Financial_advice_response_sms.png "Financial advice")

Figure 24: Financial Advice Flow

1. The scheme sends an 0220 online financial advice to Thredd.
2. Thredd responds to the scheme with an 0230 message.
3. Thredd sends the request to the external host (Program Manager).
4. The Program Manager adjusts the card balance, based on the amount in the advice and returns an acknowledgement to Thredd.

### AFD Transactions

Transactions from Automatic Fuel Dispensors (AFDs) work slightly differently to other types of financial messages. The initial amount approved may be for a nominal amount (e.g., 1 USD), which you can either approve or decline. If approved, the AFD pumps up to the permitted maximum it is allowed to clear and sends a financial advice to say how much fuel was actually delivered. In EHI modes where you maintain the card balance, you should return an acknowledgement and then update the balance on the card, to reflect the amount in the financial advice.

AFD transactions (MCC 5542) are blocked by default on the Thredd platform. This will result in an automatic decline for AFD authorisations. To enable AFD transactions, contact your account manager or implementation manager.

#### US AFD Authorisations

For non-commercial cards issued by Thredd clients in the US and used in the US, the AFD limits are as follows:

* Initial Authorised amount = 1 USD
* Amount blocked on the card = 175 USD

After the cardholder has fuelled, e.g., 75 USD, we take this amount and unblock the remaining 100 USD on the card.

### Offline Transactions

In Single Message System offline transactions are received as Online Financial Advice messages (0220). See Online Financial Advice.