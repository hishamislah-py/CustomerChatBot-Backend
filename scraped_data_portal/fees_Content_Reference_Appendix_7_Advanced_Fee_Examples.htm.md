# Appendix 7: Advanced Authorisation Fee Examples

This section provides some examples to illustrate how fees configuration works when applied to card transactions. Terminology used in this section:

* Domestic country â local country in which the card is issued.
* Base currency â currency in which the card is issued.
* Transaction currency â currency in which the transaction takes place.
* Non-domestic country â country that is not the same as the country in which the card is issued. Example, a purchase in Spain on a card issued in France.
* Non-base currency â currency that is not the same as the currency in which the card is issued. Example, a purchase in EUR on a card issued in GBP.

You can set up your authorisation fees to take into account both the Currency and the Country of the card and transaction.

## Examples of Authorisation Fees without Currency Checks

### Example 1 â Advanced Authorisation Fees (Domestic Country)

This example shows setup of simple authorisation fees for card usage in the same country as the card is issued. The processing code determines what fee is applied.

| Authorisation Fee [Processing Code] | Fee | Rate (%) | Min Fee | Cap Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **0.50** | 0.00 | 0.00 | 0.00 |
| Debits (goods with cash back) [090000] | **0.55** | 0.00 | 0.00 | 0.00 |

*Domestic country: Card issued in the United Kingdom*

* When the card is used in the UK at an ATM for cash withdrawals [Proc\_Code = 010000], a charge of 0.50 GBP is applied to the transaction.
* When the card is used n the UK for a purchase with cashback [Proc\_Code = 090000], a charge of 0.55 GBP is applied to the transaction.

### Example 2 â Advanced Authorisation Fees (Non-domestic Country)

This example shows authorisation fees for card usage in a *non-domestic* country (not in same country as where the card is issued). The processing code determines what fee is applied.

| Authorisation Fee [Processing Code] | Fee | Rate (%) | Min Fee | Cap Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **2.00** | 0.00 | 0.00 | 0.00 |

*Non-Domestic country: Card issued in France, Non-Domestic country*

* When the card is used at an ATM for non-domestic country cash withdrawals [Proc\_Code = 010000], a fixed charge of 2.00 EUR.

  + Example: For an ATM Withdrawal of 90.00 EUR a non-domestic fixed charge of 2.00 EUR. The total fee applied will be 92.00 EUR.

## Examples of Authorisation Fees with Currency Checks

### Example 3 â Advanced Authorisation Fees (Domestic Country and Non-base Currency)

This example shows authorisation fees for card usage in a *domestic* country and in a non-domestic card currency. The processing code determines what fee is applied.

| Authorisation Fee [Processing Code] | Non-Dom Fee | Non-Dom Rate (%) | Non-Dom Min Fee | Non-Dom Max Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **2.00** | **1.00** | 0.00 | 0.00 |

*Domestic country and currency: Card issued in the United Kingdom, GBP. Non-Domestic currency: EUR*

* When the card is used at an ATM for non-base currency cash withdrawals [Proc\_Code = 010000], a fixed charge of 2.00 GBP plus a Non-Dom rate of 1% is applied to the transaction. The minimum fee that will be charged for non-domestic usage on this processing code is 2.50 GBP.

  + Example 1: For an ATM Withdrawal of 90.00 EUR (75.00 GBP), a percentage rate charge of 0.75 GBP, plus a non-domestic fixed charge of 2.00 GBP. The total fee applied will be 2.75 GBP.

### Example 4 â Advanced Authorisation Fees (Non-domestic Country and Non-base Currency)

This example shows authorisation fees for card usage in a *non-domestic* country (not in same country as where the card is issued) and in a non-domestic card currency. The processing code determines what fee is applied.

| Authorisation Fee [Processing Code] | Non-Dom Fee | Non-Dom Rate (%) | Non-Dom Min Fee | Non-Dom Max Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **2.00** | **1.00** | 0.00 | 0.00 |

*Domestic country and currency: Card issued in the United Kingdom, GBP. Non-Domestic country: Card used in France*

* When the card is used at an ATM for non-domestic cash withdrawals [Proc\_Code = 010000], a fixed charge of 2.00 GBP plus a Non-Dom rate of 1% is applied to the transaction. The minimum fee that will be charged for non-domestic usage on this processing code is 2.50 GBP.

  + Example 1: For an ATM Withdrawal of 90.00 EUR (75.00 GBP), a percentage rate charge of 0.75 GBP, plus a non-domestic fixed charge of 2.00 GBP. The total fee applied will be 2.75 GBP.
  + Example 2: For an ATM Withdrawal of 30.00 EUR (25.00 GBP), a percentage rate charge of 0.25 GBP, plus a non-domestic fixed charge of 2.00 GBP. The total fee is 2.25 GBP. Since this is less than the Non-Dom Min Fee of 2.50 GBP, the fee that is applied is the minimum fee of 2.50 GBP.

If the Non-Dom minimum fee exceeds the combined value of the Non-Dom fixed fee and Non-Dom fee rate, then Thredd will apply the Non-Dom minimum fee. However, if the Non-Dom minimum fee is lower than the sum of the Non-Dom fixed fee and Non-Dom rate fees, then Thredd will apply the fee which includes the combination of Non-Dom fixed fee and Non-Dom fee rate.

### Example 5 â Foreign Exchange (FX) Fees

This example shows authorisation fees for transactions with currency conversion. The processing code determines what fee is applied.

| Authorisation Fee | FX Fixed Fee | FX Rate (%) | FX Min Fee | FX Cap Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 1.50 | 1.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | 0.00 | 1.50 | 1.00 | 0.00 |

*Domestic currency: GBP. Non-Domestic currency: EUR*

When the card is used for purchases that involve currency conversion, then a percentage fee rate of 1.5% is applied to the transaction.  
 Example: for a purchase for 60.00 EUR (50.00 GBP), a percentage rate charge of 0.75 GBP is applied. Since this is below the FX Min Free threshold, the minimum fee of 1.00 GBP is applied.

### Example 6 â Combining Authorisation Fees

Your fee setup can include a combination of fees. The complexity of your fees can be configured to the needs of your card programme. See the example below (combining some of the authorisation fees from examples 1-3).

| Authorisation Fee | Dom Fee | Dom Rate (%) | Dom Min Fee | Dom Max Fee | Non-Dom Fee | Non-Dom Rate (%) | Non-Dom Min Fee | Non-Dom Max Fee | Non-Dom Cap Fee | FX Fixed Fee | FX Rate (%) | FX Min Fee | FX Cap Fee |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.50 | 2.00 | 0.00 |
| Debits (for ATM withdrawals) (010000) | **0.50** | 0.00 | 0.00 | 0.00 | **2.00** | 1.00 | 2.50 | 0.00 | 0.00 | 0.00 | 1.50 | 2.00 | 0.00 |

* In this example, no fees are applied for purchases [Proc\_Code = 000000] in the domestic country or non-domestic countries. Minimum Fees are applied for FX conversion.
* A fixed fee of 0.5 GBP is applied ATM withdrawals in the domestic country.
* For ATM withdrawals in a non-domestic country and currency, a number of fees apply.

Example: For an ATM Withdrawal of 60.00 EUR (50.00 GBP), the following fees apply:

* Fixed Non-Dom Min Fee: 2.50 GBP

* FX Min Fee: 1.00 GBP
* Total = 3.50 GBP