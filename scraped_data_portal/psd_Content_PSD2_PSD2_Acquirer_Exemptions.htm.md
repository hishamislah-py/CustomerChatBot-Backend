# PSD2 Acquirer Exemption Types

This section provides details of how acquirers are able to flag transactions as exempt from SCA checks or delegate authority for SCA to their merchant.

Acquirers can use the following exemptions in order to process transactions without Strong Customer Authentication (SCA):

* [Low value transactions](#Low)
* [Transaction risk analysis](#Transact)
* [Recurring transactions](#Recurrin)
* [Delegated authentication](#Delegate)
* [Other exemptions](#Other)

Using these exemptions can help acquirers to bypass SCA checks, reducing the number of abandoned customer purchases and improving conversion. Acquirers will try to balance between security and customer ease of use, based on a risk assessment and using the available exemptions. This requires a continuous analysis of transaction and fraud data as well as a continuous improvement of risk management.

For details of which acquirer exemptions are verified and which are accepted, see [Step 3: Check for PSD2 Acquirer Exemptions](#).

You can find out whether any acquirer SCA exemptions apply using the `GPS_POS_Data` field, position 23: *Acquirer Exempt from SCA indicator*. See the [EHI Guide > GPS\_POS\_Data](https://docs.thredd.ai/ehi/Content/Appendices/GPS_POS_Data.htm).

## Low Value Transactions

Low value transactions are payments with a value of less than 30 EUR\*. The total cumulative value of all transactions since the last Strong Customer Authentication must not exceed EUR 100\* and no more than five transactions in total may have taken place since the last SCA.

The card issuer needs to track the number of total transactions and the cumulative value of a card, since the acquirer will not have this data. Acquirers will be unaware of transactions on other acquirers with the same card, so will not be in a position to check for the cumumulative total limit since the last SCA. For this reason, Thredd recommends that you set your Thredd card product *PSD2 Acquirer Low-Value Max exemption value* to 0.00. See [PSD2 Product Settings](PSD2_Settings.htm).

\* Values may vary per country, as set by the local Financial Regulator.

## Transaction Risk Analysis

In transaction risk analysis, the exemption rule depends on the acquirer's [fraud rate![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The fraud rate is the percentages of transactions received by the acquirer which are identified as fraudulent.
For example, if 10,000 transactions per day are received, and 10 of these are identified as fraudulent, the fraud rate would be 0.01.](#), in combination with the transaction value. For transactions of more than 500 EUR\*, the Transaction Risk Analysis no longer applies. For transaction values between 250 and 500 EUR\*, the acquirer must prove a fraud rate of no more than 0.01 percent in order to be allowed to process a transaction without Strong Customer Authentication. For lower transaction values, slightly higher fraud rates are tolerated (up to a maximum of 0.13%).

Thredd suggests you consider set a limit for this exemption, if you want to avoid honouring this exemption for very large amounts. See the *PSD2 Txn Risk Analysis Max exemption value* field in [PSD2 Product Settings](PSD2_Settings.htm).

\* Values may vary per country, as set by the local Financial Regulator.

## Recurring Transactions

Recurring transactions are multiple transactions processed at predetermined intervals, representing an agreement between a customer and a merchant to take payments over a period of time. Typically, SCA is performed on the first transaction, while subsquent transactions are treated as cardholder not present and not subject to SCA: the merchant uses card details stored on file and processes the subsequent transactions through their acquirer as a *recurring transaction*.

Only transactions in which the amount and the payment recipient match the first transaction are recognised as recurring transactions.

## Delegated Authentication

In delegated authentication, the merchant carries out strong customer authentication. This provides for an improved customer experience, where a PSD2 and SCA compliant one-click checkout is possible.

## Other Exemptions

Below are additional exemptions that may be flagged by the acquirer:

* **Secure Corporate Payment** - the transaction is part of a secure corporate payment transaction (e.g., using a qualifying commercial card where the transaction was initiated in a secure corporate environment).
* **Merchant Initiated Transaction** - the transaction has been initiated by the merchant without interacting with the cardholder (e.g., London Underground transport billing after the journey is complete).
* **Authentication Outage Exemption** - where the merchant or acquirer was unable to complete authentication due to an outage (e.g, was unable to connect to the 3D Secure directory server).
* **Trusted Merchant (identified by Acquirer)** - the merchant is part of the acquirer's trusted merchant scheme, which enables transactions to be completed without SCA.