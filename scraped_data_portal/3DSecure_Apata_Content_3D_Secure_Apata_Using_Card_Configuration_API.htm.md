# 15 Using the Card Configuration API

You can use 3D Secure Configuration (`Ws_ApataCardLevelConfigurations`), which is a Thredd Web Service using SOAP to add, update or delete card level configurations for Apata. This web service lets you set configurations such as the language used in the Apata Challenge screens and the Challenge Profile. For more details on this web service, refer to the Thredd [Web Services Guide](https://developer.globalprocessing.com/Web_Services_Guide.htm).

See the example below:

#### Request

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

#### Notes

* **Apata3DSLanguage** â Language to apply to the 3DS challenge screens displayed to the cardholder. [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag) is the language format that is used by Apata, for example, en-EN and fr-FR. The language content must first be set up for your card products. Once this is done, your 3DS Implementation Manager will share with you the language codes to use.
* **ApataChallengeProfileId** â Unique ID configured by Apata to represent the challenge profile (default and fallback challenge options).
* **ApataCardProgramId** â Unique ID configured by Apata to represent the specific card program and associated BIN ranges.
* **ApataKBANumberOfQuestionsToAnswer** â Number of KBA questions to answer correctly across all questions presented to the cardholder.
* **ApataKBANumberOfIncorrectPermissible** â Number of incorrect answers permissible for KBA across all questions presented to the cardholder.
* All Apata fields are optional, but at least one field must be populated. Thredd will respond with action code 441 if all five fields are blank.

For **Apata3DSLanguage**, **ApataChallengeProfileIdand** and **ApataCardProgramId**. If no value is provided, then the field is ignored. If you provide an empty space as a value, then this will delete any existing database values.

For **ApataKBANumberOfQuestionsToAnswer** and **ApataKBANumberOfIncorrectPermissible**. If no value is provided, then the field is ignored. If you provide an empty space as a value, then this will update the database value to 0.

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