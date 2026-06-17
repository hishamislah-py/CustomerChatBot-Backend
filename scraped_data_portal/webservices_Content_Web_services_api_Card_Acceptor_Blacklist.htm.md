# Card Acceptor Deny List

API: `Ws_CardAcceptorBlacklist`

This web service enables you to manage Card Acceptor (MerchantID) *Deny* lists, which can then be assigned to a card or group of cards. Any merchant IDs in the disallow will see transactions declined by Thredd at the authorisation stage. The response code will be â*05 â Do not honour*â.

If the card does not have the disallow group assigned, this will need to be added via `Ws_Card_Change_Cardacceptor_List` or `Ws_Change_Cardacceptor_List`. See [Card Change Acceptor List](Card_Change_Acceptor_List.htm) and [Card Change Acceptor List (Bulk)](Card_Change_Acceptor List_1.htm).

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <BlackList> | AN | 1 | 255 | Identifier for a Card Acceptor Deny list in Thredd. | Mandatory | Mandatory |
| <CardAcceptors> | - | - | - | Provides a list of `CardAcceptorModifier` elements; see [CardAcceptorModifier Description](#Card) below. If the list is empty, the web service returns a list of all the `CardAcceptorModifier` elements in the Deny list. | Mandatory | Omit |
| <SysDate> | AN | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <NoOfInvalidCardAcceptors> | N | 1 | 9 | Number of invalid *CardAcceptorModifier* elements detected. Check the `<ActionCode>` of each one to see the reason for the rejection. | Omit | Mandatory |
| <InvalidCardAcceptors> | - | - | - | See [Invalid Card Acceptor Description](#Invalid) below. Provides a list of `InvalidCardAcceptor` elements. | Omit | Mandatory |

#### CardAcceptorModifier Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <CardAcceptorID> | AN | 1 | 50 | Card Acceptor ID. Also known as Merchant ID (DE 42). | Mandatory | N/A |
| <Action> | N | 1 | 9 | Action Code:  0 = Delete Card Acceptor ID  1 = Insert Card Acceptor ID | Mandatory | N/A |

#### Invalid CardAcceptorModifier Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <AcceptorNo> | N | 1 | 9 | Unique, sequential identifier for the entry in the list. | N/A | Mandatory |
| <CardAcceptorID> | AN | 1 | 50 | Card Acceptor ID. Also known as Merchant ID (DE 42). | N/A | Mandatory |
| <ErrorCode> | AN | 3 | 4 | Action Code for this Card Acceptor ID:  781 = CardAcceptorId is empty  782 = Invalid Action (parameter value was invalid)  783 = CardAcceptorID not found (valid when Action = 0)  799 = CardAcceptorID already exists | N/A | Mandatory |
| ErrorDescription | AN | 1 | 255 | Description of the error. | N/A | Mandatory |

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
   <soap:Body>  
      <hyp:Ws_CardAcceptorBlackList>  
         <hyp:WSID>202107150820</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:BlackList>BL1</hyp:BlackList>   
         <hyp:CardAcceptors>  
            <!--Zero or more repetitions:-->    
            <hyp:CardAcceptorModifier>  
               <hyp:CardAcceptorID>123456789</hyp:CardAcceptorID>  
               <hyp:Action>1</hyp:Action>  
            </hyp:CardAcceptorModifier>  
         </hyp:CardAcceptors>  
      </hyp:Ws_CardAcceptorBlackList>  
   </soap:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CardAcceptorBlackListResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CardAcceptorBlackListResult>  
            <WSID>201507150820</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <SysDate>2021-07-15</SysDate>  
            <BlackList>BL1</BlackList>  
            <NoOfInvalidCardAcceptors>1</NoOfInvalidCardAcceptors>  
            <InvalidCardAcceptors>  
               <InvalidCardAcceptor>  
                  <AcceptorNo>1</AcceptorNo>  
                  <CardAcceptorID>123456789</CardAcceptorID>  
                  <ErrorCode>799</ErrorCode>  
                  <ErrorDescription>This card acceptor is already added to the Deny list of the given scheme</ErrorDescription>  
               </InvalidCardAcceptor>  
            </InvalidCardAcceptors>  
         </Ws_CardAcceptorBlackListResult>  
      </Ws_CardAcceptorBlackListResponse>  
   </soap:Body>  
</soap:Envelope>
```