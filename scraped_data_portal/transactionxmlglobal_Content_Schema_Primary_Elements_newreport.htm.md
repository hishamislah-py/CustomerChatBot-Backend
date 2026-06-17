# 2.1 Primary Elements

Primary Elements are listed within a `<Transactions>` parent element, which defines the top-level entities of the message. See the table below for details.

For Discover Global Network reporting, Thredd use the new Global Transaction reporting format, which separates primary element into two separate reports:   
â¢ Non-clearing report â containing authorisation and other real-time messages.  
â¢ Clearing report â containing financial messages based on the card scheme's release cycles (Discover implement one release cycle per day).

| Element Name | Description | Data Type | Occurs |
| --- | --- | --- | --- |
| Non-Clearing Report Primary Elements | | | |
| [CardAuthorisation](CardAuthorisation.htm) | Describes an Authorisation or Reversal. | <CardAuthorisation> | 0 - n |
| [CardOnlineFinancial](CardOnlineFinancial.htm) | Describes single message transactions for the requirements of card payment networks in the US.  **Note**: Not applicable to the Discover Global Network. | <CardOnlineFinancial> | 0 - n |
| [CardFee (Interchange)](CardFee_NCLR.htm) | Describes a fee (and commission).  **Note**: Not applicable to the Discover Global Network. | <CardFee> | 0 - n |
| [CardLoadUnload](CardLoadUnload.htm) | Describes loading and unloading of a card.  **Note**: Not applicable to the Discover Global Network. | <CardLoadUnload> | 0 - n |
| [ApprovedAgencyBanking](Approved_Agency_Banking_Transaction.htm) | Describes an approved Agency Banking transaction (relevant only if you are using the Agency Banking service)  **Note**: Not applicable to the Discover Global Network. | <ApprovedAgencyBanking> | 0 â n |
| [DeclinedAgencyBanking](Declined_Agency_Banking_Transaction.htm) | Describes declined Agency Banking transaction (relevant only if you are using the Agency Banking service)  **Note**: Not applicable to the Discover Global Network. | <DeclinedAgencyBanking> | 0 â n |
| [AgencyBankingFee](Agency_Banking_Fee.htm) | Describes any bank charges applied to Agency Banking transaction (relevant only if you are using the Agency Banking service).  **Note**: Not applicable to the Discover Global Network. | <AgencyBankingFee> | 0 â n |
| [CardBalAdjust](CardBalAdjust.htm) | Describes a card account Balance Adjustment or Reversal.  **Note**: Not applicable to the Discover Global Network. | <CardBalAdjust> | 0 â n |
| [CardEvent](CardEvent.htm) | Describes a card status change event.  **Note**: Not applicable to the Discover Global Network. | <CardEvent> | 0 â n |
| Clearing Report Primary Elements | | | |
| [CardFinancial](CardFinancial.htm) | Describes a Financial Advice or Financial Reversal. | <CardFinancial> | 0 â n |
| [CardFee](CardFee_CLR.htm) | Describes a fee (and commission).  **Note**: Not applicable to the Discover Global Network. | <CardFee> | 0 â n |
| [MasterCardFee](MasterCardFee.htm) | Describes a Financial Advice or Financial Reversal MasterCard fee. | <MasterCardFee> | 0 â n |
| [CardChrgBackRepRes](CardChrgBackRepRes.htm) | Describes a Chargeback, Chargeback Reversal, Representment or Representment Reversal. | <CardChrgBackRepRes> | 0 - n |

Primary elements within an XML message depends on the card activity for the period being reported.  For example, `<CardChrgBackRepRes>` elements are only present when a chargeback (or reversal) or Representment (or reversal) is reported.

#### Non Clearing Report XML Example

This example shows the Primary Elements in a Non Clearing Report.

[Copy](javascript:void(0);)

```
<?xmlversion="1.0"encoding="utf-8"?>  
<Transactions>  
   <CardAuthorisation>â¦detail ommittedâ¦</CardAuthorisation>  
   <CardOnlineFinancial>â¦detail ommittedâ¦</CardOnlineFinancial>  
   <CardFee>â¦detail ommittedâ¦</CardFee>  
   <CardLoadUnload>â¦detail ommittedâ¦</CardLoadUnload>  
   <CardBalAdjust>â¦detail ommittedâ¦</CardBalAdjust>  
   <CardEvent>â¦detail ommittedâ¦</CardEvent>  
   <ApprovedAgencyBanking>â¦detail ommittedâ¦</ApprovedAgencyBanking>  
   <AgencyBankingFee>â¦detail ommittedâ¦</AgencyBankingFee>  
</Transactions>
```

#### Clearing Report XML Example

This example shows the Primary Elements in a Clearing Report.

[Copy](javascript:void(0);)

```
<?xmlversion="1.0"encoding="utf-8"?>  
<Transactions>  
   <CardFinancial>â¦detail ommittedâ¦</CardFinancial>  
   <CardFee>â¦detail ommittedâ¦</CardFee>  
   <MasterCardFee>â¦detail ommittedâ¦</MasterCardFee>  
   <CardChrgBackRepRes>â¦detail ommittedâ¦</CardChrgBackRepRes>  
</Transactions>
```