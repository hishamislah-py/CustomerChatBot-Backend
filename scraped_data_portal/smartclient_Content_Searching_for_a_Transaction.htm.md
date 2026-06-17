# 6 Searching for a Transaction

This topic explains how to find a specific transaction or list of transactions in Smart Client, and how to search and filter on information.

Smart Client provides powerful and flexible search functions and filters to help you find specific transactions. This is useful when trying to locate a transaction using only partial information from a card holder, such as the approximate date and time that a transaction took place. These options allow you to search:

* For specific types of transactions, such as declined transactions
* For a specific 6-digit BIN
* Based on specific card details, such as token number or card holderâs name, or on transaction details such as location
* Across a range of dates and times

## 6.1 Finding Transactions

To search for transactions:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. Use the options displayed along the top of the screen to narrow your search (for example, to display only declined transactions) or select **All** to display all transactions. The different search options are shown below and explained in the table:

   ![](Resources/Images/Searching_for_a_Transaction.png)

   Figure 12: Available Search options on the View Transactions screen

3. After making your selections, click **Search** to display transactions matching your criteria.

The following section explains how to use each of these options to find transactions. See the examples for typical scenarios and for hints and tips to help you take advantage of Smart Clientâs powerful search functions.

## 6.2 Searching for transaction types

You can search for specific types of transactions by selecting the following options:

| Transaction type | Description |
| --- | --- |
| Auth Not Cleared | An authorisation that has not cleared (Thredd has not yet received a presentment that can be matched to the authorisation on the token). If Thredd does not receive a presentment that can be linked to the authorisation, Thredd reverses the authorisation automatically after the hanging auth filter period has expired (as specified by the client for the product). For standard authorisations this is typically 7 days. It is usually longer (up to 30 days) for merchants using pre-authorisations, including (but not limited to) Car Hire and Hotels. |
| Auth Cleared | An authorisation which has cleared (Thredd has received a presentment that could be matched to the authorisation). |
| Declined | A transaction that has been declined. To find the decline reason, scroll right to the notes field of the transaction to see the reason for the decline. For a list of the most common decline reasons, see [Appendix A: Common Decline Reasons](Appendix_A_Common_Decline.htm). |
| **Reversed** | An authorisation that was reversed. To find the reversal reason, right click the reversal and choose **More details** > **View transaction details**. See the **Response Status (DE039)**. There are various reasons for a reversal, including: Customer Cancellation, Wrong Format, Manual Reversal, Issuer Time-Out. For a full list of reasons, refer to the Mastercard *Customer Interface Specification*, or *Visa Base* manual, or *Discover Getting Started Guide*. |
| **Load/Unload** | Load and unload Web Service (funds paid in, for example, via a load channel such as a retailer e.g., PayPoint in the UK, Ireland, or Romania, or unloaded by the Program Manager). |
| Presentment | A transaction for authorisations that require settlement. First presentment occurs when the merchant sends a request to take either part, or all the amount previously authorised on the card. |
| **Chargeback** | Presentments that have gone through the chargeback process. For more information, see [Managing Chargebacks](Managing_Chargebacks.htm). |
| **Balance Adjust** | An adjustment to the balance or the blocked amount. This can be a Credit or a Debit. |
| **Offline** | Offline transactions occur when a presentment is received without a matching authorisation. This can happen in situations where an authorisation is not possible (for example, a transaction on a plane where there is no internet connection). |
| **Expiry** | Transaction Expiry, response 54 âExpired Cardâ (Process â Debits Unload). |
| **Refund/ Fin Rev** | Presentment returning funds to the Card Holder/ Financial Reversal â Process (Credits for Refund). |
| **Payment** | Payment originating from non-card network entity, paying funds into or out of the customer account (for example, Faster Payments and BACS). |
| **Advices** | A system generated message about the transaction. This message is for information only (typically from Visa or Mastercard) and has no effect on the transaction. For example, it may note a slow response time. |
| **Unknown** | Card not found: Unknown Card. In large volumes this can indicate a BIN attack. For information, see [FAQs](FAQs.htm) |

There are 2 other transaction types that display in the View Transactions screen, but cannot be searched for. These are:

* Financial Request (Declined displays red, settled displays green)
* Financial Reversal Advice (Displays in pink)

## 6.3 Searching for a BIN

You can search for a single BIN at a time. To search for a specific BIN:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. From the **View Transactions** screen, use the BIN drop-down box to search for transactions with a specific 6-digit BIN.

   ![](Resources/Images/SC_BIN_dropdown.png)

   Figure 13:  BIN drop-down box

## 6.4 Searching using other details

To search for transactions using other details:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. From the **View Transactions** screen, expand the drop-down box labelled **Token** (the default).
3. Select the required search parameter using other card and transaction details.

   You can filter your search further using the drop-down box to the right and specifying a search value.
   You can search on PANs, Public tokens (including 9 digit and 16-digit tokens). When you enter a PAN number and select search, Smart Client automatically converts it to the 16-digit token. Select from the following list:

   ![Diagram

   Description automatically generated](Resources/Images/search_params_SC_annotated.png)

   Figure 14:  Search options available from the drop-down box beneath Token

## 6.5 Searching based on date and time

Use the date and time filters to search for transactions that occurred on a specific date and time. By default, todayâs date is shown.

You can also narrow your search to a specific time or range (for example, if a customer reports that a transaction happened around lunchtime). The time is in Thredd UK server time, not the country of transaction time.

To search transactions based on the date and time:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. From the **View Transactions** screen, select the required date range.

   ![](Resources/Images/Searching_for_a_Transaction_2_171x46.png)

   Figure 15:  Available Search options for date and time.
3. Click **Search** to display the relevant transactions.

## 6.6 Show all transactions for a specific day

To see all transactions that occurred on a specific day:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. Select **All**.
3. In **Date**, specify the date (by default, todayâs date is shown). To search across a date range, select **To** and specify the date. The range you can search across depends on the type of search â it may be one day or up to 180.

   To narrow your search further to a specific time or range, specify the time, for example:

   ![](Resources/Images/Searching_for_a_Transaction_2_171x46.png)

   Figure 16:  Available Search options for date and time.

## 6.7 Setting default search options

You can tailor your default search parameters so that your current selections are used in future.

To set your current search parameters as the default:

1. Select **Card Activity** > **View Transactions** to display the **View Transactions** screen.
2. From the **View Transactions** screen, click the arrow to the right of **Search**.
3. Choose **Set Ticked as Default**.

   ![](Resources/Images/Set_Ticked_as_Default.png)

   Figure 17: The menu option for setting the ticked items as default.

## 6.8 Next Steps

For information about interpreting the results displayed in the **View Transactions** screen and the colour-coding used, see [Viewing Transaction Details](Viewing_Transaction_Details.htm).

After finding the transaction(s) you want to examine, you can explore further details, for example, to discover why a transaction was declined. For more information about how to drill down deeper into transaction details, see [Examining a transaction in detail](Viewing_Transaction_Details.htm#Examinin).