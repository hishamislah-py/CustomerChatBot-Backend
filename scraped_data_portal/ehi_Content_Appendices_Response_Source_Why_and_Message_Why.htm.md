# 4.31 Response\_Source\_Why and Message\_Why

This field describes the reason why the response and message source sent the message. It indicates:

* Why the `Response_Source` sent the 0110 response message to the terminal.
* Why the `Message_Source` created this (usually advice/reversal) message in the first place.

It may be present in Authorisation Advice and/or Authorisation Reversal messages.

## 4.31.1 Possible Values

| Why | Description |
| --- | --- |
| 0 | Unknown / not-applicable / not-a-fault |
| 1 | Issuer signed off |
| 2 | Issuer signed off by switch |
| 3 | Issuer communications line down or unavailable |
| 4 | Issuer sent DE39 instruction to force network [Stand In Processing (STIP)Closed The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer. Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) |
| 5 | Issuer timed out |
| 6 | PCAS/Limit-1 diverted (transactions under the limit sent to network STIP) |
| 7 | Issuer is in *Suppress Inquiry* mode |
| 8 | Issuer selected option |
| 9 | MIP/VAP error |
| 10 | Issuer Edit Response Error (if Mastercard, DE60.3 may contain DE in error) |
| 11 | Issuer system error |
| 12 | Network not dispatched error |
| 13 | Issuer undelivered |
| 14 | Direct down option |
| 15 | Network unable to map virtual PAN |
| 16 | Automated Fuel Dispenser (AFD) transaction acquired in USA met Visa Transaction Advisor Service criteria |
| 17 | Visa Payment Controls (VPC) rule |
| 18 | Selective acceptance service |
| 19 | Automated Referral Service |
| 20 | Original processed in STIP |
| 21 | Network Account Management system |
| 22 | PIN verification error |
| 23 | Unable to translate PIN |
| 24 | CVV error |
| 25 | Source or destination does not support service |
| 26 | ARQC verification error |
| 27 | Network error |
| 28 | Network unable to deliver response to acquirer |
| 29 | Duplicate detected by network |
| 30 | Invalid merchant |
| 31 | Network transaction blocking service |
| 32 | Acquirer acknowledgement of 0110 not received |
| 33 | Foreign system sent message |
| 34 | AFD confirmation advice |
| 35 | Exception file maintenance |
| 36 | Reversal matched original authorisation request |
| 37 | No matching original authorisation request found |
| 38 | Issuer notification of token vault provisioned or status change |
| 39 | Issuer notification of card-on-file token issuance |
| 40 | Pay with rewards processing advice to issuer |
| 41 | Network MDES advice to issuer |
| 42 | Authentication advice to issuer |
| 43 | CAT Risk Level 3 |
| 44 | EMV Offline advice to issuer |
| 45 | In-Control processing advice to issuer |
| 46 | Adminstrative text message |
| 47 | Transaction voided by customer |
| 48 | Transaction not completed |
| 49 | No confirmation from terminal |
| 50 | Partial Reversal |
| 51 | Payment Token Status Change  In this case (MTID=â0100â, Txn\_Type=âAâ, Proc\_Code=â360000â Token Event Notification) it indicates that the `PaymentToken_creatorStatus` has been changed by the payment token creator.  The Thredd status may also have changed too.   * `PaymentToken_id` - indicates which payment token the status change is for * `PaymentToken_creatorStatus` - indicates the new status as set by the creator * `PaymentToken_status` - indicates the current Thredd status as set on [Thredd PortalClosed Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or [Smart ClientClosed Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#) |
| 52 | Payment Token Replaced  In this case (MTID=â0100â, Txn\_Type=âAâ, Proc\_Code=â360000â Token Event Notification) it indicates that a new payment token has been digitised (i.e. personalised) with the following properties:   * There was already a previously digitised payment token on the same device * The properties of the new digitised token as the same as the previous one, except that the expiry date has been updated. * `PaymentToken_id` is the same (as same underlying payment token entry on the Thredd system) * `PaymentToken_expdate` has the new payment token expiry date * The previous expiry date is not included (if this is required, you should request it) |
| 53 | Activation code expired (e.g. for a payment token activation) |
| 54 | Activation code wrong (e.g. for a payment token activation) |
| 55 | Activation code maximum attempts exceeded (e.g. for a payment token activation) |
| 56 | Incremental authorisation |
| 57 | Resubmission |
| 58 | Delayed charges |
| 59 | Re-authorisation |
| 60 | No show |
| 61 | Account top up |
| 62 | Consumer Transaction Controls service |
| 63 | Dispute financial |
| 64 | Recurring payment Blocking Service |
| 65 | Merchant country on Issuers exclusion list |
| 66 | Office of Foreign Assets Control (OFAC) embargo |
| 67 | Cashback processing error |
| 68 | Invalid CAVV |
| 69 | Luhn check digit failure |
| 70 | Issuer does not support gambling transactions |
| 71 | Payment token created |
| 72 | Payment token provisioning result |
| 73 | Payment token activation code verification result |
| 74 | Payment token call centre activation result |
| 75 | Payment token mobile banking activation result |
| 76 | Payment token [EMVClosed EMV originally stood for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.](#) session keys replenishment confirmation |
| 77 | Payment token provisioning-update results |
| 78 | PAN expiry date changed |
| 79 | PAN replaced |
| 80 | Payment token activated |
| 81 | Payment token suspended |
| 82 | Payment token deactivated |
| 83 | Network Payment Fraud Disruption service |
| 84 | Payment-Token Device binding |
| 85 | Payment-Token Device binding removed |
| 86 | Payment-Token Device binding complete without authentication |
| 87 | Payment-Token Device binding activation code verification result |
| 88 | Payment-Token Device binding call centre activation result |
| 89 | Payment-Token Device binding mobile banking verification result |
| 90 | Cardholder verification complete without authentication |
| 91 | Cardholder verification activation code verification result |
| 92 | Cardholder verification call centre activation result |
| 93 | Cardholder verification mobile banking activation results |
| 94 | Payment-Token re-personalised after personalisation data update |
| 95 | Payment-Token expiry date updated |
| 96 | Deferred Authorisation. (i.e. authorisation is received a long time after the cardholder interacted with the terminal. Could easily be many hours later. Common for mass-transit transactions, such as commuter railways and buses.) |
| 97 | Acquirer authorisation advice (Merchant/Acquirer approved authorisation offline) |
| 100 | Device binding with FIDO intent. |
| 101 | Device binding â implicit green flow. |
| other | Ask Thredd for updated information codes |

|  |  |
| --- | --- |