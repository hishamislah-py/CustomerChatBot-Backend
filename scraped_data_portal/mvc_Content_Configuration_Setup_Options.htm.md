# 3 MVC Setup Options

You can specify MPC setup options using the Product Setup Form (PSF). These include setting up product, sub-bin ranges and balances. For more information, discuss your requirements with your Thredd Implementation Manager.

## 3.1 Product Setup

You can set up an MVC as a separate card product. Alternatively, you can configure an MVC to share the same card product as other card types:

| Product setup option | Card Usage Group and Limit Group Setup |
| --- | --- |
| Dedicated product for your MVC | Set up a default card [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#) and [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#) for your MVC product.  When creating the card, you only need to specify the card product that you are using. |
| MVCs shares same product as other cards | Set up a default card [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#) and [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#) for MVC-type cards.  When creating the MVC, assign the MVC limit and usage groups to the card. |

## 3.2 Sub-Bin Setup

The MVC can share the same sub-bin range as your other types of cards. Alternatively, you could assign a dedicated sub-bin range to the MVC if required.

Since you cannot print or use MVCs for purchases, Thredd recommend you do not use separate BIN ranges, as this reduces the number of available BINs that you can use.

## 3.3 Balance Setup

Your MVC can share the balance with other types of cards, or have its separate balance.

| Balance setup | Usage |
| --- | --- |
| Shared Balance | The MVC holds the master balance for all cards.  During transactions, a token links cards and an MVC allocates funds to other cards. The linked physical or virtual cards do not hold a balance.  To use this option, you require a [Card Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#). For details, check with your Implementation Manager.  This option is not supported on EHI Cooperative Processing (mode 2) with *approve with load*. |
| Separate Balance | The MVC and other types of cards maintain their own separate balance.  You transfer funds manually from an MVC to the required cards. |

If an MVC is on a separate Product ID to your physical or virtual cards (or under another Thredd Scheme/ BIN), you can share balances and transfer funds between the MVC and cards. You can transfer funds automatically or use the [Thredd API](Using_Web_Services.htm) or [Cards API](Using_Cards_API.htm).

#### Shared Balances

For shared balances, the Card Linkage Group allocates funds from the MVC to be used as transactions, which works in the following ways:

* Limits can be applied to authorisations, loads, and payments.
* Certain capabilities can be set on the secondary card, such as loading and payments.

* Funds left on the cardholder's cards are swept back to the MVC overnight.
* If there has been a reversal, the funds are returned to the MVC.
* In the case of a refund, scheme rules dictate that refunds need to return to the card that performed the transaction.

When reporting shared balances, note the following:

* The cardholder's card does not have a balance and is reported in the Transaction xml (as the transactions took place on this card.)
* The MVC shows in the Balance xml as it holds the balance.

If the Program Manager wants this sweep to happen immediately (rather than overnight), then this capability needs to be developed on their platform. Alternatively, they can use `WS_BalanceTransfer` to configure their sweeps. `WS_BalanceTransfer` is a dedicated SOAP web service for transferring balances (for more details, see [Transferring a Balance](Using_Web_Services.htm#Transfer))