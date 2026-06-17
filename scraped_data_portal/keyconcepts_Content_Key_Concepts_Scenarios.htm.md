# 5 Use Case Scenarios

This section provides example use cases illustrating how Program Managers can implement their service through Thredd. It covers three common business cases:

* [Prepaid Card Service](#Prepaid)
* [Neobank/ Digital Banking](#Neobank/)
* [Travel and Foreign Exchange](#Agency)

Company names and examples provided here are fictional and for illustrative purposes only.

## 5.1 Prepaid Card Service

This use case is for a typical Fintech offering a prepaid card service.

#### Business proposition

SchoolCard is a new fintech company offering a simple prepaid card service for use in schools, colleges and universities across the UK. The cards are able to be used in school and campus canteens and to purchase products at participating merchant stores. SchoolCard provides features such as student rewards and loyalty discounts. Users are able to top up funds on the card and the educational faculty are able to use the cards to provide rewards to students.

#### Service architecture

Below is an example of the setup for the SchoolCard prepaid card service:

Click the image to expand.

[![](../Resources/Images/Scenario_1.png "Example of a Prepaid Card Service")](../Resources/Images/Scenario_1.png)

Figure 10: Prepaid Card Service

#### Service implementation

SchoolCard offers a Customer Portal, where customers can sign up for the card and manage their account (for example, top-up and activate cards). For customers with Smart Phones, SchoolCard has a Customer App that can be downloaded and used to manage the card. The Customer Portal and mobile app use the Thredd web services API to connect to Thredd for card services.

All other aspects of the service are provided via Thredd and third-party partners:

* SchoolCard use the service of an existing issuer (BIN Sponsor).
* They hire a software firm to develop a customer mobile app, to enable the service to be managed from a mobile phone.
* They sign an agreement with a local card manufacturer who is pre-integrated to Thredd, for printing and postage of branded cards to educational institutions. The cards can then be distributed to students. Student users must use their app or Customer Portal to activate the card and load with funds.
* SchoolCard is set up in the Thredd system with a simple, single card product configuration, supporting a single currency (GBP). Card usage groups are used to control the features of the card, such as where and how it can be used. Usage groups are assigned dynamically at card creation. SchoolCard use the Thredd fees module to charge a small one-off setup fee and an annual card usage fee.
* Users can top up their account using the SchoolCard payment service, supported via a third-party payment service provider.
* When the card is used at supporting stores, Thredd provides full card authorisation and management of the card balance (Full Service Processing).

## 5.2 Neobank/ Digital Banking

Below is an example of the setup for a typical Neobank offering a digital banking service.

#### Business proposition

Sunrise Bank is a new bank, being launched in the Middle East. The service offers a digital account and multi-currency wallet functionality, enabling cards to be used in countries across the Middle East.

#### Service architecture

Below is an example of the setup for the Sunrise Bank digital banking service:

Click the image to expand.

[![](../Resources/Images/Scenario_2.png "Example of a Neobank / Digital Banking service")](../Resources/Images/Scenario_2.png)

Figure 11: Neobank Digital Banking Service

#### Service implementation

* Sunrise Bank is self-issuing. They have an agreement with their card scheme to issue BIN ranges.
* The bank provides its own in-house CRM, Customer Support and Cardholder mobile App.
* Customer identity, address verification and PEPs checks are carried out by a third-party service provider.
* They sign an agreement with a local card manufacturer for printing and postage of cards to cardholders.
* Since they are supporting multiple countries and currencies, they will need a separate card product set up in Thredd for each currency and issuing country. For details, see the [Thredd Data Model](Setting_up_Program.htm#_GPS_Data_Model).
* The bank manages card authorisation and updates to the card balance (Gateway Processing).
* The bank manages any fees and charges to customers for using their service.
* Thredd provides fraud management services using Fraud Transaction Monitoring and cardholder 3D Secure authentication.

## 5.3 Travel and Foreign Exchange

This use case is for a typical travel and foreign exchange service.

#### Business proposition

SafeHorizons is a new fintech, offering a local debit card for overseas workers. These workers cannot obtain a local bank account and want to have their salaries paid into a local debit card account, in the local currency. They can then use the funds in their country of temporary residence.

Customers can load funds onto their SafeHorizons account or request their employer pay directly into the account. They can use the banking facility provided by SafeHorizons's issuer. Once SafeHorizon has confirmed the funds are in the customer's account, they load the funds onto the customer's local currency card account, using the Thredd API. This ensures that the funds are available for use immediately on the local debit card.

SafeHorizons charge a small load fee to the customer, which is applied each time funds are loaded onto the card, and automatically deducted from the card's balance.

Customers who want to use their new debit card back home, or in another country, are able to create additional currency wallet accounts, linked to their master account. They can transfer funds between their master account and any linked currency accounts. SafeHorizons use an FX services provider to obtain the latest currency rates and charge a small FX transaction fee percentage to the customer.

#### Service architecture

Below is an example of the setup for a typical travel and foreign exchange service:

Click the image to expand.

[![](../Resources/Images/Scenario_3.png "Example of an Agency Banking setup")](../Resources/Images/Scenario_3.png)

Figure 12: Travel and FX Service

#### Service implementation

* SafeHorizons use the services of an existing issuer that has agreement with the card scheme to issue BIN ranges in a number of countries.
* SafeHorizons use a third-party service for Customer Relationship Management (CRM) and Customer Support. Their cardholder mobile App is also developed by a third-party provider of app services.
* Customer identity, address verification and PEPs checks are carried out by a third-party service provider.
* SafeHorizons sign agreements with a local card manufacturer, for printing and postage of cards to cardholders.
* SafeHorizons use their Issuer's Banking service to provide their customers with a means to make payments into and out of their card account.
* When the card is used at supporting stores, Thredd processes and sends to the Program Manager for authorisation. SafeHorizons returns the authorisation decision to Thredd (using Gateway Processing).
* SafeHorizons use the Thredd fees module for managing card service and usage charges.
* Thredd provide fraud management services using Fraud Transaction Monitoring and cardholder 3D Secure authentication.