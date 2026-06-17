# 2.4 JSON Data Types and EHI Fields

This section describes the data types of the fields in the JSON message. You should use these details together with the information on [Data Types](Data_Types.htm) for EHI GetTransaction messages.

The Request field values are case sensitive.

The EHI feed does not send JSON fields to externally-hosted systems where the values for the field data are blank. This is different from EHI feeds with XML fields where the feed can send blank values.

### Request Fields

| Field | JSON Data Type | Null Allowed | Compatible with  IEEE 754 binary-64 (double precision) ? |
| --- | --- | --- | --- |
| Acquirer\_id\_DE32 | String |  | N/A |
| ActBal | Number | Y | Y |
| Additional\_Amt\_DE54 | String |  | N/A |
| Amt\_Tran\_Fee\_DE28 | String |  | N/A |
| Auth\_Code\_DE38 | String |  | N/A |
| Avl\_Bal | Number | Y | Y |
| Bill\_Amt | Number | Y | Y |
| Bill\_Ccy | String |  | N/A |
| BlkAmt | Number | Y | Y |
| Cust\_Ref | String |  | N/A |
| FX\_Pad | Number | Y | Y |
| Fee\_Fixed | Number | Y | Y |
| Fee\_Rate | Number | Y | Y |
| LoadSRC | String |  | N/A |
| LoadType | String |  | N/A |
| MCC\_Code | String |  | N/A |
| MCC\_Desc | String |  | N/A |
| MCC\_Pad | Number | Y | Y |
| Merch\_ID\_DE42 | String |  | N/A |
| Merch\_Name\_DE43 | String |  | N/A |
| Note | String |  | N/A |
| POS\_Data\_DE22 | String |  | N/A |
| POS\_Data\_DE61 | String |  | N/A |
| POS\_Termnl\_DE41 | String |  | N/A |
| POS\_Time\_DE12 | String |  | N/A |
| Proc\_Code | String |  | N/A |
| Resp\_Code\_DE39 | String |  | N/A |
| Ret\_Ref\_No\_DE37 | String |  | N/A |
| Settle\_Amt | Number | Y | Y |
| Settle\_Ccy | String |  | N/A |
| Status\_Code | String |  | N/A |
| Token | Number | Y | Y |
| Trans\_link | String |  | N/A |
| Txn\_Amt | Number | Y | Y |
| Txn\_CCy | String |  | N/A |
| Txn\_Ctry | String |  | N/A |
| Txn\_Desc | String |  | N/A |
| Txn\_GPS\_Date | String |  | N/A |
| TXn\_ID | Number | Y | Y |
| Txn\_Stat\_Code | String |  | N/A |
| TXN\_Time\_DE07 | String |  | N/A |
| Txn\_Type | String |  | N/A |
| Additional\_Data\_DE48 | String |  | N/A |
| Authorised\_by\_GPS | String |  | N/A |
| AVS\_Result | String |  | N/A |
| CU\_Group | String |  | N/A |
| InstCode | String |  | N/A |
| MTID | String |  | N/A |
| ProductID | Number | Y | Y |
| Record\_Data\_DE120 | String |  | N/A |
| SubBIN | Number | Y | Y |
| TLogIDOrg | Number | Y | Y |
| VL\_Group | String |  | N/A |
| Dom\_Fee\_Fixed | Number | Y | Y |
| Non\_Dom\_Fee\_Fixed | Number | Y | Y |
| Fx\_Fee\_Fixed | Number | Y | Y |
| Other\_Fee\_Amt | Number | Y | Y |
| Fx\_Fee\_Rate | Number | Y | Y |
| Dom\_Fee\_Rate | Number | Y | Y |
| Non\_Dom\_Fee\_Rate | Number | Y | Y |
| Additional\_Data\_DE124 | String |  | N/A |
| CVV2 | String |  | N/A |
| Expiry\_Date | Number | Y | Y |
| PAN\_Sequence\_Number | Number | Y | Y |
| PIN | String |  | N/A |
| PIN\_Enc\_Algorithm | String |  | N/A |
| PIN\_Format | String |  | N/A |
| PIN\_Key\_Index | String |  | N/A |
| SendingAttemptCount | Number | Y | Y |
| source\_bank\_ctry | String |  | N/A |
| source\_bank\_account\_format | String |  | N/A |
| source\_bank\_account | String |  | N/A |
| dest\_bank\_ctry | String |  | N/A |
| dest\_bank\_account\_format | String |  | N/A |
| dest\_bank\_account | String |  | N/A |
| GPS\_POS\_Capability | String |  | N/A |
| GPS\_POS\_Data | String |  | N/A |
| Acquirer\_Reference\_Data\_031 | String |  | N/A |
| Response\_Source | String |  | N/A |
| Response\_Source\_Why | Number | Y | Y |
| Message\_Source | String |  | N/A |
| Message\_Why | Number | Y | Y |
| traceid\_lifecycle | String |  | N/A |
| Balance\_Sequence | Number | Y | N |
| Balance\_Sequence\_Exthost | Number | Y | N |
| PaymentToken\_id | Number | Y | Y |
| PaymentToken\_creator | String |  | N/A |
| PaymentToken\_expdate | String |  | N/A |
| PaymentToken\_type | String |  | N/A |
| PaymentToken\_status | String |  | N/A |
| PaymentToken\_creatorStatus | String |  | N/A |
| PaymentToken\_wallet | String |  | N/A |
| PaymentToken\_deviceType | String |  | N/A |
| PaymentToken\_lang | String |  | N/A |
| PaymentToken\_deviceTelNum | String |  | N/A |
| PaymentToken\_deviceIp | String |  | N/A |
| PaymentToken\_deviceId | String |  | N/A |
| PaymentToken\_deviceName | String |  | N/A |
| PaymentToken\_activationCode | String |  | N/A |
| PaymentToken\_activationExpiry | String |  | N/A |
| PaymentToken\_activationMethodData | String |  | N/A |
| PaymentToken\_activationMethod | Number | Y | Y |
| ICC\_System\_Related\_Data\_DE55  This field applies to both Visa and Mastercard. | String |  | N/A |
| Merch\_Name | String |  | N/A |
| Merch\_Street | String |  | N/A |
| Merch\_City | String |  | N/A |
| Merch\_Region | String |  | N/A |
| Merch\_Postcode | String |  | N/A |
| Merch\_Country | String |  | N/A |
| Merch\_Tel | String |  | N/A |
| Merch\_URL | String |  | N/A |
| Merch\_Name\_Other | String |  | N/A |
| Merch\_Net\_id | String |  | N/A |
| Merch\_Tax\_id | String |  | N/A |
| Merch\_Contact | String |  | N/A |
| auth\_type | String |  | N/A |
| auth\_expdate\_utc | String |  | N/A |
| Matching\_Txn\_ID | Number | Y | Y |
| Reason\_ID | Number | Y | Y |
| Dispute\_Condition | String |  | N/A |
| Network\_Chargeback\_Reference\_Id | String |  | N/A |
| Acquirer\_Forwarder\_ID | String |  | N/A |
| Currency\_Code\_Fee | String |  | N/A |
| Currency\_Code\_Fee\_Settlement | String |  | N/A |
| Interchange\_Amount\_Fee | Number | Y | Y |
| Interchange\_Amount\_Fee\_Settlement | Number | Y | Y |
| Clearing\_Process\_Date | String |  | N/A |
| Settlement\_Date | String |  | N/A |
| DCC\_Indicator | Number | Y | Y |
| multi\_part\_txn | Number | Y | Y |
| multi\_part\_txn\_final | Number | Y | Y |
| multi\_part\_number | Number | Y | Y |
| multi\_part\_count | Number | Y | Y |
| SettlementIndicator | String |  | N/A |
| Network\_TxnAmt\_To\_BillAmt\_Rate | String |  | N/A |
| Network\_TxnAmt\_To\_BaseAmt\_Rate | String |  | N/A |
| Network\_BaseAmt\_To\_BillAmt\_Rate | String |  | N/A |
| POS\_Date\_DE13 | String |  | N/A |
| Traceid\_Message | String |  | N/A |
| Traceid\_Original | String |  | N/A |
| Network\_Currency\_Conversion\_Date | String |  | N/A |
| Mastercard\_AdviceReasonCode\_DE60 | String |  | N/A |
| Network\_Original\_Data\_Elements\_DE90 | String |  | N/A |
| Visa\_ResponseInfo\_DE44 | String |  | N/A |
| Visa\_STIP\_Reason\_Code | String |  | N/A |
| Network\_Issuer\_Settle\_ID | String |  | N/A |
| Network\_Replacement\_Amounts\_DE95 | String |  | N/A |
| Visa\_POS\_Data\_DE60 | String |  | N/A |
| Network\_Transaction\_ID | String |  | N/A |
| Misc\_TLV\_Data | String |  | N/A |
| Acquirer\_Country | String |  | N/A |
| PaymentToken\_PanSource | String |  | N/A |
| ClearingFileID | String |  | N/A |
| Network\_Fraud\_Data | String |  | N/A |
| SenderData | String |  | N/A |
| ReceiverData | String |  | N/A |
| AuthenticationAmountUpper | Number | Y | Y |
| AuthenticationCurrency | String |  | N/A |
| AuthenticationMerchantHash | String |  | N/A |
| FxProviderCardholderRate | Number |  | Y |
| FxProviderBookedRate | Number |  | Y |

