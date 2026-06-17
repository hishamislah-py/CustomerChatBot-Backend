# 7 Viewing Transaction Details

This topic describes how to display a list of transactions using the **View Transactions** screen, and how to drill down deeper into the transaction details.

To display the **View Transactions** screen:

1. From the main Smart Client menu, select **Card Activity** > **View Transactions**.

   The **View Transactions** screen appears.

   For information about how to search for transactions, see [Searching for a Transaction](Searching_for_a_Transaction.htm).

## 7.1 Understanding the View Transaction Screen

The **View Transactions** screen provides a wealth of information about each transaction and the ability to drill down into the details (described later). This section explains what information is displayed and the colour-coding used to highlight the different types of transaction.

The results of your search appear in colour-coded rows. The colours are explained in the key at the bottom of the screen. When an option at the top of the screen is selected, only those types of transactions are displayed, for example, Auth Not Cleared, Declined.

Use the scroll bar at the bottom of the screen to view all the fields.

You can sort the list (for example, by date or transaction type) by clicking on the column headers and using the up and down arrows to sort in ascending or descending order.

![](Resources/Images/View_transactions_TLID.png)

Figure 18:  The View Transactions screen

The following information is shown for each transaction:

the information displayed depends on the type of transaction, for example, more information is shown about authorisations than about presentments.

