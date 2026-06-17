# 2.4 CardFee

The CardFee primary element describes Card Fee records. The FeeClass child element, as described below, distinguishes between the permissible types.

The CardFee element is present in both Clearing Reports and Non-Clearing Reports. The Clearing report contains any interchange fees and the Non-Clearing report contains any non-interchange fees. For details, the [FeeClass](Sub_Elements_and_Attributes.htm#FeeClas) sub-element.

**Note**: This element is not applicable to the Discover Global Network.

| Child Element | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| CardFeeId | Identifier for a CardFee record. Note that if there is a non-domestic fee and an FX fee on the same transaction, they share the same `CardFeeId`. | xs:unsignedLong | Yes | 0 to 2^64 |
| LocalDate | The date and time the terminal (POS or ATM) or acquirer generates the record in the local timezone. | <LocalDate> | Yes | See the [LocalDate](Sub_Elements_and_Attributes.htm#LocalDat) sub-element |
| SettlementDate | The date when the transaction has been processed. | <Settlement  Date> | Yes | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element |
| Card | Provides details of the card related to the fee. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| Account | Provides details of the cardholder account related to the fee. | <Account> | Yes | See the [Account](Sub_Elements_and_Attributes.htm#Account) sub-element |
| TxId | If applicable, the *FinId* of the related *CardFinancial* (transaction) record for this CardFee record (foreign key).  For Fee Collection rrecords, it shows the *AuthId* of the related *CardAuthorisation* record (if found)  If a matching *CardAuthorisation* or *CardFinancial* record cannot be found, the Id shows as *0*. | xs:unsignedLong | Yes | 0 to 2^64  If not applicable, use default value 0 |
| TxnCode | Indicates the type of transaction. | <TxnCode> | No | See the  [TxnCode](Sub_Elements_and_Attributes.htm#TxnCode) sub-element |
| MerchCode | A unique code identifying the merchant (also known as the *Card Acceptor Identifier*) | <MerchCode> | No | See the [MerchCode](Sub_Elements_and_Attributes.htm#MerchCod) sub-element |
| MsgSource | Describes the derivative source of the record. | <MsgSource> | No | See the [MsgSource](Sub_Elements_and_Attributes.htm#MsgSourc) sub-element |
| FeeClass | Describes the derivation and nature of the fee. | <FeeClass> | Yes | See the [FeeClass](Sub_Elements_and_Attributes.htm#FeeClas) sub-element |
| LoadUnloadId | If applicable the LoadUnloadId of the related CardLoadUnload record for this CardFee Record (foreign key). | xs:unsignedLong | No | 0 to 2^64 |
| Desc | Fee description. | <Desc> | Yes | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element |
| FeeAmt | The FeeAmt represents the fee amount. This has the following behaviour:   * When FeeClass type is 1 then it is the fee amount for a Card Load, Expiry, Recurring payment, FX, SMS, Domestic or non-Domestic Fee as set up by the Programme Manager. * When FeeClass type is 4 or 5 then it is a Scheme fee, such as an Interchange, Chargeback or ATM Fee Collection Fee from the Scheme. | <Direction  Amount> | No | See the  [FeeAmt](Sub_Elements_and_Attributes.htm#FeeAmt) sub-element |
| Amt | This amount is described as follows:   * For Scheme fees (see [FeeClass:](Sub_Elements_and_Attributes.htm#FeeClas) type = 2, 4 and 5), this is the settlement amount posted to the settlement account. * When the fee is NOT a Settlement (see [FeeClass](Sub_Elements_and_Attributes.htm#FeeClas): type = 1), this is the fee billed (posted) to the cardholder's account. | <Direction  Amount> | Yes | See the [Amt](Sub_Elements_and_Attributes.htm#Amt) sub-element  When a fee is levied against the cardholder, the normal direction is: âdebitâ for FeeClass type =1,2 & 5  âcreditâ for FeeClass Type = 4 |
| FIID | Forwarding Institution identification code. | <FIID> | No | See the [FIID](Sub_Elements_and_Attributes.htm#FIID) sub-element |
| ReasonCode | Message reason code. | xs:string | Yes | Only applicable for settlement  See [Message\_Reason\_Codes.htm](../Reference/Message_Reason_Codes.htm)  For Fees, see the [FeeClass](Sub_Elements_and_Attributes.htm#FeeClas) sub-element |
| Recon | Details of the reconciliation. | <Recon> | No | See the [Recon](Sub_Elements_and_Attributes.htm#Recon) sub-element |

#### Non-Clearing Report Example

[Copy](javascript:void(0);)

```
<CardFee>  
    <CardFeeId>13961469923</CardFeeId>  
    <LocalDate>20240213033057</LocalDate>  
    <SettlementDate>20240213</SettlementDate>  
    <Card PAN="1132466665781123" MaskedPAN="113246******1123" product="MCRD" programid="ONEUKA"   
    productid="4368" branchcode="00000000" />  
    <Account no="246666578" type="01" />  
    <TxId>13961469923</TxId>  
    <FeeClass interchangeTransaction="no" type="1" code="1000" />  
    <LoadUnloadId>0</LoadUnloadId>  
    <Desc>CCB ATM A5600225       DOLNA BANYA   BGR</Desc>  
    <FeeAmt value="0.50" currency="826" direction="debit" />  
    <Amt value="0.50" currency="826" direction="debit" />  
    <ReasonCode />  
  </CardFee>
```

#### Clearing Report Example

[Copy](javascript:void(0);)

```
  <CardFee>  
    <CardFeeId>843249</CardFeeId>  
    <LocalDate>20190326000000</LocalDate>  
    <SettlementDate>20200103</SettlementDate>  
    <Card PAN="8062328177229342" MaskedPAN="806232******9342" product="VISA" programid="GPS"   
    productid="9815" branchcode="00000000" />  
    <Account no="232817722" type="02" />  
    <TxId>3762429334</TxId>  
    <FeeClass interchangeTransaction="no" type="1" code="1000" />  
    <LoadUnloadId>0</LoadUnloadId>  
    <Desc>Domestic Fee</Desc>  
    <FeeAmt value="5.00" currency="826" direction="debit" />  
    <Amt value="5.00" currency="826" direction="debit" />  
    <ReasonCode />  
    <Recon date="20191205" cycle="05" />  
  </CardFee>
```