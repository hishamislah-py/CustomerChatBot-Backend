# Customer Enquiry

API: `Ws_Customer_Enquiry` and `Ws_Customer_Enquiry_V2`

This web service returns the list of cards associated with a customer name. It does not return the details of archived cards.

Thredd recommend you use V2 of this service, which provides additional request and response parameters. V2 returns all cards linked to a specified `<PublicToken>`or `<CustAccount>` including secondary cards. See below.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value 4. | Mandatory | Mandatory |
| <ClientCode> | AN | 1 | 64 | User ID of the customer using the service. Only applicable to systems using member logins. Returned in the response if present in the request. **Note**: Legacy field. Not used.  Removed in V2 of service | Conditional | Conditional |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<ClientCode>` or `<accno>` are not provided. | Optional | Omit |
| <AccNo> | AN | 1 | 28 | Account number of the card. Mandatory if neither `<PublicToken>` nor `<PAN>` are provided. Returned in the response if present in the request.  Removed in V2 of service | Conditional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token, Mandatory in request if `<PAN>` and `<accno>` are not present. Mandatory in the response. | Conditional | Mandatory |
| <CustAccount> | AN | 1 | 25 | Cardholder account number or reference number. You can use this reference to find the cards linked to a cardholder. Also displayed in Smart Client and in Thredd Portal as *Customer Reference*.  Only available in V2 of the service | Omit | Optional |
| <CurrCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the currency (e.g. EUR). | Conditional | Conditional |
| <CardList> | - | - | - | See [Card List](#Card) below. | Omit | Optional |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <ItemSrc> | N | 1 | 5 | Source field to define alternate fees. Legacy field for information purposes only; see [Item Source Types.](../Reference/Item_Source_Types.htm) Suggest using 0. | Mandatory | Omit |
| <SysDate> | YYYY-MM\_DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |

#### Card List

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PAN> | AN | 14 | 19 | Card Number. Unique card identifier. | Omit | Mandatory |
| <ExpDate> | YYYY-MM\_DD | 10 | 10 | Expiry date of the card in *YYYY-MM-DD* format. | Omit | Mandatory |
| <CurCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the currency (e.g. EUR). | Omit | Mandatory |
| <StatCode> | AN | 2 | 2 | The status code of the card. See [Status Codes](../Reference/Status_Codes.htm). | Omit | Mandatory |
| <CrdProduct> | AN | 4 | 5 | The identifier of the card product, or `Product ID`, within Thredd. For details, check with your Implementation Manager. | Omit | Mandatory |
| <Program> | AN | 1 | 6 | The ID of the [ProgramClosed Logical grouping of your products set up in Smart Client. This is setup with whatever the customer (issuer or program manager) wants. Can be viewed in reports or via the web services API and may also be sent to the card manufacturer.](#) this card belongs to. | Omit | Optional |
| <DesignRef> | AN | 1 | 50 | Predefined design reference code associated with the card, also known as [PRODUCT\_REFClosed The predefined reference code associated with the card, which is included in the XML file sent to the card manufacturer. This field is called the <ProductRef> on ws\_create\_card and the <DesignRef> on ws\_customer\_enquiry and ws\_customer\_enquiry\_v2](#). | Omit | Optional |
| <AvlBal> | D | 1 | 20 | The current balance on the card account. This includes all financial transactions and outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <LastName> | AN | 1 | 100 | Cardholderâs last name. | Omit | Mandatory |
| <FirstName> | AN | 1 | 100 | Cardholderâs first name. | Omit | Mandatory |
| <EmbossName> | AN | 1 | 51 | Name embossed on the card. | Omit | Mandatory |
| <BlkAmt> | D | 1 | 20 | Amount of funds blocked on the card account as a result of all outstanding authorisations. The balance amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Omit | Mandatory |
| <CustType> | D | 1 | 1 | Identifies the owner of the card: 0 = primary customer; 1 = additional customer (authorised user).  Legacy field, no longer used." | Omit | Mandatory |
| <PaymentTokenUsageGroup> | AN | 1 | 50 | The unique 3-digit numeric code assigned to the payment token usage group at time of creation - plus a description of the payment token usage group. For example: â123-Company XYZ Full VDEPâ. For details, check with your Implementation Manager. | Omit | Mandatory |
| **Note**: Fields listed below are only available in V2 of the web service | | | | | | |
| <PublicToken> | AN | 1 | 9 | Thredd 9-digit public token of the card. | Omit | Mandatory |
| <Primary> | AN | 1 | 1 | Indicates if the card is the Primary card. | Omit | Mandatory |
| <IsLive> | N | 1 | 1 | Specifies whether the card is active or not. 1 or True = Active; 0 or False = Not Active. | Omit | Mandatory |
| <scheme> | AN | 1 | 50 | The cardâs [Thredd schemeClosed The name of the high-level product type set up in Thredd, usually at a BIN level.](#). | Omit | Mandatory |
| <product> | AN | 1 | 50 | The name you give to your Thredd card product. This is stored in Smart Client. | Omit | Mandatory |
| <MaskedPAN> | AN | 14 | 19 | Card Number displayed as masked. i.e. 675926\*\*\*\*\*\*1234. | Omit | Mandatory |
| <StartDate> | AN | 5 | 5 | Start date printed on the card in the format *MM/YY*. | Omit | Mandatory |
| <EndDate> | AN | 5 | 5 | Physical end date printed on the card in the format *MM/YY*. | Omit | Mandatory |
| <LimitsGroup> | AN | 1 | 10 | Group code of the [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). | Omit | Mandatory |
| <MCCGroup> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). | Omit | Mandatory |
| <PERMSGroup> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). | Omit | Mandatory |
| <FeeGroup> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). | Omit | Mandatory |
| <SchedFeeGroup> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). | Omit | Mandatory |
| <WSFeeGroup> | AN | 1 | 10 | Group code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#). | Omit | Mandatory |
| <LinkageGroup> | AN | 1 | 10 | Group code of the [Card Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#). | Omit | Mandatory |
| <AuthCalendarGroup> | AN | 1 | 10 | Group code of the [Auth Calendar GroupClosed Controls the dates and times when authorisations on a card are allowed. You can use this option to control when the card can be used, for example, prevent usage on weekends or out of hours.](#). | Omit | Mandatory |
| <FXGroup> | AN | 1 | 10 | Group code of the [FX GroupClosed Controls the rates for FX currency conversions if the purchase currency is different from the card's currency.](#). | Omit | Mandatory |
| <ProductID> | N | 1 | 5 | Thredd Product ID. | Omit | Mandatory |
| <ProductRef> | AN | 1 | 50 | The physical card design reference as used by the Card Manufacturer. Identifies the *PRODUCT\_REF* field in the XML file sent to the card manufacturer. | Omit | Mandatory |

#### Request (v1)

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
      <hyp:Ws_Customer_Enquiry>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>4</hyp:TxnCode>  
         <hyp:ClientCode></hyp:ClientCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:AccNo></hyp:AccNo>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:CurrCode>GBP</hyp:CurrCode>  
         <hyp:LocDate>2013-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:ItemSrc>2</hyp:ItemSrc>  
      </hyp:Ws_Customer_Enquiry>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response (v1)

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Customer_EnquiryResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Customer_EnquiryResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>4</TxnCode>  
            <ClientCode/>  
            <PublicToken>123456789</PublicToken>  
            <AccNo>1234567891234567</AccNo>  
            <CurCode>GBP</CurCode>  
            <LocDate>2013-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2013-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <Cards>  
               <CardList>  
                  <PAN>530823******1234</PAN>  
                  <ExpDate>2015-03-31</ExpDate>  
                  <CurCode>GBP</CurCode>  
                  <StatCode>00</StatCode>  
                  <CrdProduct>MCRD</CrdProduct>  
                  <Program>GPSCRU2C</Program>  
                  <DesignRef/>  
                  <EmbossName>GIFT CARD</EmbossName>  
                  <AvlBal>10</AvlBal>  
                  <BlkAmt>1</BlkAmt>  
                  <FirstName>Firstname</FirstName>  
                  <LastName>Lastname</LastName>  
                  <CustType/>  
               </CardList>  
            </Cards>  
         </Ws_Customer_EnquiryResult>  
      </Ws_Customer_EnquiryResponse>  
   </soap:Body>  
</soap:Envelope>
```

