# Card Get Passcode

API: `Ws_Get_Passcode`

This web service enables you to retrieve the [Access Code![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Pass code or activation code which you supply to Thredd. You can use the access code to authenticate user access to card services or to request a user to activate the card by entering their access code.](#) (also known as passcode or activation code) of a card.

You must first provide the Access Code to Thredd when creating a card. See [Card Create](Card_Create.htm).

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Omit |
| <AccCode> | AN | 0 | 6 | Access code. For setting a code which is validated during activation, e.g. via an [IVR systemClosed Interactive Voice Response System Typically a telephony-based system, where the user calls in and selects options via an automated voice prompt.](#). If provided, it must be 6 digits, leading zeroes are acceptable. Leave empty if not required. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

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
   <soap:Body>  
      <hyp:Ws_Get_Passcode>  
         <hyp:WSID>202107150820</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
      </hyp:Ws_Get_Passcode>  
   </soap:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Get_PasscodeResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Get_PasscodeResult>  
            <WSID>202107150820</WSID>  
            <AccCode>935647</AccCode>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
         </Ws_Get_PasscodeResult>  
      </Ws_Get_PasscodeResponse>  
   </soap:Body>  
</soap:Envelope>
```