## 9.4 Transaction Report Primary Elements

Primary Elements are listed within a `<Transactions>` parent element, which defines the top-level entities of the message. See the table below for details of elements relevant to Discover Global Network.

For Discover Global Network reporting, Thredd use the new Global Transaction reporting format, which separates primary element into two separate reports:   
â¢ Non-clearing report â containing authorisation and other real-time messages   
â¢ Clearing report â containing financial messages based on the card scheme's release cycles (Discover implement one release cycle per day).

| Element Name | Description | Data Type | Occurs |
| --- | --- | --- | --- |
| Non-Clearing Report Primary Elements | | | |
| [CardAuthorisation](CardAuthorisation.htm) | Describes an Authorisation or Reversal. | <CardAuthorisation> | 0 - n |
| Clearing Report Primary Elements | | | |
| [CardFinancial](CardFinancial.htm) | Describes a Financial Advice or Financial Reversal. | <CardFinancial> | 0 â n |
| [CardChrgBackRepRes](CardChrgBackRepRes.htm) | Describes a Chargeback, Chargeback Reversal, Representment or Representment Reversal. | <CardChrgBackRepRes> | 0 â n |
| [MasterCardFee](MasterCardFee.htm) | Describes a MasterCard fee. | <MasterCardFee> | 0 â n |

The presence of primary elements within an XML message depends on the card activity for the period being reported.  For example, `<CardChrgBackRepRes>` elements are only present when a chargeback (or reversal) or Representment (or reversal) is reported.

#### Non Clearing Report XML Example

This example shows the Primary Elements in a Non Clearing Report.

[Copy](javascript:void(0);)

```
<?xmlversion="1.0"encoding="utf-8"?>  
<Transactions>  
<CardAuthorisation>â¦detail ommittedâ¦</CardAuthorisation>  
</Transactions>
```

#### Clearing Report XML Example

This example shows the Primary Elements in a Clearing Report.

[Copy](javascript:void(0);)

```
<?xmlversion="1.0"encoding="utf-8"?>  
<Transactions>  
<CardChrgBackRepRes>â¦detail ommittedâ¦</CardChrgBackRepres>  
<CardFinancial>â¦detail ommittedâ¦</CardFinancial>  
<MasterCardFee>â¦detail ommittedâ¦</MasterCardFee>  
</Transactions>
```