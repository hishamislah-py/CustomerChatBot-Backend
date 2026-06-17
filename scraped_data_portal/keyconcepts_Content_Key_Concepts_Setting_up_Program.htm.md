# 4 Setting up a Program with Thredd

This section provides an overview of what you need to get started and describes the data model of setting up a program in the Thredd system.

For information about the steps in a typical project, see the [Getting Started Guide](https://docs.thredd.ai/gettingstarted/Content/GSHome.htm).

## 4.1 What you need to Get Started

### 4.1.1 Issuer/BIN-sponsor

The issuer provides Thredd with the card BIN ranges (the first 6 or 8 digits of the long card number), which are used to generate the card PANs used in a card program. The issuer has an existing relationship with the card scheme, who authorises them to use cards in this BIN range.

You can use the services of an existing Issuer or become self-issuing.

For advice on which option may be best for your organisation, please contact your Business Development Manager.

### 4.1.2 Payment Service Provider or Agency Banking Service

If your customers are funding their account via card payments, you will need to use the services of a Payment Service Provider (PSP). Alternatively, you can use an Agency Banking provider to process payments and bank transfer payments via BACS, CHAPS, Faster Payments and SEPA.

Client money linked to your cards must be held in a separate, ring-fenced bank account, which is protected in the event your business fails.

For details, please contact your Business Development Manager.

### 4.1.3 Card Manufacturer

If you are providing your customers with physical cards, then you will need to sign a commercial agreement with one of the card manufacturers which Thredd supports. For details, please contact your Business Development Manager.

To use a card manufacturer not currently integrated to Thredd, please discuss with your Business Development Manager or Account Manager.

## 4.2 Thredd Data Model

The figure below provides an example of the typical data hierarchy when setting up a new program on the Thredd system.

![](../Resources/Images/System_Hierarchy.png "Thredd Data Model - Account Hierarchy")

Figure 9: Setting up an Account with Thredd

Each Thredd customer (Program Manager) is set up under an Issuer Bank and Institution. The Institution is linked to a Program Manager.

The Program Manager account may consist of multiple Thredd Schemes; these are required if supporting multiple BINs or more than one card manufacturer; separate Thredd Schemes may be required if you want to create both physical and virtual cards.

Thredd Schemes are links to card *Products*. A card product provides most of the configuration options relating to a card. Separate card products are required per issuing country, billing currency and supported EHI mode.

Card *Usage Groups*, which define how the card can be used, are assigned at card level, and can be linked to more than one card product.

Each level of the hierarchy enables different configuration options to be set. See below for details.

### 4.2.1 Bank

The bank represents the issuing bank (BIN Sponsor or IIN sponsor). A separate bank entity must be set up for each card scheme (i.e., per Visa BID or Mastercard ICA[1  An ICA can be unique or shared Visa only allow 1 BID per issuer, per region.](#)) and region.

A bank can be linked to multiple Institutions, which is managed at card product level.

| Configuration options defined at this level |
| --- |
| Member ID (5 or 6 digits for Mastercard and 8 digits for Visa). |
| Chargeback interfaces |
| Card scheme reporting |
| Tokenisation keys (VDEP/MDES) |

### 4.2.2 Institution

An institution represents an organisation set up on the Thredd system, such as a Program Manager, Bank or Card Manufacturer. Typically, one is set up per Program Manager.

| Configuration options defined at this level |
| --- |
| Chargeback reporting |
| Settlement reporting |
| Issuer Summary report |
| SAFE reporting (Mastercard only) |

### 4.2.3 Program Manager

One Program Manager account is set up per Thredd customer. Each Program Manager is assigned a unique Program Manager code. This code is included in all web service requests. A Program Manager is linked to an Institution.

| Configuration options defined at this level |
| --- |
| API credentials (for SOAP web services or REST-based Cards API) |
| PGP keys for virtual cards |

### 4.2.4 Thredd Scheme

This is an internal Thredd scheme which defines some features of the card program. It is linked to an Institution.

One Thredd scheme is set up per BIN and Card Manufacturer. If you want to support both physical and virtual cards, these must be set up as separate Thredd Schemes.[2  Conversion from Virtual to Physical cards can be supported on the same Thredd Scheme.](#)

You can have multiple Thredd schemes for different setups (e.g., if you use multiple card manufacturers, you will need a different scheme for each manufacturer).

| Configuration options defined at this level |
| --- |
| Card validity period |
| Card activation method |
| BIN (6-8 digit) |
| Card features (e.g., Magnetic or CHIP) |
| Card Manufacturer |

### 4.2.5 Products

One product is set up per BIN range, issuing country, billing currency, EHI settings and PSD2. A global program can have hundreds of products.

A product is linked to an Issuing Bank.

Cards are linked to a product, which is defined by a unique Product ID.

| Configuration options defined at this level |
| --- |
| Product type |
| Card type |
| Card details: Embossed name, default usage groups |
| Card scheme (Visa, Mastercard) |
| Billing currency |
| Physical card layout |
| BIN range |
| Card acceptor list |
| PSD2 setup |
| Risk Management settings |

### 4.2.6 Card Usage Groups

Card usage groups are used to control what the cardholder is able to do with the card, as well as the various card usage fees that are charged to the cardholder. See the table below.

| Group | Description |
| --- | --- |
| Limit Groups | Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Thredd Portal or Smart Client. |
| Authorisation Fee Groups | Group which controls the card transaction authorisation fees. |
| Recurring/Scheduled Fee Groups | Controls whether a card is charged a recurring fee, such as a monthly platform fee. |
| Web Service Fee Groups | Controls the fees charges for web service usage. Different web services can have different fees associated with them. |
| MCC Groups Merchant Category Code (MCC) Group | The MCC is a four-digit number used by the Card Schemes to define the trading category of the merchant. |
| Usage Groups | Group that controls where a card can be used. For example: POS or ATM. |
| Linkage Groups | The Linkage Group set up in Thredd Portal or Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager. |
| FX Groups | Controls the rates for FX currency conversions if the purchase currency is different from the card's currency. |
| Auth Calendar Groups | Controls the dates time when authorisations on a card are allowed. You can use this option to control when the card can be used, for example, prevent usage on weekends or out of hours. |
| Payment Token Usage Groups | Defines configuration options specific to the provisioning of a digital payment token. For details, see the [Tokenisation Service Guide](https://docs.thredd.ai/Tokenisation_Guide.htm?tocpath=Technical%20Documentation%7C_____5). |

#### Notes

* Groups can be shared across multiple Products within an Institution. You can set up as many groups as required.
* You can use the Thredd API to assign a card to card usage groups at the time of the card creation and also to change the card usage group assigned to the card at a late stage if needed.
* When you create a card on the Thredd system, if you do not specify which groups to link to the card, then the groups of the linked card Product are used.