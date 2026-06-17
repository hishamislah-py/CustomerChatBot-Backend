# 2 Using Thredd for Fraud and Loss Reporting

Access to Smart Client is required to use this service. In Smart Client, this service is still referred to as the **MasterCom SAFE report.**

## 2.1 Creating a MasterCom SAFE Report

You can use Smart Client to report fraudulent transactions to Mastercard.

To create a SAFE report:

1. Log in to Smart Client.
2. In the **Transactions** window, right-click the required transaction and select **Create MasterCom SAFE report**.

   The **Create MasterCom SAFE report** window is displayed.

   ![](../Resources/Images/Introduction.png)

   Figure 1: Create MasterCom SAFE Report Window
3. Provide all the details as per the instructions in the table below and click **Save**.

   The report is sent to MasterCom. A confirmation message is displayed, indicating if the SAFE Report request was successfully registered with MasterCom. In this case a Claim ID and Fraud ID are returned, which you can use to track the status of the request.

   If the SAFE Report request failed, a message box is displayed, providing details of the error. For example, an invalid claim ID. Please resolve the error and try again or contact Thredd support.
4. To close the message box, click **OK**.

The created SAFE message is displayed in the **SAFE Report Details** window. See [Handling Error Codes](#_Viewing_SAFE_Report) .

| Option | Description |
| --- | --- |
| Token | Displays the unique token linked to the card PAN on which the transaction was made. |
| Date/Time | Displays the date-time stamp of the transaction. |
| Account device type | Select an option. |
| Card validation code | Select an option. |
| Amount | Displays the transaction amount. |
| Fraud Type Code | Select a fraud type option. |
| Sub Fraud Type Code | Select a sub-fraud type code. Options include:  Convenience or Balance Transfer check transaction  PIN not used in transaction  PIN used in transaction  Unknown |
| Issuer ID | Displays the card issuer ID. |
| Charged Back | Tick this option if the transaction is Charged Back. |
| Account Closed | Tick this option if the account has been closed. |

#### Handling Error Codes

An error code returned from MasterCom starting with â1â indicates errors from MasterCom; an error code starting with â5â indicates the error has occurred during Thredd processing of [chargeback![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
For more information, see the Payments Dispute Management Guide.](#) request. You can try fixing the details and resending the chargeback request or contact Thredd support.

## 2.2 Viewing SAFE Report Details

This option enables you to view details of all SAFE reports submitted to MasterCom.

1. From the Smart Client menu, select, **Management Reports > Safe Report Details**

   The **Safe Report Details** window is displayed.

   ![](../Resources/Images/Introduction_2.png)

   Figure 2: Safe Report Details Window
2. To view only pending transactions, tick the **Pending Transactions** option.

   Alternatively, to filter the list of historical transactions, tick the **History Transactions** option and select the **Date** range.
3. Click **Search**.