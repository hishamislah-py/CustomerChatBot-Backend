# 7 Case Filing

As of 17 July 2020, Mastercard changed the Chargeback process to a rules-based system which is designed to make disputes fairer and more responsive for all parties.

As a result of these changes, arbitration is no longer part of the Chargeback process. Instead, if a chargeback is rejected and the customer wants to dispute the case further, they can raise this as a *case filing* to Mastercard.

The fees associated with the case filing process are also different to that for chargebacks. For more information about the fee structure, contact Mastercard.

## 7.1 What is Case Filing?

Mastercard case filing is a feature through which an issuer or an acquirer can raise a concern with Mastercard.

To dispute a transaction after completion of the chargeback cycle, you can create either a pre-arbitration or arbitration case. Pre-arbitration case filing differs from arbitration case filing only in terms of the fees charged by Mastercard. For information about fees, contact Mastercard.

In terms of reporting, case filings and chargebacks are two different transaction types. No transaction is created at card level for the new arbitration/pre-arbitration case filings, thus no data is sent to EHI.

Thredd do not currently support compliance case filings (pre-compliance and compliance). Thredd supports only pre-arbitration and arbitration case filings.

## 7.2 Creating a Case

If you want to dispute a transaction after completion of the chargeback cycle, you can create either a pre-arbitration or arbitration case.

To raise a case with Mastercard, you can either use Smart Client or you can file arbitration cases directly with Mastercard using the Mastercom UI.

To access case filing functionality, you require the appropriate user permissions which you must request from Thredd. Contact your Account Manager for more information.

The following section explains how to use Smart Client to raise a case with Mastercard, and view cases.

### 7.2.1 Creating a Case in Smart Client

From the **View Transactions** screen:

1. Right click on the second presentment transaction.
2. Select **Actions** > **Create Case Filing**.

   ![Graphical user interface, application, table, Excel

   Description automatically generated](Resources/Images/Case Filing.png)

   Figure 20: Create Case Filing menu option

   The **Create Case Filing** screen appears showing the second presentment details:

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Case_Filing_1.png)

   Figure 21: Create Case Filing Screen

3. Choose whether to raise a **Pre Arbitration** or an **Arbitration** case.
4. To upload a file, select **Upload File**. The following screen appears where you can select the file you want to upload.

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Case_Filing_2.png)

   Figure 22: Upload Files to Case Filing Screen
5. Click **Submit** to create the case.

### 7.2.2 Viewing Cases

To view cases using Smart Client:

1. Select **Card activity** > **Case Filing**. The **Case Filing** screen appears.

   ![Graphical user interface, text, application, email

   Description automatically generated](Resources/Images/Case_Filing_3.png)

   Figure 23: Case Filing Screen

### 7.2.3 Updating a Case

To update a case:

1. Select **Card activity** > **Case Filing**
2. Right click a file and choose **Update Case Filing**. The following screen appears:

   ![Graphical user interface, text, application, email

   Description automatically generated](Resources/Images/Case_Filing_4.png)

   Figure 24: Update Case Filing Screen
3. Choose whether to **Escalate**, **Withdraw**, **Rebut**, or **Doc\_Retry**.
4. Select **Submit**.

### 7.2.4 Viewing the Status of a Case

To retrieve the status of a case:

1. Select **Card activity** > **Case Filing**
2. Right click a file and choose **Retrieve Case File Status**.

   A screen appears showing the status of the case:

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Case_Filing_5.png)

   Figure 25: Retrieve Case Filing Screen

### 7.2.5 Downloading a Case Document

You can use the download functionality to check what documents you uploaded as part of the case.

To download a document associated with a case:

1. Select **Card activity**> **Case Filing**.
2. Right click a file and choose **Download Case Filing file**.
3. When prompted, confirm that you want to proceed with the download.

   ![Graphical user interface, text, application

   Description automatically generated](Resources/Images/Case_Filing_6.png)

   Figure 26: Download Case Filing File Screen

## 7.3 Crediting a Successful Case

This section explains how to credit a successful case to the cardholder.

Unlike chargebacks, upon a successful case filing there is no simple method to credit funds directly into the cardholderâs account. This is because there is no transaction record created at card level for arbitration/pre-arbitration case filings, and therefore no way to link arbitration information to the original transaction.

Instead, after identifying that a case filing is successful, you must credit the funds via a balance adjustment or load. For more information, see the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).

## 7.4 Viewing Case Filing Fees

This section explains how to see information relating to the fees associated with the case filing.

All fees related to arbitration / pre-arbitration case filing records from Mastercard are included in the Mastercard Fee section of the Transaction XML reports. For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.ai/Transaction_XML_Reporting_Guide.htm).