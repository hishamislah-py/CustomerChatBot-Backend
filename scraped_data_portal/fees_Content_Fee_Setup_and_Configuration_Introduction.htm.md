# 1 Introduction

The Thredd system provides flexible configuration options for setting up and applying card usage and administration fees to the cards in your program, giving you full control over the type of fees to include.

The card fees you charge cardholders must be approved by your [issuer (BIN Sponsor)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Financial organisation and scheme member, licensed by the scheme to issue cards and process transactions using the schemeâs network.](#), and must comply with the card scheme (payment network) regulations.

Thredd fees for your card products are configured using Fee Groups. These groups are currency agnostic and you can define the fee currencies that apply to the group. See [Fee Groups](#_Fee_Groups).

You can specify multiple fee groups for your card program (e.g., to reflect different cardholder product offerings, such as premium, business and standard or different country and currency options) and link each card to a set of fee groups. Each fee group defines the fees that are applicable to a card. See [Figure 1](#Card) below:

![](../Resources/Images/Fee_setup_overview.png)

Figure 1: Card Products and Fee Groups

When creating a card on the Thredd system, you can specify which fee groups to link to the card. Certain fees can be waived at the time the card is created. It is also possible to configure a one-off fee to apply to a specific card; see [Applying Fees to a Card](Fee_Maintenance.htm#_Applying_Fees_to_1).

#### Card Product and Default Fees

Cards are set up on the Thredd system at a Product level. A card product is defined as a combination of country of issue and currency. This means that a different card product is required for each country of issue and currency pair (e.g., France-Euro, or UK-GBP).

While cards are set up at a product level, Fee groups are set up at a [Program Manager![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) level (i.e., per Program Manager) and can be applied to cards belonging to different products or programs (Scheme Masters).

When creating a card using the Thredd API, if you do not specify any fee groups, the card will be linked to the default fees configured for your card product (if defaults have been set up for your card products). In practise, for large programs operating in multiple countries and currencies, it is not practical to set up unique fee groups per product, so in this case, when creating a card you will need to specify the fee groups to link to the card.

#### Changing Card Fees

You cannot directly change your fee group configuration settings (including the fee amounts) on the Thredd system; you will need to raise a change request with your account manager or via JIRA. If you increase any fees that you charge to your cardholder, you must also give them sufficient notice[1  For UK/EEA customers, you must provide 60 daysâ notice. Check with your issuer for notice periods in other regions.](#).

For your current fee setup information, always refer to the latest signed-off copy of the [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#).

#### Fees and EHI Mode

The option to configure fees using the Thredd system is available to customers on all External Host Interface (EHI) modes[2  Please check with your account manager for restrictions, as some fee options may not work for some EHI modes. Currently, web service fees and recurring fees are not supported on Gateway Processing (Modes 1 and 4).](#). However, in EHI modes where you maintain the card balance (Gateway Processing - Mode 1 and Gateway Processing with STIP - Mode 4), Thredd strongly recommends you also manage the fees applied to the card using your own systems.

## 1.1 Fee Groups

Thredd provides three main fee groups:

* Authorisation Fee groups
* Recurring Fee groups
* API Usage Fees groups

Each of these groups in described in further detail below.

### 1.1.1 Authorisation Fee Groups

The Authorisation Fee groups define fees to apply to a card on a per transaction basis when the card is used (e.g., at an ATM, website or merchant terminal) or when a payment is made out of the account. For more information, see [Authorisation Fees](Authorisation_Fees.htm).

For examples of authorisation fees and how they can be applied to your cards, see [Appendix 6: Basic Authorisation Fee Examples](../Reference/Appendix_6_Fee_Examples.htm).

### 1.1.2 Recurring Fee Groups

The Recurring Fee groups define fees to apply to a card on a recurring basis (e.g., monthly, annually or over a defined period). For more information, see [Recurring Fees](Recurring_Fees.htm).

### 1.1.3 API Usage Fees Groups

The API Usage Fee groups define fees to apply to a card when a specific Thredd API is used (example, for a load, balance transfer or balance enquiry). Thredd offer a choice of either SOAP Web Services API or REST-based Cards API for managing your card program. For more information, see [API Usage Fees](Web_Service_Fees.htm).

## 1.2 Configuring your Program Fees

Thredd recommends that you always speak to your card issuer for advice on what fees to apply to your cards. Then talk to your Thredd implementation manager about your fee requirements and the options readily available on the Thredd system.

The card fees that apply to your program are defined using the [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#). The PSF provides the following tabs where the fee groups for your program are recorded:

* 06a. Basic Auth Fees and 06b. Advanced Auth Fees
* 07. Recurring Fees
* 0.8 API Usage Fees

Your implementation manager will complete this form and provide you with a copy to review and make any amendments required. Once you have agreed the contents of the PSF, your implementation manager will set up your fees on the Thredd system.

If you have already set up fees and require changes or new fee groups, please contact your account manager. Any changes to fees should also first be approved by your issuer.

Keep your fees simple â complicated fee configuration can lead to a poor user experience.

#### Bespoke fees

If you require a bespoke fee configuration, please speak to your account manager. Any changes that require development work require Thredd approval and may incur additional charges.

### 1.2.1 Linking a Card to Fee Groups

Fee groups are set up at a Program Manager (Institution) level. When you create a card, you should specify the fee groups to link to the card. If you do not specify any fee groups, then the default fee groups for the linked card product are applied (if default fee groups have been set up).

### 1.2.2 Viewing and Updating a Cardâs Fee Groups

You can use the Thredd API to query the fee groups linked to a card. The Thredd API also enables you to change the fee groups linked to a card and to apply any additional one-off fee charges to a card. For details of how to change a card's fees groups using Thredd SOAP Web Services, see [Managing Fee Groups (SOAP with XML examples)](Fee_Maintenance.htm#_Managing_Fee_Groups). For details of how to change a card's fees groups using Thredd REST-based Cards API, see [Managing Fee Groups (REST with JSON examples)](Fee_Maintenance_REST.htm#Managing).

### 1.2.3 Viewing a Cardâs Transaction Fees

Transaction-related fees are listed in your daily transaction XML report. You can also view transaction-related fees in messages sent via the Thredd External Host Interface (EHI) and on [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#). For details, see [Viewing Fees](Viewing_Fees.htm).

### 1.2.4 Negative Balances and Fees

Thredd cards provide a balance and a spending limit equal to the available balance; Thredd will not deduct a fee if it takes a card into a negative balance. If insufficient funds are available on a card to cover your card transaction and administration fees, Thredd can create a pending fee record. See [Querying Pending Fees.](Fee_Maintenance.htm#_Querying_Pending_Fees) (Note: available on SOAP Web Services). Thredd also enable you to specify that a partial fee amount is taken if insufficient funds are available to take the full fee[3  Pending fee records and partial fees are only implemented if pending fees has been set up for your fee group.](#).See [Partial Fees](Other_Fees.htm#_Example_Partial_Fee).

## 1.3 How are fees applied when a card is used?

[Figure 2](#Applying) below shows the typical process for applying fees on a per transaction basis when a card is used (authorisation process).

![](../Resources/Images/Auth_fee_overview.png)

Figure 2: Applying Card Fees

1. The cardholder uses their card at a [Point of Sale (POS) Terminal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A hardware device for processing card payments at retail stores. The device has embedded software that is used to read the cardâs magnetic strip data.](#), ATM or online merchant website.
2. The merchant website, POS terminal or ATM sends an authorisation request, via their acquirer, to the card scheme (payment network).
3. The card scheme (e.g., Visa, Mastercard or Discover) sends the transaction to Thredd.
4. The Thredd Message Processing System (MPS) processes the transaction. It validates the card, looks up the cardâs usage group to verify the transaction is permitted and then authorises the transaction (Full Service Processing - mode 3) or forwards to your systems for authorisation (Gateway Processing - modes 1,4,5 or Cooperative Processing - mode 2).   
   Thredd identifies the type of transaction based on the processing code in the message, checks the fee groups linked to the card (each fee group defines the type of fee, fee currency and amount) and calculates the correct card product fees.
5. Thredd provides real-time authorisation messages and financial notifications via the External Host Interface (EHI), which include details of fees applied to cards during transactions. The daily XML reports also contain details of fees calculated during transactions. You can view details of fees linked to a specific card or transaction in Thredd Portal or Smart Client.
6. You can use the Thredd API to view and change the fee groups linked to a card and to apply additional card fees.

A transaction may incur additional fees, such as card scheme network interchange fees and FX fees. These are also detailed in the XML reports and EHI messages.

### 1.3.1 Fee Application and Fee Reconciliation

The fee charges applied to a card for a transaction can be viewed in [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#) and in the Transaction Reporting Fee records. Please note the following:

* Any authorisation fees applied by Thredd will be based on the fee configuration you have set up for different transaction types. See [Authorisation Fees: Transaction Types](Authorisation_Fees.htm#_Fee_Options).
* Where an authorisation request is declined, you can configure decline fee to be applied, based on the reason (response code) for the decline. See [Authorisation Fees: Response Codes](Authorisation_Fees.htm#_Response_Codes).
* For details of how fees are applied to cross-currency transactions, see [Appendix 8: Applying Fees to FX Transactions](../Reference/Appendix_8_Multicurrency_fees.htm).
* The following fees may apply to reversals and refunds:

  + If you have set up fees to apply for *authorisation reversals* and *refunds*, then these fees will be applied at the time when a transaction is reversed or refunded.
  + In some instances, merchants may issue *partial refunds*, and not refunds for the full amount (for example, where their contract terms specify a non-refundable booking element), in which case the cardholder will not receive back the same amount as the original transaction amount.
  + For cross-currency transactions where the *transaction* currency is different to the *billing* (base card) currency, the Card Schemes apply a currency conversion rate to the conversion from the transaction amount to the card billing amount. As this conversion rate is based on the Scheme's daily currency pair conversion rate, this rate is not static, and can fluctuate. Bear this in mind, in particular when reconciling fees applied around authorisations, authorisation reversals and refunds â which may take place on different days with differing conversion rates being applied. See [Appendix 8: Applying Fees to FX Transactions](../Reference/Appendix_8_Multicurrency_fees.htm).
* Merchants, acquirers and the card networks may apply additional fees to a transaction (for example, an ATM withdrawal fee and an interchange fee for cross-border transactions). These fees are also visible in the detailed transaction records. See [Other Card Fees](#Other).
* Where Thredd is unable to deduct the full fee from the card, due to insufficient funds, we will create a pending fee record. See [Querying Pending Fees.](Fee_Maintenance.htm#_Querying_Pending_Fees)  
  If enabled for your card product, Thredd can also apply a partial fee. See [Partial Fees](Other_Fees.htm#_Example_Partial_Fee).

## 1.4 Other Card Fees

This section describes additional types of fees that may be raised against a transaction. These are external fees that are not created or managed by Thredd systems.

### 1.4.1 Network Fees

The acquirers and card schemes (networks such as Visa, Mastercard and Discover) charge interchange fees for the processing of transactions over their networks. For example:

* POS transactions â positive interchange fee is paid to the [issuer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Financial organisation and scheme member, licensed by the scheme to issue cards and process transactions using the schemeâs network.](#) (the [merchant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.](#) pays)
* ATM transactions â negative interchange fee is paid to the operator of the ATM
* ATM card capture â fee is paid to the operator of the ATM
* Stolen card fee â interchange fee is paid to the issuer

These fees are only finalised at the [presentment![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment. For more information, see the External Host Interface Guide.](#) stage when settlement and transfer of funds occurs. These fees are not charged directly to the cardholder and are reported separately. You should factor your fee structure in line with potential network fees.

### 1.4.2 Chargeback Fees

Disputed transactions where a [Chargeback![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.](#) is raised may incur additional Chargeback fees, payable to the card scheme (e.g., Visa, Mastercard or Discover) and acquirer/issuer.

It is possible to configure a one-off fee to apply to a card, to reflect any fees incurred as a result of a Chargeback. See [Applying Fees to a Card](Fee_Maintenance.htm#_Applying_Fees_to_1). (Note: available on SOAP Web Services).

For further details on Chargebacks, refer to the [Payment Disputes Management Guide](https://docs.thredd.ai/Chargeback_Guide.htm).