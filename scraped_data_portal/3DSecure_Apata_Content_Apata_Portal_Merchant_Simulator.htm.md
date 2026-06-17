# 25 Using the Merchant Simulator

The Merchant Simulator menu on the [Apata Portal Dashboard](Apata_dashboard.htm#Apata_Portal_Dashboard) enables you to run simulated 3D Secure transactions. You can use simulated transactions to test the outcome of your cardholder authentication rules when applied to different types of card usage scenarios.

This option will only be visible if enabled for your organisation. For details, please check with your 3D Secure project manager.

## 25.1 Running a Simulated Transaction

1. To run a simulated transaction, select Merchant Simulator from the left-hand menu.

[![](../Resources/Images/Apata/Merchant_Simulator.png "Merchant Simulator screen")](../Resources/Images/Apata/Merchant_Simulator.png)

Figure 41: Merchant Simulator screen

2. Enter the details of the 3D Secure transaction you want to simulate. See [Transaction Simulation Fields](#Transact).
3. Scroll down to the bottom of the page and click Submit Test Transaction.

### 25.1.1 Transaction Simulation Fields

Refer to the table below for details of transaction simulation fields.

| Field | Description |
| --- | --- |
| Test Cards | Ignore this field. it is not relevant to Thredd programmes. |
| PAN | Enter the full Primary Account Number (PAN) of the card you want to test. |
| Merchant | Enter details of the merchant requesting cardholder authentication: Merchant name, Merchant ID and Merchant Country. |
| Amount | Enter the Amount and Currency of the transaction. |
| Protocol Version | Select the 3D Secure protocol version (e.g., 2.1.0 or 2.2.0). For more information, see [Support for 3D Secure Versions](../3D_Secure_Apata/Additional_3D_Secure_Considerations.htm#_Support_for_3D). |
| Challenge Preference | Select the required challenge method from the drop-down: |
| Device | Select the device type used for the 3D secure session. Options are: *Browser* or *App*. |
| Alias | Provide a name for your test transaction. |

### 25.1.2 Viewing Simulated Transactions

You can use the Transactions menu to search for your simulated transactions.

This option will only be visible if enabled for your organisation. For details, please check with your 3D Secure project manager.

* To view simulated transactions, click the Transaction Simulation toggle button (at the top-right of the [Transactions](Transactions.htm) page).

![](../Resources/Images/Apata/transaction_simulation_toggle.png "Transaction Simulation toggle button")

Figure 42: Merchant Simulator toggle button

## 25.2 Backtesting Risk Profiles

Backtesting enables you to simulate how an updated version of a draft risk profile performs by running transactions on historical data. The backtest generates various insights on the draft risk profile, such as challenge and fraud rates, which help you to assess and decide on your next action. For example, you can edit the risk profile and run the backtest again if the challenge and fraud rates are too high. For further analysis, you can also export the backtested transactions to a CSV file.

For details on creating a draft risk profile, refer to [Creating Draft Risk Profiles](Authentication.htm#Creating)

### 25.2.1 Running a Backtest

1. From the risk profile that you want to backtest, click **Backtest**.

![](../Resources/Images/Apata/created_draftprofile.png)

Figure 43: Backtest button

2. In the displayed window, select the option to run a backtest against all transactions using the same risk profile.

   ![](../Resources/Images/Apata/run_backtest.png "Run Backtest")

   Figure 44: Options for running a backtest
3. Select a time range for the backtest in the **Date** selector.
4. Enter a name for the backtest in the **Backtest name** field.
5. Click **Run**. The backtest job starts to run. The job appears as an entry on the Backtesting page and, when finished, shows as COMPLETE in the Status column.

![](../Resources/Images/Apata/Backtest_result.png)

Figure 45: Backtest result as Complete

A backtest may take some time to complete which, depending on the volumes of evaluated transactions, can range from a few minutes to an hour.

You cannot run a backtest on a draft profile if the profile is older than three months.

### 25.2.2 Viewing Insights from the Backtest

1. Click the ![](../Resources/Images/Apata/job_button_42x39.png "Back Test Job button") button.

The backtest shows insights that consist of overall results and a breakdown by metrics. The insights compare historical transactions prior to running the test, as well as projected rates after the draft rules are applied to the historical transactions. The following is an explanation of the different rates.

| Rate Category | Description |
| --- | --- |
| Frictionless | The rate in which transactions are processed without 3D-Secure challenges (or requests for further authentication). |
| Challenge | The rate in which transactions are processed with 3D-Secure challenges, where there is a request for further authentication. |
| Reject | The rate in which transactions were declined during the 3D-Secure process. |
| Fraud | Apata categorises reported fraud based on the transaction outcome as follows:  * Confirmed Fraud - Transactions that were frictionless but were reported as fraudulent by the Issuers. * Apata Prevented Fraud - Transactions that were rejected by Apata but were reported as fraudulent by the Issuers. * Apata Challenged Fraud - Transactions that were challenged by Apata but were reported as fraudulent by the Issuers. |

You can view pie charts of the overall rates, and click on the image to see the data in bar chart format.

![](../Resources/Images/Apata/backtest_kpi.png)

Figure 46: KPIs represented as pie charts

Summary boxes show metrics where there is a breakdown of changes to individual rates. In the example below, the reject rate increased by 7.83% from 1.8% to 9.63%. This resulted in an increase from 39,258 historically rejected transactions to 209,623.

![](../Resources/Images/Apata/reject_rate.png)

Figure 47: Boxes for breakdown by metrics

There are also metrics for individual risk rules within a profile in the above categories. A change in a risk rule may trigger a change in various rates.

There are these additional rates in the metrics for individual rules.

* Continue Rate, which is the number and rate of transactions that resulted in a "next" action by the rule, historically and during the backtest.
* Evaluated Rate, which is the total number of transactions evaluated by the rule, historically and during the backtest, along with the respective rates.

![](../Resources/Images/Apata/rule_metrics.png)

Figure 48: Metrics on individual rules

### 25.2.3 Exporting Backtest Transactions

The Export Transactions options allows you to export all the results to a .CSV file.

* Click **Export Transactions** located in the top-right corner of the page. The .CSV file includes details of the transaction, as well as fields containing the following additional data.

| Additional Field | Description |
| --- | --- |
| action\_historical | The action taken for this transaction historically, either *challenged*, *accepted*, or *rejected*. |
| action\_projected | The action that would have been taken, either *challenged*, *accepted*, or *rejected*. |
| reason\_historical | For a transaction that was rejected historically, this field indicates the reason. |
| reason\_projected | For a transaction that was rejected during the backtest, this field indicates the reason. |
| exemption\_historical | For a transaction that was accepted historically, this field specifies the exemption applied. |
| exemption\_projected | For a transaction that was accepted during the backtest, this field specifies the exemption applied. |
| termRuleId\_historical | The ID of the risk rule that produced the original outcome. |
| termRuleId\_projected | The ID of the risk rule that would produce the outcome under the backtest scenario. |
| fraudType\_historical | Indicates the fraud classification for the transaction historically as *Confirmed Fraud*, *Apata Prevented Fraud*, or *Apata Challenged Fraud*. |
| fraudType\_projected | Indicates the projected fraud classification for the transaction during the backtest as *Confirmed Fraud*, *Apata Prevented Fraud*, or *Apata Challenged Fraud*. |

If you have any queries, contact the Thredd 3DSecure team for assistance.