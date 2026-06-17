# 2.2 Transaction Matching

A typical card payment transaction generates multiple messages during its life cycle. The `GetTransaction` message types you receive for a transaction must be linked to the previous messages for that transaction. This matching enables you to track the history of the transaction, compare the financial effect of a new messages with previous messages and re-calculate card balances.

In Full Service Processing (mode 3) and Cooperative Processing (mode 2), Thredd manages transaction matching.

## 2.2.1 Matching Overview

Your systems should match new to previous transactions as follows:

![](../Resources/Images/transaction_matching_SMS.png "Transaction matching for Single Message System")

Figure 26: Transaction Matching Criteria

For further details, see the [Transaction Matching Criteria](#Transact) below.

Where 3D Secure authentication applies, additional transaction matching should be performed to match details in the authorisation to the 3D Secure authentication details. For detail see [Transaction Matching - Authentications and Authorisations](../Appendices/Transaction_Matching_Guidelines.htm).

### Matching Criteria and Accuracy

Matching a transaction to its original (e.g., *Presentment* to matching *Authorisation*, or *Authorisation Reversal* to matching *Authorisation*) is based on the information received. In most cases transactions match. However, acquirers do not always send accurate information, so mistakes can occur.[1  Visa/Mastercard do not verify whether acquirer information matches, so data from the acquirer may be inaccurate.](#)

You can use the following options to find a match:

* The matching criteria recommended in the section [Transaction Matching Criteria](#Transact)
* Your own matching criteria
* A combination of both the above.

As a general rule, the more matching fields that correctly match, the more reliable the match. If some fields match and some do not, this indicates an âunreliableâ match.

### Transaction Matching Criteria

The table below provides best-practise guidelines on how to match transactions.

Match Criteria:

* If â*Match to*â is â-â, this means there is nothing to match against.
* âTHISâ = this transaction (i.e., the one with `MTID` + `Txn_Type` from the same row) is the transaction you have just received in the EHI message
* âOTHERâ = the other transaction (in the âMatch toâ column) that is being found by matching (to match to THIS)
* Syntax:  *OTHER.other\_field\_name = THIS.this\_field\_name* where the field names refer to the [GetTransaction Message Fields.](GetTransaction_Message.htm)

| MTID | Txn\_Type | Description | Match to? | Match Criteria |
| --- | --- | --- | --- | --- |
| 0100 | A | Authorisation Request | -  (For an [incremental authorisationClosed A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation. For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.](#), match to Authorisation Request. | OTHER.token=THIS.token  AND  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle    For an incremental authorisation, check for a transaction of `Txn_Type` 'A' arriving with the same `traceid_lifecycle` as a previous authorisation request. For more information, see [What is an incremental authorisation and how do I identify it?](../FAQs.htm#Q.3) |
| - | D | Automatic Authorisation Reversal | Authorisation Request | OTHER.token=THIS.token  AND  OTHER.trans\_link = THIS.trans\_link |
| 0101 | A | Authorisation Repeat (Visa Only)  **Note**: This transaction is uncommon as only a few acquirers use it.  You should respond to a repeat request in the same way as you respond to an original authorisation request. If you decline the repeat authorisation, the terminal may send a new 0100 authorisation, however, you should not assume that this will always occur. | Authorisation Request | OTHER.mtid=â0100â  AND  OTHER.traceid\_lifecycle=THIS.traceid\_lifecycle  AND  OTHER.trans\_link=THIS.trans\_link  AND  OTHER.Ret\_Ref\_No\_DE37=THIS.Ret\_Ref\_No\_DE37  AND  OTHER.TXN\_Time\_DE07=THIS.TXN\_Time\_DE07  AND  OTHER.POS\_Termnl\_DE41=THIS.POS\_Termnl\_DE41  AND  OTHER.Token=THIS.Token |
| 0120 | J | Authorisation Advice | Authorisation Request  (Auth request may not exist) | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  OR (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  OR (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. Normally traceid\_lifecycle will always be present if an authorisation exists. For most authorisation advices, Auth\_Code\_DE38 and trans\_link will probably be missing. |
| 0120 | D | Authorisation reversal due to a 0120 Automated Fuel Dispenser Advice | Authorisation Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. Normally traceid\_lifecycle will always be present if an authorisation exists. |
| 0200 | M | Online Financial Request | - | Only relevant to [Single Message Systems](../Getting_Started/Single_vs_Dual_Message.htm). There are no previous messages to match to. |
| 0220 | Q | Online Financial Advice | Online Financial Request | Only relevant to [Single Message Systems](../Getting_Started/Single_vs_Dual_Message.htm). Match to any previous Online Financial Request or authorisation request if applicable.  OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle=THIS.traceid\_lifecycle  AND (if THIS.trans\_link exists)  OTHER.trans\_link=THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. Normally traceid\_lifecycle will always be present if an online financial request exists. For most online financial advices, Auth\_Code\_DE38 and trans\_link will probably be missing. |
| 0400 | D | Authorisation Reversal Request | Authorisation Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. If the reversal is due to timeout at the acquirer, THIS.traceid\_lifecycle may not exist.  **Note**: The Auth\_Code\_DE38 is not mandatory for Visa authorisation reversal transactions and therefore acquirers can choose to send it or not.; In some cases, the auth code is sent in the original request but not in the authorisation reversal. In this case treat *Auth\_Code\_DE38 = '000000'* as you would do when it is blank. |
| 0420 | D | Authorisation Reversal Advice | Authorisation Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. If the reversal is due to a timeout at the acquirer, THIS.traceid\_lifecycle may not exist. |
| 0420 | V | Online Financial Reversal | Online Financial Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. |
| 0420 | V | Online Financial Reversal | Online Financial Advice | OTHER.token=THIS.token AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_ lifecycle AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  Only relevant to Single Message Systems. Match to any previous Online Financial Request or authorisation request if applicable. |
| 1240  05pp  06pp  07pp    (p=space) | A | Authorisation Advice Notification  (New dummy authorisation created if a financial notification has no matching authorisation.)  1240 for Mastercard  05pp, 06pp or 07pp for Visa where p=space | - | This message should be ignored.  It indicates an offline transaction where Thredd has not received a previous authorisation request. See [First Presentment for an Offline Transaction](../Getting_Started/Transaction_Flow_Scenarios.htm#First).    You will receive the financial notification corresponding to authorisation advice, which has all the information required. |
| 1240 | E | Financial Reversal  Some credit/refund transactions may be reported as MTID â1240â, Txn\_type 'P' (with processing code 20xxxx). | Financial Notification | OTHER.Acquirer\_Reference\_Data\_031 = THIS.Acquirer\_Reference\_Data\_031  AND  OTHER.token=THIS.token  AND  OTHER.Txn\_Amt=THIS.Txn\_Amt  AND  OTHER.Txn\_CCy=THIS.Txn\_CCy  AND  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.POS\_Time\_DE12=THIS.POS\_Time\_DE12  AND  OTHER.Ret\_Ref\_No\_DE37=THIS. Ret\_Ref\_No\_DE37  **Note**: In some cases both OTHER.Auth\_Code\_DE38 and THIS.Auth\_Code\_DE38 are not present. |
| 1240 | C | Chargeback Notification | Financial Notification | OTHER.Acquirer\_Reference\_Data\_031 = THIS.Acquirer\_Reference\_Data\_031  AND  OTHER.token=THIS.token  AND  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  **Note**: In some cases both OTHER.Auth\_Code\_DE38 and THIS.Auth\_Code\_DE38 are not present. |
| 1240 | H | Chargeback Notification (Non-Credit) | Financial Notification | As above (see MTID=1240, Txn\_Type=âCâ) |
| 1240 | K | Chargeback Reversal | Chargeback | As above (see MTID=1240, Txn\_Type=âCâ), except that OTHER (the original to match) will have Txn\_Type of âCâ or âHâ) |
| 1240 | N | Financial Notification (Second Presentment) | Financial Notification and/or Chargeback Notification (Txn\_Type H or N) | As above (see MTID=1240, Txn\_Type=âCâ) |
| 1240 | P | Financial Notification  (First Presentment) | Authorisation  (0100 or 0120) | Rule 1: (reliable match if found, Thredd and acquirer matching data)  OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER.Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  AND  OTHER.TXn\_ID = THIS.Matching\_Txn\_ID  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below )    Rule 2: (run if no match on rule 1, AND THIS.traceid\_lifecycle exists. Uses Acquirer matching data only)  OTHER.token=THIS.token  AND  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below too)    Rule 3: (run if no match on rule 1. Uses Thredd matching data only)  OTHER.token=THIS.token  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER.Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  AND  OTHER.TXn\_ID = THIS.Matching\_Txn\_ID  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below)    **NOTES**  1. The above rules are best advice, but there may be some instances where the authorisation and presentment do not match (due to acquirer inconsistencies).  2. OTHER.trans\_link may not exist if matching to a MTID=0120.  So rule 2 is useful here.  3. Other fields that should normally match include:   * Txn\_Amt (except for tips, partial approval, many-auths to 1 Presentment) * Proc\_Code (but not a 1-to-1 match) * Merch\_ID\_DE42 * POS\_Termnl\_DE41   3. If rule 2 matches and rule 3 does not, (or vice-versa), this indicates an unreliable match. It is up to you if you use the found match or not.  4. Normally traceid\_lifecycle will always be present if an authorisation exists. However, if this is a refund, then there will not be an authorisation with a matching traceid\_lifecycle. |
| 05pp    (p = space) | N | Financial Notification of a Purchase (from Visa)  (Second Presentment) | Prior Financial Notification or Chargeback | As above (see MTID=1240, Txn\_Type=âNâ) |
| 06pp    (p = space) | N | Financial Notification of a Refund or Credit-to-cardholder (from Visa)  (Second Presentment)  Some credit/refund transactions may be reported as MTID â05ppâ, Txn\_type 'P' (with processing code 20xxxx). | Prior Financial Notification or Chargeback | As above (see MTID=1240, Txn\_Type=âNâ) |
| 07pp    (p = space) | N | Financial Notification of a Cash Withdrawal or disbursement (from Visa)  (Second Presentment) | Prior Financial Notification or Chargeback | As above (see MTID=1240, Txn\_Type=âNâ) |
| 05pp    (p = space) | P | Financial Notification of a Purchase (from Visa) | Authorisation | As above (see MTID=1240, Txn\_Type=âPâ) |
| 06pp    (p = space) | P | Financial Notification of a Refund or Credit-to-cardholder (from Visa)  (First Presentment) | Authorisation | As above (see MTID=1240, Txn\_Type=âPâ) |
| 07pp    (p = space) | P | Financial Notification of a Cash Withdrawal or disbursement (from Visa)  (First Presentment) | Authorisation | As above (see MTID=1240, Txn\_Type=âPâ) |
| 25pp    (p = space) | E | Financial Reversal of a Purchase (from Visa)  (First Presentment) | Prior Financial notification (MTID=05) | As 1240 Financial Reversal above (see MTID=1240 Txn\_Type=âEâ)  Note: If you cannot match on Acquirer\_Reference\_Data\_031 then try matching on  traceid\_lifecycle and trans\_link. If you cannot match on these, then try Auth\_Code\_DE38 and Merch\_ID\_DE42. |
| 26pp    (p = space) | E | Financial Reversal of a Refund/Credit-to-cardholder (from Visa) | Prior Financial notification (MTID=06) | As 1240 Financial Reversal above (see MTID=1240 Txn\_Type=âEâ)  Note: If you cannot match on Acquirer\_Reference\_Data\_031 then try matching on  traceid\_lifecycle and trans\_link. If you cannot match on these, then try Auth\_Code\_DE38 and Merch\_ID\_DE42. |
| 27pp    (p = space) | E | Financial Reversal of a Cash Withdrawal/disbursement (from Visa) | Prior Financial notification (MTID=07) | As 1240 Financial Reversal above (see MTID=1240 Txn\_Type=âEâ)  Note: If you cannot match on Acquirer\_Reference\_Data\_031 then try matching on traceid\_lifecycle and trans\_link. If you cannot match on these, then try Auth\_Code\_DE38 and Merch\_ID\_DE42. |
| - | L | Load | - | - |
| - | U | Unload | - | - |
| - | G | Payment | - | - |
| - | B | Balance Adjustment | - | - |
| - | Y | Card Expiry | - | - |
| - | F | Fee | - | - |

#### Resolving Transaction Matching Issues

For more information on resolving matching issues, see [Troubleshooting FAQs: Transactions and Matching](../Troubleshooting_FAQs.htm#Transact).

## 2.2.2 Blocking and Unblocking of Card Funds

When processing and matching transaction messages, you should appropriately apply or remove any card blocks. Below are some guidelines:

* If the authorisation request is for a debit, you should apply a card block to the full billing amount, plus any fees that you or Thredd has applied to the transaction.
* If the authorisation request is a reversal, you should remove the card block for the amount that has been reversed.
* If the authorisation request is for a credit, you can choose to not change any card blocks.

It is important to understand who sent the message before you update the block. Did these originate from the Acquirer, the Network or Thredd?

## 2.2.3 Transaction Processing Summary

The following table summarises how you should process the different types of transactions sent via EHI to the external host. For additional information, see [Transaction Type Decoding](GetTransaction_Message.htm#_Ref448230275).

| MTID | Txn\_Type | Description | Action |
| --- | --- | --- | --- |
| 0100 | A | Authorisation request. | Process normally.  **Note**: if the [traceid\_lifecycle](GetTransaction_Message.htm#traceid_lifecycle) value matches the [traceid\_lifecycle](GetTransaction_Message.htm#traceid_lifecycle) value in a previous 0100 authorisation request, then this is an incremental authorisation.  (Normally a single financial, with the same traceid\_lifecycle, will arrive in this case.) |
|  | D | Automatic authorisation reversal.  Thredd automatically reverses a transaction if it does not receive a presentment transaction from the network within the [hanging filterClosed The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) period.  In the EHI message, all the transaction data fields normally sent by the acquirer (e.g., STAN, RRN, AID and FID) will be identical to the original authorisation request (MTID=0100, Txn\_Type=âAâ). | Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process accordingly. |
| 0101 | A | Authorisation repeat (Visa only) | Match to see if an 0100 original message existed (see above matching criteria table.)   * If you find the 0100 original, this is the \*same\* authorisation. In this case, respond with the original 0100 response (and do not treat this as a new authorisation.) * If you cannot find the 0100 original, this indicates that you did not receive the original 0100 message. In this case, treat this as a new authorisation, and process as with a 0100 message with Txn\_Type=âAâ. |
| 0120 | J | Authorisation advice  Also provided in the following cases:   * Stand-in processing (STIP) by the network. * Automated Fuel Dispenser (AFD) transactions if the final amount is higher than the amount originally authorised in the MTID=0100 Txn\_Type=âAâ authorisation request. | Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process the advice normally. Before blocking any funds you should check the `Resp_Code_DE39` field to determine whether the transaction was [STIPClosed The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer. Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) approved or declined:   * If approved, then replace the existing block for this transaction with a new block for the amount in this advice. * If declined, then remove the block for this transaction.  * If the processing code indicates a credit, you can optionally choose to not change any blocks.   For more information, see [Transaction Matching Guidelines](../Appendices/Transaction_Matching_Guidelines.htm).    **Note**: If a matching authorisation request exists (that needed to be cancelled), then you will separately receive a reversal (e.g. if the original response to the original authorisation request was not sent to the terminal).  The following fields give more information on the advice:   * `Response_Source` - indicates the system that sent the response to the authorisation message * `Response_Source_Why` - indicates the reason for the message response * `Message_Source` - indicates the system that sent the authorisation message * `Message_Why` - indicates the reason for the message response |
| 0120 | D | Authorisation reversal due to an Automated Fuel Dispenser (AFD) 0120 Advice message.  (An AFD sends a 0120 advice to confirm how much fuel was actually dispensed. Thredd sends this to you as a reversal, to reverse the unspent part of the original authorisation from the AFD.) | Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process this reversal accordingly. |
| 0200 | M | Online Financial Request | Process normally. |
| 0220 | Q | Online Financial Advice | If applicable, match to any original online financial request (MTID=0200, Txn\_Type=âMâ) or any previous authorisation request (MTID=0100, Txn\_Type=âAâ) and process the advice normally. Before adjusting any balance on the card you should check the `Resp_Code_DE39` field to determine whether the transaction was [STIPClosed The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer. Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) approved or declined:   * If approved, then adjust the balance on the card according to the amount in this advice if necessary. * If declined, then return any previously deducted amount to the card.  * If the processing code indicates a credit, you should credit the card for this amount.   For more information, see [Transaction Matching Guidelines](../Appendices/Transaction_Matching_Guidelines.htm).    **Note**: If a matching online financial request exists (that needed to be cancelled), then you will separately receive a reversal (e.g. if the original response to the original request was not sent to the terminal).  The following fields give more information on the advice:   * `Response_Source` - indicates the system that sent the response to the online financial request message * `Response_Source_Why` - indicates the reason for the message response * `Message_Source` - indicates the system that sent the message * `Message_Why` - indicates the reason for the message response |
| 0400 | D | Authorisation reversal request  This is a reversal received from the network, to reverse a prior authorisation request (MTID=0100, Txn\_Type=âAâ). | Check you have not already received and processed this reversal. If so, ignore it.  Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process accordingly (unblock the reversal amount)  **Note**: if the Txn\_Amt in the reversal matches the Txn\_Amt in the original authorisation request, then this indicates a full reversal. Unblock whatever was originally blocked.  (The Bill\_Amt in the reversal may slightly differ to the Bill\_Amt in the original due to exchange rate fluctuations.)  **Note**: it is important to apply any blocks due to an 0120 Auth Advice before applying the 0400 reversal. Never unblock more than was currently blocked due to all the messages for the same transaction set.  For more information, see [Transaction Matching Guidelines](../Appendices/Transaction_Matching_Guidelines.htm). |
| 0420 | D | Authorisation reversal advice  This is a reversal received from the network, to reverse a prior authorisation request (MTID=0100, Txn\_Type=âAâ).  This is effectively identical to to above (MTID=0400, Txn\_Type=âDâ), only the MTID is different.  The only reason for the difference is that we are sending the MTID as received from the network, and some network specifications for reversals use 0400, and others use 0420. But there is no effective difference â both should be treated as a reversal advice (as in you cannot decline.)  (Note: Visa use 0400 and 0420. Mastercard use 0400 when originated by the acquirer, and 0420 when originated by the network.) | Check you have not already received and processed this reversal. If so, ignore it.  Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process accordingly (unblock the reversal amount)  **Note**: if the Txn\_Amt in the reversal matches the Txn\_Amt in the original authorisation request, then this indicates a full reversal. Unblock whatever was originally blocked.  (The Bill\_Amt in the reversal may slightly differ to the Bill\_Amt in the original due to exchange rate fluctuations.) |
| 0420 | V | Online Financial Reversal Advice | Check you have not already received and processed this reversal. If so, ignore it.  Match to the original online financial request (MTID=0200, Txn\_Type=âMâ) or online financial advise (MTID=0220, Txn\_Type=âQâ)and process accordingly (apply the reversal amount) |
| 1240  05pp  06pp  07pp    (p = space) | A | Authorisation advice notification  (Dummy authorisation created if a financial notification has no matching authorisation.)  1240 if from Mastercard  05pp, 06pp, or 07pp if from Visa. (p = space) | Discard â this is not needed.  (The purpose of this message is to provide a dummy authorisation to match to a financial notification.) |
| 1240 | E | Financial reversal | Match to a financial notification (MTID=1240, Txn\_Type=âPâ or Txn\_Type=âNâ) and process accordingly |
| 1240 | C | Chargeback notification | Process normally.  (Optionally match to a financial notification (MTID=1240, Txn\_Type=âPâ) or (MTID=1240, Txn\_Type=âNâ)) |
| 1240 | H | Chargeback notification (Non-Credit) | Process normally.  (Optionally match to a financial notification (MTID=1240, Txn\_Type=âPâ) or (MTID=1240, Txn\_Type=âNâ)) |
| 1240 | K | Chargeback reversal | Process normally.  This reverses the effect of a chargeback (e.g., if the chargeback changed the account balance, this reverses the effect on the account balance.)  Optionally match to the chargeback (MTID=1240, (Txn\_Type=âCâ or Txn\_Type=âHâ)) |
| 1240 | N | Financial notification (Second Presentment) | Process normally.  (Optionally match to a financial notification (MTID=1240, Txn\_Type=âPâ) or Chargeback (MTID=1240, Txn\_Type=âHâ / âCâ) |
| 1240 | P | Financial notification  (First Presentment) | Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process accordingly. Note that not all financial notifications will have a matching authorisation. |
| 05pp    (p = space) | N | Financial notification (Second Presentment) | Process normally.  (Optionally match to a financial notification (MTID=05pp, Txn\_Type=âPâ) or Chargeback (MTID=1240, Txn\_Type=âHâ / âCâ) |
| 06pp    (p = space) | N | Financial notification (Second Presentment) | Process normally.  (Optionally match to a financial notification (MTID=06pp, Txn\_Type=âPâ) or Chargeback (MTID=1240, Txn\_Type=âHâ / âCâ) |
| 07pp    (p = space) | N | Financial notification (Second Presentment) | Process normally.  (Optionally match to a financial notification (MTID=07pp, Txn\_Type=âPâ) or Chargeback (MTID=1240, Txn\_Type=âHâ / âCâ) |
| 05pp    (p = space) | P | Financial notification of a purchase (from Visa) | Match to the original authorisation request (MTID=0100, Txn\_Type=âAâ) and process accordingly. Note that not all financial notifications will have a matching authorisation. |
| 06pp    (p = space) | P | Financial notification of a Refund/Credit-to-cardholder (from Visa) | Match to Auth request (MTID=0100, Txn\_Type=âAâ) and process accordingly.  Note that not all Financial Notifications will have a matching Authorisation. |
| 07pp    (p = space) | P | Financial notification of a cash withdrawal/disbursement (from Visa) | Match to Auth request (MTID=0100, Txn\_Type=âAâ) and process accordingly.  Note that not all Financial Notifications will have a matching Authorisation. |
| 25pp    (p = space) | E | Financial reversal of a purchase (from Visa) | Match to financial notification (MTID=â05â, Txn\_Type=âPâ or Txn\_Type=âNâ) and process accordingly |
| 26pp    (p = space) | E | Financial reversal of a refund/credit-to-cardholder (from Visa) | Match to financial notification (MTID=â06â, Txn\_Type=âPâ or Txn\_Type=âNâ) and process accordingly |
| 27pp    (p = space) | E | Financial reversal of a cash withdrawal/disbursement (from Visa) | Match to financial notification (MTID=â07â, Txn\_Type=âPâ or Txn\_Type=âNâ) and process accordingly |
| - | L | Load | Process normally. |
| - | U | Unload | Process normally. |
| - | G | Payment | Process normally. |
| - | B | Balance Adjustment | Process normally. |
| - | Y | Card Expiry | Process normally. |
| - | P | Fee | Process normally  Amounts are in the Fee fields (Bill\_Amt will be zero) |

## 2.2.4 Incremental Authorisations

Visa and Mastercard allow certain merchants â such as hotels, car rental companies and cruise liners â to obtain an estimated initial authorisation when the final amount of the purchase is unknown and to request incremental funds if needed.

You can match incremental authorisations using the `traceid_lifecycle` value; each incremental authorisation will have a different `txn_ID`.

Under normal circumstances Thredd expects, in the same life cycle:

*Final presentment transaction amount = SUM(all approved transaction amounts) â SUM(all reversed transaction amounts)*

#### Example 1

The following scenario illustrates how incremental authorisations work:

* Assume starting blocked amount is zero

  a.    First Authorisation: Â£20  - blocked amount now Â£20

  b.    Incremental Authorisation: Â£30 â blocked amount now Â£50

  c.    Partial Reversal: Â£40 â blocked amount now Â£10

  d.    Presentment would be for Â£10

Note that there is no guarantee the above sums will always add up:

* In all cases, on receipt of the presentment you should unblock the amount that was blocked
* the final presentment amount may be less than expected
* the final presentment amount may be more than expected

Incremental authorisations will have:

* Same Thredd token
* Same currency
* Different `txn_ID`
* Same `traceid_lifecycle`

You can decline any of the incremental authorisations (or all).

## 2.2.5 Exception Transactions

Some transactions may have slightly different rules than expected. This is normally due to waivers granted by the card scheme to permit this.

Below are some examples that Thredd are aware of. For more information on any of the below, or to see if there are any other situations, contact your Issuer.

### Transport for London (United Kingdom of GB and NI) Merchant Transactions

Transport for London (TFL) (London's Public Transport network) have various waivers on authorisation requirements, in order to permit more [offline transactions![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card is not checked in realtime, there is a risk that the card may not have the amount required to cover the transaction.](#) and for amounts larger than usually permitted, after a single approved authorisation request.

#### Example 2

The following example is from Mastercard:

(All of the below have the same `traceid_lifecycle`)

* MTID=0100 authorisation for GBP 6.60, which was approved
* MTID=1240 presentment for GBP 6.60
* MTID=1240 presentment for GBP 5.80
* MTID=1240 presentment for GBP 5.30

Rules differ for UK and non-UK BIN ranges. Check with your Issuer for the latest network rules.

### Other merchants

There may be other examples of merchants with waivers to the normal process.

Contact your Issuer or the network for more information.