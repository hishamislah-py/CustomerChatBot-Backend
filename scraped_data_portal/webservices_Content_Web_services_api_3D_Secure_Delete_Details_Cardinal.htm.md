# 3D Secure Delete Details (Cardinal Batch)

API: `Ws_Delete3DSecureDetails`

This web service enables you to delete 3D secure details for a card (where you are using the Cardinal 3D Secure service).

This web service uses the Cardinal batch file interface. (Legacy Option)

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <Token> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

Request

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
           <hyp:Ws_Delete3DSecureDetails>  
               <hyp:IssCode>PMT</hyp:IssCode>  
               <hyp:Token>123456789</hyp:Token>  
           </hyp:Ws_Delete3DSecureDetails>  
       </soapenv:Body>  
</soapenv:Envelope>
```

Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Delete3DSecureDetailsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Delete3DSecureDetailsResult>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
         </Ws_Delete3DSecureDetailsResult>  
      </Ws_Delete3DSecureDetailsResponse>  
   </soap:Body>  
</soap:Envelope>
```