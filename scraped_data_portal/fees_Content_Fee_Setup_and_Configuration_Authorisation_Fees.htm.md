# 3 Authorisation Fees

Basic authorisation fees are set up on the **06a. Basic Auth Fee** tab on the Product Setup Form (PSF). Advanced authorisation fees are set up on the **06a. Basic Auth Fee** tab.

An Authorisation Fee group enables you to define unique fees for a card product. You can have multiple **Authorisation Fee Groups** set up for your program (for example, to apply different fees depending on your card product).

Within a fee group, you can set up multiple fees, to be applied based on the type of card authorisation transaction. The type of authorisation transaction is determined by the 6-letter processing code assigned to the transaction. For a full list of transaction types, see [Transaction Types](#_Fee_Options).

## 3.1 Basic Authorisation Fee Configuration

The figure below shows basic fee configuration options (currency-based only). These options are suitable for simple card programs that do not require complex FX currency configuration.

![](../Resources/Images/Authorisation_fee_groups.png)

Figure 7: Authorisation Fee Group - showing basic, currency-based only

For further information on fee use cases and configuration, see [Fee Use Cases](Fee_use_cases.htm).

For examples of fee configuration, based on these use cases see [Appendix 6: Basic Authorisation Fee Examples](../Reference/Appendix_6_Fee_Examples.htm).

## 3.2 Advanced Authorisation Fee Configuration

The figure below shows advanced fee configuration options (cross-border and bespoke FX fees), which can be specified on the 06b. Advanced Auth Fee tab of the Product Setup Form. These options are suitable for card programs that require complex FX currency configuration.

![](../Resources/Images/Advanced_fees_psf.png)

Figure 8: Authorisation Fee Group - showing advanced fees (Cross-Border & Bespoke FX Fees)

For further information on fee use cases and configuration, see [Fee Use Cases](Fee_use_cases.htm).

For examples of fee configuration, based on these use cases see [Appendix 7: Advanced Authorisation Fee Examples](../Reference/Appendix_7_Advanced_Fee_Examples.htm).

#### How to use the Authorisation Fee Groups Form

Your implementation manager completes this form:

1. The **Group Name** field displays the unique name of the fee group. This name is used when linking a card to an authorisation fee group (using Thredd's API).
2. The **Thredd Code** field displays the internal Thredd fee code.
3. Each transaction type is listed as its own row in column D (**Authorisation Fee**). See [Transaction Types](#_Fee_Options). To add additional transaction type, select a transaction type from drop-down menu, and then configure the fees you want to apply to that transaction type.

   Click the  **![](../Resources/Images/down_arrow.png)** arrow to view and select a transaction type.

### 3.2.1 Transaction Types

Refer to the table below for a list of transaction types. The code in square brackets (for example [`000000`]) is the processing code for this transaction type, as provided by the card scheme (payment network). This processing code is returned in the transaction XML reports and EHI messages and is used as part of the Thredd fee logic to calculate the fee.

You can use the processing code to track the source of any authorisation transaction card fee applied to a card. For a full list, see [Appendix 1: Processing Codes (DE003)](../Reference/Appendix_1_Processing_Codes.htm).

The transaction types listed below are relevant to both Mastercard and Visa, unless specified otherwise. Rows highlighted in yellow indicate the main transaction type codes (identified by the first two digits of the code. Rows below this are sub-level codes that indicate a variation of the main code.

| Transaction Type | Description |
| --- | --- |
| Debit POS payments | |
| Debits (goods and services) [`00`0000] | Payment in store at a point of sale (POS) terminal. |
| Purchase with Savings account [`00`1000] | POS payment using a linked savings account. |
| Purchase with Checking account [`00`2000] | POS payment using a linked checking account. |
| Purchase with Credit Card account [`00`3000] | POS payment using a linked credit card account. |
| Purchase with Universal account [`00`4000] | POS payment using a linked universal account. |
| ATM Payments | |
| Debits (for ATM withdrawals, or for cash disbursements using Maestro cards) [010000] | Cash withdrawal from an automated teller machine (ATM). |
| Withdrawal with Savings account [`01`1000] | ATM withdrawal from a savings account. |
| Withdrawal with Checking account [`01`2000] | ATM withdrawal from a checking account. |
| Withdrawal with Credit Card account [`01`3000] | ATM withdrawal from a credit card account. |
| Withdrawal with Universal Account [`01`4000] | ATM withdrawal from a universal account. |
| Cashback Payments | |
| Debits (goods with cash back) [`09`0000] | Cashback transaction. |
| Purchase with Cash Back with Checking Account [`09`2000] | Cashback transaction from a checking account. |
| Account Funding transactions | |
| Account Funding Transaction (AFT) [`10`0000] | Transaction where funds are pulled from a Visa account and are subsequently used to fund another Visa or non-Visa account[1  Not supported by all issuers. In this case, the AFT is converted to a debit transaction (000000).](#). |
| Quasi-cash (POS) transactions | |
| Visa quasi-cash (POS) transactions [`11`0000] Visa | POS transaction where the payment was for a cash service (Visa). |
| Quasi-Cash Transaction (Credit Card Account) [`11`3000] Visa | Quasi-cash transaction for a credit card account (Visa). |
| Cash disbursements and cash advances | |
| Cash Disbursement [`12`0000] Mastercard Clearing | Cash payment (Mastercard). |
| Debits (for cash advances) [`17`0000] Mastercard | Cash advance (Mastercard). |
| Debits (for cash advances) [`17`1000] Mastercard | Cash advance (Mastercard). |
| Cash disbursement [`17`2000] Mastercard | Cash payment (Mastercard). |
| Cash disbursement with Credit Card Account [`17`3000] Mastercard | Cash payment from a credit card account (Mastercard). |
| Refunds and credits | |
| Purchase refunds [`20`0000] | Refund to the cardholder. |
| Purchase Return/Refund - Checking Account [`20`2000] | Refund from a checking account. |
| Purchase Return/Refund - Credit Card Account [`20`3000] | Refund from a credit card account. |
| Original Credit [`26`0000] Visa | Payment credit (Visa). |
| Credits (for Payment Transaction) [`28`0000] Mastercard | Payment credit (Mastercard). |
| Balance Enquiries (ATM) | |
| Balance inquiry service [`30`0000] | ATM balance enquiry. |
| Balance Enquiry with Saving Account [`30`1000] | Balance enquiry on a savings account. |
| Balance Enquiry with Checking Account [`30`2000] | Balance enquiry on a checking account. |
| Balance Enquiry with Credit Card Account [`30`3000] | Balance enquiry on a checking account. |
| Balance Enquiry with Universal Account [`30`4000] | Balance enquiry on a universal account. |
| PIN Services (ATM) | |
| PIN change transactions [`70`0000] Visa | Cardholder requests a PIN change (Visa). |
| PIN unblock transactions [`72`0000] Visa | Cardholder requests a PIN unblock (Visa). |
| PIN unblock transactions [`91`0000] Mastercard | Cardholder requests a PIN unblock (Mastercard). |
| PIN change transactions [`92`0000] Mastercard | Cardholder requests a PIN change (Mastercard). |

### 3.2.2 Authorisation Fee Options (Basic - Currency Based Only)

Refer to the table below for a list of fees and fee options that can be applied to each of the authorisation fee types listed above.

| Fee Option | Description |
| --- | --- |
| Domestic - Base Card Currency | |
| Fixed fee | Fixed amount to apply to the transaction. |
| Rate (%) fee | Percentage of the transaction amount to apply. |
| Minimum fee | Minimum fee to apply. |
| Cap Fees | Maximum fee to apply. |
| Non-Domestic - Non-base Card Currency | |
| Fixed fee | Fixed amount to apply to the transaction. |
| Rate (%) fee | Percentage of the transaction amount to apply. |
| Minimum fee | Minimum fee to apply. |
| Cap Fees | Maximum fee to apply. |
| FX Fixed fee | Fixed amount to apply to an FX transaction. |
| FX Rate (%) fee | Percentage of an FX transaction amount to apply. |
| FX Minimum fee | Minimum fee to apply. |
| FX Cap Fees | Maximum fee to apply. |
| Various Fees | |
| Decline Fee | Enter the amount and in **column AB** select the decline Response Codes that will trigger the decline fee. You can select multiple response codes. See [Response Codes](#_Response_Codes).  **Note**: if you do not select any response codes, then all the decline response codes can trigger the decline fee. |
| Allow Partial | Whether to apply a partial fee if the card does not have sufficient funds to cover the full fee. Select YES or NO. |
| Allow Multiple Fees | Allows you to define different fees for lower-level transactions of the same type (i.e., that have the same first two digits in their processing code). The default is NO. See [Allowing Multiple Fees](#_Allowing_Multiple_Fees).  **Note**: This option should always be set to NO, unless required to support card processing in your region. |
| Threshold type | Select the threshold type to trigger the fee:  > triggers the fee if the amount is greater than the specified **Threshold amount**  < triggers the fee if the amount is less than the specified **Threshold amount** |
| Threshold amount | Specify a transaction threshold amount to trigger the fee. For example: > 1.50. Any authorisation above this amount will trigger the fee. |
| No of free txn/month | Specify the number of free transactions allowed per month before the fee is triggered. |
| No of free txn/Activation | Specify the number of free transactions allowed once the card is activated before the fee is triggered. |
| SMS fee | Specify the fee to be charged for any SMS notification messages sent to the cardholder for this type of transaction. |
| Currency | Specify the 3-digit ISO currency code. Only applicable for Multi-Wallet setup. |

### 3.2.3 Response Codes

You can configure the **Response Codes** that trigger a Decline fee. The response codes that trigger a decline fee are shown in **Column AB**, in the row beneath **Response Codes**. See the example below. For a list of response codes, see [Appendix 3: Response Decline Codes](../Reference/Appendix_3_Response_Decline.htm).

![](../Resources/Images/Response_codes.png)

Figure 9: Example of Response Codes

If you do not select any response codes, then all the decline response codes can trigger the decline fee.

There is a specific type of authorisation, known as an [Account Status Information (ASI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A standard message type which allows the merchant to check the Card Validation Code (CVC) and, if address details are provided, to optionally use the Address Verification Service (AVS). If these checks are successful Thredd responds with an 00 approval to the merchant. They normally then submit a second transaction, but with an actual transaction amount included.](#) transaction, which may not trigger a decline fee. For details, see [Fee Processing of ASI Transactions](../Reference/Appendix_5_Fee_Processing.htm#_Fee_Processing_Rules).

### 3.2.4 Allowing Multiple Fees

The Allow Multiple Fees option enables you to define lower-level transaction fees for transactions of the same type (i.e., that have the same first two digits in their processing code).

* If set to NO, then Thredd only checks the first two digits of the processing code
* If set to YES, then Thredd checks the full 6 digits of the processing code, enabling you to apply different fees for each type of lower-level transaction.

The default option is NO (disabled) and this setting is recommended. Multiple fees should only be used to support specific regional use cases.

#### Example

Payments Out (processing code `16`0000) can be broken down into separate fees per payment type by enabling multiple fees and configuring separate fees for each of the following:

* Faster Payment out = `161000`
* BACS Out = `162000`
* Direct Debit out = `163000`

Payments In (processing code `29`0000) can be broken down into separate fees per payment type by enabling multiple fees and configuring separate fees for each of the following:

* Faster Payments In = `291000`
* BACS In = `292000`