# 4.16 Mastercard\_AdviceReasonCode\_DE60

The `Mastercard_AdviceReasonCode_DE60` field is present for `MTID`=â0120â (Authorisation Advice) and `MTID`=â0420â (Reversal Advice) transactions on Mastercard. In both cases it provides information on why the advice was generated.

Mastercard may add, remove or change any of the values at any time.

The field is divided into three parts:

| Position | Length | Format | Description |
| --- | --- | --- | --- |
| 1 to 3 | 3 | N(3,3) | Advice Reason Code â reason why this advice was created  See [Positions 1-3 Advice Reason Code](#_Ref41058597) |
| 4 to 7 | 4 | N(4,4) | Advice Detail Code â May be present (depending on the Advice Reason Code) providing additional information.  See [Positions 4-7 Advice Detail Code](#_Ref41058661) |
| 8 to the end | 1 to 53 | ANS(1,53) | Advice Detail Text â May be present (depending on the Advice Reason Code) providing additional information as human readable format. |

## 4.16.1 Positions 1-3 Advice Reason Code

Provides three digits to describe why the MTID=0120 or MTID=0420 advice was created. See the table below.

Not all the codes below are applicable, for example: some may only apply to Acquirers, and some only apply to services you may not be using.   
      â¢  *Alternate Issuer Route* refers to the Mastercard STIP system.   
      â¢  *MIP* is part of the Mastercard system. The Acquirer is connected to one [MIP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Mastercard Interface Processor (MIP)
The processing hardware and software system that interfaces with Mastercard's Global Payment System communications network.](#), Issuer (Thredd) is connected to another MIP.

| Advice Reason Code | Meaning |
| --- | --- |
| 100 | Alternate Issuer Route: Issuer selected option |
| 101 | Alternate Issuer Route: IPS signed out |
| 102 | Alternate Issuer Route: IPS timed out |
| 103 | Alternate Issuer Route: IPS unavailable |
| 105 | Transaction processed via X-Code (i.e., Mastercard processed this at their Acquiring MIP). |
| 107 | PIN processing error |
| 108 | Alternate Issuer Route: MIP Error |
| 109 | Alternate Issuer Route: Issuer Edit Response Error |
| 111 | Alternate Issuer Route: Issuer Host System Error |
| 112 | Alternate Route: Network Not Dispatched Error |
| 113 | Alternate Route: Issuer Undelivered |
| 114 | Alternate Route: Direct Down Option |
| 115 | Transaction Processed via On-behalf Service Decision |
| 116 | Invalid Merchant |
| 120 | Transaction Blocking ( blocked by a Mastercard Fraud System; this normally configured with your issuer; Thredd is not involved .) |
| 121 | Account Lookup Service |
| 126 | Pay with Rewards Processing Advice to Issuer |
| 140 | Unable to convert contactless or virtual account  number |
| 141 | Mastercard Digital Enablement Service Advice to Issuer |
| 150 | Mastercard Transaction blocking for Mastercard Send or other transaction blocking service. |
| 151 | In Control Processing Advice to Issuer (Mastercard  Merchant Presented QR) |
| 160 | Authentication Advice to Issuer |
| 180 | CAT Risk Level 3 |
| 190 | Acquirer Processing System (APS) Approved |
| 191 | Acquirer Processing System (APS) Completed  Authorization Transaction |
| 192 | M/Chip Offline Advice to Issuer |
| 200 | In Control Processing Advice to Issuer |
| 400 | Unable to deliver response from Mastercard to Acquirer |
| 401 | No acknowledgement from Acquirer to Mastercard |
| 402 | Issuer Time-out |
| 403 | Issuer Signed out |
| 409 | Issuer Response Error |
| 410 | Reversal message provided by a system other than Mastercardâs online authorisation system (Banknet) |
| 413 | Issuer Undelivered |
| other | Mastercard may add other values when they please |

## 4.16.2 Positions 4-7 Advice Detail Code

This is a 4 digit number which may be present, providing additional information, as follows:

| Advice Detail Code | Meaning |
| --- | --- |
| 0000 | Accepted/Approved |
| Any other code | Reason why transaction was declined.    There are too many codes to practically put them in this specification, if you want to know a particular value, if you have access to the Mastercard Customer Interface Specification you can look in there, otherwise you can ask Thredd. |