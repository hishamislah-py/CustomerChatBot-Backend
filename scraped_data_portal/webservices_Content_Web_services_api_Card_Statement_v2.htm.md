# Card Statement (V2)

API: `Ws_Banking_Card_Statement_V2`

This web service is an enhancement to `Ws_Card_Statement` (see [Card Statement (V1)](Card_Statement_v1.htm)) and returns all statement details for this card, as well as for previous cards if the card has been replaced.

#### Request Description

The details for the request are identical to those in [Card Statement (V1](Card_Statement_v1.htm)): `Ws_Card_Statement`.

`Ws_Banking_Card_Statement_V2` excludes card status change entries prior to 2022. Card status changes before this year are no longer retrievable. If you want to retrieve card status changes prior to 2022, raise a ticket with Thredd and a member of the App Support team will deal with your request.

Thredd recommend you start with a simple check of the status of the web service to make sure you can connect, using `Ws_Check`. See [Check Service Availability](Check_Service_Availability.htm).

#### Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). |  | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. |  | Optional |
| <Statements > | List (`CardStatement2`  ) |  |  | A list of card statements. Each statement gives details of the card's associated statements. For details, see [Card Statement (V1)](Card_Statement_v1.htm). |  |  |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>*****</hyp:strUserName>  
         <hyp:strPassword>*****</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_Banking_Card_Statement_V2>  
         <hyp:request>  
            <hyp:WSID>1234465</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:TxnCode>5</hyp:TxnCode>  
            <hyp:ClientCode></hyp:ClientCode>  
            <hyp:ItemSrc>2</hyp:ItemSrc>  
            <hyp:AuthType>1</hyp:AuthType>  
            <hyp:PAN></hyp:PAN>  
            <hyp:Track2></hyp:Track2>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
            <hyp:DOB></hyp:DOB>  
            <hyp:CVV></hyp:CVV>  
            <hyp:AccCode></hyp:AccCode>  
            <hyp:LastName></hyp:LastName>  
            <hyp:LocDate>2021-01-01</hyp:LocDate>  
            <hyp:LocTime>120000</hyp:LocTime>  
            <hyp:TerminalID></hyp:TerminalID>  
            <hyp:TxnFilter>5</hyp:TxnFilter>  
            <hyp:StartDate></hyp:StartDate>  
            <hyp:EndDate></hyp:EndDate>  
            <hyp:NumTxn>0</hyp:NumTxn>  
            <hyp:DataSrc>0</hyp:DataSrc>  
            <hyp:DescriptionDelimiter>,</hyp:DescriptionDelimiter>  
         </hyp:request>  
      </hyp:Ws_Banking_Card_Statement_V2>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
  <soap:Body>  
    <Ws_Banking_Card_Statement_V2Response xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <Ws_Banking_Card_Statement_V2Result>  
        <WSID>1234</WSID>  
        <ActionCode>string</ActionCode>  
        <ErrorText>string</ErrorText>  
        <Statements>  
          <CardStatement2>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>5</TxnCode>  
            <ClientCode></ClientCode>  
            <PublicToken>123456789</PublicToken>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <StartBal>10</StartBal>  
            <EndBal>0</EndBal>  
            <TxnFilter>5</TxnFilter>  
            <StartDate></StartDate>  
            <EndDate></EndDate>  
            <NumTxn>2</NumTxn>  
            <ItemSrc>2</ItemSrc>  
            <CurBill>GBP</CurBill>  
            <AvlBal>0</AvlBal>  
            <BlkAmt>0</BlkAmt>  
            <SysDate>2021-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <Transactions xsi:nil="true" />  
          </CardStatement2>  
          <CardStatement2>  
            <WSID>20211234567896</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>5</TxnCode>  
            <ClientCode></ClientCode>  
            <PublicToken>234456789</PublicToken>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <StartBal>10</StartBal>  
            <EndBal>0</EndBal>  
            <TxnFilter>5</TxnFilter>  
            <StartDate></StartDate>  
            <EndDate></EndDate>  
            <NumTxn>2</NumTxn>  
            <ItemSrc>2</ItemSrc>  
            <CurBill>GBP</CurBill>  
            <AvlBal>0</AvlBal>  
            <BlkAmt>0</BlkAmt>  
            <SysDate>2021-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <Transactions xsi:nil="true" />  
          </CardStatement2>  
        </Statements>  
      </Ws_Banking_Card_Statement_V2Result>  
    </Ws_Banking_Card_Statement_V2Response>  
  </soap:Body>  
</soap:Envelope> 
```