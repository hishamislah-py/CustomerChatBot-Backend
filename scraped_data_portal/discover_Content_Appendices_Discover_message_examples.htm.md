# 10 Discover Message Examples

This page details examples of requests and responses for authorisations.

* [Authorisation Request](#Authoris)
* [Authorisation Request (Auth Advice)](#Authoris2)
* [Authorisation Request (Payment Token Activation)](#Authoris3)
* [Authorisation Reversal for AFD](#Authoris4)

## 10.1 Authorisation Request

Below is an example of the HTTP POST body data for an authorisation request.

Some key elements of this request are:

* The `MTID` value is 0100 and the `Txn_Type` is A, indicating that this is an Authorisation Request.
* The transaction is for Â£1. This is indicated by the `Bill_Amt` having a value of 1.0000 and the `Bill_Ccy` being set to 826 (for Great British Pounds).
* The `SendingAttemptCount` field checks to show whether this is a duplicate request. This will be zero for a first attempt.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32>0852729540</Acquirer_id_DE32>   
 <ActBal>984.9800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38>129833</Auth_Code_DE38>   
 <Avl_Bal>951.2300</Avl_Bal>   
 <Bill_Amt>-1.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-33.7500</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC />   
<LoadType />   
<MCC_Code>4111</MCC_Code>   
 <MCC_Desc>Commuter Transport, Ferries</MCC_Desc>   
 <MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42>4111</Merch_ID_DE42>   
 <Merch_Name_DE43>Travel Like A Pro                    GBR</Merch_Name_DE43>   
 <Note />   
<POS_Data_DE22>010</POS_Data_DE22>   
 <POS_Data_DE61>0000000000000826</POS_Data_DE61>   
 <POS_Termnl_DE41 />   
<POS_Time_DE12>090254</POS_Time_DE12>   
 <Proc_Code>000000</Proc_Code>   
 <Resp_Code_DE39>00</Resp_Code_DE39>   
 <Ret_Ref_No_DE37>216708203774</Ret_Ref_No_DE37>   
 <Settle_Amt>1.0000</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>220616003774729540</Trans_link>   
 <Txn_Amt>1.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Travel Like A Pro                    GBR</Txn_Desc>   
 <Txn_GPS_Date>2022-06-16 10:02:55.970</Txn_GPS_Date>   
 <TXn_ID>6152627830</TXn_ID>   
 <Txn_Stat_Code>A</Txn_Stat_Code>   
 <TXN_Time_DE07>0616090254</TXN_Time_DE07>   
 <Txn_Type>A</Txn_Type>   
 <Additional_Data_DE48>008R9203984</Additional_Data_DE48>   
 <Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group>PMT-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID>0100</MTID>   
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
<GPS_POS_Capability>0011000010000000000000000000000000100000000001016</GPS_POS_Capability>   
 <GPS_POS_Data>0168000800000Nx00100001U0NCUXXU</GPS_POS_Data>   
 <Acquirer_Reference_Data_031 />   
<Response_Source />   
<Response_Source_Why>0</Response_Source_Why>   
 <Message_Source />   
<Message_Why>0</Message_Why>   
 <traceid_lifecycle>BNET-20220616-MCC003774</traceid_lifecycle>   
 <Balance_Sequence>172</Balance_Sequence>   
 <Balance_Sequence_Exthost>0</Balance_Sequence_Exthost>   
 <PaymentToken_id />   
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
<PaymentToken_activationMethod />   
<ICC_System_Related_Data_DE55 />   
<Merch_Name>Travel Like A Pro</Merch_Name>   
 <Merch_Street />   
<Merch_City />   
<Merch_Region />   
<Merch_Postcode />   
<Merch_Country>GBR</Merch_Country>   
 <Merch_Tel />   
<Merch_URL />   
<Merch_Name_Other />   
<Merch_Net_id />   
<Merch_Tax_id />   
<Merch_Contact />   
<auth_type>0</auth_type>   
 <auth_expdate_utc>2022-06-23 09:02:54.898       </auth_expdate_utc>   
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
<DCC_Indicator> </DCC_Indicator>   
 <multi_part_txn />   
<multi_part_txn_final />   
<multi_part_number />   
<multi_part_count />   
<SettlementIndicator />   
<Network_TxnAmt_To_BillAmt_Rate>1000000:6</Network_TxnAmt_To_BillAmt_Rate>   
 <Network_TxnAmt_To_BaseAmt_Rate />   
<Network_BaseAmt_To_BillAmt_Rate />   
<POS_Date_DE13>2022-06-16</POS_Date_DE13>   
 <Traceid_Message>BNET-20220616-MCC003774</Traceid_Message>   
 <Traceid_Original />   
<Network_Currency_Conversion_Date>2022-06-16</Network_Currency_Conversion_Date>   
 <Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID>MCC0037740616</Network_Transaction_ID>   
 <Misc_TLV_Data>G00001S0010005AkhilG00001S0020001KG00001S0030005KumarG00001S0040010VallachiraG00001S0060003KRLG00001S0070003INDG00001S0080006680562G00001S00900108050282677G00001S010000829081987G00001S0160003INDG00001S0170003INDG00001R0010006DhanyaG00001R0030012BalachandranG00001R0050007ParavurG00001R0060003KRLG00001R0070003INDG00001R0080006683513G00001R00900109686534677G00001R010000827011990G00001R01300011G00001R0160003INDG00001R0170003IND</Misc_TLV_Data>   
 <Acquirer_Country />   
<Network_Fraud_Data />   
<SenderData />   
<ReceiverData />   
<AuthenticationAmountUpper />   
<AuthenticationCurrency />   
<AuthenticationMerchantHash />   
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>   
 <SchemeTransactionIdentifier />   
<TokenUniqueReference />   
</GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

### Authorisation Response

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

## 10.2 Authorisation Request (Auth Advice)

Below is an example of the HTTP POST body data for an Authorisation advice message.

Some key elements of this request are:

* The `MTID` value is 0120 and the Txn\_Type is J, indicating that this is Authorisation Advice matched to an Authorisation Request.
* This type of message is for EHI Mode 3 (Full Service Processing).
* The `Message_Source` value is set to MC-STIP, indicating Stand-In processing.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32>0843788220</Acquirer_id_DE32>   
 <ActBal>852.7900</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38>120465</Auth_Code_DE38>   
 <Avl_Bal>811.5900</Avl_Bal>   
 <Bill_Amt>1.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-41.2000</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC />   
<LoadType />   
<MCC_Code>4112</MCC_Code>   
 <MCC_Desc />   
<MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42>4112           </Merch_ID_DE42>   
 <Merch_Name_DE43>Passenger Railway - SCAEx             GB</Merch_Name_DE43>   
 <Note />   
<POS_Data_DE22>0110</POS_Data_DE22>   
 <POS_Data_DE61>                                          </POS_Data_DE61>   
 <POS_Termnl_DE41>        </POS_Termnl_DE41>   
 <POS_Time_DE12 />   
<Proc_Code>000000</Proc_Code>   
 <Resp_Code_DE39>00</Resp_Code_DE39>   
 <Ret_Ref_No_DE37>217108201834</Ret_Ref_No_DE37>   
 <Settle_Amt>0.00</Settle_Amt>   
 <Settle_Ccy />   
<Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>220620001834788220</Trans_link>   
 <Txn_Amt>1.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Passenger Railway - SCAEx             GB</Txn_Desc>   
 <Txn_GPS_Date>2022-06-20 05:37:47.367</Txn_GPS_Date>   
 <TXn_ID>6152633700</TXn_ID>   
 <Txn_Stat_Code>A</Txn_Stat_Code>   
 <TXN_Time_DE07>0620043747</TXN_Time_DE07>   
 <Txn_Type>J</Txn_Type>   
 <Additional_Data_DE48 />   
<Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group />   
<InstCode>PMT</InstCode>   
 <MTID>0120</MTID>   
 <ProductID>2042</ProductID>   
 <Record_Data_DE120 />   
<SubBIN>43788220</SubBIN>   
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
<GPS_POS_Capability>00001001000000000000000100010000001000000001130C0</GPS_POS_Capability>   
 <GPS_POS_Data>9968000800000Nx000</GPS_POS_Data>   
 <Acquirer_Reference_Data_031 />   
<Response_Source>MC-STIP</Response_Source>   
 <Response_Source_Why>5</Response_Source_Why>   
 <Message_Source>MC-STIP</Message_Source>   
 <Message_Why>5</Message_Why>   
 <traceid_lifecycle>BNET-20220616-MCC003776</traceid_lifecycle>   
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
<Merch_Name>Passenger Railway - SCAEx</Merch_Name>   
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
 <auth_expdate_utc>2022-06-28 04:37:47.307</auth_expdate_utc>   
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
<POS_Date_DE13>0000-00-00</POS_Date_DE13>   
 <Traceid_Message>BNET-20220616-MCC003776</Traceid_Message>   
 <Traceid_Original />   
<Network_Currency_Conversion_Date />   
<Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code>9020</Visa_STIP_Reason_Code>   
 <Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
 <Network_Transaction_ID>MCC0037740616</Network_Transaction_ID>   
 <Misc_TLV_Data />   
</GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

### Authorisation Response (Auth Advice Response)

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

## 10.3 Authorisation Request (Payment Token Activation)

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
            <Acquirer_id_DE32>06015611</Acquirer_id_DE32>  
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
            <MCC_Code>5969</MCC_Code>  
            <MCC_Desc>Direct Marketing - Other</MCC_Desc>  
            <MCC_Pad>0.0000</MCC_Pad>  
            <Merch_ID_DE42>MDES special 01</Merch_ID_DE42>  
            <Merch_Name_DE43>Mastercard             St. Louis     MO </Merch_Name_DE43>  
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
            <Txn_Desc>Mastercard             St. Louis     MO </Txn_Desc>  
            <Txn_GPS_Date>2018-02-28 13:14:55.807</Txn_GPS_Date>  
            <TXn_ID>2512969074</TXn_ID>  
            <Txn_Stat_Code>A</Txn_Stat_Code>  
            <TXN_Time_DE07>0228131455</TXN_Time_DE07>  
            <Txn_Type>A</Txn_Type>  
      <Additional_Data_DE48>038T230221260310333200101C061150110030273</Additional_Data_DE48>  
            <Authorised_by_GPS>N</Authorised_by_GPS>  
            <AVS_Result />  
            <CU_Group>GPS-CU-001</CU_Group>  
            <InstCode>GPS</InstCode>  
            <MTID>0100</MTID>  
            <ProductID>93305</ProductID>  
            <Record_Data_DE120 />  
            <SubBIN>51000028</SubBIN>  
            <TLogIDOrg>0</TLogIDOrg>  
            <VL_Group>PMT-EX-001</VL_Group>  
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
    <GPS_POS_Capability>01000010000000000000001001000000000000000230010</GPS_POS_Capability>  
            <GPS_POS_Data>5018000800000Nx000</GPS_POS_Data>  
            <Acquirer_Reference_Data_031 />  
            <Response_Source />  
            <Response_Source_Why>0</Response_Source_Why>  
            <Message_Source />  
            <Message_Why>0</Message_Why>  
            <traceid_lifecycle>BNET-20180228-MTP13REG5</traceid_lifecycle>  
            <Balance_Sequence>0</Balance_Sequence>  
            <Balance_Sequence_Exthost>0</Balance_Sequence_Exthost>  
            <PaymentToken_id>58621</PaymentToken_id>  
            <PaymentToken_creator>MC-MDES</PaymentToken_creator>  
            <PaymentToken_expdate />  
            <PaymentToken_type>SE</PaymentToken_type>  
            <PaymentToken_status>00</PaymentToken_status>  
            <PaymentToken_creatorStatus />  
            <PaymentToken_wallet>APPLE</PaymentToken_wallet>  
            <PaymentToken_deviceType>U</PaymentToken_deviceType>  
            <PaymentToken_lang />  
            <PaymentToken_deviceTelNum>5935</PaymentToken_deviceTelNum>  
            <PaymentToken_deviceIp>1FDC469E</PaymentToken_deviceIp>  
            <PaymentToken_deviceId>04181013B72B80014315107675932778BEBF83E6DF785407</PaymentToken_deviceId>  
            <PaymentToken_deviceName />  
       <PaymentToken_activationCode>393805</PaymentToken_activationCode>  
       <PaymentToken_activationExpiry>2018-02-28 13:44:00.000</PaymentToken_activationExpiry>  
       <PaymentToken_activationMethod>1</PaymentToken_activationMethod>  
       <PaymentToken_activationMethodData>+447777123456</PaymentToken_activationMethodData>  
            <ICC_System_Related_Data_DE55 />  
            <Merch_Name>Mastercard</Merch_Name>  
            <Merch_Street />  
            <Merch_City>St. Louis</Merch_City>  
            <Merch_Region>MO</Merch_Region>  
            <Merch_Postcode>63368</Merch_Postcode>  
            <Merch_Country>USA</Merch_Country>  
            <Merch_Tel />  
            <Merch_URL />  
            <Merch_Name_Other />  
            <Merch_Net_id />  
            <Merch_Tax_id />  
            <Merch_Contact />  
            <auth_type>F</auth_type>  
            <auth_expdate_utc>2016-01-18 14:05:13.747</auth_expdate_utc>  
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
            <Traceid_Message>BNET-20180228-MTP13REG5</Traceid_Message>  
            <Traceid_Original />  
            <Network_Transaction_ID>MTP13REG50228</Network_Transaction_ID>  
            <POS_Date_DE13>2016-01-18</POS_Date_DE13>  
            <Network_Currency_Conversion_Date>2016-01-18</Network_Currency_Conversion_Date>  
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
            <AuthenticationCurrency />              
            <AuthenticationAmountUpper />        
            <AuthenticationMerchantHash />  
            <FxProviderCardholderRate />              
        </GetTransaction>  
    </s:Body>  
</s:Envelope
```

[Back to Top](#Top)

## 10.4 Authorisation Reversal for AFD

Below is an example of the HTTP POST body data for an authorisation reversal for an Automated Fuel Dispenser (AFD). An AFD sends a 0120 advice to confirm how much fuel was actually dispensed. Thredd sends this to you as a reversal, to reverse the unspent part of the original authorisation from the AFD.

Some key elements of this request are:

* The `MTID` value is 0120 and the `Txn_Type` is D, indicating that this is Authorisation reversal due to an Automated Fuel Dispenser (AFD) 0120 Advice message
* The `MCC_Code` value will be set to 5542, which identifies this is an AFD transaction
* This example has the `Bill_Amt` value set to 1.000, indicating that the fuel pump has taken a nominal Â£1 amount. The pump will then allow up to the permitted maximum it is allowed to clear according to the chargeback rules. It will then send an advice to say how much fuel was actually delivered.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32>0852729540</Acquirer_id_DE32>   
 <ActBal>975.4800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38 />   
<Avl_Bal>942.6600</Avl_Bal>   
 <Bill_Amt>1.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-32.8200</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC />   
<LoadType />   
<MCC_Code>5542</MCC_Code>   
 <MCC_Desc>0000-6010</MCC_Desc>   
 <MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42>5542</Merch_ID_DE42>   
 <Merch_Name_DE43>BP Petrol Station                    GBR</Merch_Name_DE43>   
 <Note>Reversal due to AFD Advice with different amount. (AFD Amount=1.0000)</Note>   
 <POS_Data_DE22>051</POS_Data_DE22>   
 <POS_Data_DE61>1010010001500196</POS_Data_DE61>   
 <POS_Termnl_DE41>        </POS_Termnl_DE41>   
 <POS_Time_DE12>120319</POS_Time_DE12>   
 <Proc_Code>000000</Proc_Code>   
 <Resp_Code_DE39 />   
<Ret_Ref_No_DE37>217308203845</Ret_Ref_No_DE37>   
 <Settle_Amt>1.0000</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>220622003845729540</Trans_link>   
 <Txn_Amt>1.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>BP Petrol Station                    GBR</Txn_Desc>   
 <Txn_GPS_Date>2022-06-22 13:03:40.197</Txn_GPS_Date>   
 <TXn_ID>6152637268</TXn_ID>   
 <Txn_Stat_Code>A</Txn_Stat_Code>   
 <TXN_Time_DE07>0622120319</TXN_Time_DE07>   
 <Txn_Type>D</Txn_Type>   
 <Additional_Data_DE48>007C8002TV</Additional_Data_DE48>   
 <Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result> </AVS_Result>   
 <CU_Group>PMT-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID>0120</MTID>   
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
<GPS_POS_Capability>00001001000000000000000100000010000000000012230C1</GPS_POS_Capability>   
 <GPS_POS_Data>0151000300000Nx000</GPS_POS_Data>   
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
<Merch_Name>BP Petrol Station</Merch_Name>   
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
 <auth_expdate_utc>2022-06-29 12:03:19.210</auth_expdate_utc>   
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
<POS_Date_DE13>2022-06-22</POS_Date_DE13>   
 <Traceid_Message>BNET-20220622-MC 003845</Traceid_Message>   
 <Traceid_Original />   
<Network_Currency_Conversion_Date>2022-06-22</Network_Currency_Conversion_Date>   
 <Mastercard_AdviceReasonCode_DE60>4020000</Mastercard_AdviceReasonCode_DE60>   
 <Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID />   
<Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID>MC 0038450622</Network_Transaction_ID>   
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

### Authorisation Response (Auth Reversal Response)

Below is an example of HTTP response to the above authorisation reversal message.

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