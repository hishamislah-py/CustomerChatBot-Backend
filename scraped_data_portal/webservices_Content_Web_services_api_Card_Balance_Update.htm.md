# Card Balance Update

API: `Ws_BalanceUpdate`

This web service updates the available and current ([STIP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stand-In Processing. Where Thredd holds the card balance on behalf of a Program Manager, in some instances where the Program Manager is not available, we are able to provide an authorisation decision for a transaction on their behalf.](#)) balance for [EHI![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) External Host Interface (EHI) is a Thredd facility that enables exchange of data between the Thredd processing centre and external systems using online web services.
All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions such as Authorisations, the External Host can participate in payment transaction authorisation.](#) (External Host Interface) Mode 4 cards. See the EHI Guide.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value 16. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Unique card identifier. Required in request if `<PublicToken>` is not present. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <CurrCode> | AN | 3 | 3 | In Request: the currency code of the adjustment. Must match the currency of the card account.  In Response: the currency code of the balance returned. This is the same as the currency of the card account. | Mandatory | Mandatory |
| <AvlBalance\_GPS\_STIP> | D | 1 | 20 | The new available to spend balance on the card:  *Available Balance = Current Balance â Blocked Amount* | Mandatory | Omit |
| <CurBalance\_GPS\_STIP> | D | 1 | 20 | The new current balance on the card. Must not be less than the available balance. | Mandatory | Omit |
| <Balance\_Sequence\_Exthost> | N | 1 | 18 | [External HostClosed External Host Interface (EHI) is a Thredd facility that enables exchange of data between the Thredd processing centre and external systems using online web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions such as Authorisations, the External Host can participate in payment transaction authorisation.](#) balance sequence number.  In request: sets the new balances only if this sequence number is higher than the existing balance sequence number currently held in Thredd. This is to ensure that an out-of-date balance is not set due to [race conditionsClosed When two separate processes are reading and updating a value at the same time, then the latest process can overwrite the previous saved result.](#).  In response: the external host balance sequence number in Thredd after this update. (This will be `<Balance_Sequence_Exthost>` in the request message if set, or the current value on Thredd if not set.) | Mandatory | Mandatory |
| <LoadedBy> | AN | 1 | 30 | Name of person or cashier making the adjustment. | Optional | Omit |
| <Balance\_Sequence> | N | 1 | 18 | The Thredd balance sequence returned in the response. This is updated each time Thredd updates the actual balance or blocked amount. | Omit | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ItemID> | AN | 1 | 20 | The unique item ID returned for the adjustment. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |

#### Request

[Copy](javascript:void(0);)

```
<soap:Body>  
   <hyp:Ws_BalanceUpdate>  
      <hyp:WSID>202112345678967890</hyp:WSID>  
      <hyp:IssCode>PMT</hyp:IssCode>  
      <hyp:TxnCode>16</hyp:TxnCode>  
      <hyp:PAN></hyp:PAN>  
      <hyp:PublicToken>123456789</hyp:PublicToken>  
      <hyp:LocDate>2021-01-01</hyp:LocDate>  
      <hyp:LocTime>120000</hyp:LocTime>  
      <hyp:CurrCode>GBP</hyp:CurrCode>  
      <hyp:AvlBalance_GPS_STIP>100</hyp:AvlBalance_GPS_STIP>  
      <hyp:CurBalance_GPS_STIP>110</hyp:CurBalance_GPS_STIP>  
      <hyp:Balance_Sequence_Exthost>1</hyp:Balance_Sequence_Exthost>  
      <hyp:LoadedBy>Test Update</hyp:LoadedBy>  
      </hyp:Ws_BalanceUpdate>  
</soap:Body>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Body>  
   <Ws_BalanceUpdateResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <Ws_BalanceUpdateResult>  
         <WSID>202112345678967890</WSID>  
         <IssCode>PMT</IssCode>  
         <TxnCode>16</TxnCode>  
         <PublicToken>123456789</PublicToken>  
         <LocDate>2021-01-01</LocTime>  
         <LocTime>120000</LocTime>  
         <CurCode>GBP</CurCode>  
         <Balance_Sequence_Exthost>2</Balance_Sequence_Exthost>  
         <Balance_Sequence>2</Balance_Sequence>  
         <SysDate>2021-01-01</SysDate>  
         <ItemID>23290</ItemID>  
         <ActionCode>000</ActionCode>  
         <WebServiceResult/>   
      </Ws_BalanceUpdateResult>  
   </Ws_BalanceUpdateResponse>  
</soap:Body>
```