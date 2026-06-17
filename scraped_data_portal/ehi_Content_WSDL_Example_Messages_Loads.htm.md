# 3.6 Example Messages from Loads & Balance Adjustments

This page details examples of requests and responses for messages related to Thredd Web Services or Cards API.

* [Load Request](#Load)
* [Unload Request](#Unload)
* [Balance Adjustment Request](#Balance)

## 3.6.1 Load Request

A load request transaction is where a Program Manager has loaded money onto a card. This is done using Thredd API (Web Services or Cards API). For Cooperative and Full Service Processing (modes 2 and 3) it will update the balance.

Below is an example of the HTTP POST body data for a Load request.

Some key elements of this request are:

* The `Txn_Amt` value 2.0000 and the `Txn_Ccy` of 826 indicates that Â£2 has been loaded onto the card for this transaction.
* We consider it good practice to include a description for the transaction in the `Note` field, to help with auditing of each transaction.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32 />   
<ActBal>975.4800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38 />   
<Avl_Bal>947.1600</Avl_Bal>   
 <Bill_Amt>2.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-28.3200</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC>33</LoadSRC>   
 <LoadType>3</LoadType>   
 <MCC_Code />   
<MCC_Desc />   
<MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42 />   
<Merch_Name_DE43 />   
<Note>Refund sent to customer Date - Jun 22 2022  8:22AM</Note>   
 <POS_Data_DE22 />   
<POS_Data_DE61 />   
<POS_Termnl_DE41 />   
<POS_Time_DE12 />   
<Proc_Code>220000</Proc_Code>   
 <Resp_Code_DE39 />   
<Ret_Ref_No_DE37 />   
<Settle_Amt>2.0000</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>6152636856</Trans_link>   
 <Txn_Amt>2.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Load</Txn_Desc>   
 <Txn_GPS_Date>2022-06-22 08:22:15.613</Txn_GPS_Date>   
 <TXn_ID>6152636856</TXn_ID>   
 <Txn_Stat_Code>S</Txn_Stat_Code>   
 <TXN_Time_DE07 />   
<Txn_Type>L</Txn_Type>   
 <Additional_Data_DE48 />   
<Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group>GPS-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID />   
<ProductID>1697</ProductID>   
 <Record_Data_DE120 />   
<SubBIN>52729540</SubBIN>   
 <TLogIDOrg>0</TLogIDOrg>   
 <VL_Group>PMT-VL-100</VL_Group>   
 <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>   
 <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>   
 <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>   
 <Other_Fee_Amt>0.0000</Other_Fee_Amt>   
 <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>   
 <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>   
 <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>   
 <Additional_Data_DE124 />   
<CVV2 />   
<PIN />   
<PIN_Enc_Algorithm />   
<PIN_Format />   
<PIN_Key_Index />   
<SendingAttemptCount>0</SendingAttemptCount>   
 <source_bank_ctry />   
<source_bank_account_format />   
<source_bank_account />   
<dest_bank_ctry />   
<dest_bank_account_format />   
<dest_bank_account />   
<GPS_POS_Capability>           </GPS_POS_Capability>   
 <GPS_POS_Data>               000</GPS_POS_Data>   
 <Acquirer_Reference_Data_031 />   
<Response_Source />   
<Response_Source_Why>0</Response_Source_Why>   
 <Message_Source />   
<Message_Why>0</Message_Why>   
 <traceid_lifecycle />   
<PaymentToken_id>0</PaymentToken_id>   
 <PaymentToken_creator />   
<PaymentToken_expdate />   
<PaymentToken_type />   
<PaymentToken_status />   
<PaymentToken_creatorStatus> </PaymentToken_creatorStatus>   
 <PaymentToken_wallet />   
<PaymentToken_deviceType />   
<PaymentToken_lang>  </PaymentToken_lang>   
 <PaymentToken_deviceTelNum />   
<PaymentToken_deviceIp />   
<PaymentToken_deviceId />   
<PaymentToken_deviceName />   
<PaymentToken_activationCode />   
<PaymentToken_activationExpiry />   
<PaymentToken_activationMethodData />   
<PaymentToken_activationMethod>0</PaymentToken_activationMethod>   
 <ICC_System_Related_Data_DE55 />   
<Merch_Name />   
<Merch_Street />   
<Merch_City />   
<Merch_Region />   
<Merch_Postcode />   
<Merch_Country>GBR</Merch_Country>   
 <Merch_Tel />   
<Merch_URL />   
<Merch_Name_Other />   
<Merch_Net_id />   
<Merch_Tax_id>0</Merch_Tax_id>   
 <Merch_Contact />   
<auth_type />   
<auth_expdate_utc />   
<Matching_Txn_ID>0</Matching_Txn_ID>   
 <Reason_ID>0</Reason_ID>   
 <Dispute_Condition />   
<Network_Chargeback_Reference_Id />   
<Acquirer_Forwarder_ID />   
<Currency_Code_Fee />   
<Currency_Code_Fee_Settlement />   
<Interchange_Amount_Fee />   
<Interchange_Amount_Fee_Settlement />   
<Clearing_Process_Date />   
<Settlement_Date />   
<DCC_Indicator>0</DCC_Indicator>   
 <multi_part_txn>0</multi_part_txn>   
 <multi_part_txn_final>0</multi_part_txn_final>   
 <multi_part_number />   
<multi_part_count />   
<SettlementIndicator />   
<Network_TxnAmt_To_BillAmt_Rate />   
<Network_TxnAmt_To_BaseAmt_Rate />   
<Network_BaseAmt_To_BillAmt_Rate />   
<POS_Date_DE13 />   
<Traceid_Message />   
<Traceid_Original />   
<Network_Currency_Conversion_Date />   
<Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID />   
<Misc_TLV_Data />   
<Acquirer_Country />   
<Network_Fraud_Data />   
<SenderData />   
<ReceiverData />   
<AuthenticationAmountUpper>0.0000</AuthenticationAmountUpper>   
 <AuthenticationCurrency />   
<AuthenticationMerchantHash />   
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>   
 </GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

### Load Response

Below is an example of HTTP response to the above Load Request message.

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

## 3.6.2 Unload Request

Below is an example of the HTTP POST body data for an Unload request.

Some key elements of this request are:

* The `Txn_Amt` value 2.0000 and the `Txn_Ccy` of 826 indicates that Â£2 has been loaded onto the card for this transaction.
* We consider it good practice to include a description for the transaction in the `Note` field, to help with auditing of each transaction.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32 />   
<ActBal>973.4800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38 />   
<Avl_Bal>945.1600</Avl_Bal>   
 <Bill_Amt>-2.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-28.3200</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC>4</LoadSRC>   
 <LoadType>3</LoadType>   
 <MCC_Code />   
<MCC_Desc />   
<MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42 />   
<Merch_Name_DE43 />   
<Note>Amount unloaded from card on date - Jun 22 2022  8:15AM</Note>   
 <POS_Data_DE22 />   
<POS_Data_DE61 />   
<POS_Termnl_DE41 />   
<POS_Time_DE12 />   
<Proc_Code>230000</Proc_Code>   
 <Resp_Code_DE39 />   
<Ret_Ref_No_DE37 />   
<Settle_Amt>2.0000</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>6152636847</Trans_link>   
 <Txn_Amt>2.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Unload</Txn_Desc>   
 <Txn_GPS_Date>2022-06-22 08:15:33.693</Txn_GPS_Date>   
 <TXn_ID>6152636847</TXn_ID>   
 <Txn_Stat_Code>S</Txn_Stat_Code>   
 <TXN_Time_DE07 />   
<Txn_Type>U</Txn_Type>   
 <Additional_Data_DE48 />   
<Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group>PMT-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID />   
<ProductID>1697</ProductID>   
 <Record_Data_DE120 />   
<SubBIN>52729540</SubBIN>   
 <TLogIDOrg>0</TLogIDOrg>   
 <VL_Group>PMT-VL-100</VL_Group>   
 <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>   
 <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>   
 <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>   
 <Other_Fee_Amt>0.0000</Other_Fee_Amt>   
 <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>   
 <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>   
 <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>   
 <Additional_Data_DE124 />   
<CVV2 />   
<PIN />   
<PIN_Enc_Algorithm />   
<PIN_Format />   
<PIN_Key_Index />   
<SendingAttemptCount>0</SendingAttemptCount>   
 <source_bank_ctry />   
<source_bank_account_format />   
<source_bank_account />   
<dest_bank_ctry />   
<dest_bank_account_format />   
<dest_bank_account />   
<GPS_POS_Capability>           </GPS_POS_Capability>   
 <GPS_POS_Data>               000</GPS_POS_Data>   
 <Acquirer_Reference_Data_031 />   
<Response_Source />   
<Response_Source_Why>0</Response_Source_Why>   
 <Message_Source />   
<Message_Why>0</Message_Why>   
 <traceid_lifecycle />   
<PaymentToken_id>0</PaymentToken_id>   
 <PaymentToken_creator />   
<PaymentToken_expdate />   
<PaymentToken_type />   
<PaymentToken_status />   
<PaymentToken_creatorStatus> </PaymentToken_creatorStatus>   
 <PaymentToken_wallet />   
<PaymentToken_deviceType />   
<PaymentToken_lang>  </PaymentToken_lang>   
 <PaymentToken_deviceTelNum />   
<PaymentToken_deviceIp />   
<PaymentToken_deviceId />   
<PaymentToken_deviceName />   
<PaymentToken_activationCode />   
<PaymentToken_activationExpiry />   
<PaymentToken_activationMethodData />   
<PaymentToken_activationMethod>0</PaymentToken_activationMethod>   
 <ICC_System_Related_Data_DE55 />   
<Merch_Name />   
<Merch_Street />   
<Merch_City />   
<Merch_Region />   
<Merch_Postcode />   
<Merch_Country>GBR</Merch_Country>   
 <Merch_Tel />   
<Merch_URL />   
<Merch_Name_Other />   
<Merch_Net_id />   
<Merch_Tax_id>0</Merch_Tax_id>   
 <Merch_Contact />   
<auth_type />   
<auth_expdate_utc />   
<Matching_Txn_ID>0</Matching_Txn_ID>   
 <Reason_ID>0</Reason_ID>   
 <Dispute_Condition />   
<Network_Chargeback_Reference_Id />   
<Acquirer_Forwarder_ID />   
<Currency_Code_Fee />   
<Currency_Code_Fee_Settlement />   
<Interchange_Amount_Fee />   
<Interchange_Amount_Fee_Settlement />   
<Clearing_Process_Date />   
<Settlement_Date />   
<DCC_Indicator>0</DCC_Indicator>   
 <multi_part_txn>0</multi_part_txn>   
 <multi_part_txn_final>0</multi_part_txn_final>   
 <multi_part_number />   
<multi_part_count />   
<SettlementIndicator />   
<Network_TxnAmt_To_BillAmt_Rate />   
<Network_TxnAmt_To_BaseAmt_Rate />   
<Network_BaseAmt_To_BillAmt_Rate />   
<POS_Date_DE13 />   
<Traceid_Message />   
<Traceid_Original />   
<Network_Currency_Conversion_Date />   
<Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID />   
<Misc_TLV_Data />   
<Acquirer_Country />   
<Network_Fraud_Data />   
<SenderData />   
<ReceiverData />   
<AuthenticationAmountUpper>0.0000</AuthenticationAmountUpper>   
 <AuthenticationCurrency />   
<AuthenticationMerchantHash />   
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>   
 </GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

### Unload Response

Below is an example of HTTP response to the above Unload Request message.

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

## 3.6.3 Balance Adjustment Request

Balance adjustment messages are information that a Balance Adjustment has already happened  (i.e. it is not happening at the moment, and you cannot decline it.  It is an advice).

Below is an example of the HTTP POST body data for a balance adjustment notification.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32 />   
<ActBal>975.4800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38 />   
<Avl_Bal>947.1600</Avl_Bal>   
 <Bill_Amt>-2.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-28.3200</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC>0</LoadSRC>   
 <LoadType>0</LoadType>   
 <MCC_Code />   
<MCC_Desc />   
<MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42 />   
<Merch_Name_DE43 />   
<Note>Credit Other - Checking balance adjustment</Note>   
 <POS_Data_DE22 />   
<POS_Data_DE61 />   
<POS_Termnl_DE41 />   
<POS_Time_DE12 />   
<Proc_Code>190000</Proc_Code>   
 <Resp_Code_DE39 />   
<Ret_Ref_No_DE37 />   
<Settle_Amt>2.00</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>6152636846</Trans_link>   
 <Txn_Amt>2.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Credit Other - Checking balance adjustment</Txn_Desc>   
 <Txn_GPS_Date>2022-06-22 08:10:39.547</Txn_GPS_Date>   
 <TXn_ID>6152636846</TXn_ID>   
 <Txn_Stat_Code>S</Txn_Stat_Code>   
 <TXN_Time_DE07 />   
<Txn_Type>B</Txn_Type>   
 <Additional_Data_DE48 />   
<Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group>PMT-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID />   
<ProductID>1697</ProductID>   
 <Record_Data_DE120 />   
<SubBIN>52729540</SubBIN>   
 <TLogIDOrg>0</TLogIDOrg>   
 <VL_Group>PMT-VL-100</VL_Group>   
 <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>   
 <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>   
 <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>   
 <Other_Fee_Amt>0.0000</Other_Fee_Amt>   
 <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>   
 <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>   
 <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>   
 <Additional_Data_DE124 />   
<CVV2 />   
<PIN />   
<PIN_Enc_Algorithm />   
<PIN_Format />   
<PIN_Key_Index />   
<SendingAttemptCount>0</SendingAttemptCount>   
 <source_bank_ctry />   
<source_bank_account_format />   
<source_bank_account />   
<dest_bank_ctry />   
<dest_bank_account_format />   
<dest_bank_account />   
<GPS_POS_Capability>           </GPS_POS_Capability>   
 <GPS_POS_Data>               000</GPS_POS_Data>   
 <Acquirer_Reference_Data_031 />   
<Response_Source />   
<Response_Source_Why>0</Response_Source_Why>   
 <Message_Source />   
<Message_Why>0</Message_Why>   
 <traceid_lifecycle />   
<PaymentToken_id>0</PaymentToken_id>   
 <PaymentToken_creator />   
<PaymentToken_expdate />   
<PaymentToken_type />   
<PaymentToken_status />   
<PaymentToken_creatorStatus> </PaymentToken_creatorStatus>   
 <PaymentToken_wallet />   
<PaymentToken_deviceType />   
<PaymentToken_lang>  </PaymentToken_lang>   
 <PaymentToken_deviceTelNum />   
<PaymentToken_deviceIp />   
<PaymentToken_deviceId />   
<PaymentToken_deviceName />   
<PaymentToken_activationCode />   
<PaymentToken_activationExpiry />   
<PaymentToken_activationMethodData />   
<PaymentToken_activationMethod>0</PaymentToken_activationMethod>   
 <ICC_System_Related_Data_DE55 />   
<Merch_Name />   
<Merch_Street />   
<Merch_City />   
<Merch_Region />   
<Merch_Postcode />   
<Merch_Country>GBR</Merch_Country>   
 <Merch_Tel />   
<Merch_URL />   
<Merch_Name_Other />   
<Merch_Net_id />   
<Merch_Tax_id>0</Merch_Tax_id>   
 <Merch_Contact />   
<auth_type />   
<auth_expdate_utc />   
<Matching_Txn_ID>0</Matching_Txn_ID>   
 <Reason_ID>0</Reason_ID>   
 <Dispute_Condition />   
<Network_Chargeback_Reference_Id />   
<Acquirer_Forwarder_ID />   
<Currency_Code_Fee />   
<Currency_Code_Fee_Settlement />   
<Interchange_Amount_Fee />   
<Interchange_Amount_Fee_Settlement />   
<Clearing_Process_Date />   
<Settlement_Date />   
<DCC_Indicator>0</DCC_Indicator>   
 <multi_part_txn>0</multi_part_txn>   
 <multi_part_txn_final>0</multi_part_txn_final>   
 <multi_part_number />   
<multi_part_count />   
<SettlementIndicator />   
<Network_TxnAmt_To_BillAmt_Rate />   
<Network_TxnAmt_To_BaseAmt_Rate />   
<Network_BaseAmt_To_BillAmt_Rate />   
<POS_Date_DE13 />   
<Traceid_Message />   
<Traceid_Original />   
<Network_Currency_Conversion_Date />   
<Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID />   
<Misc_TLV_Data />   
<Acquirer_Country />   
<Network_Fraud_Data />   
<SenderData />   
<ReceiverData />   
<AuthenticationAmountUpper>0.0000</AuthenticationAmountUpper>   
 <AuthenticationCurrency />   
<AuthenticationMerchantHash />   
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>   
 </GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

### Balance Adjustment Response

Below is an example of HTTP response to the above Balance Adjustment notification message.

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