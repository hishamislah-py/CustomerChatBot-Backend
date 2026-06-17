# Payment Token Get

API: `Ws_Payment_Token_Get`

This web service gets the details for both [Mastercard Digital Enablement Service![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The MasterCard Digital Enablement Service (MDES) is a data interchange platform for generating and managing secure digital payment tokens.](#) (MDES) payment token cards and Visa Token Service (VTS) cards.

Your request must provide one of the following card details: `PAN`, `PublicToken`, `DPAN` or `Payment_Token_ID`. If the MDES or VTS card is not specified, the call returns all linked MDES or VTS cards.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. If only `<IssCode>` is present in the request then this method returns the pending fee details of all cards belonging to the given program manager. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value is 9. | Mandatory | Mandatory |
| <PAN> | N | 14 | 19 | Card Number. Unique card identifier. | Conditional | Omit |
| <PublicToken> | N | 9 | 9 | Thredd 9-digit public token of the card. | Conditional | Omit |
| <DPAN> | AN | 16 | 19 | Digital PAN value for the card. | Conditional | Omit |
| <Payment\_Token\_ID> | N | 1 | 20 | Payment token identifier for the MDES or VTS Card. | Conditional | Omit |
| <LocDate> | YYYY-MM-  DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

#### Payment Token Get Res Info

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <Creator> | AN | 1 | 10 | Name of the system or process that created the token (e.g., MC-MDES and VISA-T). | Omit | Mandatory |
| <Creator\_PAN\_Ref> | AN | 1 | 48 | The token creator's unique reference to the linked card. | Omit | Mandatory |
| <Creator\_Token\_Ref> | AN | 1 | 48 | The token creator's unique reference for this payment token. (Mastercard Token Unique Reference (TUR) and Visa Token reference ID.) | Omit | Mandatory |
| <PANT> | N | 16 | 19 | PAN for the card linked to the MDES or VTS card. | Omit | Mandatory |
| <Payment\_Token > | N | 16 | 19 | Payment token Device PAN for the MDES or VTS card. | Omit | Mandatory |
| <Payment\_Token\_ExpDate > | Date | 10 | 10 | Expiry date of the payment token. | Omit | Optional |
| <Payment\_Token\_ID> | N | 1 | 20 | Payment token identifier for the MDES or VTS card. | Omit | Mandatory |
| <Payment\_Token\_Type > | AN | 1 | 2 | Payment token type. See [Payment Token Types](../Reference/Payment_Token_Types.htm). | Omit | Mandatory |
| <Wallet\_ID> | AN | 1 | 10 | Name of the wallet provider this payment token uses (For example: APPLE, ANDROID, SAMSUNG, MRCHTOKEN). | Omit | Mandatory |
| <gps\_status> | N | 2 | 2 | The Thredd status of the payment token for transacting. See [Status Codes](../Reference/Status_Codes.htm). | Omit | Mandatory |
| <Tokenised\_Datetime> | DateTime | 19 | 19 | Date and time when tokenised, in the format: *yyyy-mm-ddhhmmss*. | Omit | Optional |
| <Tokenised\_Status> | AN | 1 | 1 | Tokenised status of this payment token: U = unknown; 0 = not tokenised; 1=tokenised. | Omit | Mandatory |
| <Txn\_Status> | AN | 1 | 1 | Status of the payment token as received from the payment token creator (normally Visa or Mastercard). After tokenisation, this is not changed by Thredd.  A = Active  D = Deleted (once in this status, it is normally never changed)  I = Inactive  N = Not Tokenised  P = Pending  S = Suspended  U = Unknown  X = Deactivated | Omit | Mandatory |
| <Txn\_Status\_Actor> | AN | 1 | 10 | Indicates which system last changed the transaction status. | Omit | Mandatory |
| <Txn\_Status\_Change\_Datetime> | DateTime | 16 | 16 | Date and time that the transaction status was last changed. In the format: *yyyy-mm-ddhhmmss*. | Omit | Mandatory |
| <Accepted\_Terms\_Date\_GMT> | DateTime | 16 | 16 | Date (in GMT) that terms and conditions were accepted by the cardholder (as received from the network). | Omit | Mandatory |
| <Accepted\_Terms\_Version> | AN | 1 | 32 | Version of the terms and conditions which were accepted by the cardholder  (as received from the network). | Omit | Mandatory |
| <Auth\_Datetime> | DateTime | 16 | 16 | Date and time when the tokenisation request was last responded to. | Omit | Mandatory |
| <Auth\_Decision> | AN | 1 | 1 | Final tokenisation decision:  U = unknown  0 = approve digitisation request  A = approve digitisation request (with additional authentication). | Omit | Mandatory |
| <Auth\_RSPSRC> | AN | 10 | 10 | Name of the system or process that approved the tokenisation (e.g., MC-MDES and ISSUER). | Omit | Mandatory |
| <Auth\_Status> | AN | 1 | 1 | Status of the authorisation to digitise this payment token:  U = unknown  0 = approve digitisation request  A = approve digitisation request (with additional authentication)  1 = decline digitisation request  **Note**: this is not the same as a transaction authorisation. | Omit | Mandatory |
| <Digitisation\_Ref> | AN | 1 | 64 | Unique reference (per `payment_token_issuer_id`) which all digitisation messages use, to link them together. | Omit | Mandatory |
| <Wallet\_Account\_Score> | N | 1 | 1 | Risk score for the account, received from the wallet provider during digitisation:  1 = highest risk; 2 = higher risk  3 = neutral; 4 = lower risk; 5 = least risk | Omit | Mandatory |
| <Wallet\_Device\_Score> | N | 1 | 1 | Risk score for the device received from the wallet provider during digitisation:  1 = highest risk; 2 = higher risk  3 = neutral; 4 = lower risk; 5 = least risk | Omit | Mandatory |
| <Wallet\_Reasons> | AN | 0 | 24 | Wallet service provider tokenization recommendation reason codes. This field can be null. See [Wallet Tokenisation Reason Codes](../Reference/Wallet_Tokenisation_Reason_Codes.htm). | Omit | Optional. |
| <Activation\_Code> | AN | 1 | 40 | Activation code to be sent directly to the cardholder to activate this payment token. | Omit | Mandatory |
| <Activation\_Code\_Expdate | DateTime | 16 | 16 | Date and time when the activation code expires, in GMT (UTC) in the format: *yyyy-mm-ddhhmmss*. | Omit | Mandatory |
| <Activation\_Method> | N | 1 | 1 | Which activation method was used:  0 = none;  1 = SMS to mobile phone;  2 = email;  3 = cardholder called an automated call centre;  4 = cardholder called a human call centre;  5 = website;  6 = mobile application;  7 = voice phone call | Omit | Mandatory |
| <Device\_ID> | AN | 1 | 48 | Unique ID of the secure element in the device. | Omit | Mandatory |
| <Device\_IP> | AN | 1 | 15 | IP address (full or last part only) of the device at time of binding / digitisation. | Omit | Mandatory |
| <Device\_Lang2> | AN | 1 | 2 | Device language code as ISO 639-1 (2 letter lowercase) code. | Omit | Mandatory |
| <Device\_Latitude> | N | 1 | 3 | Device latitude in degrees at time of digitisation request:  -90 (south pole) to +90 (north pole). +ve=North, -ve=South (from equator). Example: +63.2 = North 63.2 degrees, -82.6 = South 82.6 degrees. | Omit | Mandatory |
| <Device\_Longitude> | N | 1 | 3 | Device longitude in degrees at time of digitisation request: -180 to +180; +ve = East, -ve = West (of Greenwich). Example: 176.2 = East 176.2 degrees, -98.5 = West 98.5 degrees. | Omit | Mandatory |
| <Device\_Name> | AN | 1 | 20 | Name the cardholder assigned to the device in the wallet. | Omit | Mandatory |
| <Device\_Tel\_Num> | AN | 1 | 15 | Device telephone number (full or last part only). | Omit | Mandatory |
| <Device\_Type> | AN | 1 | 1 | The type of device used at the  terminal. See [Device Types](../Reference/Device_Types.htm). | Omit | Mandatory |
| <FirstName> | AN | 1 | 40 | Cardholder's first name as provided by the wallet provider during digitisation. May not be provided, or just the initial letter. | Omit | Mandatory |
| <LastName> | AN | 1 | 40 | Cardholder's last name as provided by wallet provider during digitisation. May not be provided, or just the initial letter. | Omit | Mandatory |
| <Wallet\_Account\_Hash> | AN | 1 | 64 | Wallet provider hash of account details (optional)or PBKDF2 hash of the cardholderâs account ID with the wallet provider. | Omit | Mandatory |

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
      <hyp:Ws_Payment_Token_Get>  
         <hyp:WSID>202112345678967890</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>2</hyp:TxnCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:DPAN>0987654321012</hyp:DPAN>  
         <hyp:Payment_Token_ID></hyp:Payment_Token_ID>  
         <hyp:LocDate>2017-01-01</hyp:LocDate>  
         <hyp:LocTime>123456</hyp:LocTime>  
      </hyp:Ws_Payment_Token_Get>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Payment_Token_GetResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Payment_Token_GetResult>  
            <WSID>202112345678967890</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>2</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <PaymentTokenGetResInfo>  
               <PaymentTokenGetResInfo>  
                  <Creator>PMT</Creator>  
                  <Creator_PAN_Ref/>  
                  <Creator_Token_Ref/>  
                  <PANT>1234567890123456</PANT>  
                  <Payment_Token>*****1234</Payment_Token>  
                  <Payment_Token_ExpDate/>  
                  <Payment_Token_ID>2</Payment_Token_ID>  
                  <Payment_Token_Type>C</Payment_Token_Type>  
                  <Wallet_ID>APPLE</Wallet_ID>  
                  <GPS_Status>00</GPS_Status>  
                  <Tokenised_Datetime/>  
                  <Tokenised_Status>1</Tokenised_Status>  
                  <Txn_Status>X</Txn_Status>  
                  <Txn_Status_Actor></Txn_Status_Actor>  
                  <Txn_Status_Change_Datetime/>  
                  <Accepted_Terms_Date_GMT/>  
                  <Accepted_Terms_Version/>  
                  <Auth_Datetime/>  
                  <Auth_Decision/>  
                  <Auth_RSPSRC/>  
                  <Auth_Status>1</Auth_Status>  
                  <Digitisation_Ref>11111111111111</Digitisation_Ref>  
                  <Wallet_Account_Score/>  
                  <Wallet_Device_Score/>  
                  <Wallet_Reasons/>  
                  <Activation_Code/>  
                  <Activation_Code_Expdate/>  
                  <Activation_Method/>  
                  <Device_ID/>  
                  <Device_IP/>  
                  <Device_Lang2/>  
                  <Device_Latitude/>  
                  <Device_Longitude/>  
                  <Device_Name/>  
                  <Device_Tel_Num/>  
                  <Device_Type>M</Device_Type>  
                  <FirstName/>  
                  <LastName/>  
                  <Wallet_Account_Hash/>  
               </PaymentTokenGetResInfo>  
            </PaymentTokenGetResInfo>  
            <LocDate>2017-01-01</LocDate>  
            <LocTime>123456</LocTime>  
            <SysDate>2017-11-17</SysDate>  
            <ActionCode>000</ActionCode>  
         </Ws_Payment_Token_GetResult>  
      </Ws_Payment_Token_GetResponse>  
   </soap:Body>  
</soap:Envelope>
```