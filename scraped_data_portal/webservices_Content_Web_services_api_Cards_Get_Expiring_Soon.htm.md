# Cards Get Expiring Soon

API: `Ws_Get_Card_ExpireSoon`

This web service returns the details of cards that are going to expire before the end of the current month. The response returns all cards due to expire, regardless of the volume.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <cardList> | - | - | - | An array of `Card_Details`. See [Card\_Details](#Card) below. Can occur multiple times within the message. |  |  |

#### Card\_Details

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <Scheme> | AN | 1 | 50 | Scheme name. | Omit | Mandatory |
| <Product> | AN | 1 | 50 | Name of the product. | Omit | Mandatory |
| <PublicToken> | N | 16 | 19 | Cardâs public token. | Omit | Mandatory |
| <Emboss\_Name> | AN | 1 | 51 | Name embossed on the card. | Omit | Mandatory |
| <ExpiryDate> | YYYY-MM-DD | 10 | 10 | Expiry date of the card in *YYYY-MM-DD* format. | Omit | Mandatory |
| <IsLive> | N | 1 | 1 | Indicates whether the card is active:  1 = Active; 0 = Not Active | Omit | Mandatory |
| <ActivationDate> | YYYY-MM-DD | 10 | 10 | Activation date of the card. | Omit | Mandatory |
| <AvlBal> | D | 1 | 20 | The current balance on the card account. This includes all financial transactions and outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <BlkAmt> | D | 1 | 20 | Amount of funds blocked on the card account as a result of all outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <CurCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the account billing currency. | Omit | Mandatory |

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
      <hyp:Ws_Get_Card_ExpireSoon>  
         <hyp:WSID>20211234567896</hyp:WSID>   
         <hyp:IssCode>PMT</hyp:IssCode>  
      </hyp:Ws_Get_Card_ExpireSoon>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Get_Card_ExpireSoonResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Get_Card_ExpireSoonResult>  
            <WSID>20211234567896</WSID>  
            <IssCode>PMT</IssCode>  
            <SysDate>2021-10-22</SysDate>  
            <ActionCode>000</ActionCode>  
            <cardList>  
               <Card_Details>  
                  <Scheme>ABCD</Scheme>  
                  <Product>XYZ</Product>  
                  <PublicToken>123456789</PublicToken>  
                  <Emboss_Name>FIRSTNAME LASTNAME</Emboss_Name>  
                  <ExpiryDate>2021-11-12</ExpiryDate>  
                  <IsLive>true</IsLive>  
                  <ActivationDate>2020-11-12</ActivationDate>  
                  <AvlBal>2206</AvlBal>  
                  <BlkAmt>0.00</BlkAmt>  
                  <CurCode>GBP</CurCode>  
               </Card_Details>  
               <Card_Details>  
                  <Scheme>ABCD</Scheme>  
                  <Product>ASDF</Product>  
                  <PublicToken>789456123</PublicToken>  
                  <Emboss_Name>FIRSTNAME LASTNAME</Emboss_Name>  
                  <ExpiryDate>2021-11-15</ExpiryDate>  
                  <IsLive>true</IsLive>  
                  <ActivationDate>2020-01-08</ActivationDate>  
                  <AvlBal>0</AvlBal>  
                  <BlkAmt>0.00</BlkAmt>  
                  <CurCode>GBP</CurCode>  
               </Card_Details>            </cardList>  
         </Ws_Get_Card_ExpireSoonResult>  
      </Ws_Get_Card_ExpireSoonResponse>  
   </soap:Body>  
</soap:Envelope>
```