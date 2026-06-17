# Card Apply Fees

API: `Ws_Generic_Fees`

This web service enables you to apply fees with a comment to a particular card.

For more information on the setting up of fees and restrictions which may apply, see the Thredd [Fees Guide](https://docs.thredd.ai/Fees_Guide.htm).

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Unique card identifier. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` and `<track2>` are not present. Mandatory in the response. | Conditional | Mandatory |
| <LocDate> | YYYY-MM-  DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <ProcCode> | AN | 1 | 3 | The transaction fee processing code. See [Processing Codes (fees)](../Reference/Web_Service_Processing_Codes.htm). | Mandatory | Omit |
| <Comment> | AN\*\* | 1 | 50 | If it is blank then this is the default comment associated with the processing code. | Optional | Omit |
| <Fee> | D | 1 | 20 | Fee applied to this card. If it is 0 then will apply the default fee associated with the given processing code otherwise the input value will apply. | Optional | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ItemId> | AN | 1 | 20 | The unique item ID returned for this fee. | Omit | Mandatory |
| <IsPartial> | N | 1 | 1 | Whether a partial fee was taken. 1=true and 0=false. | Omit | Mandatory |
| <WaivedoffAmount> | D | 1 | 20 | Amount of fee that could not be taken. | Omit | Mandatory |
| <TotalAmount> | D | 1 | 20 | Total amount of fee taken. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

\*\* Some formatting may be done on this string, see [String Cleaning and Approved Characters](../Reference/String_Cleaning.htm).

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
      <hyp:Ws_Generic_Fees>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:ProcCode>47</hyp:ProcCode>  
         <hyp:Comment></hyp:Comment>  
         <hyp:LocDate>2021-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:Fee>0.0</hyp:Fee>  
      </hyp:Ws_Generic_Fees>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Generic_FeesResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Generic_FeesResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2021-01-01</SysDate>  
            <PublicToken>123456789</PublicToken>  
            <Fee>1</Fee>  
            <ItemId>1234</ItemId>  
            <IsPartial>false</IsPartial>  
            <WaivedoffAmount>1</WaivedoffAmount>  
            <TotalAmount>1</TotalAmount>  
         </Ws_Generic_FeesResult>  
      </Ws_Generic_FeesResponse>  
   </soap:Body>  
</soap:Envelope>
```