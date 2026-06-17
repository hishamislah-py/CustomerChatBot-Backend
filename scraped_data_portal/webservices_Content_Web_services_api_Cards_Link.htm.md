# Cards Link

API: `Ws_link_cards`

This web service enables you to link cards in a Primary and Secondary relationship, which is useful when the primary card with existing secondary card linkage(s) needs to be replaced with a new token. You can link secondary cards to the new token via this web service. More than one secondary card can be linked to a primary card.

#### Notes

* The billing currency of the cards you want to link must be the same.
* If the supplied PAN or PublicToken belongs to a primary card with no secondary cards then it is linked as a new secondary card of the card specified by NewPAN or NewToken.
* If the supplied PAN or PublicToken belongs to a secondary card, then the primary card of that secondary card is changed to the card identified by NewPAN/NewToken.
* If the supplied PAN or PublicToken belongs to a card with one or more secondary cards, then the primary card of each of those secondary cards is changed to NewPAN/NewToken.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | The account number of the card you want to link to another card. Mandatory in request if `<PublicToken>` is not provided. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The public token of the card you want to link to another card. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <NewPAN> | AN | 16 | 19 | The account number of the card you want to link to. Mandatory in the request if `<newToken>` is not present. | Conditional | Omit |
| <NewToken> | AN | 16 | 19 | The public token of the card you want to link to. Mandatory in the request if `<NewPAN>` is not present. | Conditional | Mandatory |
| <LinkageGroup> | AN | 1 | 10 | [Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#) to use for linking the two tokens. If not specified, uses the default Linkage Group. | Conditional | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <NewPublicToken> | AN | 1 | 9 | New public token assigned to the linked cards. | Omit | Mandatory |
| <SecondaryCards> | - | - | - | An array of secondary cards. See [Secondary Card](#Secondar) below. Can occur multiple times within the message. | Omit | Mandatory |

#### Secondary Card

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PublicToken> | AN | 1 | 9 | Public token of the secondary card. | Omit | Mandatory |

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
      <hyp:Ws_Link_Cards>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:NewPAN></hyp:NewPAN>  
         <hyp:NewToken>987654321</hyp:NewToken>  
      </hyp:Ws_Link_Cards>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Link_CardsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Link_CardsResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <PublicToken>123456789</PublicToken>  
            <NewPublicToken>987654321</NewPublicToken>  
            <ActionCode>000</ActionCode>  
            <SecondaryCards>  
               <SecondaryCard>  
                  <PublicToken>792710863</PublicToken>  
               </SecondaryCard>  
               <SecondaryCard>  
                  <PublicToken>506904572</PublicToken>  
               </SecondaryCard>  
               <SecondaryCard>  
                  <PublicToken>422232038</PublicToken>  
               </SecondaryCard>  
               <SecondaryCard>  
                  <PublicToken>546808888</PublicToken>  
               </SecondaryCard>  
               <SecondaryCard>  
                  <PublicToken>838454145</PublicToken>  
               </SecondaryCard>  
               <SecondaryCard>  
                  <PublicToken>590228767</PublicToken>  
               </SecondaryCard>  
            </SecondaryCards>  
         </Ws_Link_CardsResult>  
      </Ws_Link_CardsResponse>  
   </soap:Body>  
</soap:Envelope>
```