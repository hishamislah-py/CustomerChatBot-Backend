# MVC Unload

API: `Ws_MVCUnload`

This web service allows customers to unload back to a [Master Virtual Cards![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd virtual card that is restricted to loading and unloading to a physical card and cannot be used for e-commerce or in-store transactions.
An MVC is used to reflect the value of the âactualâ money in the Issuer's bank account. An MVC guarantees that the load is limited to the amount prefunded (i.e. loaded onto MVC) and gives the Programme Manager the ability to distribute funds immediately rather than having to wait for notification of each individual load into the Issuer Bank account.](#) (MVC) only.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <MVCToken> | N | 1 | 9 | The MVC cardâs public token. | Mandatory | Mandatory |
| <NewToken> | N | 1 | 9 | The public token to where funds should be transferred to. | Mandatory | Mandatory |
| <AmtTxn> | D | 1 | 20 | The requested amount to transfer. If not specified, the full card balance is transferred.The actual amount transferred is returned in the response. The amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Com | Mandatory |
| <CurCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217) for the currency to load (e.g. EUR). This must match the cardâs currency or the action fails (**Note**: For a Multi-FX card, the card can be loaded in any of the card's currencies). If not provided, then the card uses its billing currency. See [Currency Codes](../Reference/Currency_Codes.htm). Must be supplied in the request if an `<AmtTxn>` is specified. | Conditional | Mandatory |
| <LoadedBy> | AN | 1 | 30 | User who loaded the card. | Optional | Omit |
| <LoadSrc> | AN | 1 | 3 | The source of the load request for determining the fee of the load, if applicable. If omitted, defaults to 14 âUnknownâ. See [Load Sources](../Reference/Load_Sources.htm).The source of the transfer request. If omitted, defaults to 14 âUnknownâ. | Optional | Omit |
| <Description> | AN\*\* | 1 | 150 | Description of the load. If supplied, appears in the `<description>` tag of a response to a card or account query. See [Card Statement (V1)](Card_Statement_v1.htm). | Optional | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <AvlBal> | D | 1 | 20 | The current balance on the card account. This includes all financial transactions and outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <BlkAmt> | D | 1 | 20 | Amount of funds blocked on the card account as a result of all outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <ItemID> | AN | 1 | 20 | The unique item ID for this Card Transfer. The ID returned is the ID relating to the âunloadâ leg of the transfer, that is, the unload from the MVC.. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [MVC Action Codes](../Reference/Action_Codes.htm#MVC). | Omit | Mandatory |

\*\* Some formatting may be done on this string, see [String Cleaning and Approved Characters](../Reference/String_Cleaning.htm).

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
      <hyp:Ws_MVCUnload>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:MVCToken>102530687</hyp:MVCToken>  
         <hyp:NewToken>102531699</hyp:NewToken>  
         <hyp:AmtTxn>10</hyp:AmtTxn>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:LoadedBy><span class="mc-variable General.BrandName variable">Thredd</span> USER</hyp:LoadedBy>  
         <hyp:LoadSrc></hyp:LoadSrc>  
      </hyp:Ws_MVCUnload>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_MVCUnloadResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_MVCUnloadResult>  
            <IssCode>PMT</IssCode>  
            <MVCToken>102530687</MVCToken>  
            <NewToken>102531699</NewToken>  
            <SysDate>2021-02-27</SysDate>  
            <ActionCode>000</ActionCode>  
            <AvlBal>68</AvlBal>  
            <BlkAmt>0</BlkAmt>  
            <AmtTxn>10</AmtTxn>  
            <CurCode>GBP</CurCode>  
            <ItemID>2291733913</ItemID>  
         </Ws_MVCUnloadResult>  
      </Ws_MVCUnloadResponse>  
   </soap:Body>  
</soap:Envelope>
```