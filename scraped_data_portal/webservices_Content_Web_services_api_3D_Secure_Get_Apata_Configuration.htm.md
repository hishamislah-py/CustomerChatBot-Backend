# 3D Secure Get Card Level Configuration (Apata)

API: `Ws_GetApataCardLevelConfigurations`

This web service retrieves the card level configuration for Apata.

This service works for Apata products only. For more information on implementation of 3D Secure, refer to the *[3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm)*.

#### Request Fields

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in the request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <Apata3DSLanguage> | AN | 1 | 10 | The language to apply to the 3DS challenge screens displayed to the cardholder. (In [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag) format. For example: *en-EN*,*fr-FR*.) | Omit | Optional |
| <ApataChallengeProfileId> | AN | 1 | 255 | Unique ID configured by Apata to represent the challenge profile (default and fallback challenge options). | Omit | Optional |
| <ApataCardProgramId> | AN | 1 | 255 | Unique ID configured by Apata to represent the specific card program and associated BIN ranges. | Omit | Optional |
| <ApataKBANumberOf QuestionsToAnswer> | N | 8 | 8 | Number of KBA questions to answer correctly across all questions presented to the cardholder. | Omit | Optional |
| <ApataKBANumberOf IncorrectPermissible> | N | 8 | 8 | Number of incorrect answers permissible for KBA across all questions presented to the cardholder. | Omit | Optional |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

### Example Request

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