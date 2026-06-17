# 1 Overview

A Master Virtual Card (MVC) is a type of master account card record that you can use to reflect money loaded into a cardholder's account. An MVC is ideal for programs where it is linked to multiple physical and/or virtual cards, as you can transfer money to any of those cards. The MVC card record is restricted to loading and unloading only, and cannot be used like a regular card.

The following diagrams show how an MVC works with multiple virtual and physical cards.

![](../Resources/Images/Overview_virtual.png)

Figure 1: An MVC with Linked Virtual Cards

![](../Resources/Images/Overview_physical_950x774.png)

Figure 2: An MVC with Linked Physical Cards

Note that it is also possible to link a single MVC to both virtual and physical cards.

An MVC can link to physical and virtual cards for a particular currency. For example, an MVC can link to cards for US Dollars, while another MVC can link to cards in Euros. The above example shows MVCs set up for Pound Sterling.

A single MVC can only link to physical and virtual cards of the same currency. You cannot have an MVC with linked cards of more than one currency.

An MVC guarantees that the load is limited to the prefunded amount, where the money is loaded onto the MVC. As soon as funds have been authorised or paid into your Issuer Bank account, you can distribute the funds to the linked cards.
For additional use cases of MVCs, see [Use Case Scenarios](Use_Case_Scenarios.htm).

You can create and manage MVCs using either SOAP web services or the Cards API. Most functions are available across both types of APIs, including, creating, loading and transferring balances.

Creating physical MVCs or performing any type of Point of Sale, e-commerce, ATM or other type of payment transactions are not possible with an MVC. In addition, your Issuer (BIN sponsor) must agree to allowing MVC cards for your program. This is because MVCs are cards with loads, and are included in the Transaction, Balance and other reports sent to you and your Issuer.

## 1.1 Funding of the MVC

An MVC is a type of prefunding account which allows the Program Manager to load an
amount which is not yet assigned to any cardholder. Therefore, these are the
funds of the Program Manager and are not counted as e-money.

The Program Manager controls the settlement account and is responsible for covering the
actual money from the load into the Issuer's settlement account.

The Program Manager agrees with the Issuer on how they will be informed that funds have
arrived in the Issuers Bank account (and by whom). They also agree on who is responsible for reflecting this value on
the MVC.

Issuers maintain the following processes for managing MVCs:

* They provide the Program Manager with âview accessâ to their accounts. This ensures that, when the actual funds are available in the Issuers Bank Account, the Program Manager can then reflect that e-money
  value on the MVC.
* They advise the Program Manager when these funds are available so that the Program Manager can reflect the value on the MVC.
  This happens outside of Thredd and is between Program Manager and the Issuer to agree.

## 1.2 Setting Up Your MVC

When setting up your MVC, two options are available:

