# Bank Account Check Number

API: `Ws_Banking_AccountModulusCheck`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service validates that a sort code and account number (UK Bank Accounts provided through programmes using Thredd Bottomline Agency Banking) are valid.

This uses a modulus check to confirm that the account number *could* be a valid account number.

To use this web service call, there needs to be a financial agreement in place with Bottomline. For more informatiom, check with your Account Manager.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <SortCode> | N | 6 | 6 | The sort code of the account that needs checking.  **Note**: for accurate results, the sort code should have been registered with the Vocalink Account Modulus, otherwise all values return true. | Mandatory | Mandatory |
| <AccountNumber> | N | 8 | 8 | The account number. | Mandatory | Mandatory |

#### Reponse Description

There is no description for the response. This is a pass through from another service. You should check the `<ActionCode>` tag in the response to ensure the request was a successful and the `<Valid>` flag to determine the action.

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
      <hyp:Ws_Banking_AccountModulusCheck>  
         <hyp:request>  
            <hyp:WSID>8976875765765</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:SortCode>123456</hyp:SortCode>  
            <hyp:AccountNumber>98765432</hyp:AccountNumber>  
         </hyp:request>  
      </hyp:Ws_Banking_AccountModulusCheck>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_AccountModulusCheckResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_AccountModulusCheckResult>  
            <WSID>8976875765765</WSID>  
            <ActionCode>000</ActionCode>  
            <VSeriesResponse>  
               <AccountDetailsInput>  
                  <SortCode></SortCode>  
                  <AccountNumber></AccountNumber>  
                  <BuildingSocietyRollNumber/>  
               </AccountDetailsInput>  
               <AccountDetailsOutput>  
                  <SortCode></SortCode>  
                  <AccountNumber></AccountNumber>  
                  <BuildingSocietyRollNumber/>  
               </AccountDetailsOutput>  
               <AccountIBAN></AccountIBAN>  
               <AccountTranscribed></AccountTranscribed>  
               <UkBankBranch>  
                  <TransactionInfo>  
                     <BacsCredits></BacsCredits>  
                     <BacsDebits></BacsDebits>  
                     <FasterPaymentsService></FasterPaymentsService>  
                     <ChapsSterling></ChapsSterling>  
                     <DirectDebitInstructions></DirectDebitInstructions>  
                     <UnpaidChequeClaims></UnpaidChequeClaims>  
                     <DividendInterest></DividendInterest>  
                     <BuildingSocietyInterest></BuildingSocietyInterest>  
                  </TransactionInfo>  
               </UkBankBranch>  
               <RequiresBuildingSocietyRollNumber></RequiresBuildingSocietyRollNumber>  
               <BuildingSocietyRollNumberTranscribed></BuildingSocietyRollNumberTranscribed>  
               <PublicInvalidIssue>0</PublicInvalidIssue>  
               <Valid></Valid>  
               <InvalidReason/>  
               <InvalidParameter/>  
            </VSeriesResponse>  
         </Ws_Banking_AccountModulusCheckResult>  
      </Ws_Banking_AccountModulusCheckResponse>  
   </soap:Body>  
</soap:Envelope>
```