# Appendix 8: Applying Fees to FX Transactions

This section provides details of how fees are applied for foreign exchange (FX) transactions.

* Where the *transaction amount* is in a non-domestic currency, the card scheme (e.g., Visa, Mastercard or Discover) applies their daily exchange rate to convert this to the *billing amount* in the card's domestic currency.
* The Thredd Fees module fixed fees and fee rates are applied to the *billing amount* in the card's billing currency.
* If the *non-domestic minimum fee* exceeds the combined value of the *non-domestic fixed fee* and *non-domestic fee rate*, then Thredd will apply the *non-domestic minimum fee*.
* If the *non-domestic minimum fee* is lower than the sum of the *non-domestic fixed fee* and *non-domestic fee rate*, then Thredd will apply the fee which includes the combination of *non-domestic fixed fee* and *non-domestic fee rate*.

See the figure below.

![](../Resources/Images/Auth_fee_example.png "Auth fee example")

Figure 18: Authorisation Fee Processing Flow for an FX Transaction