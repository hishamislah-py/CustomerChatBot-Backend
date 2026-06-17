# 1 Introduction to Card Payments

This section provides a high-level description of the parties and components involved in setting up a card program and processing transactions on cards.

## 1.1 Parties Involved in Setting up a Card Program

The figure below provides an overview of the key parties involved in setting up a card program.

![](../Resources/Images/Parties_involved_card_creation.png "Parties involved in the card issuing and creation process")

Figure 1: Key Parties in Setting Up a Card Program

Each of these parties is described in further detail below.

### 1.1.1 Card Scheme (Payment Network)

The Card Scheme (e.g., Visa, Mastercard, Discover) provides the payment network used by all parties during a payment transaction. Cards that use the network are branded with the scheme logo (e.g., Visa, Mastercard, Discover and Diners).

The scheme provides mandates and rules which card issuers must follow when using their network. The schemes connect acquirers and issuers, provide daily clearing files and support the settlement and dispute management process. Schemes also charge fees to both acquirers and issuers for using their network.

Thredd plugs in directly to the payment network and has partner relationships with Visa, Mastercard, Discover, as well as smaller networks that use the [Mastercard Network Exchange![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#) (MNE), such as STAR and Pulse[1 Please contact your account manager for information on Discover network availability and restrictions. Mastercard Network Exchange enables smaller networks to use Mastercard as a routing platform for payments.](#)  .Visa, Mastercard and Discover are global networks and allow their branded cards to be used worldwide[2  Thredd is currently developing links to other global and local card schemes. Please contact your Thredd Business Development Manager for details.](#).

The Thredd platform receives transactions from the scheme networks and processes these messages. The platform can provide fraud screening, transaction checks and authorisation, before forwarding messages in real-time to your systems via the External Host Interface (EHI). For detail, refer to the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm).

If you are using the services of an Issuer, you do not need a direct relationship with the scheme, as your issuer manages this on your behalf.

#### Key Scheme Responsibilities (Payment Network)

* Provides the payment infrastructure
* Has global relationships with acquirers and issuers
* Sets product rules (e.g., Funds management, Product level capabilities and restrictions)
* Sets interchange and other scheme related fees
* Maintains the full BIN table and issues BINs to issuers
* Sets chargeback and dispute rules
* Provides value-added offerings, such as Tokenisation and Chargeback management
* Maintains cardholder usage data

### 1.1.2 Issuer (BIN Sponsor)

The card issuer is the BIN Sponsor. The Issuer âissuesâ the card BIN ranges that can be used to create new cards (based on their agreement with the card scheme).

Issuers have a direct relationship with the scheme and with Thredd.

Issuers hold client money and must have separate, ring-fenced client money accounts. They must hold additional funds in reserve to meet scheme requirements. Issuers are regulated by the Financial Authority in their region (for example, for UK issuers this is the Financial Conduct Authority), so additional regulatory compliance standards apply.

Thredd customers (Program Managers) can be self-issuers or use the services of an existing issuer.

For new Thredd customers starting out on a card program with Thredd, speed to market is quicker and easier when using an existing issuer already set up with Thredd, compared to setting yourself up as a new issuer. You can upgrade to self-issuing at a later stage without any impact on your transactions[3  Migrating to self-Issuing requires changes to reporting and BIN setup with the card scheme. If you want to find out more about how to become self-issuing, please check with your Business Development Manager.](#).

If your preferred issuer in your region does not currently have a relationship with Thredd, it will require additional Thredd integration support to on-board them. For further details, contact your Thredd Business Development Manager.

If you are using an existing issuer you will not have a direct relationship with the card scheme. Issuers settle transfers of money directly with the schemes and details of issuer are normally printed on the back of their issued cards. Your issuer must provide you with access to relevant scheme resources and administrative portals. They will also need to approve your card program before it can be switched to live.

#### Key Responsibilities (Issuer)

* Ownership and customer (Program Manager) due diligence
* Must comply with Regulator and Card Scheme rules relating to:

  + Anti-money laundering
  + Risk monitoring
  + Fraud monitoring
  + Reporting (such as quarterly member reports and quarterly operating certificate)
  + Auditing
  + Record retention guidelines
  + MIS analysis
* Typically holds funds
* Dispute management and chargebacks: may delegate to the Program Manager
* Maintains a separate cash deposit
* Maintains client money in a separate Trust account
* Responsible for settlement and reconciliation (reconciliation may sometimes be delegated)
* Provides letter of guarantee for Program Manager
* Many need to review and approve aspects of the Program Managerâs service, such as the Customer Portal, Customer App and Customer Terms & Conditions.

### 1.1.3 Program Manager

The Program Manager is a Thredd customer who manages a card program.

The Program Manager signs up their customers for an account and can issue cards and other payment products on the Thredd platform. They manage the relationship with their customers, and are responsible for customer on-boarding, Know your Customer (KYC)/Know your Business (KYB) and Anti-Money Laundering (AML) checks. The Program Manager is responsible for all customer communications and management of their customers.

Below are examples of what you need to do as a Program Manager:

* Your website/customer mobile application should provide a means for customers to contact you to report issues with cards or transactions on a card. You may need a separate Customer Relationship Management (CRM) system to manage customer queries. Your customer service staff can use the Thredd Smart Client application to view transactions on a card, issue refunds and handle chargebacks. See the Smart Client Guide.
* You will need a payment service provider to take customer payments to fund the account.
* You should provide a Customer Portal/ mobile application where customers can sign in and manage their account. You can use the Thredd web services API and real-time data from Thredd data feeds to enable customers to self-service their account, for example: top up, move money between wallet accounts, link their mobile device to a card (e.g. ApplePay), upgrade their account, report a lost or stolen card, freeze a card and enquire on the balance in their account.
* You should maintain a separate fee arrangement with your customers for usage of the cards and account service charges. Thredd offers a Fees module which you can use to manage your card fees. See the [Fees Guide](https://docs.thredd.ai/Fees_Guide.htm).
* If you want to handle or process card details, such as the cardâs Primary Account Number (PAN), you must be PCI DSS compliant. Thredd provides a means to manage cards without needing to process the PAN, using a Public Token (a unique 9 digit number that represents the card).

#### Key Responsibilities

* Card product design and development
* Card product management marketing
* Supply chain (ordering card plastics, personalisation and delivery)
* Technology development and testing
* Customer service
* Risk and analytics
* May hold the virtual balance of the card (with [EHI](System_Architecture.htm#_External_Host_Interface)  Gateway Processing or Cooperative Processing setup options)

### 1.1.4 Thredd

Thredd has existing partner relationships and connections with schemes, issuers and card manufacturers, and is integrated with service providers such as 3D Secure, Transaction Fraud Monitoring and mobile wallet token providers.

The Thredd Platform is a flexible system for creating, managing and processing transactions on multi-wallet physical and virtual cards. The system enables Program Managers to set up their card program and configure how their cards will be used. The system can also apply card usage fees on behalf of the Program Manager.

The Thredd Platform provides integrated support for key add-on services such as 3D secure authentication, Multi-FX, mobile wallet virtual cards/tokenisation, Chargeback management and Fraud mitigation.

Support is provided through your Thredd Business Development Manager and Implementation Manager during the project initiation and integration stages, and from your Account Manager once you are live.

One key aspect of the Thredd solution is the dedicated customer support provided at all stages of a project. Thredd works closely with you to configure the system to your requirements, and integrate any additional services required.

#### Key Responsibilities

* Payments and database infrastructure
* Database management, transaction authorisation, card activation
* Scheme mandate compliance, certification and accreditation[4  We will update our systems to comply with scheme transaction processing mandates; it is the Issuer and Program Managerâs responsibility to be aware of and comply with any additional scheme mandates (e.g., around fees, reporting and reconciliation).](#)
* Maintains the card balance and transaction history if required ([EHI Cooperative Processing and Full Service Processing setup or no EHI)](../Glossary.htm#_EHI)
* Connections to card manufacturers
* Reporting
* Product functionality support and velocity controls
* Fee structure

### 1.1.5 Card Manufacturer

Thredd has existing partner relationships and plug-ins to over 40 card manufacturers worldwide and can support local card creation programs in regions worldwide. Check with your Business Development Manager or Implementations Manager for details.

Thredd supports full Program Manager branded cards, with dynamic elements and [EMV![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMV is an acronymn for "Europay, Mastercard, and Visa", the three companies which created the standard. The EMV cards are also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility. These cards are smart cards.](#) configuration options.

You must have a separate commercial agreement with your card manufacturer. Cards are first pre-manufactured as blank cards. These cards contain the chips, antenna and blank magstripe.

During the initial pre-manufactured card setup stage, you should allow sufficient time for cards to be manufactured. (This can take a few weeks; please check with your card manufacturer for timelines.)  
Scheme testing may be required for new Chip profile configuration.

Once pre-manufactured cards are set up, you can use the Thredd API to create physical card instructions, to send to your card manufacturer. These instructions include the personalised details to add to the cards for individual cardholders. See the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API) or [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm) (SOAP API).

When the manufacturer receives the card creation instructions, they add the personalised data profile: they update the cardâs magstripe and Chip data, and print details on the card, such as the cardholder name, PAN, CVV2 and expiry date. (This process can take a few days.)

### 1.1.6 Cardholder

When the cardholder signs up for your service, you should provide an online website/portal or customer mobile application which customers can use to manage their account, for example: configure their card options, query the balance on their cards, change PINs and load or unload cards.

You should provide your cardholder with a means to contact you with queries or issues related to their account and card service.

## 1.2 Parties Involved in Transaction Processing

The figure below provides an overview of the key parties involved in processing transactions on a card.

![](../Resources/Images/Parties_involved_auth.png "Parties involved in authorising transactions")

Figure 2: Key Parties in Processing Card Transactions

Each of these parties is described in further detail below (in the same order as shown in the figure above).

### 1.2.1 Program Manager (before the card is used)

The Program Manager must activate a card for it to be used. This is done via the Thredd API. See the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API) or [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm) (SOAP API).

Below are examples of what you need to do as a Program Manager to support card usage:

* Depending on your card offering, you can decide whether or not to activate the card on card creation. For example, for a virtual card, used on a mobile phone, the card can be activated for immediate use on creation. However, for a card that is printed and mailed to a customer, it may be advisable to require the customer to phone in or use your Customer mobile application to activate the card after it has been received.
* When a card is created, using the Thredd web services API, you can link it to a Thredd card product, which determines the cardâs usage settings. You can also link the card to card usage groups set up for your program. This determines where and how the card can be used. See Card Usage Groups.
* Where Thredd holds the card balance on your behalf (such as with Full Service Processing setup), you must ensure the balance on the card reflects any customer money paid into or transferred out of their card account, or other balance adjustments made on the card account. You can use the Thredd API to load/unload and perform balance adjustments on a card. These API will update the Thredd cards database, where the transaction and balance ledger on the card is maintained. For details, see the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API) or [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm) (SOAP API).

### 1.2.2 Cardholder

The cardholder uses their physical or virtual card online or at a physical merchant shop (also called a Point of Sale (POS) transaction). They may use their card at an ATM (automatic teller machine) to withdraw money, change a PIN or run balance enquiries.

For POS transactions where the card is presented, the POS terminal reads the [EMV![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMV is an acronymn for "Europay, Mastercard, and Visa", the three companies which created the standard. The EMV cards are also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility. These cards are smart cards.](#)/CHIP card configuration data. This data indicates how and where the card can be used.

During a Point of Sale (POS) transaction at a terminal, the cardholder may be asked to authenticate by entering a PIN into the terminal. During an online transaction, they may be asked to enter a One-Time Password (OTP) or use another method such as Biometric authentication to verify their identity. For details, see the [3D Secure Guide](https://docs.thredd.ai/3D_Secure_Apata.htm).

Thredd is compliant with the [Second Payment Service Directive (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A system used to manage the 3D Secure authentication service for the issuer. During an authentication session, the ACS communicates with the Card Scheme and Thredd systems, and may also interact with the cardholder, by providing Challenge screens.](#) regulations relating to how card transactions are handled and authenticated. For details, see the [PSD2 and SCA Guide](https://docs.thredd.ai/PSD2_Guide.htm).

### 1.2.3 Merchant

The merchant is the business, shop or online website where the card is used. Each merchant is identified at the acquirer by a Merchant ID (MID) and assigned a [Merchant Category Code (MCC)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.](#), which indicates the type of business and business sector they are trading in.

The merchant requests payment authorisation when a card is presented to them via a website, Mail and Telephone Order (MOTO) or at a Point of Sale (POS) terminal.

You can configure your card products to control card usage, for example to allow or deny card usage based on the MCC and limit usage of the card to the domestic country. For example: you can block card usage on gambling and adult sites, based on the MCC. You can also set up permission lists, to allow cards to be restricted for use to a list of specific Merchant IDs (for example, for a corporate card or gift card, which is limited to use at merchant sites linked to a specific shopping mall).

You should be aware that an authorisation request may not be for the full or final amount (e.g., a preauthorisation or partial authorisation) and may be followed by an [incremental authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation.
For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.](#). There may also be a delay of several days or more from when the authorisation is made to when the funds are requested by the merchant. (For example, when a card is used at a hotel or a car hire service, an initial amount may be authorised, followed by the final amount several days later).

There is no direct contact between merchants and Program Managers. Your customers should contact the merchant directly in the first instance for any issues or queries relating to an item or service purchased, and only contact your or their card issuer if the problem cannot be resolved.

The Thredd [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#) application enables your customer services staff to view transactions, issue refunds, block cards and raise [Chargebacks![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.](#) (Mastercard only). For details, see the [Smart Client Guide](https://docs.thredd.ai/smartclient/Default.htm).

### 1.2.4 Acquirer

An acquirer is typically a large banking organisation authorised to trade in a region, operating within a strongly regulatory framework, and with connections to the card schemes. They provide the banking licenses and accounts that enable merchants to take payments.

The merchant acquirer owns the relationship with the merchant and provides the Merchant Account (MA) or Internet Merchant Account (IMA) to the merchant. They may also provide the physical terminals that enable merchants to take in-store POS payments.

Acquirers send transaction authorisation and other financial messages to the card schemes. When Thredd receives these messages from the card schemes, the Thredd Platform processes each message and then forwards to the Program Manager via EHI data feeds and/or transaction XML reports. See the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm) and the [Transaction XML Reporting Guide](https://docs.thredd.ai/transactionxml/Default.htm).

Acquirers are responsible for managing the settlement process on behalf of their merchants. They typically hold on to funds received via settlement from the issuers before passing the funds on to the merchant. Any dispute management and chargeback processes are managed between the acquirer and issuer, with the card scheme mediating between them. See the [Payments Dispute Management Guide](https://docs.thredd.ai/Chargeback_Guide.htm).

Acquirers charge fees for network transactions, which are reported with the transaction messages. Thredd reports these charges to the Program Manager.

You will need a payment services provider (PSP) and [Acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#) if you are taking card payments from your customers to load their accounts. This relationship is between you and the PSP and acquirer. Thredd does not currently provide a direct PSP service.

### 1.2.5 Card Scheme (Payment Network)

The card scheme provides the payment network over which card payments take place, receiving messages from acquirers and forwarding to Thredd, and receiving authorisation responses from Thredd and returning to the acquirer.

Thredd currently supports Visa, Mastercard and Discover schemes. These are global schemes that allow their branded cards to be used worldwide. We also support Mastercard Network Exchange (MNE) for enabling US debit card payments.

When a transaction is received from an acquirer, the scheme checks the cardâs Primary Account Number (PAN) to determine whether it is has an allowed BIN. They may perform other fraud management checks. The scheme then forwards the transaction to Thredd.

Where a device PAN (DPAN) is being used (for example, for a virtual card mobile payment or tokenised service), the scheme converts the DPAN back to the PAN and forwards to Thredd. See the [Tokenisation Service Guide](https://docs.thredd.ai/Tokenisation_Guide.htm).

Both Visa and Mastercard provide additional services to cardholders, acquirers and issuers. See the table below.

| Service | Scheme Platform | More Information |
| --- | --- | --- |
| Chargeback Management | Mastercom Claims Manager  Visa Resolution Online (VROL) | [Payments Dispute Management Guide](https://docs.thredd.ai/Chargeback_Guide.htm?tocpath=Technical%20Documentation%7C_____6) |
| 3D Secure | Visa Secure and Mastercard Identity Check | [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm)  [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm) |
| Tokenisation | Mastercard Digital Enablement Service (MDES) and Visa Token Service (VTS); Thredd refer to the Visa service as the Visa Digital Enablement Program (VDEP). | [Tokenisation Guide](https://docs.thredd.ai/Tokenisation_Guide.htm?tocpath=Technical%20Documentation%7C_____5) |

### 1.2.6 Thredd

Thredd receives transaction authorisation messages and financial messages from the card schemes.

Thredd provides initial validation and checking of messages: Thredd checks the EMV details, the BIN, the card usage groups and allow/deny lists to confirm whether the transaction is allowed. Thredd applies any card transaction fees (where the Program Manager is using the Thredd Fees module).

Thredd can support transaction authorisation for Program Managers who are using the External Host Interface (EHI); depending on the Program Managerâs setup, Thredd handles authorisation requests or passes on to the Program Managerâs systems for authorisation. EHI setup options are flexible, and Program Managers can do a combination, for example where they authorise, but use Thredd as a fallback if their systems are not available. For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm).

Thredd reports authorisation decisions to the card scheme in real-time.

Thredd provides both daily and real-time transactional data feeds to the Program Manager, which can be used for transaction matching and reconciliation. See the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm) and the [Transaction XML Reporting Guide](https://docs.thredd.ai/transactionxml/Default.htm).

### 1.2.7 Program Manager (when the card is used)

Thredd can authorise transactions on your behalf where we hold details of the balance on the card (Full Service Processing, Gateway Processing with Stand-in Processing or where EHI is not being used).

Alternatively, you can maintain the card balance on your own systems and manage the authorisation decision (Gateway Processing) or use Thredd as a fallback option for stand-in processing when your systems are not available (Cooperative Processing and Gateway Processing with Stand-In). For details of setup options, see [Transaction Processing and EHI](Our_Role.htm#_Transaction_Processing_and).

Where Thredd provides authorisation services and holds the card balance (e.g., Full Service Processing), you will need to update the card balance held by Thredd to reflect card loads/unloads and balance adjustments. This is done using Thredd API. See the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API) or [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm) (SOAP API).

In transaction processing setups where you manage the authorisation decision, your systems must perform transaction matching and maintain a transaction and card balance database. For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm).

Thredd can provide a Reconciliation service, powered by Kani, to support reconciliation and reporting. For more information, please contact your Account Manager.

### 1.2.8 3D Secure Provider

3D Secure is a protocol/program supported by the major card schemes, which provides Cardholder authentication during an online transaction.

3D Secure helps to reduce the risk of online fraud by requiring the cardholder to enter or provide some information or something that only they should possess:

| Knowledge | Possession | Inherence |
| --- | --- | --- |
| Something they know | Something they have | Something they are |
| Example: password or PIN. | Example: mobile phone, card reader or other device evidenced by a One-Time Password (OTP). | Example: fingerprint, face recognition or voice recognition. |

Thredd provides full 3D Secure support via a choice of 3D Secure service providers: Apata or Cardinal Commerce. Program Managers are set up with an account and access to a 3D Secure Portal for configuring their 3D Secure authentication rules and policies.

During an online transaction where 3D secure authentication is required, the card scheme sends the authentication request to the 3D Secure service provider's [Access Control Server (ACS)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A system used to manage the 3D Secure authentication service for the issuer. During an authentication session, the ACS communicates with the Card Scheme and Thredd systems, and may also interact with the cardholder, by providing Challenge screens.](#). The ACS applies the authentication rules, which the Program Manager has pre-configured, to determine whether the transaction can be seamlessly authorised without requiring cardholder input.

If further cardholder authentication is required, the ACS notifies Thredd, and Thredd notifies the Program Manager to start the authentication session.

For more information, see the [3D Secure Guide](https://docs.thredd.ai/3D_Secure_Apata.htm).