# 3D Secure Update Last Modified Type (Cardinal Batch)

API: `Ws_UpdateLastModifiedType`

This web service lets you clear the `<LastModifiedType>` flag so that you can resend another enrolment for the same card to Cardinal. For example, you can use it to re-enrol a deleted card or to update the status of a card which has an incorrectly sent status. To do this, set the `LastModifiedType>` for the token to 1.

This web service uses the Cardinal batch file interface. (Legacy Option)

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <LastModifiedType> | AN | 1 | 1 | Specify the last modified type:  1 = Create; 2 = Amend; 3 = Delete | Mandatory | Mandatory |
| <Token> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

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
      <hyp:Ws_UpdateLastModifiedType>  
          <hyp:IssCode>PMT</hyp:IssCode>  
          <hyp:LastModifiedType>3</hyp:LastModifiedType>  
          <hyp:Token>123456789</hyp:Token>  
       </hyp:Ws_UpdateLastModifiedType>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_UpdateLastModifiedTypeResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_UpdateLastModifiedTypeResult>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
         </Ws_UpdateLastModifiedTypeResult>  
      </Ws_UpdateLastModifiedTypeResponse>  
   </soap:Body>  
</soap:Envelope>
```