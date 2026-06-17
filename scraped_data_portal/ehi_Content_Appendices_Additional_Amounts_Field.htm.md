# 4.2 Additional Amount Field

The additional amount field (`Additional_Amt_DE54`) contains additional amount information for the transaction, if relevant. For example, for purchase with cashback transactions, the additional amounts field is present with the cashback amount. In practice, in request messages, you probably only want to read this field for cashback transactions to extract the cashback amount should you need it. (See also `Get Transaction Message fields: Additional_Amt_DE54`)

Mastercard and Visa may add new Account Type and Amount Type codes at any time.  Ignore any amounts where you do not understand the amount type or account type. These are not errors.

## 4.2.1 Additional Amount Subfields

The Additional amounts field ([Additional\_Amt\_DE54](../Requirements/GetTransaction_Message.htm#Additional_Amt_DE54)) can contain between 1 and 6 different amounts. Each individual amount is a 20 character block. There can be between 1 and 6 blocks. Each block is formatted as follows:

| Subfield | Name | Format | Description / Valid Values |
| --- | --- | --- | --- |
| 1 | Account Type | 2 digits 00-99 | Describes which account this amount refers to.  See [Account Type Codes](Processing_Codes.htm#Account) for valid values. |
| 2 | Amount Type | 2 digits 00-99 | Describes what this amount means.  See [Amount Type Codes](#_Ref443574305) for valid values. |
| 3 | Currency Code | 3 digits 000-999 | ISO 3-digit numeric currency code.  See [Currency Code](Currency_Codes.htm#_Ref443406586) for valid values. |
| 4 | Amount sign | âDâ or âCâ | C = Positive (credit) amount  D = Debit (negative) amount |
| 5 | Amount value | 12 decimal digits | The amount in minor units of the currency in subfield 3 (currency code.) |

## 4.2.2 Amount Type Codes

Amount Type provides a description of this amount.

| Amount Type | Description |
| --- | --- |
| 01 | Debit accounts: Ledger Balance  Credit card accounts: credit amount remaining for customer (the open to buy amount) |
| 02 | Debit accounts: Available Balance  Credit Card accounts: customerâs credit limit |
| 03 | Amount Owing |
| 04 | Amount Due |
| 10 | Healthcare eligibility amount. Allows the acquirer to indicate the portion of the amount spent on eligible healthcare products/services (USA only). |
| 11 | Prescription eligibility amount. Allows the acquirer to indicate the portion of the amount spent on eligible prescriptions (USA only). |
| 12 | Vision Rx eligibility amount. Allows the acquirer to indicate the portion of the amount spent on eligible vision Rx or vision products/services (USA only). |
| 17 | Mastercard prepaid online bill pay transaction fee amount |
| 40 | Cashback amount |
| 42 | Surcharge amount |
| 44 | Gratuity amount |
| 56 | Member provided fee |
| 57 | Original amount |
| 58 | Point of Interaction amount (e.g. before Dynamic Currency Conversion at the terminal) |
| 59 | Limit/Balance available amount from Mastercard In-Control |