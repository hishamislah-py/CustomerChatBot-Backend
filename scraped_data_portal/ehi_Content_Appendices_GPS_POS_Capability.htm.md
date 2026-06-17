# 4.12 GPS\_POS\_Capability field

This is a Thredd defined field that records POS terminal capabilities for this transaction. It is made up of various subfields.

## 4.12.1 GPS\_POS\_Capability Fields

Refer to the table below for details

All subfields are concatenated together in order. Subfields begin at position 1. You may only receive the leading subfields (i.e. 1 or more). Additional subfields may be added.

| Position | Name | Format | Description / Valid Values |
| --- | --- | --- | --- |
| 1 | Partial Approval Support | N(1,1) | Indicates if POS terminal supports partial approval or not:  0 = not supported (default assumption)  1 = supported |
| 2 | Purchase Amount only approval support | N(1,1) | Indicates if POS terminal supports approval of the purchase amount only, in a purchase with cashback transaction.  0 = not supported (default assumption)  1 = supported |
| 3 to 22 | Card Data Input Capability | AN(20,20) | Card Data Input methods supported by the terminal.  1 position for each possible method.  Each position is set to: 1=Supported, 0=Not supported  See [Card Data Input Capability subfield](#_Ref498357189) |
| 23 to 42 | Cardholder authentication capability | AN(20,20) | Cardholder authentication methods supported by the terminal.  1 position for each possible method.  Each position is set to: 1=Supported, 0=Not supported  See [Cardholder Authentication Capability subfield](#_Ref498357204) |
| 43 | Card capture capability | AN(1,1) | 0 = Card capture not supported  1 = Card capture supported  9 = Unknown |
| 44 | Terminal Attended indicator | AN(1,1) | Indicates if the terminal is attended by the merchant  0 = No terminal used  1 = Attended  2 = Unattended  9 = Unknown  **Note**: On Visa card transactions, the information in GPS\_POS\_Capability position 44 should not be relied on, as merchants/Acquirers do not always submit the correct information. |
| 45 | Terminal Environment | AN(1,1) | Indicates the Terminal Environment or Location-type  0 = No terminal used  1 = On premises of card acceptor  2 = Off premises of card acceptor  3 = On premises of cardholder  9 = Unknown |
| 46 | Terminal Card Data Output Capability | AN(1,1) | Indicates the ability of the terminal to write to the card  0 = Unknown  1 = None  (eg if no terminal used)  2 = Magnetic Stripe Write  3 = ICC  S = Other |
| 47 | Terminal output capability | AN(1,1) | Indicates the output capabilities of the terminal  0 = Unknown  1 = None  2 = Print only  3 = Display only  4 = Print and Display |
| 48 | Terminal PIN capture capability | AN(1,1) | Terminal PIN Capture Capability.  Says if the terminal can capture PINs, and if so, the maximum length of PIN supported:  0 = None  1 = Unknown  4 = Yes, max length 4 digits  5 = Yes, max length 5 digits  6 = Yes, max length 6 digits  7 = Yes, max length 7 digits  8 = Yes, max length 8 digits  9 = Yes, max length 9 digits  A = Yes, max length 10 digits  B = Yes, max length 11 digits  C = Yes, max length 12 digits |
| 49 | Terminal Type | AN(1,1) | Defines what sort of terminal this is.  (here âCATâ means Cardholder Activated Terminal.)  0 = Unknown/Unspecified  1 = CAT level 1 â Automated Dispensing Machine  2 = CAT level 2 â self-service terminal  3 = CAT level 3 â Limited Amount Terminal  4 = CAT level 4 â In-flight commerce terminal  5 = CAT level 5  6 = CAT level 6 â e-commerce terminal  7 = CAT level 7 â Transponder  8 = Remote Terminal (eg Mastercard Tap to More transaction)  9 = Mobile POS acceptance device  M = Manual (no terminal used)  A = ATM  R = Electronic Cash Register or normal attended POS device |

## 4.12.2 Card Data Input Capability subfield

This describes the âCard Data Input Capabilityâsubfield of `GPS_POS_Capability`. See above.

Card Data Input Capability is a 20 character field. Each position represents a different capability, with a value set to either:  1=Supported or 0=Not supported.

See the table below.

| GPS\_POS\_Capability position | Card Data Input Capability position | Name |
| --- | --- | --- |
| 3 | 1 | Unknown |
| 4 | 2 | Manual (eg zip-zap); no terminal or server |
| 5 | 3 | Magnetic Stripe |
| 6 | 4 | Barcode |
| 7 | 5 | OCR |
| 8 | 6 | EMV contact |
| 9 | 7 | PAN Key Entry |
| 10 | 8 | Contactless Magnetic Stripe |
| 11 | 9 | EMV contactless or qVSDC contactless |
| 12 | 10 | Account Data on File |
| 13 | 11 | QR code |
| 14 | 12 | E-Commerce |
| 15 | 13 | E-Commerce with EMV cryptogram |
| 16 | 14 | MICR reader |
| 17 | 15 | Reserved |
| 18 | 16 | Reserved |
| 19 | 17 | Reserved |
| 20 | 18 | Reserved |
| 21 | 19 | Reserved |
| 22 | 20 | Reserved |

#### Example 1

If `GPS_POS_Capability` *= â11001001000100000000000100100101000000000019234CRâ* then this indicates that the following card data input capabilities are supported:  Magnetic Stripe, EMV contact, Account Data on File.

## 4.12.3 Cardholder Authentication Capability subfield

Positions 23 to 42 inside the `GPS_POS_Capability` field represent the Cardholder Authentication Capabilities.

The table defines which Cardholder Authentication Capability is defined by each position. Each positionâs value is set to either:  1=Supported, or 0=Not supported / unknown.

| GPS\_POS\_Capability position | Cardholder authentication Capability position | Name |
| --- | --- | --- |
| 23 | 1 | None |
| 24 | 2 | PIN (online or offline) |
| 25 | 3 | Electronic signature analysis |
| 26 | 4 | biometrics |
| 27 | 5 | biographic |
| 28 | 6 | Manual signature verification |
| 29 | 7 | Manual other (eg drivers licence / ID card) |
| 30 | 8 | Offline PIN |
| 31 | 9 | Online PIN |
| 32 | 10 | 3D-Secure |
| 33 | 11 | Account based digital signature |
| 34 | 12 | Public key based digital signature |
| 35 | 13 | Unknown |
| 36 | 14 | Reserved |
| 37 | 15 | Reserved |
| 38 | 16 | Reserved |
| 39 | 17 | Reserved |
| 40 | 18 | Reserved |
| 41 | 19 | Reserved |
| 42 | 20 | Reserved |

#### Example 2

If `GPS_POS_Capability` = â11001001000100000000000100100101000000000019234CRâ this indicates that the following Cardholder authentication methods are supported: PIN, biographic, Offline PIN, 3D-secure.

## 4.12.4 Full GPS\_POS\_Capability example

If `GPS_POS_Capability` = â11001001000100000000000100100101000000000019234CRâ

Then this indicates:

| Position | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Partial approval supported |
| 2 | 1 | Purchase amount only approval supported |
| 3 | 0 | Card data input capability not unknown |
| 4 | 0 | Card data input by manual not supported |
| 5 | 1 | Card data input by magnetic stripe supported |
| 6 | 0 | Card data input by barcode not supported |
| 7 | 0 | Card data input by OCR not supported |
| 8 | 1 | Card data input by EMV contact supported |
| 9 | 0 | Card data input by PAN key entry not supported |
| 10 | 0 | Card data input by Contactless Magnetic stripe not supported |
| 11 | 0 | Card data input by EMV contactless not supported |
| 12 | 1 | Card data input by Account Data on file supported |
| 13 | 0 | Card data input by QR code not supported |
| 14 | 0 | Card data input by E-commerce not supported |
| 15 | 0 | Card data input by E-commerce with EMV not supported |
| 16 | 0 | Card data input by MICR reader not supported |
| 17 | 0 | Reserved for future use. |
| 18 | 0 | Reserved for future use. |
| 19 | 0 | Reserved for future use. |
| 20 | 0 | Reserved for future use. |
| 21 | 0 | Reserved for future use. |
| 22 | 0 | Reserved for future use. |
| 23 | 0 | No Cardholder authentication at all is not supported |
| 24 | 1 | Cardholder authentication by PIN supported |
| 25 | 0 | Cardholder authentication by Electronic signature analysis not supported |
| 26 | 0 | Cardholder authentication by biometrics not supported |
| 27 | 1 | Cardholder authentication by biographic supported |
| 28 | 0 | Cardholder authentication by manual signature not supported |
| 29 | 0 | Cardholder authentication by manual (other) not supported |
| 30 | 1 | Cardholder authentication by offline PIN supported |
| 31 | 0 | Cardholder authentication by online PIN not supported |
| 32 | 1 | Cardholder authentication by 3D-secure supported |
| 33 | 0 | Cardholder authentication by Account based digital signature not supported |
| 34 | 0 | Cardholder authentication by Public key based digital signature not supported |
| 35 | 0 | Cardholder authentication by unknown means not indicated |
| 36 | 0 | Reserved for future use. |
| 37 | 0 | Reserved for future use. |
| 38 | 0 | Reserved for future use. |
| 39 | 0 | Reserved for future use. |
| 40 | 0 | Reserved for future use. |
| 41 | 0 | Reserved for future use. |
| 42 | 0 | Reserved for future use. |
| 43 | 1 | Card capture supported |
| 44 | 9 | Unknown if terminal is attended |
| 45 | 2 | Terminal is off premises of card acceptor |
| 46 | 3 | Terminal supports card output by ICC writing |
| 47 | 4 | Terminal has Print and Display capability |
| 48 | C | Terminal can capture up to 12 digit PINs |
| 49 | R | Terminal is a normal POS or cash register |