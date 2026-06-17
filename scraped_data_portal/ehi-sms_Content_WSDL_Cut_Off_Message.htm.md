# 3.8 Cut-Off Message WSDL and Examples

This section provides a copy of the Cut off WSDL and examples of common transaction messages and responses.

## 3.8.1 Cut-Off Message WSDL

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8" ?>   
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:tns="http://tempuri.org/" xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" targetNamespace="http://tempuri.org/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">  
<wsdl:types>  
  <s:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">  
    <s:element name="Cut_Off">  
      <s:complexType>  
        <s:sequence>  
          <s:element minOccurs="1" maxOccurs="1" name="CutoffID" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="ProductID" type="s:int" />   
          <s:element minOccurs="0" maxOccurs="1" name="CutoffDate" type="s:string" />   
          <s:element minOccurs="1" maxOccurs="1" name="FirstTxn_ID" type="s:long" />   
          <s:element minOccurs="1" maxOccurs="1" name="LastTxn_ID" type="s:long" />   
          <s:element minOccurs="1" maxOccurs="1" name="Auths_Acknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="Auths_NotAcknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="Financials_Acknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="Financials_NotAcknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="LoadsUnloads_Acknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="LoadsUnloads_NotAcknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="BalanceAdjustExpiry_Acknowledged" type="s:int" />   
          <s:element minOccurs="1" maxOccurs="1" name="BalanceAdjustExpiry_NotAcknowledged" type="s:int" />   
        </s:sequence>  
      </s:complexType>  
    </s:element>  
    <s:element name="Cut_OffResponse">  
      <s:complexType>  
        <s:sequence>  
          <s:element minOccurs="0" maxOccurs="1" name="Cut_OffResult" type="s:string" />   
        </s:sequence>  
      </s:complexType>  
    </s:element>  
  </s:schema>  
</wsdl:types>  
<wsdl:message name="Cut_OffSoapIn">  
  <wsdl:part name="parameters" element="tns:Cut_Off" />   
</wsdl:message>  
<wsdl:message name="Cut_OffSoapOut">  
  <wsdl:part name="parameters" element="tns:Cut_OffResponse" />   
</wsdl:message>  
<wsdl:portType name="Service1Soap">  
  <wsdl:operation name="Cut_Off">  
    <wsdl:input message="tns:Cut_OffSoapIn" />   
    <wsdl:output message="tns:Cut_OffSoapOut" />   
  </wsdl:operation>  
</wsdl:portType>  
<wsdl:binding name="Service1Soap" type="tns:Service1Soap">  
  <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />   
  <wsdl:operation name="Cut_Off">  
    <soap:operation soapAction="http://tempuri.org/Cut_Off" style="document" />   
    <wsdl:input>  
      <soap:body use="literal" />   
    </wsdl:input>  
    <wsdl:output>  
      <soap:body use="literal" />   
    </wsdl:output>  
  </wsdl:operation>  
</wsdl:binding>  
<wsdl:binding name="Service1Soap12" type="tns:Service1Soap">  
  <soap12:binding transport="http://schemas.xmlsoap.org/soap/http" />   
  <wsdl:operation name="Cut_Off">  
    <soap12:operation soapAction="http://tempuri.org/Cut_Off" style="document" />   
    <wsdl:input>  
      <soap12:body use="literal" />   
    </wsdl:input>  
    <wsdl:output>  
      <soap12:body use="literal" />   
    </wsdl:output>  
  </wsdl:operation>  
</wsdl:binding>  
<wsdl:service name="Service1">  
  <wsdl:port name="Service1Soap" binding="tns:Service1Soap">  
    <soap:address location="http://localhost:22355/Service1.asmx" />   
  </wsdl:port>  
  <wsdl:port name="Service1Soap12" binding="tns:Service1Soap12">  
    <soap12:address location="http://localhost:22355/Service1.asmx" />   
  </wsdl:port>  
</wsdl:service>  
</wsdl:definitions>
```

## 3.8.2 Example Cut-Off

### Example Cut-Off Request Message

[Copy](javascript:void(0);)

```
HTTP POST body data:  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
  <s:Body>  
     <Cut_Off xmlns="http://tempuri.org/">  
        <CutoffID>983</CutoffID>  
        <ProductID>1686</ProductID>  
        <CutoffDate>2021-03-23 13:16:42.999</CutoffDate>  
        <FirstTxn_ID>245001</FirstTxn_ID>  
        <LastTxn_ID>256999</LastTxn_ID>  
        <Auths_Acknowledged>15</Auths_Acknowledged>  
        <Auths_NotAcknowledged>80</Auths_NotAcknowledged>  
        <Financials_Acknowledged>200</Financials_Acknowledged>  
        <Financials_NotAcknowledged>16</Financials_NotAcknowledged>  
        <LoadsUnloads_Acknowledged>1819</LoadsUnloads_Acknowledged>  
        <LoadsUnloads_NotAcknowledged>1001</LoadsUnloads_NotAcknowledged>          <BalanceAdjustExpiry_Acknowledged>256</BalanceAdjustExpiry_Acknowledged>  
<BalanceAdjustExpiry_NotAcknowledged>8612</BalanceAdjustExpiry_NotAcknowledged>  
     </Cut_Off>  
  </s:Body>  
</s:Envelope>
```

### Example Cut-Off Response Message

This is an example response to the above example request message, showing the HTTP Response body data:

[Copy](javascript:void(0);)

```
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
    <s:Body>  
        <Cut_OffResponse xmlns="http://tempuri.org/">  
            <Cut_OffResult>1</Cut_OffResult>  
        </Cut_OffResponse>  
    </s:Body>  
</s:Envelope>
```