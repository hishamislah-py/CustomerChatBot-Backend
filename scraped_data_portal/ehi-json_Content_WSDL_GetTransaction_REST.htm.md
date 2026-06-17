# 3.1 GetTransaction Example Messages

This section provides examples of common transaction messages and responses. This section includes these topics:

* [Example Authorisation](#Example2)
* [Example Authorisation Reversal](#Example3)
* [Example Financial Presentment (Mastercard)](#Example4)
* [Example Second Financial Presentment (Mastercard)](#Example5)
* [Example Financial Reversal (Visa)](#Example6)
* [Example Financial Reversal (Mastercard)](#Financia)
* [Example Visa Authorisation Advice](#Example6b)
* [Example Mastercard Authorisation Advice](#Example7)
* [Example Non-Credit Chargeback Notification (Mastercard)](#Example8)
* [Example Chargeback Notification (Mastercard)](#ChargebackNo)
* [Example Chargeback Reversal (Mastercard)](#ChargebackRever)
* [Example Balance Enquiry Message](#Example9)
* [Example ATM Cash Withdrawal Messages (Mastercard)](#ExampleATM)
* [Example Tokenisation Messages](#Example8b)
* [Example Incremental Authorisation Messages](#Example11)
* [Examples of Amount Sign](#Examples)

EHI\_JSON\_Guide\_5.5 The EHI feed does not send JSON fields to externally-hosted systems where the values for the field data are blank. This is different from EHI feeds with XML fields where the feed can send blank values.

## 3.1.1 Example Authorisations

### Authorisation Request

Below is an example of the HTTP POST body data for an authorisation request.

[Copy](javascript:void(0);)

```
{  
  "Acquirer_Country": "GBR",  
  "FxProviderCardholderRate": 0.0,  
  "POS_Date_DE13": "00000000",  
  "Traceid_Message": "VIS1-20221219-002353117950020",  
  "Visa_POS_Data_DE60": "020000000000",  
  "Network_Transaction_ID": "0002353117950020",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2022-12-27 07:28:36.045",  
  "Merch_Name": "Travel Like A Pro",  
  "Merch_Country": "HRV",  
  "GPS_POS_Capability": "00001001000000000000000100010010001000000001130C0",  
  "GPS_POS_Data": "9968000800000Nx000NNNNNU0NUUXXU",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "VIS1-20221219-002353117950020",  
  "Balance_Sequence": 114,  
  "Balance_Sequence_Exthost": 0,  
  "Acquirer_id_DE32": "0844622180",  
  "ActBal": 10001.0000,  
  "Auth_Code_DE38": "143088",  
  "Avl_Bal": 10001.0000,  
  "Bill_Amt": 1.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "4111",  
  "MCC_Desc": "Commuter Transport, Ferries",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "4111",  
  "Merch_Name_DE43": "Travel Like A Pro HR",  
  "POS_Data_DE22": "0110",  
  "Proc_Code": "200000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "235303502517",  
  "Settle_Amt": 1.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 107419774,  
  "Trans_link": "221219002517622180",  
  "Txn_Amt": 1.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "HRV",  
  "Txn_Desc": "Travel Like A Pro HR",  
  "Txn_GPS_Date": "2022-12-19 07:28:37.526",  
  "TXn_ID": 6155805913,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "1219072835",  
  "Txn_Type": "A",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "DEF_PV",  
  "InstCode": "TEST",  
  "MTID": "0100",  
  "ProductID": 99883,  
  "SubBIN": 44622180,  
  "TLogIDOrg": 0,  
  "VL_Group": "MLMS_PV_GB",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "PIN": "0",  
  "SendingAttemptCount": 0  
}
```

The above example does not include all available fields as not all fields are required for a message. For example, in the above message, the `Network_Replacement_Amounts_DE95` field is not required as part of the message.

### Authorisation Response

Below is an example of HTTP response to the above Authorisation request message.

[Copy](javascript:void(0);)

```
{  
    "MerchantAdvice":"",  
    "Responsestatus":"00",  
    "CurBalance":0,  
    "AvlBalance":100,  
    "Acknowledgement":"1",  
    "LoadAmount":50,  
    "Bill_Amt_Approved":0,  
    "Update_Balance":1,  
    "New_Balance_Sequence_Exthost":200,  
    "CVV2_Result":"M",  
    "CurBalance_GPS_STIP":0,  
    "AvlBalance_GPS_STIP":100  
}
```

## 3.1.2 Example Authorisation Reversal

### Authorisation Reversal Request

Below is an example of the HTTP POST body data for an Authorisation Reversal message.

[Copy](javascript:void(0);)

```
{  
  "AuthenticationAmountUpper": 0.0000,  
  "FxProviderCardholderRate": 0.0,  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2022-12-26 07:27:14.180",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "Travel Like A Pro",  
  "Merch_Country": "HRV",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000001016",  
  "GPS_POS_Data": "0168000800000Nx000",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20221219-MC 004279",  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "0852729540",  
  "ActBal": 3535.47,  
  "Amt_Tran_Fee_DE28": "D00000010",  
  "Auth_Code_DE38": "183715",  
  "Avl_Bal": 3401.72,  
  "Bill_Amt": 10.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": -133.75,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.50,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "4111",  
  "MCC_Desc": "Commuter Transport, Ferries",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "4111           ",  
  "Merch_Name_DE43": "Travel Like A Pro HRV",  
  "Note": "Testing  User - Dhanya.B Date - 19/12/2022 16:18:08 BillAmt - 10.00 Location - Travel Like A Pro    ",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "2000000006000191",  
  "POS_Termnl_DE41": "        ",  
  "POS_Time_DE12": "072714",  
  "Proc_Code": "000000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "235303504279",  
  "Settle_Amt": 10.00,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 107612119,  
  "Trans_link": "221219004279729540",  
  "Txn_Amt": 10.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "HRV",  
  "Txn_Desc": "Travel Like A Pro HRV",  
  "Txn_GPS_Date": "2022-12-19 10:48:03.580",  
  "TXn_ID": 6155806244,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "1219072714",  
  "Txn_Type": "D",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "CRN-CU-001",  
  "InstCode": "TEST",  
  "ProductID": 99884,  
  "SubBIN": 52729540,  
  "TLogIDOrg": 0,  
  "VL_Group": "CRN-VL-100",  
  "Dom_Fee_Fixed": 0.50,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}
```

The above example does not include all available fields as not all fields are required for a message. For example, in the above message, the `Network_Original_Data_Elements_DE90` field is not required as part of the message.

### Authorisation Reversal Response

Below is an example of HTTP response to the above Authorisation Reversal message.

[Copy](javascript:void(0);)

```
{  
    "MerchantAdvice":"",  
    "Responsestatus":"00",  
    "CurBalance":0,  
    "AvlBalance":100,  
    "Acknowledgement":"1",  
    "LoadAmount":50,  
    "Bill_Amt_Approved":0,  
    "Update_Balance":1,  
    "New_Balance_Sequence_Exthost":200,  
    "CVV2_Result":"M",  
    "CurBalance_GPS_STIP":0,  
    "AvlBalance_GPS_STIP":100  
}
```

## 3.1.3 Example Financial Presentment (Mastercard)

The following is an example presentment from Mastercard (`MTID` = 1240 and `Txn_Type` = P).

### Financial Request

Below is an example of the HTTP POST body data for a financial request.

[Copy](javascript:void(0);)

```
{  
  "ClearingFileID": "T112.0012209120005206900000025     ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1000000:6",  
  "POS_Date_DE13": "20220912",  
  "Traceid_Message": "BNET-20220912-MC 694327",  
  "Network_Issuer_Settle_ID": "52069000",  
  "Network_Transaction_ID": " MC 6943270912  ",  
  "Acquirer_Forwarder_ID": "500000",  
  "Clearing_Process_Date": "2022-09-12",  
  "Settlement_Date": "2022-09-12",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 6153911205,  
  "Reason_ID": 0,  
  "Merch_Name": "E-Comm Merchant",  
  "Merch_City": "CITY",  
  "Merch_Country": "GBR",  
  "Merch_Tel": "5032277600      ",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0010000000000000000000000000000000100000000990016",  
  "GPS_POS_Data": "51V8000800000Nx000",  
  "Acquirer_Reference_Data_031": "15000005123000006943271",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20220912-MC 694327",  
  "PaymentToken_id": 0,  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "500000",  
  "ActBal": 0.00,  
  "Auth_Code_DE38": "187239",  
  "Avl_Bal": 0.00,  
  "Bill_Amt": 50.00,  
  "Bill_Ccy": "124",  
  "BlkAmt": 0.00,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "5734",  
  "MCC_Desc": "Computer Software Stores",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "ECOMM          ",  
  "Merch_Name_DE43": "E-Comm Merchant  \\\\CITY \\ GBR",  
  "Note": " Refund matching credit auth",  
  "POS_Data_DE22": "090951S99001",  
  "POS_Termnl_DE41": "11223344",  
  "POS_Time_DE12": "220912184813",  
  "Proc_Code": "200000",  
  "Ret_Ref_No_DE37": "225504594327",  
  "Settle_Amt": 50.00,  
  "Settle_Ccy": "124",  
  "Status_Code": "00",  
  "Token": 107916050,  
  "Trans_link": "220912694327500000",  
  "Txn_Amt": 50.0000,  
  "Txn_CCy": "124",  
  "Txn_Ctry": "GBR",  
  "Txn_Desc": "E-Comm Merchant \\\\CITY \\ GBR",  
  "Txn_GPS_Date": "2022-09-12 19:49:25.513",  
  "TXn_ID": 6153911206,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "P",  
  "Additional_Data_DE48": "0002003MRG0003003MRG0023003CT60052003   014800412420158030MCC10106017322091201  NNNNNN0159067  1521544702350  1US00000001N22091201220912010165001M01700165032277600",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-001",  
  "InstCode": "PMT",  
  "MTID": "1240",  
  "ProductID": 1234,  
  "SubBIN": 52111111,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-001",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}
```

### Financial Response

Below is an example of HTTP response to the above Financial Request message.

[Copy](javascript:void(0);)

```
{    
    "Acknowledgement": "1",  
    "Responsestatus": "00"  
}
```

## 3.1.4 Example Second Financial Presentment (Mastercard)

The following is an example second presentment from Mastercard (`MTID` = 1240 and `Txn_Type` = N).

[Copy](javascript:void(0);)

```
{  
  "ClearingFileID": "T112.0012601140000003334806601",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7429006:7",  
  "POS_Date_DE13": "20251209",  
  "Traceid_Message": "BNET-20251209-MCSK2A173",  
  "Network_Issuer_Settle_ID": "033348",  
  "Network_Transaction_ID": " MCSK2A1731209  ",  
  "Acquirer_Forwarder_ID": "003499",  
  "Currency_Code_Fee": "840",  
  "Currency_Code_Fee_Settlement": "826",  
  "Interchange_Amount_Fee": 1.190000,  
  "Interchange_Amount_Fee_Settlement": 0.880000,  
  "Clearing_Process_Date": "2026-01-14",  
  "Settlement_Date": "2026-01-15",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "MERPAGO*GRUPOMODELO",  
  "Merch_Street": "AV INSURGENTES SUR 1602",  
  "Merch_City": "CIUDAD DE MEX",  
  "Merch_Region": "MEX",  
  "Merch_Postcode": "03940",  
  "Merch_Country": "MEX",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0000000010000000000000000000000000100000000230006",   
  "GPS_POS_Data": "50V80008000001x000",  
  "Acquirer_Reference_Data_031": "75177135343171088477474",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20251209-MCSK2A173",  
  "PaymentToken_id": 0,  
  "PaymentToken_activationMethod": 0,  
  "ActBal": -32.3200,  
  "Auth_Code_DE38": "345544",  
  "Avl_Bal": -32.3200,  
  "Bill_Amt": -53.6300,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5411",  
  "MCC_Desc": "Grocery Stores, Supermarkets",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "8847747        ",  
  "Merch_Name_DE43": "MERPAGO*GRUPOMODELO\\AV INSURGENTES SUR 1602\\CIUDAD DE MEX\\03940     MEXMEX",  
  "Note": "9343141128Chargeback not accepted transaction valid under card network rules and supporting evidence",  
  "POS_Data_DE22": "690550S99000",  
  "POS_Termnl_DE41": "01062906",  
  "POS_Time_DE12": "251209190355",  
  "Proc_Code": "003000",  
  "Ret_Ref_No_DE37": "            ",  
  "Settle_Amt": -53.6300,  
  "Settle_Ccy": "826",  
  "Status_Code": "83",  
  "Token": 276557146,  
  "Trans_link": "251210930797003499",  
  "Txn_Amt": 72.1900,  
  "Txn_CCy": "840",  
  "Txn_Ctry": "MEX",  
  "Txn_Desc": "MERPAGO*GRUPOMODELO\\AV INSURGENTES SUR 1602\\CIUDAD DE MEX\\03940     MEXMEX",  
  "Txn_GPS_Date": "2026-01-14 22:03:44.070",  
  "TXn_ID": 2000000082332377,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "N",  
  "Additional_Data_DE48": "0002003MCS0003003MCS001500726011300023003CT60052003210014603600290184000000000011982600000000008801480208402484284028402826201490064840000158031MCC1030501YG26011406    NNNNNNN015906733348      39120006                    1EU00000012M26011406260115010165001M0177002YY019100120262001102661264837260101  0000000072198409343141128Cardholder reported fraud                                                                ",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "BTS-CU-001",  
  "InstCode": "BTS",  
  "MTID": "1240",  
  "ProductID": 15121,  
  "SubBIN": 51540629,  
  "TLogIDOrg": 0,  
  "VL_Group": "BTS-VL-001",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

### Response

Below is an example of HTTP response to the above Second Presentment message.

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}      
                  
                
```

## 3.1.5 Financial Reversal (Mastercard)

Below is an example of the HTTP POST body data for a financial reversal (`MTID` = 1240 and `Txn_Type` = E).

A financial reversal occurs when the acquirer cancels all or part of a prior transaction (which may be a purchase, refund, cashback, cash, PIN change, or any other transaction type).

[Copy](javascript:void(0);)

```
{  
  "ClearingFileID": "T112.0012402020000002032601101     ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1000000:6",  
  "POS_Date_DE13": "20240131",  
  "Traceid_Message": "BNET-20240131-MDW2YHECL",  
  "Network_Issuer_Settle_ID": "021075",  
  "Network_Transaction_ID": " MDW2YHECL0131  ",  
  "Acquirer_Forwarder_ID": "032208",  
  "Currency_Code_Fee": "978",  
  "Currency_Code_Fee_Settlement": "978",  
  "Interchange_Amount_Fee": 0.009200,  
  "Interchange_Amount_Fee_Settlement": 0.009200,  
  "Clearing_Process_Date": "2024-02-02",  
  "Settlement_Date": "2024-02-02",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "COFFEE ISLAND",  
  "Merch_Street": "ALKINOOU 2",  
  "Merch_City": "DAFNI",  
  "Merch_Region": "GRC",  
  "Merch_Postcode": "17235",  
  "Merch_Country": "GRC",  
  "Merch_Tel": "2109766611      ",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "000000000000000000000001000100000000000000911341R",  
  "GPS_POS_Data": "0175000400000Nx000",  
  "Acquirer_Reference_Data_031": "77673704031974724943402",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20240131-MDW2YHECL",  
  "PaymentToken_id": 61531240,  
  "PaymentToken_activationMethod": 0,  
  "ActBal": 0.0000,  
  "Auth_Code_DE38": "150683",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": 4.6000,  
  "Bill_Ccy": "978",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5812",  
  "MCC_Desc": "Eating Places, Restaurants",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "5053986        ",  
  "Merch_Name_DE43": "COFFEE ISLAND\\ALKINOOU 2\\DAFNI\\17235     GRCGRC",  
  "POS_Data_DE22": "M19101M54341",  
  "POS_Termnl_DE41": "67500288",  
  "POS_Time_DE12": "240131103058",  
  "Proc_Code": "000000",  
  "Ret_Ref_No_DE37": "403102239336",  
  "Settle_Amt": 4.6000,  
  "Settle_Ccy": "978",  
  "Status_Code": "00",  
  "Token": 256713034,  
  "Trans_link": "1240131943402767370",  
  "Txn_Amt": 4.6000,  
  "Txn_CCy": "978",  
  "Txn_Ctry": "GRC",  
  "Txn_Desc": "COFFEE ISLAND\\ALKINOOU 2\\DAFNI\\17235     GRCGRC",  
  "Txn_GPS_Date": "2024-02-02 01:36:04.133",  
  "TXn_ID": 13917006447,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "E",  
  "Additional_Data_DE48": "0001018O 53721433999650260002003MDW0003003MDW001500724013010023003POI0025007R2402010044002 I005800200005901150183038325014603600290197800000000000097800000000000001470480029019780000000000000092009780000000000000092000148004978201490069780000158031DMC4300001L424020201    NNNNNNN015906721075      14097113                    1EUD2000008N24020201240202010165030M                             01700162109766611      0177002N 019100120207003337",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-002",  
  "InstCode": "PMT",  
  "MTID": "1240",  
  "ProductID": 6496,  
  "SubBIN": 12345678,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-004",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}  
    
    
  
```

### Financial Reversal Response

Below is an example of HTTP response to the above Financial Notification message.

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## 3.1.6 Financial Reversal (Visa)

Below is an example of the HTTP POST body data for a financial reversal (from Visa, `MTID`= 27 and `Txn_Type` = E) used for a Cash Withdrawal/disbursement reversal.

[Copy](javascript:void(0);)

```
{  
  "Network_TxnAmt_To_BillAmt_Rate": "1000000:6",  
  "POS_Date_DE13": "20220830",  
  "Traceid_Message": "VIS1-20220830-002242207570295",  
  "Network_Issuer_Settle_ID": "099999",  
  "Network_Transaction_ID": "002242207570295",  
  "Clearing_Process_Date": "2022-08-30",  
  "Settlement_Date": "2022-08-30",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 1,  
  "multi_part_count": 1,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "BNP ATM",  
  "Merch_Postcode": "00000",  
  "Merch_Country": "CYP",  
  "Merch_Tel": "              ",  
  "Merch_Net_id": "          ",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "000000010000000000000001000000000000000000029301A",  
  "GPS_POS_Data": "0151800380000 x000",  
  "Acquirer_Reference_Data_031": "77882202242000000000011",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "VIS1-20220830-002242207570295",  
  "PaymentToken_id": 0,  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "00000001",  
  "ActBal": 848.99,  
  "Additional_Amt_DE54": "0040826D000000000000",  
  "Auth_Code_DE38": "146367",  
  "Avl_Bal": 792.79,  
  "Bill_Amt": 1.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": -56.20,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 1.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "6011",  
  "MCC_Desc": "Automated Cash Disburse",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "6011           ",  
  "Merch_Name_DE43": "BNP ATM\\\\\\00000        CYP",  
  "POS_Data_DE22": "05          ",  
  "POS_Termnl_DE41": "        ",  
  "POS_Time_DE12": "220830000000",  
  "Proc_Code": "010000",  
  "Settle_Amt": 1.00,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 100029683,  
  "Trans_link": "220830001921788220",  
  "Txn_Amt": 1.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "CYP",  
  "Txn_Desc": "BNP ATM\\\\\\00000        CYP",  
  "Txn_GPS_Date": "2022-08-30 15:12:04.157",  
  "TXn_ID": 6153544584,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "E",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMTPAYROLL",  
  "InstCode": "PMT",  
  "MTID": "27  ",  
  "ProductID": 1234,  
  "SubBIN": 43111111,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT CO1",  
  "Dom_Fee_Fixed": 1.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}
```

### Financial Reversal Response

Below is an example of HTTP response to the above Financial Reversal message.

[Copy](javascript:void(0);)

```
{  
  "FxProviderCardholderRate": 0.0,  
  "POS_Date_DE13": "00000000",  
  "Visa_ResponseInfo_DE44": "020000000000",  
  "Visa_STIP_Reason_Code": "9020",  
  "Network_Transaction_ID": "0002353127640022",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2022-12-27 07:44:44.137",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "Passenger Railway - SCAEx",  
  "Merch_Country": "CYP",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "00001001000000000000000100010010001000000001130C0",  
  "GPS_POS_Data": "9968000800000Nx000",  
  "Response_Source": "VISA-STIP",  
  "Response_Source_Why": 5,  
  "Message_Source": "VISA-STIP",  
  "Message_Why": 5,  
  "traceid_lifecycle": "VIS1-20221219-002353127640022",  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "0844622180",  
  "ActBal": 10001.00,  
  "Avl_Bal": 10001.00,  
  "Bill_Amt": 1.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.00,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "4112",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "4112           ",  
  "Merch_Name_DE43": "Passenger Railway - SCAEx CY",  
  "POS_Data_DE22": "0110",  
  "Proc_Code": "000000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "235303502519",  
  "Settle_Amt": 0.00,  
  "Status_Code": "00",  
  "Token": 107419774,  
  "Trans_link": "221219002519622180",  
  "Txn_Amt": 1.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "CYP",  
  "Txn_Desc": "Passenger Railway - SCAEx CY",  
  "Txn_GPS_Date": "2022-12-19 07:44:44.203",  
  "TXn_ID": 6155805963,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "1219074444",  
  "Txn_Type": "J",  
  "Authorised_by_GPS": "N",  
  "InstCode": "TEST",  
  "MTID": "0120",  
  "ProductID": 99883,  
  "SubBIN": 44622180,  
  "TLogIDOrg": 0,  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

## 3.1.7 Example Visa Authorisation Advice

Below is an example of the HTTP POST body data for a Visa authorisation advice.

[Copy](javascript:void(0);)

```
{  
  "FxProviderCardholderRate": 0.0,  
  "POS_Date_DE13": "00000000",  
  "Visa_ResponseInfo_DE44": "020000000000",  
  "Visa_STIP_Reason_Code": "9020",  
  "Network_Transaction_ID": "0002353127640022",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2022-12-27 07:44:44.137",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "Passenger Railway - SCAEx",  
  "Merch_Country": "CYP",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "00001001000000000000000100010010001000000001130C0",  
  "GPS_POS_Data": "9968000800000Nx000",  
  "Response_Source": "VISA-STIP",  
  "Response_Source_Why": 5,  
  "Message_Source": "VISA-STIP",  
  "Message_Why": 5,  
  "traceid_lifecycle": "VIS1-20221219-002353127640022",  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "0844622180",  
  "ActBal": 10001.00,  
  "Avl_Bal": 10001.00,  
  "Bill_Amt": 1.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.00,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "4112",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "4112           ",  
  "Merch_Name_DE43": "Passenger Railway - SCAEx CY",  
  "POS_Data_DE22": "0110",  
  "Proc_Code": "000000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "235303502519",  
  "Settle_Amt": 0.00,  
  "Status_Code": "00",  
  "Token": 107419774,  
  "Trans_link": "221219002519622180",  
  "Txn_Amt": 1.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "CYP",  
  "Txn_Desc": "Passenger Railway - SCAEx CY",  
  "Txn_GPS_Date": "2022-12-19 07:44:44.203",  
  "TXn_ID": 6155805963,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "1219074444",  
  "Txn_Type": "J",  
  "Authorised_by_GPS": "N",  
  "InstCode": "TEST",  
  "MTID": "0120",  
  "ProductID": 99883,  
  "SubBIN": 44622180,  
  "TLogIDOrg": 0,  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

### Response

Below is an example of HTTP response to the above Visa authorisation advice message.

[Copy](javascript:void(0);)

```
{  
    "MerchantAdvice":"",  
    "Responsestatus":"00",  
    "CurBalance":0,  
    "AvlBalance":100,  
    "Acknowledgement":"1",  
    "LoadAmount":50,  
    "Bill_Amt_Approved":0,  
    "Update_Balance":1,  
    "New_Balance_Sequence_Exthost":200,  
    "CVV2_Result":"M",  
    "CurBalance_GPS_STIP":0,  
    "AvlBalance_GPS_STIP":100  
}
```

## 3.1.8 Example Mastercard Authorisation Advice

Below is an example of the HTTP POST body data for a Mastercard authorisation advice.

[Copy](javascript:void(0);)

```
{  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1000000:6",  
  "POS_Date_DE13": "20221219",  
  "Traceid_Message": "BNET-20221219-MC 004280",  
  "Network_Currency_Conversion_Date": "2022-12-19",  
  "Mastercard_AdviceReasonCode_DE60": "4020000",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2022-12-26 07:39:24.520",  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 0,  
  "Merch_Name": "Travel Like A Pro",  
  "Merch_Country": "HRV",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0011000010000000000000000000000000100000000001016",  
  "GPS_POS_Data": "0168000800000Nx000",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20221219-MC 004280",  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "0852729540",  
  "ActBal": 3535.47,  
  "Amt_Tran_Fee_DE28": "D00000010",  
  "Auth_Code_DE38": "183716",  
  "Avl_Bal": 3392.72,  
  "Bill_Amt": 10.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": -142.75,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "4111",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "4111",  
  "Merch_Name_DE43": "Travel Like A Pro HRV",  
  "POS_Data_DE22": "010",  
  "POS_Data_DE61": "0162000000006000191",  
  "POS_Time_DE12": "072725",  
  "Proc_Code": "000000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "235303504280",  
  "Settle_Amt": 0.00,  
  "Status_Code": "00",  
  "Token": 107612119,  
  "Trans_link": "221219004280729540",  
  "Txn_Amt": 10.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "HRV",  
  "Txn_Desc": "Travel Like A Pro HRV",  
  "Txn_GPS_Date": "2022-12-19 07:39:24.607",  
  "TXn_ID": 6155805959,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "1219072725",  
  "Txn_Type": "J",  
  "Additional_Data_DE48": "001R",  
  "Authorised_by_GPS": "N",  
  "InstCode": "TEST",  
  "MTID": "0120",  
  "ProductID": 99884,  
  "SubBIN": 52729540,  
  "TLogIDOrg": 0,  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

### Response

Below is an example of HTTP response to the above Mastercard authorisation advice message.

[Copy](javascript:void(0);)

```
{  
    "MerchantAdvice":"",  
    "Responsestatus":"00",  
    "CurBalance":0,  
    "AvlBalance":100,  
    "Acknowledgement":"1",  
    "LoadAmount":50,  
    "Bill_Amt_Approved":0,  
    "Update_Balance":1,  
    "New_Balance_Sequence_Exthost":200,  
    "CVV2_Result":"M",  
    "CurBalance_GPS_STIP":0,  
    "AvlBalance_GPS_STIP":100  
}
```

## 3.1.9 Example Non-Credit Chargeback Notification (Mastercard)

The following is an example of a non-credit chargeback notification. If the chargeback is non-credit, the chargeback amount is taken from the customer's account. The HTTP POST body data for a non-credit chargeback notification includes: `MTID` = 1240 and `Txn_Type` = H).

[Copy](javascript:void(0);)

```
{  
  "AuthenticationAmountUpper": 0.0000,  
  "FxProviderCardholderRate": 0.0,  
  "Network_Chargeback_Reference_Id": "3013854930852",  
  "Acquirer_Forwarder_ID": "020779",  
  "Currency_Code_Fee": "826",  
  "Currency_Code_Fee_Settlement": "826",  
  "Interchange_Amount_Fee": 0.734250,  
  "Interchange_Amount_Fee_Settlement": 0.734250,  
  "Settlement_Date": "2026-01-21",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 2000000083237157,  
  "Reason_ID": 4853,  
  "Merch_Name": "SP ZERINDI",  
  "Merch_Street": "Manegelaan 57",  
  "Merch_City": "HOOFDDORP",  
  "Merch_Region": "NH",  
  "Merch_Postcode": "2131 XA",  
  "Merch_URL": "ZERINDI.COM",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "0010000000000000000000000000000000100000001291106",  
  "GPS_POS_Data": "50V00000000001x000",  
  "Acquirer_Reference_Data_031": "82644316021500002346397",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "ActBal": 0.1300,  
  "Auth_Code_DE38": "393261",  
  "Avl_Bal": 0.1300,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5691",  
  "MCC_Desc": "Menâs, Womenâs Clothing Stores",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "SRAIHWIFULCFNFN",  
  "Merch_Name_DE43": "SP ZERINDI\\Manegelaan 57\\HOOFDDORP\\2131 XA   NH NLD",  
  "POS_Data_DE22": "0916",  
  "POS_Termnl_DE41": "HLIQPVJB",  
  "POS_Time_DE12": "260120171836",  
  "Proc_Code": "000000",  
  "Ret_Ref_No_DE37": " ",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 277008040,  
  "Trans_link": "260120656766020779",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "826",  
  "Txn_Desc": "SP ZERINDI\\Manegelaan 57\\HOOFDDORP\\2131 XA   NH NLD",  
  "Txn_GPS_Date": "2026-02-14 02:35:55.333",  
  "TXn_ID": 2000000087438932,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "H",  
  "Additional_Data_DE48": "0002003MCS0003003MCS001500726012010023003CT6005200321001460360029018260000000000738260000000000730147048002901826000000000000734250826000000000000734250014800482620158031MCC3050041EV26012102    NNNNNNN015906733348      39120006                    1EU00000012N26012102260121010165001M0175011ZERINDI.COM0177002YN01910012",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "BTS-CU-001",  
  "InstCode": "BTS",  
  "MTID": "1240",  
  "ProductID": 15121,  
  "SubBIN": 51540629,  
  "TLogIDOrg": 0,  
  "VL_Group": "BTS-VL-001",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
 }  
            
```

### Chargeback Response

Below is an example of HTTP response to the above Chargeback notification message.

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## 3.1.10 Example Chargeback Notification (Mastercard)

The following is an example of a chargeback notification, where the disputed amount is credited to the customer's account. The HTTP POST body data for a non-credit chargeback notification includes: `MTID` = 1240 and `Txn_Type` = C).

[Copy](javascript:void(0);)

```
{  
  "AuthenticationAmountUpper": 0.0000,  
  "FxProviderCardholderRate": 0.0,  
  "Network_Chargeback_Reference_Id": "308900918928",  
  "Acquirer_Forwarder_ID": "003325",  
  "Currency_Code_Fee": "826",  
  "Currency_Code_Fee_Settlement": "826",  
  "Interchange_Amount_Fee": -0.115000,  
  "Interchange_Amount_Fee_Settlement": -0.115000,  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 14288894490,  
  "Reason_ID": 4834,  
  "Merch_Name": "NATWEST BANK",  
  "Merch_Street": "CHANCERY LN HBRN 5",  
  "Merch_City": "LONDON",  
  "Merch_Region": "ENG",  
  "Merch_Postcode": "WC1V 7PX",  
  "Merch_Country": "GBR",  
  "Merch_Name_Other": "NATWEST BANK",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "000000010000000000000001000000100000000000121146A",  
  "GPS_POS_Data": "0151000300000Nx000",  
  "Acquirer_Reference_Data_031": "85433254125005252052527",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "Acquirer_id_DE32": "543325",  
  "ActBal": 0.00,  
  "Auth_Code_DE38": "156039",  
  "Avl_Bal": 0.00,  
  "Bill_Amt": 50.00,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.00,  
  "FX_Pad": 0.00,  
  "Fee_Fixed": 0.00,  
  "Fee_Rate": 0.00,  
  "MCC_Code": "6011",  
  "MCC_Desc": "Automated Cash Disburse",  
  "MCC_Pad": 0.00,  
  "Merch_ID_DE42": "N576331        ",  
  "Merch_Name_DE43": "NATWEST BANK\\CHANCERY LN HBRN 5\\LONDON\\WC1V 7PX  ENGGBR",  
  "Note": "ChargeBack - Credit to Card",  
  "POS_Data_DE22": "5112",  
  "POS_Termnl_DE41": "N576331 ",  
  "POS_Time_DE12": "240504111533",  
  "Proc_Code": "010000",  
  "Ret_Ref_No_DE37": "050400005252",  
  "Settle_Amt": 50.00,  
  "Settle_Ccy": "826",  
  "Status_Code": "43",  
  "Token": 133235724,  
  "Trans_link": "240504005252003325",  
  "Txn_Amt": 50.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "GBR",  
  "Txn_Desc": "NATWEST BANK\\CHANCERY LN HBRN 5\\LONDON\\WC1V 7PX  ENGGBR",  
  "Txn_GPS_Date": "2024-06-24 10:02:48.457",  
  "TXn_ID": 14501288226,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "C",  
  "Additional_Data_DE48": "0002003MDS0003003MDS001500724050310023003ATM01460360019018260000000000128260000000000120147048001901826000000000000115000826000000000000115000014800482620158031DMC48260015124050701    NNNNNNN015906723167      39120006                    1EU00000012N24050701240507010165001M0172012NATWEST BANK0173012NATWEST BANK0177002N 019100120213003826",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "ZIG-CU-001",  
  "InstCode": "ZIG",  
  "MTID": "1240",  
  "ProductID": 7574,  
  "SubBIN": 53576700,  
  "TLogIDOrg": 0,  
  "VL_Group": "ZIG-VL-001",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}  
            
```

### Chargeback Response

Below is an example of HTTP response to the above Chargeback notification message.

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## 3.1.11 Example Chargeback Reversal (Mastercard)

The following is an example of a chargeback reversal, The HTTP POST body data for a chargeback reversal includes: `MTID` = 1240 and `Txn_Type` = K).

[Copy](javascript:void(0);)

```
{  
  "AuthenticationAmountUpper": 0.0000,  
  "FxProviderCardholderRate": 0.0,  
  "Network_Chargeback_Reference_Id": "3012289249155",  
  "Acquirer_Forwarder_ID": "018512",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "Matching_Txn_ID": 0,  
  "Reason_ID": 4853,  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "",  
  "GPS_POS_Data": "000",  
  "Acquirer_Reference_Data_031": "85130705142500004920001",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "PaymentToken_id": 0,  
  "PaymentToken_creatorStatus": " ",  
  "PaymentToken_lang": "  ",  
  "PaymentToken_activationMethod": 0,  
  "ActBal": 33.6100,  
  "Auth_Code_DE38": "161388",  
  "Avl_Bal": 33.6100,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "5399",  
  "MCC_Desc": "Miscellaneous General Merchandise",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "Y0BXWG4SFPV5HCE",  
  "Merch_Name_DE43": "SP LANSLIN\\THOMSON COMM BLDG 8 THOMSON RD\\WANCHAI\\999077    KL HKG",  
  "Note": " CBC:Chargeback Credit confirmed on (MasterCom) 17-07-2025 05:55:01",  
  "POS_Data_DE22": "0916",  
  "POS_Termnl_DE41": "NLDVIQHD",  
  "POS_Time_DE12": "250522064945",  
  "Proc_Code": "000000",  
  "Ret_Ref_No_DE37": " ",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "840",  
  "Status_Code": "46",  
  "Token": 275389481,  
  "Trans_link": "250521351405018512",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "840",  
  "Txn_Desc": "SP LANSLIN\\THOMSON COMM BLDG 8 THOMSON RD\\WANCHAI\\999077    KL HKG",  
  "Txn_GPS_Date": "2025-07-25 04:06:43.510",  
  "TXn_ID": 2000000055175340,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "K",  
  "Additional_Data_DE48": "0002003MCS0003003MCS001500725052110023003CT600520032100146036002901826000000000054826000000000054014800482620158031MCC1040501YA25052203    NNNNNNN015906733348      39120006                    1EU00000012N25052203250522010165001M0175012LANSLIN.SHOP0177002YN01910012",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "BTS-CU-001",  
  "InstCode": "BTS",  
  "MTID": "1240",  
  "ProductID": 15121,  
  "SubBIN": 51540629,  
  "TLogIDOrg": 0,  
  "VL_Group": "BTS-VL-001",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}  
            
```

### Chargeback Response

Below is an example of HTTP response to the above Chargeback reversal message.

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## 3.1.12 Example Balance Enquiry Message

Below is an example of the HTTP POST body data for a balance enquiry request. A balance enquiry provides details of changes to a cardâs account balance. Card balance adjustments are made using Thredd's API (web services or Cards API) and are relevant to program managers on [EHI Operating modes](../Getting_Started/EHI_operating_modes.htm) where Thredd maintains a record of the card balance.

[Copy](javascript:void(0);)

```
{  
  "Acquirer_Country": "GBR",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1000000:6",  
  "POS_Date_DE13": "20240925",  
  "Traceid_Message": "BNET-20240924-MPB4IFV1M",  
  "Network_Currency_Conversion_Date": "2024-09-24",  
  "Network_Transaction_ID": "MPB4IFV1M0924",  
  "Acquirer_Forwarder_ID": "200148",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "0",  
  "auth_expdate_utc": "2024-10-01 23:27:09.712",  
  "Merch_Name": "HFX  ECCLES CHURCH ST",  
  "Merch_City": "MANCHESTER",  
  "Merch_Postcode": "M30 0DA",  
  "Merch_Country": "GBR",  
  "GPS_POS_Capability": "00001001000000000000000100000010000000000012230CA",  
  "GPS_POS_Data": "0151000300000Nx0002110NU0NCUXXU",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20240924-MPB4IFV1M",  
  "Balance_Sequence": 0,  
  "Balance_Sequence_Exthost": 0,  
  "ICC_System_Related_Data_DE55": "9F2608FF63FD5AD4CEDDF89F2701809F10120110A00003220000000000000000000000FF9F3704E4F0B2D09F3602009B950580000480009A032409259C01309F02060000000000005F2A020826820218009F1A0208269F34034203009F33036040208407A0000000041010",  
  "Acquirer_id_DE32": "06002309",  
  "ActBal": 0.0000,  
  "Auth_Code_DE38": "161883",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": 0.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "Cust_Ref": "A2",  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "6011",  
  "MCC_Desc": "Automated Cash Disburse",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "LTS1",  
  "Merch_Name_DE43": "HFX  ECCLES CHURCH ST    MANCHESTER  GBR",  
  "Note": "PSD2 Counter Reset",  
  "POS_Data_DE22": "051",  
  "POS_Data_DE61": "1010010000500826M30 0DA",  
  "POS_Termnl_DE41": "HA88EC11",  
  "POS_Time_DE12": "002709",  
  "Proc_Code": "300000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "20882       ",  
  "Settle_Amt": 0.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
  "Token": 358713475,  
  "Trans_link": "240925925631002309",  
  "Txn_Amt": 0.0000,  
  "Txn_CCy": "826",  
  "Txn_Ctry": "GBR",  
  "Txn_Desc": "HFX  ECCLES CHURCH ST    MANCHESTER  GBR",  
  "Txn_GPS_Date": "2024-09-25 00:27:09.911",  
  "TXn_ID": 14890418727,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "0924232709",  
  "Txn_Type": "A",  
  "Additional_Data_DE48": "007Z8002TV",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "PMT-CU-004",  
  "InstCode": "PMT",  
  "MTID": "0100",  
  "ProductID": 15455,  
  "SubBIN": 53908886,  
  "TLogIDOrg": 0,  
  "VL_Group": "PMT-VL-008",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

### Message Response

Below is an example of HTTP response to the above balance enquiry message.

[Copy](javascript:void(0);)

```
{  
"Acknowledgement":"1",  
"Responsestatus":"00",  
"CurBalance":2425.6300,  
"AvlBalance":2125.6300  
}
```

## 3.1.13 Example ATM Cash Withdrawal Messages (Mastercard)

### Example Authorisation Message

The example below shows a typical authorisation message of an ATM cash withdrawal for Mastercard.

Note that there is a value for Amt\_Tran\_Fee\_DE28. This indicates that there is a transaction fee for the cash withdrawal as there is a value (D00000590),

[Copy](javascript:void(0);)

```
{  
  "Acquirer_Country": "DEU",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1121282:5",  
  "POS_Date_DE13": "2025-08-21",  
  "Traceid_Message": "BNET-20250821-*********",  
  "Network_Currency_Conversion_Date": "2025-08-20",  
  "Network_Transaction_ID": "MDW2*****0821",  
  "Acquirer_Forwarder_ID": "200123",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "auth_type": "F",  
  "auth_expdate_utc": "2025-08-22 05:34:17.926",  
  "Merch_Name": "M-Hbf. III",  
  "Merch_City": "Hauptbahnhof",  
  "Merch_Postcode": "60489",  
  "Merch_Country": "DEU",  
  "GPS_POS_Capability": "00001001000000000000000100000010000000000012130C1",  
  "GPS_POS_Data": "*******************************",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20250821-*********",  
  "Balance_Sequence": 0,  
  "Balance_Sequence_Exthost": 0,  
  "ICC_System_Related_Data_DE55": "**********************************************************************************************************************************************************************************************************************************************************************************",  
  "Acquirer_id_DE32": "06010480",  
  "ActBal": 0.0000,  
  "Amt_Tran_Fee_DE28": "D00000590",  
  "Auth_Code_DE38": "60**05",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": -2308.7200,  
  "Bill_Ccy": "752",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "6011",  
  "MCC_Desc": "Automated Cash Disburse",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "52410300",  
  "Merch_Name_DE43": "M-Hbf. III             Hauptbahnhof  DEU",  
  "Note": "PSD2 Counter Reset",  
  "POS_Data_DE22": "051",  
  "POS_Data_DE61": "100001000150128060489",  
  "POS_Termnl_DE41": "00002468",  
  "POS_Time_DE12": "073337",  
  "Proc_Code": "010000",  
  "Resp_Code_DE39": "00",  
  "Ret_Ref_No_DE37": "08******8158",  
  "Settle_Amt": 2308.7200,  
  "Settle_Ccy": "752",  
  "Status_Code": "00",  
  "Token": 14******4,  
  "Trans_link": "25082*******010480",  
  "Txn_Amt": 205.9000,  
  "Txn_CCy": "978",  
  "Txn_Ctry": "DEU",  
  "Txn_Desc": "M-Hbf. III             Hauptbahnhof  DEU",  
  "Txn_GPS_Date": "2025-08-21 06:34:18.011",  
  "TXn_ID": *****475865,  
  "Txn_Stat_Code": "A",  
  "TXN_Time_DE07": "0821053417",  
  "Txn_Type": "A",  
  "Additional_Data_DE48": "*******************",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "***-**-***",  
  "InstCode": "***",  
  "MTID": "0100",  
  "ProductID": 1234,  
  "SubBIN": ********,  
  "TLogIDOrg": 0,  
  "VL_Group": "***-VL-***",  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{  
"Responsestatus":"00",  
"Acknowledgement":"1"  
}
```

### Example Presentment Message

The example below shows a presentment message for an ATM cash withdrawal for Mastercard.

[Copy](javascript:void(0);)

```
{  
  "ClearingFileID": "T112.0012508220000002032602201     ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "1121282:5",  
  "POS_Date_DE13": "20250821",  
  "Traceid_Message": "BNET-20250821-MDW2IPTG0",  
  "Network_Issuer_Settle_ID": "021075",  
  "Network_Transaction_ID": " MDW2IPTG00821  ",  
  "Acquirer_Forwarder_ID": "010480",  
  "Currency_Code_Fee": "978",  
  "Currency_Code_Fee_Settlement": "978",  
  "Interchange_Amount_Fee": 0.000000,  
  "Interchange_Amount_Fee_Settlement": 0.000000,  
  "Clearing_Process_Date": "2025-08-22",  
  "Settlement_Date": "2025-08-22",  
  "DCC_Indicator": 0,  
  "multi_part_txn": 0,  
  "multi_part_txn_final": 0,  
  "multi_part_number": 0,  
  "multi_part_count": 0,  
  "SettlementIndicator": "0",  
  "auth_type": "0",  
  "Matching_Txn_ID": 16386475865,  
  "Reason_ID": 0,  
  "Merch_Name": "REISEBANK FRANKFURT AT",  
  "Merch_City": "MUENCHEN",  
  "Merch_Region": "DEU",  
  "Merch_Postcode": "60528",  
  "Merch_Country": "DEU",  
  "Merch_Tax_id": "0",  
  "GPS_POS_Capability": "000000010000000000000001000001000000000000121346A",  
  "GPS_POS_Data": "0151000100000Nx000",  
  "Acquirer_Reference_Data_031": "75506185234281662061591",  
  "Response_Source_Why": 0,  
  "Message_Why": 0,  
  "traceid_lifecycle": "BNET-20250821-MDW2IPTG0",  
  "PaymentToken_id": 0,  
  "PaymentToken_activationMethod": 0,  
  "ActBal": 0.0000,  
  "Additional_Amt_DE54": "0042978D000000000590",  
  "Auth_Code_DE38": "606805",  
  "Avl_Bal": 0.0000,  
  "Bill_Amt": -2308.7200,  
  "Bill_Ccy": "752",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "6011",  
  "MCC_Desc": "Automated Cash Disburse",  
  "MCC_Pad": 0.0000,  
  "Merch_ID_DE42": "4052245/4052245",  
  "Merch_Name_DE43": "REISEBANK FRANKFURT AT\\\\MUENCHEN     \\60528     DEUDEU",  
  "POS_Data_DE22": "511201C11346",  
  "POS_Termnl_DE41": "00002468",  
  "POS_Time_DE12": "250821073337",  
  "Proc_Code": "010000",  
  "Ret_Ref_No_DE37": "082107058158",  
  "Settle_Amt": -205.9000,  
  "Settle_Ccy": "978",  
  "Status_Code": "00",  
  "Token": 143654784,  
  "Trans_link": "250821882458010480",  
  "Txn_Amt": 205.9000,  
  "Txn_CCy": "978",  
  "Txn_Ctry": "DEU",  
  "Txn_Desc": "REISEBANK FRANKFURT AT\\\\MUENCHEN     \\60528     DEUDEU",  
  "Txn_GPS_Date": "2025-08-22 04:15:05.103",  
  "TXn_ID": 16390740846,  
  "Txn_Stat_Code": "S",  
  "Txn_Type": "P",  
  "Additional_Data_DE48": "0002003MDW0003003MDW001500725082010023003ATM014603600190197800000000000097800000000000001470480019019780000000000000000009780000000000000000000148008978275220158031DMC30500125625082202    N2NNNNN015906721075      14097113                    1EUD2000008N25082202250822010165001M0177002N 01910012",  
  "Authorised_by_GPS": "N",  
  "CU_Group": "CRV-CU-002",  
  "InstCode": "CRV",  
  "MTID": "1240",  
  "ProductID": 6540,  
  "SubBIN": 55744496,  
  "TLogIDOrg": 0,  
  "VL_Group": "CRV-VL-182",  
  "Dom_Fee_Fixed": 0.00,  
  "Non_Dom_Fee_Fixed": 0.00,  
  "Fx_Fee_Fixed": 0.00,  
  "Other_Fee_Amt": 0.00,  
  "Fx_Fee_Rate": 0.00,  
  "Dom_Fee_Rate": 0.00,  
  "Non_Dom_Fee_Rate": 0.00,  
  "SendingAttemptCount": 0  
}
```

#### Response

Example response from the external host system:

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```

## 3.1.14 Example Tokenisation Messages

### Example EHI TAR (330000) Message

The example below shows a typical EHI 0100 authorisation message for a Token Authorisation Request (TAR) in a JSON format.

[Copy](javascript:void(0);)

```
{  
  "SchemeTransactionIdentifier": "BNETF64",  
  "TokenUniqueReference": "DM4MMC1PT0000000be3ec16ef999999ab7d4b47da4456277",  
  "PaymentTokenPan": "5372403458767765",  
  "PaymentToken_PanSource": "F",  
  "Network_Fraud_Data": "00199991",  
  "FxProviderCardholderRate": 0.000000000,  
  "Network_TxnAmt_To_BillAmt_Rate": "7849290:7",  
  "POS_Date_DE13": "00000000",  
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
  "Merch_Name_DE43": "Klarna-EU St. Louis USA",  
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

### ACN (340000) Message

[Copy](javascript:void(0);)

```
{  
  "SchemeTransactionIdentifier": "BNETF64",  
  "TokenUniqueReference": "DM4MMC1DE0000000cac6e366341d49819f38090c57f15677",  
  "PaymentTokenPan": "5372403458767765",  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "00000000",  
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
{  
  "Responsestatus":"00",  
  "CurBalance":0.0,  
  "AvlBalance":0.0,  
  "Acknowledgement":1,  
  "LoadAmount":0.0,  
  "Bill_Amt_Approved":0.0,  
  "Update_Balance":0,  
  "New_Balance_Sequence_Exthost":0,  
  "CVV2_Result":"",  
  "AvlBalance_GPS_STIP":0.0,  
  "CurBalance_GPS_STIP":0.0  
}
```

### TCN (350000) Message

[Copy](javascript:void(0);)

```
{  
  "SchemeTransactionIdentifier": "BNETF64",  
  "TokenUniqueReference": "DM4MMC1DE0000000cac6e366341d49819f38090c57f15677",  
  "PaymentTokenPan": "5372403458767765",  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "00000000",  
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
{  
  "Responsestatus":"00",  
  "CurBalance":0.0,  
  "AvlBalance":0.0,  
  "Acknowledgement":1,  
  "LoadAmount":0.0,  
  "Bill_Amt_Approved":0.0,  
  "Update_Balance":0,  
  "New_Balance_Sequence_Exthost":0,  
  "CVV2_Result":"",  
  "AvlBalance_GPS_STIP":0.0,  
  "CurBalance_GPS_STIP":0.0  
}
```

### TEN (360000) Message

[Copy](javascript:void(0);)

```
{  
  "SchemeTransactionIdentifier": "BNETF64",  
  "TokenUniqueReference": "DM4MMC1PT0000000be3ec16ef999999ab7d4b47da4456277",  
  "PaymentTokenPan": "5372403458767765",  
  "Network_Fraud_Data": "00199991                        ",  
  "FxProviderCardholderRate": 0.0,  
  "Network_TxnAmt_To_BillAmt_Rate": "7878970:7",  
  "POS_Date_DE13": "00000000",  
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
{  
  "Responsestatus":"00",  
  "CurBalance":0.0,  
  "AvlBalance":0.0,  
  "Acknowledgement":1,  
  "LoadAmount":0.0,  
  "Bill_Amt_Approved":0.0,  
  "Update_Balance":0,  
  "New_Balance_Sequence_Exthost":0,  
  "CVV2_Result":"",  
  "AvlBalance_GPS_STIP":0.0,  
  "CurBalance_GPS_STIP":0.0  
}
```

## 3.1.15 Example Incremental Authorisation Messages

### Incremental Authorisation Request

Below is an example of the HTTP POST body data for an incremental authorisation request.

[Copy](javascript:void(0);)

```
{  
  "FxProviderCardholderRate":0.000000000,  
  "Network_TxnAmt_To_BillAmt_Rate":"1000000:6",  
  "POS_Date_DE13":"20241127",  
  "Traceid_Message":"BNET-20241127-MCC680561",  
  "Traceid_Original":"BNET-20241127-MCC686194",  
  "Network_Currency_Conversion_Date":"2024-11-27",  
  "Network_Transaction_ID":"MCC6805611127",  
  "DCC_Indicator":0,  
  "multi_part_txn":0,  
  "multi_part_txn_final":0,  
  "auth_type":"P",  
  "auth_expdate_utc":"2024-12-27 13:26:26.363",  
  "Matching_Txn_ID":0,  
  "Reason_ID":0,  
  "Merch_Name":"ASDA GROCERIES",  
  "Merch_City":"LONDON",  
  "Merch_Postcode":"SW1 3AN",  
  "Merch_Country":"GBR",  
  "Merch_Tax_id":"0",  
  "GPS_POS_Capability":"000100000000010000000000000000000010000000000100M",  
  "GPS_POS_Data":"10V8000800000Nx006",  
  "Response_Source_Why":0,  
  "Message_Why":0,  
  "traceid_lifecycle":"BNET-20241127-MCC686194",  
  "PaymentToken_id":0,  
  "PaymentToken_creatorStatus":" ",  
  "PaymentToken_lang":"  ",  
  "PaymentToken_activationMethod":0,  
  "Acquirer_id_DE32":"06555555",  
  "ActBal":100723.40,  
  "Auth_Code_DE38":"166297",  
  "Avl_Bal":100009.40,  
  "Bill_Amt":-20.00,  
  "Bill_Ccy":"826",  
  "BlkAmt":-714.00,  
  "FX_Pad":0.00,  
  "Fee_Fixed":2.00,  
  "Fee_Rate":0.00,  
  "MCC_Code":"5734",  
  "MCC_Desc":"Computer Software Stores",  
  "MCC_Pad":0.00,  
  "Merch_ID_DE42":"MERCHANT 000001",  
  "Merch_Name_DE43":"ASDA GROCERIES         LONDON        GBR",  
  "Note":"  Gen: Pre-Authorization Request",  
  "POS_Data_DE22":"812",  
  "POS_Data_DE61":"2031104000100826SW1 3AN",  
  "POS_Termnl_DE41":"ECOMM001",  
  "POS_Time_DE12":"012626",  
  "Proc_Code":"000000",  
  "Resp_Code_DE39":"00",  
  "Ret_Ref_No_DE37":"433210456861",  
  "Settle_Amt":20.00,  
  "Settle_Ccy":"826",  
  "Status_Code":"00",  
  "Token":108336227,  
  "Trans_link":"241127683518555555",  
  "Txn_Amt":20.0000,  
  "Txn_CCy":"826",  
  "Txn_Ctry":"GBR",  
  "Txn_Desc":"ASDA GROCERIES         LONDON        GBR",  
  "Txn_GPS_Date":"2024-11-27 13:26:26.783",  
  "TXn_ID":6162588064,  
  "Txn_Stat_Code":"A",  
  "TXN_Time_DE07":"1127132626",  
  "Txn_Type":"A",  
  "Additional_Data_DE48":"038T420701038106315MCC6861941127  9203***",  
  "Authorised_by_GPS":"N",  
  "CU_Group":"PMT-CU-001",  
  "InstCode":"TEST",  
  "MTID":"0100",  
  "ProductID":99884,  
  "SubBIN":52729540,  
  "TLogIDOrg":0,  
  "VL_Group":"QE-LIMIT",  
  "Dom_Fee_Fixed":2.0000,  
  "Non_Dom_Fee_Fixed":0.0000,  
  "Fx_Fee_Fixed":0.0000,  
  "Other_Fee_Amt":0.0000,  
  "Fx_Fee_Rate":0.0000,  
  "Dom_Fee_Rate":0.0000,  
  "Non_Dom_Fee_Rate":0.0000,  
  "SendingAttemptCount":0  
  }
```

### Incremental Authorisation Response

Below is an example response.

[Copy](javascript:void(0);)

```
{  
  "MerchantAdvice":null,  
  "Responsestatus":"00",  
  "CurBalance":0,  
  "AvlBalance":100,  
  "Acknowledgement":"1",  
  "LoadAmount":50,  
  "Bill_Amt_Approved":0,  
  "Update_Balance":1,  
  "New_Balance_Sequence_Exthost":200,  
  "CVV2_Result":"M",  
  "CurBalance_GPS_STIP":0,  
  "AvlBalance_GPS_STIP":100  
}
```

## 3.1.16 Examples of Amount Signs

The table below provides an overview of the signs on important amount fields used in many transactions and illustrates using examples.

The `TXn_ID` field is provided for internal Thredd usage and can be ignored.

| MTID | Txn\_Type | cr/db | Proc\_ Code | Source | settle\_ccy | settle\_amt | txn\_ccy | txn\_amt | bill\_ccy | bill\_amt | TXn\_ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0100 | A | Debit | 000000 | Banknet | 978 | 7.1900 | 826 | 6.3000 | 978 | -7.1900 | 3178117382 |
| 0100 | A | Debit | 000000 | Visa B1 | 978 | 22.2500 | 826 | 19.4800 | 978 | -22.2500 | 3178117377 |
| 0100 | A | Credit | 280000 | Banknet | 826 | 47.7500 | 826 | 47.7500 | 826 | 47.7500 | 3178096311 |
| 0100 | A | Credit | 260000 | Visa B1 | 978 | 77.7100 | 826 | 70.0000 | 978 | 77.7100 | 3076890895 |
|  | D | Credit | 000000 | Banknet | 978 | 1.0000 | 978 | 1.0000 | 978 | 1.0000 | 3177930769 |
|  | D | Credit | 003000 | Visa B1 | 978 | 29.9400 | 554 | 50.0000 | 978 | 29.9400 | 3177930766 |
|  | D | Debit | 280000 | Banknet | 826 | 10.0000 | 826 | 10.0000 | 826 | -10.0000 | 3179976368 |
|  | D | Debit | 200000 | Visa B1 | 840 | 10.0000 | 826 | 8.0200 | 124 | -14.0400 | (not real) |
| 0120 | J | Credit | 000000 | Banknet |  | 0.0000 | 784 | 21.0300 | 826 | 4.4400 | 3178071058 |
| 0120 | J | Credit | 003000 | Visa B1 |  | 0.0000 | 458 | 2.4800 | 978 | 0.5400 | 3178059229 |
| 0120 | J | Credit | 200000 | Banknet |  | 0.0000 | 826 | 25.0000 | 978 | 30.0000 | (not real) |
| 0120 | J | Credit | 260000 | Visa B1 |  | 0.0000 | 826 | 70.0000 | 978 | 77.7100 | 3076890919 |
| 1240 | P | Debit | 000000 | GCMS | 978 | -129.0000 | 978 | 129.0000 | 978 | -129.0000 | 3185427850 |
| 1240 | P | Credit | 200000 | GCMS | 978 | 39.2300 | 978 | 39.2300 | 978 | 39.2300 | 3185427844 |
| 05pp | P | Debit | 000000 | Visa B2 | 826 | -30.5800 | 710 | 550.0000 | 826 | -30.5800 | 3184113150 |
| 06pp | P | Credit | 200000 | Visa B2 | 978 | 7.1300 | 036 | 11.3600 | 978 | 7.1300 | 3183968531 |
| 07pp | P | Debit | 010000 | Visa B2 | 978 | -901.7500 | 978 | 901.7500 | 978 | -901.7500 | 3183970358 |
| 1240 | A | Debit (dummy auth) | 010000 | GCMS | 840 | -64.9300 | 704 | 1500000.0000 | 978 | -57.6000 | 3189756992 |
| 1240 | A | Credit (dummy auth) | 200000 | GCMS | 978 | 39.2300 | 978 | 39.2300 | 978 | 39.2300 | (not real) |
| 05pp | A | Debit (dummy auth) | 000000 | Visa B2 | 840 | -18.9300 | 756 | 19.0000 | 840 | -18.9300 | 3189248664 |
| 06pp | A | Credit (dummy auth) | 200000 | Visa B2 | 978 | 7.1300 | 036 | 11.3600 | 978 | 7.1300 | (not real) |
| 07pp | A | Debit (dummy auth) | 010000 | Visa B2 | 826 | -207.7100 | 484 | 5100.0000 | 826 | -207.7100 | 3189246992 |
| 1240 | C | Chargeback | 180000 | Other | 978 | 200.0000 | 978 | 200.0000 | 978 | 200.0000 | 3186093786 |
| 1240 | C | Chargeback | 000000 | Other | 826 | 98.0000 | 826 | 98.0000 | 826 | 98.0000 | 3189694682 |
| 1240 | C | Chargeback | 010000 | Other | 978 | 80.0000 | 978 | 80.0000 | 978 | 80.0000 | 3189323524 |
|  | L | Load | 220000 | Other | 978 | 90.0000 | 978 | 90.0000 | 978 | 90.0000 | 3189759169 |
|  | U | Unload | 230000 | Other | 826 | 8.8400 | 826 | 8.8400 | 826 | -8.8400 | 2993509894 |
|  | B | Bal Adj | 190000 | Other | 978 | 0.1900 | 978 | 0.1900 | 978 | -0.1900 | 3188058606 |
|  | B | Bal Adj | 021000 | Other | 826 | 4.9900 | 826 | 4.9900 | 826 | 4.9900 | 3188057935 |
|  | P | Fee | 083999 | Thredd  (Fee fields have amounts) | 826 | 0.0000 | 826 | 0.0000 | 826 | 0.0000 | 5071773234 |

#### Notes

In the above table, a âpâ indicates the space character, and the âSourceâ column indicates the origin of the message as follows:

* âVisa B1â if from Visa Base 1 (i.e., Visa online authorisation system)
* âVisa B2â if from Visa Base 2 (i.e., Visa offline clearing system)
* âBanknetâ if from Mastercard Banknet (i.e., Mastercard online authorisation system)
* âGCMSâ if from Mastercard Global Clearing system (i.e., Mastercard offline clearing system)
* âOtherâ means not Visa or Mastercard. For example, internal (via Thredd Portal, Smart Client) or a web service call / Cards API call.