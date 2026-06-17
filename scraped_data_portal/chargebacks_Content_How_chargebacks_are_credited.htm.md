# 5 How Chargebacks are Credited

This section explains chargeback processing and how to determine the amount being credited back to a card.

Chargebacks can be automatically credited back to a customer's card by enabling the **Auto Credit** chargeback feature. This feature is configured during product setup in the Product Setup Form (PSF). If you want to enable Auto Credit, contact your Thredd Account Manager.

To prevent a card from going into negative balance while a chargeback is being processed, you can also enable the **Do Not Debit Second Presentment** option. This is configured by setting the `SecondPresentmentNotDebited` flag which stops the Second Presentment from debiting funds from a card when a chargeback is in the process of being settled. When enabled, the second presentment is applied to the card but no funds will be debited from the card (in other words, the bill amount will be zero). The second presentment can then be settled directly with the scheme. If you want to enable this option, contact your Thredd Account Manager.

If you are using Smart Client to manage chargebacks, you also have the option to credit a chargeback to a customer's card using the `Credit to Card` field in the **Create Chargeback** screen. This allows you to credit chargebacks for particular cases. If you've enabled the Auto Credit feature at product level, the `Credit to Card` field is selected by default; however, you can deselect it. For more information, see [Creating a Chargeback](Managing_Chargebacks_on_SmartClient.htm#_Creating_a_Chargeback).

## 5.1 Viewing the Amount Credited

There are different types of chargeback transaction, including:

* A credit transaction where funds are credited back to the customer
* A non-credit transaction
* A chargeback reversal transaction

You can see the amount credited back to the customerâs card in the Thredd Transaction XML report.

1. Inspect the **RecordType** under the element `CardChrgBackRepRes`.
2. To determine whether this is a credit or a non-credit transaction, inspect the `<BillAmt>` field.

For example:

[Copy](javascript:void(0);)

```
<BillAmt value="24.95"currency="826"rate="1.000000"></BillAmt>
```

Chargeback credit transactions have a bill amount.

If `<BillAmt>` is zero, this is a non-credit chargeback transaction (for example, you may see this for chargebacks where auto credit is not enabled so the chargeback amount cannot be automatically refunded to the customer). To see the chargeback amount that is pending, inspect the `<Pending_Billing_Amount>` field. For example,

[Copy](javascript:void(0);)

```
<Pending_Billing_Amount>500.50</Pending_Billing_Amount>
```

Similarly, Second Presentment Debit transactions have a bill amount. If this is zero, this is a non-debit second presentment transaction (for example, you may see this for second presentments where the **Do Not Debit Second Presentment** option is enabled so the presentment amount cannot be automatically debited from the customer).

For non-credit transactions, EHI will also show the `<BillAmt>` as zero; however, the `<Pending_Billing_Amount>` is not sent to EHI. In EHI, you will see chargeback credit transactions labelled with the letter C, non-credit transactions labelled with the letter H, and reversals labelled with the letter K. For more information, see the [EHI Guide](https://docs.thredd.ai/EHI_Guide.htm).

For more information about the Transaction XML report, see the [Transaction XML Reporting Guide.](https://docs.thredd.ai/Transaction_XML_Reporting_Guide.htm)