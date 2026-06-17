# Remove Cardholder Data

API: `Ws_Remove_CardHolder_Data`

This web service removes personally identifiable cardholder data (cardholder name, address, email and phone number) from the specified card. You can remove data from multiple cards in a single request.

Before removing data from a card record, the web service checks that the card's issue date is more than 6 years old. The card must not have any balance or blocked amount. The status of the card must be either *Destroyed* or *Expired*.

This web service does not remove any transactional details, and does not affect transactional data, such as authorisations and financial records.

Once deleted, this operation cannot be undone. Ensure you take extra care before using this web service.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every web service request sent. For details, see the [FAQs](../FAQs.htm).**Tip**: You could use a number based on the current date and time, as long as it is unique (e.g., *20201217145006*). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TokenData> | AN | 1 | 9 | The public token of the card. You can specify an array of `TokenData` elements, to remove cardholder data from multiple cards in a single request. | Mandatory | Omit |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <TokensCount> | AN | 1 | 4 | The number of public token updates requested. | Omit | Mandatory |
| <TokenDetailsResponse> |  |  |  | Provides an array of token results, one for each public token update request. See [TokenResult](#TokenRes). | Omit | Mandatory |

#### TokenResult

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PublicToken> | AN | 1 | 9 | The public token of the card. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the public token: *000* indicates that the public token has been sucessfully updated. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <ActionDescription> | AN | 1 | 4 | Description of the result of the request: *Normal, approve* indicates that the public token has been sucessfully updated. | Omit | Mandatory |

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
        <hyp:Ws_Remove_CardHolder_Data>  
            <hyp:WSID>2022202208301234556</hyp:WSID>              
            <hyp:IssCode>PMT</hyp:IssCode>              
            <hyp:TokenData>  
                <!--Zero or more repetitions:-->  
                <hyp:TokenData>                      
                    <hyp:PubToken>523686956</hyp:PubToken>  
                </hyp:TokenData>  
                <hyp:TokenData>                      
                    <hyp:PubToken>136331110</hyp:PubToken>  
                </hyp:TokenData>  
                <hyp:TokenData>                      
                    <hyp:PubToken>112060766</hyp:PubToken>  
                </hyp:TokenData>  
                <hyp:TokenData>                      
                    <hyp:PubToken>112060766</hyp:PubToken>  
                </hyp:TokenData>  
                <hyp:TokenData>                      
                    <hyp:PubToken>112730529</hyp:PubToken>  
                </hyp:TokenData>  
            </hyp:TokenData>              
                 <hyp:LocDate>2022-20-05</hyp:LocDate>                   
                 <hyp:LocTime>1200800</hyp:LocTime>  
        </hyp:Ws_Remove_CardHolder_Data>  
    </soapenv:Body>
```

#### Response

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
    <soap:Body>  
        <Ws_Remove_CardHolder_DataResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
            <Ws_Remove_CardHolder_DataResult>  
                <WSID>2022202208301234556</WSID>  
                <IssCode>PMT</IssCode>  
                <ActionCode>000</ActionCode>  
                <SysDate>2022-04-01</SysDate>  
                <TokensCount>5</TokensCount>  
                <TokenDetailsResponse>  
                    <TokenResult>  
                        <PubToken>136331110</PubToken>  
                        <ActionCode>000</ActionCode>  
                        <ActionDescription>Normal, approve</ActionDescription>  
                    </TokenResult>  
                    <TokenResult>  
                        <PubToken>112060766</PubToken>  
                        <ActionCode>000</ActionCode>  
                        <ActionDescription>Normal, approve</ActionDescription>  
                    </TokenResult>  
                    <TokenResult>  
                        <PubToken>523686956</PubToken>  
                        <ActionCode>000</ActionCode>  
                        <ActionDescription>Normal, approve</ActionDescription>  
                    </TokenResult>  
                    <TokenResult>  
                        <PubToken>112060766</PubToken>  
                        <ActionCode>000</ActionCode>  
                        <ActionDescription>Normal, approve</ActionDescription>  
                    </TokenResult>  
                    <TokenResult>  
                        <PubToken>112730529</PubToken>  
                        <ActionCode>000</ActionCode>  
                        <ActionDescription>Normal, approve</ActionDescription>  
                    </TokenResult>  
                </TokenDetailsResponse>  
                <LocDate>2022-20-05</LocDate>  
                <LocTime>1200800</LocTime>  
            </Ws_Remove_CardHolder_DataResult>  
        </Ws_Remove_CardHolder_DataResponse>  
    </soap:Body>  
</soap:Envelope>
```