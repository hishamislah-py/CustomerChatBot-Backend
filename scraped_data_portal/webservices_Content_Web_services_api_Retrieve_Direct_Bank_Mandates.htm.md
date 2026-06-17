# Retrieve Direct Debit Mandates

API: `Ws_Banking_DD_GetMandate`

This Web service retrieves all mandates for a given token.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Optional | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Optional | Omit |
| <CardDesign> | AN | 1 | 8 | The Thredd `Product ID`. For details, check with your Implementation Manager. | Mandatory | Omit |
| <Token> | N | 1 | 9 | The 9 digit public token associated with the account. | Mandatory | Omit |
| <DD\_Mandates> | A list of DD\_Mandates |  |  | A list of mandates. See [DD\_Mandates.](../Reference/Enums.htm#DDMandates) | Omit | Mandatory |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). If the action code is 576, full details can be found in `<Messages>`. | Omit | Mandatory |
| <Messages> | A list of BankingError |  |  | Displays details of the error message. See [BankingError.](../Reference/Enums.htm#BankingE2) | Omit | Optional |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. | Omit | Optional |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <!--Optional:-->  
         <hyp:strUserName>OnePayTest1</hyp:strUserName>  
         <!--Optional:-->  
         <hyp:strPassword>**********</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:WS_Banking_DD_GetMandates>  
         <hyp:request>  
            <!--Optional:-->  
            <hyp:WSID>${=(long)(Math.random()*Long.MAX_VALUE)}</hyp:WSID>  
            <!--Optional:-->  
            <hyp:IssCode>ONE</hyp:IssCode>  
            <hyp:CardDesign>2018</hyp:CardDesign>  
            <hyp:Token>106239304</hyp:Token>  
         </hyp:request>  
      </hyp:WS_Banking_DD_GetMandates>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <WS_Banking_DD_GetMandatesResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <WS_Banking_DD_GetMandatesResult>  
            <WSID>3371287256120270848</WSID>  
            <ActionCode>000</ActionCode>  
            <DD_Mandates>  
               <DD_Mandate>  
                  <MandateId>M101BZWED</MandateId>  
                  <MerchantName>M101BZWED</MerchantName>  
                  <LastScheduledAmount>5.5550</LastScheduledAmount>  
                  <MandateStatus>EXPIRE</MandateStatus>  
                  <MandateCreatedDate>17/03/2022 10:11:28</MandateCreatedDate>  
               </DD_Mandate>  
               <DD_Mandate>  
                  <MandateId>M101BZWEF</MandateId>  
                  <MerchantName>M101BZWED</MerchantName>  
                  <LastScheduledAmount>0.0000</LastScheduledAmount>  
                  <MandateStatus>CANCEL</MandateStatus>  
                  <MandateCreatedDate>17/03/2022 10:17:08</MandateCreatedDate>  
               </DD_Mandate>  
            </DD_Mandates>  
            <Messages/>  
         </WS_Banking_DD_GetMandatesResult>  
      </WS_Banking_DD_GetMandatesResponse>  
   </soap:Body>  
</soap:Envelope>
```