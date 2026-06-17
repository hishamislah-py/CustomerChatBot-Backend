# 1 Payments Dispute Management Overview

You should provide a means for cardholders to contact you to query any payments taken out of their account (e.g., by providing a call centre number printed on the back of their card or a ticketing system to log issues).

The cardholder may dispute a payment for a number of reasons, for example: they may not recognise the payment, the payment amount may be incorrect or the goods or services they paid for were not received or not as advertised. You can look up payment transaction details in [Smart Client![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's user interface for managing your account on the Thredd Platform.
Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.](#), using the transaction date, card number/Thredd public token or other filters to find the transaction you are looking for. See [Showing Transactions for a Card.](Managing_Chargebacks_on_SmartClient.htm#Showing)

In all instances, the cardholder should first contact the merchant to attempt to resolve their issue, for example, by asking the merchant to issue a refund or send a replacement. Where the customer and merchant cannot agree on a resolution, the cardholder has the right to contact their card issuer and ask them to raise a chargeback.

## 1.1 What is a Chargeback?

A chargeback is a type of transaction dispute where a cardholder contacts their card issuer and requests their money back for an item or service purchased using their card. The cardholder can only dispute a charge on their account and request a chargeback where they have a valid reason. For example:

* Goods or services not received
* Goods or services received not as advertised, faulty or of an unsatisfactory quality
* The amount charged is incorrect
* Fraudulent transaction â the cardholder did not make the transaction and their card details were obtained fraudulently

The card schemes (i.e., Visa and Mastercard; also known as card networks) provide rules and processes, as well as systems to handle chargebacks. You can find out more about their rules at the following links:

* [Mastercard Chargeback Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)
* [Visa Chargeback Guidelines for Merchants](https://usa.visa.com/dam/VCOM/download/merchants/chargeback-management-guidelines-for-visa-merchants.pdf) (see Section 5 for issuer guidelines)

## 1.2 What is the Chargeback Process?

Figure 1 below provides a summary of the chargeback process.

![](Resources/Images/Chargeback_flow.png)

Figure 1: Chargeback Transaction Flow (Simplified)

Note that the communication between issuer and acquirer and the arbitration process is managed via the relevant [card scheme![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Discover, Mastercard or Visa); it is not shown in this figure.

The Thredd Mastercard API development provides support for creating and managing the chargeback process described below, and includes new options such as arbitration and pre-arbitration case filings and bulk chargeback creation.

1. The cardholder disputes a transaction with their issuer (card issuing bank or their Program Manager).
2. Where required by scheme rules the card issuer sends a retrieval request to the merchantâs acquirer (financial institute providing the merchant with a merchant trading account) to obtain additional information.

Mastercard offer a [Collaboration Option](#_Notes), where the chargeback first goes directly to the merchant before involving the acquirer.

3. The acquirer and issuer attempt to resolve the dispute if possible (for example, by issuing a refund), otherwise the acquirer sends a chargeback notification to the merchant.
4. The merchant either accepts the chargeback or refutes it. If they refute the chargeback, they must submit the necessary evidence through representment.
5. The acquirer reviews the evidence, checks it meets the requirements and sends to the issuer.
6. The issuer reviews the new evidence and makes a final decision.
7. At this point, any party unhappy with the decision can either request further review, via pre-arbitration or go directly to the arbitration stage. If the acquirer and issuer cannot reach an agreement, the process enters arbitration. The card schemes will examine the evidence and make a final decision.

The arbitration process can last for months and costs hundreds of pounds, which must be paid to the card schemes.

## 1.3 How does Thredd Support Chargebacks?

As a Program Manager or card issuer, your cardholders should have a means to contact you directly to raise disputes about a transaction on their account. This is typically via a call centre number printed on their card or advertised on your website. When a cardholder queries a transaction, you can use the Thredd Smart Client application to view details of the transaction. Smart Client also provides a facility to enable you to raise and manage chargebacks (Note that this is only available for Mastercard issuers in Europe/UK at present). See [Managing Chargebacks on Smart Client](Managing_Chargebacks_on_SmartClient.htm).

Chargebacks are also supported via the relevant card scheme (e.g., MasterCard or Visa), which provide online systems where issuers and acquirers can view and respond to chargeback notifications.

If you are a card issuer, you will be able to respond directly to the card schemes. However, most Thredd clients are Program Managers, who use an existing card issuer to provide their card service, and in this case, Thredd can mediate on your behalf with your issuerâs permission.

Some issuers manage all chargebacks for their Program Manager clients, while others want their clients to raise their chargebacks directly with us and have enabled our Mastercom API to facilitate this.   
If you are a Program Manager you will not have a direct relationship with the card scheme. You will need your issuer or Thredd to provide you with information to help you manage your chargebacks.

## 1.4 Payment Authorisation Transaction Process

Figure 2 provides an overview of the transaction process and parties involved in a typical card payment scenario.

![](Resources/Images/Card_Pay_Auth_1013x230.png)

Figure 2: Card Payment Authorisation

Visa and Mastercard distribute Bank Identification Number (BIN) and sub BIN range tables to their customers (acquirers and issuers).

1. When a cardholder uses their card at a merchant store or website, or draws out money from an ATM, the acquirer Point of Sale (POS) terminal or Online PSP forwards the authorisation request to the merchantâs acquirer.
2. The acquirer uses the BIN range tables to determine where to route the transaction.
3. The acquirer routes the transaction to the relevant card scheme (Visa or Mastercard).
4. Using the same BIN range, tables Visa and Mastercard identify the card issuer and route the transaction to the issuer.

If the acquirer and issuer are the same bank, then the transaction is processed internally, and not sent to Mastercard or Visa.   
In some countries domestic transactions are routed via national switches, but not sent to Mastercard or Visa (e.g. BKM in Turkey).

If you are a Program Manager, the card scheme will route the transaction to Thredd, who then forwards on to your card issuer. Depending on your External Host Interface (EHI) setup, in cases where the Thredd External Host system holds the balance on the card (e.g., Full Service Processing), Thredd may perform the payment authorisation and then forward to the issuer. You will receive real-time transactional data via your EHI data feed or overnight as transactional XML reports. See Figure 3.

![](Resources/Images/Tnx_flow_GPS.png)

Figure 3: Role of Thredd in Transaction Authorisation

At a transactional level, issuer BINs are routed to Thredd. However, issuers still settle the funds between Mastercard and Visa, as Thredd does not hold the funds on the card.

Mastercard and Visa both provides online systems to enable acquirers and Issuers to raise and manage disputes. Issuers have different preferences as to how they want to manage chargebacks for their Program Managers:

* Some issuers prefer to handle chargebacks on behalf of their Program Managers.
* Some issuers provide their Program Managers with access to Mastercard (Mastercom UI) and Visa (Visa VROL) online systems to enable them to directly raise and respond to chargebacks
* Other issuers want Thredd to manage this at a programme level for the Program Manager, which we do via [Smart Client![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's user interface for managing your account on the Thredd Platform.
  Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.](#).

Please refer to your issuer in the first instance for details.

## 1.5 Chargeback Processes â Transaction Status View

Figure 4 below shows the typical transaction status changes during the life cycle of a transaction, from authorisation through to presentment and chargeback. This is a simplified view and does not show all the steps involved.

![](Resources/Images/Chargeback_flow_1.png)

Figure 4: Transaction Life Cycle (Simplified)

1. The cardholder uses their card to make a purchase and the transaction is Authorised. This step involves checking the balance on the account to ensure there are sufficient available funds for the transaction. At this stage the authorised amount may be reserved on the cardholderâs account or the merchant may want to take it immediately.
2. When the merchant is ready to take the funds, the transaction is submitted for clearing, where the authorised amount is debited from the cardholderâs account. This stage is known as Clearing or First Presentment. In Smart Client, this is shown as a Presentment status.
3. Settlement is the process where actual funds are exchanged between the issuer and acquirer (the acquirer implements a separate settlement process with their merchant).

Thredd receive settlement reports from the scheme and pass it to our clients without any checks or additional processing. Actual settlement (funds transfer) is between the schemes and our issuers. This stage is shown in Figure 4 for completeness and is not recorded as a transaction status within Smart Client.

4. A chargeback request can be initiated on a transaction that has reached the Presentment stage, and only on Thredd's side, not the acquirer's side. (Prior to this, a PM or issuer can remove an authorisation, but this will not prevent a first presentment from being applied.)
5. Once a chargeback is raised, it is sent to the card scheme (Mastercard or Visa) who forwards it on to the merchantâs acquirer. At this stage the acquirer can accept the chargeback. If the acquirer does not agree with the chargeback, they can refute the chargeback, and the transaction goes into the Second presentment stage.
6. If the chargeback cannot be resolved, the card issuer can decide to proceed with case filing and case the transaction enters the Arbitration stage. The card scheme reviews and make a final decision.

After completion of the chargeback process, the acquirer and issuer can file relevant case documents. They can also raise fee collection requests.

### 1.5.1 Collaboration Option

Mastercard offer a collaboration option, where the chargeback first goes directly to the merchant (the acquirer is not involved at this stage). If the merchant accepts collaboration, they will need to issue the refund as a separate transaction[1  In this case the chargeback is rejected by Mastercard with Reject reason code 5000 and an email notification is sent to the Issuer. The refund will be received in the normal clearing files from Mastercard. Note that a 5001 reject code indicates a credit voucher issued by the merchant; this will not generate a refund transaction.](#).

By improving communication between the issuer and merchant prior to the formal dispute process taking place, many disputes can be settled without entering the chargeback process.

This service is enabled via Mastercard. Check with your Issuer for details.