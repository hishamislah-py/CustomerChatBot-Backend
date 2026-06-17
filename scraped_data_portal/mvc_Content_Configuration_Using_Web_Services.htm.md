# 4 Using Thredd Web Services (SOAP)

This section describes how to use the Thredd SOAP web services API to create and manage your MVCs.

Thredd includes SOAP-based APIs specific to MVCs, for example, `Ws_Activate_MVCLoad`. However, using these APIs is not mandatory, as you can use APIs that are generic across all card product, such as `Ws_CreateCards`, `Ws_Load` and `Ws_Unload`.

## 4.1 Creating an MVC

To create an MVC, use the `Ws_CreateCard` SOAP web service with `CreateType` set to 4. You can use the web service to create an MVC as a separate product, or an MVC for the same card product. For more details, see [Create Card](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm).

You do not need to complete card fulfilment and other non-mandatory details when creating a card.

#### Example MVC Request

The following is a request for creating an MVC as a separate card product.

Note that you must include the following:

* The `WSID` , which must be unique for the request.
* The `IssCode` as assigned to you by Thredd.
* The `LocDate` and `LocTime` to state the precise date and time of the request.
* The `CreateType`, which must be set to 4 (indicating an MVC).
* The `ExpDate`, which must be blank.
* `ActivateNow` should be set to 0

[Copy](javascript:void(0);)

