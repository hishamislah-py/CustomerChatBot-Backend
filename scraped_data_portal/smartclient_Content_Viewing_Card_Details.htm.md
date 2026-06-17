# 8 Viewing Card Details

This topic explains how to view more information about cards and how to drill down into the details.

## 8.1 Display the Card Master

You can access card details either through the **View Cards** screen or the **Transaction Details** screen.

1. Display the Card Master using:

   1. Either **Card Activity** > **View Cards** > **View Attributes**
   2. Or **Card Activity** > **View Transactions** > **More details** > **View Transaction Details** >**Show Card Details** > **Show Card Attributes**

## 8.2 View Card Details using the Card Information

1. Select **Card Activity** > **View Cards**. Search for a card (for information, see: [Searching for a Card](Searching_for_a_Card.htm)).
2. From the **View Cards** screen, highlight the card in the list, right-click and choose **View Attributes** to display the **Card Master** screen.

   ![](Resources/Images/SC_Card_Master_JD_793x505.png)

   Figure 29:  The Card Master screen

## 8.3 View the Card Details from a Transaction

To view card details:

1. Select **Card Activity** > **View Transactions** . Search for a transaction (for information, see [Searching for a Transaction](Searching_for_a_Transaction.htm)):
2. Highlight the transaction, right-click and choose **More details** > **View Transaction Details**.
3. Click the **Show Card Details** button (bottom of screen). The **Card General Details** screen shows information about the card associated with this transaction.

   ![](Resources/Images/Show_Card_General_Details.png)

   Figure 30:  The Card General Details screen
4. Click the **Show Card Attributes** button (bottom of screen) to display the **Card Master** screen with details about the cardholder and card purchaser for the selected token.

   ![](Resources/Images/SC_Card_Master_JD_793x505.png)

   Figure 31:  The Card Master screen

   You can also display the **Card Master** screen by right clicking on a transaction and choosing **More Details** > **View Attributes**.
5. Click **Close** when you have finished reviewing the Card Details on the Card Master screen.

## 8.4 About the Card Details

The following table explains the main card information and useful fields in the **Card Master** screen:

