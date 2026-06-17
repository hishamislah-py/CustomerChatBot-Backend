# 3D Secure Update Details (Cardinal Batch)

API: `Ws_Update3DSecureDetails`

This web service enables you to amend the 3D secure phone number for sending the 3D Secure verification code for a given card.

This web service uses the Cardinal batch file interface. (Legacy Option)

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <Token> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <MemorableName> | AN | 1 | 20 | The cardholder's specified *Memorable Name* to be used as [VDEClosed Virtual Data Element, used for 3D Secure identification. Examples are memorable name, memorable place and memorable date.](#) for 3D Secure.  No longer used. Ensure you opulate with ânotavailableâ (no spaces) | Conditional | Omit |
| <MemorablePlace> | AN | 1 | 20 | Cardholder's specified Memorable Place to be used as VDE for 3D Secure.  No longer used. Ensure you populate with ânotavailableâ (no spaces). | Conditional | Omit |
| <MemorableDate> | YYYY-MM-DD | 10 | 10 | Memorable date to be used as VDE for 3D Secure.  No longer used. Ensure you populate with â1900-01-01â | Conditional | Omit |
| <ActivationCode> | AN | 6 | 6 | Programme Manager specified activation code to be used as VDE for 3D Secure.  No longer used. Ensure you populate with ânotavailableâ (no spaces) | Conditional | Omit |
| <Phone> | AN | 1 | 20 | Telephone number. See [Processing of Phone Numbers](../Reference/String_Cleaning.htm#Processi). | Conditional | Omit |
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
      <hyp:Ws_Update3DSecureDetails>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:Token>123456789</hyp:Token>  
         <hyp:MemorableName>notavailable</hyp:MemorableName>  
         <hyp:MemorablePlace>notavailable</hyp:MemorablePlace>  
         <hyp:MemorableDate>1900-01-01</hyp:MemorableDate>  
         <hyp:ActivationCode>notavailable</hyp:ActivationCode>  
         <hyp:Phone></hyp:Phone>  
      </hyp:Ws_Update3DSecureDetails>  
   </soapenv:Body>  
</soapenv:Envelope>  
 
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Update3DSecureDetailsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Update3DSecureDetailsResult>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
         </Ws_Update3DSecureDetailsResult>  
      </Ws_Update3DSecureDetailsResponse>  
   </soap:Body>  
</soap:Envelope>  
```