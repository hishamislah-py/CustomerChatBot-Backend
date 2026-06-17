# 4.31 Response\_Source and Message\_Source

This field is used to identify the source (originator) of the message. It indicates:

* Who sent the 0110 response message to the terminal (`Response_Source`)
* Who sent this (usually advice/reversal) message in the first place (`Message_Source`)
* Who created the payment token (`PaymentToken_creator`)

`Response_Source` and `Message_Source` may be present in the Authorisation Advice and/or Authorisation Reversal messages.

## 4.31.1 Possible Values

| Source | Description |
| --- | --- |
| UNKNOWN | Unknown or not applicable |
| ISSUER | Thredd Issuer Auth System (primary site) |
| ISSUER-ALT | Alternate Issuer System (Secondary site) |
| ACQUIRER | Acquirer |
| TERMINAL | Terminal |
| CARD | Chip Card |
| EHI | Issuer PM Host via EHI connection |
| ACQ-MC-X | Acquirer X-Code (Mastercard) |
| MC-X | Mastercard X-Code at acquirer [MIPClosed Mastercard Interface Processor (MIP) The processing hardware and software system that interfaces with Mastercard's Global Payment System communications network.](#) |
| MC-STIP | Mastercard [Stand-In processingClosed The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer. Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) |
| VISA-STIP | Visa Stand-In processing |
| VISA-IARS | Visa International Automated Referral Service |
| MC-ICPS | Mastercard in-control processing service |
| MC-PREVAL | Mastercard pre-validation services |
| MC-BLOCK | Mastercard transaction blocking service |
| MC-RPCS | Mastercard Recurring Payment cancellation service |
| MC-MDES | Mastercard tokenisation system (MDES) |
| CARD-APP | Application running on cardholderâs card device (e.g. phone application) |
| VISA-T | Visa Tokenisation system (Visa Europe/International Token Service) |
| CARD-WAL | Wallet application running on cardholderâs card device (e.g. phone) |
| WALLET | Wallet Service Provider (generic) systems - not on cardholder device (e.g. WAL-AP or WAL-AN or WAL-SA) |
| WAL-AP | Apple Wallet Systems (Apple servers - not on cardholder device) |
| WAL-AN | Android Wallet Systems (Google servers - not on cardholder device) |
| WAL-SA | Samsung Wallet Systems (Samsung servers - not on cardholder device) |
| CRDHLR | Cardholder |
| MC | Mastercard |
| VISA | Visa |