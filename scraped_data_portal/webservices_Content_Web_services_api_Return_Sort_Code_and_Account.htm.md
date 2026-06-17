# Return Sort Code and Account

API: `Ws_Banking_ReturnBankDetailsFromToken`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service returns the sort code and account number (for UK bank accounts provided through programmes using Agency Banking) from a token.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd.  Mandatory in the request. If only `<IssCode>` is present in the request, then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. | Mandatory | Mandatory |
| <SortCode> | N | 6 | 6 | The sort code associated with the token. | Omit | Mandatory |
| <AccountNumber> | N | 8 | 8 | The account number associated with the token. | Omit | Mandatory |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. | Omit | Optional |

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
      <hyp:Ws_Banking_ReturnBankDetailsFromToken>  
         <hyp:request>  
            <hyp:WSID>20160415093831</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
         </hyp:request>  
      </hyp:Ws_Banking_ReturnBankDetailsFromToken>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_ReturnBankDetailsFromTokenResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_ReturnBankDetailsFromTokenResult>  
            <WSID>20160415093831</WSID>  
            <PublicToken>891614123</PublicToken>  
            <SortCode>666666</SortCode>  
            <AccountNumber>00000186</AccountNumber>  
             <ErrorText></ErrorText>  
            <ActionCode>000</ActionCode>  
         </Ws_Banking_ReturnBankDetailsFromTokenResult>  
      </Ws_Banking_ReturnBankDetailsFromTokenResponse>  
   </soap:Body>  
</soap:Envelope>
```