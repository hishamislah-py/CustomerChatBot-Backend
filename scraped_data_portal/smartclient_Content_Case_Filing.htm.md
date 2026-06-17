# 11 Case Filing

As of 17 July 2020, Mastercard changed the Chargeback process to a rules-based system which is designed to make dispute resolution fairer and more responsive for all parties.

As a result of these changes, arbitration is no longer part of the Chargeback process. Instead, if a chargeback is rejected and the customer wants to dispute the case further, they can raise this as a case filing to Mastercard.

The fees associated with the case filing process are also different to that for chargebacks. For more information about the fee structure, contact Mastercard.

## 11.1 What is Case Filing?

Mastercard case filing is a feature through which an issuer or an acquirer can raise a concern with Mastercard.

To dispute a transaction after completion of the chargeback cycle, you can create either a pre-arbitration or arbitration case. Pre-arbitration case filing differs from arbitration case filing only in terms of the fees charged by Mastercard. For information about fees, contact Mastercard.

In terms of reporting, case filings and chargebacks are two different transaction types. No transaction is created at card level for the new arbitration / pre-arbitration case filings; thus, no data is sent to EHI.

Thredd do not currently support compliance case filings (pre-compliance and compliance). Thredd supports only pre-arbitration and arbitration case filings.

## 11.2 Creating a Case

If you want to dispute a transaction after completion of the chargeback cycle, you can create either a pre-arbitration or arbitration case. To raise a case with Mastercard, you can either use Smart Client or you can file arbitration cases directly with Mastercard using the Mastercom UI.

To access case filing functionality, you require the appropriate user permissions which you must request from Thredd. Contact your Account Manager for more information.

The following section explains how to use Smart Client to raise a case with Mastercard, and view cases.

### 11.2.1 Creating a Case in Smart Client

This section describes how to raise a case with Mastercard.

To create a Case in Smart Client:

1. From the Smart Client menu, select **Card Activity** > **View Transactions** to view the **Transactions** screen.
2. From the **View Transactions** screen, right click on the second presentment transaction.
3. Select **Actions** > **Create Case Filing**.

   ![Graphical user interface, application, table, Excel

   Description automatically generated](Resources/Images/Create_case_file_menu_938x469.png)

   Figure 74: Create Case Filing menu option
4. The **Create Case Filing** screen appears showing the second presentment details:

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Create_case_file_screen.png)

   Figure 75: Create Case Filing Screen
5. Choose whether to raise a **Pre Arbitration** or an **Arbitration** case.
6. To upload a file, select **Upload File**. The following screen appears where you can select the file you want to upload.

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Case_file_upload.png)

   Figure 76: Upload Files to Case Filing Screen
7. Click **Submit** to create the case.

### 11.2.2 Viewing Cases

To view cases using Smart Client:

1. Select **Card activity** > **Case Filing** to display the **Case Filing** screen.

   ![Graphical user interface, text, application, email

   Description automatically generated](Resources/Images/Case_file_view.png)

   Figure 77: Case Filing Screen

### 11.2.3 Updating a Case

To update a case:

1. Select **Card activity** > **Case Filing** to display the **Case Filing** screen.
2. Right click a file and choose **Update Case Filing**. The following screen appears:

   ![Graphical user interface, text, application, email

   Description automatically generated](Resources/Images/Updating_a_case.png)

   Figure 78: Update Case Filing Screen
3. Choose **Escalate**, **Withdraw**, **Rebut**, or **Doc\_Retry**.
4. Select **Submit**.

### 11.2.4 Viewing the Status of a Case

To retrieve the status of a case:

1. Select **Card activity** > **Case Filing** to display the **Case Filing** screen.

   Right click a file and choose **Retrieve Case File Status**. A screen appears showing the status of the case:

   ![Graphical user interface, application

   Description automatically generated](Resources/Images/Case_file_status.png)

   Figure 79: Retrieve Case Filing Screen

### 11.2.5 Downloading a Case Document

You can use the download functionality to check what documents you uploaded as part of the case.

To download a document associated with a case:

1. Select **Card activity** > **Case Filing to display the **Case Filing** screen**.
2. Right click a file and choose **Download Case Filing file**.

   ![Graphical user interface, text, application

   Description automatically generated](Resources/Images/Case_file_download.png)

   Figure 80: Download Case Filing File Screen
3. When prompted, confirm that you want to proceed with the download.

## 11.3 Crediting a Successful Case

This section explains how to credit a successful case to the cardholder.

Unlike chargebacks, upon a successful case filing there is no simple method to credit funds directly into the cardholderâs account. This is because there is no transaction record created at card level for arbitration / pre-arbitration case filings, and therefore no way to link arbitration information to the original transaction.

Instead, after identifying that a case filing is successful, you must credit the funds via a balance adjustment or load.

## 11.4 Viewing Case Filing Fees

This section explains how to see information relating to the fees associated with the case filing.

All fees related to arbitration / pre-arbitration case filing records from Mastercard are included in the Mastercard Fee section of the Transaction XML reports. For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.ai/Transaction_XML_Reporting_Guide.htm).

## 11.5 Example Case Filing Scenarios

The following scenarios show which party incurs a pre-arbitration fee in a pre-arbitration case involving claims with first chargebacks cleared on or after 17 July 2020.

| Billing Event Number | Billing Event Number | Service ID |
| --- | --- | --- |
| 2MS2601 | Pre-arbitrationâReceiver | MS |
| 2MS2602 | Pre-arbitrationâSender | MS |

#### Scenario 1

Acting as the sender, an issuer sends a pre-arbitration case to an acquirer. Acting as the receiver, the acquirer decides that the transaction is its responsibility. The acquirer accepts the case and financial responsibility for it. The disputed amount returns to the issuer. Mastercard assesses billing event 2MS2601; Mastercard does not assess billing event 2MS2602.

#### Scenario 2

Acting as the sender, an issuer sends a pre-arbitration case to an acquirer. Acting as the receiver, the acquirer decides that the transaction is not its responsibility. The acquirer rejects the case and does not assume financial responsibility for it. Mastercard assesses billing event 2MS2602; Mastercard does not assess billing event 2MS2601.

After the acquirer rejects the pre-arbitration case, the issuer, if permitted by the rules, may escalate the case to an arbitration case.

#### Scenario 3

Acting as the sender, an issuer sends a pre-arbitration case to an acquirer. Acting as the receiver, the acquirer does not respond in the required time period as chargeback rules specify. Mastercom automatically rejects the case. The acquirer does not assume financial responsibility for the case. Mastercard assesses billing event 2MS2602; Mastercard does not assess billing event 2MS2601.

After the acquirer does not respond in the required time period, the issuer, if permitted by chargeback rules, may escalate the case to an arbitration case.

#### Scenario 4

Acting as the sender, an issuer sends a pre-arbitration case to an acquirer. However, before the acquirer, acting as the receiver, acts on the case or before Mastercom automatically rejects the case, the issuer withdraws the case. The acquirer does not assume financial responsibility for the case. Mastercard assesses billing event 2MS2602; Mastercard does not assess billing event 2MS2601.