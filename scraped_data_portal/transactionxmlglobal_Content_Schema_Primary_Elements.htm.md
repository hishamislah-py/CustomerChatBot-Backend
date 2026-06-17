# 4.11 Primary Elements

Primary Elements are listed within a `<Transactions>` parent element, which defines the top-level entities of the message. See the table below for details.

| Element Name | Description | Data Type | Occurs |
| --- | --- | --- | --- |
| [CardAuthorisation](CardAuthorisation.htm) | Describes an Authorisation or Reversal. | <CardAuthorisation> | 0 - n |
| [CardFinancial](CardFinancial.htm) | Describes a Financial Advice or Financial Reversal. | <CardFinancial> | 0 â n |
| [CardChrgBackRepRes](CardChrgBackRepRes.htm) | Describes a Chargeback, Chargeback Reversal, Representment or Representment Reversal. | <CardChrgBackRepRes> | 0 â n |
| [CardFee](CardFee.htm) | Describes a fee (and commission). | <CardFee> | 0 â n |
| [MasterCardFee](MasterCardFee.htm) | Describes a MasterCard fee. | <MasterCardFee> | 0 â n |
| [CardLoadUnload](CardLoadUnload.htm) | Describes a Card Load, Card Load Reversal, Card Unload and Card Unload Reversal. | <CardLoadUnload> | 0 â n |
| [ApprovedAgencyBanking](Approved_Agency_Banking_Transaction.htm) | Describes an approved Agency Banking transaction (relevant only if you are using the Agency Banking service) | <ApprovedAgencyBanking> | 0 â n |
| [DeclinedAgencyBanking](Declined_Agency_Banking_Transaction.htm) | Describes declined Agency Banking transaction (relevant only if you are using the Agency Banking service) | <DeclinedAgencyBanking> | 0 â n |
| [AgencyBankingFee](Agency_Banking_Fee.htm) | Describes any bank charges applied to Agency Banking transaction (relevant only if you are using the Agency Banking service). | <AgencyBankingFee> | 0 â n |
| [CardBalAdjust](CardBalAdjust.htm) | Describes a card account Balance Adjustment or Reversal. | <CardBalAdjust> | 0 â n |
| [CardEvent](CardEvent.htm) | Describes a card status change event. | <CardEvent> | 0 â n |
| [FXConversion](FXConversion.htm) | Describes Foreign Exchange (FX) rate conversion. | <FXConversion> | 0 â n |
| [WalletTransaction](WalletTransaction.htm) | Describes a wallet account transaction. | <WalletTransaction> | 0 â n |

The presence of primary elements within an XML message depends on the card activity for the period being reported.  For example, `<CardChrgBackRepRes>` elements are only present when a chargeback (or reversal) or Representment (or reversal) is reported.

#### Transactional XML example showing several Primary Elements

[Copy](javascript:void(0);)

```
<?xmlversion="1.0"encoding="utf-8"?>  
<Transactions>  
<CardAuthorisation>â¦detail ommittedâ¦</CardAuthorisation>  
<CardBalAdjust>â¦detail ommittedâ¦</CardBalAdjust>  
<CardChrgBackRepRes>â¦detail ommittedâ¦</CardChrgBackRepres>  
<CardFee>â¦detail ommittedâ¦</CardFee>  
<CardFinancial>â¦detail ommittedâ¦</CardFinancial>  
<CardLoadUnload>â¦detail ommittedâ¦</CardLoadUnload>  
<MasterCardFee>â¦detail ommittedâ¦</MasterCardFee>  
<WalletTransaction>â¦detail ommittedâ¦</WalletTransaction>  
</Transactions>
```