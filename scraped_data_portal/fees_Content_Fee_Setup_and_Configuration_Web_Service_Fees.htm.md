# 5 API Usage Fees

Fees can be applied to a card when specific Thredd APIs are used. Examples of use of Thredd API include card balance enquires, card replacement, card load and bank transfer fees (for a list of API Usage fee processing codes, see [Appendix 2: Fee Processing Codes](../Reference/Appendix_2_Fee_Processing.htm)).

API Usage Fees are only available for Threddâs SOAP web services

Below is an example of one of the API Usage fee groups set up on the **0.8 API Usage Fee** tab. You can have multiple fee groups set up for your program.

![](../Resources/Images/API_Usage_Fees.png)

Figure 11: API Usage Fee Group

The **Group Name** is the unique name of the fee group, to be used when linking a card to the fee group. API Usage fees are set up in the cardâs domestic currency.

You can define the following fees for each API usage fee type:

* **Fee** â fixed fee to be applied to that transaction
* **Rate (%) fee** â a percentage of the transaction is charged

* **Minimum fee** â a minimum fee to apply to a transaction if you are using a rate fee.
* **Allow Partial Fee** â whether to allow a partial fee of the required fee to be charged based on the available balance (less than the fee) on the card.
* **SMS Fee** â if the API triggers an SMS message that is sent to the cardholder.

#### How to use the API Usage Fee Groups Form

Your implementation manager completes this form:

1. The **Group Name** field displays the unique name of the fee group.
2. The **Thredd Code** field displays the internal Thredd fee code.
3. The **Enable Pending** field indicates whether pending fees are enabled[1  If a fee cannot be taken due to insufficient funds, Thredd creates a Pending fee record.](#).
4. API usage fee types are listed in column C, in the row under **API Usage Fee** (select from drop-down menu). For a list of fee processing codes, see [Appendix 2: Fee Processing Codes](../Reference/Appendix_2_Fee_Processing.htm).
5. Each API usage fee type is listed as its own row in column C. The **down ![](../Resources/Images/down_arrow.png)** arrow enables you to view and select additional API types if required.
6. For each row, the fees and fee options that apply to this API type are shown.