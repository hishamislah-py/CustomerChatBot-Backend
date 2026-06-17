# 14 Using the Card Enrolment API

You can use either the Thredd API or the Cards API to enrol your cards in 3D Secure.

## 14.1 Using Cards API

If you are using our Cards API, you can enrol your cards in 3D Secure and register your cards for different authentication types (e.g., OTP SMS, KBA and Biometric) using the 3D Secure API endpoints. This is a REST-based API, which requires sending your request in JSON format. For more information, see the [Cards API Website > Managing 3D Secure Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials).

## 14.2 Using the Thredd API

If you are using our Thredd API, you can enrol your cards in 3D Secure and register the card for different authentication types (e.g., OTP SMS, KBA and Biometric), use the 3D Secure (`Ws_AddUpDelCredentials`) Thredd API. This is a SOAP-based web service, which requires sending your request as an XML message. This web service is described in detail in the [Web Services Guide (SOAP)](https://developer.globalprocessing.com/Web_Services_Guide.htm).

See the example below:

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">     
<soapenv:Header>        
   <hyp:AuthSoapHeader>                    
         <hyp:strUserName>*******</hyp:strUserName>  
         <hyp:strPassword>*******</hyp:strPassword>  
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
                        <hyp:Value> Customer App Biometric </hyp:Value>  
            </hyp:Credential>           
         </hyp:Credentials>   
      </hyp:Ws_AddUpDelCredentials>     
</soapenv:Body></soapenv:Envelope>
```

#### Notes

Thredd token of the card to enrol in 3D Secure:

> [Copy](javascript:void(0);)
>
> ```
>          <hyp:PublicToken>123456789</hyp:PublicToken>
> ```

To enrol the card and add an authentication type, use the **Add** Action:

> [Copy](javascript:void(0);)
>
> ```
>          <hyp:Action>Add</hyp:Action>
> ```

Specify the credentials to add to the card. In this example BIOMETRIC is specified. This will be used together with the phone number set up for the card, for 3D secure SMS **OTP** messages:

> [Copy](javascript:void(0);)
>
> ```
>             <hyp:Credential>  
>                <hyp:ID>0</hyp:ID>  
>                <hyp:Type>BIOMETRIC</hyp:Type>  
>                         <hyp:Value> Customer App Biometric </hyp:Value>  
>             </hyp:Credential>
> ```

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
          <Value>Customer App Biometric</Value>    
          <KBA_Answer></hyp:KBA_Answer>  
          <KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>              
      </Credential>              
   </Credentials>           
  </Ws_AddUpDelCredentialsResult>        
  </Ws_AddUpDelCredentialsResponse>     
  </soap:Body>  
</soap:Envelope>
```

#### Notes

* Your card sub-BIN/BIN range must be set up for 3D Secure before you can use this web service.
* If you want to register the card for more than one authentication type in the same request, you can specify an array of credentials; see [Q. How do I add multiple authentication types to a card?](../FAQs.htm#_Q._How_do)
* When registering the BIOMETRIC type, the `<Value>` parameter is for your reference only and is not used by Thredd or Cardinal.
* When registering the KBA type, the `<Value>` parameter is the ID of the question to use and `<KBA_Answer>` is the answer for Thredd to store[1  Answers are stored in hash-encoded format in the Thredd database. Answers are case-sensitive; for example, âLondonâ would be hash-encrypted differently from âlondonâ or âLONDONâ.](#). For more information, see [Appendix 4: KBA Questions](../Reference/KBA_Questions.htm#_Appendix_5:_KBA).
* For details of the types supported, see [Supported Authentication Types](Additional_3D_Secure_Considerations.htm#_Supported_Authentication_Types).
* You can use the same web service to add, update and delete credentials. You can use the `Get` function to return a list of credentials linked to a card.

## 14.3 Card Renewals and Credential Auto-enrolment

When an existing card is about to expire, you can renew the card using either the Card Renew (`Ws_Renew_Card`) Thredd API (see the [Web Services Guide (SOAP) > Card Renew](https://developer.globalprocessing.com/webservices/Content/Web_services_api/Card_Renew.htm)), or the [Card Renew](https://cardsapidocs.thredd.com/docs/card-renewal-and-replacement) Cards API endpoint.

Renewing the card may result in a new card being created, with a new PAN, Expiry Date and CVV. In this case, if old card has already been enrolled with 3D Secure credentials, then, the new replacement card is automatically enrolled with the same 3D Secure credentials as the old card.