```
<hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_CreateCard>  
         <hyp:WSID>120120241234</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>10</hyp:TxnCode>  
         <hyp:ClientCode></hyp:ClientCode>  
         <hyp:Title></hyp:Title>  
         <hyp:LastName>Ken</hyp:LastName>  
         <hyp:FirstName>Davies</hyp:FirstName>  
         <hyp:Addrl1></hyp:Addrl1>  
         <hyp:Addrl2></hyp:Addrl2>  
         <hyp:Addrl3></hyp:Addrl3>  
         <hyp:City></hyp:City>  
         <hyp:PostCode></hyp:PostCode>  
         <hyp:Country></hyp:Country>  
         <hyp:Mobile></hyp:Mobile>  
         <hyp:CardDesign>1628</hyp:CardDesign>  
         <hyp:ExternalRef></hyp:ExternalRef>  
         <hyp:DOB></hyp:DOB>  
         <hyp:LocDate>2024-01-12</hyp:LocDate>  
         <hyp:LocTime>120100</hyp:LocTime>  
         <hyp:TerminalID></hyp:TerminalID>  
         <hyp:LoadValue>20</hyp:LoadValue>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:Reason></hyp:Reason>  
         <hyp:AccCode></hyp:AccCode>  
         <hyp:ItemSrc>0</hyp:ItemSrc>  
         <hyp:LoadFundsType>0</hyp:LoadFundsType>  
         <hyp:LoadSrc></hyp:LoadSrc>  
         <hyp:LoadFee>0</hyp:LoadFee>  
         <hyp:LoadedBy></hyp:LoadedBy>  
         <hyp:CreateImage>0</hyp:CreateImage>  
         <hyp:CreateType>4</hyp:CreateType>  
         <hyp:CustAccount>0</hyp:CustAccount>  
         <hyp:ActivateNow>0</hyp:ActivateNow>  
         <hyp:Source_desc></hyp:Source_desc>  
         <hyp:ExpDate></hyp:ExpDate>  
         <hyp:CardName></hyp:CardName>  
         <hyp:LimitsGroup></hyp:LimitsGroup>  
         <hyp:MCCGroup></hyp:MCCGroup>  
         <hyp:PERMSGroup></hyp:PERMSGroup>  
         <hyp:ProductRef></hyp:ProductRef>  
         <hyp:CarrierType></hyp:CarrierType>  
         <hyp:Fulfil1></hyp:Fulfil1>  
         <hyp:Fulfil2></hyp:Fulfil2>  
         <hyp:DelvMethod></hyp:DelvMethod>  
         <hyp:ThermalLine1></hyp:ThermalLine1>  
         <hyp:ThermalLine2></hyp:ThermalLine2>  
         <hyp:EmbossLine4></hyp:EmbossLine4>  
         <hyp:ImageId></hyp:ImageId>  
         <hyp:LogoFrontId></hyp:LogoFrontId>  
         <hyp:LogoBackId></hyp:LogoBackId>  
         <hyp:Replacement>0</hyp:Replacement>  
         <hyp:FeeGroup></hyp:FeeGroup>  
         <hyp:PrimaryToken></hyp:PrimaryToken>  
         <hyp:Delv_AddrL1></hyp:Delv_AddrL1>  
         <hyp:Delv_AddrL2></hyp:Delv_AddrL2>  
         <hyp:Delv_AddrL3></hyp:Delv_AddrL3>  
         <hyp:Delv_City></hyp:Delv_City>  
         <hyp:Delv_County></hyp:Delv_County>  
         <hyp:Delv_PostCode></hyp:Delv_PostCode>  
         <hyp:Delv_Country></hyp:Delv_Country>  
         <hyp:Delv_Code></hyp:Delv_Code>  
         <hyp:Lang></hyp:Lang>  
         <hyp:Sms_Required></hyp:Sms_Required>  
         <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
         <hyp:WSFeeGroup></hyp:WSFeeGroup>  
         <hyp:CardManufacturer></hyp:CardManufacturer>  
         <hyp:CoBrand></hyp:CoBrand>  
         <hyp:PublicToken></hyp:PublicToken>  
         <hyp:ExternalAuth></hyp:ExternalAuth>  
         <hyp:LinkageGroup></hyp:LinkageGroup>  
         <hyp:VanityName></hyp:VanityName>  
         <hyp:PBlock></hyp:PBlock>  
         <hyp:PINMailer></hyp:PINMailer>  
         <hyp:FxGroup></hyp:FxGroup>  
         <hyp:Email></hyp:Email>  
         <hyp:MailOrSMS></hyp:MailOrSMS>  
         <hyp:AuthCalendarGroup></hyp:AuthCalendarGroup>  
         <hyp:Quantity></hyp:Quantity>  
         <hyp:LoadToken></hyp:LoadToken>  
         <hyp:FeeWaiver></hyp:FeeWaiver>  
         <hyp:BlackList></hyp:BlackList>  
         <hyp:WhiteList></hyp:WhiteList>  
         <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
         <hyp:VirtualCardImage></hyp:VirtualCardImage>  
         <hyp:ImageSize></hyp:ImageSize>  
         <hyp:Url></hyp:Url>  
         <hyp:IsNonReloadable>0</hyp:IsNonReloadable>  
         <hyp:IsSingleUse>0</hyp:IsSingleUse>  
      </hyp:Ws_CreateCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following is a request for creating an MVC for the same card product. All the requirements for the fields in the request apply as per the above example. However, note the following:

* The `ExpDate` should be set to 8 years from creation.
* There must be a `LinkageGroup`, which is the same as the card product.

In this example, there is product with an `ExpDate` of 2031-12-31 (assuming a `LocDate` of 2023-12-31) and a `LinkageGroup` of GPSIXRSTST.

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>*******</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_CreateCard>  
         <hyp:WSID>15012027999</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>10</hyp:TxnCode>  
         <hyp:ClientCode></hyp:ClientCode>  
         <hyp:Title></hyp:Title>  
         <hyp:LastName>Ken</hyp:LastName>  
         <hyp:FirstName>Davies</hyp:FirstName>  
         <hyp:Addrl1></hyp:Addrl1>  
         <hyp:Addrl2></hyp:Addrl2>  
         <hyp:Addrl3></hyp:Addrl3>  
         <hyp:City></hyp:City>  
         <hyp:PostCode></hyp:PostCode>  
         <hyp:Country></hyp:Country>  
         <hyp:Mobile></hyp:Mobile>  
         <hyp:CardDesign>1628</hyp:CardDesign>  
         <hyp:ExternalRef></hyp:ExternalRef>  
         <hyp:DOB></hyp:DOB>  
         <hyp:LocDate>2023-12-21</hyp:LocDate>  
         <hyp:LocTime>120100</hyp:LocTime>  
         <hyp:TerminalID></hyp:TerminalID>  
         <hyp:LoadValue>20</hyp:LoadValue>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:Reason></hyp:Reason>  
         <hyp:AccCode></hyp:AccCode>  
         <hyp:ItemSrc>0</hyp:ItemSrc>  
         <hyp:LoadFundsType>0</hyp:LoadFundsType>  
         <hyp:LoadSrc></hyp:LoadSrc>  
         <hyp:LoadFee>0</hyp:LoadFee>  
         <hyp:LoadedBy></hyp:LoadedBy>  
         <hyp:CreateImage>0</hyp:CreateImage>  
         <hyp:CreateType>2</hyp:CreateType>  
         <hyp:CustAccount>0</hyp:CustAccount>  
         <hyp:ActivateNow>1</hyp:ActivateNow>  
         <hyp:Source_desc></hyp:Source_desc>  
         <hyp:ExpDate>2031-12-31</hyp:ExpDate>  
         <hyp:CardName></hyp:CardName>  
         <hyp:LimitsGroup></hyp:LimitsGroup>  
         <hyp:MCCGroup></hyp:MCCGroup>  
         <hyp:PERMSGroup></hyp:PERMSGroup>  
         <hyp:ProductRef></hyp:ProductRef>  
         <hyp:CarrierType></hyp:CarrierType>  
         <hyp:Fulfil1></hyp:Fulfil1>  
         <hyp:Fulfil2></hyp:Fulfil2>  
         <hyp:DelvMethod></hyp:DelvMethod>  
         <hyp:ThermalLine1></hyp:ThermalLine1>  
         <hyp:ThermalLine2></hyp:ThermalLine2>  
         <hyp:EmbossLine4></hyp:EmbossLine4>  
         <hyp:ImageId></hyp:ImageId>  
         <hyp:LogoFrontId></hyp:LogoFrontId>  
         <hyp:LogoBackId></hyp:LogoBackId>  
         <hyp:Replacement>0</hyp:Replacement>  
         <hyp:FeeGroup></hyp:FeeGroup>  
         <hyp:PrimaryToken></hyp:PrimaryToken>  
         <hyp:Delv_AddrL1></hyp:Delv_AddrL1>  
         <hyp:Delv_AddrL2></hyp:Delv_AddrL2>  
         <hyp:Delv_AddrL3></hyp:Delv_AddrL3>  
         <hyp:Delv_City></hyp:Delv_City>  
         <hyp:Delv_County></hyp:Delv_County>  
         <hyp:Delv_PostCode></hyp:Delv_PostCode>  
         <hyp:Delv_Country></hyp:Delv_Country>  
         <hyp:Delv_Code></hyp:Delv_Code>  
         <hyp:Lang></hyp:Lang>  
         <hyp:Sms_Required></hyp:Sms_Required>  
         <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
         <hyp:WSFeeGroup></hyp:WSFeeGroup>  
         <hyp:CardManufacturer></hyp:CardManufacturer>  
         <hyp:CoBrand></hyp:CoBrand>  
         <hyp:PublicToken></hyp:PublicToken>  
         <hyp:ExternalAuth></hyp:ExternalAuth>  
         <hyp:LinkageGroup>GPSIXRSTST</hyp:LinkageGroup>  
         <hyp:VanityName></hyp:VanityName>  
         <hyp:PBlock></hyp:PBlock>  
         <hyp:PINMailer></hyp:PINMailer>  
         <hyp:FxGroup></hyp:FxGroup>  
         <hyp:Email></hyp:Email>  
         <hyp:MailOrSMS></hyp:MailOrSMS>  
         <hyp:AuthCalendarGroup></hyp:AuthCalendarGroup>  
         <hyp:Quantity></hyp:Quantity>  
         <hyp:LoadToken></hyp:LoadToken>  
         <hyp:FeeWaiver></hyp:FeeWaiver>  
         <hyp:BlackList></hyp:BlackList>  
         <hyp:WhiteList></hyp:WhiteList>  
         <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
         <hyp:VirtualCardImage></hyp:VirtualCardImage>  
         <hyp:ImageSize></hyp:ImageSize>  
         <hyp:Url></hyp:Url>  
         <hyp:IsNonReloadable></hyp:IsNonReloadable>  
         <hyp:IsSingleUse></hyp:IsSingleUse>  
      </hyp:Ws_CreateCard>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Example Response

Thredd returns a `PublicToken` for the MVC in the response. You should use the `PublicToken` to link to an MVC. The following is an example response where the MVC is for the same card product.

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CreateCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CreateCardResult>  
            <WSID>15012028999</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>112366247</PublicToken>  
            <ExternalRef/>  
            <LocDate>2024-01-12</LocDate>  
            <LocTime>120100</LocTime>  
            <ItemID>6160057433</ItemID>  
            <ClientCode>0</ClientCode>  
            <SysDate>2024-01-15</SysDate>  
            <ActionCode>000</ActionCode>  
            <LoadValue>20.00</LoadValue>  
            <IsLive>true</IsLive>  
            <StartDate>01/24</StartDate>  
            <ExpDate>12/24</ExpDate>  
            <CVV>390</CVV>  
            <MaskedPAN>9999999465355698</MaskedPAN>  
            <WebServiceResult/>  
         </Ws_CreateCardResult>  
      </Ws_CreateCardResponse>  
   </soap:Body>  
</soap:Envelope>
```

