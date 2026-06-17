# Card Renew

API: `Ws_Renew_Card`

This web service enables you to renew or replace a card. It combines the functionality of card replacement and card renewal. The replacement card has the same balance that the original card had at the time when the replacement card is activated. Any linked cards will still point to the correct card.

If you want to transfer the card balance immediately to the new card, and update any linked wallet/card payment tokens at the same time, then select one of the following [Renew Options](#Renew) (`<RenewOptions>`): 18,19,20,21,26 & 28.

If you are replacing the card with a physical card, then you need to activate the card. See [Card Activate](Card_Activate.htm).

When the new card is activated, Thredd changes the status of the old card to *62 restricted card*.

When a card is renewed, if you have enrolled the old card with 3D Secure credentials, then the new card is automatically enrolled with the same 3D Secure credentials. For details, see the 3D Secure Guide.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. Mandatory in response. Card number is displayed as masked (e.g., 675926\*\*\*\*\*\*1234).  If you are PCI compliant, the full PAN can be returned. Check with your Implementation Manager. | Conditional | Mandatory |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <RenewOptions> | N | 1 | 8 | See [Renew Options](#Renew) below. | Mandatory | Omit |
| <ExpDate> | AN | 10 | 10 | Expiry Date in *YYYY-MM-DD* format; this is forced to the last day of the given month. Mandatory if `<RenewOptions>` is 8, 10, 12, 26 or 28. | Conditional | Mandatory |
| <NewProductID> | N | 1 | 8 | Thredd Product ID for the new card. Mandatory if `<RenewOptions>` is 4, 5, 12, 20, 21 or 28. | Conditional | Omit |
| <SendSMS> | N | 1 | 1 | Whether an SMS is sent to the cardholder with the card's CVV. 1 = yes; 0 =No. The default is â0â. The SMS is configurable. | Mandatory | Omit |
| <MailOrSMS> | AN | 1 | 1 | The cardholder's preferred contact method. 0 = SMS; 1 = email. 2 = SMS and email. Default value is â0â. | Optional | Omit |
| <CreateImage> | N | 1 | 1 | Specifies whether to create a card image. 1= yes, 0 = No. Images are returned in the `<Image>` response parameter, encrypted by a pre-shared PGP encryption key. | Optional | Omit |
| <FeeWaiver> | N | 1 | 1 | Indicates whether to waive any web service fee set up on the system: 0 = No, 1=Yes. Default is 0. | Optional | Omit |
| <ProductRef> | AN | 1 | 50 | The physical card design reference as used by the Card Manufacturer. Identifies the *PRODUCT\_REF* field in the XML file sent to the card manufacturer. | Optional | Omit |
| <VirtualCardImage> | AN | 1 | 16 | The Image ID for the virtual image for the new card. You can set up Image IDs in [Smart ClientClosed Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#) in the **Image Master** and **Virtual Card Images** screens.**Note**: If you do not provide an image ID, the default virtual card image for the product is used. | Optional | Omit |
| <ImageSize> | N | 1 | 1 | The size of the virtual image: 1 = 100%; 2 = 200%; 3 = 300%; 4 = 400%; 5 = 500%. Default is 1. | Optional | Omit |
| <DelvMethod> | AN | 1 | 1 | The delivery method for the card. Options include:  0 = Standard delivery;  1 = Registered mail;  2 = Direct delivery;  3 = Customized DelvMethod 1;  4 = Customized DelvMethod 2;  5 = Customized DelvMethod 3;  6= Customized DelvMethod 4;  7 = Customized DelvMethod 5;  Default value is 0 | Optional | Omit |
| < CarrierType> | AN | 1 | 30 | The Carrier Product design reference as used by the Card Manufacturer. This is the letter onto which the card is attached when sent to the cardholder. Identifies the Carrier Product type of the Card Manufacturer. | Optional | Omit |
| <Url> | AN | 1 | 100 | This value is included in the Thredd Card Generation file, in the `<QRCode>` field. For example: *https://www.your-e-card.com/balance/2909680989632389*  For details, see the [Card Generation Interface Specifications](https://developer.globalprocessing.com/Card_Generation_Interface_Specification.htm). | Optional | Omit |
| <CVV> | AN | 3 | 3 | New card CVV. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Image> | Base 64 |  |  | [PGPClosed Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. uses PGP for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.](#)-encrypted image of the card. Requires configuration within Smart Client. Check with your Implementation Manager. | Omit | Conditional |
| EWALLETS |  |  |  | If you are renewing an eWallet, the response returns an EWALLET structure. | Omit | Conditional |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |

#### Renew Options

| Description |
| --- |
| 0 = No options turned on, produce a card identical to the cardholder's current card (used for damaged card replacement)  1 = Calculate a new expiry date.  2 = Use a new card number with same expiry as the replaced card.  3 = Use a new card number with new expiry.  4 = Use a new product with same expiry as replaced card.  5 = Use a new product with new expiry.  8 = Override normal expiry date calculation.  10 = Use new card number and override normal expiry date calculation.  12 = Use new product and override normal expiry date calculation.  18 = Immediate balance transfer and use a new card number with same expiry as the replaced card.  19 = Immediate balance transfer and use a new card number with new expiry.  20 = Immediate balance transfer and use a new product with same expiry as replaced card.  21 = Immediate balance transfer and use a new product with new expiry.  26 = Immediate balance transfer and use new card number and override normal expiry date calculation.  28 = Immediate balance transfer and use new product and override normal expiry date calculation.  **Note**: Do not choose Renew Options 0, 1 and 8 if the card status is 41, 43, 83, 98 or 99. |

#### EWALLET Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IDENTITY> | AN | 1 | 9 | The Thredd 16-digit public token. Mandatory in the response. | Omit | Mandatory |
| <CARDS> |  |  |  | See [CARDS Description](#CARDS) below. | Omit | Mandatory |
| <ACCOUNTS> |  |  |  | See [ACCOUNTS Description](#ACCOUNT) below; may occur multiple times. | Omit | Mandatory |

#### CARDS Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PAN> | AN | 1 | 9 | Cardâs physical PAN. | Omit | Mandatory |
| <CRDCURRCODE> | AN | 3 | 3 | 3-digit Alpha currency code. | Omit | Mandatory |
| <CRDPRODUCT> | AN | 1 | 50 | Thredd product type. | Omit | Mandatory |
| <CUSTCODE> | AN | 1 | 25 | Customer account number. Mandatory in the response if present. | Omit | Conditional |
| <PRIMARY> | AN | 1 | 1 | Indicates if the card is the Primary card. Default value is 'Y'. | Omit | Mandatory |
| <PROGRAMID> | AN | 1 | 50 | Cardâs program ID. | Omit | Mandatory |
| <STATCODE> | AN | 2 | 2 | The status code of the card. See [Status Codes](../Reference/Status_Codes.htm). | Omit | Mandatory |
| <EXPDATE> | AN | 10 | 10 | Expiry date of the card in *YYYY-MM-DD* format. | Omit | Mandatory |

#### ACCOUNTS Response Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <ACCNO> | AN | 1 | 9 | Account number of the card. | Omit | Mandatory |
| <ACCTYPE> | AN | 2 | 2 | Type of card account. See [Account Types](../Reference/Account_Types.htm). | Omit | Mandatory |
| <CURRCODE> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the cardholder's account (billing) currency. | Omit | Mandatory |
| <FINAMT> | D | 1 | 20 | Balance of the account, excluding blocked amount. | Omit | Mandatory |
| <BLKAMT> | D | 1 | 20 | Amount of funds blocked on the card account as a result of all outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <AMTAVL> | D | 1 | 20 | Balance of the card account. This includes all financials and outstanding authorisations. | Omit | Mandatory |

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
      <hyp:Ws_Renew_Card>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:RenewOptions>3</hyp:RenewOptions>  
         <hyp:ExpDate>2025-06-30</hyp:ExpDate>  
         <hyp:NewProductID></hyp:NewProductID>  
         <hyp:SendSMS>0</hyp:SendSMS>  
         <hyp:MailOrSMS></hyp:MailOrSMS>  
         <hyp:CreateImage>0</hyp:CreateImage>  
         <hyp:FeeWaiver></hyp:FeeWaiver>  
         <hyp:ProductRef></hyp:ProductRef>  
         <hyp:DelvMethod></hyp:DelvMethod>  
         <hyp:VirtualCardImage></hyp:VirtualCardImage>  
         <hyp:ImageSize></hyp:ImageSize>  
         <hyp:CarrierType>123456789012345678901234567890123</hyp:CarrierType>  
         <hyp:Url></hyp:Url>  
      </hyp:Ws_Renew_Card>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Renew_CardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Renew_CardResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <PAN>999999******1234</PAN>  
            <PublicToken>123456789</PublicToken>  
             <ExpDate>2025-06-30</ExpDate>  
            <ActionCode>000</ActionCode>  
            <CVV>404</CVV>  
            <WebServiceResult/>   
         </Ws_Renew_CardResult>         
      </Ws_Renew_CardResponse>  
   </soap:Body>  
</soap:Envelope>
```