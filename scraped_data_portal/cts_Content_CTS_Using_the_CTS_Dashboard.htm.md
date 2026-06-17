# 5 Using the CTS Dashboard

This topic describes the main CTS screen and explains how to run the built-in tests available.

## 5.1 About the Main CTS Screen

After logging into the CTS platform, the main CTS screen appears:

![](../Resources/Images/CTS_dashboard new.png)

Figure 6: CTS Dashboard

The interface is divided into three main sections:

* **Toolbar** â Use the toolbar along the top of the screen to see your username and sign out.
* **Menus** â Use the menu on the left-hand side to select an option such as a standard test, display your account profile, and reset your password. See [Running Standard Tests](#_Running_Standard_Tests) for more information.
* **Dashboard** â View the dashboard to access standard tests, simulations, and transaction history details. See [Using the CTS Dashboard](#_Using_the_CTS) for more information.

### 5.1.1 CTS and Mastercard Network Exchange

For customers using [Mastercard Network Exchange![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#) (MNE), it is possible to process tests for tokens that originate from an MNE sub-network by selecting the **Process Transaction via MNE** option during the setup of the test.

![](../Resources/Images/MNE_Transaction_Field.png)

Figure 7: Process transaction via MNE allows for tokens to be processed by MNE networks.

The token entered in the *Token* field must be associated with a sub-network for the *Process transaction via MNE* check box to be enabled. If the token is not associated with a sub-network then the check box will be disabled.

The PIN change option in ATM, and the Recurring option in MOTO, do not currently support processing transactions in MNE.

## 5.2 CTS and Discover Global Network

CTS can be used to test the following Discover Global Network (DGN) transaction types:

* Ecommerce, MOTO, STIP Ecommerce, Clearing, Reversal, and Refund transactions.

Please contact your Thredd Implementation or Account Manager to enable DGN transaction tests on CTS.

CTS does not currently support the following DGN transaction types: POS, ATM, STIP-POS and AFD transactions.

Be aware that status changes for DGN clearing transactions can typically take several minutes to complete.

## 5.3 Running Standard Tests

CTS provides the following standard simulation tests:

* **POS** â simulates a Point-of-Sale transaction completed through a card terminal
* **ATM** â simulates a balance enquiry or cash withdrawal transaction made on an [Automated Teller Machine (ATM)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Automated Teller (Cash) Machine.](#)
* **E-Commerce** â simulates an online, e-commerce transaction
* **MOTO** â simulates a Mail Order/Telephone Order (MOTO) transaction
* **Refund** â simulates a refund transaction initiated by a cardholder or merchant
* **Reversal** â simulates an [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) reversing a previous [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#)
* **AFD** â simulates an Automated Fuel Dispenser (AFD) transaction

To run a test:

* Click **Standard tests** on the dashboard and select a test (or choose a test from the menu). A screen appears showing the standard tests available:

![](../Resources/Images/CTS_Standard_Tests.png)

Figure 8: Standard Tests Screen

See the following sections for more information about the various tests.

### 5.3.1 POS Transaction Test

Use this test to simulate a Point-of-Sale (POS) transaction on a card terminal.

![](../Resources/Images/CTS_POS_Test.png)

Figure 9: POS Transaction Test Screen

1. Select the card element being tested:

   * [Contact chip![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card transaction where the POS terminal reads and validates the cardâs chip.](#)
   * [Contactless![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure payment method using a debit or credit card or another payment device by using RFID technology and near-field communication. To use the system, a cardholder taps the payment card near a POS terminal equipped with the technology.](#)
   * [Magstripe![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The magnetic stripe on the back of the card. Can be used for a card point of sale (POS) transaction using a merchant POS terminal.](#)
2. Enter the 9-digit **Token**, **Transaction currency**, **Transaction amount**, card **PIN** and **POS Location - Country**.

   Note: If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
3. Select a Merchant Category Code (**MCC**) from the drop-down list. If you do not select one, the default MCC is used.
4. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox. For more information on MNE, see [CTS and Mastercard Network Exchange](#CTS).
5. Click **Run Test**.

### 5.3.2 ATM Transaction Test

Use this test to simulate an [ATM![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Automated Teller (Cash) Machine.](#) balance enquiry or cash withdrawal at an ATM location.

![](../Resources/Images/CTS_ATM_Test_2.png)

Figure 10: ATM Transaction Test Screen

1. Select the ATM element being tested:

   * ATM balance enquiry
   * Contact chip (EMV) cash withdrawal
   * Contactless cash withdrawal
   * Magstripe cash withdrawal
   * PIN Change
2. Enter the 9-digit **Token**, **Transaction currency**, **Transaction amount**, card **PIN** and **ATM Location** (country).

   If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
3. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox.

   The Process transaction via MNE check box cannot be used with the Change PIN option currently.
4. Click **Run Test**.

### 5.3.3 E-commerce Transaction Test

Use this test to simulate an e-commerce transaction made through an online website.

![](../Resources/Images/CTS_ecommerce_Test.png)

Figure 11: E-Commerce Transaction Test Screen

1. Enter the 9-digit **Token**, the cardsâ **CVV2** (if required) and the card **Expiry date**.
2. Enter the **Transaction currency**, **Transaction amount**, and **Merchant Location** (country).

   If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
3. In **Merchant Location**, specify a location for the merchant.
4. Select a Merchant Category Code (**MCC**) from the drop-down list. If you do not select one, the default MCC is used.
5. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox. For more information on MNE, see [CTS and Mastercard Network Exchange](#CTS).
6. Click **Run Test**.

   To simulate a recurring transaction, select **Recurring**.

### 5.3.4 MOTO Test

Use this test to simulate a Mail and Telephone Order (MOTO) transaction, which is a payment made over the telephone (for example, via a call centre) or via a mail order catalogue.

![](../Resources/Images/CTS_MOTO_Test.png)

Figure 12: MOTO Transaction Test Screen

The Process transaction via MNE check box cannot be used for MOTO tests currently.

1. To simulate a recurring transaction, select **Recurring**.
2. Enter the 9-digit **Token**, the cardâs **CVV2** (if required) and the card **Expiry date**.
3. Enter the **Transaction currency**, **Transaction amount**, and **Merchant Location** (country).

   If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
4. Select a Merchant Category Code (**MCC**) from the drop-down list. If you do not select one, the default MCC is used.
5. Click **Run Test**.

### 5.3.5 Refund

Use this test to simulate a refund process initiated by the cardholder and merchant.

![](../Resources/Images/CTS_Refund_Test.png)

Figure 13: Refund Screen

1. Enter the 10-digit **Transaction ID** that corresponds to a transaction that has been successfully cleared.
2. Enter the **Refund amount** (this can be a partial amount, or full amount which cannot exceed the total amount of the transaction).
3. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox. For more information on MNE, see [CTS and Mastercard Network Exchange](#CTS).
4. Click **Run Test**.

### 5.3.6 Reversal

Use this test to simulate an [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) reversing a previous [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#).

![](../Resources/Images/CTS_Reversal_Test.png)

Figure 14: Reversals Screen

1. Enter the 10-digit **Transaction ID** that corresponds to an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#).
2. Select either **Full Reversal** or **Partial Reversal** and specify the **Reversal amount**.
3. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox.
4. Click **Run Test**.

Unlike full reversals, partially reversed transactions must be sent for clearing. In a partial reversal, there are two transactions: one with the original transaction amount and another partial reversal transaction with a lower amount. Both transactions must be sent for clearing so that the Merchant's Processor can calculate the Settlement amount (the new transaction amount to be used for Settlement and Account Billing). For information, see [Clearing](#Clearing).

### 5.3.7 AFD Test

Use this test to simulate an Automated Fuel Dispenser (AFD) transaction.

Automatic Fuel Dispensers are machines that can be used to deliver fuel to vehicles, normally at a petrol station. These are identified with a specific Merchant Category Code of 5542. The cardholder pays at the machine, normally by inserting their card (or swiping or contactless), and the fuel pump machine will then either:

* authorise a maximum amount (e.g., Â£100), then pump up to this, and send an advice to say how much fuel was actually delivered (common outside USA).

-or-

* authorise a nominal amount (e.g., 1 USD), then pump up to the permitted maximum it is allowed to clear according to the chargeback rules, then it will send an advice to say how much fuel was actually delivered (common in USA).

![](../Resources/Images/CTS_AFD_Test.png)

Figure 15: AFD Test Screen

1. Enter the 9-digit **Token**
2. Enter the **Maximum amount**.
3. Enter the **Transaction currency** and **Transaction amount**.

   If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
4. Enter a card **PIN**.
5. Select the **AFD Location - Country** from the drop-down list.
6. Select the **MCC 5542** Merchant Category Code from the drop-down list.
7. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox. For more information on MNE, see [CTS and Mastercard Network Exchange](#CTS).
8. Click **Run Test**.

## 5.4 Running a STIP test

Use this test to simulate scheme [Stand-in Processing (STIP)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer (BIN sponsor).
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) messages for POS and e-commerce transactions.

![](../Resources/Images/CTS_STIP_POS_Test.png)

Figure 16: STIP Tests Screen

1. Select the STIP scenario and decision that you would like to simulate.
2. Choose the POS type from the list.
3. Enter the 9-digit **Transaction ID** that corresponds to an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer (BIN sponsor) to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#).
4. Enter the **Transaction currency** and **Transaction amount**.

   If the transaction currency is different to the billing currency of the card, Thredd provides an FX transaction based on static values pulled from a database. These rates may not represent the market value.
5. For the STIP E-Commerce test, select a **Merchant Location**.
6. If you're using a token that is associated with a sub-network, click the *Process transaction via MNE* checkbox. For more information on MNE, see [CTS and Mastercard Network Exchange](#CTS).
7. Click **Run Test**.

## 5.5 Transaction History

The History screen displays a list of all the transactions made using CTS.

![](../Resources/Images/CTS_History.png)

Figure 17: History Screen

### 5.5.1 Filtering transactions

To filter transactions, click **Filters**. The filter pane appears where you can refine the list of transactions:

![](../Resources/Images/Using the CTS Dashboard_23.png)

Figure 18: Filter pane

Click **Submit** to apply a filter.

### 5.5.2 Exporting data to CSV

To export data to a CSV file, click **CSV**. If you have applied a filter, only filtered data will be included in the CSV file. If no filter is applied, all data will be included.

## 5.6 Clearing

The Clearing screen displays a list of all eligible transactions made using CTS that can be cleared to simulate the presentment/financial record.

![](../Resources/Images/CTS_Clearing.png)

Figure 19: Clearing Screen

Select the authorisations you want to send to clearing, and then click **Send Clearing**.

To filter transactions, click **Filters**. The filter pane appears where you can refine the list of transactions.

### 5.6.1 Clearing Partial Reversals

Unlike full reversals, partially reversed transactions must be sent for clearing. In a partial reversal, there are two transactions: one with the original transaction amount and another partial reversal transaction with a lower amount. Both transactions must be sent for clearing so that the Merchant's Processor can calculate the Settlement amount (the new transaction amount to be used for Settlement and Account Billing).

To simulate a partial reversal:

* Run the **Reversal** standard test, and select the **Partial Reversal** option. See [Reversal](#Reversal) for more information.
* In the Clearing screen, select the transaction ID and click **Send Clearing**.

The transaction appears in the list with a status of **Clearing** or **Cleared**. Cleared transactions are also visible in the **History** screen.