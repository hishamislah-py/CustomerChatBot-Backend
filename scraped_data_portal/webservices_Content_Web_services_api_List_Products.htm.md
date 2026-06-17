# List Products

API: `Ws_List_Products`

This web service enables you to list products your program has on Thredd systems and view the details of each product.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <ProductInfo> | - | - | - | A list of ProductListInfo data, See [ProductListInfo](#Product) below. Can occur multiple times within the message. |  |  |

#### ProductListInfo

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <ProductID> | N | 1 | 10 | The identifier of the Modulr card product, or `Product ID`, within Thredd. For details, check with your Implementation Manager. | Omit | Mandatory |
| <ProductName> | AN | 1 | 50 | Name of the product. | Omit | Mandatory |
| <ProductDesc> | AN | 1 | 100 | Product description. | Omit | Mandatory |
| <ProgramID> | AN | 1 | 50 | Program ID. | Omit | Mandatory |
| <Currency> | AN | 3 | 3 | Billing currency. | Omit | Mandatory |
| <CrdProduct> | AN | 1 | 50 | Scheme name. For example, Visa, Mastercard or Discover. | Omit | Mandatory |
| <GroupLimitCode> | AN | 1 | 10 | Group code of the [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). | Omit | Mandatory |
| <GroupFeeTranCode> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). | Omit | Mandatory |
| <GroupFeeMasterCode> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). | Omit | Mandatory |
| <GroupFeeWebCode> | AN | 1 | 10 | Group code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#). | Omit | Mandatory |
| <GroupMCCCode> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). | Omit | Mandatory |
| <GroupUsageCode> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). | Omit | Mandatory |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>******</hyp:strUserName>  
         <hyp:strPassword>******</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_List_Products>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
      </hyp:Ws_List_Products>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_List_ProductsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_List_ProductsResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <SysDate>2014-11-26</SysDate>  
            <ActionCode>000</ActionCode>  
            <ProductInfo>  
               <ProductListInfo>  
                  <ProductID>100</ProductID>  
                  <ProductName>PRD1</ProductName>  
                  <ProductDesc>Product 1</ ProductDesc >  
                  <ProgramID>PRD1</ProgramID>  
                  <Currency>GBP</Currency>  
                  <CrdProduct>MCRD</CrdProduct>  
                  <GroupLimitCode>GRPLIMIT1</GroupLimitCode>  
                  <GroupFeeTranCode>GRPAUTH1</GroupFeeTranCode>  
                  <GroupFeeMasterCode>GRPREC1</GroupFeeMasterCode>  
                  <GroupFeeWebCode>GRPWEB1</GroupFeeWebCode>  
                  <GroupMCCCode>MCC1</GroupMCCCode>  
                  <GroupUsageCode>USAGE1</GroupUsageCode>  
               </ProductListInfo>  
               <ProductListInfo>  
                  <ProductID>101</ProductID>  
                  <ProductName>PRD2</ProductName>  
                  <ProductDesc>Product 2</ ProductDesc >  
                  <ProgramID>PRD2</ProgramID>  
                  <Currency>USD</Currency>  
                  <CrdProduct>MCRD</CrdProduct>  
                  <GroupLimitCode>GRPLIMIT2</GroupLimitCode>  
                  <GroupFeeTranCode>GRPAUTH2</GroupFeeTranCode>  
                  <GroupFeeMasterCode>GRPREC2</GroupFeeMasterCode>  
                  <GroupFeeWebCode>GRPWEB2</GroupFeeWebCode>  
                  <GroupMCCCode>MCC2</GroupMCCCode>  
                  <GroupUsageCode>USAGE2</GroupUsageCode>  
               </ProductListInfo>  
               <ProductListInfo>  
                  <ProductID>102</ProductID>  
                  <ProductName>PRD3</ProductName>  
                  <ProductDesc>Product 3</ ProductDesc >  
                  <ProgramID>PRD3</ProgramID>  
                  <Currency>EUR</Currency>  
                  <CrdProduct>MCRD</CrdProduct>  
                  <GroupLimitCode>GRPLIMIT3</GroupLimitCode>  
                  <GroupFeeTranCode>GRPAUTH3</GroupFeeTranCode>  
                  <GroupFeeMasterCode>GRPREC3</GroupFeeMasterCode>  
                  <GroupFeeWebCode>GRPWEB3</GroupFeeWebCode>  
                  <GroupMCCCode>MCC3</GroupMCCCode>  
                  <GroupUsageCode>USAGE3</GroupUsageCode>  
               </ProductListInfo>  
            </ProductInfo>  
         </Ws_List_ProductsResult>  
      </Ws_List_ProductsResponse>  
   </soap:Body>  
</soap:Envelope>
```