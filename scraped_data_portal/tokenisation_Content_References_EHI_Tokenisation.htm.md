# Appendix C: EHI Tokenisation Fields

The table below lists the EHI message fields relevant to the tokenisation service.

| Field | Description |
| --- | --- |
| PaymentToken\_id | Unique Thredd token reference. |
| PaymentToken\_creator | The token service provider (Mastercard or Visa). |
| PaymentToken\_expdate | The expiry date of the token. |
| PaymentToken\_type | The payment token type. Defines the technology the token is being held on. |
| PaymentToken\_status | Indicates the status of the token. Please note, this can differ from the status of the PAN. |
| PaymentToken\_creatorStatus | Indicates the status as set by the token service provider (Mastercard/Visa) and also on the device itself. This adds information around the progress of token setup along with whether a post-setup token is active or not. This field can contain â â or be empty when no value has been provided. |
| PaymentToken\_wallet | The wallet provider (e.g., Apple Pay, Google Pay) the token is linked to. |
| PaymentToken\_deviceType | The type of device the token is linked to (e.g., Mobile Phone, watch, tablet). |
| PaymentToken\_lang | The language configured on the device linked to the token (if available). |
| PaymentToken\_deviceTelNum | The telephone number of the device linked to the token. |
| PaymentToken\_deviceIp | The IP address of the device linked to the token. |
| PaymentToken\_deviceId | The device ID of the device linked to the token. (Also called the DE124 Payment Application Instance Id at Mastercard and SEIDs (Secure element ID) at Apple.) |
| PaymentToken\_deviceName | The name of the device linked to the token. |
| PaymentToken\_activationCode | The token activation code. |
| PaymentToken\_activationExpiry | The token activation expiry date. |
| PaymentToken\_activationMethod | The token activation method (e.g., 0=none; 1 = SMS) |
| PaymentToken\_activationMethodData | The token activation method details (e.g., if the activation method is 1 for SMS, then provides the mobile phone number to send the SMS). |