| Field | Description |
| --- | --- |
| **Card Purchaser** | Name and address of card purchaser. This may differ to the cardholder if the card was purchased by a company but is used by an employee.  If an alternative address has been submitted via Thredd API, then this information appears here. For details, see: [â¢ Cards API Website (REST)](https://cardsapidocs.thredd.com/docs/create-card-2). (**Note**: The `fulfilment` object fields are used to specify card purchaser details â where a separate delivery address is specified for the card manufacturer to deliver the card. If no details are supplied in the fulfilment object, then Card Purchaser is populated from the Cardholder address fields.) [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Web Services Guide (SOAP).](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Create.htm?Highlight=Ws_CreateCard) (**Note**: The `Delv_` fields are used to specify card purchaser delivery details â where a separate delivery address is specified for the card manufacturer to deliver the card. If no details are supplied in the delivery address fields, then Card Purchaser is populated from the Cardholder address fields .) |
| **Card Holder** | Name and address of the person in possession of the card. The cardholder address reflects the Address Verification Service (AVS) checks that are performed.  Records can be amended using Thredd API. For details, see:  [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Cards API Website (REST)](https://cardsapidocs.thredd.com/docs/create-card-2)   [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Web Services Guide (SOAP).](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Create.htm?Highlight=Ws_CreateCard) |
| **Actual Balance** | Current card balance. |
| **File Generated On** | Date the token was created. |
| **Status** | Card status code and description, for example, 00 - All Good. For more information, see [Appendix B: Card Status Codes](Appendix_B_Card_Status_Codes.htm). |
| **Activation Date** | Date the card was activated (if blank, the card is not activated yet) |
| Thredd Expiry | Card expiry date held on the Thredd platform |

The fields in the right-hand pane relate to the rules governing card acceptance. These are known as Usage Rules which you can set to control card acceptance. For example, you can prevent a card from being used on gambling sites by disallowing specific Merchant Category Codes (MCC). For information about the usage rules and card acceptance methods, see [Appendix C: Usage Groups](Appendix_C_Usage_Groups.htm).

#### Viewing 3D Secure Enrolment Details

To view the 3D Secure Enrolment Details:

1. [Display the Card Master](#Display).
2. In the **Card Master** screen, click the **Fetch 3DS Credentials** button (bottom middle of screen) to display the 3the **3DS Credentials** screen. This screen contains a list of the 3D Secure authentication methods that the card is enrolled in (e.g., OTP SMS, KBA or biometric).

   ![](Resources/Images/3DS_Credentials.png)

   Figure 32:  The 3D Credentials screen

   For more information on 3D Secure, see the [3D Secure Guide](https://docs.thredd.ai/3D_Secure_RDX.htm).

## 8.5 Viewing the Card Limits Graph

You can get an 'at a glance' view of the daily and cumulative limits in place for a card or an account, as per the product configuration, using the **Limit Graph**. This graph also shows the frequency of the cardâs use, cumulative cash withdrawal, load, payments in, payments out, and POS (Point of Sale) spend amounts for the specified period. For more information about the limits set on a card, see [Viewing card limits](#Viewing3).

The **Limit Graph** is useful to understand when spend limits are being reached or how much is still available to use.

To view the **Limit Graph** screen:

1. From the **View Transactions** screen, highlight a transaction in the list, right-click and choose **More details**.

   ![](Resources/Images/Navigate_to_Show_Limits.png)

   Figure 33:  The Show Limits menu option
2. Choose **Show Limits** to display the **Limit Graph**.

   The following example shows the data by day, every 31 days, and 365 days. The cumulative time periods are configurable.

   ![](Resources/Images/SC_Limit_Graph_JD_944x277.png)

   Figure 34:  The Card Limits Graph

   ## 8.6 Viewing the Card Limits

   The card limits are based on the **Group Limit** settings in the **Card Master** screen. See [Display the Card Master](#Display) for instructions on how to navigate to the Card Master screen.

   From the Card Master screen, click the arrow next to **Group Limit** in the **Card Master** screen to see the limits configured. For example:

   ![](Resources/Images/Group_Limit_Settings_1.png)

   Figure 35: The Group Limit Settings screen showing an example of typical limits

## 8.7 Viewing Card Status History

Using the **Card Status History** screen, you can see a history of the activities completed on the card, such as balance adjustments and loads.

To view a cardâs status history:

1. From the **View Transactions** screen, highlight a transaction in the list, right-click and choose **More details**.
2. Choose **Status History**. The **Card Status History** screen appears.

   ![](Resources/Images/SC_card_status_history_JD.PNG)

   Figure 36:  The Card Status History screen

There are three tabs: **Card Status History**, **Card Spending History** and **Show Limits**.

By default, the **Card Status History** tab appears, showing a history of card activity.

The **Notes** field displays useful information about activity - you can adjust the column widths to see it. You can also sort the list (for example in date order) by clicking on the column headers and using the up and down arrows to sort in ascending or descending order.

The other tabs are described below.

### 8.7.1 Viewing spending history

To view the spending history of a card:

1. View the Card Status History screen. See [Viewing Card Status History](#Viewing4) for instructions.
2. From the **Card Status History** screen, click the **Card Spending History** tab. A history of spending activity appears.

   ![](Resources/Images/SC_card_spending_history_JD.PNG)

   Figure 37:  The Card Spending History tab on the Card Status History screen

### 8.7.2 Viewing card limits

You can view the limits that are applied to a card, such as limits on cash withdrawals, the number of times a cardholder can use an ATM or load their card.

To view card limits:

1. View the Card Status History screen. See [Viewing Card Status History](#Viewing4) for instructions.
2. From the **Card Status History** screen, click the **Show Limits** tab. Daily and accumulated limits for the card are shown together with the transactions and amounts contributing to these limits.

![](Resources/Images/SC_show_limits_JD.PNG)

Figure 38:  The Show Limits tab on the Card Status History screen

## 8.8 Viewing Card Fees and Fee Settings

You can see the fees associated with a card, which were configured during product set up. For example, you can see the domestic and non-domestic fees that apply when the card is used at home and abroad. For more information on the setting up of fees, see the [Thredd Fees Guide](https://docs.thredd.com/Fees_Guide.htm).

To view card fees and settings:

1. From the **View Transactions** screen, highlight a transaction in the list, right-click and choose **More details**.
2. Choose **Card Details inc Fees** to display the **Card Master** screen with two additional tabs.

   For more information about the details shown in the **Card Master** screen, see: [Viewing Card Details](#).
3. Click the **Fees** tab to view the fees associated with the card.

   ![](Resources/Images/Viewing_Card_Fees_Tab.png)

   Figure 39:  The Fees tab on the Card Master screen

   * Fees can only be altered using a Change Request. You cannot update fees using Smart Client. Contact your Thredd Account Manager for more information.
   * Local (domestic) fees, fixed fees, and fees based on a percentage are shown.
   * **Partial Allowed** indicates whether a partial fee is permitted or not. For example, if the fee is Â£1 but the customer has only fifty pence in their account, only a partial fee of 0.50 can be claimed.

## 8.9 Viewing Payment Tokens

You can see information about payment tokens, such as when a token was set up with MDES/VDEP, and the form factor which is the type of device used for the wallet (for example, a mobile phone). For more information, see [Managing MDES and VDEP cards](Managing_MDES_VDEP_cards.htm).

To view payment tokens:

1. From the **View Transactions** screen, highlight a transaction in the list, right-click and choose **More details**.
2. Choose **Card Details inc Fees** to display the **Card Master** screen with two additional tabs.
3. Click the **Payment Tokens** tab. The results appear in colour-coded rows. The colours are explained in the key at the bottom of the screen.

   ![](Resources/Images/Viewing_Card_Details_4.png)

   Figure 40:  The Payment Tokens tab on the Card Master screen

4. Double click the required Payment Token to open the Payment Token screen.

   ![](Resources/Images/Payment_Token_Screen.png)

   Figure 41:  The Payment Token screen

   For more information, see [Managing MDES/VDEP cards](Managing_MDES_VDEP_cards.htm).

## 8.10 Viewing Fees Configuration

You can see information about the fees that apply to a card, including recurring fees, and authorisation fees, using the **Fees Configuration** screen.

To view fees configuration:

1. From the **View Transactions** screen, highlight a transaction in the list, right-click and choose **More details**.
2. Choose **Show Fees Settings**. The **Fees Configuration** screen appears.

   ![](Resources/Images/Fees_Configuration.png)

   Figure 42:  The Fees Configuration screen

   Use the scroll bars to see more information on the right-hand side, such as the **Note** field.

The Fee Groups displayed in the Fees Configuration screen are:

* **Auth Fee (Group)** â Displays fees configured on the card which are applied during the authorisation stage based on the processing code.
* **Recurring Fee (Group)** â Displays any rule-based fees which apply to the card such as a dormancy fee due to card inactivity.
* **Webservice Fee (Group and Product)** â Displays any fees triggered by Web Services.

## 8.11 Next Steps

For information about managing cards and transactions, such adjusting a balance, or activating a card, see [Managing Cards](Managing_Cards.htm). For more information on fee setup, see the [Thredd Fees Guide](https://docs.thredd.com/Fees_Guide.htm).