# 2.8 Agency Banking Fee

This element is only relevant if you are using the Agency Banking service.

**Note**: This element is not applicable to the Discover Global Network.

The AgencyBankingFee primary element is used to describe any bank charges applied to an Agency Banking transaction.

| Child Element | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| BankingFeeId | Unique identitifier for this ApprovedAgencyBanking record. | xs:unsignedLong | Yes | 0 to 2^32 |
| SettlementDate | The settlement date for the transaction. | <SettlementDate> | Yes | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element |
| Card | Provides details of the card used in the transaction. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| AgencyAccount | Provides details of the cardholder account and Agency Bank account details. | <AgencyAccount> | Yes | See the [AgencyAccount](Sub_Elements_and_Attributes.htm#Agency) sub-element |
| AbId | The BankingId of the related ApprovedAgencyBanking or DeclinedAgencyBanking record for this Agency Banking Fee Record (foreign key). | xs:string | Yes | 0 to 2^64  If not applicable, use default value 0 |
| Desc | The reference quoted on the bank charge. This field may be empty. | <Desc> | Yes | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element |
| Amt | The amount of the bank charge applied to the receipt or payment. | <Direction  Amount> | Yes | See the [Amt](Sub_Elements_and_Attributes.htm#Amt) sub-element |

#### Example

[Copy](javascript:void(0);)

[Copy](javascript:void(0);)

```
<AgencyBankingFee>  
    <BankingFeeId>902400</BankingFeeId>  
    <SettlementDate>20200101</SettlementDate>  
    <Card PAN="8063993043846328" MakedPAN="806399******6328" product="MCRD" programid="GPS"   
    productid="9916" branchcode="" />  
    <AgencyAccount no="399304384" type="01" sortcode="" bankacc="" name="N/A" />  
    <AbId>2300456354</AbId>  
    <Desc>Unloading bank transaction 109807 from suspense account. Suspense transaction ID 2300456353</Desc>  
    <Amt value="1.25" currency="826" direction="debit" />  
 </AgencyBankingFee>
```