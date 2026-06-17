# Update Card Status

API: `Ws_Banking_UpdateBankingEnabledCard`

This web service updates the status of banking services for a card depending on it's current status (see table below showing which statuses can be changed).

If changing the status of a primary account with sub-accounts to *closed*, the call will close each sub-account and move any money into the primary account. If the primary account has a balance, the account cannot be closed and you are informed via the response. Applies only to programmes using Agency Banking.

| New Status | Open | SuspendedPaymentsIn | FullySuspended | Deceased | Probate | Closed |
| --- | --- | --- | --- | --- | --- | --- |
| Open | - | Y | Y | X | X | X |
| SuspendedPaymentsIn | Y | - | Y | X | X | X |
| FullySuspended | Y | Y | - | X | X | X |
| Deceased | Y | Y | Y | - | X | X |
| Probate | X | X | X | Y | - | X |
| Closed | Y | Y | Y | Y | Y | - |

Y = Yes (can change from this status); X = No. For example: You can change the status of an account to *Open* ony if it has a status of *SuspendedPaymentsIn* or *FullySuspended*. Onced an account is closed, you cannot change its status.

#### Record Request Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. | Mandatory | Mandatory |
| <NewStatus> | ENUM\_AccountStatus |  |  | See [ENUM\_AccountStatus](../Reference/Enums.htm#AccountS). |  |  |
| <UpdateSubAccountsToSame> | B |  |  | Whether all sub-accounts should be set to the same value. This is ignored if the primary account is set to *Closed*. |  |  |
| <Notes> |  |  |  | A simple field for notes to be stored on the system. |  |  |

#### Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <PublicToken> | N | 9 | 9 | The 9 digit public token associated with the account. |  | Mandatory |
| <Accounts> | BLAccount |  |  | A list of BLAccounts that were updated. See [BLAccount](../Reference/Enums.htm#BLAccoun). |  | Optional |
| <TotalBalance> | D |  |  | Shows the balance on the card or any sub-accounts. |  | Optional |
| <CloseAccountStatus> |  |  |  | The status of the attempt. See [ENUM\_CloseAccountStatus](../Reference/Enums.htm#CloseAcc). |  | Mandatory |
| <ErrorText> | AN |  |  | Human readable text of the error that occurred. Should be read in conjunction with the `<ActionCode>`. |  | Optional |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). |  | Mandatory |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>    
         <hyp:strUserName>******** </hyp:strUserName>    
         <hyp:strPassword>***** </hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_Banking_UpdateBankingEnabledCard>  
         <hyp:request>  
            <hyp:WSID>5767455646545</hyp:WSID>  
            <hyp:IssCode>PMTD</hyp:IssCode>  
            <hyp:PublicToken>123456789</hyp:PublicToken>  
            <hyp:NewStatus>Closed</hyp:NewStatus>  
            <hyp:UpdateSubAccountsToSame>false</hyp:UpdateSubAccountsToSame>  
            <hyp:Notes>This is a test </hyp:Notes>  
         </hyp:request>  
      </hyp:Ws_Banking_UpdateBankingEnabledCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Banking_UpdateBankingEnabledCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Banking_UpdateBankingEnabledCardResult>  
            <WSID>5767455646545</WSID>  
            <PublicToken>123456789</PublicToken>  
            <Accounts>  
               <BLAccount>  
                  <PublicToken>123456789</PublicToken>  
                  <SortCode></SortCode>  
                  <AccountNumber></AccountNumber>  
                  <Status>Closed</Status>  
                  <Balance>0</Balance>  
               </BLAccount>  
            </Accounts>  
            <TotalBalance>0</TotalBalance>  
            <CloseAccountStatus>AllClosed</CloseAccountStatus>  
            <ErrorText></ErrorText>  
            <ActionCode>000</ActionCode>  
         </Ws_Banking_UpdateBankingEnabledCardResult>  
      </Ws_Banking_UpdateBankingEnabledCardResponse>  
   </soap:Body>  
</soap:Envelope>
```