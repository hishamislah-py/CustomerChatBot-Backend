# 3.2 GetTransaction WSDL

This section provides a copy of the GetTransaction WSDL.

For details of the 2001 XMLSchema datatypes, see: https://www.w3.org/2001/XMLSchema.xsd

[Copy](javascript:void(0);)

### Version 5.2 WSDL

[Copy](javascript:void(0);)

```
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://tempuri.org/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:http="http://schemas.microsoft.com/ws/06/2004/policy/http" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" targetNamespace="http://tempuri.org/" name="IEndpointVersion52" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">  
  <wsdl:types>  
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">  
      <xsd:element name="GetTransaction">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_id_DE32" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ActBal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Amt_DE54" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Amt_Tran_Fee_DE28" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Auth_Code_DE38" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Avl_Bal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="BlkAmt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Cust_Ref" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FX_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadSRC" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_ID_DE42" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_DE43" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Note" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE22" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE61" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Termnl_DE41" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Time_DE12" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Proc_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Resp_Code_DE39" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Ret_Ref_No_DE37" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Status_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Token" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Trans_link" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_CCy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_GPS_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Stat_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXN_Time_DE07" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE48" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Authorised_by_GPS" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AVS_Result" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CU_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="InstCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MTID" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ProductID" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Record_Data_DE120" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="SubBIN" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TLogIDOrg" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="VL_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="EHIVersion" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Other_Fee_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE124" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CVV2" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Expiry_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PAN_Sequence_Number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Enc_Algorithm" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Key_Index" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SendingAttemptCount" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Capability" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Reference_Data_031" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="traceid_lifecycle" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence_Exthost" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_expdate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_status" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creatorStatus" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_wallet" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_lang" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceTelNum" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceIp" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceId" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceName" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationExpiry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethodData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethod" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ICC_System_Related_Data_DE55" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Street" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_City" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Region" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Postcode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tel" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_URL" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_Other" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Net_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tax_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Contact" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_expdate_utc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Matching_Txn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Reason_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dispute_Condition" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Chargeback_Reference_Id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Forwarder_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Clearing_Process_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settlement_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="DCC_Indicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn_final" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_count" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SettlementIndicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BaseAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_BaseAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Date_DE13" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Message" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Original" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Currency_Conversion_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Mastercard_AdviceReasonCode_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Original_Data_Elements_DE90" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_ResponseInfo_DE44" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_STIP_Reason_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Issuer_Settle_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Replacement_Amounts_DE95" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_POS_Data_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Transaction_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Misc_TLV_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_PanSource" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ClearingFileID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Fraud_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SenderData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ReceiverData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationAmountUpper" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationCurrency" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationMerchantHash" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FxProviderCardholderRate" type="xsd:decimal" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SchemeTransactionIdentifier" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TokenUniqueReference" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentTokenPan" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FleetData" type="xsd:string" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:element name="GetTransactionResponse">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="GetTransactionResult" type="tns:EndpointResponse52" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:complexType name="EndpointResponse52">  
        <xsd:sequence>  
          <xsd:element minOccurs="0" maxOccurs="1" name="MerchantAdvice" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Responsestatus" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance" type="xsd:double" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Acknowledgement" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="LoadAmount" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Bill_Amt_Approved" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Update_Balance" type="xsd:int" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="New_Balance_Sequence_Exthost" type="xsd:long" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="CVV2_Result" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance_GPS_STIP" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance_GPS_STIP" type="xsd:double" />  
        </xsd:sequence>  
      </xsd:complexType>  
    </xsd:schema>  
  </wsdl:types>  
  <wsdl:message name="IEndpointVersion52_GetTransaction_InputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransaction" />  
  </wsdl:message>  
  <wsdl:message name="IEndpointVersion52_GetTransaction_OutputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransactionResponse" />  
  </wsdl:message>  
  <wsdl:portType name="IEndpointVersion52">  
    <wsdl:operation name="GetTransaction">  
      <wsdl:input message="tns:IEndpointVersion52_GetTransaction_InputMessage" />  
      <wsdl:output message="tns:IEndpointVersion52_GetTransaction_OutputMessage" />  
    </wsdl:operation>  
  </wsdl:portType>  
  <wsdl:binding name="BasicHttpBinding_IEndpointVersion52_soap" type="tns:IEndpointVersion52">  
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />  
    <wsdl:operation name="GetTransaction">  
      <soap:operation soapAction="http://tempuri.org/IEndpointVersion52/GetTransaction" style="document" />  
      <wsdl:input>  
        <soap:body use="literal" />  
      </wsdl:input>  
      <wsdl:output>  
        <soap:body use="literal" />  
      </wsdl:output>  
    </wsdl:operation>  
  </wsdl:binding>  
  <wsdl:service name="IEndpointVersion52">  
    <wsdl:port name="BasicHttpBinding_IEndpointVersion52_soap" binding="tns:BasicHttpBinding_IEndpointVersion52_soap">  
      <soap:address location="http://localhost:5009/Version5.2/Service.asmx" />  
    </wsdl:port>  
  </wsdl:service>  
</wsdl:definitions>
```

