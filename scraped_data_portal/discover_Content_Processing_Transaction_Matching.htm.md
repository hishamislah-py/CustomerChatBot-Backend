# 4 Transaction Matching

A typical card payment transaction generates multiple messages during its life cycle. The `GetTransaction` message types you receive for a transaction must be linked to the previous messages for that transaction. This matching enables you to track the history of the transaction, compare the financial effect of a new messages with previous messages and re-calculate card balances.

In Full Service Processing (mode 3) and Cooperative Processing (mode 2), Thredd manages transaction matching.

The matching examples below are for customers connecting to Discover networks. Only transaction types supported in Discover Phase 1 are shown.

## 4.1 Matching Overview

Your systems should match new to previous transactions as follows:

![](../Resources/Images/Transaction_Matching_Discover.png "Transaction matching")

Figure 10: Transaction Matching Criteria for Discover Networks

For further details, see the [Transaction Matching Criteria](#Transact) below.

Where 3D Secure authentication applies, additional transaction matching should be performed to match details in the authorisation to the 3D Secure authentication details. For detail see [External Host Interface (EHI) Guide > Transaction Matching - Authentications and Authorisations](https://docs.thredd.com/ehi/Content/Appendices/Transaction_Matching_Guidelines.htm).

### Matching Criteria and Accuracy

Matching a transaction to its original (e.g., *Presentment* to matching *Authorisation*, or *Authorisation Reversal* to matching *Authorisation*) is based on the information received. In most cases transactions match. However, acquirers do not always send accurate information, so mistakes can occur.[1  Discover Network does not verify whether acquirer information matches, so data from the acquirer may be inaccurate.](#)

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
* Syntax:  *OTHER.other\_field\_name = THIS.this\_field\_name*  where the field names refer to the [GetTransaction Message Fields.](../Appendices/GetTransaction_Message.htm)

| MTID | Txn\_Type | Description | Match to? | Match Criteria |
| --- | --- | --- | --- | --- |
| 0100 | A | Authorisation Request | -  (For an [incremental authorisationClosed A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation. For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.](#), match to Authorisation Request) | OTHER.token=THIS.token  AND  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle |
| - | D | Automatic Authorisation Reversal | Authorisation Request | OTHER.token=THIS.token  AND  OTHER.trans\_link = THIS.trans\_link |
| 0120 | J | Authorisation Advice | Authorisation Request  (Auth request may not exist) | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. Normally traceid\_lifecycle will always be present if an authorisation exists. For most authorisation advices, Auth\_Code\_DE38 and trans\_link will probably be missing. |
| 0120 | D | Authorisation reversal due to a 0120 Automated Fuel Dispenser Advice | Authorisation Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. Normally traceid\_lifecycle will always be present if an authorisation exists. |
| 0420 | D | Authorisation Reversal Advice | Authorisation Request | OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND (if THIS.trans\_link exists)  OTHER.trans\_link = THIS.trans\_link  **Note**: If neither THIS.traceid\_lifecycle or THIS.trans\_link is present, then there is no match. If the reversal is due to a timeout at the acquirer, THIS.traceid\_lifecycle may not exist. |
| 1240 | A | Authorisation Advice Notification  (New dummy authorisation created if a financial notification has no matching authorisation.) | - | This message should be ignored.  It indicates an offline transaction where Thredd has not received a previous authorisation request.    You will receive the financial notification corresponding to authorisation advice, which has all the information required. |
| 1240 | E | Financial Reversal | Financial Notification | OTHER.Acquirer\_Reference\_Data\_031 = THIS.Acquirer\_Reference\_Data\_031  AND  OTHER.token=THIS.token  AND  OTHER.Txn\_Amt=THIS.Txn\_Amt  AND  OTHER.Txn\_CCy=THIS.Txn\_CCy  AND  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.POS\_Time\_DE12=THIS.POS\_Time\_DE12  AND  OTHER.Ret\_Ref\_No\_DE37=THIS. Ret\_Ref\_No\_DE37  **Note**: In some cases both OTHER.Auth\_Code\_DE38 and THIS.Auth\_Code\_DE38 are not present. |
| 1240 | C | Chargeback Notification | Financial Notification | OTHER.Acquirer\_Reference\_Data\_031 = THIS.Acquirer\_Reference\_Data\_031  AND  OTHER.token=THIS.token  AND  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  **Note**: In some cases both OTHER.Auth\_Code\_DE38 and THIS.Auth\_Code\_DE38 are not present. |
| 1240 | H | Chargeback Notification (Non-Credit) | Financial Notification | As above (see MTID=1240, Txn\_Type=âCâ) |
| 1240 | K | Chargeback Reversal | Chargeback | As above (see MTID=1240, Txn\_Type=âCâ), except that OTHER (the original to match) will have Txn\_Type of âCâ or âHâ) |
| 1240 | N | Financial Notification (Second Presentment) | Financial Notification and/or Chargeback Notification (Txn\_Type H or N) | As above (see MTID=1240, Txn\_Type=âCâ) |
| 1240 | P | Financial Notification  (First Presentment) | Authorisation  (0100 or 0120) | Rule 1: (reliable match if found, Thredd and acquirer matching data)  OTHER.token=THIS.token  AND (if THIS.traceid\_lifecycle exists)  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER.Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  AND  OTHER.TXn\_ID = THIS.Matching\_Txn\_ID  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below )    Rule 2: (run if no match on rule 1, AND THIS.traceid\_lifecycle exists. Uses Acquirer matching data only)  OTHER.token=THIS.token  AND  OTHER.traceid\_lifecycle = THIS.traceid\_lifecycle  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER. Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below too)    Rule 3: (run if no match on rule 1. Uses Thredd matching data only)  OTHER.token=THIS.token  AND (if THIS.Auth\_Code\_DE38 exists)  OTHER.Auth\_Code\_DE38 = THIS.Auth\_Code\_DE38  AND  OTHER.trans\_link = THIS.trans\_link  AND  OTHER.TXn\_ID = THIS.Matching\_Txn\_ID  AND OTHER.Txn\_CCy = THIS.Txn\_CCy  (see notes below)    **NOTES**  1. The above rules are best advice, but there may be some instances where the authorisation and presentment do not match (due to acquirer inconsistencies).  2. OTHER.trans\_link may not exist if matching to a MTID=0120.  So rule 2 is useful here.  3. Other fields that should normally match include:   * Txn\_Amt (except for tips, partial approval, many-auths to 1 Presentment) * Proc\_Code (but not a 1-to-1 match) * Merch\_ID\_DE42 * POS\_Termnl\_DE41   3. If rule 2 matches and rule 3 does not, (or vice-versa), this indicates an unreliable match. It is up to you if you use the found match or not.  4. Normally traceid\_lifecycle will always be present if an authorisation exists. However, if this is a refund, then there will not be an authorisation with a matching traceid\_lifecycle. |
| - | L | Load | - | - |
| - | U | Unload | - | - |
| - | G | Payment | - | - |
| - | B | Balance Adjustment | - | - |
| - | Y | Card Expiry | - | - |
| - | F | Fee | - | - |