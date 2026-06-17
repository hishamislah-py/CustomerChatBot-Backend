# 4.5 Payment Token Fields

This section provides details of the fields which hold payment token information.

## 4.5.1 activationmethod

Describes the method used to activate the payment token. The table below describes the valid options and the content for each method.

| PaymentToken\_activationMethod | Description | Content included |
| --- | --- | --- |
| 0 | None | Empty |
| 1 | SMS to mobile | Mobile phone number held on Thredd for the cardholder |
| 2 | Email | Email address held on Thredd for the cardholder |
| 3 | Cardholder to call automated call centre | Call centre number |
| 4 | Cardholder to call normal call centre | Call centre number |
| 5 | Website | Website URL |
| 6 | Mobile application | Mobile application reference |
| 7 | Cardholder will receive a voice call | Mobile phone number held on Thredd for the cardholder |

## 4.5.2 devicetype

Describes the type of device the payment token is installed on. Below is a list of possible values.

| PaymentToken\_deviceType | Description |
| --- | --- |
| A | Clothing or apparel |
| B | Media or gaming device(e.g., XBox, TV, set-top box) |
| C | Card |
| E | Mini-card. A physical card of reduced dimensions (height and width) which is smaller than the standard ID-1 card size (See [ISO 7810](https://en.wikipedia.org/wiki/ISO/IEC_7810) for the ID-1 standard.) |
| D | Domestic application (e.g., fridge, washing machine) |
| F | Fob or key fob |
| G | Mobile tag, case or sleeve |
| H | Fashion accessory (e.g., handbag, glasses) |
| J | Jewelry (e.g., necklace, rings, bracelets). For Visa Contactless devices, this implies any wrist-worn device (including watches and wristbands.) |
| M | Mobile phone |
| N | Non-Card. This originates from Visa Contactless devices, where it indicates anything except: Card (C), Mini-Card (E), Mobile Phone (M) or Wrist-worn device (J). |
| P | Personal computer or laptop |
| R | Wristband |
| S | Sticker |
| T | Tablet |
| U | Unknown |
| V | Vehicle |
| W | Watch |
| X | Mobile phone or tablet |
| other | Ask Thredd for any additional values |

## 4.5.3 type

Describes the type of payment token. Below is a list of possible values.

| PaymentToken\_type | Description |
| --- | --- |
| BW | Browser accessible Wallet |
| C | Contactless device PAN |
| CF | Card on File PAN |
| CL | Cloud-based payments PAN |
| P | Real PAN |
| SE | Secure Element PAN |
| U | Unknown (other PAN mapping not otherwise defined) |
| V | Virtual PAN |

## 4.5.4 creatorstatus

Describes the status of the payment token on the token creatorâs system. Below is a list of possible values.

Thredd receive this value from the token creatorâs system.

.

| PaymentToken\_creatorStatus | Description | Is this status reversible? |
| --- | --- | --- |
| A | Active | Yes |
| D | Deleted on cardholder device | No |
| I | Inactive | Yes |
| N | Not tokenised | Yes |
| S | Suspended | Yes |
| X | Deactivated | No |

## 4.5.5 wallet

Describes the type of eWallet the payment token belongs to. Below is a list of possible values.

| PaymentToken\_wallet | Description |
| --- | --- |
| ADYEN | Adyen (Gateway TSP) |
| AMAZON | Amazon |
| ANDROID | Google Pay Wallet  (known before 20/2/2018 as âAndroid Pay Walletâ) |
| APPLE | Apple Pay Wallet |
| ASIA | Asia Pay |
| CHUNGHWA | Chungwa |
| FITBIT | Fitbit Pay Wallet |
| GARMIN | Garmin Pay |
| LGPAY | LG Electronics |
| MASTERPASS | MasterPass from Mastercard |
| MICROSOFT | Microsoft |
| MRCHTOKEN | Merchant Tokenisation Program |
| MTBLANC | Montblanc Pay |
| PAYNETPHYR | Phyre |
| RELIANCE | Reliance |
| SAMA | Saudi Arabia Monetary Authority |
| SAMSUNG | Samsung Pay Wallet |
| SECURECO | SecureCo |
| STOCARD | Stocard Pay Wallet |
| VISA\_DCA | Visa Digital Commerce App |
| VISACKOUT | Visa Checkout |
| WORLDPAY | WorldPay |
| other | Ask Thredd for any additional wallets |