### Version 5.3 WSDL

[Copy](javascript:void(0);)

```
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://tempuri.org/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:http="http://schemas.microsoft.com/ws/06/2004/policy/http" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" targetNamespace="http://tempuri.org/" name="IEndpointVersion53" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">  
  <wsdl:types>  
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">  
      <xsd:element name="GetTransaction">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_id_DE32" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ActBal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Amt_DE54" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Amt_Tran_Fee_DE28" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Auth_Code_DE38" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Avl_Bal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="BlkAmt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Cust_Ref" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FX_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadSRC" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_ID_DE42" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_DE43" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Note" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE22" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE61" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Termnl_DE41" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Time_DE12" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Proc_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Resp_Code_DE39" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Ret_Ref_No_DE37" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Status_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Token" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Trans_link" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_CCy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_GPS_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Stat_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXN_Time_DE07" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE48" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Authorised_by_GPS" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AVS_Result" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CU_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="InstCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MTID" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ProductID" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Record_Data_DE120" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="SubBIN" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TLogIDOrg" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="VL_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="EHIVersion" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Other_Fee_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE124" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CVV2" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Expiry_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PAN_Sequence_Number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Enc_Algorithm" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Key_Index" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SendingAttemptCount" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Capability" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Reference_Data_031" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="traceid_lifecycle" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence_Exthost" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_expdate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_status" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creatorStatus" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_wallet" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_lang" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceTelNum" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceIp" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceId" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceName" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationExpiry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethodData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethod" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ICC_System_Related_Data_DE55" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Street" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_City" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Region" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Postcode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tel" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_URL" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_Other" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Net_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tax_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Contact" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_expdate_utc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Matching_Txn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Reason_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dispute_Condition" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Chargeback_Reference_Id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Forwarder_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Clearing_Process_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settlement_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="DCC_Indicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn_final" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_count" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SettlementIndicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BaseAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_BaseAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Date_DE13" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Message" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Original" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Currency_Conversion_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Mastercard_AdviceReasonCode_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Original_Data_Elements_DE90" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_ResponseInfo_DE44" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_STIP_Reason_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Issuer_Settle_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Replacement_Amounts_DE95" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_POS_Data_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Transaction_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Misc_TLV_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_PanSource" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ClearingFileID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Fraud_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SenderData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ReceiverData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationAmountUpper" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationCurrency" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationMerchantHash" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FxProviderCardholderRate" type="xsd:decimal" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SchemeTransactionIdentifier" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TokenUniqueReference" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentTokenPan" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FleetData" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ElapsedTimeToLive" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="NumberOfTransactionsCount" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="TotalOfTransactionAmounts" type="xsd:decimal" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:element name="GetTransactionResponse">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="GetTransactionResult" type="tns:EndpointResponse53" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:complexType name="EndpointResponse53">  
        <xsd:sequence>  
          <xsd:element minOccurs="0" maxOccurs="1" name="MerchantAdvice" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Responsestatus" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance" type="xsd:double" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Acknowledgement" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="LoadAmount" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Bill_Amt_Approved" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Update_Balance" type="xsd:int" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="New_Balance_Sequence_Exthost" type="xsd:long" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="CVV2_Result" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance_GPS_STIP" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance_GPS_STIP" type="xsd:double" />  
        </xsd:sequence>  
      </xsd:complexType>  
    </xsd:schema>  
  </wsdl:types>  
  <wsdl:message name="IEndpointVersion53_GetTransaction_InputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransaction" />  
  </wsdl:message>  
  <wsdl:message name="IEndpointVersion53_GetTransaction_OutputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransactionResponse" />  
  </wsdl:message>  
  <wsdl:portType name="IEndpointVersion53">  
    <wsdl:operation name="GetTransaction">  
      <wsdl:input message="tns:IEndpointVersion53_GetTransaction_InputMessage" />  
      <wsdl:output message="tns:IEndpointVersion53_GetTransaction_OutputMessage" />  
    </wsdl:operation>  
  </wsdl:portType>  
  <wsdl:binding name="BasicHttpBinding_IEndpointVersion53_soap" type="tns:IEndpointVersion53">  
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />  
    <wsdl:operation name="GetTransaction">  
      <soap:operation soapAction="http://tempuri.org/IEndpointVersion53/GetTransaction" style="document" />  
      <wsdl:input>  
        <soap:body use="literal" />  
      </wsdl:input>  
      <wsdl:output>  
        <soap:body use="literal" />  
      </wsdl:output>  
    </wsdl:operation>  
  </wsdl:binding>  
  <wsdl:service name="IEndpointVersion53">  
    <wsdl:port name="BasicHttpBinding_IEndpointVersion53_soap" binding="tns:BasicHttpBinding_IEndpointVersion53_soap">  
      <soap:address location="http://localhost:5009/Version5.3/Service.asmx" />  
    </wsdl:port>  
  </wsdl:service>  
</wsdl:definitions>
```

