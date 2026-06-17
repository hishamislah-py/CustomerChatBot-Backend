# 3D Secure Credentials (Cardinal and Apata)

API: `Ws_AddUpDelCredentials`

This web service enables you to enrol a cardholder in the Cardinal or Apata 3D Secure service and get, add, update and delete the user's credentials.

For more information on implementation of 3D Secure, refer to the *[3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm)* or *[3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm)*.

#### Request Fields

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <Action> | Enum |  |  | The type of action: *Get*, *Add*, *Update*, *Delete*.    Each Action is represented as a numerical value in the SmartClient log:  â¢ Add - 1 â¢ Update - 2 â¢ Delete - 3 â¢ Get - 4 | Mandatory | Mandatory |
| <Credentials> | ListOf Credential objects |  |  | Contains one or more *credential* objects. There can be more than one credential in the same call when `<Action>` is *Get*, *Add* or *Update*.  When `<Action>` is *Delete* and `<Credentials>` is empty then all credentials of `<PublicToken>` are deleted.  When `<Action>` is *Delete* and there are no existing credentials, then [Action Code](../Reference/Action_Codes.htm) 598 is returned. | Conditional | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |
| Credentials | | | | | | |
| <Credential> |  |  |  | If the action is *Add*, you should include the credential *<ID>* of 0 and *<Type>*.  If the action is *Get*, you should include an empty *<hyp:Credentials/>* tag.  If the action is *<Delete>* and you specify the *<ID>* then only that credential will be deleted. |  |  |
| <ID> | N | 1 | 8 | Credential ID. If `<Action>` is *Add* the ID is not mandatory, but input 0 since the data type is numeric. Thredd generates a unique ID and returns it in the response.  ID is mandatory when `<Action>` is *Update*.  ID is not mandatory when `<Action>` is *Delete*, unless a specific credential needs to be deleted. | Conditional | Mandatory |
| <Type> | Enum |  |  | Credential type:  â¢ RBA (done via Cardinal)  â¢ OTPSMS  â¢ OTPEMAIL  â¢ BIOMETRIC  â¢ OUTOFBAND  â¢ KBA    For details, see the [3D Secure FAQs.](../FAQs.htm#3D)  **Note**: OTPEMAIL is only available for the Apata 3DS Service.  **Note**: Discuss with your Implementation Manager before implementing the OUTOFBAND method.  There is no need to enrol cards into RBA; this is automatic once the cards are enrolled at the scheme and can be configured in the Cardinal portal.  **Note**: For a *Get* request - returns the specified type if present, or else returns all types. If no credentials are found for that token then the [action code](../Reference/Action_Codes.htm) 437 is returned.  **Note**: For an *Add* request - adds the specified type. If the credential type already exists, then returns the [action code](../Reference/Action_Codes.htm) 438.  **Note**: For an *Update* request - does not change the type. You cannot edit the credential *type*, only the *value*. | Conditional | Mandatory |
| <Value> | AN | 1 | 256 | Credential value (e.g. a phone number, email address or KBA question ID).  For OTPSMS enter a phone number, for sending the OTP SMS. (For valid phone number formats, see [Processing of Phone Numbers](../Reference/String_Cleaning.htm#Processi)).  For OTPEMAIL enter a valid email address, for sending the OTP email.  **Note**: OTPEMAIL is only available for 3DS Apata. For more information, see the [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm).  For KBA enter the ID to be used as the customer's question choice (e.g., 5). See [KBA Question ID](#KBA).  For BIOMETRIC and OUTOFBAND this field is optional and you can include a reference. The value will not be used. | Conditional | Mandatory |
| <KBA\_Answer> | AN | 1 | 45 | The cardholder's answer to the KBA question (e.g., for `Value`= *5*, `KBA_Answer` = *London*.)  **Note**: Mandatory for an *Add* or *Update* if `Type` is *KBA*. If not provided, returns [action code](../Reference/Action_Codes.htm) 594. | Conditional | Conditional |
| <KBA\_AnswerOldValue> | AN | 1 | 45 | You can use this optional field when changing the saved KBA answer (i.e.,`Action` is *Update* and `Type` is *KBA*) if you want to supply the old answer to check that it matches what is currently held in the Thredd system. If it does not match then no update will happen and Thredd returns the [action code](../Reference/Action_Codes.htm) 599.  If no value is supplied then the update will be done without any comparison. | Optional | Optional |

#### KBA Question ID

If using Knowledge Based Authentication (KBA) , enter one of the IDs below in the `value` field. This identifies which predefined KBA question to use.

| KBA ID | KBA Question |
| --- | --- |
| 1 | What was your first pet's name? |
| 2 | What is your maternal grandmother's maiden name? |
| 3 | What is the name of your favourite childhood friend? |
| 4 | What was the make of your first car? |
| 5 | In what city or town did your mother and father meet? |

### Example Add Request - Biometric

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
      <hyp:Ws_AddUpDelCredentials>  
         <hyp:WSID>14012021141223</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:Action>Add</hyp:Action>  
         <hyp:Credentials>  
            <hyp:Credential>  
               <hyp:ID>0</hyp:ID>  
               <hyp:Type>BIOMETRIC</hyp:Type>  
               <hyp:Value>+5858585858588</hyp:Value>  
               <KBA_Answer></hyp:KBA_Answer>  
               <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
            </hyp:Credential>           
         </hyp:Credentials>   
      </hyp:Ws_AddUpDelCredentials>     
</soapenv:Body></soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"   
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
xmlns:xsd="http://www.w3.org/2001/XMLSchema">     
 <soap:Body>        
  <Ws_AddUpDelCredentialsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">           
   <Ws_AddUpDelCredentialsResult>              
    <WSID>14012021141223</WSID>              
    <IssCode>PMT</IssCode>              
    <ActionCode>000</ActionCode>              
    <PublicToken>123456789</PublicToken>              
    <Action>Add</Action>              
    <Credentials>                 
      <Credential>                    
         <ID>123456</ID>                    
         <Type>BIOMETRIC</Type>                    
         <Value>Customer Biometric app</Value>  
         <KBA_Answer></hyp:KBA_Answer>  
         <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>                
      </Credential>              
   </Credentials>   
   <WebServiceResult/>          
  </Ws_AddUpDelCredentialsResult>        
  </Ws_AddUpDelCredentialsResponse>     
  </soap:Body>  
</soap:Envelope>
```

### Example Get Request

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
      <hyp:Ws_AddUpDelCredentials>  
         <hyp:WSID>15012021151223</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:Action>Get</hyp:Action>  
         <hyp:Credentials/>              
      </hyp:Ws_AddUpDelCredentials>     
</soapenv:Body></soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

Customer Biometric app

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"   
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
xmlns:xsd="http://www.w3.org/2001/XMLSchema">     
 <soap:Body>        
  <Ws_AddUpDelCredentialsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">           
   <Ws_AddUpDelCredentialsResult>              
    <WSID>15012021151223</WSID>              
    <IssCode>PMT</IssCode>              
    <ActionCode>000</ActionCode>              
    <PublicToken>123456789</PublicToken>              
    <Action>Add</Action>              
    <Credentials>                 
      <Credential>                    
         <ID>123456</ID>                    
         <Type>BIOMETRIC</Type>                    
         <Value>Customer Biometric app</Value>  
         <KBA_Answer></hyp:KBA_Answer>  
         <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>                
      </Credential>              
   </Credentials>   
   <WebServiceResult/>          
  </Ws_AddUpDelCredentialsResult>        
  </Ws_AddUpDelCredentialsResponse>     
  </soap:Body>  
</soap:Envelope>
```

### Example Add Request - KBA

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
      <hyp:Ws_AddUpDelCredentials>  
         <hyp:WSID>04012022121223</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:Action>Add</hyp:Action>  
         <hyp:Credentials>  
            <hyp:Credential>  
               <hyp:ID>0</hyp:ID>  
               <hyp:Type>KBA</hyp:Type>  
               <hyp:Value>5</hyp:Value>  
               <KBA_Answer>London</hyp:KBA_Answer>  
               <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
            </hyp:Credential>           
         </hyp:Credentials>   
      </hyp:Ws_AddUpDelCredentials>     
</soapenv:Body></soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"   
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
xmlns:xsd="http://www.w3.org/2001/XMLSchema">     
 <soap:Body>        
  <Ws_AddUpDelCredentialsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">           
   <Ws_AddUpDelCredentialsResult>              
    <WSID>04012022121223</WSID>              
    <IssCode>PMT</IssCode>              
    <ActionCode>000</ActionCode>              
    <PublicToken>123456789</PublicToken>              
    <Action>Add</Action>              
    <Credentials>                 
      <Credential>                    
         <ID>123456</ID>                    
         <Type>KBA</Type>                    
         <Value>5</Value>  
         <KBA_Answer>London</hyp:KBA_Answer>  
         <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>                
      </Credential>              
   </Credentials>         
   <WebServiceResult/>     
  </Ws_AddUpDelCredentialsResult>        
  </Ws_AddUpDelCredentialsResponse>     
  </soap:Body>  
</soap:Envelope>
```