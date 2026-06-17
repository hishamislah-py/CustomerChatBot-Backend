# 2.13 MasterCardFee

MasterCardFee records are used to describe non-card Mastercard Fees. They only appear in the transaction XML if the Mastercard [ICA![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Interbank Card Association Number (ICA) is a five-digit number assigned by MasterCard to a financial institution, third-party processor or other member to identify the member in the transaction.](#) is not shared between clients.

| Child Element | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| RecordType | Record type, used to distinguish between data types. | xs:string | Yes | See the [RecordType](Sub_Elements_and_Attributes.htm#RecordTy) sub-element. |
| MastercardFeeId | Unique identifier for this fee record. | xs:unsignedLong | Yes | 0 to 2^32. |
| MTID | Message Type Identifier. Takes values as supplied by Mastercard in the Chargeback Fee or Fee collection data | xs:unsignedint | Yes | Examples: 1442, 1644 and 1740.  See [Message Reason Codes](../Reference/Message_Reason_Codes.htm#4.5.2) |
| Function\_Code\_024 | Function Code for the fee record.  **Note**: This element is not applicable to the Discover Global Network. | <FunctionCode> | Yes | See the [FunctionCode](Sub_Elements_and_Attributes.htm#Function) sub-element. |
| Conversion\_Rate\_Reconciliation | Factor used in converting transaction amount to a reconciliation amount.  **Note**: This element is not applicable to the Discover Global Network. | xs:unsignedint | Yes | 0 to 2^32. |
| Additional\_Data\_048 | The additional data received from Mastercard.  **Note**: Not applicable to Discover Global Network. | xs:string | Yes | String. Refer to the Mastercard IPM Clearing Formats manual. |
| LocalDate | The date and time of the transaction in the local timezone. | <LocalDate> | Yes | See the [LocalDate](Sub_Elements_and_Attributes.htm#LocalDat) sub-element. |
| SettlementDate | The settlement date and time for the transaction. | <Settlement  Date> | No | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element. |
| FeeClass | Describes the derivation and nature of the fee. | <MasterCard  FeeClass> | Yes | For MasterCardFee records the FeeClass type=â0â, code=â0â and interchangeTransaction=ânoâ. |
| Desc | Fee description. This field may be empty. | <Desc> | No | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element. |
| FeeAmt | The fee amount as received from Mastercard.  **Note**: For a chargeback, this field provides details of any chargeback fees. For details of the chargeback amount, see <BillAmt> in the [CardChrgBackRepRes](CardChrgBackRepRes.htm#top) record. | <Direction  Amount> | Yes | See the [[FeeAmt](Sub_Elements_and_Attributes.htm#FeeAmt)](Sub_Elements_and_Attributes.htm#FeeAmt) sub-element. |
| Amt | The net transaction amount expressed in the original transaction currency, as advised by Mastercard. | <Direction  Amount> | Yes | See the [Amt](Sub_Elements_and_Attributes.htm#Amt) sub-element. |
| ReasonCode | Message reason code. | xs:string | Yes | See [Message Reason Codes.](../Reference/Message_Reason_Codes.htm) |
| Data\_Record\_072 | Free form text for Mastercard fee messages.  **Note**: This element is not applicable to the Discover Global Network. | xs:string | No | String, Refer to Mastercard IPM Clearing Formats Manual. |
| DE93\_Txn\_Dest\_ID | Identifies the transaction destination institution. | xs:string | Yes | Length 6 â 11 digits. |
| DE94\_Txn\_Orig\_ID | Identifies the transaction originator institution. | xs:string | No | Length 6 â 16 digits. |
| File\_ID\_PDS0105 | Identifies the logical data file exchanged between Thredd and the clearing system. | xs:string | Yes | See the [PDS0105](Sub_Elements_and_Attributes.htm#PDS0105) sub-element. |
| FileProcessDate | Date the Fee collection file was processed. | xs:string | Yes | In the format: YYYYMMDD HHMMSS. |
| Recon | Details of the reconciliation. | <Recon> | No | See the [Recon](Sub_Elements_and_Attributes.htm#Recon) sub-element. |
| Settlement | Details of the settlement. | <Settlement> | No | See the [Settlement](Sub_Elements_and_Attributes.htm#Settleme2) sub-element. |
| SettlementRecapID | Settlement Group identifier for Discover. | <SettlementRecapID> | If applicable | See [SettlementRecapID](Sub_Elements_and_Attributes.htm#SettlementRecapID) sub-element. |

#### Example

[Copy](javascript:void(0);)

```
<MasterCardFee>  
    <RecordType>FC</RecordType>  
    <MastercardFeeId>8285</MastercardFeeId>  
    <MTID>1740</MTID>  
    <Function_Code_024>783</Function_Code_024>  
    <Conversion_Rate_Reconciliation_009>1.000000</Conversion_Rate_Reconciliation_009>  
    <Additional_Data_048>013701766700000000000000014800497820158030MCC3050012   
    19011402    NNNNNN015906717053      33010001351899      
    1EU00000008N19011402190114010165001M01910012</Additional_Data_048>  
    <LocalDate>20170319000000</LocalDate>  
    <SettlementDate>20210121</SettlementDate>  
    <FeeClass interchangeTransaction="no" type="0" code="0" memberID="021212" />  
    <Desc>Clearing Issuer Master</Desc>  
    <FeeAmt value="4.85" currency="978" direction="debit" />  
    <Amt value="4.85" currency="978" direction="debit" />  
    <ReasonCode>7800</ReasonCode>  
    <Data_Record_072>MCBS - 0017053 E3 - Clearing Issuer Master  978 4.85 BILLING CYCLE DATE - JAN 13, 2019</Data_Record_072>  
    <DE93_Txn_Dest_ID>021212</DE93_Txn_Dest_ID>  
    <DE94_Txn_Orig_ID>003191</DE94_Txn_Orig_ID>  
    <File_ID_PDS0105>T112.0011901140000001705302201     </File_ID_PDS0105>  
    <FileProcessDate>20200120054648</FileProcessDate>  
    <Recon date="20200120" cycle="02" />  
    <Settlement date="20210121" cycle="01" />  
  </MasterCardFee>
```