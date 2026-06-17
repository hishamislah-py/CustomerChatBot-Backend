# 9 Managing Chargebacks

You must use the Discover Xchange system to create and manage chargebacks.
(Please contact your Discover account manager for login credentials.)

For more information on the Xchange system, refer to the *Xchange User Guide*.

For more information on Diners Club International chargeback procedures and policies, see the *Discover Chargeback Guide*. Please read this guide for information on:

* Chargeback forms and chargeback policy
* Retrieval requests
* Interchange Chargeback Policies

## 9.1 Processing of Chargeback Records

Discover processes chargeback requests and sends Thredd a daily file containing chargeback records and fees.

Thredd process the file and generates chargeback transaction records, which you can view in the Transaction XML Reports. See [Transaction Reports](../Reporting/Transaction_reports.htm).

## 9.2 Viewing Chargebacks on Smart Client

You can use the Chargebacks and Chargeback History screens to view chargebacks that you have raised and track their progress.

![](../Resources/Images/Managing_Chargebacks_1.png "Chargebacks screen")

Figure 12:  Chargebacks screen

Thredd currently only support functionality to view Chargebacks. You will need to use the Discover XChange system to create chargebacks and manage the chargeback process.

For more information, see the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).

For an overview of chargebacks and how they work, see the [Payments Dispute Management Guide](https://docs.thredd.com/Chargeback_Guide.htm).

## 9.3 Discover Chargeback Procedures

Discover adopt similar chargeback procedures to other Card Scheme networks (such as Visa and Mastercard).
See the figure below.

![](../Resources/Images/Chargeback_stages.png "Chargeback stages")

Figure 13: Stages in the Discover Network's Payments Dispute Management Process

The information in this section is provided for reference only, and you should always refer to the Discover or Diners Club International documentation to confirm details.

### 9.3.1 Retrieval Request

You or your issuer can request a copy of the receipt and/or additional documentation related to a card charge. Issuers have up to 365 days from the transaction date to submit a *Retrieval Request*. The acquirer then has up to 30 days to respond with a *Retrieval Response*, containing the requested receipt and/or documentation.

### 9.3.2 Chargeback

A Chargeback is a transaction, processed by Discover, that reverses the entire amount or a portion of a card charge.

If you or the cardholder wishes to dispute the transaction, you can raise a Chargeback request. For example, due to an incomplete or lack of response to a Retrieval Request, or a cardholder submitting compelling evidence to support a Chargeback. You have 120 days from the charge date (or 30 days from the Retrieval Request date, if requested), to initiate a Chargeback.

The Chargeback initiation date may be 540 days for certain cases (e.g. if the service is for a future date).

### 9.3.3 Chargeback Stages (Cycle)

Updates to the chargeback transaction must be processed sequentially through:

| Cycle | Dispute Stage | Description and Notes |
| --- | --- | --- |
| A | Chargeback | Request for a partial or full charge back to the card. Raised by the issuer.  Please check the Discover documentation for timelines, amount restrictions, supporting documentation and requirements, which are specified per Chargeback reason code. |
| B | Representment | The acquirer responds to the chargeback request with supporting documentation if they wish to challenge the chargeback request (represent the merchant's right to the amount charged). |
| C1 | Arbitration: Pre-arbitration | The issuer can initiate the Arbitration process by submitting a Pre-Arbitration Notice update on the Transaction. This must be submitted within 30 calendar days of the last update in the chargeback submission cycle. Please check the Discover documentation for requirements and supporting documentation. |
| C2 | Arbitration: Dispute arbitration | The acquirer has 30 calendar days to respond, by submitting a Pre-Arbitration Response update. If the Acquirer accepts financial responsibility, the PreâArbitration Response generates the appropriate financial transaction.  If no response is received within 30 days, the Xchange System generates a financial message reversing the Representment update. This ends the process. |
| C3 | Arbitration of Financial Responsibility | The issuer can initiate Dispute Arbitration within ten (10) days of the deadline for response by the Acquirer to a Pre-Arbitration Inquiry. Either Participant may accept financial responsibility within fifteen (15) days of the Arbitration notice, known as the Arbitration acceptance period. |

Issuers will be charged a Chargeback fee for each Cycle A Chargeback initiated. Please check the Discover Chargeback documentation to confirm these details.

### 9.3.4 Chargeback Reasons

Chargeback reasons are organised into four categories:

* Authorization Related
* Processing Errors
* Fraud Related
* Cardholder Disputes

For more information, refer to the *Discover Chargeback Guide*.