# List Groups

API: `Ws_list_group`

This web service lists the codes and descriptions of all groups of a certain type (e.g. Fee Groups, Limit Groups).

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <GroupType> | N | 1 | 2 | Group Type identifier. Possible values are:  1 = Limit Groups  2 = Authorisation Fee Groups  3 = Recurring/Scheduled Fee Groups  4 = Web Service Fee Groups  5 = MCC Groups  6 = Usage Groups  7 = Linkage Groups  8 = FX Groups  9 = Auth Calendar Groups  10 = Payment Token Usage Groups | Mandatory | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <GroupInfo> | - | - | - | Returns a list of `<GroupListInfo>`. See [Group List Info](#Group) below. Can occur multiple times within the message. |  |  |

#### Group List Info

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <GroupCode> | AN | 1 | 10 | Group code. | Omit | Mandatory |
| <GroupDesc> | AN | 1 | 30 | Group description. | Omit | Mandatory |

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
      <hyp:Ws_List_Group>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:GroupType>1</hyp:GroupType>  
      </hyp:Ws_List_Group>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_List_GroupResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_List_GroupResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <GroupType>1</GroupType>  
            <SysDate>2014-10-28</SysDate>  
            <ActionCode>000</ActionCode>  
            <GroupInfo>  
               <GroupListInfo>  
                  <GroupCode>GRP_EURO</GroupCode>  
                  <GroupDesc>GROUP EURO</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRP_GBP</GroupCode>  
                  <GroupDesc>GROUP GBP</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRP_USD</GroupCode>  
                  <GroupDesc>GROUP USD</GroupDesc>  
               </GroupListInfo>  
            </GroupInfo>  
         </Ws_List_GroupResult>  
      </Ws_List_GroupResponse>  
   </soap:Body>  
</soap:Envelope>
```