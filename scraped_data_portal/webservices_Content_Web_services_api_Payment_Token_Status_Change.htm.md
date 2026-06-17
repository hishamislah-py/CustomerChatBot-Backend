# Payment Token Status Change

API: `Ws_Payment_Token_StatusChange`

This web service changes the status of an [MDES![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The MasterCard Digital Enablement Service (MDES) helps transform any connected device into a commerce device to make and receive payments. The MDES platform is used in iPhone 6, iPhone 6 Plus and Apple Watch to enable secure payments to take place for contactless and in-app payments.](#) (Mastercard Digital Enablement Service) or Visa Token Service (VTS) payment token card. The web service also changes the [Usage Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group that controls where a card can be used. For example: POS or ATM.](#) of the card.

#### Record Description

| Tag | Type | Minimum Len | Maximum Len | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value 2. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Unique card identifier. The PAN is Mandatory if `<PublicToken>` is not supplied. | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | Thredd 9-digit public token of the card. Mandatory if the PAN is not supplied. | Conditional | Mandatory |
| <DPAN> | AN | 16 | 19 | Digital PAN value for the card. Mandatory if `<PaymentTokenId>` is not supplied. | Conditional | Mandatory |
| <PaymentTokenId> | AN | 1 | 20 | Payment token identifier for the MDES or VTS Card. Mandatory if the DPAN is not supplied. | Conditional | Mandatory |
| <LocDate> | YYYY-MM-  DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <NewStatCode> | AN | 2 | 2 | New status code you want to change to. The Card Scheme is notified of the status change. See [Status Codes](../Reference/Status_Codes.htm).    **Note**: You must specify a value for either *<NewStatCode>* or *<UsageGroup>*. If both fields are left blank or not specified in the request, then the error message *712-invalid filter* is returned.  **Note**: To temporary *Suspend*  a Card Scheme payment token, you can use status code values of 02, 05, 57, 59, 62, 63, G1, G2, G3 or G4. To permentantly *Delete* or *Deactivate* a Card Scheme payment token, you can use status code values of: 04, 41, 43, 46, 83 or 99. We recommend using a value which corresponds best to the suspension or deactivation/deletion reason. | Conditional | Omit |
| <TerminalID> | AN | 1 | 15 | Point of Sale (POS) or other terminal identifier, such as a hostname. | Optional | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <NetworkError> | AN | 1 | 6 | Error code give if there is a problem sending the MDES 0302 message. | Omit | Conditional |
| <UsageGroup> | AN | 1 | 15 | Updates the [usage groupClosed Group that controls where a card can be used. For example: POS or ATM.](#) of the card linked to the payment token. The usage group determines where the payment token can be used (e.g., Point of Sale terminal, ATM, ecommerce).This corresponds to the `<PERMSGroup>` field in the [Card Create](Card_Create.htm) web service.    **Note**: You must specify a value for either *<NewStatCode>* or *<UsageGroup>*. If both fields are left blank or not specified in the request, then the error message *712-invalid filter* is returned.  **Note**: If an invalid usage group is specified, then the error message *866 - Invalid Usage group code* is returned. | Conditional | Omit |
| <Activate> | Boolean | 1 | 1 | Whether to activate the payment token on the MDES system (Mastercard tokens only).  1= activate the token; 0 = do not activate the token.    **Note**: If no value is specified, this will default to 0.  **Note**: If you receive a 951 action code in the response you can retry the web service call or else use the Mastercard Portal to update the token status. | Conditional | Omit |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |

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
      <hyp:Ws_Payment_Token_StatusChange>  
         <hyp:WSID>202112345678967890</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>2</hyp:TxnCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:DPAN>0987654321012</hyp:DPAN>  
         <hyp:PaymentTokenId></hyp:PaymentTokenId>  
         <hyp:LocDate>2017-01-01</hyp:LocDate>  
         <hyp:LocTime>123456</hyp:LocTime>  
         <hyp:NewStatCode>00</hyp:NewStatCode>  
         <hyp:TerminalID></hyp:TerminalID>  
         <hp:UsageGroup>GROUP1</hyp:UsageGroup>  
         <hp:Activate>1</hyp:Activate>  
      </hyp:Ws_Payment_Token_StatusChange>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Payment_Token_StatusChangeResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Payment_Token_StatusChangeResult>  
            <WSID>202112345678967890</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>2</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <PaymentTokenId>2</PaymentTokenId>  
            <LocDate>2017-01-01</LocDate>  
            <LocTime>123456</LocTime>  
            <SysDate>2017-11-17</SysDate>  
            <ActionCode>000</ActionCode>  
            <WebServiceResult/>   
         </Ws_Payment_Token_StatusChangeResult>  
      </Ws_Payment_Token_StatusChangeResponse>  
   </soap:Body>  
</soap:Envelope>
```