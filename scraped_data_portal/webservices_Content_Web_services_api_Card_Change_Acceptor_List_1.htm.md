# Card Change Acceptor List (Bulk)

API: `Ws_Change_Cardacceptor_List`

This web service is used to modify acceptor lists, such as the Allow lists and Deny lists that a group of cards belong to. This determines the list of merchants at which the cards can be used.

The acceptance of a card can be subject to either a Allow list or a Deny list, not both.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardDesc> | - | - | - | See [CARD Description](#CARD) below. | Omit | Mandatory |
| <CardSelector> | N | 1 | 2 | Card Selector type:  1 = Product ID; 2 = Customer account number;  3 = To be confirmed | Mandatory | Mandatory |
| <CardSelectorValue> | AN | 1 | 30 | Card Selector value.  If `<Card Selector>` is 1 then this is a product ID (e.g. 12345). If `<Card Selector>` is 2 then this is a customer account number (e.g. 008480510001), and wildcards are supported in the Card Selector value (e.g. â0084505\*â). | Mandatory | Mandatory |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <BlackList> | AN | 1 | 10 | Group code of the card acceptor Deny list. See [Card Acceptor Deny list.](Card_Acceptor_Blacklist.htm) | Optional | Omit |
| <WhiteList> | AN | 1 | 10 | Group code of the card acceptor Allow list. See [Card Acceptor Allow list](Card_Acceptor_Whitelist.htm). | Optional | Omit |
| <CurrentBlackList> | AN | 1 | 10 | Group code of the Deny list to further select cards. If specified, then only the cards within the Card Selector value that belong to this group are migrated to the new group. If not specified, all cards within the Card Selector value are moved. | Optional | Omit |
| <CurrentWhiteList> | AN | 1 | 10 | Group code of the Allow list to further select cards. If specified, then only the cards within the Card Selector value that belong to this group are migrated to the new group. If not specified, all cards within the Card Selector value are moved. | Optional | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

#### CARD Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in the response. | Omit | Mandatory |
| <CurrentBlackList> | AN | 1 | 10 | Group code of the Deny list to further select cards. If specified, then only the cards within the Card Selector value that belong to this group are migrated to the new group. If not specified, all cards within the Card Selector value are moved. | Omit | Mandatory |
| <CurrentWhiteList> | AN | 1 | 10 | Group code of the Allow list to further select cards. If specified, then only the cards within the Card Selector value that belong to this group are migrated to the new group. If not specified, all cards within the Card Selector value are moved. | Omit | Mandatory |

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
      <hyp:Ws_Change_Cardacceptor_List>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:CardSelector>1</hyp:CardSelector>  
         <hyp:CardSelectorValue>123</hyp:CardSelectorValue>  
         <hyp:LocDate>2021-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:BlackList>XYZ</hyp:BlackList>  
   
         <hyp:WhiteList></hyp:WhiteList>  
   
         <hyp:CurrentBlackList>ABCD</hyp:CurrentBlackList>  
   
         <hyp:CurrentWhiteList></hyp:CurrentWhiteList>  
      </hyp:Ws_Change_Cardacceptor_List>  
      </hyp:Ws_Change_Groups>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Change_Cardacceptor_ListResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Change_Cardacceptor_ListResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <CardSelector>1</CardSelector>  
            <CardSelectorValue>123</CardSelectorValue>  
            <ActionCode>000</ActionCode>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2021-01-01</SysDate>  
            <CardsAccepter>  
               <CardAccepterList>  
                  <PublicToken>123456789</PublicToken>  
                  <CurrentBlackList>XYZ</CurrentBlackList>  
                  <CurrentWhiteList/>  
               </CardAccepterList>  
               <CardAccepterList>  
                  <PublicToken>223456789</PublicToken>  
                  <CurrentBlackList>XYZ</CurrentBlackList>  
                  <CurrentWhiteList/>  
               </CardAccepterList>  
            </CardsAccepter>  
         </Ws_Change_Cardacceptor_ListResult>  
      </Ws_Change_Cardacceptor_ListResponse>  
   </soap:Body>  
</soap:Envelope>  
 
```