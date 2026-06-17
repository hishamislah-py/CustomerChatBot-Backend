# Register a Customer for Banking

API: `Ws_Banking_CreateCustomer`

For Modulr Agency Banking integrations, you must register the customer prior to calling `Ws_CreateCard_V2` to create the bank account. This web service enables you to register customer details without creating associated bank accounts.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardDesign> | AN | 1 | 8 | The Thredd `Product ID`. For details, check with your Implementation Manager. | Mandatory |  |
| <Associates> | A list of Associate |  |  | A list of associates (for business customer accounts). Must contain at least one associate. For example, this could contain the details of the company directors for a limited company, or the partners for a partnership. For details, see [Associate](../Reference/Enums.htm#Associat). | Mandatory |  |
| <DocumentInfo> | A list of DocumentInfo |  |  | A list of document information (for business customer accounts). Examples of documents could be proof of a company director's identity or address, articles of association or a partnership agreement. For details, see [DocumentInfo](../Reference/Enums.htm#Document). | Optional |  |
| <ExpectedMonthlySpend> | N |  |  | An expected monthly spend must be included. If this is unknown, select an approximate amount. | Mandatory |  |
| <ExternalReference> | AN | 1 | 30 | Enables you to add your own external customer reference. | Optional |  |
| <IndustryCode> | AN |  |  | Industry code if this is a business customer. Mandatory for all `<Type>`except for 'INDIVIDUAL'. | Conditional |  |
| <RegisteredAddress> | A  Banking Address |  |  | The address of the company's registered office (for a business customer). For details, see [RegisteredAddress](../Reference/Enums.htm#Register). | Optional |  |
| <TCSVersion> | N |  |  | The version of the Modulr terms and conditions that you have agreed to. | Mandatory |  |
| <TradingAddress> | A Banking Address |  |  | Business customer trading address. Mandatory for all `<Type>` except for INDIVIDUAL. For details, see [TradingAddress](../Reference/Enums.htm#TradingA). | Conditional |  |
| <Type> | Enum  (see desc) |  |  | Type of the account to be opened. Takes values of: INDIVIDUAL, CHARITY, LLP, LPARTNRSHP, OPARTNRSHP, SOLETRADER, PLC, LLC, PCM\_INDIVIDUAL, PCM\_BUSINESS, TRUST and PREQUALIFIED. | Mandatory |  |
| <Name> | AN |  |  | Customer's company name (for a business customer). You can provide alpha-numeric characters plus: [ \_ ' @ , & Â£ $ â¬ Â¥ = # % â â : ; \ / < > Â« Â» ! â â â . ? - \*{ } + % ( )]. Mandatory for all `<Type>` except 'INDIVIDUAL'. | Conditional |  |
| <CompanyRegNumber> | AN |  |  | The company registration or incorporation number for a business customer. Only applicable for companies registered with Companies House. | Optional |  |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). If the action code is 576, full details can be found in `<Messages>`. | Omit | Mandatory |
| <Messages> | A list of BankingError |  |  | If the action code returned is 576, then full details of any Modulr errors are returned. See [BankingError](../Reference/Enums.htm#BankingE2). | Omit | Optional |
| <CustomerID> | AN | 10 | 10 | Unique identifier for the newly registered customer, returned in the response. Begins with 'C'. This must be used in all subsequent web service requests relating to this customer. | Omit | Mandatory |
| ComplianceData | Object |  |  | If `<Type>` is *PREQUALIFIED* then `ComplianceData` is mandatory and all fields under it should have a value. See [ComplianceData Fields](#Complian). | Conditional |  |

#### ComplianceData Fields

These fields are mandatory if `<Type>` is *PREQUALIFIED*.

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <TypeDescription> | AN | 1 | 200 | Description of the compliance data type. Expecting a string value of maximum length 200. | Conditional |  |
| <RiskLevel> | AN | 3 | 20 | Value can be LOW, MEDIUM, HIGH or UNDETERMINED. If any value other than these is submitted, then a default value UNDETERMINED is used. | Conditional |  |
| <VulnerabilityReasons> | AN | 6 | 30 | Expecting a string array of maximum length 30 per string element. Value can be one or more of the following elements: LIFE\_EVENTS, HEALTH, RESILIENCE, CAPABILITY, FINANCIAL\_DIFFICULTY. | Conditional |  |

#### Request

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
  <soap:Header>  
    <AuthSoapHeader xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <strUserName>******</strUserName>  
      <strPassword>******</strPassword>  
    </AuthSoapHeader>  
  </soap:Header>  
  <soap:Body>  
    <Ws_Banking_CreateCustomer xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <request>  
        <WSID>2021123456789</WSID>  
        <IssCode>PMT</IssCode>  
        <CardDesign>string</CardDesign>  
        <Associates>  
          <Associate>  
            <applicant>boolean</applicant>  
            <dateOfBirth>dateTime</dateOfBirth>  
            <documentInfo xsi:nil="true" />  
            <email>string</email>  
            <firstName>string</firstName>  
            <middleName>string</middleName>  
            <lastName>string</lastName>  
            <ownership>int</ownership>  
            <phone>string</phone>  
            <type>string</type>  
              
<homeAddress>  
          <addressLine1>string</addressLine1>  
          <addressLine2>string</addressLine2>  
          <posttown>string</posttown>  
          <postCode>string</postCode>  
          <country>string</country>  
        </homeAddress>  
          </Associate>  
        </Associates>  
        <DocumentInfo>  
          <DocumentInfo>  
            <filename>string</filename>  
            <filepath>string</filepath>  
            <uploadDate>dateTime</uploadDate>  
          </DocumentInfo>  
        </DocumentInfo>  
        <ExpectedMonthlySpend>decimal</ExpectedMonthlySpend>  
        <ExternalReference>string</ExternalReference>  
        <IndustryCode>string</IndustryCode>  
        <RegisteredAddress>  
          <addressLine1>string</addressLine1>  
          <addressLine2>string</addressLine2>  
          <posttown>string</posttown>  
          <postCode>string</postCode>  
          <country>string</country>  
        </RegisteredAddress>  
        <TCSVersion>int</TCSVersion>  
        <TradingAddress>  
          <addressLine1>string</addressLine1>  
          <addressLine2>string</addressLine2>  
          <posttown>string</posttown>  
          <postCode>string</postCode>  
          <country>string</country>  
        </TradingAddress>  
        <Type>INDIVIDUAL or CHARITY or LLP or LPARTNRSHP or OPARTNRSHP or SOLETRADER or PLC, LLC,  PCM_INDIVIDUAL, PCM_BUSINESS, TRUST and PREQUALIFIED.</Type>  
        <Name>string</Name>  
        <CompanyRegNumber>string</CompanyRegNumber>  
      <ComplianceData>  
         <hTypeDescription>Prequalified<TypeDescription>  
         <RiskLevel>HIGH<RiskLevel>  
         <VulnerabilityReasons>      
           <string>LIFE_EVENTS</string>  
           <string>HEALTH</string>  
         </VulnerabilityReasons>  
       </ComplianceData>  
      </request>  
    </Ws_Banking_CreateCustomer>  
  </soap:Body>  
</soap:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<Ws_Banking_CreateCustomerResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <Ws_Banking_CreateCustomerResult>  
        <WSID>2021123456789</WSID>  
        <IssCode> PMT </IssCode>  
        <ActionCode>string</ActionCode>  
        <CustomerID>string</CustomerID>  
        <Messages>  
            <BankingError>  
            <field>string</field>  
            <code>string</code>  
            <message>string</message>  
            <error>string</error>  
          </BankingError>  
        </Messages>  
      </Ws_Banking_CreateCustomerResult>  
    </Ws_Banking_CreateCustomerResponse>
```