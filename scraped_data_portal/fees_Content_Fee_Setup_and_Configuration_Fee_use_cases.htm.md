# Fee Use Cases

This section provides details of common use case scenarios when setting up fees for your card program. These fee configuration use cases can be flexibly combined, to meet the needs of your card program.

## Basic Authorisation Fee Configuration (Currency Based Only)

These use cases are applicable to simple card programs, and should be sufficient to meet the needs of many card programs.

![](../Resources/Images/basic_fee_use_case.png "Basic Fee Configuration")

Figure 3: Basic Fee Building Blocks

For examples of basic fees and how they can be applied to your cards, see [Appendix 6: Basic Authorisation Fee Examples](../Reference/Appendix_6_Fee_Examples.htm).

### Use Case 1: Domestic Transaction in Base Card Currency

This use case provides a simple way to apply fees to transactions where the *transaction* currency is the same as the card's *billing* currency. There are no country checks.  
For example, a transaction made in Singapore, in SGD (Singapore Dollars), where the card's billing currency is also SGD.

* The fee configuration building blocks include a combination of Fixed Fee and/or Rate Fee (fee percentage) applied per transaction, as well as the Minimum and Maximum (Cap) fee to apply to the transaction.
* Fees can be applied per transaction type â enabling you to specify different fees for different types of transactions. For example, you can set up different fees for purchases, ATM withdrawals, refunds, balance inquiries, and so on.

### Use Case 2: Non-Domestic Transaction in Non-Base Card Currency

This use case extends the card fees setup to scenarios where the *transaction* currency is different to the card's *billing* currency. There are no country checks.

For example, a transaction made in ASD (Australian Dollars), on card with SGD (Singapore Dollars) as the card's billing currency.

You can apply fees to cover any additional charges or costs associated with transactions that involve currency conversion (as a way of recovering costs or as a means of earning revenue on such transactions).

* The fee configuration building blocks include a combination of Fixed Fee and/or Rate Fee (fee percentage) applied per transaction, as well as the Minimum and Maximum (Cap) fee to apply to the transaction made in the foreign country.
* FX fee configuration building blocks can be used to ensure that different fees are applied to transactions involving foreign currency (FX) exchange. The fee building blocks include the same combination of Fixed Fee, Rate Fee, Minimum and Maximum fee to apply to the FX transaction.
* These configuration building blocks can be applied per transaction type â enabling you to specify different fees for different types of transactions. For example, you can set up different fees for purchases, ATM withdrawals, refunds, balance inquiries, and so on.

## Advanced Authorisation Fee Configuration (Cross-Border and FX Fees)

Advanced fee configuration options provide a more granular application of fees, suitable for more complex fee configurations. The use cases in this section enable different fees to be applied based on different combinations of country and currency.

![](../Resources/Images/advanced_fee_use_case.png "Advanced Fee Configuration")

Figure 4: Advanced Fee Building Blocks

For examples of advanced fees and how they can be applied to your cards, see [Appendix 7: Advanced Fee Examples](../Reference/Appendix_7_Advanced_Fee_Examples.htm).

### Use Case 3: No Currency Checks â Domestic and Non-Domestic (Card Issuance)

This use case provides a way to apply fees to both local (domestic) transactions, made in the same country as the card is issued, and non-domestic transactions (made in another country). The currency of the transaction is not taken into account.  
For example, a transaction made in the France, in EUR (Euro), on a German-issued EUR card.

* Separate fee configuration building blocks are available for domestic versus non-domestic transactions, and include a combination of Fixed Fee and/or Rate Fee (fee percentage) applied per transaction, as well as the Minimum and Maximum (Cap) fee to apply to the transaction.
* Fees can be applied per transaction type â enabling you to specify different fees for different types of transactions. For example, you can set up different fees for ATM withdrawals in a non-domestic country (bank charges for such withdrawals may be higher than in the domestic country).

### Use Case 4: With Currency Checks â Domestic (in Card Issuance Country)

This use case provides a way to apply fees to domestic transactions, made in the same country as the card is issued, but where the currency of the transaction may be different. The focus here is on the *currency* that is being used in the *domestic* transaction.  
For example, a transaction made in the UK, in EUR (Euro), on a UK-issued GBP card (this could happen when a cardholder withdraws cash from a local ATM that supports foreign currency cash withdrawals; such ATMs are commonly found at domestic airports and major transport hubs).

* Separate fee configuration building blocks are available for domestic transactions in the same currency as the card versus domestic transactions in a non-base currency. They include a combination of Fixed Fee and/or Rate Fee (fee percentage) applied per transaction, as well as the Minimum and Maximum (Cap) fee to apply to the transaction.
* Fees can be applied per transaction type â enabling you to specify different fees for different types of transactions. For example, you can set up different fees for ATM withdrawals in a non-domestic currency (bank charges for such foreign currency withdrawals may be higher than for domestic currency withdrawals).

### Use Case 5: With Currency Checks â Non-Domestic (outside Card Issuance Country)

This use case provides a way to apply fees to non-domestic transactions, made in the same currency as the card is issued, or in a different currency. It is similar to use case 4, but here the focus is on the *currency* that is being used in the *non-domestic* transaction.  
For example, a transaction made in the Italy, in EUR (Euro), on a UK-issued EUR card, and a transaction in Turkey, in TRY (Turkish Lira), on a UK-issued EUR card.

* Separate fee configuration building blocks are available for non-domestic transactions in the same currency as the card versus non-domestic transactions in a non-base currency. They include a combination of Fixed Fee and/or Rate Fee (fee percentage) applied per transaction, as well as the Minimum and Maximum (Cap) fee to apply to the transaction.
* Fees can be applied per transaction type â enabling you to specify different fees for different types of transactions.

### Use Case 6: With Default or Bespoke Currency Pair Checks â Domestic and Non-Domestic

This use case is similar to use cases 4 and 5, however here you can select bespoke currency pairs and apply fees to usage of the currency pairs. For example:

* Apply separate fees for different currencies, plus bespoke fees per currency. For example:

  + fee for a domestic transaction in USD (US Dollars), where USD is defined as the default currency
  + fee for a non-domestic transaction made in France, in USD (US Dollars), where USD is defined as the default currency
* Exclude specific currency pairs from FX transactions fees. For example:

  + fee for a EUR to USD FX transaction

## Recurring and API Usage Fee Configuration

### Use Case 7: Subscriptions and Recurring charges

In this use case, you can apply annual or monthly scheduled fees, and fees for card dormancy and card inactivity. These fees can be based on the frequency and day of the month you specify. For example, your card product may include an annual subscription charge. You can also apply fees if the card is dormant (not activated) or not used over a specified period (e.g., as a way to apply card administration fees and/or encourage card usage).

![](../Resources/Images/Recurring_fee_use_case.png "Recurring Fee Use Case")

Figure 5: Recurring Fee Building Blocks

### Use Case 8: Thredd API Usage Fees

In this use case, you can apply fees to a card when specific Thredd API are used. You may provide your cardholder and customer service call centre staff with an app or online portal where they can log in to check the card balance, order card replacements, load funds onto the card or transfer to another account. Whenever users make these types of transactions, your systems will need to call the Thredd API to retrieve information or update the card record. In this scenario, use of the Thredd API may involve costs that you may consider passing on to the cardholder.

![](../Resources/Images/API_usage_fee_use_case.png "API Usage Fee Use case")

Figure 6: API Usage Fee Building Blocks