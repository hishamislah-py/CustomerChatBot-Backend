# Cancel Direct Bank Mandate

API: `Ws_Banking_DD_CancelMandate`

This Web service cancels a specific mandate for a mandateId and token.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardDesign> | AN | 1 | 8 | The Thredd `Product ID`. For details, check with your Implementation Manager. | Mandatory | Omit |
| <Token> | N | 1 | 9 | The 9 digit public token associated with the account. | Mandatory | Omit |
| <MandateId> | AN |  |  | The mandateId related to the direct debit mandate. | Mandatory | Omit |
| <MerchantNumber> | AN |  |  | The merchant number. | Optional | Omit |
| <CancellationCode> | AN | ENUM |  | The cancellation code for the direct debit mandate. | Mandatory | Omit |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Messages> | A list of BankingError |  |  | Displays details of the error message. See [BankingError.](../Reference/Enums.htm#BankingE2) | Omit | Optional |

#### Request

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
<soap:Header>  
     <AuthSoapHeader xmlns="http://www.globalprocessing.ae/HyperionWeb">  
           <strUserName>string</strUserName>  
           <strPassword>string</strPassword>  
     </AuthSoapHeader>  
</soap:Header>  
<soap:Body>  
       <Ws_Banking_DD_CancelMandate xmlns="http://www.globalprocessing.ae/HyperionWeb">  
               <request>  
                      <WSID>string</WSID>  
                      <IssCode>string</IssCode>  
                      <CardDesign>string</CardDesign>  
                      <Token>PUBTOKEN/PANPUBT</Token>  
                      <MandateId>string</MandateId>  
                      <MerchantNumber>string</MerchantNumber>  
                      <CancellationCode>string</CancellationCode>  
            </request>  
         </Ws_Banking_DD_CancelMandate>  
</soap:Body>  
</soap:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
<soap:Body>  
<Ws_Banking_DD_CancelMandateResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_DD_CancelMandateResult>  
                 <WSID>string</WSID>  
                 <ActionCode>string</ActionCode>  
                 <Messages>  
                       <BankingError>  
                             <field>string</field>  
                             <code>string</code>  
                             <message>string</message>  
                             <error>string</error>  
                        </BankingError>  
                 <Messages>              
          </Ws_Banking_DD_CancelMandateResult>  
</Ws_Banking_DD_CancelMandateResponse>  
</soap:Body>  
</soap:Envelope>
```