# 4.39 Visa\_POS\_Data\_DE60

The `Visa_POS_Data_DE60` field contains the raw Visa POS data Thredd received in Visa online authorisation related messages.  It can be useful for diagnosis in exception cases. Thredd processes this field to set the `GPS_POS_Data` and `GPS_POS_Capability` fields.

The values supplied in this field are subject to change by Visa. We advise you not to configure your systems to make decisions based on this field.

## 4.39.1 Visa\_POS\_Data\_DE60 Positions

Each different position holds a different piece of POS information. Note that not all positions may arrive.

For more information on this field, refer to Visa.  Only a summary of the relevant values are given below.

The position is the character offset in the field; the first character is âposition 1â.

| Position | Description | More Information |
| --- | --- | --- |
| 1 | Terminal Type | See [Position 1 â Terminal Type](#Position) |
| 2 | Terminal Entry Capability | See [Position 2 â Terminal Entry Capability](#Position2) |
| 3 | Chip Condition Code | See [Position 3 â Chip Condition Code](#Position3) |
| 4 | Special Condition indicator â existing debt | See [Position 4 â Special condition (existing debt)](#Position4) |
| 5 â 6 | RFU |  |
| 7 | Chip Transaction Indicator | See [Position 7 â Chip Transaction indicator](#Position5) |
| 8 | Chip Card Authentication reliability indicator | See [Position 8 â Chip card authentication reliability indicator](#Position6) |
| 9 â 10 | Mail/Phone/E-Commerce/Payment indicator | See [Position 9-10 â Mail/Phone/E-Commerce/Payment indicator](#Position7) |
| 11 | Cardholder ID method indicator | See [Position 11 â Cardholder ID Method Indicator](#Position8) |
| 12 | Additional authorisation indicators | See [Position 12 â Additional Authorisation Indicators](#Position9) |
| 13 and up | Unknown | Reserved for future use |

## 4.39.2 Position 1 â Terminal Type

| Value | Description |
| --- | --- |
| 0 | Unspecified |
| 1 | Unattended cardholder-activated, no authorization, below-floor-limit transaction (not allowed in zero floor markets) |
| 2 | ATM |
| 3 | Unattended cardholder-activated, authorized transaction |
| 4 | Electronic cash register |
| 5 | Home terminals, which include personal computers, personal digital assistants, interactive televisions, and telephones |
| 7 | Telephone device (including Visa dial terminals) |
| 8 | Reserved for future use |
| 9 | Mobile acceptance solution (mPOS) |
| Any other value | Unknown |

## 4.39.3 Position 2 â Terminal Entry Capability

| Value | Description |
| --- | --- |
| 0 | Unknown |
| 1 | Terminal not used |
| 2 | Magnetic Stripe read capability |
| 3 | Barcode read capability |
| 4 | OCR-read capability |
| 5 | Chip-capable terminal |
| 8 | Proximity-read-capable terminal |
| 9 | Terminal does not have the capability to read card data |
| Any other value | Unknown |

## 4.39.4 Position 3 â Chip Condition Code

| Value | Description |
| --- | --- |
| 0 | Not applicable |
| 1 | Transaction was initiated from a magnetic stripe with a service code beginning with 2 or 6 and the last read at VSDC terminal was a successful chip read or was not a chip transaction |
| 2 | Transaction was initiated at a chip-capable terminal from a magnetic stripe that contains service code 2 or 6, and the previous transaction initiated by that terminal was an unsuccessful chip read. |
| Any other value | Unknown |

## 4.39.5 Position 4 â Special Condition (existing debt)

| Value | Description |
| --- | --- |
| 0 | Default value |
| 1 | Purchase of Central Bank Digital Currency (CBDC) or tokenized depositsCentral Bank Digital Currency (CBDC) or tokenized deposits |
| 2 | Purchase of Stablecoin (Fiat-backed) |
| 3 | Purchase of Blockchain Native Token/Coin |
| 4 | Purchase of Non-Fungible Token (NFT) |
| 7 | Purchase of Cryptocurrency |
| 8 | Quasi-Cash |
| 9 | Existing debt indicator |
| Any other value | Unknown |

## 4.39.6 Position 7 â Chip Transaction Indicator

| Value | Description |
| --- | --- |
| 0 | Not applicable |
| 1 | Standard third bitmap or field 55 used to submit chip data |
| 2 | Expanded third bitmap used to submit chip data |
| 3 | Visa dropped chip data due to invalid format for chip card type |
| 4 | Token-based transaction |
| Any other value | Unknown |

## 4.39.7 Position 8 â Chip Card Authentication Reliability Indicator

| Value | Description |
| --- | --- |
| 0 | No information / not applicable |
| 1 | Acquirer indicates that Card Authentication may not be reliable |
| 2 | Visa indicates acquirer inactive for Card Authentication |
| 3 | Visa indicates issuer inactive for Card Authentication |
| Any other value | Unknown |

## 4.39.8 Position 9-10 â Mail/Phone/E-Commerce/Payment Indicator

| Value | Description |
| --- | --- |
| 00 | Not applicable |
| 01 | Mail/Phone Order (MOTO).  Indicates that the transaction is a mail/phone order purchase, not a recurring transaction or installment payment. |
| 02 | Recurring transaction from acquirer in Visa US region |
| 03 | Installment payment. Indicates a purchase of goods or services that is billed to the account in multiple charges over a period of time agreed upon by the cardholder and merchant. |
| 04 | Unknown classification/other mail order. Indicates that the type of mail/telephone order is unknown. |
| 05 | Secure electronic commerce transaction.  Indicates that the electronic commerce transaction has been authenticated using a Visa-approved protocol, such as [3D SecureClosed 3D Secure (3-domain structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as âVerified by Visa/Visa Secureâ and âMastercard SecureCode/Mastercard Identity Checkâ respectively.](#). |
| 06 | Non-authenticated security transaction at a 3D Secure-capable merchant, and merchant attempted to authenticate the cardholder using 3D Secure  Identifies an electronic commerce transaction where the merchant attempted to authenticate the cardholder using 3D Secure, but was unable to complete the authentication because the issuer or cardholder does not participate in the 3D Secure program. |
| 07 | Non-authenticated Security Transaction  Identifies an electronic commerce transaction that uses data encryption for security; however, cardholder authentication is not performed using a Visa-approved protocol, such as 3D Secure. |
| 08 | Non-secure transaction  Identifies an electronic commerce transaction that has no data protection. (This value is not allowed in Europe) |
| 09 | Reserved for future use |
| Any other value | Unknown |

## 4.39.9 Position 11 â Cardholder ID Method Indicator

| Value | Description |
| --- | --- |
| 0 | Unspecified |
| 1 | Signature |
| 2 | Online PIN |
| 3 | Unattended terminal, no PIN pad |
| 4 | Mail/Telephone/Electronic Commerce |
| Any other value | Unknown |

## 4.39.10 Position 12 â Additional Authorisation Indicators

| Value | Description |
| --- | --- |
| 0 | Not applicable |
| 1 | Terminal accepts partial authorization responses, amount is not an estimate. |
| 2 | Estimated amount, terminal does not support partial authorization responses. |
| 3 | Estimated amount and terminal accepts partial authorization responses |
| Any other value | Unknown |