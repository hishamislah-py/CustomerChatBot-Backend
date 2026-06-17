# Apply FX Rate

API: `Ws_Client_FX`

This web service enables you to send your own FX (foreign exchange) rates to Thredd. You can stream in FX rates at your chosen frequency, such as: hourly or daily. The rates could be used for Multi-FX wallet functions or for services such as provisioning of fixed rate FX cards.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <GroupFxID> | N | 1 | 4 | Currency conversion Group ID. | Mandatory | Mandatory |
| <Rates> |  |  |  | An array of rates. See [Rate Details](#Rate) below. Can occur multiple times within the request. | Mandatory | Omit |

#### Rate Details (in request)

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <SrcCurCode> | AN | 3 | 3 | Alpha currency code of source currency( e.g. GBP). | Mandatory | Omit |
| <DesCurCode> | AN | 3 | 3 | Alpha currency code of destination currency (e.g. EUR). | Mandatory | Omit |
| <BuyRate> | D | 1 | (6,8)[\*](#Notes) | Currency buying rate. | Mandatory | Omit |
| <SellRate> | D | 1 | (6,8) | Currency selling rate. If not used, then pass '0' as the default value. | Optional | Omit |
| <MidRate> | D | 1 | (6,8) | Middle currency rate (median average of buy and sell rates). If not used, then pass '0' as the default value. | Optional | Omit |

##### Notes

* (6,8) is 6 numeric with 8 decimal values. This represents a maximum value of 999999.99999999.

#### Rate Details (in response)

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <ActionCode> | AN | 3 | 3 | The action code for the response. Possible action codes in the response are:  000 = Normal, approve.  801 = IssCode is missing.  909 = System malfunction, deny.  868 = Duplicate WSID in the request, deny.  707 = Invalid FX Group ID. | Omit | Mandatory |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <NoOfInvalidRates> | N | 1 | 4 | Number of invalid rates in the request. | Omit | Mandatory |
| <InvalidRates> |  |  |  | See [Invalid Rate Details](#Invalid) below. Can occur multiple times within the response. It is the rejected list of rates in the request. If all rates in the request are valid then it will not present in the response. | Omit | Conditional |

#### Invalid Rate Details (in response)

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <RateNo> | N | 1 | 4 | Position of invalid rate in the request. | Omit | Mandatory |
| <SrcCurCode> | AN | 3 | 3 | Alpha currency code of source currency( e.g. GBP). | Omit | Mandatory |
| <DesCurCode> | AN | 3 | 3 | Alpha currency code of destination currency (e.g. EUR). | Omit | Mandatory |
| <BuyRate> | D | 1 | (6,8)[\*](#Notes) | Currency buying rate. | Omit | Mandatory |
| <SellRate> | D | 1 | (6,8) | Currency selling rate. | Omit | Optional |
| <MidRate> | D | 6,8 | (6,8) | Middle currency rate (median average of buy and sell rates). | Omit | Optional |
| <ErrorCode> | AN | 3 | 3 | Reason code for the rejection. Possible error codes are:  702 = Invalid Currency Buy Rate. It should be greater than 0.0.  703 = Invalid Currency Sell Rate. It should be non-negative.  704 = Invalid Currency Sell Rate. It should be non-negative.  705 = Invalid source currency code  706 = Invalid destination currency code | Omit | Mandatory |
| <ErrorDescription> | AN | 1 | 150 | Reason for the rate rejection. | Omit | Mandatory |

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
      <hyp:Ws_Client_Fx>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:GroupFxID>123</hyp:GroupFxID>  
         <hyp:Rates>  
            <hyp:Rates>  
               <hyp:SrcCurCode>GBP</hyp:SrcCurCode>  
               <hyp:DesCurCode>USD</hyp:DesCurCode>  
               <hyp:BuyRate>1.4</hyp:BuyRate>  
               <hyp:SellRate>1.4</hyp:SellRate>  
               <hyp:MidRate>1.4</hyp:MidRate>  
            </hyp:Rates>  
            <hyp:Rates>  
               <hyp:SrcCurCode>GBP</hyp:SrcCurCode>  
               <hyp:DesCurCode>EUR</hyp:DesCurCode>  
               <hyp:BuyRate>1.1</hyp:BuyRate>  
               <hyp:SellRate>1.1</hyp:SellRate>  
               <hyp:MidRate>1.1</hyp:MidRate>  
            </hyp:Rates>  
            <hyp:Rates>  
               <hyp:SrcCurCode>GBP</hyp:SrcCurCode>  
               <hyp:DesCurCode>ABC</hyp:DesCurCode>  
               <hyp:BuyRate>1.1</hyp:BuyRate>  
               <hyp:SellRate>1.1</hyp:SellRate>  
               <hyp:MidRate>1.1</hyp:MidRate>  
            </hyp:Rates>  
         </hyp:Rates>  
      </hyp:Ws_Client_Fx>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Client_FxResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Client_FxResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <SysDate>2014-08-29</SysDate>  
            <GroupFxID>1</GroupFxID>  
            <NoOfInvalidRates>1</NoOfInvalidRates>  
            <InvalidRates>  
               <InvalidRate>  
                  <RateNo>3</RateNo>  
                  <SrcCurCode>GBP</SrcCurCode>  
                  <DesCurCode>ABC</DesCurCode>  
                  <BuyRate>1.1</BuyRate>  
                  <SellRate>1.1</SellRate>  
                  <MidRate>1.1</MidRate>  
                  <ErrorCode>706</ErrorCode>  
                  <ErrorDescription>Invalid destination currency code</ErrorDescription>  
               </InvalidRate>  
            </InvalidRates>  
         </Ws_Client_FxResult>  
      </Ws_Client_FxResponse>  
   </soap:Body>  
</soap:Envelope>
```