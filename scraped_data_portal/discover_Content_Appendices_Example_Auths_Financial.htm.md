## 9.15 Example Financial Notifications

This page details examples of financial message notifications and financial responses.

* [Financial Notification (First Presentment)](#Financia)
* [Financial Notification (Second Presentment)](#Financia3)
* [Financial Notification (Reversal)](#Financia2)

### 9.15.1 Financial Notification (First Presentment)

Below is an example of the HTTP POST body data for a financial notification (first presentment).

Some key elements of this request are:

* The `MTID` value is 1240 and the `Txn_Type` is P, indicating that this is an Financial Notification (First Presentment).
* A presentment (settlement or clearing request) is a financial transaction where Thredd receives a request to settle an amount that was previously authorised on a card. A presentment is typically linked to a previous authorisation transaction - in this case, `traceid_lifecycle` and `trans_link` can be used for you to make your own matching, while `Matching_Txn_ID` has the transaction id for the original transaction.

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
<s:Body>  
<GetTransaction xmlns="http://tempuri.org/">  
<Acquirer_id_DE32>00000361603</Acquirer_id_DE32>  
<ActBal>0.0000</ActBal>  
<Additional_Amt_DE54/>  
<Amt_Tran_Fee_DE28/>  
<Auth_Code_DE38>185437</Auth_Code_DE38>  
<Avl_Bal>0.0000</Avl_Bal>  
<Bill_Amt>-4.0000</Bill_Amt>  
<Bill_Ccy>826</Bill_Ccy>  
<BlkAmt>0.0000</BlkAmt>  
<Cust_Ref/>  
<FX_Pad>0.0000</FX_Pad>  
<Fee_Fixed>0.0000</Fee_Fixed>  
<Fee_Rate>0.0000</Fee_Rate>  
<LoadSRC/>  
<LoadType/>  
<MCC_Code>5734</MCC_Code>  
<MCC_Desc>Computer Software Stores</MCC_Desc>  
<MCC_Pad>0.0000</MCC_Pad>  
<Merch_ID_DE42/>  
<Merch_Name_DE43>\MERCHANT\LONDON\ 826</Merch_Name_DE43>  
<Note/>  
<POS_Data_DE22>100990090000</POS_Data_DE22>  
<POS_Data_DE61/>  
<POS_Termnl_DE41/>  
<POS_Time_DE12/>  
<Proc_Code>000000</Proc_Code>  
<Resp_Code_DE39/>  
<Ret_Ref_No_DE37/>  
<Settle_Amt>-4.0000</Settle_Amt>  
<Settle_Ccy>826</Settle_Ccy>  
<Status_Code>00</Status_Code>  
<Token>116551735</Token>  
<Trans_link>361603</Trans_link>  
<Txn_Amt>4.0000</Txn_Amt>  
<Txn_CCy>826</Txn_CCy>  
<Txn_Ctry>GBR</Txn_Ctry>  
<Txn_Desc>\MERCHANT\LONDON\ 826</Txn_Desc>  
<Txn_GPS_Date>2024-07-31 10:21:26.093</Txn_GPS_Date>  
<TXn_ID>6161750188</TXn_ID>  
<Txn_Stat_Code>S</Txn_Stat_Code>  
<TXN_Time_DE07/>  
<Txn_Type>P</Txn_Type>  
<Additional_Data_DE48/>  
<Authorised_by_GPS>N</Authorised_by_GPS>  
<AVS_Result/>  
<CU_Group>MOP-CU-001</CU_Group>  
<InstCode>PMT</InstCode>  
<MTID>1420</MTID>  
<ProductID>10051</ProductID>  
<Record_Data_DE120/>  
<SubBIN>99999910</SubBIN>  
<TLogIDOrg>0</TLogIDOrg>  
<VL_Group>GPS-VL-004</VL_Group>  
<Dom_Fee_Fixed>0.00</Dom_Fee_Fixed>  
<Non_Dom_Fee_Fixed>0.00</Non_Dom_Fee_Fixed>  
<Fx_Fee_Fixed>0.00</Fx_Fee_Fixed>  
<Other_Fee_Amt>0.00</Other_Fee_Amt>  
<Fx_Fee_Rate>0.00</Fx_Fee_Rate>  
<Dom_Fee_Rate>0.00</Dom_Fee_Rate>  
<Non_Dom_Fee_Rate>0.00</Non_Dom_Fee_Rate>  
<Additional_Data_DE124/>  
<CVV2/>  
<PIN/>  
<PIN_Enc_Algorithm/>  
<PIN_Format/>  
<PIN_Key_Index/>  
<SendingAttemptCount>0</SendingAttemptCount>  
<source_bank_ctry/>  
<source_bank_account_format/>  
<source_bank_account/>  
<dest_bank_ctry/>  
<dest_bank_account_format/>  
<dest_bank_account/>  
<GPS_POS_Capability>00 </GPS_POS_Capability>  
<GPS_POS_Data>5000000000000 x000</GPS_POS_Data>  
<Acquirer_Reference_Data_031>27039998</Acquirer_Reference_Data_031>  
<Response_Source/>  
<Response_Source_Why>0</Response_Source_Why>  
<Message_Source/>  
<Message_Why>0</Message_Why>  
<traceid_lifecycle>DGN-20240731-017363682879502</traceid_lifecycle>  
<PaymentToken_id>0</PaymentToken_id>  
<PaymentToken_creator/>  
<PaymentToken_expdate/>  
<PaymentToken_type/>  
<PaymentToken_status/>  
<PaymentToken_creatorStatus/>  
<PaymentToken_wallet/>  
<PaymentToken_deviceType/>  
<PaymentToken_lang/>  
<PaymentToken_deviceTelNum/>  
<PaymentToken_deviceIp/>  
<PaymentToken_deviceId/>  
<PaymentToken_deviceName/>  
<PaymentToken_activationCode/>  
<PaymentToken_activationExpiry/>  
<PaymentToken_activationMethodData/>  
<PaymentToken_activationMethod>0</PaymentToken_activationMethod>  
<ICC_System_Related_Data_DE55/>  
<Merch_Name/>  
<Merch_Street>MERCHANT</Merch_Street>  
<Merch_City>LONDON</Merch_City>  
<Merch_Region/>  
<Merch_Postcode/>  
<Merch_Country>GBR</Merch_Country>  
<Merch_Tel/>  
<Merch_URL/>  
<Merch_Name_Other/>  
<Merch_Net_id/>  
<Merch_Tax_id>0</Merch_Tax_id>  
<Merch_Contact/>  
<auth_type>0</auth_type>  
<auth_expdate_utc/>  
<Matching_Txn_ID>6161750184</Matching_Txn_ID>  
<Reason_ID>0</Reason_ID>  
<Dispute_Condition/>  
<Network_Chargeback_Reference_Id/>  
<Acquirer_Forwarder_ID/>  
<Currency_Code_Fee/>  
<Currency_Code_Fee_Settlement/>  
<Interchange_Amount_Fee/>  
<Interchange_Amount_Fee_Settlement/>  
<Clearing_Process_Date>2024-07-31</Clearing_Process_Date>  
<Settlement_Date>2024-07-31</Settlement_Date>  
<DCC_Indicator>0</DCC_Indicator>  
<multi_part_txn>0</multi_part_txn>  
<multi_part_txn_final>0</multi_part_txn_final>  
<multi_part_number>0</multi_part_number>  
<multi_part_count>0</multi_part_count>  
<SettlementIndicator>0</SettlementIndicator>  
<Network_TxnAmt_To_BillAmt_Rate>1000000:6</Network_TxnAmt_To_BillAmt_Rate>  
<Network_TxnAmt_To_BaseAmt_Rate/>  
<Network_BaseAmt_To_BillAmt_Rate/>  
<POS_Date_DE13/>  
<Traceid_Message>DGN-20240731-017363682879502</Traceid_Message>  
<Traceid_Original/>  
<Network_Currency_Conversion_Date/>  
<Mastercard_AdviceReasonCode_DE60/>  
<Network_Original_Data_Elements_DE90/>  
<Visa_ResponseInfo_DE44/>  
<Visa_STIP_Reason_Code/>  
<Network_Issuer_Settle_ID>00000361603</Network_Issuer_Settle_ID>  
<Network_Replacement_Amounts_DE95/>  
<Visa_POS_Data_DE60/>  
<Network_Transaction_ID>017363682879502</Network_Transaction_ID>  
<Misc_TLV_Data/>  
<ClearingFileID>20240731092101251 </ClearingFileID>  
<FxProviderCardholderRate>0.0</FxProviderCardholderRate>  
</GetTransaction>  
</s:Body>  
</s:Envelope>
```

#### Financial Response

Below is an example of HTTP response to the above Financial Notification message.

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

### 9.15.2 Financial Notification (Second Presentment)

Below is an example of the HTTP POST body data for a financial notification (second presentment).

Some key elements of this request are:

* The `MTID` value is 1240 and the `Txn_Type` is N, indicating that this is a Financial Notification (Second Presentment)
* A second presentment is used when a merchant resubmits the transaction with evidence to counter the chargeback. More information on this can be found in the [Payments Dispute Management Guide.](https://docs.thredd.ai/chargebacks/Content/Home.htm)

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">   
 <s:Body>   
 <GetTransaction xmlns="http://tempuri.org/">   
 <Acquirer_id_DE32>52729540</Acquirer_id_DE32>   
 <ActBal>972.9800</ActBal>   
 <Additional_Amt_DE54 />   
<Amt_Tran_Fee_DE28 />   
<Auth_Code_DE38>112897</Auth_Code_DE38>   
 <Avl_Bal>938.6600</Avl_Bal>   
 <Bill_Amt>-1.0000</Bill_Amt>   
 <Bill_Ccy>826</Bill_Ccy>   
 <BlkAmt>-34.3200</BlkAmt>   
 <Cust_Ref />   
<FX_Pad>0.0000</FX_Pad>   
 <Fee_Fixed>0.0000</Fee_Fixed>   
 <Fee_Rate>0.0000</Fee_Rate>   
 <LoadSRC />   
<LoadType />   
<MCC_Code>4111</MCC_Code>   
 <MCC_Desc>Commuter Transport, Ferries</MCC_Desc>   
 <MCC_Pad>0.0000</MCC_Pad>   
 <Merch_ID_DE42>4111           </Merch_ID_DE42>   
 <Merch_Name_DE43>Travel Like A Pro                    GBR</Merch_Name_DE43>   
 <Note />   
<POS_Data_DE22>090901199001</POS_Data_DE22>   
 <POS_Data_DE61 />   
<POS_Termnl_DE41>        </POS_Termnl_DE41>   
 <POS_Time_DE12>220622135626</POS_Time_DE12>   
 <Proc_Code>000000</Proc_Code>   
 <Resp_Code_DE39 />   
<Ret_Ref_No_DE37>217308203852</Ret_Ref_No_DE37>   
 <Settle_Amt>-1.0000</Settle_Amt>   
 <Settle_Ccy>826</Settle_Ccy>   
 <Status_Code>00</Status_Code>   
 <Token>123456789</Token>   
 <Trans_link>220622201147038521</Trans_link>   
 <Txn_Amt>1.0000</Txn_Amt>   
 <Txn_CCy>826</Txn_CCy>   
 <Txn_Ctry>GBR</Txn_Ctry>   
 <Txn_Desc>Travel Like A Pro                    GBR</Txn_Desc>   
 <Txn_GPS_Date>2022-06-22 15:12:01.147</Txn_GPS_Date>   
 <TXn_ID>6152637730</TXn_ID>   
 <Txn_Stat_Code>S</Txn_Stat_Code>   
 <TXN_Time_DE07 />   
<Txn_Type>N</Txn_Type>   
 <Additional_Data_DE48>0002003MRG0003003MRG0023003CT6014800482620158030MCC10106017322062201    NNNNNN0159067       1521544702350                   1US00000001N22062201220622010165001M01700165032277600      0177002YY0191001200150072103312</Additional_Data_DE48>   
 <Authorised_by_GPS>N</Authorised_by_GPS>   
 <AVS_Result />   
<CU_Group>PMT-CU-001</CU_Group>   
 <InstCode>PMT</InstCode>   
 <MTID>1240</MTID>   
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
<GPS_POS_Capability>00         </GPS_POS_Capability>   
 <GPS_POS_Data>     00  00 0 x000</GPS_POS_Data>   
 <Acquirer_Reference_Data_031>17295405123000000038521</Acquirer_Reference_Data_031>   
 <Response_Source />   
<Response_Source_Why>0</Response_Source_Why>   
 <Message_Source />   
<Message_Why>0</Message_Why>   
 <traceid_lifecycle>BNET-20220622-MC 003852</traceid_lifecycle>   
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
<Merch_Tax_id>0</Merch_Tax_id>   
 <Merch_Contact />   
<auth_type>0</auth_type>   
 <auth_expdate_utc />   
<Matching_Txn_ID>0</Matching_Txn_ID>   
 <Reason_ID>0</Reason_ID>   
 <Dispute_Condition />   
<Network_Chargeback_Reference_Id />   
<Acquirer_Forwarder_ID>52729540</Acquirer_Forwarder_ID>   
 <Currency_Code_Fee />   
<Currency_Code_Fee_Settlement />   
<Interchange_Amount_Fee />   
<Interchange_Amount_Fee_Settlement />   
<Clearing_Process_Date>2022-06-22</Clearing_Process_Date>   
 <Settlement_Date>2022-06-22</Settlement_Date>   
 <DCC_Indicator>0</DCC_Indicator>   
 <multi_part_txn>0</multi_part_txn>   
 <multi_part_txn_final>0</multi_part_txn_final>   
 <multi_part_number>0</multi_part_number>   
 <multi_part_count>0</multi_part_count>   
 <SettlementIndicator />   
<Network_TxnAmt_To_BillAmt_Rate>1000000:6</Network_TxnAmt_To_BillAmt_Rate>   
 <Network_TxnAmt_To_BaseAmt_Rate />   
<Network_BaseAmt_To_BillAmt_Rate />   
<POS_Date_DE13>20220622</POS_Date_DE13>   
 <Traceid_Message>BNET-20220622-MC 003852</Traceid_Message>   
 <Traceid_Original />   
<Network_Currency_Conversion_Date />   
<Mastercard_AdviceReasonCode_DE60 />   
<Network_Original_Data_Elements_DE90 />   
<Visa_ResponseInfo_DE44 />   
<Visa_STIP_Reason_Code />   
<Network_Issuer_Settle_ID>52729540</Network_Issuer_Settle_ID>   
 <Network_Replacement_Amounts_DE95 />   
<Visa_POS_Data_DE60 />   
<Network_Transaction_ID> MC 0038520622  </Network_Transaction_ID>   
 <Misc_TLV_Data />   
<ClearingFileID>T112.0012206220005272954000065     </ClearingFileID>   
 <FxProviderCardholderRate>0.0</FxProviderCardholderRate>   
 </GetTransaction>   
 </s:Body>   
 </s:Envelope>
```

#### Financial Response

Below is an example of HTTP response to the above Financial Notification message.

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

### 9.15.3 Financial Notification (Reversal)

Below is an example of the HTTP POST body data for a financial notification (type E reversal).

Some key elements of this request are:

* The `MTID` value is 1240 and the `Txn_Type` is E, indicating that this is a Financial Notification (Reversal)
* A financial reversal occurs when the acquirer cancels all or part of a prior transaction (which may be a purchase, refund, cashback, cash, PIN change, or any other transaction type). For example, if the acquirer has already taken the funds and are aware of a processing error (e.g., double charging), they can submit an 1240 Financial Reversal.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
   <s:Body>  
      <GetTransaction xmlns="http://tempuri.org/">  
         <Acquirer_id_DE32 />  
         <ActBal>306.4400</ActBal>  
         <Additional_Amt_DE54 />  
         <Amt_Tran_Fee_DE28 />  
         <Auth_Code_DE38>160310</Auth_Code_DE38>  
         <Avl_Bal>306.4400</Avl_Bal>  
         <Bill_Amt>22.0500</Bill_Amt>  
         <Bill_Ccy>978</Bill_Ccy>  
         <BlkAmt>0.0000</BlkAmt>  
         <Cust_Ref />  
         <FX_Pad>0.0000</FX_Pad>  
         <Fee_Fixed>0.0000</Fee_Fixed>  
         <Fee_Rate>0.0000</Fee_Rate>  
         <LoadSRC />  
         <LoadType />  
         <MCC_Code>5200</MCC_Code>  
         <MCC_Desc>Home Supply Warehouse Stores</MCC_Desc>  
         <MCC_Pad>0.0000</MCC_Pad>  
         <Merch_ID_DE42>102642301</Merch_ID_DE42>  
         <Merch_Name_DE43>Hornbach Baumarkt AG F\Am Storrenacker 6\Karlsruhe\76139     DEUDEU</Merch_Name_DE43>  
         <Note />  
         <POS_Data_DE22>M10101C13346</POS_Data_DE22>  
         <POS_Data_DE61 />  
         <POS_Termnl_DE41>65203001</POS_Termnl_DE41>  
         <POS_Time_DE12>231128180200</POS_Time_DE12>  
         <Proc_Code>000000</Proc_Code>  
         <Resp_Code_DE39 />  
         <Ret_Ref_No_DE37>112818154720</Ret_Ref_No_DE37>  
         <Settle_Amt>22.0500</Settle_Amt>  
         <Settle_Ccy>978</Settle_Ccy>  
         <Status_Code>00</Status_Code>  
         <Token>497305583</Token>  
         <Trans_link>240201838967054127</Trans_link>  
         <Txn_Amt>22.0500</Txn_Amt>  
         <Txn_CCy>978</Txn_CCy>  
         <Txn_Ctry>DEU</Txn_Ctry>  
         <Txn_Desc>Hornbach Baumarkt AG F\Am Storrenacker 6\Karlsruhe\76139     DEUDEU</Txn_Desc>  
         <Txn_GPS_Date>2024-02-01 07:08:38.967</Txn_GPS_Date>  
         <TXn_ID>13913456785</TXn_ID>  
         <Txn_Stat_Code>S</Txn_Stat_Code>  
         <TXN_Time_DE07 />  
         <Txn_Type>E</Txn_Type>  
         <Additional_Data_DE48>0002003MRJ0003003MRJ001500724013100023003POI0025007R23112901460360029019780000000000379780000000000370147048002901978000000000000374850978000000000000374850014800497820158031MCC42800018524020103 MRJNNNNNNN015906717298      00000526837                 1EU00000008N24020103240201010165001M0177002N 01910012</Additional_Data_DE48>  
         <Authorised_by_GPS>N</Authorised_by_GPS>  
         <AVS_Result />  
         <CU_Group>PMT-CU-001</CU_Group>  
         <InstCode>PMT</InstCode>  
         <MTID>1240</MTID>  
         <ProductID>963</ProductID>  
         <Record_Data_DE120 />  
         <SubBIN>12345678</SubBIN>  
         <TLogIDOrg>0</TLogIDOrg>  
         <VL_Group>PMT-VL-003</VL_Group>  
         <Dom_Fee_Fixed>0.00</Dom_Fee_Fixed>  
         <Non_Dom_Fee_Fixed>0.00</Non_Dom_Fee_Fixed>  
         <Fx_Fee_Fixed>0.00</Fx_Fee_Fixed>  
         <Other_Fee_Amt>0.00</Other_Fee_Amt>  
         <Fx_Fee_Rate>0.00</Fx_Fee_Rate>  
         <Dom_Fee_Rate>0.00</Dom_Fee_Rate>  
         <Non_Dom_Fee_Rate>0.00</Non_Dom_Fee_Rate>  
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
         <GPS_POS_Capability>000000000000000000000001000000100000000000012345R</GPS_POS_Capability>  
         <GPS_POS_Data>0151000300000Nx000</GPS_POS_Data>  
         <Acquirer_Reference_Data_031>02713373332078336054127</Acquirer_Reference_Data_031>  
         <Response_Source />  
         <Response_Source_Why>0</Response_Source_Why>  
         <Message_Source />  
         <Message_Why>0</Message_Why>  
         <traceid_lifecycle>BNET-20231128-MRJRU72NS</traceid_lifecycle>  
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
         <Merch_Name>Hornbach Baumarkt AG F</Merch_Name>  
         <Merch_Street>Am Storrenacker 6</Merch_Street>  
         <Merch_City>Karlsruhe</Merch_City>  
         <Merch_Region>DEU</Merch_Region>  
         <Merch_Postcode>76139</Merch_Postcode>  
         <Merch_Country>DEU</Merch_Country>  
         <Merch_Tel />  
         <Merch_URL />  
         <Merch_Name_Other />  
         <Merch_Net_id />  
         <Merch_Tax_id>0</Merch_Tax_id>  
         <Merch_Contact />  
      </GetTransaction>  
   </s:Body>  
</s:Envelope>
```

#### Financial Reversal Response

Below is an example of HTTP response to the above Financial Notification message.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
   <soap:Body>  
      <GetTransactionResponse xmlns="http://tempuri.org/">  
         <GetTransactionResult>  
            <Acknowledgement>1</Acknowledgement>  
         </GetTransactionResult>  
      </GetTransactionResponse>  
   </soap:Body>  
</soap:Envelope>
```

[Back to Top](#Top)