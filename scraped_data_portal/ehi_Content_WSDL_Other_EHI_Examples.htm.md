# 3.7 Other EHI Examples

This section provides other examples of common transaction messages and responses. It includes the following examples:

* [Example Payment Message](#Example5)
* [Example Fee (Financial) Message](#Example6)
* [Example Card Expiry Message](#Example7)
* [Example Tokenisation Messages](#Example8)
* [Example Balance Enquiry Message](#ExampleBalance)
* [Examples of Amount Signs](#Examples)

## 3.7.1 Example Payment Message

Payment messages are information that a Payment has already happened  (i.e. it is not happening at the moment, and you cannot decline it.  It is an advice).

Below is an example of the HTTP POST body data for a payment advice notification.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
          <Acquirer_id_DE32>06019869</Acquirer_id_DE32>  
          <ActBal>442.0000</ActBal>  
          <Additional_Amt_DE54 />  
          <Amt_Tran_Fee_DE28 />  
          <Auth_Code_DE38>163746</Auth_Code_DE38>  
          <Avl_Bal>262.0000</Avl_Bal>  
          <Bill_Amt>-10.0000</Bill_Amt>  
          <Bill_Ccy>392</Bill_Ccy>  
          <BlkAmt>-180.0000</BlkAmt>  
          <Cust_Ref>s035nPHAD15oxK0yoo4Zj2</Cust_Ref>  
          <FX_Pad>0.0000</FX_Pad>  
          <Fee_Fixed>0.0000</Fee_Fixed>  
          <Fee_Rate>0.0000</Fee_Rate>  
          <LoadSRC />  
          <LoadType />  
          <MCC_Code>4111</MCC_Code>  
          <MCC_Desc>Commuter Transport, Ferries</MCC_Desc>  
          <MCC_Pad>0.0000</MCC_Pad>  
          <Merch_ID_DE42>CARD ACCPT IDC</Merch_ID_DE42>  
          <Merch_Name_DE43>Mastercard TA          St. Louis     MO </Merch_Name_DE43>  
          <Note />  
          <POS_Data_DE22>070</POS_Data_DE22>  
          <POS_Data_DE61>1000000000300826SW1H 0TL</POS_Data_DE61>  
          <POS_Termnl_DE41>TERM0015</POS_Termnl_DE41>  
          <POS_Time_DE12>151242</POS_Time_DE12>  
          <Proc_Code>000000</Proc_Code>  
          <Resp_Code_DE39>00</Resp_Code_DE39>  
          <Ret_Ref_No_DE37>000000694130</Ret_Ref_No_DE37>  
          <Settle_Amt>10.0000</Settle_Amt>  
          <Settle_Ccy>392</Settle_Ccy>  
          <Status_Code>00</Status_Code>  
          <Token>837513924</Token>  
          <Trans_link>210408694416019869</Trans_link>  
          <Txn_Amt>0.1000</Txn_Amt>  
          <Txn_CCy>840</Txn_CCy>  
          <Txn_Ctry>GBR</Txn_Ctry>  
          <Txn_Desc>Mastercard TA          St. Louis     MO </Txn_Desc>  
          <Txn_GPS_Date>2021-04-08 15:12:50.907</Txn_GPS_Date>  
          <TXn_ID>6150900956</TXn_ID>  
          <Txn_Stat_Code>A</Txn_Stat_Code>  
          <TXN_Time_DE07>0408151242</TXN_Time_DE07>  
          <Txn_Type>A</Txn_Type>  
          <Additional_Data_DE48>192T23022126031033044+4As7jPVqipH7RxD6nmCHg3ePZd6qW56JPMScSSkF8E=33540101C021655743500719964780304231206115011003027308020534110000100000W61050000164040400711250C 51V 18C 751301030520202049203619</Additional_Data_DE48>  
          <Authorised_by_GPS>N</Authorised_by_GPS>  
          <AVS_Result />  
          <CU_Group>TESTAUTO_P</CU_Group>  
          <InstCode>CORP</InstCode>  
          <MTID>0100</MTID>  
          <ProductID>94</ProductID>  
          <Record_Data_DE120 />  
          <SubBIN>54281200</SubBIN>  
          <TLogIDOrg>0</TLogIDOrg>  
          <VL_Group>CSL-VL-002</VL_Group>  
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
          <GPS_POS_Capability>00000000001000000000000100000010000000000002130C0</GPS_POS_Capability>  
          <GPS_POS_Data>0171000300000Nx000</GPS_POS_Data>  
          <Acquirer_Reference_Data_031 />  
          <Response_Source />  
          <Response_Source_Why>0</Response_Source_Why>  
          <Message_Source />  
          <Message_Why>0</Message_Why>  
          <traceid_lifecycle>BNET-20210408-MCC770613</traceid_lifecycle>  
          <PaymentToken_id>13067</PaymentToken_id>  
          <PaymentToken_creator />  
          <PaymentToken_expdate>2023-12-31</PaymentToken_expdate>  
          <PaymentToken_type />  
          <PaymentToken_status>00</PaymentToken_status>  
          <PaymentToken_creatorStatus>A</PaymentToken_creatorStatus>  
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
          <Merch_Name>Mastercard TA</Merch_Name>  
          <Merch_Street />  
          <Merch_City>St. Louis</Merch_City>  
          <Merch_Region>MO</Merch_Region>  
          <Merch_Postcode>SW1H 0TL</Merch_Postcode>  
          <Merch_Country>GBR</Merch_Country>  
          <Merch_Tel />  
          <Merch_URL />  
          <Merch_Name_Other />  
          <Merch_Net_id />  
          <Merch_Tax_id>0</Merch_Tax_id>  
          <Merch_Contact />  
          <auth_type>F</auth_type>  
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
          <Network_TxnAmt_To_BillAmt_Rate>1000000:6</Network_TxnAmt_To_BillAmt_Rate>  
          <Network_TxnAmt_To_BaseAmt_Rate />  
          <Network_BaseAmt_To_BillAmt_Rate />  
          <POS_Date_DE13>20210408</POS_Date_DE13>  
          <Traceid_Message>BNET-20210408-MCC770613</Traceid_Message>  
          <Traceid_Original />  
          <Network_Currency_Conversion_Date>2021-04-08</Network_Currency_Conversion_Date>  
          <Mastercard_AdviceReasonCode_DE60 />  
          <Network_Original_Data_Elements_DE90 />  
          <Visa_ResponseInfo_DE44 />  
          <Visa_STIP_Reason_Code />  
          <Network_Issuer_Settle_ID />  
          <Network_Replacement_Amounts_DE95 />  
          <Visa_POS_Data_DE60 />  
          <Network_Transaction_ID>MCC7706130408</Network_Transaction_ID>  
          <Misc_TLV_Data />  
          <Acquirer_Country>GBR</Acquirer_Country>  
          <PaymentToken_PanSource>2</PaymentToken_PanSource>  
          <Network_Fraud_Data>999</Network_Fraud_Data>  
          <SenderData>0104Adam0703ROM080511A56V10205</SenderData>  
          <ReceiverData>0310John Smith</ReceiverData>  
          <AuthenticationCurrency />           
          <AuthenticationAmountUpper />            
          <AuthenticationMerchantHash />  
          <FxProviderCardholderRate />    
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Payment Response

Below is an example of HTTP response to the above Payment advice message.

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

## 3.7.2 Example Fee (Financial) Message

Below is an example of the HTTP POST body data for a financial fee request.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
            <Acquirer_id_DE32 />  
            <ActBal>156.6300</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28 />  
            <Auth_Code_DE38 />  
            <Avl_Bal>137.6300</Avl_Bal>  
            <Bill_Amt>0.0000</Bill_Amt>  
            <Bill_Ccy>826</Bill_Ccy>  
            <BlkAmt>-19.0000</BlkAmt>  
            <Cust_Ref>9841867703</Cust_Ref>  
            <FX_Pad>0.0000</FX_Pad>  
            <Fee_Fixed>1.5000</Fee_Fixed>  
            <Fee_Rate>0.0000</Fee_Rate>  
            <LoadSRC>0</LoadSRC>  
            <LoadType>0</LoadType>  
            <MCC_Code />  
            <MCC_Desc />  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42 />  
            <Merch_Name_DE43 />  
            <Note>Fees</Note>  
            <POS_Data_DE22 />  
            <POS_Data_DE61 />  
            <POS_Termnl_DE41 />  
            <POS_Time_DE12 />  
            <Proc_Code>083999</Proc_Code>  
            <Resp_Code_DE39 />  
            <Ret_Ref_No_DE37 />  
            <Settle_Amt>0.0000</Settle_Amt>  
            <Settle_Ccy>826</Settle_Ccy>  
            <Status_Code>00</Status_Code>  
            <Token>936270603</Token>  
            <Trans_link>5071773234</Trans_link>  
            <Txn_Amt>0.0000</Txn_Amt>  
            <Txn_CCy>826</Txn_CCy>  
            <Txn_Ctry />  
            <Txn_Desc> QCF - Quasi cash transaction Fee. Posted date - Feb 13 2020  1:12AM</Txn_Desc>  
            <Txn_GPS_Date>2020-02-13 01:12:32.407</Txn_GPS_Date>  
            <TXn_ID>5071773234</TXn_ID>  
            <Txn_Stat_Code>S</Txn_Stat_Code>  
            <TXN_Time_DE07 />  
            <Txn_Type>P</Txn_Type>  
            <Additional_Data_DE48 />  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group>ABC-CU-001</CU_Group>  
            <InstCode>ABC</InstCode>  
            <MTID />  
            <ProductID>4368</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>51234500</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group>ABC-VL-001</VL_Group>  
            <Dom_Fee_Fixed>1.5000</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
            <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
            <Additional_Data_DE124 />  
            <CVV2 />  
            <Expiry_Date>0</Expiry_Date>  
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
            <GPS_POS_Capability />  
            <GPS_POS_Data />  
            <Acquirer_Reference_Data_031 />  
            <Response_Source />  
            <Response_Source_Why>0</Response_Source_Why>  
            <Message_Source />  
            <Message_Why>0</Message_Why>  
            <traceid_lifecycle />  
            <Balance_Sequence />  
            <Balance_Sequence_Exthost />  
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
            <PaymentToken_activationMethod />  
            <PaymentToken_activationMethodData />  
            <ICC_System_Related_Data_DE55 />  
            <Merch_Name />  
            <Merch_Street />  
            <Merch_City />  
            <Merch_Region />  
            <Merch_Postcode />  
            <Merch_Country />  
            <Merch_Tel />  
            <Merch_URL />  
            <Merch_Name_Other />  
            <Merch_Net_id />  
            <Merch_Tax_id />  
            <Merch_Contact />  
            <auth_type />  
            <auth_expdate_utc />  
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
            <Settlement_Date />  
            <DCC_Indicator />  
            <multi_part_txn />  
            <multi_part_txn_final />  
            <multi_part_number />  
            <multi_part_count />  
            <SettlementIndicator>0</SettlementIndicator>  
            <Traceid_Message />  
            <Traceid_Original />  
            <Network_Transaction_ID />  
            <POS_Date_DE13 />  
            <Network_Currency_Conversion_Date />  
            <Network_TxnAmt_To_BillAmt_Rate />  
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
            <Acquirer_Country />  
            <PaymentToken_PanSource />  
            <Network_Fraud_Data />  
            <SenderData />  
            <ReceiverData />  
            <AuthenticationCurrency />           
           <AuthenticationAmountUpper />            
           <AuthenticationMerchantHash />  
           <FxProviderCardholderRate />             
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Fee (Financial) Response

Below is an example of HTTP response to the above Fee(Financial) Request message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soap:Body>  
    <GetTransactionResponse xmlns="http://tempuri.org/">  
      <GetTransactionResult>  
        <Responsestatus>00</Responsestatus>  
        <CurBalance>0.5</CurBalance>  
        <AvlBalance>0.5</AvlBalance>  
        <Acknowledgement>1</Acknowledgement>  
        <LoadAmount>0.00</LoadAmount>  
      </GetTransactionResult>  
    </GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

## 3.7.3 Example Card Expiry Message

Card Expiry messages inform you that a Card has Expired.  (i.e. it is not happening at the moment, and you cannot decline it. It is an advice.)

Here â`Bill_Amt`â is set to either:

* â0.00â if the Card Product âBreakage feeâ flag is not set
* The amount remaining on the card, if Card Product âBreakage feeâ flag is set. Below â-5.89â indicates that a positive balance of â5.89â was on the card.

### Card Expiry Request

Below is an example of the HTTP POST body data for a card expiry advice notification.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction xmlns="http://tempuri.org/">  
            <Acquirer_id_DE32 />  
            <ActBal>0.0000</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28 />  
            <Auth_Code_DE38 />  
            <Avl_Bal>0.0000</Avl_Bal>  
            <Bill_Amt>-5.8900</Bill_Amt>  
            <Bill_Ccy>826</Bill_Ccy>  
            <BlkAmt>0.0000</BlkAmt>  
            <Cust_Ref>4050b028-abcd</Cust_Ref>  
            <FX_Pad>0.0000</FX_Pad>  
            <Fee_Fixed>0.0000</Fee_Fixed>  
            <Fee_Rate>0.0000</Fee_Rate>  
            <LoadSRC />  
            <LoadType />  
            <MCC_Code />  
            <MCC_Desc />  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42 />  
            <Merch_Name_DE43 />  
            <Note />  
            <POS_Data_DE22 />  
            <POS_Data_DE61 />  
            <POS_Termnl_DE4 />  
            <POS_Time_DE12 />  
            <Proc_Code>220000</Proc_Code>  
            <Resp_Code_DE39 />  
            <Ret_Ref_No_DE37 />  
            <Settle_Amt>5.8900</Settle_Amt>  
            <Settle_Ccy>826</Settle_Ccy>  
            <Status_Code>54</Status_Code>  
            <Token>663368509</Token>  
            <Trans_link>5960771322</Trans_link>  
            <Txn_Amt>5.8900</Txn_Amt>  
            <Txn_CCy>826</Txn_CCy>  
            <Txn_Ctry />  
            <Txn_Desc>Card Expiry</Txn_Desc>  
            <Txn_GPS_Date>2020-07-15 01:03:28.330</Txn_GPS_Date>  
            <TXn_ID>5960771322</TXn_ID>  
            <Txn_Stat_Code>S</Txn_Stat_Code>  
            <TXN_Time_DE07 />  
            <Txn_Type>Y</Txn_Type>  
            <Additional_Data_DE48 />  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group>ABC-CU-001</CU_Group>  
            <InstCode>ABC</InstCode>  
            <MTID />  
            <ProductID>2114</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>59833440</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group>ABC-VL-002</VL_Group>  
            <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
            <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
            <Additional_Data_DE124 />  
            <CVV2 />  
            <Expiry_Date>0</Expiry_Date>  
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
            <GPS_POS_Capability />  
            <GPS_POS_Data />  
            <Acquirer_Reference_Data_031 />  
            <Response_Source />  
            <Response_Source_Why>0</Response_Source_Why>  
            <Message_Source />  
            <Message_Why>0</Message_Why>  
            <traceid_lifecycle />  
            <Balance_Sequence />  
            <Balance_Sequence_Exthost />  
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
            <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
            <PaymentToken_activationMethodData />  
            <ICC_System_Related_Data_DE55 />  
            <Merch_Name />  
            <Merch_Street />  
            <Merch_City />  
            <Merch_Region />  
            <Merch_Postcode />  
            <Merch_Country />  
            <Merch_Tel />  
            <Merch_URL />  
            <Merch_Name_Other />  
            <Merch_Net_id />  
            <Merch_Tax_id>0</Merch_Tax_id>  
            <Merch_Contact />  
            <auth_type />  
            <auth_expdate_utc />  
            <Matching_Txn_ID />  
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
            <multi_part_txn />  
            <multi_part_txn_final />  
            <multi_part_number />  
            <multi_part_count />  
            <SettlementIndicator>0</SettlementIndicator>  
            <Traceid_Message />  
            <Traceid_Original />  
            <Network_Transaction_ID />  
            <POS_Date_DE13 />  
            <Network_Currency_Conversion_Date />  
            <Network_TxnAmt_To_BillAmt_Rate />  
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
            <Acquirer_Country />  
            <PaymentToken_PanSource />  
            <Network_Fraud_Data />  
            <SenderData />  
            <ReceiverData />  
            <AuthenticationCurrency />       
            <AuthenticationAmountUpper />        
            <AuthenticationMerchantHash />  
            <FxProviderCardholderRate />              
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Card Expiry Response

Below is an example of HTTP response to the above Card Expiry Advice message:

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soap:Body>  
    <GetTransactionResponse xmlns="http://tempuri.org/">  
      <GetTransactionResult>  
        <Responsestatus>00</Responsestatus>  
        <CurBalance />  
        <AvlBalance />  
        <Acknowledgement>1</Acknowledgement>  
        <LoadAmount>0.00</LoadAmount>  
      </GetTransactionResult>  
    </GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

## 3.7.4 Example Tokenisation Messages

Below are examples of typical EHI messages sent during the process of provisioning and activating a payment token (digital PAN) for use on a mobile device or merchant website. For more information on tokenisation, refer to the Tokenisation Guide.

If you want to receive token type messages via EHI, please contact your Implementation Manager to enable this service.

### Token Authorisation Requests (TAR) Request

Below is an example of the HTTP POST body data for a token authorisation request (TAR) notification. This message is sent when a token service provider requests authorisation from Thredd to set up a token.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
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
         <Bill_Ccy>826</Bill_Ccy>  
         <BlkAmt>0.0000</BlkAmt>  
         <Cust_Ref />  
         <FX_Pad>0.0000</FX_Pad>  
         <Fee_Fixed>0.0000</Fee_Fixed>  
         <Fee_Rate>0.0000</Fee_Rate>  
         <LoadSRC />  
         <LoadType />  
         <MCC_Code>6012</MCC_Code>  
         <MCC_Desc>Financial Institutions</MCC_Desc>  
         <MCC_Pad>0.0000</MCC_Pad>  
         <Merch_ID_DE42>400425000000001</Merch_ID_DE42>  
         <Merch_Name_DE43>Visa Tokenisation System Foster City US</Merch_Name_DE43>  
         <Note />  
         <POS_Data_DE22>0000</POS_Data_DE22>  
         <POS_Data_DE61 />  
         <POS_Termnl_DE41 />  
         <POS_Time_DE12 />  
         <Proc_Code>330000</Proc_Code>  
         <Resp_Code_DE39>00</Resp_Code_DE39>  
         <Ret_Ref_No_DE37>102300045678</Ret_Ref_No_DE37>  
         <Settle_Amt>0.0000</Settle_Amt>  
         <Settle_Ccy>826</Settle_Ccy>  
         <Status_Code>00</Status_Code>  
         <Token>123456789</Token>  
         <Trans_link>210318077635001234</Trans_link>  
         <Txn_Amt>0.0000</Txn_Amt>  
         <Txn_CCy>840</Txn_CCy>  
         <Txn_Ctry>GBR</Txn_Ctry>  
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
         <Dom_Fee_Fixed>0.0000</Dom_Fee_Fixed>  
         <Non_Dom_Fee_Fixed>0.0000</Non_Dom_Fee_Fixed>  
         <Fx_Fee_Fixed>0.0000</Fx_Fee_Fixed>  
         <Other_Fee_Amt>0.0000</Other_Fee_Amt>  
         <Fx_Fee_Rate>0.0000</Fx_Fee_Rate>  
         <Dom_Fee_Rate>0.0000</Dom_Fee_Rate>  
         <Non_Dom_Fee_Rate>0.0000</Non_Dom_Fee_Rate>  
         <Additional_Data_DE124 />  
         <CVV2 />  
         <Expiry_Date>2304</Expiry_Date>  
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
         <GPS_POS_Capability>0000000000000000000000000000000000100000000990010</GPS_POS_Capability>  
         <GPS_POS_Data>9908000800000Nx000</GPS_POS_Data>  
         <Acquirer_Reference_Data_031 />  
         <Response_Source />  
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
         <ICC_System_Related_Data_DE55 />  
         <Merch_Name>Visa Provisioning Service</Merch_Name>  
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
         <Settlement_Date />  
         <DCC_Indicator />  
         <multi_part_txn />  
         <multi_part_txn_final />  
         <multi_part_number />  
         <multi_part_count />  
         <SettlementIndicator />  
         <Traceid_Message />  
         <Traceid_Original />  
         <Network_Transaction_ID />  
         <POS_Date_DE13 />  
         <Network_Currency_Conversion_Date />  
         <Network_TxnAmt_To_BillAmt_Rate />  
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
         <Acquirer_Country />  
         <PaymentToken_PanSource />  
         <Network_Fraud_Data />  
         <SenderData />  
         <ReceiverData />  
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

### Token Authorisation Requests (TAR) Response

Below is an example of HTTP response to the above TAR advice message:

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <soap:Body>  
    <GetTransactionResponse xmlns="http://tempuri.org/">  
      <GetTransactionResult>  
        <Responsestatus>00</Responsestatus>  
        <CurBalance />  
        <AvlBalance />  
        <Acknowledgement>1</Acknowledgement>  
        <LoadAmount />  
      </GetTransactionResult>  
    </GetTransactionResponse>  
  </soap:Body>  
</soap:Envelope>
```

### Token Event Notification (TEN) Request

Below is an example of the HTTP POST body data for a token completion notification (TEN). This message is sent when a token service provider notifies Thredd of a change to the token, for example: activation, status change or deletion.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
   <s:Body>  
      <GetTransaction xmlns="http://tempuri.org/">  
         <Acquirer_id_DE32 />  
         <ActBal>0.0000</ActBal>  
         <Additional_Amt_DE54 />  
         <Amt_Tran_Fee_DE28 />  
         <Auth_Code_DE38 />  
         <Avl_Bal>0.0000</Avl_Bal>  
         <Bill_Amt>0.0000</Bill_Amt>  
         <Bill_Ccy>826</Bill_Ccy>  
         <BlkAmt>0.0000</BlkAmt>  
         <Cust_Ref />  
         <FX_Pad>0.0000</FX_Pad>  
         <Fee_Fixed>0.0000</Fee_Fixed>  
         <Fee_Rate>0.0000</Fee_Rate>  
         <LoadSRC />  
         <LoadType />  
         <MCC_Code />  
         <MCC_Desc />  
         <MCC_Pad>0.0000</MCC_Pad>  
         <Merch_ID_DE42>VisaTokenSystem</Merch_ID_DE42>  
         <Merch_Name_DE43>Visa Tokenisation System Foster City US</Merch_Name_DE43>  
         <Note>Success:</Note>  
         <POS_Data_DE22>1000</POS_Data_DE22>  
         <POS_Data_DE61 />  
         <POS_Termnl_DE41 />  
         <POS_Time_DE12 />  
         <Proc_Code>360000</Proc_Code>  
         <Resp_Code_DE39>00</Resp_Code_DE39>  
         <Ret_Ref_No_DE37>102300045678</Ret_Ref_No_DE37>  
         <Settle_Amt>0.0000</Settle_Amt>  
         <Settle_Ccy />  
         <Status_Code>00</Status_Code>  
         <Token>123456789</Token>  
         <Trans_link>210318077635</Trans_link>  
         <Txn_Amt>0.0000</Txn_Amt>  
         <Txn_CCy>840</Txn_CCy>  
         <Txn_Ctry>USA</Txn_Ctry>  
         <Txn_Desc>Visa Tokenisation System</Txn_Desc>  
         <Txn_GPS_Date>2021-03-18 15:08:15.223</Txn_GPS_Date>  
         <TXn_ID>1250779094</TXn_ID>  
         <Txn_Stat_Code>A</Txn_Stat_Code>  
         <TXN_Time_DE07>0318150814</TXN_Time_DE07>  
         <Txn_Type>J</Txn_Type>  
         <Additional_Data_DE48 />  
         <Authorised_by_GPS>N</Authorised_by_GPS>  
         <AVS_Result />  
         <CU_Group />  
         <InstCode>RAI</InstCode>  
         <MTID>0620</MTID>  
         <ProductID>5877</ProductID>  
         <Record_Data_DE120 />  
         <SubBIN>45967201</SubBIN>  
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
         <Expiry_Date>2304</Expiry_Date>  
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
         <GPS_POS_Capability>000100000000000000000000000000000000000000000001M</GPS_POS_Capability>  
         <GPS_POS_Data>10F0000000000Nx000</GPS_POS_Data>  
         <Acquirer_Reference_Data_031 />  
         <Response_Source>UNKNOWN</Response_Source>  
         <Response_Source_Why>0</Response_Source_Why>  
         <Message_Source>VISA-T</Message_Source>  
         <Message_Why>71</Message_Why>  
         <traceid_lifecycle>VIS1-20210318-381077544887139</traceid_lifecycle>  
         <PaymentToken_id>12365432</PaymentToken_id>  
         <PaymentToken_creator>VISA-T</PaymentToken_creator>  
         <PaymentToken_expdate>2023-12-31</PaymentToken_expdate>  
         <PaymentToken_type>SE</PaymentToken_type>  
         <PaymentToken_status>00</PaymentToken_status>  
         <PaymentToken_creatorStatus>A</PaymentToken_creatorStatus>  
         <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
         <PaymentToken_deviceType>W</PaymentToken_deviceType>  
         <PaymentToken_lang>en</PaymentToken_lang>  
         <PaymentToken_deviceTelNum>47912345678</PaymentToken_deviceTelNum>  
         <PaymentToken_deviceIp>192.0.0.8</PaymentToken_deviceIp>  
         <PaymentToken_deviceId>01234B234C1230011230054848300695D86E17C703548A4A</PaymentToken_deviceId>  
         <PaymentToken_deviceName>Test Apple Wa</PaymentToken_deviceName>  
         <PaymentToken_activationCode />  
         <PaymentToken_activationExpiry />  
         <PaymentToken_activationMethodData />  
         <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
         <ICC_System_Related_Data_DE55 />  
         <Merch_Name>Visa Tokenisation System</Merch_Name>  
         <Merch_Street />  
         <Merch_City>Test City</Merch_City>  
         <Merch_Region>TA</Merch_Region>  
         <Merch_Postcode>12345</Merch_Postcode>  
         <Merch_Country>USA</Merch_Country>  
         <Merch_Tel />  
         <Merch_URL />  
         <Merch_Name_Other />  
         <Merch_Net_id />  
         <Merch_Tax_id>0</Merch_Tax_id>  
         <Merch_Contact />  
         <auth_type />  
         <auth_expdate_utc />  
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
         <Settlement_Date />  
         <DCC_Indicator />  
         <multi_part_txn />  
         <multi_part_txn_final />  
         <multi_part_number />  
         <multi_part_count />  
         <SettlementIndicator />  
         <Traceid_Message />  
         <Traceid_Original />  
         <Network_Transaction_ID />  
         <POS_Date_DE13 />  
         <Network_Currency_Conversion_Date />  
         <Network_TxnAmt_To_BillAmt_Rate />  
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
         <Acquirer_Country />  
         <PaymentToken_PanSource />  
         <Network_Fraud_Data />  
         <SenderData />  
         <ReceiverData />  
         <SchemeTransactionIdentifier />  
         <TokenUniqueReference>DNITHE582599999942043245</TokenUniqueReference>          
         <PaymentTokenPan>5372403458767765</PaymentTokenPan>  
      </GetTransaction>  
   </s:Body>  
</s:Envelope>
```

### Activation Code Notification (ACN) Request

Below is an example of the HTTP POST body data for a token Activation Code Network notification (ACN). This message contains the One-Time Password (OTP) used to verify the cardholder.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
   <s:Body>  
      <GetTransaction xmlns="http://tempuri.org/">  
         <Acquirer_id_DE32>06423378</Acquirer_id_DE32>  
         <ActBal>0.0000</ActBal>  
         <Additional_Amt_DE54 />  
         <Amt_Tran_Fee_DE28 />  
         <Auth_Code_DE38 />  
         <Avl_Bal>0.0000</Avl_Bal>  
         <Bill_Amt>0.0000</Bill_Amt>  
         <Bill_Ccy />  
         <BlkAmt>0.0000</BlkAmt>  
         <Cust_Ref />  
         <FX_Pad>0.0000</FX_Pad>  
         <Fee_Fixed>0.0000</Fee_Fixed>  
         <Fee_Rate>0.0000</Fee_Rate>  
         <LoadSRC />  
         <LoadType />  
         <MCC_Code>6012</MCC_Code>  
         <MCC_Desc />  
         <MCC_Pad>0.0000</MCC_Pad>  
         <Merch_ID_DE42>VisaTokenSystem</Merch_ID_DE42>  
         <Merch_Name_DE43>Visa Tokenisation System Foster City US</Merch_Name_DE43>  
         <Note>Sent VDEP API Token Activation 123456758473.</Note>  
         <POS_Data_DE22 />  
         <POS_Data_DE61 />  
         <POS_Termnl_DE41>VDEP_API</POS_Termnl_DE41>  
         <POS_Time_DE12 />  
         <Proc_Code>340000</Proc_Code>  
         <Resp_Code_DE39 />  
         <Ret_Ref_No_DE37>11107115</Ret_Ref_No_DE37>  
         <Settle_Amt>0.0000</Settle_Amt>  
         <Settle_Ccy />  
         <Status_Code>00</Status_Code>  
         <Token>123045451</Token>  
         <Trans_link>210316107115423378</Trans_link>  
         <Txn_Amt>0.0000</Txn_Amt>  
         <Txn_CCy />  
         <Txn_Ctry>USA</Txn_Ctry>  
         <Txn_Desc>Visa Tokenisation System</Txn_Desc>  
         <Txn_GPS_Date>2021-03-16 14:47:00.837</Txn_GPS_Date>  
         <TXn_ID>1234595471</TXn_ID>  
         <Txn_Stat_Code>A</Txn_Stat_Code>  
         <TXN_Time_DE07>0101120000</TXN_Time_DE07>  
         <Txn_Type>J</Txn_Type>  
         <Additional_Data_DE48>VDEP API Token Activation, 'x-request-id='a2019024-d477-42b5-a0d3-1a1a54681502</Additional_Data_DE48>  
         <Authorised_by_GPS>N</Authorised_by_GPS>  
         <AVS_Result />  
         <CU_Group />  
         <InstCode>ABC</InstCode>  
         <MTID>0120</MTID>  
         <ProductID>5877</ProductID>  
         <Record_Data_DE120 />  
         <SubBIN>45678901</SubBIN>  
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
         <Expiry_Date>0</Expiry_Date>  
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
         <GPS_POS_Capability>0000000010010000100000000000000000100000000001100</GPS_POS_Capability>  
         <GPS_POS_Data>10 0 0 00 000</GPS_POS_Data>  
         <Acquirer_Reference_Data_031 />  
         <Response_Source />  
         <Response_Source_Why>0</Response_Source_Why>  
         <Message_Source>VISA-T</Message_Source>  
         <Message_Why>0</Message_Why>  
         <traceid_lifecycle>VDEP a2019024-d477-42b5-a0d3-1a1a54681502</traceid_lifecycle>  
         <PaymentToken_id>26623376</PaymentToken_id>  
         <PaymentToken_creator>VISA-T</PaymentToken_creator>  
         <PaymentToken_expdate>2023-12-31</PaymentToken_expdate>  
         <PaymentToken_type>SE</PaymentToken_type>  
         <PaymentToken_status>00</PaymentToken_status>  
         <PaymentToken_creatorStatus>I</PaymentToken_creatorStatus>  
         <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
         <PaymentToken_deviceType>M</PaymentToken_deviceType>  
         <PaymentToken_lang>en</PaymentToken_lang>  
         <PaymentToken_deviceTelNum>37065031123</PaymentToken_deviceTelNum>  
         <PaymentToken_deviceIp>090.131.038.249</PaymentToken_deviceIp>  
         <PaymentToken_deviceId>01234B1B2357800192920701362030300E3F0970A8CDBDA2</PaymentToken_deviceId>  
         <PaymentToken_deviceName>Test</PaymentToken_deviceName>  
         <PaymentToken_activationCode>REDACTED</PaymentToken_activationCode>  
         <PaymentToken_activationExpiry>2021-03-16 15:17:00.000</PaymentToken_activationExpiry>  
         <PaymentToken_activationMethodData />  
         <PaymentToken_activationMethod>1</PaymentToken_activationMethod>  
         <ICC_System_Related_Data_DE55 />  
         <Merch_Name>Visa Tokenisation System</Merch_Name>  
         <Merch_Street />  
         <Merch_City>Test City</Merch_City>  
         <Merch_Region />  
         <Merch_Postcode />  
         <Merch_Country>USA</Merch_Country>  
         <Merch_Tel />  
         <Merch_URL />  
         <Merch_Name_Other />  
         <Merch_Net_id />  
         <Merch_Tax_id>0</Merch_Tax_id>  
         <Merch_Contact />  
         <auth_type />  
         <auth_expdate_utc />  
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
         <Settlement_Date />  
         <DCC_Indicator />  
         <multi_part_txn />  
         <multi_part_txn_final />  
         <multi_part_number />  
         <multi_part_count />  
         <SettlementIndicator />  
         <Traceid_Message />  
         <Traceid_Original />  
         <Network_Transaction_ID />  
         <POS_Date_DE13 />  
         <Network_Currency_Conversion_Date />  
         <Network_TxnAmt_To_BillAmt_Rate />  
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
         <Acquirer_Country />  
         <PaymentToken_PanSource />  
         <Network_Fraud_Data />  
         <SenderData />  
         <ReceiverData />  
         <SchemeTransactionIdentifier />  
         <TokenUniqueReference>DNITHE582599999942043245</TokenUniqueReference>          
         <PaymentTokenPan>5372403458767765</PaymentTokenPan>  
      </GetTransaction>  
   </s:Body>  
</s:Envelope>
```

### Token Complete Notification (TCN) Request

Below is an example of the HTTP POST body data for a token completion notification (TCN). This message is sent when a token service provider confirms successful setup of the token.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
   <s:Body>  
      <GetTransaction xmlns="http://tempuri.org/">  
         <Acquirer_id_DE32 />  
         <ActBal>0.0000</ActBal>  
         <Additional_Amt_DE54 />  
         <Amt_Tran_Fee_DE28 />  
         <Auth_Code_DE38 />  
         <Avl_Bal>0.0000</Avl_Bal>  
         <Bill_Amt>0.0000</Bill_Amt>  
         <Bill_Ccy>826</Bill_Ccy>  
         <BlkAmt>0.0000</BlkAmt>  
         <Cust_Ref />  
         <FX_Pad>0.0000</FX_Pad>  
         <Fee_Fixed>0.0000</Fee_Fixed>  
         <Fee_Rate>0.0000</Fee_Rate>  
         <LoadSRC />  
         <LoadType />  
         <MCC_Code />  
         <MCC_Desc />  
         <MCC_Pad>0.0000</MCC_Pad>  
         <Merch_ID_DE42>VisaTokenSystem</Merch_ID_DE42>  
         <Merch_Name_DE43>Visa Tokenisation System Foster City US</Merch_Name_DE43>  
         <Note>Provisioning Successful</Note>  
         <POS_Data_DE22>1000</POS_Data_DE22>  
         <POS_Data_DE61 />  
         <POS_Termnl_DE41 />  
         <POS_Time_DE12 />  
         <Proc_Code>350000</Proc_Code>  
         <Resp_Code_DE39>00</Resp_Code_DE39>  
         <Ret_Ref_No_DE37>102300045678</Ret_Ref_No_DE37>  
         <Settle_Amt>0.0000</Settle_Amt>  
         <Settle_Ccy />  
         <Status_Code>00</Status_Code>  
         <Token>123456789</Token>  
         <Trans_link>210318083533</Trans_link>  
         <Txn_Amt>0.0000</Txn_Amt>  
         <Txn_CCy>840</Txn_CCy>  
         <Txn_Ctry>USA</Txn_Ctry>  
         <Txn_Desc>Visa Tokenisation System</Txn_Desc>  
         <Txn_GPS_Date>2021-03-18 15:08:23.250</Txn_GPS_Date>  
         <TXn_ID>1250779618</TXn_ID>  
         <Txn_Stat_Code>A</Txn_Stat_Code>  
         <TXN_Time_DE07>0318150821</TXN_Time_DE07>  
         <Txn_Type>J</Txn_Type>  
         <Additional_Data_DE48 />  
         <Authorised_by_GPS>N</Authorised_by_GPS>  
         <AVS_Result />  
         <CU_Group />  
         <InstCode>RAI</InstCode>  
         <MTID>0620</MTID>  
         <ProductID>5877</ProductID>  
         <Record_Data_DE120 />  
         <SubBIN>45967201</SubBIN>  
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
         <Expiry_Date>0</Expiry_Date>  
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
         <GPS_POS_Capability>000100000000000000000000000000000000000000000001M</GPS_POS_Capability>  
         <GPS_POS_Data>10F0000000000Nx000</GPS_POS_Data>  
         <Acquirer_Reference_Data_031 />  
         <Response_Source>UNKNOWN</Response_Source>  
         <Response_Source_Why>0</Response_Source_Why>  
         <Message_Source>VISA-T</Message_Source>  
         <Message_Why>72</Message_Why>  
         <traceid_lifecycle>VIS1-20210318-381077544887139</traceid_lifecycle>  
         <PaymentToken_id>12365432</PaymentToken_id>  
         <PaymentToken_creator>VISA-T</PaymentToken_creator>  
         <PaymentToken_expdate>2023-12-31</PaymentToken_expdate>  
         <PaymentToken_type>SE</PaymentToken_type>  
         <PaymentToken_status>00</PaymentToken_status>  
         <PaymentToken_creatorStatus>A</PaymentToken_creatorStatus>  
         <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
         <PaymentToken_deviceType>W</PaymentToken_deviceType>  
         <PaymentToken_lang>en</PaymentToken_lang>  
         <PaymentToken_deviceTelNum>47912345678</PaymentToken_deviceTelNum>  
         <PaymentToken_deviceIp>192.0.0.8</PaymentToken_deviceIp>  
         <PaymentToken_deviceId>01234B234C1230011230054848300695D86E17C703548A4A</PaymentToken_deviceId>  
         <PaymentToken_deviceName>Test Apple Wa</PaymentToken_deviceName>  
         <PaymentToken_activationCode />  
         <PaymentToken_activationExpiry />  
         <PaymentToken_activationMethodData />  
         <PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
         <ICC_System_Related_Data_DE55 />  
         <Merch_Name>Visa Tokenisation System</Merch_Name>  
         <Merch_Street />  
         <Merch_City>Test City</Merch_City>  
         <Merch_Region>TA</Merch_Region>  
         <Merch_Postcode>12345</Merch_Postcode>  
         <Merch_Country>USA</Merch_Country>  
         <Merch_Tel />  
         <Merch_URL />  
         <Merch_Name_Other />  
         <Merch_Net_id />  
         <Merch_Tax_id>0</Merch_Tax_id>  
         <Merch_Contact />  
         <auth_type />  
         <auth_expdate_utc />  
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
         <Settlement_Date />  
         <DCC_Indicator />  
         <multi_part_txn />  
         <multi_part_txn_final />  
         <multi_part_number />  
         <multi_part_count />  
         <SettlementIndicator />  
         <Traceid_Message />  
         <Traceid_Original />  
         <Network_Transaction_ID />  
         <POS_Date_DE13 />  
         <Network_Currency_Conversion_Date />  
         <Network_TxnAmt_To_BillAmt_Rate />  
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
         <Acquirer_Country />  
         <PaymentToken_PanSource />  
         <Network_Fraud_Data />  
         <SenderData />  
         <ReceiverData />  
         <SchemeTransactionIdentifier />  
         <TokenUniqueReference>DNITHE582599999942043245</TokenUniqueReference>          
         <PaymentTokenPan>5372403458767765</PaymentTokenPan>  
      </GetTransaction>  
   </s:Body>  
</s:Envelope>
```

## 3.7.5 Example Balance Enquiry Message

Below is an example of the HTTP POST body data for a balance enquiry request. A balance enquiry provides details of changes to a cardâs account balance. Card balance adjustments are made using Thredd's API (web services or Cards API) and are relevant to program managers on [EHI Operating modes](../Getting_Started/EHI_operating_modes.htm) where Thredd maintains a record of the card balance.

[Copy](javascript:void(0);)

```
<s:Envelope  
    xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransaction  
            xmlns="http://tempuri.org/">  
            <Acquirer_id_DE32>06462469</Acquirer_id_DE32>  
            <ActBal>0.0000</ActBal>  
            <Additional_Amt_DE54 />  
            <Amt_Tran_Fee_DE28 />  
            <Auth_Code_DE38>169350</Auth_Code_DE38>  
            <Avl_Bal>0.0000</Avl_Bal>  
            <Bill_Amt>0.0000</Bill_Amt>  
            <Bill_Ccy>978</Bill_Ccy>  
            <BlkAmt>0.0000</BlkAmt>  
            <Cust_Ref />  
            <FX_Pad>0.0000</FX_Pad>  
            <Fee_Fixed>0.0000</Fee_Fixed>  
            <Fee_Rate>0.0000</Fee_Rate>  
            <LoadSRC />  
            <LoadType />  
            <MCC_Code>6011</MCC_Code>  
            <MCC_Desc>Automated Cash Disburse</MCC_Desc>  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42>12345678</Merch_ID_DE42>  
            <Merch_Name_DE43>GELDMAAT UTRECHTSESTRAAT AMERSFOORT   NL</Merch_Name_DE43>  
            <Note>PSD2 Counter Reset</Note>  
            <POS_Data_DE22>0510</POS_Data_DE22>  
            <POS_Data_DE61 />  
            <POS_Termnl_DE41>812902</POS_Termnl_DE41>  
            <POS_Time_DE12>145115</POS_Time_DE12>  
            <Proc_Code>300000</Proc_Code>  
            <Resp_Code_DE39>00</Resp_Code_DE39>  
            <Ret_Ref_No_DE37>424714827917</Ret_Ref_No_DE37>  
            <Settle_Amt>0.0000</Settle_Amt>  
            <Settle_Ccy>978</Settle_Ccy>  
            <Status_Code>00</Status_Code>  
            <Token>312587809</Token>  
            <Trans_link>240903827917462469</Trans_link>  
            <Txn_Amt>0.0000</Txn_Amt>  
            <Txn_CCy>978</Txn_CCy>  
            <Txn_Ctry>NLD</Txn_Ctry>  
            <Txn_Desc>GELDMAAT UTRECHTSESTRAAT AMERSFOORT   NL</Txn_Desc>  
            <Txn_GPS_Date>2024-09-03 13:51:31.548</Txn_GPS_Date>  
            <TXn_ID>14799013605</TXn_ID>  
            <Txn_Stat_Code>A</Txn_Stat_Code>  
            <TXN_Time_DE07>0903125131</TXN_Time_DE07>  
            <Txn_Type>A</Txn_Type>  
            <Additional_Data_DE48 />  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group>PMT-CU-001</CU_Group>  
            <InstCode>PMT</InstCode>  
            <MTID>0100</MTID>  
            <ProductID>15385</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>46975400</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group>PMT-YS-010</VL_Group>  
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
            <GPS_POS_Capability>00001001000000000000000100010010000000000011130CA</GPS_POS_Capability>  
            <GPS_POS_Data>0151000300000Nx0002110NC0NCUXXU0</GPS_POS_Data>  
            <Acquirer_Reference_Data_031 />  
            <Response_Source />  
            <Response_Source_Why>0</Response_Source_Why>  
            <Message_Source />  
            <Message_Why>0</Message_Why>  
            <traceid_lifecycle>VIS1-20240903-484247462919598</traceid_lifecycle>  
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
            <ICC_System_Related_Data_DE55>5F3401009F2701809F34034201009F410268189F3303604020950580800400009F37043D2D34D09F100706001203A020019F26082D44EBEDF681E2939F3602009E820238009C01309F1A0205289A032409039F02060000000000005F2A0209788407A0000000031010</ICC_System_Related_Data_DE55>  
            <Merch_Name>12345678</Merch_Name>  
            <Merch_Street>GELDMAAT UTRECHTSESTRAAT</Merch_Street>  
            <Merch_City>AMERSFOORT</Merch_City>  
            <Merch_Region />  
            <Merch_Postcode />  
            <Merch_Country>NLD</Merch_Country>  
            <Merch_Tel />  
            <Merch_URL />  
            <Merch_Name_Other />  
            <Merch_Net_id />  
            <Merch_Tax_id />  
            <Merch_Contact />  
        </GetTransaction>  
    </s:Body>  
</s:Envelope>
```

### Message Response

Below is an example of HTTP response to the above balance enquiry message.

[Copy](javascript:void(0);)

```
<s:Envelope  
    xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <GetTransactionResponse  
            xmlns="http://tempuri.org/">  
            <GetTransactionResult>  
                <Responsestatus>00</Responsestatus>  
                <CurBalance>69.6300</CurBalance>  
                <AvlBalance>66.8200</AvlBalance>  
                <Acknowledgement>1</Acknowledgement>  
            </GetTransactionResult>  
        </GetTransactionResponse>  
    </s:Body>  
</s:Envelope>
```

## 3.7.6 Examples of Amount Signs

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
* âOtherâ means not Visa or Mastercard. For example, internal (via Smart Client) or a web service / [Cards API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Thredd Cards API is a new REST-based API which can be used to connect to the Thredd system in place of using the traditional Thredd SOAP-based Web Services. The REST API provides messages in JSON format. If you are interested in the Cards API, please contact your Account Manager.](#) call