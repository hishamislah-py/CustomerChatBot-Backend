# 4.25 POS\_Data\_DE22 in Authorisation Messages

The POS Entry Mode and POS PIN Capture capability field (`POS_Data_DE22`) is made up of various subfields. (See also [Get Transaction Message fields: POS\_Data\_DE22](../Requirements/GetTransaction_Message.htm#POS_Data_DE22))

Similar values are used by Visa and Mastercard, but there are some subtle differences. The differences for each are described in the tables below.

## 4.25.1 POS\_Data\_DE22 Layout Format

The field for Mastercard Authorisation Messages consists of 3 decimal digits as follows:

| Position | Length | Description |
| --- | --- | --- |
| 1-2 | 2 | PAN Entry Method  See [POS\_Data\_DE22 positions 1-2: PAN Entry Method](#_Ref41580122) |
| 3 | 1 | PIN Entry Capability  See [POS\_Data\_DE22 positions 3: Terminal PIN Entry Capability](#_Ref41580135) |

The field for Visa Authorisation Messages consists of 4 decimal digits as follows:

| Position | Length | Description |
| --- | --- | --- |
| 1-2 | 2 | PAN Entry Method  See [[POS\_Data\_DE22 positions 1-2: PAN Entry Method](#top)](#_Ref41580122) |
| 3 | 1 | PIN Entry Capability  See [POS\_Data\_DE22 positions 3: Terminal PIN Entry Capability](#_Ref41580135) |
| 4 | 1 | Filler â value â0â |

## 4.25.2 POS\_Data\_DE22 positions 1-2: PAN Entry Method

A normalised value to identify the Card Data Input Method can be found in GPS\_POS\_Data field, in position 3. See [GPS\_POS\_Data field](GPS_POS_Data.htm) for more information.

This field is formatted as follows:

| Value | Mastercard Description | Visa Description |
| --- | --- | --- |
| 00 | Unknown or no terminal | Unknown or terminal not used |
| 01 | Manual Key Entry | (manual key entry) for application-based e-commerce transactions, and card-not-present transactions initiated with a token |
| 02 | Partial Magnetic Stripe Read | Magnetic stripe read; CVV checking may not be possible Plus transactions: Exact Track 2 contents read, but transaction is not eligible for CVV checking |
| 03 | Barcode | Optical code |
| 04 | OCR | Not valid |
| 05 | Contact EMV ICC | Integrated circuit card read; CVV or iCVV checking is possible |
| 07 | Contactless EMV ICC | (contactless chip using VSDC rules) for transactions at contactless-enabled devices with a mobile-issued token payment |
| 10 | Credential-on-file  Indicates a Merchant is initiating a transaction on behalf of the Cardholder using credentials stored on file. | Credential-on-file  Indicates a Merchant is initiating a transaction on behalf of the Cardholder using credentials stored on file. |
| 79 | PAN+expdate key entered by Acquirer (PAN+expdate read from Magnetic Stripe and communicated verbally to acquirer who keyed in the transaction.  Neither Track1 or Track2 will be present.) | Not valid |
| 80 | Magnetic Stripe (fallback from EMV ICC) | Not valid |
| 81 | e-commerce | Not valid |
| 82 | PAN data on file | Not valid |
| 90 | Magnetic Stripe Read | (magnetic stripe read; CVV check is possible; exact content of Track 1 or Track 2 included) |
| 91 | Contactless Magnetic Stripe | (contactless chip using magnetic stripe data rules) for transactions at contactless-enabled devices with a mobile-issued token payment |
| 95 | Contact EMV ICC (something unreliable) | Integrated circuit card read; CVV or iCVV checking may not be possible |
| 96 | Stored Value from pre-registered checkout service | Not valid |

## 4.25.3 POS\_Data\_DE22 positions 3: Terminal PIN Entry Capability

A normalised value to identify if the terminal supports PIN entry can be found in GPS\_POS\_Capability field, specifically in positions 24, 30, 31 and 48. See [GPS\_POS\_Capability field](GPS_POS_Capability.htm) for more information.

This describes the capability of the Terminal to accept a PIN. The field is formatted as follows:

| Value | Mastercard Description | Visa Description |
| --- | --- | --- |
| 0 | Unknown | Unknown |
| 1 | Terminal supports PIN. | Indicates that the point-of-transaction terminal can accept and forward an online PIN. |
| 2 | Terminal does not support PIN. | Indicates that the point-of-transaction terminal cannot accept and forward an online PIN. |
| 8 | Terminal supports PIN, but PIN pad is not working. | Terminal PIN pad is down |