# Card List Pending Fees

API: `Ws_List_Pending_Fees`

This web service lists details of pending fees that relate to a specific card.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. Mandatory in the request. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards that belong to the given program manager. | Mandatory | Mandatory |
| <PAN> | N | 14 | 19 | Original PAN number embossed on the card. If present in the request, then this method returns the pending fee details of the given card only. | Optional | Omit |
| <PublicToken> | N | 9 | 9 | Cardâs public token. If present in the request, then this method returns the pending fee details of the given card only. | Optional | Omit |
| <FeeProcessingCode> | AN | 2 | 2 | The transaction fee processing code. See [Processing Codes (fees)](../Reference/Web_Service_Processing_Codes.htm). | Optional | Omit |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Fees> | - | - | - | An array of `Fee` records. See [Fee Record](#Fee) below. Can occur multiple times within the message. |  |  |

#### Fee Record

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PublicToken> | N | 9 | 9 | Cardâs public token. | Omit | Mandatory |
| <PostDate> | YYYY-MM-DD | 10 | 10 | Actual date when Thredd received the fee request. | Omit | Mandatory |
| <TransDate> | YYYY-MM-DD | 10 | 10 | Date in which Thredd processed the fee request. | Omit | Mandatory |
| <ProcCode> | AN | 1 | 3 | The transaction fee processing code. See [Processing Codes (fees)](../Reference/Web_Service_Processing_Codes.htm). | Omit | Mandatory |
| <ActualAmt> | D | 1 | 20 | Actual fee amount. | Omit | Mandatory |
| <AmtTaken> | D | 1 | 20 | Amount already taken. | Omit | Mandatory |
| <RemainingAmt> | D | 1 | 20 | Remaining amount need to take as fee, i.e., *<ActualAmt> - <AmtTaken>*. | Omit | Mandatory |
| <Description> | AN | 1 | 150 | Fee description. | Omit | Mandatory |
| <PartialAllowed> | N | 1 | 1 | Whether a partial amount is allowed.  1 = Allowed; 0 = Not allowed | Omit | Mandatory |
| <Collected> | N | 1 | 1 | Whether the fee has been taken.  1 = Taken; 0 = Not taken | Omit | Mandatory |
| <PendingFeesEnabled> | N | 1 | 1 | Whether pending fees is enabled. 1 = Enabled; 0 = Disabled | Omit | Mandatory |

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
      <hyp:Ws_List_Pending_Fees>  
         <hyp:WSID>20211234567896789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:FeeProcessingCode></hyp:FeeProcessingCode>  
      </hyp:Ws_List_Pending_Fees>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_List_Pending_FeesResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_List_Pending_FeesResult>  
            <WSID>20211234567896789</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <Fees>  
               <Fee>  
                  <PublicToken>123456789</PublicToken>  
                  <PostDate>2021-09-14</PostDate>  
                  <TransDate>2021-09-14</TransDate>  
                  <ProcCode>10</ProcCode>  
                  <ActualAmt>1</ActualAmt>  
                  <AmtTaken>1</AmtTaken>  
                  <RemainingAmt>0.1</RemainingAmt>  
                  <Description>Load fee</Description>  
                  <PartialAllowed>true</PartialAllowed>  
                  <Collected>true</Collected>  
                  <PendingFeesEnabled>true</PendingFeesEnabled>  
               </Fee>  
               <Fee>  
                  <PublicToken>123456789</PublicToken>  
                  <PostDate>2021-09-14</PostDate>  
                  <TransDate>2021-09-14</TransDate>  
                  <ProcCode>82</ProcCode>  
                  <ActualAmt>2</ActualAmt>  
                  <AmtTaken>0</AmtTaken>  
                  <RemainingAmt>2</RemainingAmt>  
                  <Description>Card Issue Fee</Description>  
                  <PartialAllowed>false</PartialAllowed>  
                  <Collected>true</Collected>  
                  <PendingFeesEnabled>true</PendingFeesEnabled>  
               </Fee>  
            </Fees>  
         </Ws_List_Pending_FeesResult>  
      </Ws_List_Pending_FeesResponse>  
   </soap:Body>  
</soap:Envelope>
```