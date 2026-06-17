# 1.3 EHI Operating Modes

For authorisation types of transactions, the external host interface can operate in one of five supported modes. See the table below:

| Setup type | Mode | Who Authorises? | Who Maintains the Balance? | Thredd Authorisation Stand-In | Details |
| --- | --- | --- | --- | --- | --- |
| Gateway Processing | 1 | External Host | External Host | No | Your systems maintain the balance and perform authorisation. |
| Cooperative Processing | 2 | Thredd | Thredd / External Host | Yes | Thredd maintains the balance and performs authorisation. You can override an approval decision.  In [Approval with Load](#Approval) your systems can update the Thredd-maintained balance. |
| Full Service Processing | 3 | Thredd | Thredd | No | Thredd maintains the balance and performs authorisation. You receive a read-only response. |
| Gateway Processing with STIP | 4 | External Host | External Host | Yes | Your systems maintain the balance and perform authorisation. Thredd provides Stand-In authorisation if the external host is unavailable. |

Each mode is described in more detail below.

Not sure which mode you need? To find the right mode for your business, try our [EHI Mode Selector Wizard](https://docs.thredd.ai/ehi_mode_selector/story.html).

## 1.3.1 Gateway Processing (Mode 1) - External Host Maintains Balances

You manage the cardholder balances and approve or decline a payment [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) request.

Your system should always calculate the total balance impact of the transaction, for example billing amount and fees, when determining whether to approve the transaction.  (See [Calculating the Total Cost](../Appendices/Calculating_the_Total.htm).)

![](../Resources/Images/Mode1.png "EHI Mode 1")

Figure 3: Gateway Processing (Mode 1) - external host approves transaction

1. The [card scheme![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Visa or Mastercard) sends an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) or [online financial![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.](#) request.
2. The Thredd Message Processing System (MPS) performs checks such as [authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.](#), [validation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date](#) and fraud protection[1 Fraud protection is based on whether you are using Thredd's real-time Fraud Transaction Monitoring service. If a rule is triggered it can decline the card transaction.](#), as well as checks based on your product configuration. (This results in a decline if the checks fail. In this case Thredd sends an advice only to the Program Manager and no authorisation decision is required.)
3. The EHI server sends the request to the external host URL endpoint configured for the Program Manager.
4. The external host (i.e., Program Manager's systems) then decides whether to approve or decline the transaction, by checking details of the balance held on the card.
5. The EHI server waits for a response from the external host. The response must be received within the allowed time period (see [EHI Configuration Options](EHI_Configuration_Options.htm)) or the transaction is declined. When received, this is forwarded to the card scheme.

## 1.3.2 Cooperative Processing (Mode 2) - Thredd Maintains Balances

Thredd performs all types of checks (card, cardholder and balance). But the external host can overrule the Thredd decision and advise to decline the transaction.

![](../Resources/Images/Mode2.png "EHI Mode 2")

Figure 4: Cooperative Processing (Mode 2) - Thredd approves in first instance

1. The [card scheme![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Visa or Mastercard) sends an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) or [online financial![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.](#) request.
2. The Thredd Message Processing System (MPS) performs checks such as authentication, validation and fraud protection, as well as checks based on your product configuration.
3. Thredd decides whether to approve or decline the transaction, based on the balance details held by Thredd.
4. The EHI server sends the Thredd response (approve or decline) to the external host URL endpoint configured for the Program Manager.

   * If declined, you can overrule the Thredd decision only for a balance decline (where *Approve with Load* is enabled)[2 In mode 2 - Approval with Load you can override a balance decline, where Thredd declined because the Thredd held balance indicated insufficient available funds to cover the authorisation; in this case, you should follow up the override by loading the amount to the card, to update the Thredd held balance.](#).
   * If approved, you can decide whether to overrule the Thredd decision and decline the transaction.
   * You can approve for a partial amount if the transaction satisfies the conditions for [partial amount approval](Transaction_Flow_Scenarios.htm#Partial).
5. The approve or decline response is sent to the card scheme.

Since Thredd maintains the balance, we update the balance as part of the payment transaction life-cycle.

In Mode 2, you can override a Thredd decline code of 51 (Insufficient Funds) with another decline code by passing this in the `ResponseStatus` field of your EHI response. Adding a different decline code is useful for passing to a cardholder a more specific decline reason. However, note that if the Thredd response status is not 51 (Insufficient Funds), then any response status from your end is ignored and the original Thredd response status (as provided in the `Status_Code` field) is preserved.

### Stand In

In Mode 2 EHI supports authorisation *Stand-In* where Thredd can fully approve transactions at times where there is no connection to the external host. If *Stand In* is enabled and there is no response from the external host during the allocated time-out period, Thredd approves or declines the transaction, based on Thredd data (such as available balance, card usage rules and risk settings). âOn behalfâ approved transactions have the `Authorised by Thredd` flag set to â*Yes*â and when delivered to the external host, Thredd only requires an acknowledgement response.

### Approval with Load

Your external host systems can approve a card transaction with a simultaneous instruction to Thredd for loading an amount to the card (in order to update the Thredd-maintained card balance ledger).   
If this is required and the product is enabled with the *Approval with Load* option, the response message of the approved transaction must contain the â*0A*â response code and the amount to load. The load is done before the transaction amount is debited from the current balance.

Your external host systems should take into account the total balance impact of the transaction (billing amount, fees and padding) when determining whether to approve the transaction.  (See [Calculating the Total Cost](../Appendices/Calculating_the_Total.htm).)

Multi-currency FX cards do not support *Approval with load*.

For clients using Master Virtual Cards (MVCs). MVC setup is restricted to the *Separate Balance* option, which supports loading funds to a single MVC card during the authorisation approval and load process. A *Shared Balance* setup, where funds are automatically transferred between primary and secondary cards, is not supported. For more information, see the [Master Virtual Cards Guide: MVC Setup Options](https://docs.thredd.com/mvc/Content/Configuration/Setup_Options.htm).

The Card Schemes (Mastercard and Visa) must approve any *Approve with Load* programmes.

## 1.3.3 Full Service Processing (Mode 3) - Read-only Data Subscription

Thredd manages the card transaction request and approves or declines. The external host interface is used only as a transaction data feed from the Thredd system to the Program Managerâs system.

![](../Resources/Images/Mode3.png)

Figure 5: Full Service Processing (Mode 3) - Thredd approves and external host receives data subscription service only

1. The [card scheme![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Visa or Mastercard) sends an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) or [online financial![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.](#) request.
2. The Thredd Message Processing System (MPS) performs checks such as authentication, validation and fraud protection, as well as checks based on your product configuration.
3. Thredd decides whether to approve or decline the transaction, based on the balance details held by Thredd. Thredd updates the balance.
4. The approve or decline response is sent to the card scheme.
5. The EHI server sends an advice with the transaction outcome, including the latest card balance, to the external host URL endpoint configured for the Program Manager.

## 1.3.4 Gateway Processing with STIP (Mode 4) â External Host Maintains Balance (with Thredd Stand-in)

EHI Mode 4 is as EHI Mode 1 (where you approve the transaction), except that the external host can maintain the Thredd stand-in balances. If the external host cannot be contacted, then Thredd approves or declines using the current Thredd stand-in balance. The Thredd stand-in balances can be updated by any of the below options:

* EHI response messages (see [`Update_Balance`](../Requirements/GetTransaction_Message.htm#_Ref448230883) field).
* Balance Update Web Service (see `ws_BalanceUpdate` in the [*Web Services Guide*](https://docs.thredd.com/Web_Services_Guide.htm)).
* STIP Balance Update endpoint (see the [API Hub documentation](https://cardsapidocs.thredd.com/v2.0/docs/card-balance-update)).

In EHI Mode 4, all transactions (authorisations and financials) updates the Thredd stand-in balance.

![](../Resources/Images/Mode4.png "EHI Mode 4")

Figure 6: Gateway Processing with STIP (Mode 4) - External host approves, but Thredd can stand in if external host is not available

1. The [card scheme![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.](#) (Visa or Mastercard) sends an [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) or [online financial![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.](#) request.
2. The Thredd Message Processing System (MPS) performs checks such as [authentication![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.](#), [validation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date](#) and fraud protection, as well as checks based on your product configuration. This result in a decline if the checks fail. In this case Thredd send an advice only to the Program Manager and no authorisation decision is required.
3. The EHI server sends the card transaction request to the external host URL endpoint configured for the Program Manager.
4. The external host (or the Program Manager's systems) decides whether to approve or decline the transaction, by checking details of the balance held on the card.
5. The EHI server waits for a response from the external host. If EHI receives an approve or decline response, the response is returned to the card scheme.
6. If no response is received, then Thredd does stand-in authorisation on behalf of the Program Manager and sends this to the card scheme.