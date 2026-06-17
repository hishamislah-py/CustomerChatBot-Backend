# Cancel a Direct Debit

API: `Ws_Banking_CancelDirectDebitBankingEnabledCard`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service marks a direct debit as cancelled where a card has an associated UK Bank Account (provided through programmes using Agency Banking). The web service requires a GUID (Globally Unique ID) for the direct debit, which you can obtain by calling this web service and selecting the correct direct debit.

#### Request Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. | Mandatory | Mandatory |
| <DDIdentifier> | AN |  |  | The unique identifier of the direct debit. | Mandatory |  |
| <Reason> | ENUM\_DirectDebitCancellationReason |  |  | The reason for cancelling the direct debit. See [ENUM\_DirectDebitCancellationReason](../Reference/Enums.htm#ENUM_Dir3) | Mandatory |  |

#### Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <Response> | ENUM\_DirectDebitCancelStatus |  |  | The result of the request. See [ENUM\_DirectDebitCancelStatus](../Reference/Enums.htm#ENUM_Dir). | Omit | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. | Omit | Optional |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

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
      <hyp:Ws_Banking_CancelDirectDebitBankingEnabledCard>  
         <hyp:request>  
            <hyp:WSID>67567675</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:PublicToken>?</hyp:PublicToken>  
            <hyp:DDIdentifier>?</hyp:DDIdentifier>  
            <hyp:Reason>?</hyp:Reason>  
         </hyp:request>  
      </hyp:Ws_Banking_CancelDirectDebitBankingEnabledCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_CancelDirectDebitBankingEnabledCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_CancelDirectDebitBankingEnabledCardResult>  
            <WSID>67567675</WSID>  
            <Response>Success</Response>  
            <ActionCode>000</ActionCode>  
         </Ws_Banking_CancelDirectDebitBankingEnabledCardResult>  
      </Ws_Banking_CancelDirectDebitBankingEnabledCardResponse>  
   </soap:Body>  
</soap:Envelope>
```