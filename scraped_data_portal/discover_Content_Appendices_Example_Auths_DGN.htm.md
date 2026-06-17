## 9.14 Example Authorisations on Discover Cards

This page details examples of requests and responses for authorisations on Discover Global Network cards.

* [Authorisation Request](#Authoris)
* [Authorisation Advice (Auth Advice)](#Authoris2)

### 9.14.1 Authorisation Request

Below is an example of the HTTP POST body data for a Discover Global Network authorisation request.

Some key elements of this request are:

* The `MTID` value is 0100 and the `Txn_Type` is A, indicating that this is an Authorisation Request.
* The transaction is for Â£1. This is indicated by the `Bill_Amt` having a value of 1.0000 and the `Bill_Ccy` being set to 826 (for Great British Pounds).
* The `SendingAttemptCount` field checks to show whether this is a duplicate request. This will be zero for a first attempt.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
<s:Body>  
<GetTransaction xmlns="http://tempuri.org/">  
<Acquirer_id_DE32>00000361603</Acquirer_id_DE32>  
<ActBal>0.0000</ActBal>  
<Auth_Code_DE38>185405</Auth_Code_DE38>  
<Avl_Bal>0.0000</Avl_Bal>  
<Bill_Amt>3.0000</Bill_Amt>  
<Bill_Ccy>826</Bill_Ccy>  
<BlkAmt>0.0000</BlkAmt>  
<Cust_Ref/>  
<Fee_Rate>0.0000</Fee_Rate>  
<MCC_Code>7011</MCC_Code>  
<MCC_Pad>0.0000</MCC_Pad>  
<Merch_ID_DE42>MERCHANT 000001</Merch_ID_DE42>  
<Merch_Name_DE43>AMAZON MERCHANT\\LONDON\W2 61C 826</Merch_Name_DE43>  
<POS_Data_DE22>160090103000</POS_Data_DE22>  
<POS_Termnl_DE41>ECOMM001</POS_Termnl_DE41>  
<POS_Time_DE12>070725</POS_Time_DE12>  
<Proc_Code>000000</Proc_Code>  
<Resp_Code_DE39>00</Resp_Code_DE39>  
<Settle_Amt>3.0000</Settle_Amt>  
<Settle_Ccy>826</Settle_Ccy>  
<Token>116551735</Token>  
<Trans_link>6161750095</Trans_link>  
<Txn_Amt>3.0000</Txn_Amt>  
<Txn_CCy>826</Txn_CCy>  
<Txn_Ctry>GBR</Txn_Ctry>  
<Txn_Desc>AMAZON MERCHANT\\LONDON\W2 61C 826</Txn_Desc>  
<Txn_GPS_Date>2024-07-31 08:48:25.940</Txn_GPS_Date>  
<TXn_ID>6161750095</TXn_ID>  
<Txn_Stat_Code>A</Txn_Stat_Code>  
<TXN_Time_DE07>0731074825</TXN_Time_DE07>  
<Txn_Type>A</Txn_Type>  
<CU_Group>SPD-CU-010</CU_Group>  
<InstCode>PMT</InstCode>  
<MTID>0100</MTID>  
<ProductID>10051</ProductID>  
<SubBIN>0</SubBIN>  
<VL_Group>GPS-VL-004</VL_Group>  
<Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
<Expiry_Date>2410</Expiry_Date>  
<GPS_POS_Capability>01000000000100000000100000000000000000000000006</GPS_POS_Capability>  
<GPS_POS_Data>50V0000300000Nx000NNNNNU0UU9XXU</GPS_POS_Data>  
<traceid_lifecycle>DGN-20240731-014755045402703</traceid_lifecycle>  
<Merch_Name>AMAZON MERCHANT</Merch_Name>  
<Merch_Street/>  
<Merch_City>LONDON</Merch_City>  
<Merch_Region/>  
<Merch_Postcode>W2 61C</Merch_Postcode>  
<Merch_Country>GBR</Merch_Country>  
<POS_Date_DE13>2024-07-31</POS_Date_DE13>  
<Traceid_Message>DGN-20240731-014755045402703</Traceid_Message>  
<Acquirer_Country>GBR</Acquirer_Country>  
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>  
</GetTransaction>  
</s:Body>  
</s:Envelope>
```

#### Authorisation Response

Below is an example of HTTP response to the above Authorisation request message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>   
 <s:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransactionResponse xmlns="http://tempuri.org/">   
 <GetTransactionResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">   
 <Responsestatus>00</Responsestatus>   
 <CurBalance>0</CurBalance>   
 <AvlBalance>100</AvlBalance>   
 <Acknowledgement>1</Acknowledgement>   
 <LoadAmount>50</LoadAmount>   
 <Bill_Amt_Approved>0</Bill_Amt_Approved>   
 <Update_Balance>1</Update_Balance>   
 <New_Balance_Sequence_Exthost>200</New_Balance_Sequence_Exthost>   
 <CVV2_Result>M</CVV2_Result>   
 <CurBalance_GPS_STIP>0</CurBalance_GPS_STIP>   
 <AvlBalance_GPS_STIP>100</AvlBalance_GPS_STIP>   
 </GetTransactionResult>   
 </GetTransactionResponse>   
 </s:Body>   
 </s:Envelope>
```

[Back to Top](#Top)

### 9.14.2 Authorisation Advice (Auth Advice)

Below is an example of the HTTP POST body data for an Authorisation advice message.

Some key elements of this request are:

* The `MTID` value is 0120 and the Txn\_Type is J, indicating that this is Authorisation Advice matched to an Authorisation Request.
* This type of message is for EHI Mode 3 (Full Service Processing).
* The `Message_Source` value is set to MC-STIP, indicating that Discover Global Network Stand-In processing

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
<s:Body>  
<GetTransaction xmlns="http://tempuri.org/">  
<Acquirer_id_DE32>00000361603</Acquirer_id_DE32>  
<ActBal>0.0000</ActBal>  
<Auth_Code_DE38>185406</Auth_Code_DE38>  
<Avl_Bal>0.0000</Avl_Bal>  
<Bill_Amt>3.0000</Bill_Amt>  
<Bill_Ccy>826</Bill_Ccy>  
<BlkAmt>0.0000</BlkAmt>  
<Cust_Ref/>  
<Fee_Rate>0.0000</Fee_Rate>  
<MCC_Code>7011</MCC_Code>  
<MCC_Pad>0.0000</MCC_Pad>  
<Merch_ID_DE42>MERCHANT 000001</Merch_ID_DE42>  
<Merch_Name_DE43>AMAZON MERCHANT\\LONDON\W2 61C 826</Merch_Name_DE43>  
<POS_Data_DE22>160090103000</POS_Data_DE22>  
<POS_Termnl_DE41>ECOMM001</POS_Termnl_DE41>  
<POS_Time_DE12>070726</POS_Time_DE12>  
<Proc_Code>000000</Proc_Code>  
<Resp_Code_DE39>00</Resp_Code_DE39>  
<Settle_Amt>3.0000</Settle_Amt>  
<Settle_Ccy>826</Settle_Ccy>  
<Token>116551735</Token>  
<Trans_link>6161750096</Trans_link>  
<Txn_Amt>3.0000</Txn_Amt>  
<Txn_CCy>826</Txn_CCy>  
<Txn_Ctry>GBR</Txn_Ctry>  
<Txn_Desc>AMAZON MERCHANT\\LONDON\W2 61C 826</Txn_Desc>  
<Txn_GPS_Date>2024-07-31 08:48:26.985</Txn_GPS_Date>  
<TXn_ID>6161750096</TXn_ID>  
<Txn_Stat_Code>A</Txn_Stat_Code>  
<TXN_Time_DE07>0731074826</TXN_Time_DE07>  
<Txn_Type>J</Txn_Type>  
<CU_Group>SPD-CU-010</CU_Group>  
<InstCode>PMT</InstCode>  
<MTID>0120</MTID>  
<ProductID>10051</ProductID>  
<SubBIN>0</SubBIN>  
<VL_Group>GPS-VL-004</VL_Group>  
<Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
<Expiry_Date>2410</Expiry_Date>  
<GPS_POS_Capability>01000000000100000000100000000000000000000000006</GPS_POS_Capability>  
<GPS_POS_Data>50V0000300000Nx000NNNN0U0UU9NNN</GPS_POS_Data>  
<traceid_lifecycle>DGN-20240731-014755045402703</traceid_lifecycle>  
<Merch_Name>AMAZON MERCHANT</Merch_Name>  
<Merch_Street/>  
<Merch_City>LONDON</Merch_City>  
<Merch_Region/>  
<Merch_Postcode>W2 61C</Merch_Postcode>  
<Merch_Country>GBR</Merch_Country>  
<POS_Date_DE13>2024-07-31</POS_Date_DE13>  
<Traceid_Message>DGN-20240731-014755045402703</Traceid_Message>  
<Acquirer_Country>GBR</Acquirer_Country>  
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>  
</GetTransaction>  
</s:Body>  
</s:Envelope>
```

#### Authorisation Response (Auth Advice Response)

Below is an example of HTTP response to the above Authorisation advice message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>   
 <s:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransactionResponse xmlns="http://tempuri.org/">   
 <GetTransactionResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">   
 <Responsestatus>00</Responsestatus>   
 <CurBalance>0</CurBalance>   
 <AvlBalance>100</AvlBalance>   
 <Acknowledgement>1</Acknowledgement>   
 <LoadAmount>50</LoadAmount>   
 <Bill_Amt_Approved>0</Bill_Amt_Approved>   
 <Update_Balance>1</Update_Balance>   
 <New_Balance_Sequence_Exthost>200</New_Balance_Sequence_Exthost>   
 <CVV2_Result>M</CVV2_Result>   
 <CurBalance_GPS_STIP>0</CurBalance_GPS_STIP>   
 <AvlBalance_GPS_STIP>100</AvlBalance_GPS_STIP>   
 </GetTransactionResult>   
 </GetTransactionResponse>   
 </s:Body>   
 </s:Envelope>
```

[Back to Top](#Top)