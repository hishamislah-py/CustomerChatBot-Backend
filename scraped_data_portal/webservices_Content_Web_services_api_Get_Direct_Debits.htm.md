# Get Direct Debits

API: `Ws_Banking_GetDirectDebitInstructionsBankingEnabledCard`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service returns a list of all direct debits for a given token (with or without sub-accounts).

#### Record Request Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Conditional | Mandatory |
| <CardDesign> | AN | 1 | 8 | The identifier of the card product, or `Product ID`, within Thredd, for which you want to retrieve a list of direct debits. | Conditional | Omit |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account from which to retrieve a list of direct debits. | Mandatory | Mandatory |
| <IncludeSubAccounts> | N | 1 | 1 | Whether all sub-accounts are included. 0 = No; 1 = Yes. Default is 1. | Optional | Optional |
| <CreatedFrom> | DateTime |  |  | The date from which the direct debits are included. In *YYYY-MM-DD* format. | Optional | Optional |
| DirectDebitStatus | ENUM\_DirectDebitStatus |  |  | The status of the direct debits to be included. See [ENUM\_DirectDebitStatus](../Reference/Enums.htm#ENUM_Dir2). | Optional | Optional |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. | Omit | Optional |
| <DirectDebit> | List (BLDirectDebit  ) |  |  | A list of direct debits. See [BLDirectDebit](../Reference/Enums.htm#Appendix). | Omit | Mandatory |

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
      <hyp:Ws_Banking_GetDirectDebitInstructionsBankingEnabledCard>  
         <hyp:request>  
            <hyp:WSID>2021123456789</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:CardDesign>?</hyp:CardDesign>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
            <hyp:IncludeSubAccounts>?</hyp:IncludeSubAccounts>  
            <hyp:CreatedFrom>?</hyp:CreatedFrom>  
            <hyp:DirectDebitStatus>?</hyp:DirectDebitStatus>  
         </hyp:request>  
      </hyp:Ws_Banking_GetDirectDebitInstructionsBankingEnabledCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_GetDirectDebitInstructionsBankingEnabledCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_GetDirectDebitInstructionsBankingEnabledCardResult>  
            <WSID>2021123456789</WSID>  
            <ActionCode></ActionCode>  
            <DirectDebits>  
               <BLDirectDebit>  
                  <Created></Created>  
                  <CreationMethod></CreationMethod>  
                  <CreditorAccountName></CreditorAccountName>  
                  <CreditorBIC/>  
                  <CreditorIBAN/>  
                  <CreditorReference/>  
                  <DebtorAccountID></DebtorAccountID>  
                  <DerivedReference></DerivedReference>  
                  <IBAN></IBAN>  
                  <ID></ID>  
                  <IgnoreTransactionCode></IgnoreTransactionCode>  
                  <IsInstructionHeldAtBank></IsInstructionHeldAtBank>  
                  <IsPaperless></IsPaperless>  
                  <IsThroughNotificationService></IsThroughNotificationService>  
                  <LastChanged></LastChanged>  
                  <Reference></Reference>  
                  <ServiceUserNumber></ServiceUserNumber>  
                  <Status></Status>  
                  <SuppressFirstDirectDebit></SuppressFirstDirectDebit>  
               </BLDirectDebit>  
           <BLDirectDebit>  
                  <Created></Created>  
                  <CreationMethod></CreationMethod>  
                  <CreditorAccountName></CreditorAccountName>  
                  <CreditorBIC/>  
                  <CreditorIBAN/>  
                  <CreditorReference/>  
                  <DebtorAccountID></DebtorAccountID>  
                  <DerivedReference></DerivedReference>  
                  <IBAN></IBAN>  
                  <ID></ID>  
                  <IgnoreTransactionCode></IgnoreTransactionCode>  
                  <IsInstructionHeldAtBank></IsInstructionHeldAtBank>  
                  <IsPaperless></IsPaperless>  
                  <IsThroughNotificationService></IsThroughNotificationService>  
                  <LastChanged></LastChanged>  
                  <Reference></Reference>  
                  <ServiceUserNumber></ServiceUserNumber>  
                  <Status></Status>  
                  <SuppressFirstDirectDebit></SuppressFirstDirectDebit>  
               </BLDirectDebit>  
            </DirectDebits>  
         </Ws_Banking_GetDirectDebitInstructionsBankingEnabledCardResult>  
      </Ws_Banking_GetDirectDebitInstructionsBankingEnabledCardResponse>  
   </soap:Body>  
</soap:Envelope>  
 
```