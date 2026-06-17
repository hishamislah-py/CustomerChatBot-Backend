# Check Service Availability

API: `Ws_Check`

This web service is used to check web service availability. It validates the SOAP credentials and Issuer Code.

Thredd has extensive automated monitoring of web services availability and response times. Our current annual service availability is over 99.96%.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). If the web service is available, returns â000â. | Omit | Mandatory |

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
      <hyp:Ws_Check>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
      </hyp:Ws_Check>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CheckResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CheckResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>              
            <ActionCode>000</ActionCode>             
         </Ws_CheckResult >  
      </ Ws_CheckResponse>  
   </soap:Body>  
</soap:Envelope>
```