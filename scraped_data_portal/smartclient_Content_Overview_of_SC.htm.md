# 1 Overview of Smart Client

This topic introduces Smart Client, describes its key features and components, and explains how you can use it to manage your card programmes.

Smart Client is the user interface for managing your account on the Thredd Platform. Using the Smart Client portal, you can configure and control your payment programmes in real-time. Smart Client provides a feature-rich dashboard that allows you to view and manage the full lifecycle of your customersâ transactions and card usage.

Using Smart Client, you can:

* Display details about card activity, transaction type, and customer interaction
* Drill down into the details of a specific transaction, for example, to view the:

  + Precise Point-of-Sale where a transaction took place.
  + Chip settings at the time of transaction
  + Data stored on the chip of an individual card.
  + Cardholder verification results
  + Terminal capability

* Allow Customer Service Agents to amend details and take appropriate actions, including:

  + Restoring blocked PINs and sending in-app notifications direct to customers
  + Providing customers with a clear explanation of transaction status
  + Viewing a real-time dashboard on limits and usage
  + Accessing an instant easy-to-understand breakdown of card usage to share with customers.

* Manage the entire chargeback lifecycle, including initiating a request and producing chargeback reports.
* Use the Case Filing process for dispute management to raise pre-arbitration or arbitration requests to Mastercard.
* View information about MDES- and VDEP-enabled cards
* Retrieve cards that have been archived.

## 1.1 About the Card Payment Process

To understand what information Smart Client shows and how you can use it to manage your customersâ transactions and how a card can be used, you need to know about the card payment process. This topic describes the main concepts, components, and processes.

The following diagram shows the key components in the payment flow:

![Diagram shows that cardholder purchase from merchant, and authorisation request goes to Acquirer, Card Scheme, Thredd, then Program Manager, and response goes back.](Resources/Images/EHI-transaction-flow-overview_984x158.png)

Figure 1: Parties involved in the payment process.

When a cardholder uses a card to make a purchase, the authorisation request is sent from the merchant terminal to the merchant acquirer, and then to the relevant card scheme (payment network). The authorisation request is passed to Thredd for authorisation where it is processed according to the card usage rules determined by the Program Manager (card issuer). The payment process is explained in more detail below.

### 1.1.1 Cards

Cards can be either physical or virtual. Physical cards are printed by a manufacturer and sent to the cardholder. Virtual cards are linked to a card image which is displayed to the cardholder. Thredd supports the following types of cards:

* Prepaid cards and gift cards â the card is loaded with a prepaid amount available for the cardholder to spend. The card is not permitted to go into a negative balance, and you can provide a facility to enable cardholders to load additional funds to the card if required.
* Multi-currency (FX) cards â the card is linked to a multi-currency wallet and enables the cardholder to pay in any desired currency.
* Credit cards â on the Thredd platform, there is no distinction between a prepaid and a credit card. If you offer cardholders a credit facility, you will need to have a separate arrangement with them relating to overdraft charges and loading the card with an available funds limit in accordance with the overdraft facility. The Thredd card must hold a sufficient balance to enable a card payment.

Thredd provides web services (APIs) to create cards.

### 1.1.2 Card Usage Groups

Card usage groups are used to control what the cardholder can do with the card, as well as the various card usage fees that are charged to the cardholder.

### 1.1.3 Tokens

Tokens enable you to use the Thredd platform without needing to store or supply the full 16-digit card primary account number (PAN). Smart Client tokenises card numbers so that sensitive information is not shown. Thredd generates two types of tokens:

* 9-digit unique random token, linked to the PAN.
* 16-digit, formed from the 3-digit identifier, plus the 9-digit token, plus the last 4 digits of the PAN.

Both Mastercard and Visa offer a tokenisation service to card issuers. Mastercard offer the Digital Enablement Service (MDES), and Visa the Visa Token Service (VTS) which Thredd refers to as the Visa Digital Enablement Program (VDEP). Thredd supports both tokenisation services.

### 1.1.4 Acquirer

This is the merchant acquirer or bank that offers the merchant a trading account, to enable them to take payments in store or online from cardholders. For example, Worldpay.

### 1.1.5 Card Scheme

This is the card network , such as MasterCard or Visa,that is responsible for managing transactions over the network and for arbitration of any disputes.

### 1.1.6 Thredd Platform

The Thredd Platform is a robust, scalable issuer processing platform that is certified by Mastercard and VisaMastercard, Visa, and Discover Global Networks. The Thredd Platform supports Chip and PIN (EMV), magstripe, virtual and contactless card processing across prepaid, debit and credit rails. Smart Client is the user interface for the Thredd platform.

### 1.1.7 External Host Interface (EHI)

The External Host Interface (EHI) offers a way to exchange transactional data between the Thredd processing system and the Program Managerâs externally hosted systems. All transaction data processed by Thredd is transferred to the external host system via EHI in real time.

### 1.1.8 Card Transactions

The main transactions that take place on a card are:

* Authorisations. These transactions occur at the stage where a merchant requests approval for a card payment by sending a request to the card issuer to check the card is valid, and the requested authorisation amount is available on the card. Funds are not deducted from the card at this stage.
* Presentments. This is the stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). Also referred to as the *First presentment*.

### 1.1.9 Program Manager (Issuer)

A Thredd customer who manages a card programme. The Program Manager can create branded cards, load funds, and provide other card or banking services to their end customers. Each Program Manager is assigned their own unique issuer code on the system.

The card issuer is typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme (payment network).