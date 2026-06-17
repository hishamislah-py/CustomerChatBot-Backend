# Create Card with Agency Banking

API: `Ws_CreateCard_V2`

This web service creates a card which has a bank account linked to it, with Agency Banking features enabled. It will also upgrade an existing card to have banking features. This service applies only to programmes using Agency Banking.

Before using this web service, use `Ws_Banking_CreateCustomer` to register the customer and obtain the unique `CustomerID`. See [Register a Customer for Banking](Register_Customer_for_Banking.htm).

To replace a card, you must use the [Card Renew](Card_Renew.htm) web service (`Ws_Renew_Card`).

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Should be unique for every web service request sent | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. Default value 10. | Mandatory | Mandatory |
| <clientCode> | AN | 1 | 64 | User ID of the customer using the service. Only applicable to systems using member logins.  Returned in the response if present in the request | Optional | Conditional |
| <Title> | AN | 1 | 4 | Cardholder's title. If no delivery address is supplied it is also assumed to be the card purchaserâs title | Optional | Omit |
| <LastName> | AN | 1 | 30 | Cardholder's last name. If no delivery address is supplied it is also assumed to be the card purchaserâs last name | Conditional | Omit |
| <MiddleName> | AN | 1 | 100 | Cardholder's middle name. The `<MiddleName>` is not part of the `<EmbossName>` and therefore, does not check manufacture-approved characters. If a delivery address is not supplied, the cardholder's middle name will be the card purchaser's middle name. | Conditional | Omit |
| <FirstName> | AN | 1 | 30 | Cardholder's first name. If no delivery address is supplied it is also assumed to be the card purchaserâs first name  Mandatory if <lastName> is present. | Conditional | Omit |
| <Address1> | AN | 1 | 50 | Cardholder's address line 1. If no delivery address is supplied it is also assumed to be the card purchaserâs address line 1  Mandatory if âAddressâ fields are being specified | Conditional | Omit |
| <Address2> | AN | 1 | 50 | Cardholder's Address line 2. If no delivery address is supplied it is also assumed to be the card purchaserâs Address line 2. | Optional | Omit |
| <Address3> | AN | 1 | 35 | Cardholder's Address line 3. If no delivery address is supplied it is also assumed to be the card purchaserâs Address line 3. | Optional | Omit |
| <City> | AN | 1 | 50 | Cardholder's home city. If no delivery address is supplied it is also assumed to be the card purchaserâs home city  Mandatory if <addrL1> is present, and <postcode> is not present. | Conditional | Omit |
| <Postcode> | AN | 1 | 10 | Cardholder's home postcode. If no delivery address is supplied it is also assumed to be the card purchaserâs home postcode  Mandatory if <addrL1> is present, and <city> is not present.    Post code supports following characters only.  The Arabic numerals "0" to "9" Letters of the ISO basic Latin alphabet (A-Z, a-z) Spaces, hyphens(-). | Conditional | Omit |
| <ISOCountryCode> | AN | 1 | 3 | Cardholder's Country of Residence. This is represented as  ISO numeric country code e.g. 826 for UK.  Mandatory if <addrL1> is present. | Conditional | Omit |
| <Mobile> | AN | 1 | 15 | Cardholderâs mobile phone number (including dialing code if applicable). See [Processing of Telephone Numbers](../Reference/String_Cleaning.htm#Processi). | Optional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. The public token of the newly-created card will always be returned in the response. | Omit | Mandatory |
| <CardDesign> | AN | 1 | 8 | The Thredd `Product ID`. For details, check with your Implementation Manager. | Conditional | Omit |
| <ExternalRef> | AN | 1 | 30 | Enables you to add your own external customer reference. | Optional | Conditional |
| <DateOfBirth> | YYYY-MM-  DD | 10 | 10 | Date of Birth. | Optional | Omit |
| <AccCode> | AN | 1 | 6 | Access code. If provided, must be 6 digits, leading zeroes are acceptable.  Leave empty if not required.  Can be used to  set a code which is validated during activation e.g. via the IVR | Optional | Omit |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The current date | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The current time | Mandatory | Mandatory |
| <TerminalID> | AN | 1 | 15 | POS or other Terminal Identifier | Optional | Omit |
| <LoadValue> | D | 1 | 20 | Load value to put on card. If no load value is required, specify 0. | Mandatory | Mandatory |
| <CurCode> | AN | 3 | 3 | Currency of the amount to load as ISO Alpha code e.g. EUR This must match the cardâs currency or the action fails. Mandatory only when LoadValue is specified and not zero. | Conditional | Omit |
| <Reason> | AN | 1 | 60 | Reason for card status change.  Overrides default of âCard Activatedâ that is shown in card Processor | Optional | Omit |
| <ItemSrc> | N | 1 | 5 | Source field to define alternate fees. It is used in conjunction with existing fee server Item. See [Item Source Types](../Reference/Item_Source_Types.htm) | Mandatory | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The processing system date | Optional | Mandatory |
| <LoadFundsType> | AN | 1 | 3 | Payment method of funds for the load. See [Load Fund Types](../Reference/Load_Fund_Types.htm) | Optional | Omit |
| <LoadSrc> | AN | 1 | 3 | The source of the load request  [Load Sources](../Reference/Load_Sources.htm)..  If omitted, defaults to 14 âUnknownâ | Optional | Omit |
| <LoadFee> | D | 1 | 20 | Fixed fee amount charged to the card purchaser for handling the card purchase and load. If no Load Fee is required, specify 0. The LoadFee does not affect the card balance. It is only reported in the XML reports. | Mandatory | Omit |
| <LoadedBy> | AN | 1 | 30 | User who loads amount to the card | Optional | Omit |
| <CreateImage> | N | 1 | 1 | If this is 1 then generate an image for the card. If it is 0 then do not create the image. Images are returned in the âImageâ response parameter, encrypted by a pre-shared PGP encryption key. | Mandatory | Omit |
| <CreateType> | N | 1 | 1 | There are 4 possible values for the CreateType.   |  |  | | --- | --- | | Type | Description | | 1 | Create a virtual card for the customer with the given amount. | | 2 | Create physical card with the given amount. The web service also creates a card file and send the card file to the manufactures for activate the card later. | | 3 | Create a virtual card. Works in the same way as option 1. | | 4 | Create a Master Virtual Card which is a deposit account that can be used to load other cards from. |     Note: CreateType 1 also allows a virtual card to be converted to a physical card. | Mandatory | Omit |
| <CustAccount> | AN | 1 | 25 | Client reference for the Card. | Optional | Omit |
| <ActivateNow> | N | 1 | 1 | If it is 1 then card is activated, otherwise not.  When `<Quantity>` is greater than 1 then creation of `<Quantity>` numbers of identical cards triggers in a batch process that starts within minutes of the request. If `<ActivateNow>` is 1 in such requests then the issued tokens are sent to the customer with active flag ON otherwise not.    This parameter only takes effect if the request is for a new card. | Mandatory | Omit |
| <SourceDesc> | AN | 1 | 50 | Load source description, normally the address of the web site or the POS machine. | Optional | Omit |
| <StartDate> | AN | 5 | 5 | Physical start date printed on the card in format MM/YY. | Optional | Mandatory |
| <ExpDate> | YYYY-MM-DD | 10 | 10 | Card Physical Expiry date. If it is blank then update with the default expiry date otherwise update with the input value  The actual physical expiry is returned in MM/YY format. | Optional | Omit |
| <CVV> | AN | 3 | 3 | Card Verification Value, the 3-digit code printed on the back of the card. | Optional | Omit |
| <CardName> | AN | 1 | 27 | Cardâs Emboss name. This is an optional parameter. If present in the request then emboss name of card should be the given value. If itâs not available and <Firstname> and <Lastname> are available then <Title> + <Firstname> + <Lastname> is the emboss name. If all the above parameters are unavailable in the request then default emboss name remains as the emboss name. If a blank emboss name is required, then pass a single space character.  The list of allowed characters is:  abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ  0123456789  Some non-english characters i.e. âÃ¤Ã¶Ã¼ÃÃÃâ  â\â (backslash)  â-â (hyphen)  â^â (caret)  â.â (full stop)  â â (space character)  âââ (apostrophe) | Optional | Omit |
| <MaskedPAN> | AN | 14 | 19 | Card Number displayed as masked. i.e. 675926\*\*\*\*\*\*1234. N.B. The full PAN can be returned if required, ask for details. | Optional | Omit |
| <LimitsGroup> | AN | 1 | 10 | Group code of the group limit. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <MCCGroup> | AN | 1 | 10 | Group code of the MCC group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â. The MCC group allows the card to be linked to a list of Merchant Category Codes that the card is allowed to or conversely is NOT allowed to transact at. The MCCGroup is setup and configured via smart client. | Optional | Omit |
| <PERMSGroup> | AN | 1 | 10 | Group code of the Usage group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <FeeGroup> | AN | 1 | 10 | Group code of the Fee Group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <ScheduledFeeGroup> | AN | 1 | 10 | Group code of the Scheduled Fee Group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <WSFeeGroup> | AN | 1 | 10 | Group code of the Web Service Fee Group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â. WSFeeGroup allows the card to be linked to a set of Web Service fees that are already set up on the system. These fees can be configured and altered by using the smart client. | Optional | Omit |
| <FXGroup> | AN | 1 | 10 | Group code of the FX Fee Group. If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <ProductRef> | AN | 1 | 50 | Identifies Product. N.B. This is the Physical Card Design Reference as used by the card printer. | Optional | Omit |
| <CarrierType> | AN | 1 | 30 | Defines carrier product. N.B. This is the Carrier Product Design reference as used by the card printer. | Optional | Omit |
| <Fulfil1> | AN | 1 | 50 | Cardâs FULFIL1. Can be used for transferring extra information to be printed on the Carrier | Optional | Omit |
| <Fulfil2> | AN | 1 | 50 | Cardâs FULFIL2 Can be used for transferring extra information to be printed on the Carrier | Optional | Omit |
| <DelvMeth> | AN | 1 | 1 | The delivery method for the card:  0â Standard delivary  1â Registered mail  2â Direct delivery (Courier)  Default value is 0 - Standard delivery. | Optional | Omit |
| <ThermalLine1> | AN | 1 | 120 | Can be used for transferring extra information to be printed on the card. | Optional | Omit |
| <ThermalLine2> | AN | 1 | 70 | Can be used for transferring extra information to be printed on the card. | Optional | Omit |
| <Lang> | AN | 1 | 2 | Language to be used for Card Mailers.  Uses ISO 639-1 standard for two-character language codes e.g.:  En â English  Fr - French  Not all languages are available with all manufacturers, it depends on card manufacturer support.  Also used if bespoke SMS templates are set up | Optional | Omit |
| <EmbossLine4> | AN | 1 | 27 | Cardâs emboss\_line\_4. | Optional | Omit |
| <ImageID> | AN | 1 | 16 | Identifies the image file that will be printed on the face of the card. | Optional | Omit |
| <LogoFrontID> | AN | 1 | 30 | Identifies the logo file that will be printed on the face of the card. | Optional | Omit |
| <LogoBackID> | AN | 1 | 30 | Identifies the image file that will be printed on the back of the card, if supported. | Optional | Omit |
| <PrimaryToken> | AN | 16 | 19 | The primary cardâs public token. If it is blank then the newly created card is a primary card otherwise it is the secondary card in a primary/secondary relationship.  Cannot be the token of a card that is already linked as a secondary card. | Optional | Omit |
| <DelvAddrL1> | AN | 1 | 50 | Delivery address line 1.  Mandatory if âDelivery Addressâ fields are being specified. | Optional | Omit |
| <DelvAddrL2> | AN | 1 | 50 | Delivery Address line 2 | Optional | Omit |
| <DelvAddrL3> | AN | 1 | 50 | Delivery Address line 3 | Optional | Omit |
| <DelvCity> | AN | 1 | 50 | Delivery City.  Mandatory if <Delv\_AddrL1> is present, and <Delv\_PostCode> is not present. | Optional | Omit |
| <DelvPostcode> | AN | 1 | 10 | Delivery Post code.  Mandatory if <Delv\_AddrL1> is present, and <Delv\_City> is not present.    Delivery postcode supports following characters only.  The Arabic numerals "0" to "9" Letters of the ISO basic Latin alphabet (A-Z, a-z) Spaces, hyphens(-). | Optional | Omit |
| <DelvCounty> | AN | 1 | 20 | Delivery County | Optional | Omit |
| <DelvCountry> | AN | 1 | 3 | Delivery Country code.  ISO numeric code E.g. 826 for UK  Mandatory if <Delv\_AddrL1> is present. | Optional | Omit |
| <DelvCode> | AN | 1 | 12 | The delivery code for the card:  If specified, all cards with the same delivery code are to be sent together to the specified delivery address. | Optional | Omit |
| <SMSRequired> | AN | 1 | 1 | If it is 1 then sends an SMS to the customer with the cards CVV otherwise not. By default it is â1â.  If set to 0, no message â SMS or Email - is sent to the cardholder. | Optional | Omit |
| <IsLive> | N | 1 | 1 | Indicates the card in active or not.  1/True â Active  0/False â Not Active | Optional | Mandatory |
| <CardManufacturer> | AN | 1 | 50 | The manufacturer to send the card generation request to. If omitted, the default for the Scheme will be used.  Examples of valid choices are:  TCT  AllPay  GNC  Gemalto  Nitecrest  Exceet  Idemia | Optional | Omit |
| <CoBrand> | AN | 1 | 6 | The CoBrand code for the card. If supplied it will replace PROGRAMID in the Balance XML. | Optional | Omit |
| <ExternalAuth> | AN | 1 | 1 | External Authorisation flag. Possible values are:  0 â Do not set External Authorisation on  1 â Set External Authorisation  Empty value defaults to 0.  Not applicable if using EHI | Optional | Omit |
| <LinkageGroup> | AN | 1 | 10 | Group code of the Card Linkage Group. If this parameter is not supplied and this is a new card request then the default group for the cards product will be used. If the default group is not desired, it can be removed by passing a space character â â. | Optional | Omit |
| <VanityName> | AN | 1 | 32 | Vanity Name. Alternative form of title e.g. âCompany Directorâ | Optional | Omit |
| <PBlock> | AN | 4 | 12 | Initial value of PIN | Optional | Omit |
| <PINMailer> | AN | 1 | 1 | PIN Mailer:  0 -> Do not send PIN Mailer (default)  1 -> Do send PIN Mailer  If 1, Thredd sends instructions in the file to the manufacturer for them to create a PIN Mailer letter. | Optional | Omit |
| <Email> | AN | 1 | 50 | E-mail address of the cardholder | Optional | Omit |
| <MailOrSMS> | AN | 1 | 1 | Flag to choose the alert type.  0 = send alert SMS to the cardholder mobile.  1 = send e-mail alert to the cardholder mail address  2 = send SMS and e-mail.  Default value is â0â. | Optional | Omit |
| <AuthCalendarGroup> | AN | 1 | 10 | Group code of the Card Auth Calender Group. If this parameter is not supplied and this is a new card request then the default group for the cards product will be used. If the default group is not desired, it can be removed by passing a space character â â | Optional | Omit |
| <Quantity> | N | 1 | 5 | If specified, will trigger the creation of <Quantity> numbers of identical cards in a batch process that starts within minutes of the request. The issued tokens are sent to the customer in an xml file over SFTP. If the cards are physical, a manufacturer file is also sent to the printer. | Optional | Omit |
| <LoadToken> | N | 1 | 9 | If specified, LoadToken is the 9-digit Public Token of the (usually an MVC) card that the initial Load Amount is to be taken from. The load will show as an MVC Balance Transfer (Unload + Load) in smart client. | Optional | Omit |
| <RequiredBankingFeatures> | BankingFeatures |  |  | The required banking features that are required. You must pass in, *BankinInEnabled*, *BankingOutEnabled*, *DirectDebitInEnabled*, *DirectDebitOutEnabled*, *SEPAInEnabled*, *SEPAOutEnabled* and *CardEnabled*. Other features are optional. See [BankingFeatures](../Reference/Enums.htm#BankingF2). | Mandatory | Omit |
| <IsActive> | B |  |  | Setting this flag to true will create a physical card from the virtual card and the card will be instantly active allowing payments out via the banking functionality. | Mandatory | Omit |
| <CustomerID> | AN |  |  | The ID of the customer that this account is to be associated with. This can be obtained by calling `Ws_Banking_CreateCustomer`. | Optional | Omit |
| <PaymentTokenUsageGroup> | AN | 1 | 10 | Payment token usage group code.  **Note**: This is a numeric value, only digits 0-9 are valid. Leave empty if no group required. | Optional | Omit |
| <IsSingleUse> | AN | 1 | 5 | Enables you to specify whether the card is [single use onlyClosed Card which can only be used for a single transaction.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <IsNonReloadable> | AN | 1 | 5 | Enables you to specify whether the card is [non-reloadableClosed Card which is loaded with funds at the time of card creation, but cannot be reloaded after this.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <Url> | AN | 1 | 100 | This value is included in the Thredd Card Generation file, in the `<QRCode>` field. For example: *https://www.your-e-card.com/balance/2909680989632389*  For details, see the [Card Generation Interface Specifications](https://developer.globalprocessing.com/Card_Generation_Interface_Specification.htm). | Optional | Omit |
| <OOBAppURL> | AN | 1 | 2048 | Out Of Band app URL used in a 3D Secure authentication session. The Card Scheme (e.g., Mastercard) requires issuers using Out of Band/Biometric authentication to support the automatic redirection of cardholders from the merchant app to the authenticator app. OOBAppURL is the URL of this authenticator app. | Optional | Omit |
| <SortCode> | N | 6 | 6 | The sort code from the associated product that was supplied in the request. | Omit | Optional |
| <AccountNumber> | N | 8 | 8 | A unique account number is returned in the response. | Omit | Optional |
| <AccountName> | AN | 0 | 50 | Account name. | Omit | Optional |
| <ErrorText> | AN |  |  | Readable text of the error. Should be read in conjunction with the ActionCode | Omit | Optional |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Messages> | List of BankingError |  |  | If the ActionCode returned is 576, then full details of any errors can be found here. See [Banking Error](../Reference/Enums.htm#BankingE2). | Omit | Mandatory |

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
      <hyp:Ws_CreateCard_V2>  
         <hyp:request>  
            <hyp:WSID>2021123456789</hyp:WSID>  
            <hyp:IssCode>PMT</hyp:IssCode>  
            <hyp:TxnCode>?</hyp:TxnCode>  
            <hyp:clientCode>?</hyp:clientCode>  
            <hyp:Title>?</hyp:Title>  
            <hyp:LastName>?</hyp:LastName>  
            <hyp:MiddleName>?</hyp:MiddleName>  
            <hyp:FirstName>?</hyp:FirstName>  
            <hyp:Address1>?</hyp:Address1>  
            <hyp:Address2>?</hyp:Address2>  
            <hyp:Address3>?</hyp:Address3>  
            <hyp:City>?</hyp:City>  
            <hyp:Postcode>?</hyp:Postcode>  
            <hyp:ISOCountryCode>?</hyp:ISOCountryCode>  
            <hyp:Mobile>?</hyp:Mobile>   
            <hyp:CardDesign>?</hyp:CardDesign>  
            <hyp:ExternalRef>?</hyp:ExternalRef>  
            <hyp:DateOfBirth>?</hyp:DateOfBirth>  
            <hyp:AccCode>?</hyp:AccCode>  
            <hyp:LocDate>?</hyp:LocDate>  
            <hyp:LocTime>?</hyp:LocTime>  
            <hyp:TerminalID>?</hyp:TerminalID>  
            <hyp:LoadValue>?</hyp:LoadValue>  
            <hyp:CurCode>?</hyp:CurCode>  
            <hyp:Reason>?</hyp:Reason>  
            <hyp:ItemSrc>?</hyp:ItemSrc>  
            <hyp:SysDate>?</hyp:SysDate>  
            <hyp:LoadFundsType>?</hyp:LoadFundsType>  
            <hyp:LoadSrc>?</hyp:LoadSrc>  
            <hyp:LoadFee>?</hyp:LoadFee>  
            <hyp:LoadedBy>?</hyp:LoadedBy>  
            <hyp:CreateImage>?</hyp:CreateImage>  
            <hyp:CreateType>?</hyp:CreateType>  
            <hyp:CustAccount>?</hyp:CustAccount>  
            <hyp:ActivateNow>?</hyp:ActivateNow>  
            <hyp:SourceDesc>?</hyp:SourceDesc>  
            <hyp:StartDate>?</hyp:StartDate>  
            <hyp:ExpDate>?</hyp:ExpDate>  
            <hyp:CVV>?</hyp:CVV>  
            <hyp:CardName>?</hyp:CardName>  
            <hyp:MaskedPAN>?</hyp:MaskedPAN>  
            <hyp:LimitsGroup>PMT-VL-002</hyp:LimitsGroup>  
            <hyp:MCCGroup></hyp:MCCGroup>  
            <hyp:PERMSGroup>PMT-CU-002</hyp:PERMSGroup>  
            <hyp:FeeGroup></hyp:FeeGroup>  
            <hyp:ScheduledFeeGroup></hyp:ScheduledFeeGroup>  
            <hyp:WSFeeGroup>?</hyp:WSFeeGroup>  
            <hyp:ProductRef>?</hyp:ProductRef>  
            <hyp:CarrierType>?</hyp:CarrierType>  
            <hyp:Fulfil1>?</hyp:Fulfil1>  
            <hyp:Fulfil2>?</hyp:Fulfil2>  
            <hyp:DelvMeth>?</hyp:DelvMeth>  
            <hyp:ThermalLine1>?</hyp:ThermalLine1>  
            <hyp:ThermalLine2>?</hyp:ThermalLine2>  
            <hyp:Lang>?</hyp:Lang>  
            <hyp:EmbossLine4>?</hyp:EmbossLine4>  
            <hyp:ImageID>?</hyp:ImageID>  
            <hyp:LogoFrontID>?</hyp:LogoFrontID>  
            <hyp:LogoBackID>?</hyp:LogoBackID>              
            <hyp:PrimaryToken>?</hyp:PrimaryToken>  
            <hyp:DelvAddrL1>?</hyp:DelvAddrL1>  
            <hyp:DelvAddrL2>?</hyp:DelvAddrL2>  
            <hyp:DelvAddrL3>?</hyp:DelvAddrL3>  
            <hyp:DelvCity>?</hyp:DelvCity>  
            <hyp:DelvPostcode>?</hyp:DelvPostcode>  
            <hyp:DelvCounty>?</hyp:DelvCounty>  
            <hyp:DelvCountry>?</hyp:DelvCountry>  
            <hyp:DelvCode>?</hyp:DelvCode>  
            <hyp:SMSRequired>?</hyp:SMSRequired>  
            <hyp:IsLive>?</hyp:IsLive>  
            <hyp:CardManufacturer>?</hyp:CardManufacturer>  
            <hyp:CoBrand>?</hyp:CoBrand>  
            <hyp:ExternalAuth>?</hyp:ExternalAuth>  
            <hyp:LinkageGroup>?</hyp:LinkageGroup>  
            <hyp:VanityName>?</hyp:VanityName>  
            <hyp:PBlock>?</hyp:PBlock>  
            <hyp:PINMailer>?</hyp:PINMailer>  
            <hyp:FXGroup>?</hyp:FXGroup>  
            <hyp:Email>?</hyp:Email>  
            <hyp:MailOrSMS>?</hyp:MailOrSMS>  
            <hyp:Quantity>?</hyp:Quantity>  
            <hyp:AuthCalendarGroup>?</hyp:AuthCalendarGroup>  
            <hyp:LoadToken>?</hyp:LoadToken>  
            <hyp:RequiredBankingFeatures>  
               <hyp:ExistingToken>?</hyp:ExistingToken>  
               <hyp:BankingInEnabled>?</hyp:BankingInEnabled>  
               <hyp:BankingOutEnabled>?</hyp:BankingOutEnabled>  
               <hyp:DirectDebitInEnabled>?</hyp:DirectDebitInEnabled>  
               <hyp:DirectDebitOutEnabled>?</hyp:DirectDebitOutEnabled>  
               <hyp:CardEnabled>?</hyp:CardEnabled>  
               <hyp:Status>?</hyp:Status>  
               <hyp:CompanyName>?</hyp:CompanyName>  
               <hyp:AccountName>?</hyp:AccountName>  
            </hyp:RequiredBankingFeatures>  
            <hyp:IsActive>?</hyp:IsActive>  
            <hyp:CustomerID>?</hyp:CustomerID>  
            <hyp:PaymentTokenUsageGroup>?</hyp:PaymentTokenUsageGroup>  
            <hyp:IsSingleUse>false</hyp:IsSingleUse>  
            <hyp:IsNonReloadable>false</hyp:IsNonReloadable>  
            <hyp:Url>https://www.your-e-card.com/balance/7109680989634104</hyp:Url>  
            <hyp:OOBAppURL>https://login.app.bank1.com/</hyp:OOBAppURL>  
         </hyp:request>  
      </hyp:Ws_CreateCard_V2>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CreateCard_V2Response xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CreateCard_V2Result>  
            <WSID>87576567675</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <ExternalRef/>  
            <LocDate></LocDate>  
            <LocTime></LocTime>  
            <ItemID></ItemID>  
            <ClientCode></ClientCode>  
            <SysDate></SysDate>  
            <ActionCode></ActionCode>  
            <LoadValue></LoadValue>  
            <IsLive></IsLive>  
            <SortCode></SortCode>  
            <AccountNumber></AccountNumber>  
            <AccountName></AccountName>  
            <ErrorText></ErrorText>  
         </Ws_CreateCard_V2Result>  
      </Ws_CreateCard_V2Response>  
   </soap:Body>  
</soap:Envelope>
```