| Column | Description |
| --- | --- |
| **Token** | Unique Thredd 9-digit token assigned to this card. |
| **Scheme** | The scheme name configured by Thredd Implementations during set up. |
| **Product** | Specific card networkâs product. |
| **Date** | Date and time the transaction occurred. The time relates to Thredd time, for example, GMT. |
| **Location** | Location provided by the merchant. |
| **Transaction** | Type of transaction, such as authorisation, balance adjustment, presentment, and auth reversal. |
| **Status** | Transaction status, such as Settled. |
| **T Ccy** | Transaction currency. |
| **Tx Amt** | Transaction amount (in the transaction currency). |
| **Bill Amt** | Bill amount (in the currency of the card). |
| **Act Bal** | Actual balance after the transaction. |
| **Blk Amt** | Blocked amount (pending payments) after the transaction. |
| **Avl Bal** | Available balance after the transaction. |
| **F Fee** | Fixed fees levied against the transaction. |
| **R Fee** | Rate-based fee. Fees levied against the transaction based on a percentage charge. |
| **Fx Pdg** | Financial padding (to allow for currency fluctuations) |
| **MCC Pdg** | Financial padding applied to transactions in specific MCCs (typically used for hotels and rental cars where cardholders might be charged a little more than authorised for). |
| **Process** | Transaction processing code, for example, recurring fees, balance inquiry. |
| **Orig Stan** | 6-digit system trace audit number (STAN) used to link the authorisation and the presentment. |
| **TLID** | Transaction Link Identifier. This is an ID that links an original authorisation with transaction lifecycle messages, such as refunds and chargebacks. The identifier appears in Mastercard transactions only. For analysis, you can view details of the TLID as part of the DE105 message from Mastercard (see [Viewing TLID and Economically Related TransactionID Details](#ViewingTLID)). |
| **EconomicallyRelatedTransactionID** | This ID is for linking a TLID with a subsequent related transaction, such as a recurring payment, a refund, or an instalment if available. The identifier appears in Mastercard transactions only. More details of the Economically Related Transaction ID and its decoding from a DE105 message are described in [Viewing TLID and Economically Related Transaction ID Details](#ViewingTLID). |
| **Customer ref** | An alphanumeric identifier unique to the cardholder which is different to the Thredd token. This is defined in the client's web service calls. |
| **Notes** | Information about the transaction, such as why a decline has happened.  The **Notes** field is a useful source of information about a transaction, particularly for declines, as it can point you to what has happened. For example, in the case of a decline, an incorrect PIN or the transaction exceeding the maximum permitted limit. Scroll right on the **View Transactions** screen to display it. |

## 7.2 Examining a Transaction in Detail

This section explains how to drill down deeper into the details of a specific transaction.

To display more details about a particular transaction:

1. Highlight the transaction in the **View Transactions** screen, then right-click.
2. Select **More Details** from the drop-down menu.

   ![](Resources/Images/Viewing_Transaction Details_1.png)

   Figure 19:  Further options available in the View Transactions screen

   Use the **Copy to Clipboard** and **Copy Whole Row to Clipboard** options to copy information about the transaction. This is useful, for example, to copy a token number across screens.
3. Choose **View Transaction Details** to display the **Transaction Details** screen. The **Transaction Details** screen shows detailed information about the transaction, including the transaction date, status, card acceptor name location, transaction amount and fees. The example below shows details for an authorisation advice:

   ![](Resources/Images/Transaction_Details_Screen.png)

   Figure 20: Transaction Details screen

   The details shown depend on the type of transaction, for example, fields relating to presentments, such as Settlement Amount (DE005), are blank for authorisations. The available options are explained in more details in the following section.

#### About the Transaction Details screen

The following section explains the main transaction information shown:

DE000âDE999 refers to the Data Element number (for example, DE004 = Transaction Amount). For a full list of Data Elements and their definitions, refer to the Mastercard *Customer Interface Specification*, or*Visa Base* manual, or *Discover Getting Started Guide*.  
Click the arrow available next to some fields to display more information, for example, POS data (DE061).

The available fields depends on the transaction source network and transaction type.

| Field | Description |
| --- | --- |
| **Message Type** | The type of transaction, such as an authorisation or presentment. |
| **Token** | The unique token number associated with the transaction. |
| **Date Expiry** | The expiry date provided at the time of the transaction (useful to check in case the cardholder has entered an incorrect expiry date). |
| **POS entry mode (DE022)** | How the transaction was created, for example, contactless at a machine, ecommerce, online, ATM. ICC indicates the card was physically inserted into a machine and the PIN entered. |
| Network Reference ID (DE123) | The Network Reference ID (NRID) is a numeric ID generated by DCI and remains unchanged for the life of the Card Transaction.  **Note:** Only applies to Discover Global Network. |
| Transaction Date | The date of the transaction. Format YYYY-MM-DD HH:MM:SS:MS. |
| **Message Reason Code** | Provides the receiver of a request, advice or notification message with the reason, or purpose, of that message.  **Note:** Only applies to Discover Global Network. |
| **Advice Reason Code** | Mastercard Authorisation Advice Reason Code. Explains why Mastercard Stand-In processing (STIP) occurred or why an advice was created.  **Note:** This field will only be present for transactions received by Thredd from Mastercard. |
| Visa Response Code (DE63) | Visaâs Response Data, exactly as provided from Visa to Thredd.  **Note:** This field will only be present for transactions received by Thredd from Visa. |
| **Response status (DE039)** | The status sent back to the merchant, for example, 05 - do not honour. Click the arrow next to this field to see more information. |
| **STAN (DE011)** | System Trace Audit Number. This links the authorisation and presentment (note this number is not unique). |
| **Processing code** | Indicates the type of transaction, for example, a debit. |
| **Additional Amounts (DE054)** | Contains additional amount information for the transaction, if relevant. For example, for purchase with cashback transactions, the additional amounts field will be present with the cashback amount. |
| **POS data (DE061)** | Useful information about the machine on which the transaction took place. Click the arrow next to this field to see more information, for example, if the card is in card capture status. |
| Additional Amounts (DE054) | Contains additional amount information for the transaction, if relevant. For example, for purchase with cashback transactions, the additional amounts field will be present with the cashback amount. |
| **Card Acceptor Identification Code (DE042)** | Code relating to the specific Point of Sale (POS) terminal. |
| **Card Acceptor Name Location (DE043)** | Merchantâs details. |
| **Additional Response Data (DE044)** | Visaâs Additional Response Data, exactly as provided from Visa to Thredd. This will only be present for transactions received by Thredd from Visa Base1, if DE44 was present.  It provides information on Visaâs validation checks of data in the message. This will only be set for Visa online authorisation transactions. |
| **Till Time** | Time provided by the merchant (can be incorrect but matches what is on the receipt). |
| Card Acceptor Terminal Identification (DE041) | Uniquely identifies the terminal which accepted the card. Always present if the card data was read by a terminal. |
| Response Source | Indicates which system sent the 0110 or 0210 response to the terminal. Normally present only for some Authorisation advices and Authorisation reversals. |
| Response Reason | Indicates the reason why the Response Source sent a response to the terminal. Normally present only for some Authorisation advices and Authorisation reversals. |
| **Transaction ID** | Identifier for tracing a specific transaction and narrowing a search. This a unique identifier generated by Thredd to help identify and search for transaction in the Thredd platform. |
| **Transaction Amount (DE004)** | Transaction amount and currency. |
| **Settlement Amount (DE005)** | Settlement amount and currency. |
| **Billing Amount (DE006)** | Amount applied to the account in the currency of the card. |
| Amounts, Transaction Fee (PDS0146) | The fee charged (for example, by the acquirer) for transaction activity in the transaction currency code. This field is only applicable to presentments. |
| **Merchant Category Code (MCC)** | Code that describes a merchant's primary business activities. |
| **Retrieval Reference Number (DE037)** | A unique reference to the transaction assigned by the acquirer. All messages related to the same transaction (reversals, presentments, chargebacks) should have the same RRN; however, this may not be enforced. |
| **Acquirer Reference Data (DE031)** | Acquirer Reference Number/Data. ISO 8583 field 31.  The acquirer reference number exists for clearing messages only (Financial advices/notifications, and Chargeback advices/notifications (and reversals of)). |
| Acquirer ID in ARN (DE31) | Acquirer ID found in the Acquirer Reference Number (ARN). |
| Acquirer ID | Acquiring Bank ID as assigned by the network. Note that the format differs depending on whether this is an Authorisation or a Financial type message.  For Authorisation messages:   * 2 digits length of Acquirer ID (01 to 09) * Acquirer ID   For Financial messages:   * 6 digit Acquirer ID (possibly with leading zeros) |
| FID (DE033) | Identifies the acquiring institution forwarding a Request or Advice message. |
| Authorisation Code | Authorisation code generated by Thredd for approved and declined authorisation requests. |
| **Network** | The network that processed the transaction. |
| DE053 | The Security-Related Control Information provides specific information about PIN block encoding and PIN data encryption in processing PINs entered at the point of interaction. |
| **Request Time** | The time when Thredd receives this authorisation, in the local time zone of the Thredd servers. |
| **Response Time** | The time when Thredd sends the response (the difference between the request and response times is shown below in milliseconds), in the local time zone of the Thredd servers. Note that the response time in milliseconds is the time for the *entire* transaction to complete across all parties. |
| **ICC Data (DE055 - 0100)** | Data from the cardâs chip. Click the arrow next to this field to see more information, for example, you can check whether the online and offline PINs were verified when making a transaction. |
| Difference (in milliseconds) | The difference, in milliseconds, between the request time and the response time of the transaction. |
| ****Additional data (DE048**)** | Information about 3D Secure (payer authentication) for online transactions. Click the arrow next to this field to see more information. For more information, see [Viewing 3D Secure details.](#Viewing) |
| **DE034** | The Primary Account Number (PAN), Extended, identifies a customer account or relationship. This is only used when the PAN begins with a 59 BIN. |
| **Fees Detail Note** | Shows any fees applied to this transaction. |
| **Function Code** | The Function Code data element is the code indicating the specific purpose of the message within the message class.  **Note:** Only visible for Discover Global Network authorisations. This setting is not displayed in the above screenshot. |
| **Surcharge Fee** | This field contains the data to support transaction-level information when a Service Establishment assesses a surcharge on a Card Sale.  **Note:** Only visible for Discover Global Network authorisations. This setting is not displayed in the above screenshot. |
| **Additional Authorization Data DGN** | This data element contains multiple tags with unique functions. Please refer to the table for details.  **Note:** Only applies to Discover Global Network. This setting is not displayed in the above screenshot. |
| **Transaction Destination IIC** | The Transaction Destination Institution Identification Code (IIC) data element is the code identifying the institution that is the transaction destination.  **Note:** Only applies to Discover Global Network. This setting is not displayed in the above screenshot. |
| **Transaction Originator IIC** | The Transaction Originator Institution Identification Code (IIC) data element is the code identifying the institution that is the transaction originator.  **Note:** Only applies to Discover Global Network. This setting is not displayed in the above screenshot. |

### 7.2.1 Viewing all transactions for the card

To display a list of all the transactions for the specified token:

1. Highlight the transaction in the **View Transactions** screen, then right-click and choose **Show All results for the Card**.

   ![](Resources/Images/Show_all_results_for_the_card.png)

   Figure 21: Show All results for the Card menu option

   You can also double-click on a transaction to display all the results.
2. Review all the activity for the specified card in the **View Transaction** screen.

   ![](Resources/Images/View_All_Transactions_for_a_Card.png)

   Figure 22: View all activity for the selected card

### 7.2.2 Viewing 3D Secure details

3D Secure is a set of online protocols created by the different card networks to improve the level of security in card-not-present (CNP) transactions. Branded with different names, including 3D Secure, Mastercard ID Check, Verified by Visa, and 3DS, 3D Secure provides additional protection when making ecommerce transactions. By default, authentication is biometric (âin client appâ authentication), with fallback authentication set to 'OTPSMS', where a one-time passcode (OTP) is sent to the cardholder via SMS. For more information, see the *3D Secure Guide RDX and Biometric or In-App Authentication Guide*.

#### Viewing Mastercard 3D Secure transactions

To see information about a Mastercard 3D Secure transaction:

1. In the **View Transactions** screen, right click the transaction and select **More Details** > **View Transaction Details**.
2. In the **Transaction Details** screen, inspect the **Additional Data (DE048)** field (bottom right).

   ![](Resources/Images/Viewing_Transaction_Details_2.png)

   Figure 23: Additional Data (DE048) field on the Transaction Details screen
3. Click the arrow ![](Resources/Images/Viewing_Transaction_Details_3_22x19.png) to expand the information displayed. For example:

   ![](Resources/Images/Viewing_Transaction_Details_4.png)

   Figure 24: Decoded values in the DE048 field on the Transaction Details screen

   - **PDS42** contains Electronic Commerce Indicators (ECI) results.  
   - For non-3D Secure transactions such as eCommerce merchants who are not enrolled or have disabled the checks, these display as âUCAF data collection is not supported by the Merchantâ.  
   - **PDS43** contains the Accountholder Authentication Value (AAV). The results are provided by the 3D Secure Provider to the Merchant/Acquirer and are submitted within the Authorisation request.

   External Host Interface (EHI) data also provides 3D Secure Authentication results containing AAV data, for example:  `<cavv>jDjy8/KIra5GCBAVEjPpB0kAAAA=</cavv>`. For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).

#### Viewing Visa 3D Secure transactions

To see information about a Visa 3D Secure transaction:

1. In the **View Transactions** screen, right click the transaction and select **More Details** > **View Transaction Details**.
2. In the **Transaction Details** screen, inspect the **Additional Response Data (DE044)** field (left side of the screen).

   ![](Resources/Images/visa_3DSecure_SC.png)

   Figure 25: Additional Response Data (DE044) field on the Transaction Details screen
3. Click the arrow ![](Resources/Images/Viewing_Transaction_Details_3_22x19.png) to expand the information displayed. For example:

   ![](Resources/Images/visa_Â£DSecure_2_SC_dropshadow_324x167.png)

   Figure 26: Transaction Detail message displayed when the Additional Response Data (DE044) field is expanded.

   **Field 44.15** â Thredd Received Cardholder Authentication Verification Value (CAVV)

   EHI data also provides 3D Secure Authentication results containing AAV data, for example: `<cavv>AAABBBQ5KVcglogDBDkpEFQKZyo==</cavv>`. For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.com/EHI_Guide.htm).

### 7.2.3 Viewing TLID and Economically Related Transaction ID details

You can view details of a TLID and, if available, the Economically Related Transaction ID as part of the DE105 message. To obtain the IDs, you use the decode option.

To view TLID and Economically Related Transaction ID details:

1. In the **View Transactions** screen, right-click the transaction and select **More Details** > **View Transaction Details**. A screen appears that has details of the transaction.
2. Click the **Additional details** tab. The DE 105 field is populated with the message.

![](Resources/Images/Transaction_Details_TLID.png)

Figure 27: DE 105 Field with message

3. Click the arrow ![](Resources/Images/Viewing_Transaction_Details_3_22x19.png) to show the **DE105 Decoding** screen.
4. Click **Decode**. The decoded values in the DE105 message appear below the button (as in the following example).

![](Resources/Images/Decoded_DE105.png)

Figure 28: Decoded values from the DE 105 message