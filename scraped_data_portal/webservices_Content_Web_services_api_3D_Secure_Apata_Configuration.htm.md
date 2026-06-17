# 3D Secure Configuration (Apata)

API: `Ws_ApataCardLevelConfigurations`

This web service enables you to add, update or delete card level configurations for Apata, such as the language of the Apata Challenge screens and the Challenge Profile to use.

This service works for Apata products only. For more information on implementation of 3D Secure, refer to the *[3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm)*.

All Apata fields are optional, but at least one field must be populated. Thredd will respond with action code 441 if all five fields are blank.

#### Request Fields

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in the request and response. | Mandatory | Mandatory |
| <Apata3DSLanguage> | AN | 1 | 10 | The language to apply to the 3DS challenge screens displayed to the cardholder. (In [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag) format. For example: *en-EN*,*fr-FR*.)  **Note**: The language content must first be set up for your card products; once this is done, your 3DS Implementation Manager will share with you the language codes to use.  **Note**: Default language is English. If card level value is not provided, then the product level setting will be used.  **Note**: If no value is provided, then this field is ignored. If you provide an empty space as a value, then this will delete any existing database values. | Optional | Optional |
| <ApataChallengeProfileId> | AN | 1 | 255 | Unique ID configured by Apata to represent the challenge profile (default and fallback challenge options).  **Note**: If no value is provided, then this field is ignored. If no value is provided, then this field is ignored. If you provide an empty space as a value, then this will delete any existing database values. | Optional | Optional |
| <ApataCardProgramId> | AN | 1 | 255 | Unique ID configured by Apata to represent the specific card program and associated BIN ranges.  **Note**: If no value is provided, then this field is ignored. If no value is provided, then this field is ignored. If you provide an empty space as a value, then this will delete any existing database values. | Optional | Optional |
| <ApataKBANumberOf QuestionsToAnswer> | N | 8 | 8 | Number of KBA questions to answer correctly across all questions presented to the cardholder.  **Note** If no value is provided, then this field is ignored. If you provide an empty space as a value, then this will update the database value to 0. | Optional | Optional |
| <ApataKBANumberOf IncorrectPermissible> | N | 8 | 8 | Number of incorrect answers permissible for KBA across all questions presented to the cardholder.  **Note**: If no value is provided, then this field is ignored.If you provide an empty space as a value, then this will update the database value to 0. | Optional | Optional |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

### Example Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
<soapenv:Header>  
<hyp:AuthSoapHeader>  
<!--Optional:-->  
<hyp:strUserName>*****</hyp:strUserName>  
<!--Optional:-->  
<hyp:strPassword>**********</hyp:strPassword>  
</hyp:AuthSoapHeader>  
</soapenv:Header>  
<soapenv:Body>  
<hyp:Ws_ApataCardLevelConfigurations>  
<hyp:WSID>15012024123478</hyp:WSID>  
<!--Optional:-->  
<hyp:IssCode>PMT</hyp:IssCode>  
<!--Optional:-->  
<hyp:PAN></hyp:PAN>  
<!--Optional:-->  
<hyp:PublicToken>123456754</hyp:PublicToken>  
<!--Optional:-->  
<hyp:Apata3DSLanguage>en-EN</hyp:Apata3DSLanguage>  
<!--Optional:-->  
<hyp:ApataChallengeProfileId>123ab-4fdfd443-43434f352</hyp:ApataChallengeProfileId>  
<!--Optional:-->  
<hyp:ApataCardProgramId>5456</hyp:ApataCardProgramId>  
<!--Optional:-->  
<hyp:ApataKBANumberOfQuestionsToAnswer>10</hyp:ApataKBANumberOfQuestionsToAnswer>  
 <!--Optional:-->  
 <hyp:ApataKBANumberOfIncorrectPermissible>10</hyp:ApataKBANumberOfIncorrectPermissible>  
</hyp:Ws_ApataCardLevelConfigurations>  
</soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_ApataCardLevelConfigurationsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_ApataCardLevelConfigurationsResult>  
            <WSID>15012024123478</WSID>  
            <IssCode>PMT</IssCode>  
            <PublicToken>123456754</PublicToken>  
            <ActionCode>000</ActionCode>  
            <Apata3DSLanguage>en-EN</Apata3DSLanguage>  
            <ApataChallengeProfileId>123ab-4fdfd443-43434f352</ApataChallengeProfileId>  
            <ApataCardProgramId>5456</ApataCardProgramId>  
            <ApataKBANumberOfQuestionsToAnswer>10</ApataKBANumberOfQuestionsToAnswer>  
            <ApataKBANumberOfIncorrectPermissible>10</ApataKBANumberOfIncorrectPermissible>   
         </Ws_ApataCardLevelConfigurationsResult>  
      </Ws_ApataCardLevelConfigurationsResponse>  
   </soap:Body>  
</soap:Envelope>
```