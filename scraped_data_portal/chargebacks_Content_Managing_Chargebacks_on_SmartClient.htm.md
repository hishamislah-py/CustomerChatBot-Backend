# 4 Managing Chargebacks on Smart Client

Smart Client enables you to view Visa and Mastercard chargebacks.

For Mastercard transactions only you can raise chargebacks requests to Mastercard and manage your charged back transactions. This service uses the Mastercom API and requires that you first sign up for the service and enable the API data feed via your issuer. See [How to Implement](Chargeback_Options.htm#_How_to_Implement).

Using Smart Client, you are able to:

* View details of existing chargebacks across your programme or for a specific card. See [Viewing Chargebacks](#_Viewing_Chargebacks)
* View details of the transaction linked to a chargeback. See [Viewing Transaction Details](#_Viewing_Transaction_and).
* View details of the Presentment transaction linked to a chargeback. See [Viewing Presentment Details](#_View_Presentment_Details).

  Functionality described below is provided for Mastercard only.

* Retrieve information about a disputed transaction from the acquirer (prior to raising a chargeback). See [Creating a Retrieval Request](#_Create_a_Retrieval).
* Raise a chargeback for a single transaction. See [Creating a Chargeback](#_Creating_a_Chargeback).
* Raise multiple chargebacks in one transaction, using a chargeback bulk upload spreadsheet. See [Creating Bulk Chargebacks](#_Creating_Bulk_Chargebacks).
* Attach a file to a chargeback. See [Uploading Chargeback Documentation](#_Uploading_Chargeback_Documentation).
* Retrieve documentation previously uploaded for a chargeback case. See [Downloading Chargeback Documentation](#_Downloading_Chargeback_Documentatio).
* Withdraw a chargeback. See [Reversing a Chargeback](#_Reverse_a_Chargeback).
* Re-raise a rejected chargeback. See [Re-raising a Chargeback](#_Re-raise_a_Chargeback).
* Create a Fee Collection request. See [Managing Fee Collections](#_Managing_Fee_Collections).
* Send a SAFE report to Mastercom for a fraudulent transaction. See [Creating a Mastercom SAFE Report](#_Creating_a_Mastercom).

  You may require access to be set up on your account to view some of these options. Please contact Thredd Support for details.

## 4.1 Creating a Chargeback

Currently supported for Mastercard cards only.

This option enables you to raise a chargeback to Mastercom for a disputed transaction. You can do this with or without attaching documentation.

The transaction must be in the Presentment state in order to create the chargeback (i.e., the transaction has been previously authorised, and the funds have been debited from the cardholderâs account).

1. In the **View Transactions** window, right-click the transaction being disputed by the cardholder and select **Actions** > **Create Chargeback**.
2. In the **Chargebacks** window, enter the details of the chargeback. Refer to the table below for details.

   ![](Resources/Images/Managing_Chargebacks_on_Smart.png)

   Figure 5: Create a Chargeback
3. To create the chargeback request, click **Create Chargeback**.

   If all the details provided are correct, then a success response is returned from Mastercom.

   If the details provided are not correct, then an error response is returned from Mastercom.

#### Handling error codes

An error code starting with â1â indicates errors from Mastercom; an error code starting with â5â indicates the error has occurred during Thredd processing of chargeback request. You can try fixing the details and resending the chargeback request or contact Thredd support.

| Option | Description |
| --- | --- |
| Full Chargeback | Check this option if you want to dispute the full amount of the transaction. For example, for goods not received or a fraudulent transaction. |
| Partial Chargeback | Check this option to dispute a part amount of the transaction. For example, cardholder disputes the billing amount. |
| Chargeback Currency | Select the chargeback currency. Depending on the card region, options include the local card billing currency (e.g. GBP) or the international scheme currency used by the card scheme (e.g. USD).  The Amount of chargeback field is updated based on the selected currency. |
| Amount of Chargeback | Enter the chargeback amount. Up to two decimal places are allowed. If the Full Chargeback option is checked, this field is disabled, and the full amount taken during the Presentment transaction stage is displayed. |
| Reason for Chargeback | Select one of the reasons for the chargeback from the drop-down list. For a full list of chargeback reasons, see [Chargeback Reason Codes](Appendix A.htm).  If the reason is fraud related, you must create a SAFE Report before issuing the chargeback.[1](#Notes) |
| Select text format | The available text format options depend on the Reason for chargeback previously selected. Some chargeback reasons do not provide a default text format. If you are unsure as to which format to select, check with your Account Manager.  Depending on the selection, this reason is also populated in the Supporting Text field. |
| Documentation Indicator | Select how documentation to support this chargeback will be supplied:   * Supporting documentation is not required * Supporting documentation will follow   Refer to the Mastercard Guide for details of the types of Chargeback Reason Codes that require supporting documentation. |
| Days Allowed | Read-only field indicating the number of days allowed to process the chargeback. This varies between region and chargeback reason code. Typical values are 90 days, 120 days and 540 days. |
| Days Remaining | Read-only field indicating the number of days remaining to process the chargeback. If this number is negative, it indicates the period in which to submit the chargeback has been exceeded.  If you submit the chargeback, Mastercom will reject it. |
| Supporting Text | Add a description, to be displayed in the DE 72 field of the chargeback message sent to Mastercom. This field can also be populated with a standard message as selected in the Select text format field. |
| Note | Free text field to enable you to add an internal note about the chargeback request. This note is not passed on to Mastercom. |
| Edit Exclusion Indicator | Check this option to indicate to Mastercom they should ignore the Days Allowed/Days Remaining indicator. This enables you to still raise a chargeback, even if the Mastercard default eligibility period has expired.[2](#Notes)  This functionality is not yet released. Check with your Account Manager for details. |
| Credit to Card | If you check this option, the chargeback amount will be credited back to the card. [3](#Notes) |

#### Notes

1. If the reason for raising the chargeback is fraud related, Mastercard require you to first raise a SAFE report to report the fraud before raising the chargeback. See [Creating a Mastercom SAFE Report](#_Creating_a_Mastercom).
2. In some specific circumstances, it may be possible to extend the chargeback validity period for a specific transaction, even if it has expired. For details, check with your issuer.
3. Some Program Managers and issuers prefer to refund the cardholder immediately on raising a chargeback, since the chargeback process can take several weeks or months to complete. Note that raising a chargeback does not necessarily mean that the acquirer or Mastercard will approve the chargeback. You may prefer to wait for confirmation before crediting the cardholder.

## 4.2 Viewing Chargebacks

Supported for both Mastercard and Visa cards.

1. From the Smart Client menu, select **Card Activity** > **Chargebacks**.
2. In the **Chargebacks** window, you can view raised chargeback details for a specific card or for all cards:

   To query chargebacks for a specific card, in the **Token** field enter the public token number of the card you want to query.

   To list chargebacks within a specified date range and status, select the Status and date range and click **List**.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_1.png)

   Figure 6: Chargeback Window on Smart Client

3. To view details of the chargeback, use the scrollbar at the bottom-left corner of the window to scroll through the chargeback transaction table.
4. To perform further actions related to the chargeback, right-click the transaction row. The options displayed depend on the type of card and chargeback status. See the examples below:

   ![](Resources/Images/Managing_Chargebacks_on_Smart_2.png)

   Figure 7: Chargeback File Actions Menu

To display details for the specific the card issuer scheme used by your programme, click the **Select Scheme** button (Bottom-left of window), click **Clear All** and then check the relevant Card Processing Scheme. This option is only relevant if your programme supports multiple card schemes.

## 4.3 Chargeback Transaction Options

This section provides details of options you can use to view and manage the transaction and card that is linked to a chargeback.

### 4.3.1 Showing all Transactions for a Card

1. To view all transactions linked to the card, in the Chargebacks window, right-click the required transaction and select **Show All Transactions for this Card**.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_3.png)

   Figure 8: Transaction Right-Click Menu

2. The **View Transactions** window appears, with the cardâs public token preselected and displaying a list of transactions linked to the card.

### 4.3.2 Crediting a Chargeback to a Card

This option enables you to manually credit the charged back amount to the cardholderâs account. It is typically used once you have confirmation from the card scheme that the chargeback was successful.

1. To credit the chargeback amount back to the card, in the Chargebacks window, right-click the required transaction and select **Credit Chargeback to Card**.
2. A popup message is displayed, asking you to confirm. Click **Yes**.  
   The chargeback amount is credited back to the cardholderâs account.

When creating a chargeback, you can also tick the credit to card option to automatically credit the card. See [Creating a Chargeback](#_Creating_a_Chargeback).

### 4.3.3 Viewing Linked Transaction Details

This option enables you to view details of the transaction being charged back.

1. To view further details about the transaction on which you have raised the chargeback, in the **Chargebacks** window, right-click the required transaction and select **Create Report**.

   The **Transaction Details** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_4.png)

   Figure 9: Transaction Details Window

2. Use the buttons at the bottom right of the window to view further details.

Options displayed on this window may vary, depending on your version of Smart Client and the fields enabled for your account.

### 4.3.4 Viewing Chargeback History

1. To view the Chargeback history of a chargeback transaction, in the **Chargebacks** window, right-click the required transaction and select **Chargeback History**.

   The **Chargeback History** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_5.png)

   Figure 10: Chargeback History Window

### 4.3.5 Viewing Presentment Details

You can use this option to view details of the presentment linked to the chargeback.

1. To view details of the presentment transaction linked to the chargeback, in the **Chargebacks** window, right-click the required transaction and select **View Presentment Details**.

   The **View Transactions - Presentments** window is displayed, showing details of the linked presentment transaction.

   If there is a second presentment, to view details right-click the chargeback and select **View Sec Presentment Details**.

### 4.3.6 Creating a Retrieval Request

A retrieval request occurs after a cardholder communicates with their issuer to question or dispute a transaction. You can use Smart Client to create a retrieval request from the acquirer for documentation related to a disputed transaction. The acquirer fulfils a retrieval request by sending documentation through Mastercom.

After receiving the retrieval request documentation from the acquirer, you can proceed with the chargeback if required.

Retrieval requests are optional. You can proceed to create a chargeback even if you have not created a retrieval request.

To raise a retrieval request:

1. In the **Transactions** window, right-click the required transaction and select **Create Retrieval Request**.

   The **Create Retrieval Request** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_6.png)

   Figure 11: Retrieval Request Window

2. In the **Retrieval Request Reason Code** field, select an appropriate reason for the retrieval request. For details, see the table below.
3. In the **Document Required** field, select the format required. Options are:

   * Hard copy of the original document
   * Copy or image of the original document
   * Substitute draft
4. Click **Submit**. A confirmation message is displayed, indicating if the retrieval request was successfully registered with Mastercom. In this case a **Request ID** and **Claim ID** are returned, which you can use to track the status of the request. If the retrieval request failed, a message box is displayed, providing details of the error. For example, a request has already been submitted. Please resolve the error and try again or contact Thredd support.

5. To close the message box, click **OK**.

#### Retrieval Request Codes

| Codes | Description |
| --- | --- |
| 6305 | Cardholder does not agree with amount billed. |
| 6321 | Cardholder does not recognize transaction. |
| 6322 | Request Transaction Certificate for a chip transaction. |
| 6323 | Cardholder needs information for personal records. |
| 6341 | Fraud investigation. |
| 6342 | Potential chargeback or compliance documentation is required. |
| 6343 | IIAS Audit (for healthcare transactions only). |
| 6390 | Identifies a syntax error return. |

#### Tracking the Status of the Request

Once the request has been successfully registered, you can track the status of the request as follows:

* You can view the new retrieval request raised in the Chargeback window.
* Once the acquirer responds to the retrieval requests, to download the documentation, right-click the retrieval request in the Chargeback window and select **File Actions** > **Get Documentation**. For details, see [Download Chargeback Documentation](#_Download_Chargeback_Documentation).

### 4.3.7 Uploading Chargeback Documentation

You can use this option to upload documentation to support a chargeback. The documents will be sent to Mastercom and made available to the acquirer.

Uploading a new file will overwrite any previous file uploaded to Mastercom.

1. To upload supporting documentation for the chargeback, in the **Chargebacks** window, right-click the required transaction and select **File Actions** > **Upload file to chargeback**.

   The following window is displayed:

   ![](Resources/Images/Managing_Chargebacks_on_Smart_7.png)

   Figure 12: Upload File to Chargeback Window

   If you have multiple files to upload, please add these to a zipped file and upload a single zip file. Examples of files you can include are items such as scanned documents, images and transaction receipts. Make sure that all documents scanned are clear and legible, and not truncated, or these may be rejected by Mastercard.

   You can only upload a single file. If you have mutiple files to upload, ensure they are in a zip file before you upload.

2. To select a file to upload, click **Browse**.
3. You can use the **Memo** field to provide further details of the file being uploaded.
4. To upload your supporting case documentation to Mastercom, click **Upload**.   
   The uploaded file is sent to Mastercom.

Once the file is uploaded, it cannot be deleted. However, you can replace this file with another one using the upload option. The uploaded file is end-to-end encrypted; Thredd does not have access to the details in the file.

### 4.3.8 Downloading Chargeback Documentation

You can use this option to view any case documentation which you previously submitted to Mastercom.

1. To download documentation linked to the chargeback, in the **Chargebacks** window, right-click the required transaction and select **File Actions** > **Download file from chargeback**.

   The following window is displayed:

   ![](Resources/Images/Managing_Chargebacks_on_Smart_8.png)

   Figure 13: Download File from Chargeback Window

2. To continue with the download, click **Download**. The file is downloaded to your computer.

   the downloaded file is end-to-end encrypted; Thredd does not have access to the details in the file.

### 4.3.9 Reversing a Chargeback

You can use this option reverse a chargeback that has been previously successfully raised and approved by Mastercard. This can be used if you do not want to proceed with the chargeback.

1. To reverse a chargeback, in the Chargebacks window, right-click the required transaction and select **Reverse Chargeback**.
2. A pop up message is displayed, asking you to confirm. Click **Yes**.

   A confirmation message is displayed, indicating if the chargeback was successfully reversed or if the chargeback reversal failed.

3. To close the message box, click **OK**. A chargeback reversal message is sent to Mastercom.

### 4.3.10 Re-raising a Chargeback

You can use this option re-raise a chargeback request that has been rejected. You should try and fix the issue before re-raising the chargeback. There is no limit to the number of re-raise chargeback requests.

1. To re-raise a chargeback, in the **Chargebacks** window, right-click the rejected chargeback transaction and select **Re-Raise Chargeback**.

   The following window is displayed:

   ![](Resources/Images/Managing_Chargebacks_on_Smart_9.png)

   Figure 14: Re-Raise Chargeback Window

2. Provide all the details as per the instructions in the [Creating a Chargeback](#_Creating_a_Chargeback) section and click **Save**.  
   The re-raised chargeback request is sent to Mastercom. A confirmation message is displayed, indicating if the re-raised chargeback was successful or if the request failed.

### 4.3.11 Creating Bulk Chargebacks

You can use the Bulk Chargeback CSV template to record details of your chargebacks. Please request a copy of this file from Thredd Support. Send the completed file to Thredd Support, who will raise the bulk chargeback on your behalf.

![](Resources/Images/Managing_Chargebacks_on_Smart_16.png)

Figure 15: Example of a Bulk Chargeback File

 For details of the fields in this file, see the table below.

| Option | Description |
| --- | --- |
| Token | The unique 9-digit token number for the card being charged back. |
| ChargebackAmount | The charged back amount. Up to two decimal places are allowed. If the Full Chargeback option is checked, this field is disabled, and the full amount taken during the Presentment transaction stage is displayed. |
| ChargebackCurrency | The three-digit ISO code for the chargeback currency. |
| ReasonCodeDescription | Reason code for the chargeback. For a full list of chargeback reasons, see [Chargeback Reason Codes](Appendix A.htm). |
| Username | Name of the user who created the chargeback. |
| Transactionid | The unique token for the transaction being charged back. |
| IsPartialChargeback | Whether this is a partial chargeback. Enter Y to indicate a partial chargeback amount. For a full chargeback enter N. |
| IsCreditToCardTransaction | Whether to credit the chargeback amount to the cardholderâs account. Y = Yes; N = No. |
| DocumentIndicator | Whether documentation to support this chargeback will be supplied: Y = yes; N = No. Refer to the Mastercard Guide for details of the types of Chargeback Reason Codes that require supporting documentation. |
| DE 72 | Description, to be displayed in the DE 72 field of the chargeback message sent to Mastercom. This field can also be populated with a standard message as in the Select text format field. |

### 4.3.12 Fee Collections

#### Managing Fee Collections

Mastercom supports the ability of issuers to send and receive fee collections related to disputes. For more information about fee collection messages and the fee collection cycle, refer to the Mastercard [Global Clearing Management System Reference Manual](https://w201.mastercardconnect.com/hsm3ca267/homememb/library/shared/ENG/TA/webhelp_omniture/index.html). (Note: you need a Mastercom account to access this link).

To create a fee collection:

1. In the **Transactions** window, right-click the required transaction and select **Create Mastercom fee collection message**.

   The **Mastercom Fee Collection** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_10.png)

   Figure 16: Mastercom Fee Collection Window

2. Provide all the details as per the instructions in the table below and click **Submit**.

   A confirmation message is displayed, indicating if the Fee collection request was successfully registered with Mastercom. In this case a **Fee ID** and **Claim ID** are returned, which you can use to track the status of the request. If the fee collection request failed, a message box is displayed, providing details of the error. For example, a request has already been submitted. Please resolve the error and try again or contact Thredd support.

3. To close the message box, click **OK**. The created fee collection message is displayed in the **Chargeback** Window:

   ![](Resources/Images/Managing_Chargebacks_on_Smart_11.png)

You can view details of any chargeback fees raised in the **Fee Collection** window. See [Viewing Fee Collections](#_Viewing_Chargeback_Fee).

| Option | Description |
| --- | --- |
| Fee Collection Type | Select the type of fee collection. Options include:   * 700 - Fee Collection * 780 - Fee Collection Return * 781 - Fee Collection Return Resubmission * 782 - Fee Collection Arbitration Return |
| Fee Collection Amount | Enter the fee collection amount. Up to two decimal places are allowed.  Tick one of the following options to indicate who to credit the fee to:   * Credit sender â fee will be credited to your account * Credit receiver â fee will be credited to the receiver. |
| Fee Collection Currency | Select the currency of the fee. |
| Fee Collection Reason | Select the reason for the fee collection (DE 25 Message Reason Code values that apply to the fee collection). For a list, see [Fee Collection Reason Codes](Appendix B.htm). |
| Message Text | Free text field to enable you to add a short message about the fee. |
| Fee Date | Select the date on which the fee collection is requested. |
| Country | Select the country where the fee collection applies. |

#### Viewing Fee Collections

This option enables you to view details of all Mastercom fee collection requests.

1. From the Smart Client menu, select **Card Activity** > **Fee Collection**.

   The **Fee Collection** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_12.png)

   Figure 17: Fee Collection Window

2. To filter the list of fee collection transactions, enter the transaction **Token** number, select the **Status** and/or select the **Date** range.
3. Click **List**.

### 4.3.13 SAFE Report

#### Creating a Mastercom SAFE Report

Mastercard require all card issuers to report fraudulent transactions, and you should always do this before raising a chargeback in instances where the reason code is related to a fraudulent transaction.

You can report fraudulent transactions to Mastercard by creating a new fraud event in Mastercom, using their SAFE reporting facility (now referred to as the Mastercard Fraud and Loss Database).

To create a SAFE report:

1. In the **Transactions** window, right-click the required transaction and select **Create Mastercom SAFE report**.The **Create Mastercom SAFE report** window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_13.png)

   Figure 18: Create Mastercom SAFE Report Window

2. Provide all the details as per the instructions in the table below and click **Save**. A confirmation message is displayed, indicating if the SAFE Report request was successfully registered with Mastercom. In this case a **Claim ID** and **Fraud ID** are returned, which you can use to track the status of the request. If the SAFE Report request failed, a message box is displayed, providing details of the error. For example, an invalid claim ID. Please resolve the error and try again or contact Thredd support.

3. To close the message box, click **OK**.

The created SAFE message is displayed in the SAFE Report Details Window. See [Viewing SAFE Report Details](#_Viewing_SAFE_Report).

| Option | Description |
| --- | --- |
| Token | Displays the unique token linked to the card PAN on which the transaction was made. |
| Date/Time | Displays the date-time stamp of the transaction. |
| Account device type | Select an option. |
| Card validation code | Select an option. |
| Amount | Displays the transaction amount. |
| Fraud Type Code | Select a fraud type option. |
| Sub Fraud Type Code | Select a sub-fraud type code. Options include:   * Convenience or Balance Transfer check transaction * PIN not used in transaction * PIN used in transaction * Unknown |
| Issuer ID | Displays the card issuer ID. |
| Charged Back | Tick this option if the transaction is Charged Back. |
| Account Closed | Tick this option if the account has been closed. |

#### Viewing SAFE Report Details

This option enables you to view details of all SAFE reports submitted to Mastercom.

1. From the Smart Client menu, select **Card Activity** > **Safe Report Details**.

   The **Safe Report Detail**s window is displayed.

   ![](Resources/Images/Managing_Chargebacks_on_Smart_15.png)

   Figure 19: Safe Report Details Window
2. To view only pending transactions, tick the **Pending Transactions** option. Alternatively, to filter the list of historical transactions, tick the **History Transactions** option and select the Date range.
3. Click **Search**.