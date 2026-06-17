# Appendix 6: Basic Authorisation Fee Examples

This section provides some basic examples to illustrate how fees configuration works when applied to card transactions.

## Examples of Authorisation Fees with Currency Only

### Example 1 â Basic Authorisation Fees (Domestic Currency)

This example shows authorisation fees for card usage in the card's domestic (base) currency. No country checks are performed. The fees system uses the transaction processing code to decide what type of fees to apply.

| Authorisation Fee [Processing Code] | Dom Fee | Dom Rate (%) | Dom Min Fee | Dom Max Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **0.50** | 0.00 | 0.00 | 0.00 |
| Debits (goods with cash back) [090000] | **0.55** | 0.00 | 0.00 | 0.00 |

*Transaction currency = Billing currency (card's domestic currency)*

* When the card is used at an ATM for cash withdrawals [Proc\_Code = 010000], a charge of 0.50 in base currency units is applied to the transaction.
* When the card is used for a purchase with cashback [Proc\_Code = 090000], a charge of 0.55 in base currency units is applied to the transaction.

### Example 2 â Basic Authorisation Fees (Non-domestic Currency)

This example shows authorisation fees for card usage in a *non-domestic* currency (not in the same currency as the card's base currency). No country checks are performed. The fees system uses the transaction processing code to decide what type of fees to apply.

| Authorisation Fee [Processing Code] | Non-Dom Fee | Non-Dom Rate (%) | Non-Dom Min Fee | Non-Dom Max Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | **2.00** | **1.00** | 2.50 | 0.00 |

*Transaction currency â  Billing currency (card's domestic currency)*

* When the card is used at an ATM for non-domestic cash withdrawals [Proc\_Code = 010000], a fixed charge of 2.00 base currency units plus a Non-Dom Rate of 1% is applied to the transaction billing amount. The minimum fee that will be charged for non-domestic usage on this processing code is 2.50 base currency units .

  + Example A - Base Currency is GBP: The cardholder makes an ATM withdrawal of 90.00 EUR (base currency billing amount = 75.00 GBP). The fees system applies a 1% Non-Dom Rate of 0.75 GBP, plus a Non-Dom Fee of 2.00 GBP. The total fee applied is 2.75 GBP.
  + Example B - Base Currency is GBP: The cardholder makes an ATM withdrawal of 30.00 EUR (base currency billing amount = 25.00 GBP). The fees system applies a 1% Non-Dom Rate of 0.25 GBP, plus a Non-Dom Fee of 2.00 GBP. The total fee is 2.25 GBP. Since this is less than the Non-Dom Min Fee of 2.50 GBP, the fee that is applied is the minimum fee of 2.50 GBP.

## Examples of Authorisation Fees with Currency and FX

### Example 3 â Foreign Exchange (FX) Fees

This example shows authorisation fees where a Thredd fee is applied for foreign exchange (FX) transactions. The fees system uses the transaction processing code to decide what type of fees to apply.

| Authorisation Fee | FX Fixed Fee | FX Rate (%) | FX Min Fee | FX Cap Fee |
| --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 1.50 | 1.00 | 0.00 |
| Debits (for ATM withdrawals) [010000] | 0.00 | 1.50 | 1.00 | 0.00 |

*Transaction currency â  Billing currency (card's domestic currency)*

* When the card is used for purchases or cash withdrawals in a foreign currency, then a percentage FX Rate of 1.5% is applied to the transaction billing amount.
* **Example - Base currency is GBP**: for a *transaction amount* of 60.00 EUR (*billing amount* of 50.00 GBP), a 1.5% FX Rate of 0.75 GBP is applied. Since (FX Fixed Fee + FX Rate) is less than FX Min Free, the FX Min Fee of 1.00 GBP is applied.

### Example 4 â Combining Authorisation Fees

Your fee setup can include a combination of fees. The complexity of your fees can be configured to the needs of your card programme. See the example below (combining some of the authorisation fees from examples 1-3).

| Authorisation Fee | Dom Fee | Dom Rate (%) | Dom Min Fee | Dom Max Fee | Non-Dom Fee | Non-Dom Rate (%) | Non-Dom Min Fee | Non-Dom Max Fee | Non-Dom Cap Fee | FX Fixed Fee | FX Rate (%) | FX Min Fee | FX Cap Fee |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debits (goods and services) [000000] | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.50 | 1.00 | 0.00 |
| Debits (for ATM withdrawals) (010000) | **0.50** | 0.00 | 0.00 | 0.00 | **2.00** | 1.00 | 2.50 | 0.00 | 0.00 | 0.00 | 1.50 | 1.00 | 0.00 |

* In this example, no fees are applied for purchases [Proc\_Code = 000000] in the domestic currency or non-domestic currency. Foreign Exchange (FX) rate fees and minimum fees are applied.
* A fixed fee of 0.5 base currency units is applied to ATM withdrawals in the domestic currency.
* For ATM withdrawals in a non-domestic currency, a number of fees apply.

Example - base currency is GBP: For an ATM withdrawal with a *transaction amount* of 60.00 EUR (*billing currency* = 50.00 GBP), the following fees apply:

* Fixed Non-Dom Min Fee: 2.50 GBP

* FX Min Fee: 1.00 GBP
* Total = 3.50 GBP