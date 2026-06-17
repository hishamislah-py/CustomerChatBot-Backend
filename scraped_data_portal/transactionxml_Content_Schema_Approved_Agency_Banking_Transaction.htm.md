# 2.10 Approved Agency Banking Transaction

This element is only relevant if you are using the Agency Banking service.

**Note**: This sub-element is not applicable to the Discover Global Network.

The ApprovedAgencyBanking primary element is used to describe the following accepted activity:

* BACS or Faster Payment Receipt and reversal
* Outbound Faster Payment or Direct Debit Payment and reversal
* Transfers between card holderâs own accounts and reversals
* Inter-program payments between the Programme Managerâs customers and reversals

You can use the `CashType` element to uniquely identify the record and distinguish it from all other CardEvent records.

| Child Element | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| CashType | Cash type, indicates type of receipt, payment or cash transfer. | xs:string | Yes | Valid values are:  â¢ RCP (Receipt)  â¢ RCPREV (Reversal)  â¢ PAY (Payment)  â¢ PAYREV (Reversal)  â¢ TFR (Transfer)  â¢ P2P (Peer-to-Peer)  â¢ P2PREV (Peer-to-Peer reversal) |
| BankingId | Unique identifier for this ApprovedAgencyBanking record. | xs:unsignedLong | Yes | 0 to 2^64 |
| File | Provides details of the file within which notification of the receipt was received, or the name of the file in which the outbound payment was submitted for settlement. | <File> | No | See the [File](Sub_Elements_and_Attributes.htm#File) sub-element |
| SettlementDate | The settlement date for the transaction. | <SettlementDate> | Yes | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element |
| Card | Provides details of the card used in the transaction. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| AgencyAccount | Provides details of the cardholder account and Agency Bank account details. | <AgencyAccount> | Yes | See the [AgencyAccount](Sub_Elements_and_Attributes.htm#Agency) sub-element |
| External | Provides details of the external bank account on the opposite end of the transaction (source of a receipt or destination of a payment). | <External> | Yes | See the [External](Sub_Elements_and_Attributes.htm#External) sub-element |
| CashCode | Provides details of the cash transaction. | <CashCode> | Yes | See the [CashCode](Sub_Elements_and_Attributes.htm#Cash) sub-element |
| Desc | The reference quoted on the receipt or payment. This field may be empty. | <Desc> | Yes | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element |
| CashAmt | The amount of the receipt or payment before deduction of any applicable bank charges. | <RateAmount> | Yes | See the [CashAmt](Sub_Elements_and_Attributes.htm#Cash2) sub-element |
| Fee | The fee applied to the cash receipt or payment. | <Fee> | Yes | See the [Fee](Sub_Elements_and_Attributes.htm#Fee) sub-element |
| BillAmt | The amount posted to the cardholder account. | <RateAmount> | Yes | See the [BillAmt](Sub_Elements_and_Attributes.htm#BillAmt) sub-element |
| OrigTxnAmt | Original transaction amount. The value of the original transaction requested by the cardholder. This is used in the case of the transaction being a reversal. | <PartialAmount> | If Applicable | See the [OrigTxnAmt](Sub_Elements_and_Attributes.htm#OrigTxnA) sub-element |

#### Example

[Copy](javascript:void(0);)

```
<ApprovedAgencyBanking>  
    <CashType>RCP</CashType>  
    <BankingId>13962099212</BankingId>  
    <SettlementDate>20240213</SettlementDate>  
    <Card PAN="1132466669224123" product="MCRD" programid="ONEUKA"   
    productid="4368" branchcode="" />  
    <AgencyAccount no="246666922" type="01" sortcode="040083" bankacc="02548356" name="Emilia Ionita" />  
    <External sortcode="401000" bankacc="94771656" name="COICEA M" />  
    <CashCode direction="credit" CashType="fpy" CashGroup="rcp" />  
    <Desc> </Desc>  
    <CashAmt value="60.00" currency="826" />  
    <Fee value="1.25" currency="826" direction="credit" />  
    <BillAmt value="60.00" currency="826" rate="0" />  
  </ApprovedAgencyBanking>
```