For more information, refer to the [EHI Guide](https://docs.thredd.ai/EHI_Guide.htm).

## Example EHI TAR (330000) Message (XML)

The example below shows a typical EHI 0100 authorisation message for a Token Authorisation Request (TAR) in an XML format.  Your systems need to respond to tokenisation messages with an acknowledgement. For more information, refer to the [EHI XML Guide](https://docs.thredd.ai/EHI_Guide.htm).

Empty fields have been removed from this example.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
   <s:Body>  
      <GetTransaction xmlns="http://tempuri.org/">  
         <Acquirer_id_DE32>06001234</Acquirer_id_DE32>  
         <ActBal>0.00</ActBal>  
           â¦â¦..  
           <MCC_Code>6012</MCC_Code>  
         <MCC_Desc>Financial Institutions</MCC_Desc>  
         <MCC_Pad>0.00</MCC_Pad>  
         <Merch_ID_DE42>400425000000001</Merch_ID_DE42>  
         <Merch_Name_DE43> Visa Tokenisation System Foster City US </Merch_Name_DE43>            
         <Proc_Code>330000</Proc_Code>  
         <Resp_Code_DE39>00</Resp_Code_DE39>  
         <Ret_Ref_No_DE37>102300045678</Ret_Ref_No_DE37>  
         â¦â¦â¦.           
         <Txn_Desc>Visa Provisioning Service GB</Txn_Desc>  
         <Txn_GPS_Date>2021-03-18 15:08:14.650</Txn_GPS_Date>  
         <TXn_ID>1250779057</TXn_ID>  
         <Txn_Stat_Code>A</Txn_Stat_Code>  
         <TXN_Time_DE07>0318150814</TXN_Time_DE07>  
         <Txn_Type>A</Txn_Type>  
         <Additional_Data_DE48 />  
         <Authorised_by_GPS>Y</Authorised_by_GPS>  
         <AVS_Result>Y</AVS_Result>  
         <CU_Group>TST-CU-001</CU_Group>  
         <InstCode>TST</InstCode>  
         <MTID>0100</MTID>  
         <ProductID>5877</ProductID>  
         <Record_Data_DE120 />  
         <SubBIN>45967201</SubBIN>  
         <TLogIDOrg>0</TLogIDOrg>  
         <VL_Group>TST-VL-001</VL_Group>  
         <Dom_Fee_Fixed>0.00</Dom_Fee_Fixed>  
         <Non_Dom_Fee_Fixed>0.00</Non_Dom_Fee_Fixed>  
         <Fx_Fee_Fixed>0.00</Fx_Fee_Fixed>  
         <Other_Fee_Amt>0.00</Other_Fee_Amt>  
         <Fx_Fee_Rate>0.00</Fx_Fee_Rate>  
         <Dom_Fee_Rate>0.00</Dom_Fee_Rate>  
         <Non_Dom_Fee_Rate>0.00</Non_Dom_Fee_Rate>  
         â¦â¦..  
         <Expiry_Date>2304</Expiry_Date>  
         â¦â¦â¦  
         <SendingAttemptCount>0</SendingAttemptCount>  
          â¦â¦..           
         <GPS_POS_Capability>0000000000000000000000000000000000100000000990010</GPS_POS_Capability>  
         <GPS_POS_Data>9908000800000Nx000</GPS_POS_Data>  
         â¦â¦.  
         <Response_Source_Why>0</Response_Source_Why>  
         <Message_Source />  
         <Message_Why>71</Message_Why>  
         <traceid_lifecycle>VIS1-20210318-381077544887139</traceid_lifecycle>  
         <PaymentToken_id>12365432</PaymentToken_id>  
         <PaymentToken_creator>VISA-T</PaymentToken_creator>  
         <PaymentToken_expdate />  
         <PaymentToken_type>SE</PaymentToken_type>  
         <PaymentToken_status>00</PaymentToken_status>  
         <PaymentToken_creatorStatus />  
         <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
         <PaymentToken_deviceType>W</PaymentToken_deviceType>  
         <PaymentToken_lang>en</PaymentToken_lang>  
         <PaymentToken_deviceTelNum>447912345678</PaymentToken_deviceTelNum>  
         <PaymentToken_deviceIp>192.0.0.8</PaymentToken_deviceIp>  
         <PaymentToken_deviceId>01234B234C1230011230054848300695D86E17C703548A4A</PaymentToken_deviceId>  
         <PaymentToken_deviceName>Test Apple Wa</PaymentToken_deviceName>  
         <PaymentToken_activationCode />  
         <PaymentToken_activationExpiry />  
         <PaymentToken_activationMethodData />  
         <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
         â¦â¦â¦â¦.        
</GetTransaction>  
   </s:Body>  
</s:Envelope>
```

## Example EHI TAR (330000) Message (JSON)

The example below shows a typical EHI 0100 authorisation message for a Token Authorisation Request (TAR) in a JSON format. For more information, refer to the [EHI JSON Guide](https://docs.thredd.ai/EHI_Guide_JSON.htm).

[Copy](javascript:void(0);)

```
{  
  "PaymentToken_PanSource": "F",  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.000000000,  
  "Network_TxnAmt_To_BillAmt_Rate": "7849290:7",  
  "POS_Date_DE13": "0000-00-00",  
  "Traceid_Message": "BNET-20240604-MDWWKZ1AT",  
  "Network_Currency_Conversion_Date": "2024-06-04",  
  "Network_Transaction_ID": "MDWWKZ1AT0604",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2024-06-12 01:00:01.307",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "Klarna-EU",  
  "Merch_City": "St. Louis",  
  "Merch_Postcode": "63368",  
  "Merch_Country": "USA",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000230010",  
  "GPS_POS_Data": "5018000800000Nx000",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20240604-MDWWKZ1AT",  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": "N",  
  "PaymentToken_wallet": "MRCHTOKEN",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "06015611",  
  "ActBal": 0.00,  
  "Auth_Code_DE38": "117574",  
  "Avl_Bal": 0.00,  
  "Bill_Amt": 0.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.00,  
  "Cust_Ref": "49538776",  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "5969",  
  "MCC_Desc": "Direct Marketing - Other",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "CARD ACCPT IDC",  
  "Merch_Name_DE43": "Klarna-EU              St. Louis     USA",  
  "Note": "DR: Declined due to Card Status: Card Destroyed (Original status 83, changed to 05) ",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "102510900000084063368",  
  "Proc_Code": "330000",  
  "Resp_Code_DE39": "57",  
  "Settle_Amt": 0.00,  
  "Settle_Ccy": "826",  
  "Status_Code": "83",  
  "Token": 138602839,  
  "Trans_link": "240605048358015611",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "840",  
  "Txn_Ctry": "USA",  
  "Txn_Desc": "Klarna-EU              St. Louis     USA",  
  "Txn_GPS_Date": "2024-06-05 02:00:01.410",  
  "TXn_ID": 14419002829,  
  "Txn_Stat_Code": "I",  
  "TXN_Time_DE07": "0605010001",  
  "Txn_Type": "A",  
  "Additional_Data_DE48": "063T260332733260101H06115019291999808020375130103001020291710418C ",  
  "Authorised_by_GPS": "Y",  
  "CU_Group": "PMT-CU-002",  
  "InstCode": "PMT",  
  "MTID": "0100",  
  "ProductID": 3004,  
  "SubBIN": 53759000,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-020",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "Additional_Data_DE124": "195TAD00162036556451                                                                                                                                                       1                         C",  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## Additional EHI Message Examples (JSON)

The examples below, in JSON format, are for indicative purposes only.

### ACN (340000) Message

[Copy](javascript:void(0);)

```
{  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "0000-00-00",  
  "Traceid_Message": "BNET-20240603-BPD83TR98",  
  "Network_Currency_Conversion_Date": "2024-06-03",  
  "Network_Transaction_ID": "BPD83TR980603",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2024-06-11 02:37:56.380",  
  "Merch_Name": "APPLE PAY",  
  "Merch_City": "St. Louis",  
  "Merch_Postcode": "63368",  
  "Merch_Country": "USA",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000230010",  
  "GPS_POS_Data": "5018000800000Nx000NNNNNM0NUUXXU",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20240603-BPD83TR98",  
  "Balance_Sequence": 0,  
  "Balance_Sequence_Exthost": 0,  
  "PaymentToken_id": 72322899,  
  "PaymentToken_creator": "MC-MDES",  
  "PaymentToken_type": "SE",  
  "PaymentToken_status": "00",  
  "PaymentToken_creatorStatus": "N",  
  "PaymentToken_wallet": "APPLE",  
  "PaymentToken_deviceType": "M",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_deviceIp": "4E916C0C",  
  "PaymentToken_deviceId": "01234567891790022199036150316380EEB395872B0AC6ED",  
  "PaymentToken_activationCode": "169961",  
  "PaymentToken_activationExpiry": "2024-06-04 05:37:00.000",  
  "PaymentToken_activationMethodData": "+447880646031",  
  "PaymentToken_activationMethod": 1,  
  "Acquirer_id_DE32": "06015611",  
  "ActBal": 0.0000,  
  "Auth_Code_DE38": "152085",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5969",  
  "MCC_Desc": "Direct Marketing - Other",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "CARD ACCPT IDC",  
  "Merch_Name_DE43": "APPLE PAY St. Louis     USA",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "102510900000084063368",  
  "Proc_Code": "340000",  
  "Resp_Code_DE39": "00",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 335635281,  
  "Trans_link": "240604612291015611",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "840",  
  "Txn_Ctry": "USA",  
  "Txn_Desc": "APPLE PAY St. Louis     USA",  
  "Txn_GPS_Date": "2024-06-04 03:37:56.518",  
  "TXn_ID": 14414319424,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "0604023756",  
  "Txn_Type": "J",  
  "Additional_Data_DE48": "063T230221260310333200101C06115011003027375130103001020291710418C ",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-001",  
  "InstCode": "PMT",  
  "MTID": "0120",  
  "ProductID": 4252,  
  "SubBIN": 51694000,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-001",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "Additional_Data_DE124": "048ACD0015151049206169961  24060405371#########6031",  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{"Responsestatus":"00","CurBalance":0.0,"AvlBalance":0.0,"Acknowledgement":1,"LoadAmount":0.0,"Bill_Amt_Approved":0.0,"Update_Balance":0,"New_Balance_Sequence_Exthost":0,"CVV2_Result":"","AvlBalance_GPS_STIP":0.0,"CurBalance_GPS_STIP":0.0}
```

### TCN (350000) Message

[Copy](javascript:void(0);)

```
{  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "0000-00-00",  
  "Traceid_Message": "BNET-20240603-BPDR46YHK",  
  "Network_Currency_Conversion_Date": "2024-06-03",  
  "Network_Transaction_ID": "BPDR46YHK0603",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2024-06-11 01:01:20.030",  
  "Merch_Name": "APPLE PAY",  
  "Merch_City": "St. Louis",  
  "Merch_Postcode": "63368",  
  "Merch_Country": "USA",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000230010",  
  "GPS_POS_Data": "5018000800000Nx000NNNNNM0NUUXXU",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20240603-BPDR46YHK",  
  "Balance_Sequence": 0,  
  "Balance_Sequence_Exthost": 0,  
  "PaymentToken_id": 72322246,  
  "PaymentToken_creator": "MC-MDES",  
  "PaymentToken_expdate": "2027-07-31",  
  "PaymentToken_type": "SE",  
  "PaymentToken_status": "00",  
  "PaymentToken_creatorStatus": "A",  
  "PaymentToken_wallet": "APPLE",  
  "PaymentToken_deviceType": "M",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_deviceTelNum": "7181",  
  "PaymentToken_deviceIp": "97E3830C",  
  "PaymentToken_deviceId": "0123456789E5C80020103080645305102E616B5CB01EB3DD6",  
  "PaymentToken_deviceName": "Stephanie's phone (3",  
  "Acquirer_id_DE32": "06015611",  
  "ActBal": 0.0000,  
  "Auth_Code_DE38": "166647",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5969",  
  "MCC_Desc": "Direct Marketing - Other",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "CARD ACCPT IDC",  
  "Merch_Name_DE43": "APPLE PAY St. Louis USA",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "102510900000084063368",  
  "Proc_Code": "350000",  
  "Resp_Code_DE39": "00",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 374414990,  
  "Trans_link": "240604229542015611",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "840",  
  "Txn_Ctry": "USA",  
  "Txn_Desc": "APPLE PAY St. Louis USA",  
  "Txn_GPS_Date": "2024-06-04 02:01:20.142",  
  "TXn_ID": 14414251623,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "0604010119",  
  "Txn_Type": "J",  
  "Additional_Data_DE48": "097T230221260310333540101C021653724083642754730304270706115011003027308020575130103001020291710418C ",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-001",  
  "InstCode": "PMT",  
  "MTID": "0620",  
  "ProductID": 4252,  
  "SubBIN": 51694000,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-001",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "Additional_Data_DE124": "192TCD001514838250601ZILCHCONS enStephanie's phone (31269d868a6a0394114a347cfef4ee0901e24060401010DAPLMC000026259835f4ba50cdd94aea8725b3beedde4545FAPLMC00002625988947bff5eb134ffcae9822bf49031d09S",  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{"Responsestatus":"00","CurBalance":0.0,"AvlBalance":0.0,"Acknowledgement":1,"LoadAmount":0.0,"Bill_Amt_Approved":0.0,"Update_Balance":0,"New_Balance_Sequence_Exthost":0,"CVV2_Result":"","AvlBalance_GPS_STIP":0.0,"CurBalance_GPS_STIP":0.0}
```

### TEN (360000) Message

[Copy](javascript:void(0);)

```
{  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "0000-00-00",  
  "Traceid_Message": "BNET-20240603-BPDH0UE75",  
  "Network_Currency_Conversion_Date": "2024-06-03",  
  "Network_Transaction_ID": "BPDH0UE750603",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2024-06-11 01:00:16.001",  
  "Merch_Name": "Visa Provisioning Service",  
  "Merch_City": "St. Louis",  
  "Merch_Postcode": "63368",  
  "Merch_Country": "USA",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000230010",  
  "GPS_POS_Data": "5018000800000Nx000NNNNNM0NUUXXU",  
  "Response_Source_Why": 0,  
  "Message_Source": "CRDHLR",  
  "Message_Why": 51,  
  "traceid_lifecycle": "VIS1-20240604-304156486459325",  
  "Balance_Sequence": 0,  
  "Balance_Sequence_Exthost": 0,  
  "PaymentToken_id": 58098832,  
  "PaymentToken_creator": "Visa-T",  
  "PaymentToken_expdate": "2026-03-31",  
  "PaymentToken_type": "SE",  
  "PaymentToken_status": "00",  
  "PaymentToken_creatorStatus": "D",  
  "PaymentToken_wallet": "APPLE",  
  "PaymentToken_deviceType": "M",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_deviceTelNum": "1504",  
  "PaymentToken_deviceIp": "94FC8598",  
  "PaymentToken_deviceId": "01234567896A8002119909991631144010A4926E8D6D1C36",  
  "PaymentToken_deviceName": "iPhone",  
  "Acquirer_id_DE32": "06015611",  
  "ActBal": 0.0000,  
  "Auth_Code_DE38": "161404",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5969",  
  "MCC_Desc": "Direct Marketing - Other",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "CARD ACCPT IDC",  
  "Merch_Name_DE43": "Visa Provisioning Service FR",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "102510900000084063368",  
  "Proc_Code": "360000",  
  "Resp_Code_DE39": "00",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 155027420,  
  "Trans_link": "240604919020015611",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "840",  
  "Txn_Ctry": "USA",  
  "Txn_Desc": "Visa Provisioning Service FR",  
  "Txn_GPS_Date": "2024-06-04 02:00:16.121",  
  "TXn_ID": 14414250789,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "0604010015",  
  "Txn_Type": "J",  
  "Additional_Data_DE48": "091T230221260310333480101C021653724083932605950304260306115011003027375130103001020291710418C ",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-001",  
  "InstCode": "PMT",  
  "MTID": "0620",  
  "ProductID": 4252,  
  "SubBIN": 51694000,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-001",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "Additional_Data_DE124": "068TVD00067408479624  2DAPLMC000026259862dc013463464968ac77488b5bd11e9d",  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{"Responsestatus":"00","CurBalance":0.0,"AvlBalance":0.0,"Acknowledgement":1,"LoadAmount":0.0,"Bill_Amt_Approved":0.0,"Update_Balance":0,"New_Balance_Sequence_Exthost":0,"CVV2_Result":"","AvlBalance_GPS_STIP":0.0,"CurBalance_GPS_STIP":0.0}
```