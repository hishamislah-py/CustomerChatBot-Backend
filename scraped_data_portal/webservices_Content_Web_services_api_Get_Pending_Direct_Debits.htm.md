# Get Pending Direct Debits

API: `Ws_Banking_GetPendingDirectDebits`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service returns a list of all direct debits that are due for payment today for a given token (with or without sub- accounts). You can also specify whether to return a list of pending direct debits that will not be paid (idue to insufficient funds in the account). The response is indicative only and is based on the situation at 3 am processing time, and does not guarantee which Direct Debits will not be paid.

The data in this call is only valid between the first processing call (approximately 3am UK time) and the final call (approximately 3pm UK time). After this time, the Direct Debit will be processed.

#### Record Request Description

| Tag | Type | Minimum Lengthgth | Maximum Lengthgth | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardDesign> | N | 1 | 8 | The identifier of the card product, or `Product ID`, within Thredd, for which you want to retrieve a list of direct debits. |  |  |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account from which to retrieve a list of direct debits. | Mandatory | Mandatory |
| <IncludeSubAccounts> | N |  |  | Whether all sub-accounts are included. 0 = No; 1 = Yes. Default is 1. |  |  |
| <IncludeAll> | N |  |  | A flag to indicate whether all pending direct debits should be returned or just those that won't be paid. 0 = Only those not paid; 1 = All. | Optional |  |
| <PendingDirectDebits> | List (PendingDirectDebit) |  |  | A list of direct debits. See [PendingDirectDebit](../Reference/Enums.htm#ENUM_Pen). | Omit | Optional |
| <TotalValueOfTransactions> | D | 1 | 19 | Total value of transactions. | Omit | Mandatory |
| <TotalValueOfFees> | D | 1 | 19 | Total value of fees. | Omit | Mandatory |
| <TotalValueOfTransactionsAndFees> | D | 1 | 19 | Total value of transactions and fees. | Omit | Mandatory |
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
      <hyp:Ws_Banking_GetPendingDirectDebits>  
         <hyp:request>  
            <hyp:WSID></hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:CardDesign></hyp:CardDesign>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
            <hyp:IncludeSubAccounts> </hyp:IncludeSubAccounts>  
            <hyp:IncludeAll> </hyp:IncludeAll>  
         </hyp:request>  
      </hyp:Ws_Banking_GetPendingDirectDebits>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_GetPendingDirectDebitsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_GetPendingDirectDebitsResult>  
            <WSID>2021123456789</WSID>  
            <PendingDirectDebits>  
               <PendingDirectDebit>  
                  <PublicToken>123456789</PublicToken>  
                  <BLGUID> </BLGUID>  
                  <IBAN> </IBAN>  
                  <Amount></Amount>  
                  <CreatedDate></CreatedDate>  
                  <CreditorReference> </CreditorReference>  
                  <Reference> </Reference>  
                  <AvailableAmount></AvailableAmount>  
                  <PendingSuccess> </PendingSuccess>  
               </PendingDirectDebit>  
            </PendingDirectDebits>  
            <ActionCode></ActionCode>  
         </Ws_Banking_GetPendingDirectDebitsResult>  
      </Ws_Banking_GetPendingDirectDebitsResponse>  
   </soap:Body>  
</soap:Envelope>
```