For more information on JSON data types, see the [RFC 8259 JSON specification](https://www.rfc-editor.org/rfc/rfc8259).

### Response Fields

| Field | JSON Data Type | Null Allowed | Compatible with  IEEE 754 binary-64 (double precision) ? |
| --- | --- | --- | --- |
| MerchantAdvice | String | Y | N/A |
| Responsestatus | String | Y | N/A |
| CurBalance | Number | Y | N/A |
| AvlBalance | Number | Y | N/A |
| Acknowledgement | String | Y | N/A |
| LoadAmount | Number | Y | N/A |
| Bill\_Amt\_Approved | Number | Y | N/A |
| Update\_Balance | Number | Y | N/A |
| New\_Balance\_Sequence\_Exthost | Number | Y | N/A |
| CVV2\_Result | String | Y | N/A |
| CurBalance\_GPS\_STIP | Number | Y | N/A |
| AvlBalance\_GPS\_STIP | Number | Y | N/A |

### Number range and precision

For each field of JSON data type *Number*, refer to the field description in [GetTransaction Message Fields](GetTransaction_Message.htm). which describes the field length range and maximum value you need to support. This is important to ensure no loss of information, especially for the fields with potentially large values.

Some of the above fields of JSON data type *Number* have a bigger range than the RFC 8259 data type of IEEE 754 binary-64 (double precision) which is described for numbers. If using the JavaScript language to process JSON, then for whole numbers (of Thredd data type *N(min.max)*) the JavaScript data type *bigint* would be a suitable alternative to the IEEE 754 binary-64 number data type.

#### Example

The `Matching_Txn_ID` field is a number of type N(1,16), with a minimum length of 1 digits and maximum length of 16 digits. Your systems must be able to handle a value containing up to 16 digits.

####