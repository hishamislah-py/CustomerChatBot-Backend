# 1.1 Overview

The External Host Interface (EHI) offers a way to exchange transactional data between the Thredd processing system and the [Program Managerâs![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) externally hosted systems. All transaction data processed by Thredd is transferred to the [external host![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.](#) system via EHI in real time. EHI provides two main functions:

* A real-time transaction notification data feed
* Payment authorisation control

Thredd supports Visa, Mastercard and Discover networks, as well as smaller networks that use the [Mastercard Network Exchange![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#) (MNE), such as STAR and Pulse[1 Contact your account manager for information on Discover network availability and restrictions. Mastercard Network Exchange enables smaller networks to use Mastercard as a routing platform for payments.](#)  . EHI provides a single, unified message format, which enables your systems to receive and process messages using a single integration to Thredd. For more information, see [Card Payment Networks](Card_Networks.htm).

## 1.1.1 Real-time Transactional Data Feed

Thredd receives global real-time card and payment-related notifications from the [card schemes![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Visa and Mastercard networks). These notifications are merged into a single Thredd message format which your systems can process. The real-time notifications are sent via a secure connection to the external host URL endpoint you have requested for your programme. These include notifications for: *Authorisations*, *Presentments*, *Financial* messages, *Load* and *Balance Transfers* and *Expired Cards*. For details see [Transaction Types](Transaction_Types.htm).

Your systems should respond with an acknowledgement of receipt of the message.

The EHI data feed can be used to ensure you can provide your cardholders with real-time information.

For more information on the fields and attributes included in the data feeds, see [EHI Data Feeds](EHI_Data_Feeds.htm).

In addition to the real-time data feed, Thredd also provides daily batch XML reports, via [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). You can use this data to support your payment reconciliations. See the *XML Transaction Reports Specifications*.

## 1.1.2 Payment Authorisation Control

The [payment authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) process is initiated when a cardholder makes a purchase with a [merchant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.](#) , who then seeks authorisation for the card payment via their [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#). See the figure below.

![](../Resources/Images/EHI-transaction-flow-overview.png)

Figure 1: Parties involved in the payment authorisation process

When a payment authorisation request is received from the card schemes, Thredd first performs conventional transaction-related card and cardholder checks, such as EMV data, PIN, CVV2, velocity checks, fraud checks and card product checks.

Your EHI setup option determines whether Thredd or your systems manage the payment authorisation. For example:

* Gateway Processing (Mode 1): Your systems maintain the card balance. You make the authorisation decision and respond to Thredd to indicate whether the transaction can be approved or declined.
* Cooperative Processing (Mode 2): Thredd maintains the card balance. Thredd approves or declines and sends to you the transaction. This enables you to overrule any approved decision.
* Full Service Processing (Mode 3): Thredd maintains the card balance. Thredd makes the authorisation decision and provides you with the response.
* Gateway Processing with STIP (Mode 4 ): Your systems maintain the card balance. You perform authorisation. Thredd delivers Stand-In Processing (STIP) if your systems are unavailable.

Thredd provides other flexible mode options, where a combination of Thredd and external host authorisation can be used. See [EHI Operating Modes](EHI_operating_modes.htm).

Thredd will process your response and respond to the card scheme (Mastercard or Visa). The authorisation decision process is in real time.