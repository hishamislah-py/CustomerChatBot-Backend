# Return Card Enabled Option

API: `Ws_Banking_StatusQueryBankingEnabledCard`

This web service returns the Agency Banking features (UK Bank Accounts provided through programmes using Agency Banking) that are enabled on a card and the status of the card.

#### Record Request Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. | Mandatory | Mandatory |

#### Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| ActionCode | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). |  | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. |  | Optional |
| <AccountStatus> | AccountStatus |  |  | See [AccountStatus](../Reference/Enums.htm#AccountS). |  | Mandatory |

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
      <hyp:Ws_Banking_StatusQueryBankingEnabledCard>  
         <hyp:request>  
            <hyp:WSID>3747547575447</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
         </hyp:request>  
      </hyp:Ws_Banking_StatusQueryBankingEnabledCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_StatusQueryBankingEnabledCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_StatusQueryBankingEnabledCardResult>  
            <WSID>3747547575447</WSID>  
           <ErrorText></ErrorText>  
            <ActionCode>000</ActionCode>  
            <AccountStatus>  
               <AccountStatus>Open</AccountStatus>  
               <BankingInEnabled>Disabled</BankingInEnabled>  
               <BankingOutEnabled>Disabled</BankingOutEnabled>  
               <DirectDebitInEnabled>Disabled</DirectDebitInEnabled>  
               <DirectDebitOutEnabled>Disabled</DirectDebitOutEnabled>  
               <CardEnabled>Enabled</CardEnabled>  
            </AccountStatus>  
         </Ws_Banking_StatusQueryBankingEnabledCardResult>  
      </Ws_Banking_StatusQueryBankingEnabledCardResponse>  
   </soap:Body>  
</soap:Envelope>
```