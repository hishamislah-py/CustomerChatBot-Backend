# 3.5 Processing Transactions with Thredd

This section describes how Thredd can help you to authorise and process card transactions.

## 3.5.1 Receiving Transaction Messages

Program managers can use the real-time Thredd External Host Interface (EHI) API to receive card payment transactions from the scheme network.

Depending on your business requirements and resources, you may need to implement your own card balance and authorisation engine to manage transaction messages received from Thredd. Thredd can do these processing steps for you if you do not want to implement a separate authorisation engine.

For more information about the different options for receiving Thredd EHI messages, see [EHI Modes](../Managing/Transaction_Management.htm#EHI).

Details of transactions are also available through Thredd transaction reports and can be viewed on the Thredd [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#).

## 3.5.2 Authorisation Approvals and Declines

When an authorisation request arrives, Thredd runs a number of initial checks:

* Incoming message format and integrity checks.
* Is this a genuine transaction and is the card a valid card?
* Is the cardholder permitted to make this transaction (e.g., the card is not over its configured daily spend amount or single transaction amount)?
* Have any configured risk checks been passed?
* Is there a sufficient available balance on the card for the requested authorisation amount?
* Has Strong Customer Authentication (SCA) been performed on the transaction or does the card qualify for any SCA exemptions? (applicable to issuers implementing SCA in relevant regions)

Thredd works in conjunction with the program manager to make all necessary card control, card and transaction validation checks, as well as available balance checks.

![](../Resources/Images/Intro_card_payments/Card_checks.png)

Figure 13: Thredd Card Transaction Checks

If all checks are passed, then the transaction can be approved. Otherwise, the transaction is declined.

### Approving the Transaction

Who approves the transaction depends on a number of factors, including whether it is Thredd or the program managerâs systems which hold the latest card balance. See below for details of possible configuration options.

| Who authorises? | Who maintains the card Balance? | Description | Recommended EHI Setup Option |
| --- | --- | --- | --- |
| Your organisationâs systems | Your organisationâs systems | Your systems maintain the card balance and make the ultimate authorisation decision[1  Thredd may decline the transaction due to reasons such as PIN check failure or chip cryptogram failure.](#).  You update the cardâs balance in your card database to reflect the available balance on the card after this transaction. | Gateway Processing (mode 1) |
| Your  organisationâs systems | Your organisationâs  systems + Thredd | Both your systems and Thredd manage the card balance, but your systems make the ultimate authorisation decision.  You provide Thredd with details of any card loads/unloads and balance adjustments (using the Thredd web services/cards API).  Approve with load  If Thredd declined the transaction due to insufficient balance, you can override the Thredd decline by using approve with load.  In your authorisation response message you can provide Thredd with details of the latest balance on the card, which will update the Thredd held balance. | Cooperative Processing (mode 2) |
| Thredd | Thredd | Thredd maintains the card balance and makes the authorisation decision and necessary balance adjustments.  You provide Thredd with details of any card loads/unloads and balance adjustments (using the Thredd web services/cards API). | Full Service Processing (mode 3) |
| Your organisationâs systems  (Thredd as fallback) | Your organisationâs systems  + Thredd | In some instances, your systems may be unable to respond to the authorisation request in time (e.g., due to a system failure or processing delay on your end). In this case, Thredd can provide Stand-In Processing (STIP) on your behalf.  You provide Thredd with details of any card loads/unloads and balance adjustments. | Gateway Processing with STIP (mode 4) |
| Your Systems  (Scheme as fallback) | Your Systems | An alternative option is to enable scheme Stand-In Processing for you when you are unable to respond to an authorisation request in time. | Scheme configuration (not related to EHI) |

For more information about the different options for authorisation processing and balance control using the Thredd External Host Interface (EHI), see [External Host Interface](https://docs.thredd.ai/More_Information/EHI_Message_Processor.htm).

In some cases, a program manager may decide not to use EHI. In this case all authorisation decisions will be made by Thredd. No real-time notifications will be sent to your systems.