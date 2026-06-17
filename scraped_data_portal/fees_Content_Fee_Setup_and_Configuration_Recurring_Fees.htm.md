# 4 Recurring Fees

Recurring fees are applied on a recurring basis, based on the frequency you specify (e.g., monthly or annually). These are also referred to as *scheduled fees*, and can be used to apply fees for annual subscriptions, card activation, card load, card dormancy and card inactivity charges to your card products.

Below is an example of one of the Recurring Fee groups set up on the **Recurring Fee Groups** tab of the Product Setup Form (PSF). The Recurring Fee group enables you to define unique fees for a card product. You can have multiple **Recurring Fee Groups** set up for your program (for example, to apply different fees depending on your card product).

![](../Resources/Images/Recurring_fee_groups.png)

Figure 10: Recurring Fee Groups

A Recurring Fee group consists of a set of recurring fees configured for that group. For each recurring fee within a Recurring Fee group, you can define:

* The fee **Amount**.
* Whether to allow a **Partial Fee** to be taken if the available balance on the card is less than the full fee[1 Thredd fees cannot be taken if they will result in an account going into a negative balance. If you allow partial fees, the available balance on the card will be used to pay off part of the fee charge.](#).

#### How to use the Recurring Fee Groups Form

Your implementation manager completes this form:

1. The **Group Name** field displays the unique name of the fee group.
2. The **Thredd Code** field displays the internal Thredd fee code.
3. The **Enable Pending** field indicates whether pending fees are enabled[2  If a fee cannot be taken due to insufficient funds, Thredd creates a Pending fee record.](#).
4. The Recurring fee types are listed in column C, in the row under **Recurring Fee** (select from drop-down menu). See [Recurring Fee Types](#_Recurring_Fee_Types).
5. Each recurring fee type is listed as its own row in column C. The **down ![](../Resources/Images/down_arrow.png)** arrow enables you to view and select additional recurring fee types if required.
6. For each row, the fees and fee options that apply to this recurring fee type are shown.

## 4.1 Recurring Fee Types

Below is a list of recurring fees that you can set up. For more information on the available recurring fee configuration options, see [Recurring Fee Configuration Options](../Reference/Appendix_5_Fee_Processing.htm#_Rules_for_Recurring).

| Recurring Fee Type | Description |
| --- | --- |
| Dormancy Fees | |
| Dormancy Fee 1 Months (Repeat 1 Month) | Fee applied when a card has not had any transactions during the past month. |
| Dormancy Fee 2 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 2 months. |
| Dormancy Fee 3 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 3 months. |
| Dormancy Fee 6 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 6 months. |
| Dormancy Fee 12 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 12 months. |
| Dormancy Fee 13 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 13 months. |
| Dormancy Fee 24 Months (Repeat 1 Month) | Fee applied when a card has not been loaded with funds or had any transactions during the past 24 months. |
| Monthly Dormancy Fee - after card expires | Fee applied after a card has expired. |
| Activation Fees | |
| Monthly Fee - Activation | Activation fee is applied after the card is activated. |
| Monthly Fee - Activation Fee Taken 1st (1 Months After) | Activation fee is applied 1 month after the card is activated, on the 1st of the month. |
| Monthly Fee - Activation Fee Taken 1st (5 Month After) | Activation fee is applied 5 months after the card is activated, on the 1st of the month. |
| Monthly Fee - Activation Fee Taken 1st (6 Months After) | Activation fee is applied 6 months after the card is activated, on the 1st of the month. |
| Monthly Fee - Activation Fee Taken 1st (12 Months After) | Activation fee applied 12 months after the card is activated, on the 1st of the month. |
| Load Fees | |
| Monthly Fee - Following reload | Fee applied following a reload (only triggered once a card is reloaded). |
| Monthly Fee After Load (1 Month After) | Fee applied one month after a reload. |
| Monthly Fee After Load (1 Year After) | Fee applied one year after a reload. |
| Inactivity Fees | |
| Monthly Fee - No transaction in last 2 days | Fee applied when there have been no transactions on the card during the last 2 days. |
| Monthly Fee - No transaction in last 90 days | Fee applied when there have been no transactions on the card during the last 90 days. |
| Monthly Fee - No transaction in last 120 days | Fee applied when there have been no transactions on the card during the last 120 days. |
| Monthly Fee - No transaction in last 180 days | Fee applied when there have been no transactions on the card during the last 180 days. |
| Monthly Fee - No transaction in last 365 days | Fee applied when there have been no transactions on the card during the last 365 days. |
| Monthly Fee - Last Day of Month | Monthly fee, applied on the last day of each month. |
| Monthly fee 8th of every month | Monthly fee, applied on the 8th day of each month. |
| Annual Fees | |
| Yearly Fee- Annual | Annual card management fee. |

Monthly fees apply to the main account only, not to sub-accounts.

#### Dormancy Fees

If configured, dormancy fees apply when a card has not been loaded with funds or had any transactions during the specified period. Certain types of transactions are excluded from the dormancy assessment, such as:

* ATM Balance enquiries
* ATM PIN changes and PIN unblock
* Fee adjustments
* Recurring fees

If one of these types of transactions has occurred during the dormancy period, the dormancy fee will still be applied.