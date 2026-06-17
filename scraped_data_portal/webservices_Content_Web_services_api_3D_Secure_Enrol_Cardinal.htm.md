# 3D Secure Enrol (Cardinal Batch)

API: `Ws_Insert3DSecureDetails`

This web service enables you to enrol a specified cardholder onto 3D Secure using the [Cardinal 3D Secure![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Cardinal Commerce provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme. See: https://www.cardinalcommerce.com](#) service.

This web service uses the Cardinal batch file interface. (Legacy Option)

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <Token> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <MemorableName> | AN | 1 | 20 | The cardholder's specified *Memorable Name* as VDE for 3D Secure.  No longer used - ensure you populate with ânotavailableâ (no spaces) | Mandatory | Omit |
| <MemorablePlace> | AN | 1 | 20 | Cardholder's specified Memorable Place as VDE for 3D Secure.  No longer used. Ensure you populate with ânotavailableâ (no spaces). | Mandatory | Omit |
| <MemorableDate> | YYYY-MM-DD | 10 | 10 | Memorable date as VDE for 3D Secure.  No longer used. Ensure you populate with â1900-01-01â. | Mandatory | Omit |
| <ActivationCode> | AN | 6 | 6 | Programme Manager specified activation code as VDE for 3D Secure.  No longer used. Ensure you populate with ânotavailableâ (no spaces). | Mandatory | Omit |
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
      <hyp:Ws_Insert3DSecureDetails>  
        <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:Token>123456789</hyp:Token>  
         <hyp:MemorableName>notavailable</hyp:MemorableName>  
         <hyp:MemorablePlace>notavailable</hyp:MemorablePlace>  
         <hyp:MemorableDate>1900-01-01</hyp:MemorableDate>  
         <hyp:ActivationCode>notavailable</hyp:ActivationCode>  
         <hyp:Phone>07123456789</hyp:Phone>  
      </hyp:Ws_Insert3DSecureDetails>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Insert3DSecureDetailsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Insert3DSecureDetailsResult>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
         </Ws_Insert3DSecureDetailsResult>  
      </Ws_Insert3DSecureDetailsResponse>  
   </soap:Body>  
</soap:Envelope>
```