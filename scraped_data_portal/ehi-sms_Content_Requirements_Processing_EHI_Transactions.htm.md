# 2.1 Processing EHI Transactions

This section describes how to process the real-time transactional data sent from EHI to your external host system. When your external host system receives a message from EHI, it must be able to implement the following:

* [Return an acknowledgement to EHI](#Respondi)  - within the time limit set for a response
* [Respond to requests](#Respondi2) - including updating the card balance (where required by your EHI mode).
* [Respond to cut-off messages](#Respondi3) (optional)
* [Check for duplicate requests](#Checking) - and respond to EHI accordingly
* [Check fields used for 3D Secure Authentication](#Checking_fields_used_for_3D_Secure_Authentication) (if applicable) - to verify that the merchant, currency and amount match the details in the authorisation
* [Update the STIP balance if required](#Updating) - only relevant to EHI Mode 4 (Gateway Processing with STIP) where Thredd provides Stand-In Processing (STIP)
* Perform transaction matching and processing - this is internal to your systems and no response to EHI is required. For details, see [Transaction Matching](Transaction_Matching.htm).

## 2.1.1 Returning an Acknowledgement to EHI

When you receive a GetTransaction message, your external host system must respond to EHI within the allowed time limit for a response (for the default timeout, see [EHI Configuration Options](../Getting_Started/EHI_Configuration_Options.htm)), with the `Acknowledgement` field set to â1â to indicate that you have successfully processed the transaction.

EHI waits for a response with the `Acknowledgement` field set to â1â and if no response is received (or an acknowledgement = 0 is received), it continues to re-send the message until either:

* It receives a response with the `Acknowledgement` field set to â1â.

  Or
* The maximum number of permitted re-tries configured in Thredd has been reached for this message.

## 2.1.2 Responding to Requests

### Responding to Authorisation Requests or Online Financial Requests

In an authorisation request message, the Message Type Identifier (`MTID`) = *0100* and the transaction type (`Txn_Type`) = *A*.

For Program Managers receiving messages from [Single Message Systems](../Getting_Started/Single_vs_Dual_Message.htm), you will receive an Online Financial Request, where the message transaction ID (`MTID`) = *0200* and the transaction type (`Txn_Type`) = *M*.

In all EHI modes, your systems should always acknowledge the request. In EHI modes 1, 2 and 4 (Gateway and Cooperative Processing) your systems should respond with a decision (*approve* or *decline*). See [EHI Operating Modes](../Getting_Started/EHI_operating_modes.htm).

* For a request where you approve, your response to EHI should look like this:

  *<Responsestatus>00</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>*
* For a request where you decline, your response to EHI should look something like this:

  *<Responsestatus>05</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>* \*

\* `Responsestatus` = 00 indicates the request is approved.

\* `Responsestatus` = 05 indicates *Do not honour* (decline) â you can chose any suitable decline response code. See [Response Status Values](../Appendices/Response_Code.htm). Acknowledgement = 1 informs Thredd that the message was received and Thredd does not need to resend.

For EHI mode 3 (Full Service Processing - advice only), your response should look like this:

*<Acknowledgement>1</Acknowledgement>*

#### Response fields

For details of mandatory and optional fields that can be included in your response, see [Response Message Fields](GetTransaction_Message.htm#Response).

Do not return the value "null" in any response fields which require numeric values, as this results in EHI declining the transaction. Exclude fields that are optional, if you do not want to return any values.

#### What happens if EHI does not receive a response?

If no response is received in the time limit for an authorisation or online financial request then the following happens in these EHI modes:

* Gateway Processing (mode 1): Thredd declines the transaction.
* Cooperative Processing (mode 2): If Stand-In processing is not enabled, Thredd declines the transaction. If Stand-In processing is enabled, Thredd makes the decision, which could be *Approve* or *Decline*.
* Gateway Processing with STIP (mode 4): Thredd makes a stand-in processing decision, which could be *Approve* or *Decline*.
* (Full Service Processing (mode 3) is advice only)

Thredd then resends the transaction to notify you of the decision made, with these changes:

* `SendingAttemptCount` field is:

  + EHI modes 1 and 2: â1â (1st repeat) or higher (ânâ nth repeat)
  + EHI mode 4: â0â on first message, (and +1 for each time re-attempted)
* `Authorised_by_GPS` field is set to âYâ
* `Txn_Stat_Code` field is set to âAâ (Approved) or âIâ (Declined)
* `Resp_Code_DE39` field is set to the response code sent back to the network (normally â00â if approved, or â05â (declined) in most cases.)

If you get an advice that has changed the decision you originally made, this may indicate that Thredd did not receive or could not process your original decision (example, due to a network timeout or invalid response format) and has therefore applied the default response for your mode. In this case you should acknowledge the advice and reverse the effect of the original approval (example, by unblocking any previously reserved amounts or reversing a previous debit).

#### How Thredd responds to the External Host

The table below shows a summary of the type of message content sent to the external host *after* the initial authorisation request.

| Setup Option | Mode | Reponse Received from external host\* | Thredd Response | Acknowledgement Message to External Host Includes | How you should Respond |
| --- | --- | --- | --- | --- | --- |
| Gateway Processing | 1 | No | Decline | Declined: 0100A or 0200M - Authorised by Thredd "Y", Txn\_Stat\_Code "I" <DE39 Reason code>, Sending attempt count 1. | Acknowledge |
| Gateway Processing | 1 | Yes (approve or decline) | Pass on to scheme | No message sent to external host. | Not applicable |
| Cooperative Processing | 2 | N/a \*\* | Thredd approved | Approved: 0100A or 0200M - Authorised by Thredd "Y", Txn\_Stat\_Code "A" <DE39 Reason code 00>, Sending attempt count 0. | Approve or decline |
| Cooperative Processing | 2 | N/a \*\* | Thredd declined | Declined: 0100A or 0200M - Authorised by Thredd "Y", Txn\_Stat\_Code "I" <DE39 Reason code>, Sending attempt count 0. | Acknowledge or override[1 In mode 2 - Approve with Load, you can override a Thredd decline decision if the reason for the decline is insufficient balance (e.g., where the card balance held on your systems indicates the card has sufficient funds). In this case you should use the load card web service to update the Thredd held balance.](#) |
| Cooperative Processing | 2 | Yes | Pass on to scheme | No message sent to external host. | Not applicable |
| Full Service Processing | 3 | N/a \*\* | Thredd approved | Approved: 0100A or 0200M- Authorised by Thredd "Y", Txn\_Stat\_Code "A" <DE39 Reason code 00>, Sending attempt count 0. | Acknowledge |
| Full Service Processing | 3 | N/a \*\* | Thredd declined | Declined: 0100A or 0200M- Authorised by Thredd "Y", Txn\_Stat\_Code "I" <DE39 Reason code>, Sending attempt count 0. | Acknowledge |
| Gateway Processing with STIP | 4 | No | STIP approved | Approved: 0100A or 0200M- Authorised by Thredd "Y", Txn\_Stat\_Code "A" <DE39 Reason code 00>, Sending attempt count 0. | Acknowledge |
| Gateway Processing with STIP | 4 | No | STIP declined | Declined: 0100A or 0200M- Authorised by Thredd "Y", Txn\_Stat\_Code "I" <DE39 Reason code>, Sending attempt count 0. | Acknowledge |
| Gateway Processing with STIP | 4 | Yes | Pass on to scheme | No message sent to external host. | Not applicable |

#### Notes

\* Your response must be received within the default time limit for a response (see [EHI Configuration Options](../Getting_Started/EHI_Configuration_Options.htm)). Note: although you may have responded within the time limit, in some circumstances Thredd may not have received or processed your response due to a network timeout or invalid response format.

\*\* An approve or decline response is not applicable to Cooperative Processing (mode 2) and Full Service Processing (mode 3) where Thredd makes the initial approval or decline decision. In EHI Mode 3 Thredd sends the response directly to the card scheme and sends the external host an acknowledgement. In Cooperative Processing (mode 2) Thredd first sends any approved decision to the external host, which can override the decision.

### Responding to Authorisation Reversals or Online Financial Reversals

A reversal occurs when a merchant wants to reverse a previously submitted authorisation or inline financial request (for example, because the requested amount was entered incorrectly or the customer cancelled the order). The reversal normally occurs soon after the original authorisation or online financial message (or same day) and can be matched to the original authorisation or online financial message using the `traceid_lifecycle` field.

If you receive an authorisation reversal request (`MTID` = *0400* and `Txn_Type` = *D*), authorisation reversal advice (`MTID` = *0420* and `Txn_Type` = *D*) or an online financial reversal (`MTID` = *0420* and `Txn_Type` = *V*), your response to EHI should look like this:

*<Responsestatus>00</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>*.

Note that if your system was unable to process the request (For example, your database connection was down, so you could not update any outstanding blocks) you can request the message to be resent. In this case, your response to EHI should look like this:

*<Responsestatus>96</Responsestatus>* and *<Acknowledgement>0</Acknowledgement>*. (You can use codes â91â, â92â or â96â.)

### Responding to Thredd Declines

In scenarios where Thredd initially declines an authorisation or online financial request, you can respond as follows:

* In Gateway Processing (mode 1), you are not able to overrule the decline, you should return a `Responsestatus` with the same `responsecodeDe39` value that Thredd sent.
* In Full Service Processing (mode 3), you can just acknowledge the message.
* In Cooperative Processing (mode 2), you can overrule the Thredd insufficient balance decline. If you send a `Responsestatus` of â*0A*â, Thredd will load the amount you sent in `LoadAmount` field to the card, and recheck the balance is sufficient. Partial approval is also possible in this mode (see [Responding to Partial Approvals](#Respondi4).)
* In Gateway Processing with STIP (mode 4), you cannot overrule our decline (except for a partial approval).

## 2.1.3 Responding to Partial Approvals

A partial transaction approval occurs where the Program Manager approves part of the transaction amount only, for example, because the initial approval request was declined due to insufficient funds. For EHI modes where you can overrule the decline decision with a partial approval (Cooperative Processing - mode 2 , Gateway Processing with STIP - mode 4) the process is as follows:

1. Thredd receives an authorisation or online financial request from the card scheme.
2. Thredd initially declines the request due to insufficient funds.
3. The Program Manager overrides the decline, with a partial approval via EHI.
4. Thredd partially approves the request and returns the response to the card scheme.
5. Thredd sends an updated EHI message with the actual result (*Partially Approved*).
6. The Program Manager replies to the updated EHI message with an acknowledgement.

#### Example

The initial request is declined due to insufficient funds, for example: `settlementBillingAmount`= -60.00 and `Responsestatus` = 51.

For a partial approval, your response to EHI to override the decline should look like this:

*<Responsestatus>10</Responsestatus>* and *<Acknowledgement>1</Acknowledgement>*

Thredd then sends the partial approval, for example: `Bill_Amt` = -50.00 and `Resp_Code_DE39` = 10.

You will receive an authorisation or online financial advice and should respond as normal.

### Partial Approvals - Mode 1 Clients

For Gateway Processing (mode 1) clients who make the authorisation decision, partial approval works as follows:

1. Thredd receives an authorisation or online financial request from the card scheme.
2. Thredd sends the authorisation or online financial request to the Program Manager, via EHI.
3. The Program Manager partially approves via EHI.
4. Thredd sends the response back to the card scheme.

## 2.1.4 Responding to Financial Notifications

Financial notifications include transactions such as first presentments (MTID/Txn\_Type= 1240/P or 05/P, 06/P, 07/P), financial reversals (MTID/Txn\_Type = 1240/ E or 25/E, 26/E, 27/E), chargebacks (MTID/Txn\_Type = 1240/C or 1240/H).

Your response to EHI could look like this:

*<Acknowledgement>1</Acknowledgement>*.

## 2.1.5 Responding to Cut\_Off Messages

When responding to Cut\_Off messages, if you have successfully processed, `Cut_OffResult` should = â1â.

If a response with `Cut_OffResult` is received with â0â (or no valid response), EHI does not resend the message. (However, not that in a future version Thredd may re-send the Cut\_Off message, as this indicates you have failed to process it and it requires re-sending.)

## 2.1.6 Checking for Duplicates

In some cases it is possible that when your external host responds to EHI with a valid acknowledgement (`Acknowledgement` = 1), due to network issues, your acknowledgement may not be received by EHI. In this case EHI will re-send the message, resulting in a duplicate.

### How to Identify a Duplicate Message

For GetTransaction messages, if either of the following conditions is true, then the message is a duplicate:

* If the `SendingAttemptCount` field is â1â or higher (i.e. non-zero)
* If you have already received a message with the same transaction ID (`txn_id`).

### How to Process a Duplicate Message

1. First check to see if the `SendingAttemptCount` field is â1â or higher (i.e. non-zero).
2. If it is higher than 1, then check the transaction ID (`TXn_ID`) field. This is unique for every transaction (for the GetTransaction messages.)
3. If the transaction ID matches the transaction ID of an existing record in your database, this indicates a duplicate, which you should process as follows:

* If the original message was an advice, and your external host already has it then:

  + No need to re-process this
  + Respond with *<Acknowledgement>1</Acknowledgement>*
* If the original message was an advice, and your external host does not have it then:

  + Process it
  + Respond with *<Acknowledgement>1</Acknowledgement>*
* If the original message was an authorisation request (your external host is asked approve or decline), but the repeat is an advice, it will still have the same MTID. This table explains what to do:

| External Host Originally: | Advice Indicates that Thredd: | Action required by the External Host |
| --- | --- | --- |
| Approved transaction | Approved transaction | Nothing to do |
| Approved transaction | Declined transaction | Reverse effect of original approval |
| Declined transaction | Approved transaction | Action the approval |
| Declined transaction | Declined transaction | Nothing to do |
| Never received transaction | Approved transaction | Action the approval |
| Never received transaction | Declined transaction | Nothing to do (but it can be logged) |

### Cut\_Off Duplicate Checking

For Cut\_Off messages, since the `CutoffID` field is unique, you can use this field to detect if the message is a repeat.

EHI currently does not re-send a Cut\_Off message if it does not receive a valid response with `Cut_OffResult` of â1â.  However, this may be added in a future version, so you should configure your systems to expect this.

## 2.1.7 Checking fields used for 3D Secure Authentication

The following fields in the authorisation message relate to the 3D Secure authentication data arriving in the authorisation message. You can use these fields to confirm whether the authorised transaction amount is equivalent to the 3D Secure authenticated amount. [2 This check ensures that important transaction details presented to the cardholder during a 3D Secure session (such as amount and currency) match the final details authorised by Thredd or the Program Manager. Significant discrepancies may indicate a potentially fraudulent transaction.](#)

* [AuthenticationCurrency](GetTransaction_Message.htm#AuthenticationCurrency)
* [AuthenticationAmountUpper](GetTransaction_Message.htm#AuthenticationAmountUpper)
* [AuthenticationMerchantHash](GetTransaction_Message.htm#AuthenticationMerchantHash)

These fields can also be used to comply with the [PSD2![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for payment services that has the purpose of making payments more secure in Europe. It introduces legislation to improve the payment service authentication process.](#) [Strong Customer Authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) When the cardholder is authenticated during a payment transaction using a combination of at least two of the following authentication methods: Knowledge (Something the cardholder knows, such as a password), Possession (Something the cardholder has access to, such as a phone number or email account) and Biometrics (such as a fingerprint, face or voice)
Under the Payment Service Directive 2 (PSD2), strong customer authentication is required on all cardholder-initiated transactions when both the card issuer and acquirer are within the European Economic Area (EEA).](#) (SCA) dynamic linking requirements (see [Directive (EU) 2015/2366 Article 5 Dynamic Linking](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389&from=EN#d1e40-23-1 "SECURITY MEASURES FOR THE APPLICATION OF STRONG CUSTOMER AUTHENTICATION")). See the figure below.

![](../Resources/Images/3DS_dynamic_linking.png "SCA Dynamic Linking")

Figure 25: Matching the Authorisation amount to the authentication amount as part of SCA Dynamic Linking checks

You can also use the indicators provided in the [GPS\_POS\_DATA field](../Appendices/GPS_POS_Data.htm) positions 25 and 26 to check whether the transaction is exempt from SCA and to identify whether the authorisation and authentication amount and currency fields match.

### Matching Authentications to Authorisations

The table below provides details of fields you can use to match the 3D Secure authentication details to the linked Authorisation or Online Financial transaction:

| 3D Secure Authentication Field | Authorisation / Online Financial Fields |
| --- | --- |
| AuthenticationCurrency | Txn\_CCy |
| AuthenticationAmountUpper | Txn\_Amt |
| AuthenticationMerchantHash | SHA 256 hash of `Merch_Name`  **Note**: This only works if the identical name was provided at authentication.  (e.g., Microsoft and MICROSOFT will be hashed differently) |

You can use the above fields to supplement or replace any authentication checks set up for your programme on Thredd systems. For more information, see the [PSD2 and SCA Guide > PSD2 Product Settings](https://docs.thredd.ai/psd/Content/PSD2/PSD2_Settings.htm).

## 2.1.8 Updating the STIP Balance

Only relevant to EHI Modes where Thredd provides real-time Stand In Processing (STIP) if your systems are unavailable (Gateway Processing with STIP - mode 4).

Thredd approves or declines the transaction amount based on the available card balance in the Thredd database. The Thredd stand-in balances can be updated by any of the below options:

* EHI response messages (see [`Update_Balance`](GetTransaction_Message.htm#_Ref448230883) field).
* Balance Update Web Service (see `ws_BalanceUpdate` in the [*Web Services Guide*](https://docs.thredd.com/Web_Services_Guide.htm)).
* STIP Balance Update endpoint (see the [API Hub documentation](https://cardsapidocs.thredd.com/v2.0/docs/card-balance-update)).

Below is an example code snippet of a response returned by the Program Manager's systems, requesting a balance update:

[Copy](javascript:void(0);)

```
<GetTransactionResult>  
          <Responsestatus>00</Responsestatus>  
          <CurBalance>0</CurBalance>  
          <AvlBalance>100</AvlBalance>  
          <Acknowledgement>1</Acknowledgement>  
          <LoadAmount>50</LoadAmount>  
          <Bill_Amt_Approved>0</Bill_Amt_Approved>  
          <Update_Balance>1</Update_Balance>  
          <New_Balance_Sequence_Exthost>200</New_Balance_Sequence_Exthost>  
          <CVV2_Result>400</CVV2_Result>  
          <CurBalance_GPS_STIP>0</CurBalance_GPS_STIP>  
          <AvlBalance_GPS_STIP>100</AvlBalance_GPS_STIP>  
 </GetTransactionResult>
```

You should only respond with `Update_Balance` = â1â (update balance) if you have received both `Balance_Sequence` and `Balance_Sequence_Exthost` in the EHI request message. These balance sequence fields are only relevant to real-time transactions where balance adjustments can be made in the response. If you receive a financial notification and need to adjust the Thredd-held balance, you must use the [Balance Update Web Service](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Balance_Update.htm) or [STIP Balance Update API.](https://cardsapidocs.thredd.com/v2.0/docs/card-balance-update)