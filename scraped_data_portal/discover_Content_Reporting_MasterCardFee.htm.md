## 9.8 MasterCardFee

MasterCardFee records are used to describe non-card Mastercard Fees. They only appear in the transaction XML if the Mastercard [ICA![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.](#) is not shared between clients.

| Child Element | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| RecordType | Record type, used to distinguish between data types. | xs:string | Yes | See the [RecordType](Sub_Elements_and_Attributes.htm#RecordTy) sub-element. |
| MastercardFeeId | Unique identifier for this fee record. | xs:unsignedint | Yes | 0 to 2^32. |
| MTID | Message Type Identifier. Takes values as supplied by Mastercard in the Chargeback Fee or Fee collection data. | xs:unsignedint | Yes | Examples: 1442, 1644 and 1740.  See [Message Reason Codes](../Appendices/Message_Reason_Codes.htm) |
| Function\_Code\_024 | Function Code for the fee record.  Not applicable to Discover. | <FunctionCode> | Yes | See the [FunctionCode](Sub_Elements_and_Attributes.htm#Function) sub-element. |
| Conversion\_Rate\_Reconciliation | Factor used in converting transaction amount to a reconciliation amount.  Not applicable to Discover. | xs:unsignedint | Yes | 0 to 2^32. |
| Additional\_Data\_048 | The additional data received from Mastercard.  Not applicable to Discover. | xs:string | Yes | String. Refer to the Mastercard IPM Clearing Formats manual. |
| LocalDate | The local date and time of the transaction. | <LocalDate> | Yes | See the [LocalDate](Sub_Elements_and_Attributes.htm#LocalDat) sub-element. |
| SettlementDate | The settlement date and time for the transaction. | <Settlement  Date> | Optional | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element. |
| FeeClass | Describes the derivation and nature of the fee. | <MasterCard  FeeClass> | Yes | For MasterCardFee records the FeeClass type=â0â, code=â0â and interchangeTransaction=ânoâ. |
| Desc | Fee description. This field may be empty. | <Desc> | Optional | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element. |
| FeeAmt | The fee amount as received from Mastercard.  **Note**: For a chargeback, this field provides details of any chargeback fees. For details of the chargeback amount, see <BillAmt> in the [CardChrgBackRepRes](CardChrgBackRepRes.htm#top) record. | <Direction  Amount> | Yes | See the [[FeeAmt](Sub_Elements_and_Attributes.htm#FeeAmt)](Sub_Elements_and_Attributes.htm#FeeAmt) sub-element. |
| Amt | The net transaction amount expressed in the original transaction currency, as advised by Mastercard. | <Direction  Amount> | Yes | See the [Amt](Sub_Elements_and_Attributes.htm#Amt) sub-element. |
| ReasonCode | Message reason code. | xs:string | Yes | See [Message Reason Codes.](../Appendices/Message_Reason_Codes.htm) |
| Data\_Record\_072 | Free form text for Mastercard fee messages.  Not applicable to Discover. | xs:string | Optional | String, Refer to Mastercard IPM Clearing Formats Manual. |
| DE93\_Txn\_Dest\_ID | Identifies the transaction destination institution. | xs:string | Yes | Length 6 â 11 digits. |
| DE94\_Txn\_Orig\_ID | Identifies the transaction originator institution. | xs:string | Optional | Length 6 â 16 digits. |
| File\_ID\_PDS0105 | Identifies the logical data file exchanged between Thredd and the clearing system. | xs:string | Yes | See the [PDS0105](Sub_Elements_and_Attributes.htm#PDS0105) sub-element. |
| FileProcessDate | Date the Fee collection file was processed. | xs:string | Yes | In the format: YYYYMMDD HHMMSS. |
| Recon | Details of the reconciliation. | <Recon> | Optional | See the [Recon](Sub_Elements_and_Attributes.htm#Recon) sub-element. |
| Settlement | Details of the settlement. | <Settlement> | Optional | See the [Settlement](Sub_Elements_and_Attributes.htm#Settleme) sub-element. |
| SettlementRecapID | Settlement Group identifier for Discover. | <SettlementRecapID> | If applicable | See [SettlementRecapID](Sub_Elements_and_Attributes.htm#Settleme6) sub-element. |

#### Example

[Copy](javascript:void(0);)

```
<MasterCardFee>  
    <RecordType>DGN</RecordType>  
    <MastercardFeeId>30230566</MastercardFeeId>  
    <MTID>1740</MTID>  
    <Function_Code_024 />  
    <Conversion_Rate_Reconciliation_009 />  
    <Additional_Data_048 / >  
    <LocalDate>20240531</LocalDate>  
    <SettlementDate>20240531</SettlementDate>  
    <FeeClass interchangeTransaction="no" type="0" code="0" memberID="00000361662" />  
    <Desc>Disputes Processing Fee</Desc>   
    <FeeAmt value="10.00" currency="840" direction="debit" />  
    <Amt value="10.98" currency="978" direction=" debit" />  
    <ReasonCode>FV</ReasonCode>  
    <Data_Record_072> />  
    <DE93_Txn_Dest_ID>00000361662</DE93_Txn_Dest_ID>  
    <DE94_Txn_Orig_ID>00000361641</DE94_Txn_Orig_ID>  
    <File_ID_PDS0105> I7.EXCHQ.20240531.N000001</File_ID_PDS0105>  
    <FileProcessDate>20240531010716</FileProcessDate>  
    <Recon date="20240531" cycle="01" />  
    <Settlement date="20240531" cycle="01" />  
    <SettlementRecapId RecapDate="20240531" RecapNumber="093" SendingIIC="00000361641" ReceivingIIC="00000361603" CurrencyCode="826" />  
</MasterCardFee>
```