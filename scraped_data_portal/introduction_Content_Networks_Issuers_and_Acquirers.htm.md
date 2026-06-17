# 1.3 Issuers and Acquirers

Issuers and acquirers are two of the key participants in the card payment network. Traditionally, both were large and established financial organisations, such as banks. Issuers are also known as BIN sponsors.

## 1.3.1 Issuers

Issuers are authorised to issue cards to their customers. The cards are branded with the schemeâs logo and can be used across the schemeâs network. Traditionally, the card issuer would also provide the customer with the bank account linked to the card, hold the customerâs money and update the bank account balance whenever the card was used for a payment transaction. Challenger banks and [Fintechs![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Innovative Financial Technology Companies.](#) have disrupted the traditional model by offering card issuing services without the need for customers to open a traditional bank account.

## 1.3.2 Acquirers

Acquirers derive their name from their role in acquiring merchants. Merchants are the business customers of a bank â the shops, stores, retailers and providers of services who want to offer payment facilities to their own customers (i.e., a means to take payments). The Acquirer provides the merchant with a Merchant Account for trading using the card payments network. Separate merchant accounts are provided for card present (in store) and e-commerce trading.

## 1.3.3 Interaction between Issuers and Acquirers

Acquirers enable merchants to take card payments and send payment authorisation requests to the issuer using the card schemeâs network. Issuers issue cards with the schemesâ logo and authorise (approve or decline) payments made using their issued cards. Every working day, money is exchanged between issuers and acquirers, to reflect transactions that have happened on the network during that day.

![](../Resources/Images/Intro_card_payments/Acquirer_isssuer.png)

Figure 4:  Issuers and Acquirers operating on the schemeâs network

## 1.3.4 Program Managers

What's the difference between an issuer and a program manager?

Thredd refers to a company who implements a card programme as a program manager. The majority of Thredd customers are card program managers. Unless they are self-issuers who are licenced by the scheme, program managers must use the services of an existing issuer.

### Licencing and Issuing

The issuer operates like a bank and is licenced to issue and maintain card accounts and hold client money.

The issuer has the contractual relationship with the scheme. Upon request, the scheme assigns a number of [BINs![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first four or six numbers on a payment card, which identifies the institution that issues the card.](#) (bank identification numbers) to the issuer. The issuer can allocate a BIN or sub-BIN range to their program manager customers. Using the assigned BIN or sub-BIN range, the program manager can set up a card programme, create cards, each with a unique [Primary Account Number (PAN)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card identifier found on payment cards, such as credit cards and debit cards, as well as stored-value cards, gift cards and other similar cards. The cardâs 16-digit PAN is typically embossed on a physical card.](#), and activate the cards for use on the schemeâs network. The program manager creates and manages the cards in their programme.

An issuer-processor such as Thredd can be used to create and manage card records and process transactions. Alternatively, the program manager can either build their own infrastructure to do this or use a combination of Thredd and their own systems.

There are two main scenarios for how program managers work with their issuer[1  There are other ways of working with issuers. Please speak to your Business development manager.](#):

* E-Money licence. (Common)
* The program manager has their own E-Money licence and uses their issuer only for BIN sponsorship. (Common as the program manager grows)

### Holding of Cardholder Funds

On a daily basis, the issuer receives and manages any cardholder funds that have transferred to the issuerâs bank accounts. Where Thredd performs payment authorisation services on the card, then the Thredd platform will need to be updated with the latest available card balance held by the issuer, and this can be done in one of two ways:

* Some issuers may load the card balance directly onto the Thredd system using the Thredd API (where Thredd is maintaining the card balance for the program manager).
* Alternatively, the program manager will need to load the card balance to Thredd[2  The issuer may ask the program manager to provide prefunding for their cards â normally this covers seven days of transaction volume, but this will differ per issuer.](#) .

Issuers receive daily card scheme settlement files containing details of all authorised and cleared card transactions. They will transfer or make funds available to the card scheme to reflect financial transactions on the card; the scheme will then settle directly to the acquirer.

There are additional regulatory requirements in most regions for issuers who hold client money.

### Reporting and Billing

Issuers have additional reporting requirements and need to prepare daily, weekly and quarterly reports on active cards and transaction activity, which are sent to the card schemes and regulators to help monitor card usage and reduce incidents of fraud.

Scheme billing is done per identifier (Mastercard or Visa).

The schemes use the issuerâs reports on card activity to bill the issuer. If there is a significant discrepancy between the issuerâs reporting and the schemeâs system of record for that programme, then the scheme will query this discrepancy and can impose penalties.

Since the schemes bill at identifier level and do not bill at BIN level, issuers who have multiple program managers operating under the same identifier will normally divide charges across all program managers using that identifier, rather than at a BIN level. Check with your issuer for details.

### Program Manager and Scheme Relationship

The program manager typically has no direct relationship with the scheme[3  Some program managers with direct contacts with the scheme may be asked to work under another principal member until they are large enough to become a scheme member.](#). All requests and access to scheme systems must be arranged via their issuer. Some issuers provide their program managers with access to scheme systems, such as those used for payments dispute management (e.g., [Visa Resolution Online![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) System from Visa for raising disputes and sharing messages during the dispute management process.](#) and [Mastercom![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) System from Mastercard for raising disputes and sharing messages during the dispute management process.](#)). Thredd can also provide access to some scheme systems, via integrated API.

The Thredd platform enables program managers to integrate with the card payments network without the need to develop their own systems and infrastructure or arrange separate contractual agreements. Thredd manages the payment transaction messages received from the card schemes.

![](../Resources/Images/Intro_card_payments/Acquirer_processor_PM.png)

Figure 5:  Connecting Program Managers to the Scheme Network

## 1.3.5 Payment Services Provider or Payment Gateway

What's a payment services provider (PSP)/ Payment Gateway?

A payment service provider (also known as a Payment Gateway) offers merchants access to payment platforms and other payment processing services, which enables the merchant to take cardholder payments online or via a card reader terminal without needing to build their own payment infrastructure and payment systems. The payment gateway manages the communication of payment transactions between acquirers and merchants.

![](../Resources/Images/Intro_card_payments/Merchant_psp_acquirer.png)

Figure 6:  The Role of the PSP (Payment Gateway)

As a Thredd program manager, if you want to offer your customers a means to make card payments into their account, you may need to use a payment service provider/payment gateway.

### More Information

Find out more about the schemes and network participants such as issuers and acquirers using the links below.

* [Thredd Key Concepts Guide â Understanding Payments](https://docs.thredd.ai/keyconcepts/Content/Key_Concepts/Understanding_Payments.htm)