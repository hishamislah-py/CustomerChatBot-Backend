# 2 The Role of Thredd

This section provides an introduction to the role of Thredd in enabling you to build and deliver a full card and digital payment program.

## 2.1 Thredd as an Issuer-Processor

The Thredd Platform is an issuer-processor, which provides a comprehensive solution for you to manage your card program.

Click the image to expand.

[![](../Resources/Images/Thredd_Network.png "Our Role as an issuer processor")](../Resources/Images/Thredd_Network.png)

Figure 3: Thredd as an issuer-processor

The Thredd platform is integrated within the global payment network and has existing partner relationships and connections that reduces the time required to launch a card program. You can leverage the Thredd payments ecosystem, thus reducing the amount of time-consuming and costly licensing, regulatory compliance, commercial agreements, infrastructure and connections.

Thredd plays an essential role in helping our Program Managers understand the regulatory environment. We implement any changes needed to keep the Thredd systems up-to-date and compliant with the latest regulatory changes, such as the [Payment Services Directive 2 (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A system used to manage the 3D Secure authentication service for the issuer. During an authentication session, the ACS communicates with the Card Scheme and Thredd systems, and may also interact with the cardholder, by providing Challenge screens.](#) and [Payment Card Industry (PCI) Data Security Standard![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Threddâs Secure Connectivity Framework is the combination of several components which enable secure access to Threddâs resources, using a common identity store.](#).

If you want to start issuing cards without becoming an [issuer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.](#), you can use one of Threddâs Issuer/BIN Sponsor partners in your region. For a list of pre-integrated issuers for your region, please contact your Business Development Manager.

Thredd offers a global service, across Europe, North America, the Middle East and Asia Pacific regions, enabling you to expand your product offering as you grow. [1  For our current country-specific support and global roll-out roadmap, please contact your Thredd Business Development Manager.](#)

Thredd currently supports Visa, Mastercard and Discover networks, as well as smaller networks that use the [Mastercard Network Exchange![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#) (MNE), such as STAR and Pulse[2  Please contact your account manager for information on Discover network availability and restrictions. Mastercard Network Exchange enables smaller networks to use Mastercard as a
routing platform for payments.](#).

Our cloud-based processing ensures resilience, scalability, reliability and fast processing, in whatever region you are processing.

## 2.2 Thredd and the Transaction Processing Lifecycle

This section describes how card transactions are processed using Thredd and how transactions on a card are managed during the lifecycle of a transaction.

### 2.2.1 Transaction Processing and EHI Setup

See the table below for details of how Program Managers can use the External Host Interface (EHI) to support transaction processing.

| Setup Option | Who Authorises? | Who Maintains the Balance? | Thredd Stand-In | Details |
| --- | --- | --- | --- | --- |
| Gateway Processing | External Host | External Host | Yes | Your systems maintain the balance and perform authorisation.  Note: If Stand-In is enabled, then your systems maintain the balance and perform authorisation. Thredd provides Stand-In authorisation if the external host is unavailable. |
| Cooperative Processing | Thredd | Thredd / External Host | Yes | Thredd maintains the balance and performs authorisation. You can override an approval decision.  In Approval with Load, your systems maintain the balance and can update the Thredd-maintained balance. |
| Full Service Processing | Thredd | Thredd | No | Thredd maintains the balance and performs authorisation. You receive a read-only response. |

For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Content/Home.htm).

### 2.2.2 Authorisation - When the Card is Used

The purpose of payment authorisation is to confirm that a card is valid for use at the requested merchant and location, and the requested amount is available on the card for spending.

Authorisations require a response in real-time (typically within milliseconds) to a request for an authorisation.

Below are details of how an authorisation works, using two common scenarios:

* Where the Program Manager manages the authorisation decision
* Where Thredd manages the authorisation decision

#### Program Manager Authorises (Gateway and Cooperative Processing)

With Gateway and Cooperative Processing, the Program Manager is responsible for authorisation.

Pre-requisites to use these EHI setup options:

* You maintain the card ledger balance on your own systems
* You must be able to respond to an authorisation request within the Thredd system time limit[3  The default system time limit may vary, depending on your region. Please check with your Business Development Manager.](#)

See the example transaction flow below.

![](../Resources/Images/Auth_PM_approves.png " Authorisation flow where the Program Manager approves")

Figure 4: Authorisation Flow - Program Manager Approves

1. The scheme sends an authorisation request to Thredd.
2. Thredd carries out validation checks and sends the request to the external host (Program Manager).
3. The Program Manager approves the request. \*
4. The Program Manager blocks the approved amount (including fees) on the card and reduces the available balance.
5. The Program Manager returns an approved response.
6. Thredd responds to the scheme with a message indicating approval.

\*In the event that the Program Managerâs systems are unavailable, Thredd can support authorisation through Stand-In Processing (STIP). STIP options are available for Gateway Processing with STIP (mode 4).

#### Thredd Authorises (Cooperative and Full Service Processing)

In Full Service Processing, Thredd provides the authorisation decision. Cooperative Processing provides a hybrid, where Thredd can support the initial authorisation, but the Program Manager can override the decision.

You should use Cooperative Processing (mode 2) or Full Service Processing (mode 3) if:

* You want to get up and running quickly without needing to build a card balance database.
* Your systems are unable to respond with an authorisation decision within the time limit.

See the example transaction flow below.

![](../Resources/Images/Auth_We_approve.png "Authorisation process where our systems approve")

Figure 5: Authorisation Flow - where Thredd Approves

1. The scheme sends an authorisation request to Thredd.
2. Thredd carries out validation checks and approves the request. Thredd blocks the approved amount (including fees) on the card and reduces the available balance.
3. Thredd responds to the scheme with a message indicating approval.
4. Thredd sends an authorisation advice to the external host (Program Manager).

### 2.2.3 Presentments â When Funds are Cleared

A presentment is a financial message provided in the second stage of the life cycle of a transaction.

In the previous stage, the funds on the card were blocked by the authorised amount, ring-fencing this amount and reducing the balance on the card available for spending.

In the second stage, the card scheme receives a request from the merchant acquirer to take the authorised funds. This stage is called *clearing* and results in a clearing message or presentment being sent to Thredd.

Visa and Mastercard send Thredd daily batch clearing files[4  Clearing messages are received based on the card scheme clearing cycles.](#). Thredd process the clearing files and send financial advices to the Program Manager. Thredd refers to these financial advices as presentments.

When Thredd receives the presentment message and sends it to the Program Manager using EHI, the Program Managerâs systems should clear the block on the card and deduct the authorised amount. The issuer will then exchange the money with the acquirer, in a process called *settlement*.

Splitting of transactions into separate messages for authorisation and presentment is typical for card scheme networks in Europe, the UK, Middle East and Asia Pacific. In the USA, payment networks support both dual messages and also a single-stage process that combines the authorisation and presentment in a single message.

Below are details of how presentments are processed.

#### Where the Program Manager Approves (Gateway and Cooperative Processing)

![](../Resources/Images/Presentments_PM_approves.png "Presentment Stage - where Program Manager maintains the balance")

Figure 6: Presentment Stage â where Program Manager holds the balance

1. The scheme sends a batch clearing file to Thredd.
2. Thredd processes the file and sends a notification message per presentment, via EHI, to the external host (Program Manager).
3. The Program Manager matches the presentment to the original authorisation.
4. The Program Manager unblocks the pending amount and reduces the cardholder's available balance.
5. The Program Manager acknowledges the message.

#### Where Thredd Approves (Cooperative, Full Service Processing or no EHI)

![](../Resources/Images/Presentments_We_approve.png "Presentment Stage - where our systems hold the balance")

Figure 7:  Presentment Stage â where Thredd holds the balance

1. The scheme sends a batch clearing file to Thredd.
2. Thredd processes each financial record. Thredd matches the presentment to the original authorisation, unblocks the pending amount and reduces the cardholder's available balance.
3. Thredd sends a notification message per presentment, via EHI, to the external host (Program Manager).

### 2.2.4 Other Financial Messages

In addition to presentments, there may be other types of financial transactions that are linked to the original authorisation transaction. For example:

* Authorisation reversals
* Refunds
* Chargebacks

For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Default.htm).