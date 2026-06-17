# 3D Secure Query Details (Cardinal Batch)

API: `Ws_Query3DSecureDetails`

This web service enables you to view the phone number of a particular userâs token that has been enrolled for 3D secure. The service also returns the stored Thredd 3D Secure details for the token.

This web service uses the Cardinal batch file interface. (Legacy Option)

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <QueryType> | AN | 1 | 1 | Query Type. Valid values are:  0 = Return the responses of all tokens  1 = Return the response of this token only. Default is 0. | Mandatory | Omit |
| <Token> | N | 9 | 9 | The cardâs public token. Mandatory in the request and response. | Optional | Omit |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Tokens> |  |  |  | An array of token results. See [Token Results](#Token) below. | Optional | Omit |

#### Token Results

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <Token> | N | 9 | 9 | The cardâs public token. | Omit | Mandatory |
| <Phone> | AN | 1 | 15 | The phone number linked to the token. | Omit | Mandatory |
| <ResponseCode> | AN | 1 | 1 | Response code. | Omit | Mandatory |
| <LastModifiedType> | AN | 1 | 1 | Specify the last modified type:  1 = Create; 2 = Amend; 3 = Delete | Omit | Mandatory |
| <ResponseDescription> | AN | 1 | 50 | Response description. | Omit | Mandatory |
| <LastApprovedPhone> | AN | 1 | 15 | Legacy field. Not used. | Omit | Optional |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"   
xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">     
<soapenv:Header>        
    <hyp:AuthSoapHeader>           
    <hyp:strUserName>******</hyp:strUserName>           
    <hyp:strPassword>******</hyp:strPassword>        
    </hyp:AuthSoapHeader>   </soapenv:Header>     
    <soapenv:Body>        
    <hyp:Ws_Query3DSecureDetails>          
     <hyp:IssCode>PMT</hyp:IssCode>          
     <hyp:QueryType>0</hyp:QueryType>         
      <hyp:Token>123456789</hyp:Token>       
     </hyp:Ws_Query3DSecureDetails>    
 </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"   
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
xmlns:xsd="http://www.w3.org/2001/XMLSchema">     
    <soap:Body>        
     <Ws_Query3DSecureDetailsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">           
     <Ws_Query3DSecureDetailsResult>              
        <IssCode>PMT</IssCode>             
        <ActionCode>000</ActionCode>              
        <Tokens>                 
          <Token>                    
          <Token>123456789</Token>                    
          <Phone>+440123456789</Phone>                    
          <ResponseCode>-1</ResponseCode>                   
          <LastModifiedType>2</LastModifiedType>                    
          <ResponseDescription>PENDING_RESPONSE_CODE</ResponseDescription>                    
          <LastApprovedPhone/>                 
         </Token>              
       </Tokens>           
     </Ws_Query3DSecureDetailsResult>        
     </Ws_Query3DSecureDetailsResponse>     
     </soap:Body>  
 </soap:Envelope>  
 
```