1. Create a separate card product for your MVC (recommended). This lets you create a default card configuration and card usage groups that apply only to your MVCs. For example, you can set up a usage group to ensure that no transactions or fees are applied to the MVC. When creating an MVC as a separate card product, it will not expire. Note that when creating a separate product, you select a flag on the PSF form for **card account non expiry**, which means the MVC does not expire.
2. Use the same card product for the MVC and other types of cards (for example, physical or virtual). You should create an MVC to expire after 8 years. Note that once the MVC expires, any cards that are linked to an MVC need to be relinked using the Thredd API: SOAP [Link Cards](https://docs.thredd.ai/webservices/Content/Web_services_api/Cards_Link.htm) (`Ws_link_cards`) Web Service or REST-based [Update Card](https://cardsapidocs.thredd.com//reference/update-card) API (using the `parentCard` field). Using the same card product means that the default product configuration is shared. You need to first set up relevant Card Usage groups for your MVCs and then apply these groups to each MVC when created. Using the same product also requires you to adjust the expiry date of the MVC to match the cards.

You specify configuration options on your Product Setup Form (PSF). For more information see [MVC Setup Options.](../Configuration/Setup_Options.htm)

You are not required to activate an MVC, as it can receive loads without being activated. Remaining inactive provides an extra security measure should the MVC ever be compromised.

#### Controls

There are 3 types of controls to protect the MVC in a transaction environment.

* Groups: Each card product is allocated a default set of attributes or groups. An MVC includes the Velocity Limits group and a Card Usage Group. This ensures that, if the MVC ever was compromised, usage would be restricted to loading and unloading only. With Velocity Limits, the card can only be loaded. This is because Cash and POS limits are set to ZERO. With Card Usage Groups, all usage groups are restricted.
* Stop Card Going to Print: When creating an MVC, the Program Manager must stop an MVC going to print by selecting 4 as the `<CreateType>` through SOAP web service or, if using the REST-based Cards API, selecting `cardType` of *MasterVirtual*.
* PAN & CVV Should Never be Made Known to Cardholder/Corporate Client: If anyone using an MVC needs a reference, then they should be provided with the MVC's 9 digit token. The MVCâs PAN and CVV should never be retrieved or made known to the MVC holder

If an MVC is being created from the same Product ID as other cards, then it is likely that the Program Manager needs to ensure that the correct Velocity Limit Groups and Card Usage groups exist.

## 1.3 Creating MVCs

You create MVCs using either Thredd's SOAP-based Web Services or the REST-based cards API. For more information, see [Using Web Services](../Configuration/Using_Web_Services.htm) and [Using the Cards API.](../Configuration/Using_Cards_API.htm)

You should ensure that you use the correct API environment that you have been provided access to. For example, if you have been given access to the REST environment, use REST instead of SOAP.

## 1.4 Updating the Account Balance on the MVC

Your MVC can share the balance with other types of cards or have its own separate balance. For more information, see [MVC Setup Options > Sharing of Balance](../Configuration/Setup_Options.htm#Sharing).

#### Example MVC Account Balance Update Flow

The following shows an example workflow for updating an account balance.

1. The customer tops up their account via bank transfer or through accepting an online card payment. Your customer portal or mobile app should provide your cardholders with a means to top up the account. The âactualâ money is authorised and paid to your Issuer's bank account.
2. You use either the [Web Services](../Configuration/Using_Web_Services.htm) or the [Cards API](../Configuration/Using_Cards_API.htm) to load funds onto the MVC. Loading funds ensures that the money that has been paid into the account (minus any fees you charge for top-ups or currency conversion).
3. You display the latest MVC balance to the cardholder once loaded.
4. The cardholder transfers funds to any of the cards linked to their MVC wallet.
5. Your mobile app updates the balances on the cards to reflect these transactions.

For additional use cases for updating the account balance, see [Use Case Scenarios](Use_Case_Scenarios.htm).

## 1.5 Alternative Names for an MVC

An MVC can be referred to by these other names.

* iMVC (individual Master Virtual Card)
* Wallet
* Deposit Account
* Prefunding Account
* Holding Account/Pot
* Jam Jar
* Corporate Wallet

## 1.6 External Host Interface (EHI) Modes

You can use an MVC in Full Service Processing (mode 3). However, it is not applicable to Gateway Processing (modes 1 and 4). In situations where you want to override Thredd's approval or load a card on approval, you can uses Cooperative Processing (mode 2). For more information, see the [EHI Guide for XML](https://docs.thredd.com/EHI_Guide.htm) or the [EHI Guide for JSON](https://docs.thredd.com/EHI_Guide_JSON.htm).

For clients using EHI Cooperative Processing with *approve with load*.  
MVC setup is restricted to the *Separate Balance* option, which supports loading funds to a single MVC card during the authorisation approval and load process. A *Shared Balance* setup, where funds are automatically transferred between primary and secondary cards, is not supported. See [Balance Setup](../Configuration/Setup_Options.htm#Sharing).

## 1.7 MFX Functionality

If you are using MFX functionality for multiple currencies, you cannot use an MVC. This is because the MFX functionality uses multiple wallets.