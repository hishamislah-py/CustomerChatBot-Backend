# Appendix 1: Apata 3D Secure Rules

You can use the Apata Portal to create risk profiles to trigger an Accept, Reject or Challenge outcome on the Apata system (see [Managing Authentication Rules](../Apata_Portal/Authentication.htm)).

See below for a list of available rules that can be included in a risk profile.

| Rule | Description |
| --- | --- |
| Acquirer Exemption | Permits exemptions requested by the merchant acquirer. |
| Max Frictionless Transactions | The maximum number of transactions with frictionless authentication (no challenge) allowed before Challenge screens are shown to the cardholder when attempting an ecommerce transaction. |
| Conditional | Applies the configured action if the configured conditions are met. See [Adding a Condition Rule](#Adding). |
| Secure Corporate Payment | Permits the Secure Corporate Payment Exemption to be used. |
| Merchant Initiated | Exemption applied to a repeat transaction (i.e., repeat payment for fixed or variable amount, and fixed and variable interval, to the same payee, governed by an agreement to these payments). The Merchant must flag the transaction as merchant initiated. The first transaction, to set up the transaction, must be authenticated. An example of this type of transaction is a Card on File (CoF) transaction, at a store such as Amazon. |
| Whitelist | Exempts the transaction if the cardholder has added the merchant to the Trust List of allowed merchants. |
| Non Payment | Permits exemption from 3D Secure for a transaction type classed as a non-payment transaction (e.g. adding card to a digital wallet, adding a card on file). |
| Max Cumulative Frictionless Spend | The maximum cumulative total (in default rule currency) up to which a frictionless authentication is allowed (the cardholder will not be presented with any challenge screens). |
| PSD2 Low Value | Applies the low value exemption under the PSD2 rules, if the following conditions are met:   * Transaction value is less than 30.00 EUR * Cumulative spend since last challenge is less than 100 EUR * Number of transactions since last challenge is less than 5 |
| One Leg Transaction | Used for handling transactions where the issuer (BIN sponsor) or acquirer is not within EEA; in this case Strong Customer Authentication (SCA) is exempted as one leg out. |
| Recurring Payment | Exemption applied to a recurring transaction (i.e., repeat payment for fixed amount, such as a subscription, to the same payee). The Merchant must flag the transaction as recurring. The first transaction, to set up the recurring payment, must be authenticated. |