### Version 5.4 WSDL

[Copy](javascript:void(0);)

```
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://tempuri.org/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:http="http://schemas.microsoft.com/ws/06/2004/policy/http" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" targetNamespace="http://tempuri.org/" name="IEndpointVersion54" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">  
  <wsdl:types>  
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">  
      <xsd:element name="GetTransaction">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_id_DE32" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ActBal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Amt_DE54" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Amt_Tran_Fee_DE28" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Auth_Code_DE38" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Avl_Bal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="BlkAmt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Cust_Ref" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FX_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadSRC" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_ID_DE42" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_DE43" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Note" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE22" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE61" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Termnl_DE41" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Time_DE12" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Proc_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Resp_Code_DE39" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Ret_Ref_No_DE37" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Status_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Token" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Trans_link" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_CCy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_GPS_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Stat_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXN_Time_DE07" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE48" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Authorised_by_GPS" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AVS_Result" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CU_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="InstCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MTID" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ProductID" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Record_Data_DE120" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="SubBIN" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TLogIDOrg" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="VL_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="EHIVersion" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Other_Fee_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE124" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CVV2" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Expiry_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PAN_Sequence_Number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Enc_Algorithm" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Key_Index" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SendingAttemptCount" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Capability" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Reference_Data_031" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="traceid_lifecycle" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence_Exthost" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_expdate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_status" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creatorStatus" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_wallet" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_lang" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceTelNum" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceIp" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceId" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceName" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationExpiry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethodData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethod" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ICC_System_Related_Data_DE55" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Street" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_City" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Region" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Postcode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tel" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_URL" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_Other" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Net_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tax_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Contact" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_expdate_utc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Matching_Txn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Reason_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dispute_Condition" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Chargeback_Reference_Id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Forwarder_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Clearing_Process_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settlement_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="DCC_Indicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn_final" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_count" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SettlementIndicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BaseAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_BaseAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Date_DE13" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Message" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Original" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Currency_Conversion_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Mastercard_AdviceReasonCode_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Original_Data_Elements_DE90" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_ResponseInfo_DE44" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_STIP_Reason_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Issuer_Settle_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Replacement_Amounts_DE95" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_POS_Data_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Transaction_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Misc_TLV_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_PanSource" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ClearingFileID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Fraud_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SenderData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ReceiverData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationAmountUpper" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationCurrency" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationMerchantHash" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FxProviderCardholderRate" type="xsd:decimal" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SchemeTransactionIdentifier" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TokenUniqueReference" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentTokenPan" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FleetData" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ElapsedTimeToLive" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="NumberOfTransactionsCount" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="TotalOfTransactionAmounts" type="xsd:decimal" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FlexEligibilityIndicator" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FlexEligibleUseCaseIds" type="xsd:string" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:element name="GetTransactionResponse">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="GetTransactionResult" type="tns:EndpointResponse54" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:complexType name="EndpointResponse54">  
        <xsd:sequence>  
          <xsd:element minOccurs="0" maxOccurs="1" name="FlexVFCPaymentCredential" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="FlexSelectedUseCaseId" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="MerchantAdvice" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Responsestatus" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance" type="xsd:double" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Acknowledgement" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="LoadAmount" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Bill_Amt_Approved" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Update_Balance" type="xsd:int" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="New_Balance_Sequence_Exthost" type="xsd:long" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="CVV2_Result" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance_GPS_STIP" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance_GPS_STIP" type="xsd:double" />  
        </xsd:sequence>  
      </xsd:complexType>  
    </xsd:schema>  
  </wsdl:types>  
  <wsdl:message name="IEndpointVersion54_GetTransaction_InputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransaction" />  
  </wsdl:message>  
  <wsdl:message name="IEndpointVersion54_GetTransaction_OutputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransactionResponse" />  
  </wsdl:message>  
  <wsdl:portType name="IEndpointVersion54">  
    <wsdl:operation name="GetTransaction">  
      <wsdl:input message="tns:IEndpointVersion54_GetTransaction_InputMessage" />  
      <wsdl:output message="tns:IEndpointVersion54_GetTransaction_OutputMessage" />  
    </wsdl:operation>  
  </wsdl:portType>  
  <wsdl:binding name="BasicHttpBinding_IEndpointVersion54_soap" type="tns:IEndpointVersion54">  
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />  
    <wsdl:operation name="GetTransaction">  
      <soap:operation soapAction="http://tempuri.org/IEndpointVersion54/GetTransaction" style="document" />  
      <wsdl:input>  
        <soap:body use="literal" />  
      </wsdl:input>  
      <wsdl:output>  
        <soap:body use="literal" />  
      </wsdl:output>  
    </wsdl:operation>  
  </wsdl:binding>  
  <wsdl:service name="IEndpointVersion54">  
    <wsdl:port name="BasicHttpBinding_IEndpointVersion54_soap" binding="tns:BasicHttpBinding_IEndpointVersion54_soap">  
      <soap:address location="http://localhost:5009/Version5.4/Service.asmx" />  
    </wsdl:port>  
  </wsdl:service>  
</wsdl:definitions>
```

