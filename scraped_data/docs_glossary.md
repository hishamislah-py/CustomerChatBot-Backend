# Glossary

### 3D Secure

3D Secure (3-domain structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as ‘Verified by Visa’ and ‘Mastercard SecureCode’ respectively. Thredd supports Cardinal and Apata as Access Control Servers (ACS).

For more information, see either the [3D Secure - Apata](https://docs.thredd.com/3D_Secure_Apata.htm) guide, or the  [3D Secure - Cardinal](https://docs.thredd.com/3D_Secure_RDX.htm) guide.

### API Explorer

Enables you to explore our available endpoints for the API. The API Explorer contains information on each of the endpoints, such as the verb, endpoint URL and any fields (and their details) applicable to the endpoint.

### Apata 3D Secure

Apata is an Access Control Server (ACS) provider that enables support for the 3D Secure cardholder authentication scheme.

For more information, see [3D Secure - Apata](https://docs.thredd.com/3D_Secure_Apata.htm).

### Auth Calendar Group

Controls the dates and times when authorisations on a card are allowed. You can use this option to control when the card can be used, for example, to prevent usage on weekends or out of hours.

### Authentication

Authentication can refer to the following:

* 3D Secure Authentication message sent from the Merchant to the 3-D Secure service provider to obtain cardholder authentication before submitting an Authorisation message via the Acquirer to Visa/Mastercard.
* Card authentication checks that may be carried out at Visa/Mastercard, Thredd (and occasionally the Program Manager on receipt of EHI message) to validate that the card is genuine.
* Cardholder authentication checks that may be carried out at Visa/Mastercard, Thredd (and occasionally the customer on receipt of EHI message) to validate that the cardholder is genuine.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Cardholder

Consumer or account holder who is provided with a card to enable them to make purchases.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Card Linkage Group

The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.

### Card Manufacturer

Thredd has relationships with existing card manufacturers, who we can instruct to print your cards. We use Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder. Any white label test cards are typically sent to Thredd, the Program Manager and the Card Schemes.

For Thredd card interface specifications to be used by manufacturers, see the [Card Generation Interface Specification](https://docs.thredd.com/Card_Generation_Interface_Specification.htm#Card%20Generation%20Interface%20Specification).

### Card Scheme (Network)

Card network, such as MasterCard, Visa and Discover, as well as smaller networks that use the Mastercard Network Exchange (MNE), such as STAR and Pulse. These are responsible for managing transactions over the network and for arbitration of any disputes.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Card Status Codes

A two-digit code that specifies the current status of the card.

For information, see [Card Status Codes](https://cardsapidocs.thredd.com/docs/card-status-codes).

### Card Verification Value/Code 1 (CVV1 or CVC1)

This is a 3-digit number which is located on the card’s magnetic stripe tracks 1 and 2. It is used to help prevent fake magnetic stripe transactions, but is vulnerable to copying if someone can see the original magnetic stripe data. See also Card Verification Value/Code 2 (CVC2 or CVV2).

For more information, see [Managing Risk](https://docs.thredd.com/More_Information/Managing_Risk.htm).

### Card Verification Value/Code 2 (CVV2 or CVC2)

This is a 3-digit number which is located on the card’s magnetic stripe tracks 1 and 2. It is used to help prevent fake magnetic stripe transactions, but is vulnerable to copying if someone can see the original magnetic stripe data.

For more information, see [Managing Risk](https://docs.thredd.com/More_Information/Managing_Risk.htm).

### Card Verification Value/Code 3 (CVC3 / dCVV)

Card Verification Code 3 (Mastercard) / dynamic Card Verification Value (Visa) are dynamic values which are used to secure Contactless Magnetic Stripe Transactions. They are similar to a small EMV Application Cryptogram, which is placed in the discretionary part of the Track Data fields sent to Visa/Mastercard.

For more information, see [Managing Risk](https://docs.thredd.com/More_Information/Managing_Risk.htm).

### Cardinal 3D Secure

Cardinal Commerce provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme.

For more information on the Thredd 3D Secure service via Cardinal, see the [3D Secure Guide - RDX Biometric Guide](https://docs.thredd.com/3D_Secure_RDX.htm).

### Chargeback

Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer (BIN sponsor) . The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.

For more information, see the [Payments Dispute Management Guide](https://docs.thredd.com/Chargeback_Guide.htm).

### DPAN

Device PAN. The PAN value set up on the cardholder’s device. This is not visible to the cardholder, but is the PAN used for the transactions as far as the merchant is concerned.

For more information, see the [Tokenisation Service Guide](https://docs.thredd.com/Tokenisation_Guide.htm).

### EHI Operating Mode

For authorisation types of transactions, the External Host Interface (EHI) can operate in one of five modes:

* Gateway Processing (Mode 1) - the External Host maintains card balances and participates in transaction authorisation by approving or declining the transaction.
* Cooperative Processing (Mode 2) - Thredd maintains balances and performs all types of the authorisation, but the External Host can overrule in some circumstances.
* Full Service Processing (Mode 3) - read-only data feed from the Thredd system to the Client's system.
* Gateway Processing with STIP (Mode 4) - External Host maintains Balance (with Thredd stand-in).
* Gateway Processing with STIP (Mode 5) – Same as Gateway Processing with STIP (Mode 4), but clearing transactions do not update the Thredd stand-in balance.

For more information, see the [External Host Interface Guide](https://docs.thredd.com/EHI_Guide.htm).

### External Host Interface (EHI)

The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.

For more information, see the [External Host Interface Guide](https://docs.thredd.com/EHI_Guide.htm).

### Fee Groups

Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.

For more information, see the [Fees Guide](https://docs.thredd.com/Fees_Guide.htm).

### Fee Types

A card usage fee type that defines the fees that are applied to a specific type of transaction, such as a debit card payment or an ATM withdrawal. A Fee Group will consist of one or more fee types.

For more information, see the [Fees Guide](https://docs.thredd.com/Fees_Guide.htm).

### Fulfilment Address

The address which a physical card is sent to.

### JavaScript Object Notation (JSON)

A lightweight format for storing and transporting data used in the REST API.

### Limit Group

Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Master Virtual Cards (MVC)

A Thredd virtual card that is restricted to loading and unloading to a physical or virtual card and cannot be used for e-commerce or in-store transactions. An MVC is used to reflect the value of the ‘actual’ money in the Issuer's bank account. An MVC guarantees that the load is limited to the amount prefunded (i.e., loaded onto MVC) and gives the Program Manager the ability to distribute funds immediately rather than having to wait for notification of each individual load into the Issuer Bank account.

For more information, see the [Master Virtual Cards Guide](https://docs.thredd.com/MVC_Guide.htm).

### MCC Group

Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes to define the trading category of the merchant. The MDES platform is used in iPhone 6, iPhone 6 Plus and Apple Watch to enable secure payments to take place for contactless and in-app payments. You can configure your cards to allow/disallow payments based on the merchant's MCC.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Merchant

The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Merchant Category Code (MCC)

Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. MCCs are used by credit card issuers to identify the type of business in which a merchant is engaged.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### One Time Passcode (OTP)

One Time Passcode/ Activation code which is sent to the cardholder for use in authenticating during token provisioning, during the setup of Google Pay, Apple Pay or other wallet on their device.

For more information, see the [Tokenisation Service Guide](https://docs.thredd.com/Tokenisation_Guide.htm).

### Point of Sale (POS) transaction

A card payment made at a retail stores using a POS terminal device. The device has embedded software that is used to read the card’s magnetic strip data.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Postman

An application that can be used to test and explore our API.

### Postman Collection

A file that enables users to import our full API into the Postman application. There are collections available for each of the different versions that we support. See the API Explorer section for the latest version of the Postman Collection.

### Primary Account Number (PAN)

The Primary Account Number (PAN) is the card identifier found on payment cards, such as credit cards and debit cards, as well as stored-value cards, gift cards and other similar cards. The card’s 16-digit PAN is typically embossed on a physical card.

For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### Product Setup Form (PSF)

The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.

For more information, see the [Getting Started Guide](https://docs.thredd.com/Using_the_Doc_Portal.htm).

### Public Token

The Thredd 9-digit token is a unique reference for the PAN. This is used between Thredd and clients to remove the need for Thredd clients to hold actual PANs.

For more information, see [Thredd Public Token](https://docs.thredd.com/More_Information/Cards.htm).

### sFTP

Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection. SFTP is used for sending XML reports to customers. For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.com/Transaction_XML_Reporting_Guide.htm) and [Balance XML Reporting Guide](https://docs.thredd.com/Balance_XML_Reporting_Guide.htm).

### Simple Object Access Protocol (SOAP)

SOAP (Simple Object Access Protocol) is a messaging protocol for exchanging structured information in the implementation of web services. It uses Extensible Markup Language (XML) for its message format and relies on application layer protocols such as HTTP for message negotiation and transmission. SOAP allows developers to invoke processes running on disparate operating systems (such as Windows, macOS, and Linux) to authenticate, authorise, and communicate using XML.

### Smart Client

Smart Client is Thredd's user interface for managing your account on the Thredd platform. Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.

For more information, see the [Smart Client Guide](https://docs.thredd.com/Smart_Client_Guide.htm).

### Status Codes

For more information on status codes returned via EHI, see the [External Host Interface Guide](https://docs.thredd.com/EHI_Guide.htm).

### Thredd Fraud Transaction Monitoring

Thredd Fraud Transaction Monitoring uses behavioural analytics to detect and prevent fraud with machine learning software that monitors individuals' behaviour and detects anomalies to identify risk and prevent fraud attacks in real-time. Check with your Thredd account manager for details.

For more information, see the [Fraud Transaction Monitoring Guides](https://docs.thredd.com/Fraud_Transaction_Monitoring.htm).

### Tokenisation (Digital Wallets)

Tokenisation (Digital Wallets) is a security technology which replaces the sensitive 16-digit permanent account number (PAN) that is typically embossed on a physical card with a unique payment token (a digital PAN or DPAN) that can be used in payments and prevents the need to expose or store actual card details.

For more information, see [Tokenisation](https://docs.thredd.com/More_Information/Tokenisation.htm).

### Usage Group

Group that controls where a card can be used. For example: POS or ATM.

### Virtual Card

Thredd offers a virtual card service, which cardholders use online, without needing a physical card.

For more information, see the [Virtual Cards Guide](https://docs.thredd.com/Virtual_Cards_Guide.htm).