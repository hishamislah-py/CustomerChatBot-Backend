# 2.7 Declined Agency Banking Transaction

This element is only relevant if you are using the Agency Banking service.

**Note**: This element is not applicable to Discover Global Network.

The DeclinedAgencyBanking primary element describes the following declined activity for which the cardholder did not receive or lose value:

* BACS or Faster Payment Receipt and reversal
* Outbound Faster Payment or Direct Debit Payment and reversal
* Transfers between card holderâs own accounts and reversals
* Inter program payments between the Programme Managerâs customers and reversals

You can use the `CashType` element to uniquely identify the record and distinguish it from all other DeclinedAgencyBanking records.

| Child Element | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| CashType | Cash type, indicates the type of receipt, payment or cash transfer. | xs:string | Yes | Valid values are:  â¢ RCP (Receipt)  â¢ RCPREV (Reversal)  â¢ PAY (Payment)  â¢ PAYREV (Reversal)  â¢ TFR (Transfer) |
| BankingId | Unique identifier for this ApprovedAgencyBanking record. | xs:unsignedLong | Yes | 0 to 2^64 |
| File | Provides details of the file within which notification of the receipt was received, or the filename in which the outbound payment was submitted for settlement. | <File> | No | See the [File](Sub_Elements_and_Attributes.htm#File) sub-element |
| SettlementDate | The value date for the transaction. | <SettlementDate> | Yes | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element |
| Card | Provides details of the card used in the transaction. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| AgencyAccount | Provides details of the cardholder account and Agency Bank account details | <AgencyAccount> | Yes | See the [AgencyAccount](Sub_Elements_and_Attributes.htm#Agency) sub-element |
| External | Details of the external bank account on the opposite end of the transaction. This is the source of a receipt or destination of a payment. | <External> | Yes | See the [External](Sub_Elements_and_Attributes.htm#External) sub-element |
| CashCode | Provides details of the cash transaction. | <CashCode> | Yes | See the [CashCode](Sub_Elements_and_Attributes.htm#Cash) sub-element |
| Desc | The reference quoted on the receipt or payment. This field may be empty. | <Desc> | Yes | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element |
| CashAmt | The amount of the receipt or payment before deduction of any applicable bank charges. | <RateAmount> | Yes | See the [CashAmt](Sub_Elements_and_Attributes.htm#Cash2) sub-element |
| DeclineReason | The reason a receipt was declined and returned to source or a payment request was rejected and not processed. | <DeclineReason> | Yes | See the [DeclineReason](Sub_Elements_and_Attributes.htm#Decline) sub-element |
| OrigTxnAmt | Original transaction amount. The value of the original transaction requested by the cardholder.  This is used where a transaction is a reversal. | <PartialAmount> | If Applicable | See the [OrigTxnAmt](Sub_Elements_and_Attributes.htm#OrigTxnA) sub-element |

#### Example

[Copy](javascript:void(0);)

```
<DeclinedAgencyBanking>  
    <CashType>RCP</CashType>  
    <BankingId>13962741416</BankingId>  
    <SettlementDate>20240213</SettlementDate>  
    <Card PAN="1132735542365123" MaskedPAN="113273******5123" product="MCRD" programid="ONEUKA"   
    productid="4368" branchcode="" />  
    <AgencyAccount no="273554236" type="01" sortcode="040083" bankacc="01665839" name="Daniel Velichkov" />  
    <External sortcode="TRWIBE" bankacc="P1508951" name="Daniel Velichkov" />  
    <CashCode direction="credit" CashType="fpy" CashGroup="rcp" />  
    <Desc> </Desc>  
    <CashAmt value="5.00" currency="826" />  
    <DeclineReason>00</DeclineReason>  
</DeclinedAgencyBanking>
```