## 4.2 Loading an MVC

Loading allows funds to be available on an MVC. However, you can also use an MVC to load funds for a physical or virtual card. For further details on using these Thredd API web services, see the [Web Services Guide](https://docs.thredd.ai/webservices/Content/Home.htm).

#### Load an MVC

You use `Ws_Load` to load an MVC with funds. If you have loaded funds already, you can also use this web service to top-up an initial amount. For more details, see [Load](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Load.htm). Note the following:

* You must include the `PublicToken` of the MPC.
* You set the transaction code (`TxnCode`) to 1 or 20.

The following is an example request:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_Load>  
         <hyp:WSID>202418011234578</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>20</hyp:TxnCode>  
         <hyp:ClientCode></hyp:ClientCode>  
         <hyp:AuthType>1</hyp:AuthType>  
         <hyp:PAN></hyp:PAN>  
         <hyp:Track2></hyp:Track2>  
         <hyp:PublicToken>112367416</hyp:PublicToken>  
         <hyp:DOB></hyp:DOB>  
         <hyp:CVV></hyp:CVV>  
         <hyp:AccCode></hyp:AccCode>  
         <hyp:LastName></hyp:LastName>  
         <hyp:LocDate>2024-01-18</hyp:LocDate>  
         <hyp:LocTime>121100</hyp:LocTime>  
         <hyp:TerminalID></hyp:TerminalID>  
         <hyp:LoadValue>60</hyp:LoadValue>  
         <hyp:CurrCode>GBP</hyp:CurrCode>  
         <hyp:LoadFundsType>3</hyp:LoadFundsType>  
         <hyp:LoadSrc>2</hyp:LoadSrc>  
         <hyp:LoadFee>0</hyp:LoadFee>  
         <hyp:SecID>0</hyp:SecID>  
         <hyp:SecVal></hyp:SecVal>  
         <hyp:SecValPos>0</hyp:SecValPos>  
         <hyp:LoadedBy>Ken</hyp:LoadedBy>  
         <hyp:Description>MVC Load</hyp:Description>  
         <hyp:Sms_Required>0</hyp:Sms_Required>  
         <hyp:BrnCode></hyp:BrnCode>  
         <hyp:Note>MVC_Load</hyp:Note>  
      </hyp:Ws_Load>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following is an example response:

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_LoadResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_LoadResult>  
            <WSID>202418011234578</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>20</TxnCode>  
            <PublicToken>112367416</PublicToken>  
            <LocDate>2024-01-18</LocDate>  
            <LocTime>121100</LocTime>  
            <ItemID>6160073972</ItemID>  
            <ClientCode/>  
            <SysDate>2024-01-18</SysDate>  
            <ActionCode>000</ActionCode>  
            <WebServiceResult/>  
         </Ws_LoadResult>  
      </Ws_LoadResponse>  
   </soap:Body>  
</soap:Envelope>
```

#### Activate a Separate Card

If you have created a card that is not yet activated, you can load funds into that card from an MVC. Once loaded, the card is activated. It is important to note that you are activating the physical and/or virtual card and not the MVC.

You use the `Ws_Activate_MVCLoad` endpoint (see [MVC Card Activation and Load](https://docs.thredd.ai/webservices/Content/Web_services_api/MVC_Card_Activation_and_Load.htm)). This is an MVC-specific API.

Note the following:

* The `PublicToken` in `Ws_Activate_MVCLoad` is the card that you want to activate.
* The `MVCToken` is the public token of the MVC.
* The card that you are loading must be inactive with `ActivateNow` set to 0.
* The request must include a load source and currency code (`LoadSrc` and `CurCode`).

The following is an example request:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_Activate_MVCLoad>  
         <hyp:WSID>2024180101238</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>10</hyp:TxnCode>  
         <hyp:Title></hyp:Title>  
         <hyp:LastName></hyp:LastName>  
         <hyp:FirstName></hyp:FirstName>  
         <hyp:Addrl1></hyp:Addrl1>  
         <hyp:Addrl2></hyp:Addrl2>  
         <hyp:City></hyp:City>  
         <hyp:PostCode></hyp:PostCode>  
         <hyp:Country></hyp:Country>  
         <hyp:ActMethod>6</hyp:ActMethod>  
         <hyp:AuthType>1</hyp:AuthType>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>112367030</hyp:PublicToken>  
         <hyp:DOB></hyp:DOB>  
         <hyp:CVV></hyp:CVV>  
         <hyp:AccCode></hyp:AccCode>  
         <hyp:LocDate>18012024</hyp:LocDate>  
         <hyp:LocTime>110200</hyp:LocTime>  
         <hyp:MVCPAN></hyp:MVCPAN>  
         <hyp:MVCToken>112366842</hyp:MVCToken>  
         <hyp:AmtTxn>10</hyp:AmtTxn>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:LoadSrc>30</hyp:LoadSrc>  
         <hyp:LoadedBy></hyp:LoadedBy>  
         <hyp:Description></hyp:Description>  
         <hyp:FeeWaiver></hyp:FeeWaiver>  
         <hyp:BrnCode></hyp:BrnCode>  
         <hyp:ActivateOrNot>1</hyp:ActivateOrNot>  
         <hyp:ExpDate></hyp:ExpDate>  
         <hyp:ItemSrc>0</hyp:ItemSrc>  
         <hyp:SMSBalance>0</hyp:SMSBalance>  
      </hyp:Ws_Activate_MVCLoad>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following is an example response:

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Activate_MVCLoadResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Activate_MVCLoadResult>  
            <WSID>2024180101238</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>112367030</PublicToken>  
            <MVCToken>112366842</MVCToken>  
            <LocDate>18012024</LocDate>  
            <LocTime>110200</LocTime>  
            <AmtTxn>10.00</AmtTxn>  
            <CurCode>GBP</CurCode>  
            <IsLive>true</IsLive>  
            <AvlBal>30.00</AvlBal>  
            <BlkAmt>0.00</BlkAmt>  
            <ItemID>6160073922</ItemID>  
            <SysDate>2024-01-18</SysDate>  
            <ActionCode>000</ActionCode>  
         </Ws_Activate_MVCLoadResult>  
      </Ws_Activate_MVCLoadResponse>  
   </soap:Body>  
</soap:Envelope>
```

#### Load Funds from an MVC to a Card

You load funds to an active physical or virtual card linked to an MVC. You use the `Ws_MVCLoad` SOAP API web service (for more details see [MVC Load](https://docs.thredd.ai/webservices/Content/Web_services_api/MVC_Load.htm)). This is an MVC-specific API.

Note the following:

* The `MVCToken` is the token of the MVC.
* The `NewToken` is the card that receives the funds.
* There must be an amount and currency code (`AmtTxn` and `CurCode`)

The following is an example request:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_MVCLoad>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:MVCToken>114729737</hyp:MVCToken>  
         <hyp:NewToken>114729581</hyp:NewToken>  
         <hyp:AmtTxn>20</hyp:AmtTxn>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:LoadedBy>ken</hyp:LoadedBy>  
         <hyp:Description>transfer</hyp:Description>  
      </hyp:Ws_MVCLoad>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following is an example response:

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_MVCLoadResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_MVCLoadResult>  
            <IssCode>PMT</IssCode>  
            <MVCToken>114729737</MVCToken>  
            <NewToken>114729581</NewToken>  
            <SysDate>2024-01-18</SysDate>  
            <ActionCode>000</ActionCode>  
            <AvlBal>55.00</AvlBal>  
            <BlkAmt>0.00</BlkAmt>  
            <AmtTxn>20.00</AmtTxn>  
            <CurCode>GBP</CurCode>  
            <ItemID>6160074014</ItemID>  
         </Ws_MVCLoadResult>  
      </Ws_MVCLoadResponse>  
   </soap:Body>  
</soap:Envelope>
```

#### Unload Funds from a Card to an MVC

If required, you can unload funds back to an MVC from a physical or virtual card using `Ws_MVCUnload`. This is an MVC-specific API.

Note the following:

* The `MVCToken` is the token of the MVC.
* The `NewToken` is the card that sends the funds back.
* There must be an amount and currency code (`AmtTxn` and `CurCode`).

The following is an example request:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_MVCUnload>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:MVCToken>114729737</hyp:MVCToken>  
         <hyp:NewToken>114729581</hyp:NewToken>  
         <hyp:AmtTxn>5</hyp:AmtTxn>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:LoadedBy>ken</hyp:LoadedBy>  
         <hyp:LoadSrc>0</hyp:LoadSrc>  
         <hyp:Description>MVC unload</hyp:Description>  
      </hyp:Ws_MVCUnload>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following is an example response:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_MVCUnload>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:MVCToken>114729737</hyp:MVCToken>  
         <hyp:NewToken>114729581</hyp:NewToken>  
         <hyp:AmtTxn>5</hyp:AmtTxn>  
         <hyp:CurCode>GBP</hyp:CurCode>  
         <hyp:LoadedBy>ken</hyp:LoadedBy>  
         <hyp:LoadSrc>0</hyp:LoadSrc>  
         <hyp:Description>MVC unload</hyp:Description>  
      </hyp:Ws_MVCUnload>  
   </soapenv:Body>  
</soapenv:Envelope>
```

## 4.3 Linking Cards to an MVC (Primary and Secondary Cards)

You can link a secondary card to a primary card (the MVC). Using `Ws_CreateCard`, you can create the cardholder's cards (virtual or physical) which you link to the MVC. You must enter the 9-digit `PrimaryToken` value of your MVC. You need to provide the `PrimaryToken` , for example, 987654321, in the correct element:

[Copy](javascript:void(0);)

```
<hyp:PrimaryToken>987654321</hyp:PrimaryToken>
```

See [Create Card](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm) (`Ws_CreateCard`).

An MVC can have many secondary cards linked to it, however, it is not possible to cascade cards. Cascading cards is where there are two primary cards that are linked together. However, one of the primary cards is linked to secondary card(s).

## 4.4 Transferring a Balance

For transferring an amount from the MVC to a cardholderâs card, the Program Manager uses `Ws_BalanceTransfer`. An unload shows on the MVC and a load displays on the cardholder's card. The load to the cardholderâs cards is limited to the prefunded amount loaded on the MVC. The load onto the cardholderâs card is immediate and the amount is instantly available for use.

Note the following:

* The `PublicToken` is the MVC.
* The `NewToken` is the card that receives the funds.
* The `TxnCode` must be set to 7.
* There must be an amount and currency code (`AmtTxn` and `CurCode`). The below example shows 5 GBP as the balance to transfer.
* `LoadSource` must be set to 74 or 68.

The following shows an example request:

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>********</hyp:strUserName>  
         <hyp:strPassword>************</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_BalanceTransfer>  
         <hyp:WSID>202418011236</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:TxnCode>7</hyp:TxnCode>  
         <hyp:ClientCode></hyp:ClientCode>  
         <hyp:AuthType>1</hyp:AuthType>  
         <hyp:PAN></hyp:PAN>  
         <hyp:Track2></hyp:Track2>  
         <hyp:PublicToken>112363814</hyp:PublicToken>  
         <hyp:DOB></hyp:DOB>  
         <hyp:CVV></hyp:CVV>  
         <hyp:AccCode></hyp:AccCode>  
         <hyp:LastName>Davies</hyp:LastName>  
         <hyp:LocDate>2024-01-18</hyp:LocDate>  
         <hyp:LocTime>133400</hyp:LocTime>  
         <hyp:TerminalID></hyp:TerminalID>  
         <hyp:NewPAN></hyp:NewPAN>  
         <hyp:NewToken>112364353</hyp:NewToken>  
         <hyp:AmtTxn>5</hyp:AmtTxn>  
         <hyp:CurrCode>GBP</hyp:CurrCode>  
         <hyp:LoadSrc>68</hyp:LoadSrc>  
         <hyp:SecID>0</hyp:SecID>  
         <hyp:SecVal></hyp:SecVal>  
         <hyp:SecValPos>0</hyp:SecValPos>  
         <hyp:Description></hyp:Description>  
         <hyp:LoadedBy>Davies</hyp:LoadedBy>  
         <hyp:FeeWaiver>2</hyp:FeeWaiver>  
         <hyp:BrnCode></hyp:BrnCode>  
         <hyp:Fee>0</hyp:Fee>  
      </hyp:Ws_BalanceTransfer>  
   </soapenv:Body>  
</soapenv:Envelope>
```

The following shows an example response.

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_BalanceTransferResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_BalanceTransferResult>  
            <WSID>202418011236</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>7</TxnCode>  
            <PublicToken>112363814</PublicToken>  
            <LocDate>2024-01-18</LocDate>  
            <LocTime>133400</LocTime>  
            <NewPAN>9999999786646072</NewPAN>  
            <ClientCode>0</ClientCode>  
            <SysDate>2024-01-18</SysDate>  
            <ActionCode>000</ActionCode>  
            <AvlBal>15.00</AvlBal>  
            <BlkAmt>0.00</BlkAmt>  
            <AmtTxn>5.00</AmtTxn>  
            <CurCode>GBP</CurCode>  
            <ItemID>6160074146</ItemID>  
         </Ws_BalanceTransferResult>  
      </Ws_BalanceTransferResponse>  
   </soap:Body>  
</soap:Envelope>
```

Transferring a balance does not require a Card Linkage Group. This is because the cardholder is in control of the balance transfer to the card from the MVC. Setting up primary and secondary cards is also optional for a balance transfer.

## 4.5 Replacing a New Token

If the MVC needs to be replaced with a new token, you can add the `PublicToken` and the `NewToken` details to each of the virtual and physical cards using `Ws_link_cards`. This ensures that the cards are relinked to the MVC. In this web service example, you enter:

[Copy](javascript:void(0);)

```
<hyp:NewToken>112364353</hyp:NewToken>
```

for the card that the MVC links to.

For the MVC with the new token (to replace the old one), you enter the following:

[Copy](javascript:void(0);)

```
<hyp:PublicToken>112363814</hyp:PublicToken>
```

## 4.6 Viewing a List of Cards

For viewing a list of cards associated with an MVC, you use the `WS_Customer_Enquiry_V2` endpoint. A customer service representative typically checks for virtual or physical cards for an MVC. This endpoint requires you to enter the `PublicToken` for the MPC.

## 4.7 Search MVCs for Expiry

Using the `Ws_Get_Card_ExpireSoon` SOAP API web service, you can search for any MVCs that are to expire in the next month. This is provided that you have set an expiry date to one or more of your MVCs. For more details, see [`Cards Get Expiring Soon`](https://docs.thredd.ai/webservices/Content/Web_services_api/Cards_Get_Expiring_Soon.htm).

## 4.8 Load Sources

An Issuer (BIN sponsor) can see information on the load source within the various web services. Load sources are optional depending on what an Issuer wants to see reported as a load source or for applying a web service fee.

| Code | Name | Description |
| --- | --- | --- |
| 68 | Primary Card | This code is used when MVC and cardholder's cards are linked in a primary and secondary card relationship. The code allows you to transfer funds from the primary to the secondary card only. This is a mandatory setting for linked cards. |
| 74 | Master Virtual Card | This code lets you load an individual card from an MVC via balance transfer. |
| 76 | MVC Load | This code allows you to load an MVC using `Ws_Load`. |
| 77 | iMVC | This code lets you load an iMVC using `Ws_Load`. |

## 4.9 Charging Fees

If a Program Manager wants to charge fees for loading, the load source needs to be set up with the corresponding processing code for web service fees.

| Code | | Description | |
| --- | --- | --- | --- |
| 68 | Primary Card | 086: Fees | Primary card |
| 74 | Master Virtual Card | 074: Fees | Master Virtual Card |
| 76 | MVC Load | 076: Fees | MVC Load |
| 77 | iMVC Load | 077: Fees | iMVC Load |