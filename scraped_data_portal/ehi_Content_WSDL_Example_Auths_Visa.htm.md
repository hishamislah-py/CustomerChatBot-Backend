# 3.4 Example Authorisations on Visa Cards

This page details examples of requests and responses for authorisations on Visa cards.

* [Authorisation Request](#Authoris)
* [Authorisation Request (Auth Advice)](#Authoris2)
* [Authorisation Request (Payment Token Activation)](#Authoris3)

## 3.4.1 Authorisation Request

Below is an example of the HTTP POST body data for a Visa authorisation request.

* The `MTID` value is 0100 and the `Txn_Type` is A, indicating that this is an Authorisation Request.
* The transaction is for Â£20. This is indicated by the `Bill_Amt` having a value of 1.0000 and the `Bill_Ccy` being set to 826 (for Great British Pounds).
* The `SendingAttemptCount` field checks to show whether this is a duplicate request. This will be zero for a first attempt.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
          <Acquirer_id_DE32>06323232</Acquirer_id_DE32>  
          <ActBal>500.0000</ActBal>  
          <Additional_Amt_DE54 />  
          <Amt_Tran_Fee_DE28 />  
          <Auth_Code_DE38>137716</Auth_Code_DE38>  
          <Avl_Bal>191.5000</Avl_Bal>  
          <Bill_Amt>-20.0000</Bill_Amt>  
          <Bill_Ccy>826</Bill_Ccy>  
          <BlkAmt>-308.5000</BlkAmt>  
          <Cust_Ref />  
          <FX_Pad>0.0000</FX_Pad>  
          <Fee_Fixed>10.0000</Fee_Fixed>  
          <Fee_Rate>0.0000</Fee_Rate>  
          <LoadSRC />  
          <LoadType />  
          <MCC_Code>8931</MCC_Code>  
          <MCC_Desc>Accounting/Bookkeeping Services</MCC_Desc>  
          <MCC_Pad>0.0000</MCC_Pad>  
          <Merch_ID_DE42>testMerchanrt</Merch_ID_DE42>  
          <Merch_Name_DE43>Visa      Test                        GB</Merch_Name_DE43>  
          <Note />  
          <POS_Data_DE22>9010</POS_Data_DE22>  
          <POS_Data_DE61 />  
          <POS_Termnl_DE41>A0000001</POS_Termnl_DE41>  
          <POS_Time_DE12>082943</POS_Time_DE12>  
          <Proc_Code>000000</Proc_Code>  
          <Resp_Code_DE39>00</Resp_Code_DE39>  
          <Ret_Ref_No_DE37>119008935414</Ret_Ref_No_DE37>  
          <Settle_Amt>20.0000</Settle_Amt>  
          <Settle_Ccy>826</Settle_Ccy>  
          <Status_Code>00</Status_Code>  
          <Token>100467819</Token>  
          <Trans_link>210709935414323232</Trans_link>  
          <Txn_Amt>20.0000</Txn_Amt>  
          <Txn_CCy>826</Txn_CCy>  
          <Txn_Ctry>GBR</Txn_Ctry>  
          <Txn_Desc>Visa      Test                        GB</Txn_Desc>  
          <Txn_GPS_Date>2021-07-09 08:29:44.750</Txn_GPS_Date>  
          <TXn_ID>6151096705</TXn_ID>  
          <Txn_Stat_Code>A</Txn_Stat_Code>  
          <TXN_Time_DE07>0709072943</TXN_Time_DE07>  
          <Txn_Type>A</Txn_Type>  
          <Additional_Data_DE48>09F5F4F4F7F5F4F7F7F5</Additional_Data_DE48>  
          <Authorised_by_GPS>N</Authorised_by_GPS>  
          <AVS_Result />  
          <CU_Group />  
          <InstCode>PMT</InstCode>  
          <MTID>0100</MTID>  
          <ProductID>588</ProductID>  
          <Record_Data_DE120 />  
          <SubBIN>44622180</SubBIN>  
          <TLogIDOrg>0</TLogIDOrg>  
          <VL_Group>JISHNU10</VL_Group>  
          <Dom_Fee_Fixed>10.0000</Dom_Fee_Fixed>  
          <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
          <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
          <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
          <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
          <Dom_Fee_Rate>0.5000</Dom_Fee_Rate>  
          <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
          <Additional_Data_DE124 />  
          <CVV2 />  
          <Expiry_Date />  
          <PAN_Sequence_Number />  
          <PIN />  
          <PIN_Enc_Algorithm />  
          <PIN_Format />  
          <PIN_Key_Index />  
          <SendingAttemptCount>1</SendingAttemptCount>  
          <source_bank_ctry />  
          <source_bank_account_format />  
          <source_bank_account />  
          <dest_bank_ctry />  
          <dest_bank_account_format />  
          <dest_bank_account />  
          <GPS_POS_Capability>00010000000001000000000100010011000000000000300CM</GPS_POS_Capability>  
          <GPS_POS_Data>51210003000001x000</GPS_POS_Data>  
          <Acquirer_Reference_Data_031 />  
          <Response_Source />  
          <Response_Source_Why>0</Response_Source_Why>  
          <Message_Source />  
          <Message_Why>5</Message_Why>  
          <traceid_lifecycle>VIS1-20191231-000000000937589</traceid_lifecycle>  
          <PaymentToken_id>0</PaymentToken_id>  
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
          <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
          <ICC_System_Related_Data_DE55 />  
          <Merch_Name>Visa      Test</Merch_Name>  
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
          <auth_type>0</auth_type>  
          <Matching_Txn_ID>0</Matching_Txn_ID>  
          <Reason_ID>0</Reason_ID>  
          <Dispute_Condition />  
          <Network_Chargeback_Reference_Id />  
          <Acquirer_Forwarder_ID>987654</Acquirer_Forwarder_ID>  
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
          <Network_TxnAmt_To_BillAmt_Rate>2000000:6</Network_TxnAmt_To_BillAmt_Rate>  
          <Network_TxnAmt_To_BaseAmt_Rate />  
          <Network_BaseAmt_To_BillAmt_Rate />  
          <POS_Date_DE13>20210709</POS_Date_DE13>  
          <Traceid_Message>VIS1-20191231-000000000937589</Traceid_Message>  
          <Traceid_Original>VIS1-00000000-00000000010</Traceid_Original>  
          <Network_Currency_Conversion_Date />  
          <Mastercard_AdviceReasonCode_DE60 />  
          <Network_Original_Data_Elements_DE90>000100000000010000000001000100110000000000</Network_Original_Data_Elements_DE90>  
          <Visa_ResponseInfo_DE44>1</Visa_ResponseInfo_DE44>  
          <Visa_STIP_Reason_Code>9035</Visa_STIP_Reason_Code>  
          <Network_Issuer_Settle_ID />  
          <Network_Replacement_Amounts_DE95>000000000400000000000000000000000000000000</Network_Replacement_Amounts_DE95>  
          <Visa_POS_Data_DE60>5100060005</Visa_POS_Data_DE60>  
          <Network_Transaction_ID>0000000000937589</Network_Transaction_ID>  
          <Misc_TLV_Data>V1250300030012100000000010</Misc_TLV_Data>  
          <Acquirer_Country>GBR</Acquirer_Country>  
          <Network_Fraud_Data>999</Network_Fraud_Data>  
          <SenderData>0104Adam0703ROM080511A56V10205</SenderData>  
          <ReceiverData>0310John Smith</ReceiverData>  
          <AuthenticationCurrency />       
          <AuthenticationAmountUpper />        
          <AuthenticationMerchantHash />  
          <FxProviderCardholderRate />  
          <SchemeTransactionIdentifier>VIS1WT</SchemeTransactionIdentifier>  
          <TokenUniqueReference />              
          <PaymentTokenPan />  
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Authorisation Response

Below is an example of HTTP response to the above Authorisation request message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soap:Body>  
    <GetTransactionResponse xmlns="http://tempuri.org/">  
      <GetTransactionResult>  
         <Responsestatus>00</Responsestatus>  
         <CurBalance>0</CurBalance>  
         <AvlBalance>100</AvlBalance>  
         <Acknowledgement>1</Acknowledgement>  
         <LoadAmount>50</LoadAmount>  
         <Bill_Amt_Approved>0</Bill_Amt_Approved>  
         <Update_Balance>1</Update_Balance>  
         <New_Balance_Sequence_Exthost>200</New_Balance_Sequence_Exthost>  
         <CVV2_Result>400</CVV2_Result>  
         <CurBalance_GPS_STIP>0</CurBalance_GPS_STIP>  
         <AvlBalance_GPS_STIP>100</AvlBalance_GPS_STIP>  
      </GetTransactionResult>  
    </GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

[Back to Top](#Top)

## 3.4.2 Authorisation Request (Auth Advice)

Below is an example of the HTTP POST body data for a Visa authorisation advice.

Some key elements of this request are:

* The `MTID` value is 0120 and the `Txn_Type` is J, indicating that this is Authorisation Advice matched to an Authorisation Request.
* This type of message is for EHI Mode 3 (Full Service Processing).
* The `Message_Source` value is set to VISA-STIP, indicating that Visa Stand-In processing

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
           <Acquirer_id_DE32>06323232</Acquirer_id_DE32>  
            <ActBal>500.0000</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28 />  
            <Auth_Code_DE38 />  
            <Avl_Bal>161.0000</Avl_Bal>  
            <Bill_Amt>20.0000</Bill_Amt>  
            <Bill_Ccy>826</Bill_Ccy>  
            <BlkAmt>-339.0000</BlkAmt>  
            <Cust_Ref />  
            <FX_Pad>0.0000</FX_Pad>  
            <Fee_Fixed>0.0000</Fee_Fixed>  
            <Fee_Rate>0.0000</Fee_Rate>  
            <LoadSRC />  
            <LoadType />  
            <MCC_Code>8931</MCC_Code>  
            <MCC_Desc />  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42>testMerchanrt  </Merch_ID_DE42>  
            <Merch_Name_DE43>Visa      Test                        GB</Merch_Name_DE43>  
            <Note />  
            <POS_Data_DE22>9010</POS_Data_DE22>  
            <POS_Data_DE61 />  
            <POS_Termnl_DE41>A0000001</POS_Termnl_DE41>  
            <POS_Time_DE12>142152</POS_Time_DE12>  
            <Proc_Code>000000</Proc_Code>  
            <Resp_Code_DE39 />  
            <Ret_Ref_No_DE37>119314935418</Ret_Ref_No_DE37>  
            <Settle_Amt>0.0000</Settle_Amt>  
            <Settle_Ccy />  
            <Status_Code>00</Status_Code>  
            <Token>100467819</Token>  
            <Trans_link>210712935418323232</Trans_link>  
            <Txn_Amt>20.0000</Txn_Amt>  
            <Txn_CCy>826</Txn_CCy>  
            <Txn_Ctry>GBR</Txn_Ctry>  
            <Txn_Desc>Visa      Test                        GB</Txn_Desc>  
            <Txn_GPS_Date>2021-07-12 14:21:54.567</Txn_GPS_Date>  
            <TXn_ID>6151102219</TXn_ID>  
            <Txn_Stat_Code>A</Txn_Stat_Code>  
            <TXN_Time_DE07>0712132152</TXN_Time_DE07>  
            <Txn_Type>J</Txn_Type>  
            <Additional_Data_DE48>09F5F4F4F7F5F4F7F7F5</Additional_Data_DE48>  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group />  
            <InstCode>PMT</InstCode>  
            <MTID>0120</MTID>  
            <ProductID>588</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>44622180</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group />  
            <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
            <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
            <Additional_Data_DE124 />  
            <CVV2 />  
            <Expiry_Date />  
            <PAN_Sequence_Number>000</PAN_Sequence_Number>  
            <PIN />  
            <PIN_Enc_Algorithm />  
            <PIN_Format />  
            <PIN_Key_Index />  
            <SendingAttemptCount>1</SendingAttemptCount>  
            <source_bank_ctry />  
            <source_bank_account_format />  
            <source_bank_account />  
            <dest_bank_ctry />  
            <dest_bank_account_format />  
            <dest_bank_account />  
            <GPS_POS_Capability>00010000000001000000000100010011000000000000300CM</GPS_POS_Capability>  
            <GPS_POS_Data>51210003000001x000</GPS_POS_Data>  
            <Acquirer_Reference_Data_031 />  
            <Response_Source>VISA-STIP </Response_Source>  
            <Response_Source_Why>5</Response_Source_Why>  
            <Message_Source>VISA-STIP </Message_Source>  
            <Message_Why>5</Message_Why>  
            <traceid_lifecycle>VIS1-20191231-000000000937593</traceid_lifecycle>  
            <PaymentToken_id>0</PaymentToken_id>  
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
            <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
            <ICC_System_Related_Data_DE55 />  
            <Merch_Name>Visa      Test</Merch_Name>  
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
            <auth_type>0</auth_type>  
            <Matching_Txn_ID>0</Matching_Txn_ID>  
            <Reason_ID>0</Reason_ID>  
            <Dispute_Condition />  
            <Network_Chargeback_Reference_Id />  
            <Acquirer_Forwarder_ID>987654</Acquirer_Forwarder_ID>  
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
            <Network_TxnAmt_To_BillAmt_Rate>2000000:6</Network_TxnAmt_To_BillAmt_Rate>  
            <Network_TxnAmt_To_BaseAmt_Rate />  
            <Network_BaseAmt_To_BillAmt_Rate />  
            <POS_Date_DE13>20210712</POS_Date_DE13>  
            <Traceid_Message>VIS1-20191231-000000000937593</Traceid_Message>  
            <Traceid_Original>VIS1-00000000-00000000010</Traceid_Original>  
            <Network_Currency_Conversion_Date />  
            <Mastercard_AdviceReasonCode_DE60 />  
            <Network_Original_Data_Elements_DE90>000100000000010000000001000100110000000000</Network_Original_Data_Elements_DE90>  
            <Visa_ResponseInfo_DE44>1</Visa_ResponseInfo_DE44>  
            <Visa_STIP_Reason_Code>9035</Visa_STIP_Reason_Code>  
            <Network_Issuer_Settle_ID />  
            <Network_Replacement_Amounts_DE95>000000000400000000000000000000000000000000</Network_Replacement_Amounts_DE95>  
            <Visa_POS_Data_DE60>5100060005</Visa_POS_Data_DE60>  
            <Network_Transaction_ID>0000000000937593</Network_Transaction_ID>  
            <Misc_TLV_Data>V1250300030012100000000010</Misc_TLV_Data>  
            <Acquirer_Country>GBP</Acquirer_Country>  
            <Network_Fraud_Data>999</Network_Fraud_Data>  
            <SenderData>0104Adam0703ROM080511A56V10205</SenderData>  
            <ReceiverData>0310John Smith</ReceiverData>  
            <AuthenticationCurrency />       
           <AuthenticationAmountUpper />            
           <AuthenticationMerchantHash />  
           <FxProviderCardholderRate />  
           <SchemeTransactionIdentifier>VIS1WT</SchemeTransactionIdentifier>  
            <TokenUniqueReference />              
            <PaymentTokenPan />  
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Authorisation Response (Auth Advice Response)

Below is an example of HTTP response to the above Authorisation advice message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soap:Body>  
    <GetTransactionResponse xmlns="http://tempuri.org/">  
      <GetTransactionResult>  
        <Responsestatus>00</Responsestatus>  
                <CurBalance>0</CurBalance>  
                <AvlBalance>100</AvlBalance>  
                <Acknowledgement>1</Acknowledgement>  
                <LoadAmount>50</LoadAmount>  
                <Bill_Amt_Approved>0</Bill_Amt_Approved>  
                <Update_Balance>1</Update_Balance>  
                <New_Balance_Sequence_Exthost>200</New_Balance_Sequence_Exthost>  
                <CVV2_Result>400</CVV2_Result>  
                <CurBalance_GPS_STIP>0</CurBalance_GPS_STIP>  
                <AvlBalance_GPS_STIP>100</AvlBalance_GPS_STIP>  
      </GetTransactionResult>  
    </GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

[Back to Top](#Top)

## 3.4.3 Authorisation Request (Payment Token Activation)

Below is an example of the HTTP POST body data for an authorisation request for a payment token activation.

Some key elements of this request are:

* The `PaymentTokenActivationMethod` value is set to 1, meaning the method used to activate the payment token is SMS to Mobile.
* The `PaymentTokenType` value is set to SE, meaning that the type of payment token is a Secure Element PAN.
* The `PaymentTokenWallet` value is set to APPLE, meaning that the eWallet payment token belongs is an Apple Pay Wallet.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
            <Acquirer_id_DE32>06001234</Acquirer_id_DE32>  
            <ActBal>0.0000</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28 />  
            <Auth_Code_DE38>189206</Auth_Code_DE38>  
            <Avl_Bal>0.0000</Avl_Bal>  
            <Bill_Amt>0.0000</Bill_Amt>  
            <Bill_Ccy>978</Bill_Ccy>  
            <BlkAmt>0.0000</BlkAmt>  
            <Cust_Ref>HM_the_Queen</Cust_Ref>  
            <FX_Pad>0.0000</FX_Pad>  
            <Fee_Fixed>0.0000</Fee_Fixed>  
            <Fee_Rate>0.0000</Fee_Rate>  
            <LoadSRC />  
            <LoadType />  
            <MCC_Code>6012</MCC_Code>  
            <MCC_Desc>Financial Institutions</MCC_Desc>  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42>400425000000001</Merch_ID_DE42>  
            <Merch_Name_DE43> Visa Tokenisation System Foster City US </Merch_Name_DE43>  
            <Note />  
            <POS_Data_DE22>010</POS_Data_DE22>  
            <POS_Data_DE61>102510900010084063368</POS_Data_DE61>  
            <POS_Termnl_DE41 />  
            <POS_Time_DE12 />  
            <Proc_Code>340000</Proc_Code>  
            <Resp_Code_DE39>00</Resp_Code_DE39>  
            <Ret_Ref_No_DE37 />  
            <Settle_Amt>0.0000</Settle_Amt>  
            <Settle_Ccy>978</Settle_Ccy>  
            <Status_Code>00</Status_Code>  
            <Token>499040929</Token>  
            <Trans_link>180228044470015611</Trans_link>  
            <Txn_Amt>0.0000</Txn_Amt>  
            <Txn_CCy>840</Txn_CCy>  
            <Txn_Ctry>USA</Txn_Ctry>  
            <Txn_Desc>Visa Provisioning Service GB</Txn_Desc>  
            <Txn_GPS_Date>2021-03-18 15:08:14.650</Txn_GPS_Date>  
            <TXn_ID>1250779057</TXn_ID>  
            <Txn_Stat_Code>A</Txn_Stat_Code>  
            <TXN_Time_DE07>0318150814</TXN_Time_DE07>  
            <Txn_Type>A</Txn_Type>  
      <Additional_Data_DE48>038T230221260310333200101C061150110030273</Additional_Data_DE48>  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group>PMT-CU-001</CU_Group>  
            <InstCode>PMT</InstCode>  
            <MTID>0100</MTID>  
            <ProductID>93305</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>51000028</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group>TST-VL-001</VL_Group>  
            <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
            <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
            <Additional_Data_DE124>048ACD0000172680392393806  18022813441#########3456</Additional_Data_DE124>  
            <CVV2 />  
            <Expiry_Date />  
            <PAN_Sequence_Number />  
            <PIN>0</PIN>  
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
    <GPS_POS_Capability>0000000000000000000000000000000000100000000990010</GPS_POS_Capability>  
            <GPS_POS_Data>9908000800000Nx000</GPS_POS_Data>  
            <Acquirer_Reference_Data_031 />  
            <Response_Source />  
            <Response_Source_Why>71</Response_Source_Why>  
            <Message_Source />  
            <Message_Why>0</Message_Why>  
            <traceid_lifecycle>VIS1-20210318-381077544887139</traceid_lifecycle>  
            <Balance_Sequence>0</Balance_Sequence>  
            <Balance_Sequence_Exthost>0</Balance_Sequence_Exthost>  
            <PaymentToken_id>12365432</PaymentToken_id>  
            <PaymentToken_creator>VISA-T</PaymentToken_creator>  
            <PaymentToken_expdate />  
            <PaymentToken_type>SE</PaymentToken_type>  
            <PaymentToken_status>00</PaymentToken_status>  
            <PaymentToken_creatorStatus />  
            <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
            <PaymentToken_deviceType>W</PaymentToken_deviceType>  
            <PaymentToken_lang />  
            <PaymentToken_deviceTelNum>447912345678</PaymentToken_deviceTelNum>  
            <PaymentToken_deviceIp>192.0.0.8</PaymentToken_deviceIp>  
            <PaymentToken_deviceId>01234B234C1230011230054848300695D86E17C703548A4A</PaymentToken_deviceId>  
            <PaymentToken_deviceName>Test Apple Wa</PaymentToken_deviceName>  
       <PaymentToken_activationCode>393805</PaymentToken_activationCode>  
       <PaymentToken_activationExpiry>2021-03-18 15:08:14.650</PaymentToken_activationExpiry>  
       <PaymentToken_activationMethod>1</PaymentToken_activationMethod>  
       <PaymentToken_activationMethodData>+447912345678</PaymentToken_activationMethodData>  
            <ICC_System_Related_Data_DE55 />  
            <Merch_Name>Visa</Merch_Name>  
            <Merch_Street />  
            <Merch_City>Test</Merch_City>  
            <Merch_Region>GB</Merch_Region>  
            <Merch_Postcode>63368</Merch_Postcode>  
            <Merch_Country>USA</Merch_Country>  
            <Merch_Tel />  
            <Merch_URL />  
            <Merch_Name_Other />  
            <Merch_Net_id />  
            <Merch_Tax_id />  
            <Merch_Contact />  
            <auth_type>F</auth_type>  
            <auth_expdate_utc>>2021-03-18 15:08:14.650</auth_expdate_utc>  
            <Matching_Txn_ID />  
            <Reason_ID />  
            <Dispute_Condition />  
            <Network_Chargeback_Reference_Id />  
            <Acquirer_Forwarder_ID>000403750</Acquirer_Forwarder_ID>  
            <Currency_Code_Fee />  
            <Currency_Code_Fee_Settlement />  
            <Interchange_Amount_Fee />  
            <Interchange_Amount_Fee_Settlement />  
            <Clearing_Process_Date />  
            <Settlement_Date />  
            <DCC_Indicator>0</DCC_Indicator>  
            <multi_part_txn />  
            <multi_part_txn_final />  
            <multi_part_number />  
            <multi_part_count />  
            <SettlementIndicator />  
            <Traceid_Message>VIS1-20191231-000000000937589</Traceid_Message>  
            <Traceid_Original />  
            <Network_Transaction_ID />  
            <POS_Date_DE13>20210318</POS_Date_DE13>  
            <Network_Currency_Conversion_Date>2021-03-18</Network_Currency_Conversion_Date>  
            <Network_TxnAmt_To_BillAmt_Rate>9229970:7</Network_TxnAmt_To_BillAmt_Rate>  
            <Network_TxnAmt_To_BaseAmt_Rate />  
            <Network_BaseAmt_To_BillAmt_Rate />  
            <Network_Original_Data_Elements_DE90 />  
            <Network_Replacement_Amounts_DE95 />  
            <Network_Issuer_Settle_ID />  
            <Visa_ResponseInfo_DE44 />  
            <Visa_POS_Data_DE60 />  
            <Visa_STIP_Reason_Code />  
            <Mastercard_AdviceReasonCode_DE60 />  
            <Misc_TLV_Data />  
            <Acquirer_Country>GBP</Acquirer_Country>  
            <PaymentToken_PanSource>2</PaymentToken_PanSource>  
            <Network_Fraud_Data>999</Network_Fraud_Data>  
            <SenderData>0104Adam0703ROM080511A56V10205</SenderData>  
            <ReceiverData>0310John Smith</ReceiverData>  
            <AuthenticationCurrency />       
            <AuthenticationAmountUpper />        
            <AuthenticationMerchantHash />  
            <FxProviderCardholderRate />  
            <SchemeTransactionIdentifier />  
            <TokenUniqueReference>DNITHE582599999942043245</TokenUniqueReference>          
            <PaymentTokenPan>5372403458767765</PaymentTokenPan>  
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

[Back to Top](#Top)