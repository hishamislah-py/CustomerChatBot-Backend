# 16 Using the Get Card Level Configuration API

You can use 3D Secure Get Card Level Configuration (`Ws_GetApataCardLevelConfigurations`), which is a Thredd Web Service using SOAP, to retrieve the card level configurations for Apata. For more details on this web service, refer to the Thredd [Web Services Guide](https://developer.globalprocessing.com/Web_Services_Guide.htm).

See the example below:

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <!--Optional:-->  
         <hyp:strUserName>***************</hyp:strUserName>  
         <!--Optional:-->  
         <hyp:strPassword>***********</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_GetApataCardLevelConfigurations>  
         <hyp:WSID>2502320253543353</hyp:WSID>  
         <!--Optional:-->  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <!--Optional:-->  
         <hyp:PAN></hyp:PAN>  
         <!--Optional:-->  
         <hyp:PublicToken>123090776</hyp:PublicToken>  
      </hyp:Ws_GetApataCardLevelConfigurations>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_GetApataCardLevelConfigurationsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_GetApataCardLevelConfigurationsResult>  
            <WSID>730744995595027456</WSID>  
            <PublicToken>123090776</PublicToken>  
            <Apata3DSLanguage>en-EN</Apata3DSLanguage>  
            <ApataChallengeProfileId>ProfileId</ApataChallengeProfileId>  
            <ApataCardProgramId>ProgramId</ApataCardProgramId>  
            <ApataKBANumberOfQuestionsToAnswer>10</ApataKBANumberOfQuestionsToAnswer>  
            <ApataKBANumberOfIncorrectPermissible>5</ApataKBANumberOfIncorrectPermissible>  
            <ActionCode>000</ActionCode>  
         </Ws_GetApataCardLevelConfigurationsResult>  
      </Ws_GetApataCardLevelConfigurationsResponse>  
   </soap:Body>  
</soap:Envelope>
```