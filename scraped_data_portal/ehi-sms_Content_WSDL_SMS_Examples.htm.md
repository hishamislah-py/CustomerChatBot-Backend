# 3.8 SMS Examples

This section provides examples related to Single Message System (SMS) transaction messages. It includes the following examples:

* [Online Financial Transaction](#Online)
* [Financial Transaction Advice](#Financia)

## 3.8.1 Online Financial Transaction Example Request

Online financial transaction requests are sent from the acquirer to the issuer to request approval for a payment transaction. The request simultaneously posts the transaction to the cardholder's account.

Below is an example of the HTTP POST body data for a Online financial transaction request:

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
<s:Body>  
<GetTransaction xmlns="http://tempuri.org/">  
<Acquirer_id_DE32>555555</Acquirer_id_DE32>  
<ActBal>322.2800</ActBal>  
<Additional_Amt_DE54 />  
<Amt_Tran_Fee_DE28 />  
<Auth_Code_DE38 />  
<Avl_Bal>295.9800</Avl_Bal>  
<Bill_Amt>-2.0000</Bill_Amt>  
<Bill_Ccy>840</Bill_Ccy>  
<BlkAmt>-26.3000</BlkAmt>  
<Cust_Ref />  
<FX_Pad>0.0000</FX_Pad>  
<Fee_Fixed>0.0000</Fee_Fixed>  
<Fee_Rate>0.0600</Fee_Rate>  
<LoadSRC />  
<LoadType />  
<MCC_Code>5734</MCC_Code>  
<MCC_Desc>Computer Software Stores</MCC_Desc>  
<MCC_Pad>0.0000</MCC_Pad>  
<Merch_ID_DE42>MERCHANT 000005</Merch_ID_DE42>  
<Merch_Name_DE43>MERCHANT 123 AVENUE    NEW YORK     NYUS</Merch_Name_DE43>  
<Note />  
<POS_Data_DE22>070</POS_Data_DE22>  
<POS_Data_DE61 />  
<POS_Termnl_DE41>CHIPEMV1</POS_Termnl_DE41>  
<POS_Time_DE12>103942</POS_Time_DE12>  
<Proc_Code>000000</Proc_Code>  
<Resp_Code_DE39>00</Resp_Code_DE39>  
<Ret_Ref_No_DE37>517076702746</Ret_Ref_No_DE37>  
<Settle_Amt>2.0000</Settle_Amt>  
<Settle_Ccy>840</Settle_Ccy>  
<Status_Code>00</Status_Code>  
<Token>114958529</Token>  
<Trans_link>250619766442555555</Trans_link>  
<Txn_Amt>2.0000</Txn_Amt>  
<Txn_CCy>826</Txn_CCy>  
<Txn_Ctry>USA</Txn_Ctry>  
<Txn_Desc>MERCHANT 123 AVENUE    NEW YORK     NYUS</Txn_Desc>  
<Txn_GPS_Date>2025-06-19 11:39:45.241</Txn_GPS_Date>  
<TXn_ID>6165448753</TXn_ID>  
<Txn_Stat_Code>A</Txn_Stat_Code>  
<TXN_Time_DE07>0619103942</TXN_Time_DE07>  
<Txn_Type>M</Txn_Type>  
<Additional_Data_DE48>WENDYS</Additional_Data_DE48>  
<Authorised_by_GPS>N</Authorised_by_GPS>  
<AVS_Result />  
<CU_Group>PCS-CU-101</CU_Group>  
<InstCode>PCS</InstCode>  
<MTID>0200</MTID>  
<ProductID>16169</ProductID>  
<Record_Data_DE120 />  
<SubBIN>44325211</SubBIN>  
<TLogIDOrg>0</TLogIDOrg>  
<VL_Group>PMT-VL-002</VL_Group>  
<Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
<Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
<Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
<Other_Fee_Amt>0.0000</Other_Fee_Amt>  
<Fx_Fee_Rate>0.0600</Fx_Fee_Rate>  
<Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
<Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
<Additional_Data_DE124>NI05ST01E</Additional_Data_DE124>  
<CVV2 />  
<Expiry_Date />  
<PAN_Sequence_Number />  
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
<GPS_POS_Capability>000000010000000000000000000000000010000000011001R</GPS_POS_Capability>  
<GPS_POS_Data>01700000000000x00700107U0NUUXXU</GPS_POS_Data>  
<Acquirer_Reference_Data_031 />  
<Response_Source />  
<Response_Source_Why>0</Response_Source_Why>  
<Message_Source />  
<Message_Why>0</Message_Why>  
<traceid_lifecycle>MNESTAR-20250619-517076702746</traceid_lifecycle>  
<Balance_Sequence>2774</Balance_Sequence>  
<Balance_Sequence_Exthost>0</Balance_Sequence_Exthost>  
<PaymentToken_id />  
<PaymentToken_creator />  
<PaymentToken_expdate />  
<PaymentToken_type />  
<PaymentToken_status />  
<PaymentToken_creatorStatus />  
<PaymentToken_wallet />  
<PaymentToken_deviceType />  
<PaymentToken_lang />  
<PaymentToken_deviceTelNum />  
<PaymentToken_deviceIp />  
<PaymentToken_deviceId />  
<PaymentToken_deviceName />  
<PaymentToken_activationCode />  
<PaymentToken_activationExpiry />  
<PaymentToken_activationMethodData />  
<PaymentToken_activationMethod />  
<ICC_System_Related_Data_DE55>82021800950500000000009A032506199C01005F2A0208269F02060000000002009F03060000000000009F100706010A03A020019F1A0208269F26088637CE90E9475B7B9F2701809F360213599F370401BC3F56</ICC_System_Related_Data_DE55>  
<Merch_Name>MERCHANT 123 AVENUE</Merch_Name>  
<Merch_Street />  
<Merch_City>NEW YORK</Merch_City>  
<Merch_Region>NY</Merch_Region>  
<Merch_Postcode>12349</Merch_Postcode>  
<Merch_Country>USA</Merch_Country>  
<Merch_Tel />  
<Merch_URL />  
<Merch_Name_Other />  
<Merch_Net_id />  
<Merch_Tax_id />  
<Merch_Contact />  
<auth_type>0</auth_type>  
<auth_expdate_utc>2025-06-27 10:39:45.248</auth_expdate_utc>  
<Matching_Txn_ID />  
<Reason_ID />  
<Dispute_Condition />  
<Network_Chargeback_Reference_Id />  
<Acquirer_Forwarder_ID />  
<Currency_Code_Fee />  
<Currency_Code_Fee_Settlement />  
<Interchange_Amount_Fee />  
<Interchange_Amount_Fee_Settlement />  
<Clearing_Process_Date />  
<Settlement_Date>2025-06-19</Settlement_Date>  
<DCC_Indicator />  
<multi_part_txn />  
<multi_part_txn_final />  
<multi_part_number />  
<multi_part_count />  
<SettlementIndicator />  
<Network_TxnAmt_To_BillAmt_Rate />  
<Network_TxnAmt_To_BaseAmt_Rate />  
<Network_BaseAmt_To_BillAmt_Rate />  
<POS_Date_DE13 /><Traceid_Message />  
<Traceid_Original>MNESTAR-20250619-517076702746</Traceid_Original>  
<Network_Currency_Conversion_Date />  
<Mastercard_AdviceReasonCode_DE60 />  
<Network_Original_Data_Elements_DE90 />  
<Visa_ResponseInfo_DE44 />  
<Visa_STIP_Reason_Code />  
<Network_Issuer_Settle_ID />  
<Network_Replacement_Amounts_DE95 />  
<Visa_POS_Data_DE60 />  
<Network_Transaction_ID>517076702746</Network_Transaction_ID>  
<Misc_TLV_Data />  
<Acquirer_Country />  
<PaymentToken_PanSource />  
<Network_Fraud_Data />  
<SenderData />  
<ReceiverData />  
<AuthenticationAmountUpper />  
<AuthenticationCurrency />  
<AuthenticationMerchantHash />  
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>  
</GetTransaction>  
</s:Body>  
</s:Envelope>
```

### Online Financial Transaction Example Response

Below is an example of HTTP response to the above Online Financial Transaction message.

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://tempuri.org">  
  <soap:Body>  
    <tns:GetTransactionResponse>  
      <ResponseMsg>  
        <Acknowledgement>1</Acknowledgement>  
        <Responsestatus>00</Responsestatus>  
      </ResponseMsg>  
    </tns:GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

## 3.8.2 Financial Transaction Advice Example Request

A Financial Transaction Advice is used to provide advice about a financial transaction that has already been authorised or requested via an earlier message (typically an 0200 request). Unlike a request, an advice message is point-to-point and the receiver can only accept it, not reject it.

Below is an example of the HTTP POST body data for a Financial Transaction Advice request:

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
  <s:Body>  
    <GetTransaction xmlns="http://tempuri.org/">  
      <Acquirer_id_DE32>555555</Acquirer_id_DE32>  
      <ActBal>321.2800</ActBal>  
      <Additional_Amt_DE54 />  
      <Amt_Tran_Fee_DE28 />  
      <Auth_Code_DE38 />  
      <Avl_Bal>294.9800</Avl_Bal>  
      <Bill_Amt>-1.0000</Bill_Amt>  
      <Bill_Ccy>840</Bill_Ccy>  
      <BlkAmt>-26.3000</BlkAmt>  
      <Cust_Ref />  
      <FX_Pad>0.0000</FX_Pad>  
      <Fee_Fixed>0.0000</Fee_Fixed>  
      <Fee_Rate>0.0000</Fee_Rate>  
      <LoadSRC />  
      <LoadType />  
      <MCC_Code>5542</MCC_Code>  
      <MCC_Desc />  
      <MCC_Pad>0.0000</MCC_Pad>  
      <Merch_ID_DE42>MERCHANT 000005</Merch_ID_DE42>  
      <Merch_Name_DE43>WALMART 17 NORTH       DALLAS       TXUS</Merch_Name_DE43>  
      <Note>Completion for the initial transaction: 6165448758</Note>  
      <POS_Data_DE22>051</POS_Data_DE22>  
      <POS_Data_DE61 />  
      <POS_Termnl_DE41>CHIPEMV1</POS_Termnl_DE41>  
      <POS_Time_DE12>110754</POS_Time_DE12>  
      <Proc_Code>000000</Proc_Code>  
      <Resp_Code_DE39 />  
      <Ret_Ref_No_DE37>517030224831</Ret_Ref_No_DE37>  
      <Settle_Amt>1.0000</Settle_Amt>  
      <Settle_Ccy />  
      <Status_Code>00</Status_Code>  
      <Token>114958529</Token>  
      <Trans_link>250619278284555555</Trans_link>  
      <Txn_Amt>1.0000</Txn_Amt>  
      <Txn_CCy>840</Txn_CCy>  
      <Txn_Ctry>USA</Txn_Ctry>  
      <Txn_Desc>WALMART 17 NORTH       DALLAS       TXUS</Txn_Desc>  
      <Txn_GPS_Date>2025-06-19 12:07:55.152</Txn_GPS_Date>  
      <TXn_ID>6165448759</TXn_ID>  
      <Txn_Stat_Code>S</Txn_Stat_Code>  
      <TXN_Time_DE07>0619110754</TXN_Time_DE07>  
      <Txn_Type>Q</Txn_Type>  
      <Additional_Data_DE48 />  
      <Authorised_by_GPS>N</Authorised_by_GPS>  
      <AVS_Result />  
      <CU_Group />  
      <InstCode>PCS</InstCode>  
      <MTID>0220</MTID>  
      <ProductID>16169</ProductID>  
      <Record_Data_DE120 />  
      <SubBIN>44325211</SubBIN>  
      <TLogIDOrg>0</TLogIDOrg>  
      <VL_Group />  
      <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
      <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
      <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
      <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
      <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
      <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
      <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
      <Additional_Data_DE124>NI05ST01E</Additional_Data_DE124>  
      <CVV2 />  
      <Expiry_Date />  
      <PAN_Sequence_Number />  
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
      <GPS_POS_Capability>000000010000000000000000000000000010000000011001R</GPS_POS_Capability>  
      <GPS_POS_Data>01510001000000x000NNNN0C0N</GPS_POS_Data>  
      <Acquirer_Reference_Data_031 />  
      <Response_Source />  
      <Response_Source_Why>0</Response_Source_Why>  
      <Message_Source />  
      <Message_Why>0</Message_Why>  
      <traceid_lifecycle>MNESTAR-20250619-517030224831</traceid_lifecycle>  
      <Balance_Sequence>0</Balance_Sequence>  
      <Balance_Sequence_Exthost>0</Balance_Sequence_Exthost>  
      <PaymentToken_id />  
      <PaymentToken_creator />  
      <PaymentToken_expdate />  
      <PaymentToken_type />  
      <PaymentToken_status />  
      <PaymentToken_creatorStatus />  
      <PaymentToken_wallet />  
      <PaymentToken_deviceType />  
      <PaymentToken_lang />  
      <PaymentToken_deviceTelNum />  
      <PaymentToken_deviceIp />  
      <PaymentToken_deviceId />  
      <PaymentToken_deviceName />  
      <PaymentToken_activationCode />  
      <PaymentToken_activationExpiry />  
      <PaymentToken_activationMethodData />  
      <PaymentToken_activationMethod />  
      <ICC_System_Related_Data_DE55>82021800950500000000009A032506199C01005F2A0208409F02060000000003009F03060000000000009F100706010A03A020019F1A0208269F2608488652652B0D1ABB9F2701809F3602135A9F3704B1629423</ICC_System_Related_Data_DE55>  
      <Merch_Name>WALMART 17 NORTH</Merch_Name>  
      <Merch_Street />  
      <Merch_City>DALLAS</Merch_City>  
      <Merch_Region>TX</Merch_Region>  
      <Merch_Postcode>12348</Merch_Postcode>  
      <Merch_Country>USA</Merch_Country>  
      <Merch_Tel />  
      <Merch_URL />  
      <Merch_Name_Other />  
      <Merch_Net_id />  
      <Merch_Tax_id />  
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
      <Settlement_Date>2025-06-19</Settlement_Date>  
      <DCC_Indicator>0</DCC_Indicator>  
      <multi_part_txn />  
      <multi_part_txn_final />  
      <multi_part_number />  
      <multi_part_count />  
      <SettlementIndicator />  
      <Network_TxnAmt_To_BillAmt_Rate />  
      <Network_TxnAmt_To_BaseAmt_Rate />  
      <Network_BaseAmt_To_BillAmt_Rate />  
      <POS_Date_DE13 />  
      <Traceid_Message />  
      <Traceid_Original>MNESTAR-20250619-517030224831</Traceid_Original>  
      <Network_Currency_Conversion_Date />  
      <Mastercard_AdviceReasonCode_DE60 />  
      <Network_Original_Data_Elements_DE90 />  
      <Visa_ResponseInfo_DE44 />  
      <Visa_STIP_Reason_Code />  
      <Network_Issuer_Settle_ID />  
      <Network_Replacement_Amounts_DE95 />  
      <Visa_POS_Data_DE60 />  
      <Network_Transaction_ID>517030224831</Network_Transaction_ID>  
      <Misc_TLV_Data />  
      <Acquirer_Country />  
      <PaymentToken_PanSource />  
      <Network_Fraud_Data />  
      <SenderData />  
      <ReceiverData />  
      <AuthenticationAmountUpper />  
      <AuthenticationCurrency />  
      <AuthenticationMerchantHash />  
      <FxProviderCardholderRate>0.0</FxProviderCardholderRate>  
    </GetTransaction>  
  </s:Body>  
</s:Envelope>
```

### Financial Transaction Advice Example Response

Below is an example of HTTP response to the above Financial Transaction Advice message.

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://tempuri.org">  
  <soap:Body>  
    <tns:GetTransactionResponse>  
      <ResponseMsg>  
        <Acknowledgement>1</Acknowledgement>  
        <Responsestatus>00</Responsestatus>  
      </ResponseMsg>  
    </tns:GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```