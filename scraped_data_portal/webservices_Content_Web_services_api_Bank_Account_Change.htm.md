# Bank Account Change

API: `Ws_Banking_ChangeAccountBankingFeaturesStatus`

This web service is for legacy use only. For the latest Agency Banking web services via Modulr, see [Banking Services Overview](Banking_Services_Overview.htm).

This web service changes the features of the banking enabled card and allows you to switch functionality on or off.

#### Request Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. | Mandatory | Mandatory |
| <UpdateSubAccountsToSame> | B |  |  | Setting this flag to true updates all associated accounts (sub-accounts) to the same values. If missed out, the default value is true. | Optional | Optional |
| <BankingFeatures> | BankingFeaturesType |  |  | See [BankingFeaturesType](../Reference/Enums.htm#BankingF). | Mandatory | Mandatory |

#### Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <ActionCode> | A | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Mandatory | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. |  | Optional |
| <Response> | ENUM\_ChangeAccountStatus |  |  | This indicates if the call was successful or not and the reason why. See [[ENUM\_ChangeAccountStatus](../Reference/Enums.htm#ENUM_ChangeAccountStatus)](../Reference/Enums.htm#ENUM_ChangeAccountStatus). |  | Mandatory |
| <Accounts> | ChangedBankingFeatures |  |  | A list of changed accounts, detailing their current status. See [ChangedBankingFeatures](../Reference/Enums.htm#Changed). |  | Optional |

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
      <hyp:Ws_Banking_ChangeAccountBankingFeaturesStatus>  
         <hyp:request>  
            <hyp:WSID>765776764</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
            <hyp:UpdateSubAccountsToSame>false</hyp:UpdateSubAccountsToSame>  
            <hyp:BankingFeatures>  
               <hyp:BankingIn>DisableBankingIn</hyp:BankingIn>  
               <hyp:BankingOut>DisableBankingOut</hyp:BankingOut>  
               <hyp:DirectDebitIn>DisableDirectDebitIn</hyp:DirectDebitIn>  
               <hyp:DirectDebitOut>DisableDirectDebitOut</hyp:DirectDebitOut>  
            </hyp:BankingFeatures>  
         </hyp:request>  
      </hyp:Ws_Banking_ChangeAccountBankingFeaturesStatus>  
   </soapenv:Body>  
</soapenv:Envelope>
```

Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_ChangeAccountBankingFeaturesStatusResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_ChangeAccountBankingFeaturesStatusResult>  
            <WSID>765776764</WSID>  
            <ErrorText></ErrorText>  
            <ActionCode>000</ActionCode>  
            <Response>Success</Response>  
            <Accounts>  
               <ChangedBankingFeatures>  
                  <PublicToken>123456789</PublicToken>  
                  <BankingFeatures>  
                     <BankingIn>Disabled</BankingIn>  
                     <BankingOut>Disabled</BankingOut>  
                     <DirectDebitIn>Disabled</DirectDebitIn>  
                     <DirectDebitOut>Disabled</DirectDebitOut>  
                     <CardEnabled>Enabled</CardEnabled>  
                  </BankingFeatures>  
                  <UpdateSuccess>DirectDebitNotAllowed</UpdateSuccess>  
               </ChangedBankingFeatures>  
            </Accounts>  
         </Ws_Banking_ChangeAccountBankingFeaturesStatusResult>  
      </Ws_Banking_ChangeAccountBankingFeaturesStatusResponse>  
   </soap:Body>  
</soap:Envelope>
```