#### Request (V2)

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
      <hyp:Ws_Customer_Enquiry_V2>  
         <hyp:WSID>1233</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>4</hyp:TxnCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:CustAccount>ABCDE123</hyp:CustAccount>  
         <hyp:PublicToken></hyp:PublicToken>  
         <hyp:CurrCode>GBP</hyp:CurrCode>  
         <hyp:LocDate>2015-09-02</hyp:LocDate>  
         <hyp:LocTime>1610</hyp:LocTime>  
         <hyp:ItemSrc>1</hyp:ItemSrc>  
      </hyp:Ws_Customer_Enquiry_V2>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response (v2)

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Customer_Enquiry_V2Response xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Customer_Enquiry_V2Result>  
            <WSID>123</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>4</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <CustAccount>ABCDE123</CustAccount>  
            <CurCode>GBP</CurCode>  
            <LocDate>2021-09-02</LocDate>  
            <LocTime>1610</LocTime>  
            <SysDate>2021-09-02</SysDate>  
            <ActionCode>000</ActionCode>  
            <Cards>  
               <CardList2>  
                  <PAN>675926******6791</PAN>  
                  <ExpDate>2025-04-30</ExpDate>  
                  <CurCode>GBP</CurCode>  
                  <StatCode>00</StatCode>  
                  <CrdProduct>MCRD</CrdProduct>  
                  <Program>9876</Program>  
                  <DesignRef>Your product name here</DesignRef>  
                  <EmbossName>JOHN SMITH</EmbossName>  
                  <AvlBal>33.11</AvlBal>  
                  <BlkAmt>0</BlkAmt>  
                  <FirstName>John</FirstName>  
                  <LastName>Smith</LastName>  
                  <CustType/>  
                  <PublicToken>123456789</PublicToken>  
                  <Primary>Y</Primary>  
                  <IsLive>1</IsLive>  
                  <Scheme>Your Scheme Name here</Scheme>  
                  <Product> Your product name here </Product>  
                  <MCCGroup>PMT-MCC-01</MCCGroup>  
                  <LimitGroup>PMT-VL-002</LimitGroup>  
                  <PERMSGroup>PMT-CU-002</PERMSGroup>  
                  <FeeGroup>PMT-FEE-01</FeeGroup>  
                  <SchedFeeGroup>PMT-SFG-02</SchedFeeGroup>  
                  <WsFeeGroup>PMT-WSG-09</WsFeeGroup>  
                  <LinkageGroup/>  
                  <PrimaryToken>123456789</PrimaryToken>  
                  <MaskedPAN>675926******6791</MaskedPAN>  
                  <ProductID>9876</ProductID>  
                  <ProductRef>PROGRAM11</ProductRef>  
  <PaymentTokenUsageGroup></PaymentTokenUsageGroup>  
               </CardList2>  
            </Cards>  
         </Ws_Customer_Enquiry_V2Result>  
      </Ws_Customer_Enquiry_V2Response>  
   </soap:Body>  
</soap:Envelope>
```