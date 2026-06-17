# 1 Introduction

The Card Transaction System (CTS) enables you to test the integration of your card processing systems and validate the setup of your [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface (EHI) is a Thredd system that enables Thredd customers to receive and respond to real-time transaction data as well as financial messages.](#) before you go live in a production environment. A simple dashboard provides built-in standard test cases and a transaction history screen.

The service is written as an API service which enables you to submit card test transactions in the Thredd [UAT![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) User Acceptance Testing](#) environment in line with your programme setup. All input parameters are strings or numerics, making integration and testing simple and fast.

Using CTS, you can:

* Run standard built-in tests to simulate typical POS, ATM, mail-order/telephone-order (MOTO), AFD and e-commerce transactions
* Test authorisation messages for [Chip & PIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card transaction where the POS terminal reads and validates the cardâs chip.](#), [Contactless![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure payment method using a debit or credit card or another payment device by using RFID technology and near-field communication. To use the system, a cardholder taps the payment card near a POS terminal equipped with the technology.](#), [Magstripe![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The magnetic stripe on the back of the card. Can be used for a card point of sale (POS) transaction using a merchant POS terminal.](#), [ATM![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Automated Teller (Cash) Machine.](#) cash withdrawal, e-commerce, [MOTO![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Mail and Telephone Order (MOTO) transaction, which is a payment made over the telephone (e.g., via a Call centre) or via a mail order catalogue.](#), and [Scheme Stand-in Processing (STIP)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) User Acceptance Testing](#)
* Simulate clearing for all successful authorisations created on CTS, including clearing of partial refunds. The Clearing screen displays a list of all eligible transactions that can be cleared to simulate the presentment/financial record
* Execute refunds (full or partial) for all cleared transactions
* Test recurrence by specifying if a transaction is recurring (for e-commerce or MOTO)
* Execute reversals for successful authorisations that have not been cleared
* Simulate foreign exchange (FX) transactions by specifying the country where the transaction occurs to simulate cross-border transactions
* View a history of all CTS transactions which you can filter and refine
* Simulate a scheme STIP message for POS and e-commerce transactions

## 1.1 How does CTS work?

The figure below illustrates how you can simulate and test the payment authorisation flow using CTS.

![](../Resources/Images/CTS_overview.png)

Figure 1: Testing authorisations using the Card Transaction System