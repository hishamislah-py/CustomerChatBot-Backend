# Card Phone Activation

API: `Ws_Phone_Activation`

This web service enables activation of a card by phone. It also returns the PIN and the PIN status of that card.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PAN> | AN | 14 | 19 | Card Number. Unique card identifier. Mandatory in request if `<track2>` and `<PublicToken>` are not present. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` and `<Track2>` are not present. In virtual card creation `<PublicToken>` is not required in the request. Mandatory in the response. | Conditional | Mandatory |
| <SecurityCode> | N | 6 | 6 | The cardâs 6 digit security code. Mandatory when `<AuthType>` is 4. | Mandatory | Omit |
| <ActivateIfNot> | N | 1 | 1 | If set to 1, then returns the PIN number of the card and activates the card if not already activated. | Mandatory | Omit |
| <AuthType> | AN | 1 | 1 | Parameter to specify how the card is authenticated. See [Authentication Methods](../Reference/Authentication_Methods.htm). | Mandatory | Omit |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <IsLive> | N | 1 | 1 | Specifies whether the card is active or not. 1 or True = Active; 0 or False = Not Active. | Omit | Mandatory |
| <PinBlock> | AN | 4 | 12 | Current PIN number of the card, represented as a 4-12 digit PIN block. | Omit | Mandatory |
| <PINStatus> | N | 1 | 1 | Indicates whether the allowed number of card PIN tries has been exceeded. 0 = No; 1 = Yes. | Omit | Mandatory |

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
      <hyp:Ws_Phone_Activation>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:SecurityCode>0</hyp:SecurityCode>  
         <hyp:ActivateIfNot>0</hyp:ActivateIfNot>  
         <hyp:AuthType>1</hyp:AuthType>  
      </hyp:Ws_Phone_Activation>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Phone_ActivationResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Phone_ActivationResult>  
            <PublicToken>123456789</PublicToken>  
            <ActionCode>000</ActionCode>  
            <IsLive>true</IsLive>  
            <PinBlock>1234</PinBlock>  
            <PINStatus>0</PINStatus>  
         </Ws_Phone_ActivationResult>  
      </Ws_Phone_ActivationResponse>  
   </soap:Body>  
</soap:Envelope>
```