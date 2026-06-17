# WebServiceResult

In many web services, the response returns this parameter to a request when the request includes the same WSID as a previously submitted request. It can be used to check if the previous request was successful.

| Tag | Type | Minimum Length | Maximum Length | Description |
| --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID from the original request. |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. |
| <PublicToken> | AN | 1 | 9 | The public token of the card from the original request. |
| <WebServiceName> | AN | 1 | 50 | The name of the web service for the request. |
| <Description> | AN | 1 | 50 | Description of the status of the original request. If successful, returns: *Normal, approve*. |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](Action_Codes.htm). |

#### Response Example

The response returns action code 000 for the first request of `Ws_CreateCard`.

[Copy](javascript:void(0);)

```
         <WebServiceResult>  
               <WSID>2021123114561789</WSID>  
               <IssCode/>  
               <PublicToken>118423597</PublicToken>  
               <WebServiceName>Ws_CreateCard</WebServiceName>  
               <Description>Normal, approve</Description>  
               <ActionCode>000</ActionCode>  
            </WebServiceResult>
```

#### Response - Duplicate Request Example

The response returns action code 868 for a duplicate request (where the same WSID is used).

[Copy](javascript:void(0);)

```
        <WebServiceResult>  
           <WSID>2021123114561789</WSID>  
           <IssCode/>  
           <PublicToken>118423597</PublicToken>  
           <WebServiceName>Ws_CreateCard</WebServiceName>  
           <Description>Duplicate WSID in the request, deny.</Description>  
           <ActionCode>868</ActionCode>  
        </WebServiceResult>
```