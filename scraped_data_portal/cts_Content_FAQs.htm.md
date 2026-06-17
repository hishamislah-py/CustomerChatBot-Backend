# FAQs

This section provides answers to frequently asked questions about CTS.

#### Q. What MCC codes are used?

The following [Merchant Category Codes (MCC)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.](#) are used:

* E-commerce: 5734 â Computer Software Stores
* MOTO: 5311 â Department Stores
* POS: 5734 â Computer Software Stores
* ATM: 6011 â Automated Cash Disburse

#### Q. What merchant name is displayed on the transactions?

The following Merchant names are displayed:

* E-commerce: e-commerce merchant
* [MOTO![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Mail and Telephone Order (MOTO) transaction, which is a payment made over the telephone (e.g., via a Call centre) or via a mail order catalogue.](#): moto merchant
* [POS![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Point of Sale transaction.](#): Shop with Chip POS
* [ATM![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Automated Teller (Cash) Machine.](#): offsite ATM

#### Q. Are PSD2 counter limits validated in CTS?

Currently the CTS system does not validate against any PSD2 counters that may be setup in the system as there are several different hosts that manage these limits.

#### Q. Are contactless limits validated in the CTS tests?

Due to the contactless limits varying by country, currency and merchant, CTS is unable to validate this.

#### Q. What FX Rate does CTS provide?

If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.

#### Q. What is Mastercard Network Exchange (MNE) and does CTS support MNE tests?

This is a processing network for US issuers, where messages are processed based on [Single Message![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) A transaction processing message standard which combines authorisation and presentment into a single message.](#) standards. This network enables one stop integration for the US Local Debit Networks such as STAR, PULSE, NYCE. CTS supports testing of MNE transactions.

#### Q. Does CTS support testing of Discover Network Transactions?

The Discover Global Network consists of a group of card networks acquired by Discover. This includes: Discover, Diners Club International and Pulse. CTS supports testing of Discover network transactions. For more information, see [CTS and Discover Global Network](CTS/Using_the_CTS_Dashboard.htm#CTS2).