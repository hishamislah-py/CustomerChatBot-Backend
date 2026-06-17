# 1.6 Dual vs. Single Message Systems

The Dual Message System follows a payment messaging standard which provides separate messages for the [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) and clearing (presentment) stages. In contrast, the Single Message System combines the authorisation and clearing stages of a payment transaction into a Single Message. See:

* [Dual Message System](#Dual)
* [Single Message System](#Single)
* [Backwards Compatibility Mode](#Backward) â for Program Managers who are processing Dual Messages and also want to support the Single Message standard

Single Message System does **not** apply to you, unless you have configured your BINs to support Single Message System at the card scheme. You should check with your Thredd account manager and Mastercard or Visa representative to see which method is available for your region or country.

## 1.6.1 Dual Message System

This system provides separate messages for authorisation and clearing. It is a prominent method in Europe and is also used in other regions.

![](../Resources/Images/dual_message_system.png "Dual Message System")

Figure 10: Dual Message System

The initial Message Type Identifier (`MTID`) is an 0100 Authorisation message in which the billed amount or settlement amount has not yet been finalised (where the bill amount and settlement amount status is open). This is followed afterwards by the 1240 (Mastercard) or 05/06/07 (Visa) Clearing message, in which the billing amount (`Bill_Amt`) and settlement amount (`Settle_Amt`) are finalised.

Thredd receives a daily [clearing file![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.](#) from the card scheme and generates the clearing messages which are sent to the Program Manager via EHI.

### How to Handle Dual Messages

When your systems receive:

* The 0100 Authorisation message, you should respond with an *approve* or *deny*. If approved, then block the approved amount plus any transaction fees on the card.
* The 1240 or 05/06/07 Clearing message (Thredd refer to this as the [Presentment![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment.](#)), your systems should match the clearing message to the original authorisation message.

For more information on Dual Message transactions, see [Transaction Flow Scenarios - Dual Message Systems.](Transaction_Flow_Scenarios.htm)

## 1.6.2 Single Message System

Single Message System is a transaction processing message standard which combines authorisation and presentment into a Single Message. A transaction can start as a Single Message, but could be transformed into Dual message if it's routed to a Dual message network. If Dual message conversion is not applicable (for example, the US Debit Network - Mastercard Networks Exchange), the transactions are received as Single Messages from that network.

Thredd connects to [Mastercard Network Exchange![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.](#), which is a Card Scheme system that processes messages according to the Single Message System standard. If Thredd receives messages from Single Message Systems, these will be processed and sent via EHI to the external host. Examples of messages unique to Single Message Systems, which Thredd can provide via EHI, include: 0200 [online financial requests![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.](#), 0220 Online Financial Advices and 0420 V Online Financial Reversals).

Single Message System does **not** apply to you, unless you have configured your BINs at the card scheme to support Single Message System. 0100 pre-authorisation messages can still be received in a Single Message System. For example, a hotel could send a 0100 message to block an amount and then send an 0220 message to match to the previous request.

If you want to receive the relevant online financial messages, you must have configured your BINs at the card scheme to support a Single Message System.

![](../Resources/Images/single_message_system.png "Single Message System")

Figure 11: Single Message System

The initial Message Type Identifier (`MTID`) is an 0200/M online financial request or 0220/Q online financial advice message, in which the billed amount (`Bill_Amt`) and settlement (`Settle_Amt`) are finalised.

### How to Handle Single Messages

* When your systems receive the 0200/M online financial request, you should respond with *approve* or *deny* and deduct the approved amount plus any transaction fees from the card. You may also receive an **Online Financial Advices (0220/Q)** or
  **Online Financial Reversal** (0420/V), in which case you must apply the balance change.

* Thredd returns an 0210 message response to the card scheme.

If your issuer operates a Single Message System, you should ideally support the new message types above.

For more information on Single Message System transactions, see [Transaction Flow Scenarios - Single Message Systems.](Transaction_Flow_Single_Message_System.htm)