### Verson 5.5 WSDL

[Copy](javascript:void(0);)

```
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://tempuri.org/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:http="http://schemas.microsoft.com/ws/06/2004/policy/http" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" targetNamespace="http://tempuri.org/" name="IEndpointVersion55" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">  
  <wsdl:types>  
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">  
      <xsd:element name="GetTransaction">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_id_DE32" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ActBal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Amt_DE54" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Amt_Tran_Fee_DE28" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Auth_Code_DE38" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Avl_Bal" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Bill_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="BlkAmt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Cust_Ref" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FX_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadSRC" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="LoadType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MCC_Pad" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_ID_DE42" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_DE43" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Note" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE22" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Data_DE61" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Termnl_DE41" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Time_DE12" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Proc_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Resp_Code_DE39" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Ret_Ref_No_DE37" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settle_Ccy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Status_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Token" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Trans_link" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_CCy" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Desc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_GPS_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Stat_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TXN_Time_DE07" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Txn_Type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE48" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Authorised_by_GPS" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AVS_Result" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CU_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="InstCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="MTID" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ProductID" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Record_Data_DE120" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="SubBIN" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TLogIDOrg" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="VL_Group" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="EHIVersion" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Fixed" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Other_Fee_Amt" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Fx_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Non_Dom_Fee_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Additional_Data_DE124" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="CVV2" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Expiry_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PAN_Sequence_Number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Enc_Algorithm" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PIN_Key_Index" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SendingAttemptCount" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="source_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_ctry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account_format" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="dest_bank_account" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Capability" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="GPS_POS_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Reference_Data_031" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Response_Source_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Source" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Message_Why" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="traceid_lifecycle" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Balance_Sequence_Exthost" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_expdate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_status" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_creatorStatus" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_wallet" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceType" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_lang" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceTelNum" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceIp" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceId" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_deviceName" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationCode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationExpiry" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethodData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_activationMethod" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ICC_System_Related_Data_DE55" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Street" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_City" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Region" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Postcode" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tel" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_URL" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Name_Other" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Net_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Tax_id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Merch_Contact" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_type" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="auth_expdate_utc" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Matching_Txn_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Reason_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Dispute_Condition" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Chargeback_Reference_Id" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Forwarder_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Currency_Code_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Interchange_Amount_Fee_Settlement" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Clearing_Process_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Settlement_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="DCC_Indicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_txn_final" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_number" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="multi_part_count" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SettlementIndicator" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_TxnAmt_To_BaseAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_BaseAmt_To_BillAmt_Rate" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="POS_Date_DE13" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Message" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Traceid_Original" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Currency_Conversion_Date" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Mastercard_AdviceReasonCode_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Original_Data_Elements_DE90" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_ResponseInfo_DE44" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_STIP_Reason_Code" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Issuer_Settle_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Replacement_Amounts_DE95" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Visa_POS_Data_DE60" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Transaction_ID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Misc_TLV_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Acquirer_Country" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentToken_PanSource" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ClearingFileID" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="Network_Fraud_Data" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SenderData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="ReceiverData" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationAmountUpper" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationCurrency" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="AuthenticationMerchantHash" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FxProviderCardholderRate" type="xsd:decimal" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="SchemeTransactionIdentifier" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="TokenUniqueReference" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="PaymentTokenPan" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FleetData" type="xsd:string" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="ElapsedTimeToLive" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="NumberOfTransactionsCount" type="xsd:int" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="TotalOfTransactionAmounts" type="xsd:decimal" />  
            <xsd:element minOccurs="1" maxOccurs="1" name="FlexEligibilityIndicator" type="xsd:int" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="FlexEligibleUseCaseIds" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="NetworkTransactionId2" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="NetworkRelatedTransactionId" type="xsd:string" />  
            <xsd:element minOccurs="0" maxOccurs="1" name="NetworkLinkValidation" type="xsd:string" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:element name="GetTransactionResponse">  
        <xsd:complexType>  
          <xsd:sequence>  
            <xsd:element minOccurs="0" maxOccurs="1" name="GetTransactionResult" type="tns:EndpointResponse55" />  
          </xsd:sequence>  
        </xsd:complexType>  
      </xsd:element>  
      <xsd:complexType name="EndpointResponse55">  
        <xsd:sequence>  
          <xsd:element minOccurs="0" maxOccurs="1" name="FlexPaymentCredential" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="FlexSelectedUseCaseId" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="MerchantAdvice" type="xsd:string" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Responsestatus" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance" type="xsd:double" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="Acknowledgement" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="LoadAmount" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Bill_Amt_Approved" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="Update_Balance" type="xsd:int" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="New_Balance_Sequence_Exthost" type="xsd:long" />  
          <xsd:element minOccurs="0" maxOccurs="1" name="CVV2_Result" type="xsd:string" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="CurBalance_GPS_STIP" type="xsd:double" />  
          <xsd:element minOccurs="1" maxOccurs="1" name="AvlBalance_GPS_STIP" type="xsd:double" />  
        </xsd:sequence>  
      </xsd:complexType>  
    </xsd:schema>  
  </wsdl:types>  
  <wsdl:message name="IEndpointVersion55_GetTransaction_InputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransaction" />  
  </wsdl:message>  
  <wsdl:message name="IEndpointVersion55_GetTransaction_OutputMessage">  
    <wsdl:part name="parameters" element="tns:GetTransactionResponse" />  
  </wsdl:message>  
  <wsdl:portType name="IEndpointVersion55">  
    <wsdl:operation name="GetTransaction">  
      <wsdl:input message="tns:IEndpointVersion55_GetTransaction_InputMessage" />  
      <wsdl:output message="tns:IEndpointVersion55_GetTransaction_OutputMessage" />  
    </wsdl:operation>  
  </wsdl:portType>  
  <wsdl:binding name="BasicHttpBinding_IEndpointVersion55_soap" type="tns:IEndpointVersion55">  
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />  
    <wsdl:operation name="GetTransaction">  
      <soap:operation soapAction="http://tempuri.org/IEndpointVersion55/GetTransaction" style="document" />  
      <wsdl:input>  
        <soap:body use="literal" />  
      </wsdl:input>  
      <wsdl:output>  
        <soap:body use="literal" />  
      </wsdl:output>  
    </wsdl:operation>  
  </wsdl:binding>  
  <wsdl:service name="IEndpointVersion55">  
    <wsdl:port name="BasicHttpBinding_IEndpointVersion55_soap" binding="tns:BasicHttpBinding_IEndpointVersion55_soap">  
      <soap:address location="http://localhost:5009/Version5.5/Service.asmx" />  
    </wsdl:port>  
  </wsdl:service>  
</wsdl:definitions>
```