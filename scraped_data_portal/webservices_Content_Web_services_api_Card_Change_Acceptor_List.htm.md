# Card Change Acceptor List

API: `Ws_Card_Change_Cardacceptor_List`

This web service modifies the card acceptor (MerchantID) lists (such as Allow lists and Deny lists) that a card makes use of. You use a list to modify a single card. This determines the list of merchants at which the card can be used.

The acceptance of a card can be subject to an Allow list or a Deny list, not both.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. | Optional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <BlackList> | AN | 1 | 10 | Group code of the card acceptor Deny list. See [Card Acceptor Deny list.](Card_Acceptor_Blacklist.htm) | Optional | Omit |
| <WhiteList> | AN | 1 | 10 | Group code of the card acceptor Allow list. See [Card Acceptor Allow list](Card_Acceptor_Whitelist.htm). | Optional | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |

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
      <hyp:Ws_Card_Change_Cardacceptor_List>  
         <hyp:WSID>1234</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:LocDate>2021-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:BlackList>ABCD</hyp:BlackList>  
         <hyp:WhiteList>XYZ</hyp:WhiteList>        
      </hyp:Ws_Card_Change_Cardacceptor_List>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Card_Change_Cardacceptor_ListResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Card_Change_Cardacceptor_ListResult>  
            <WSID>20211234567896</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>10000</LocTime>  
            <SysDate>2021-01-01</SysDate>  
            <PublicToken/>  
            <WebServiceResult/>   
         </Ws_Card_Change_Cardacceptor_ListResult>           
      </Ws_Card_Change_Cardacceptor_ListResponse>  
   </soap:Body>  
</soap:Envelope>
```