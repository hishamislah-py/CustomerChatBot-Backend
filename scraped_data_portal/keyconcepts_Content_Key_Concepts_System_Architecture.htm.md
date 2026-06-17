# 3 Thredd Platform

This section describes the Thredd Platform key components, as well as interfaces to partner services.

Click the image to expand.

[![](../Resources/Images/Thredd_Platform.png "Thredd Platform - services and connections")](../Resources/Images/Thredd_Platform.png)

Figure 8: Thredd Platform

The above figure shows the core components of the Thredd Platform, together with interfaces to third-party service providers and partner systems. Below are details of the Thredd platform components and services available to customers.

## 3.1 Card Issuing and Management

### Web Services and Cards API

You can use the Thredd Web services (SOAP) or Cards API (REST) to create and manage the accounts and cards in your program. Below are examples of functionality that can be managed using the API:

* Creating cards
* Linking cards to usage groups
* Card load and unload
* Card expiry and replacement
* Pin management
* Card activation
* Lost and stolen status
* Balance enquires and balance adjustments
* Card fees
* 3D Secure enrolment

#### Creating Cards

When you send a request to Thredd to create a card, the Thredd Platform allocates an available card PAN to the card. It generates a unique internal Public Token, which is linked to the card. The public token is returned in the Thredd response and your systems can use this token for all subsequent queries and card management activities on the Thredd system. This enables you to handle card requests without needing to process or store the full PAN (full PAN requires [PCI DSS compliance![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Threddâs Secure Connectivity Framework is the combination of several components which enable secure access to Threddâs resources, using a common identity store.](#)).

For more information on using SOAP Web Services, see the [Web Services Guide](https://docs.thredd.ai/webservices/Default.htm). For more information on using REST-based Cards API, see the [Cards API Website](https://cardsapidocs.thredd.com/).

#### Managing Cards

You can use the Thredd API to manage your cards. You can integrate the API into your customer application, to provide your customers with self-service options to manage their account. This includes services such as card blocking and unblocking, card expiry and upgrades, card replacement, switching from a virtual to a physical card, cards loads and balance transfers, PIN changes and queries.

For more information on using SOAP Web Services, see the [Web Services Guide](https://docs.thredd.ai/webservices/Default.htm). For more information on using REST-based Cards API, see the [Cards API Website](https://cardsapidocs.thredd.com/).

### Cardholder Fee Setup and Management

The Thredd Fees module is an optional service that enables you to apply fees to the cards in your program. Fees are managed via Fee Groups. Separate fee groups are available for:

* Authorisation fees
* Recurring fees
* Web Service usage fees

You can link a card to a Fee Group and also apply ad-hoc or one-off fees.

For more information, see the [Fees Guide](https://docs.thredd.ai/Fees_Guide.htm).

## 3.2 Payment Processing

### Message Processor

The Thredd core Message Processor module performs a number of key roles:

* Receives and processes authorisation and financial messages from the schemes. Authorisation messages are received and processed in real-time.
* Runs internal transaction screening and validation checks on authorisation messages; processes messages according to the unique business logic configured for each Thredd card program (e.g., per Issuer, program, product and card usage settings).
* Where Thredd holds the card balance and provides the authorisation decision, then the system checks the internal card balance ledger to determine if sufficient funds are available and updates the balance ledger. The system can apply card fees at the same time (if you are using the Thredd Fees module).
* Initiates other related services, such as authentication and transaction reporting.

### External Host Interface (EHI)

The External Host Interface (EHI) is an API interface[1  EHI messages can be provided in either JSON or XML format.](#) which sends messages to the endpoint configured by the Program Manager. The Program Managerâs systems pick up these messages and can respond and process, based on their EHI setup.

EHI plays an important role in processing real-time authorisation and financial messages. There are flexible transaction processing setup options (see [Transaction Processing and EHI Setup](Our_Role.htm#_Transaction_Processing_and)). The EHI mode determines who is responsible for payment authorisation and who maintains the card balance ledger.

For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm).

### Card Transaction System (CTS)

The Card Transaction System (CTS) can be used to put through simulation transactions in the UAT environment. The simulation transactions generate EHI messages and can be used to test your end-to-end EHI integration and message handling.

For more information, see the [Card Tranaction System (CTS) Guide](https://docs.thredd.ai/Card_Transaction_System_Guide.htm).

### XML Reporting

The Thredd Platform provides a number of XML reports to Program Managers and Issuers, which can be used to support transaction matching and reconciliation:

* **Transaction XML Report** â daily report that provides all transaction records processed that day (both authorisation and financial messages). The Program Manager can use this report to check the transactions reported and reconcile against details in their own card database/ received from EHI. See the [Transaction XML Reporting Guide](https://docs.thredd.ai/transactionxml/Default.htm).
* **Balance XML Report** â daily report that provides the balance on all cards in the Program Managerâs program. The Program Manager can use this report to check the balance and update or reconcile against details in their own card database. See the [Balance XML Reporting Guide](https://docs.thredd.ai/balancexml/Default.htm).

Thredd provides additional reports to issuers and self-issuers:

* **Fee Collection Report** â gives a summary of Scheme (VISA/Mastercard) Fees by ICA and currency.
* **Quarterly Management Report (QMR)** â contains information needed to complete your regulatory Quarterly Management Report for Mastercard.   
  The Visa equivalent Quarterly Operating Certificate (QOC) can be provided on request.

Charges for additional reports may apply. Check with your Thredd account manager for details.

## 3.3 Account Management

### Thredd Portal

Thredd Portal is our new web application for managing your account on the Thredd platform. Using the Thredd Portal, you can configure and control your payment programmes in real-time. Thredd Portal provides a feature-rich dashboard that allows you to view and manage the full lifecycle of your customersâ transactions and card usage.

For more information, see the [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal/Default.htm).

### Smart Client (legacy)

Smart Client is our legacy desktop application that can be installed on a personal computer (PC). It provides a front-end administrative tool for viewing and managing transactions on the cards in your program. Users can perform actions such as transaction and card queries, card loads and unloads, balance enquiries and adjustments, and view and manage chargebacks. Chargeback reporting and SAFE reporting is available (Mastercard only).

For more information, see the [Smart Client Guide](https://docs.thredd.ai/smartclient/Default.htm).

### 3.3.1 Customer Experience Enablers

### Mobile Payments and Tokenisation

Tokenisation is a security technology which replaces the sensitive 16-digit permanent account number (PAN) that is typically embossed on a physical card with a unique payment token (a digital PAN or DPAN) that can be used in payments and prevents the need to expose or store actual card details. The DPAN is used to make purchases in the same way as a normal Financial PAN (FPAN).

Tokenisation enables cardholders to access mobile wallet functionality â provided by companies such as Apple and Google â which allows payments to be made in store from a smart device such as a smartphone or tokenised device. Tokenisation also helps merchants to improve the security of online payment transactions by replacing the sensitive PAN card details with a token and storing this instead. The token can then be used for repeat or recurring payments.

For more information, see the [Tokenisation Service Guide](https://docs.thredd.ai/Tokenisation_Guide.htm).

### Mobile Text Messaging

The Thredd mobile text messaging (SMS) service enables you to communicate better with your customers and enhance the customer experience by enabling you to send messages to customersâ SMS-enabled devices. For more information, see the [Mobile Text Messaging (SMS) Guide](https://docs.thredd.aiSMS_Guide.htm).

### Interactive Voice Reponse

The Thredd Interactive Voice Response (IVR) service enables customers to call a phone number to perform various actions for their card.For more information, see the [Interactive Voice Response (IVR) Guide](https://docs.thredd.aiIVR_Guide.htm).

### 3.3.2 Risk Management and Fraud

### Fraud Transaction Monitoring

Fraud Transaction Monitoring (powered by Featurespace) is a fraud solution that minimises online and offline card risk and offers real-time detection of card fraud.

Fraud Transaction Monitoring adapts to new fraud types and identifies unknown threats by detecting unexpected changes (anomalies) in real-time data.

For more information, see the [Fraud Transaction Monitoring Guides](https://docs.thredd.ai/Fraud_Transaction_Monitoring.htm).

### 3D Secure (Cardholder Authentication)

3D Secure is a protocol/program supported by the major card schemes, which provides Cardholder [authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.](#) during an online transaction.

Thredd provides full 3D Secure support using one of our 3D Secure providers: Apata or Cardinal Commerce. Program Managers are set up with an account and access to a 3D secure Portal for configuring their 3D Secure authentication rules.

For more information, see the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) or [[3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm)](https://docs.thredd.ai/3D_Secure_RDX.htm).

### Chargeback Management

Chargebacks are supported via the relevant card scheme (e.g., MasterCard or Visa); both schemes provide online systems where issuers and acquirers can view and respond to chargeback notifications.

Smart Client provides a facility to enable Program Managers to raise and manage chargebacks (Note that this is only available for Mastercard issuers in Europe/UK at present).

For more information, see the [Payments Dispute Management Guide](https://docs.thredd.ai/Chargeback_Guide.htm).

### Fraud Reporting

The ThreddSAFE Reporting facility on Smart Client enables Program Managers to report suspected fraudulent transactions to Mastercard.

For more information, see the [Fraud Reporting Guide (Mastercard)](https://docs.thredd.ai/Fraud_Reporting_Guide.htm).

## 3.4 Partnership Networks

Thredd's partners span many parts of the industry:

* Global payment acceptance through Visa, Mastercard and Discover
* 95+ Issuing Banks and BIN Sponsors integrated Certified by Visa and Mastercard to process transactions globally.
* Global and local network of card manufacturers
* Ecosystem partners: Featurespace, Apata, Cardinal, MeaWallet and Kani
* Digital Wallet (Tokenisation) and partners: Mastercard Digital Enablement Service (MDES), Visa Digital Enablement Programme (VDEP)

### Card Manufacturers

Thredd has existing partner relationships with over 40 card manufacturers worldwide. We provide a pre-integrated service and interface to these card manufacturers.

The Thredd API are used to raise card creation requests. Thredd sends card files to the card manufacturer, which contain the instructions for generating the cards in your program.

You will need to sign a separate agreement with your card manufacturer. Please contact your Business Development Manager or Implementation Manager for advice on suitable card manufacturers for your region/service.

For details of using the Thredd API to create card instructions, see the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API) or [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm) (SOAP API).