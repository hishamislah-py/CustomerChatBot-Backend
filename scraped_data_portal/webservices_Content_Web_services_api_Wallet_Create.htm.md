# Wallet Create

API: `Ws_CreateWallet`

This web service lets you create virtual wallets as well as wallets with links to physical cards.

Wallet Create constructs a jpeg image for the wallet with PAN, Public Token and expiry date embossed on it.

* For a virtual wallet: sends an SMS to the client mobile number with the CVV of the card.
* For a physical card wallet: creates an XML file for this card for sending to the card manufacturer.

If a replacement wallet is required, the cardholderâs name and address details can be left blank, in which case the existing details held in Thredd is used. Replacement wallet will be issued with the same PAN as the original card, but a different CVV.

A replacement wallet is not a valid request if the current card status is *Lost* or *Stolen*. In such cases, use the [Regenerate card](Card_Regenerate_Image.htm) request, and a different PAN is issued. The replacement wallet automatically has the same balance as the original at the time when the replacement wallet is activated.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value is 10. | Mandatory | Mandatory |
| <ClientCode> | AN | 1 | 64 | User ID of the customer using the service. Only applicable to systems using member logins. Returned in the response if present in the request.  **Note**: Legacy field. Not used. | Optional | Conditional |
| <Title> | AN | 1 | 4 | Cardholderâs title. Also used as the card purchaser's title if no delivery address is supplied. | Optional | Omit |
| <LastName> | AN | 1 | 30 | Cardholder's last name. If no delivery address is supplied, this is the card purchaserâs last name. | Conditional | Omit |
| <MiddleName> | AN | 1 | 100 | Cardholder's middle name. The `<MiddleName>` is not part of the `<EmbossName>` and therefore, does not check manufacture-approved characters. If a delivery address is not supplied, the cardholder's middle name will be the card purchaser's middle name. | Conditional | Omit |
| <FirstName> | AN | 1 | 30 | Cardholder's first name. If no delivery address is supplied it is also assumed to be the card purchaserâs first name  Mandatory if `<lastName>` is present. | Conditional | Omit |
| <Addrl1> | AN | 1 | 50 | Cardholder's address line 1. Also used as the card purchaser's address line 1 if no delivery address is supplied. Mandatory if âAddressâ fields are specified. | Conditional | Omit |
| <Addrl2> | AN | 1 | 50 | Cardholder's address line 2. Also used as the card purchaser's address line 2 if no delivery address is supplied. | Optional | Omit |
| <Addrl3> | AN | 1 | 50 | Cardholder's address line 3. Also used as the card purchaser's address line 3 if no delivery address is supplied. | Optional | Omit |
| <City> | AN | 1 | 50 | Cardholder's home city. Also used as the card purchaser's city if no delivery address is supplied. Mandatory if `<addrL1>` is present, and `<postcode>` is not present. | Conditional | Omit |
| <Postcode> | AN | 1 | 10 | Cardholder's home postcode. Also used as the card purchaser's postcode if no postcode is supplied. Mandatory if `<addrL1>` is present, and `<city>` is not present. See [Postcode Permitted Characters](../Reference/String_Cleaning.htm#Postcode). | Conditional | Omit |
| <Country> | AN | 1 | 3 | Cardholderâs country of residence. This is represented as a 3 digit [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) (e.g. 826 for UK). Mandatory if `<addrL1>` is present. | Conditional | Omit |
| <Mobile> | AN | 1 | 15 | Cardholderâs mobile phone number (including dialing code if applicable). See [Processing of Telephone Numbers](../Reference/String_Cleaning.htm#Processi). | Optional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. The response always returns the public token of the newly-created card. | Omit | Mandatory |
| <CardDesign> | AN | 1 | 8 | The identifier of the card product, or `Product ID`, within Thredd. For details, check with your Implementation Manager. **Note**: this is not the same field as the `CrdDesign` or `ProductRef`. | Conditional | Omit |
| <DOB> | YYYY-MM-  DD | 10 | 10 | The cardholder's date of birth. | Optional | Omit |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <LoadValue> | D | 1 | 20 | Load value to put on the card. The amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Mandatory | Mandatory |
| <CurCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217) for the currency to load (e.g. EUR). This must match the cardâs currency or the action fails (**Note**: For a Multi-FX card, the card can be loaded in any of the card's currencies). If not provided, then the card uses its billing currency. See [Currency Codes](../Reference/Currency_Codes.htm). | Conditional | Omit |
| <Reason> | AN | 1 | 60 | Reason for the card's status change. Overrides default of âCard Activatedâ that is shown in the card processor. Text is shown in the Smart Client **Tracker** screen. On Thredd Portal, this information is captured in the Notes column in Transaction Search results. | Optional | Omit |
| <AccCode> | AN | 0 | 6 | Access code. If provided, must be 6 digits, leading zeroes are acceptable. Leave empty if not required. | Optional | Omit |
| <ItemSrc> | N | 1 | 5 | Source field to define alternate fees. Legacy field for information purposes only; see [Item Source Types.](../Reference/Item_Source_Types.htm) Suggest using 0. | Mandatory | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <LoadFundsType> | AN | 1 | 3 | Payment method for loading funds onto the card. See [Load Fund Types](../Reference/Load_Fund_Types.htm). | Optional | Omit |
| <LoadSrc> | AN | 1 | 3 | The source of the load request for determining the fee of the load, if applicable. If omitted, defaults to 14 âUnknownâ. See [Load Sources](../Reference/Load_Sources.htm). | Optional | Omit |
| <LoadFee> | D | 1 | 20 | Fixed fee amount charged to the card purchaser for handling the card purchase and load. The amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). If no load fee is required, specify 0. The load fee does not affect the card balance. It is only reported in the XML. | Mandatory | Omit |
| <LoadedBy> | AN | 1 | 30 | User who loaded the card. | Optional | Omit |
| <CreateImage> | N | 1 | 1 | Specifies whether to create a card image. 1= yes, 0 = No. Images are returned in the `<Image>` response parameter, encrypted by a pre-shared PGP encryption key. | Mandatory | Omit |
| <CreateType> | N | 1 | 1 | This field is mandatory unless it is a replacement card request. There are five possible values:    1 = Create a virtual card. Can be converted to a physical card at a later stage using the [Convert Card](Card_Convert_to_Physical.htm) web service.  2 = Create physical card. Also triggers the creation of a card file which is sent to the manufacturer.  3 = Create a virtual card. Works in the same way as option 1.  4 = Create a Master Virtual Card which is a deposit account that can be used to load other cards from.  5 = Create a virtual card and convert to a physical card. Triggers the creation of a card file which is sent to the manufacturer.    **Note**: To use create type 5, the card must be created under a virtual product.    **Note**: If the virtual card is activated then the physical card will also be active, so you should consider the security implications of this. Please speak to your implementation manager.  Create types 3, 4 and 5 does not work if `Quantity` is greater than 1. | Conditional | Omit |
| <CustAccount> | AN | 1 | 25 | Cardholder account number or reference number. You can use this reference to find the cards linked to a cardholder. Also displayed in Smart Client and in Thredd Portal as *Customer Reference*. | Optional | Omit |
| <ActivateNow> | N | 1 | 1 | Whether to activate the card. 1= Yes, 0=No. When `<Quantity>` is greater than 1 then creation of `<Quantity>` numbers of identical cards will trigger a batch process that starts within minutes of the request. If `<ActivateNow>` is 1 in such requests then the issued tokens are sent to the customer already activated. This parameter only applies if the request is for a new card. | Mandatory | Omit |
| <StartDate> | AN | 5 | 5 | Start date printed on the card in the format *MM/YY*. | Omit | Mandatory |
| <ExpDate> | YYYY-MM-DD | 10 | 10 | Card expiry date. If left blank, updates with the default expiry date, based on the Card Scheme's validity period in months, otherwise updates with the input value. The date returned of the actual physical expiry is in *MM/YY*. | Optional | Mandatory |
| <CVV> | AN | 3 | 3 | [Card Verification ValueClosed The Card Verification Value (CVV) on a credit card or debit card is a 3 digit number on VISA, MasterCard and Discover branded credit and debit cards. Cardholder's are typically required to enter the CVV during any online or cardholder not present transactions. CVV numbers are also known as CSC numbers (Card Security Code), as well as CVV2 numbers, which are the same as CVV numbers, except that they have been generated by a 2nd generation process that makes them harder to guess.](#), the 3-digit code printed on the back of the card. | Omit | Mandatory |
| <CardName> | AN | 1 | 27 | The embossed name on the card. If present in the request then the embossed name on the card should be the given value. If it is not available and `<Firstname>` and `<Lastname>` are available then `<Title>` + `<Firstname>` + `<Lastname>` is the embossed name. If all the above parameters are unavailable in the request then the default embossed name remains as the embossed name. If a blank embossed name is required, then pass a single space character. See [Card Name Permitted Characters](../Reference/String_Cleaning.htm#Cardname). | Optional | Omit |
| <MaskedPAN> | AN | 16 | 19 | Card number displayed as masked (e.g., 675926\*\*\*\*\*\*1234).  **Note**. The full PAN can be returned if you are PCI DSS compliant. Contact your Implementation Manager. | Omit | Mandatory |
| <LimitsGroup> | AN | 1 | 10 | Group code of the [Limits GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). If this parameter is not supplied and this is a new card request, then the default group for the card's product is used. If the default group is not required, you can remove it by passing a space character â â. **Note**: The Limits Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <MCCGroup> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. The MCC group allows the card to be linked to a list of Merchant Category Codes (MCCs) that the card is allowed to or conversely is NOT allowed to transact at. **Note**: The MCC Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <PERMSGroup> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). If this parameter is not supplied and this is a new card request then the default group for the card's product is used. If the default group is not required, you can remove it passing a space character â â. **Note**: The Usage Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <FeeGroup> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. **Note**: The Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <SchedFeeGroup> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you remove it by passing a space character â â.**Note**: The Scheduled Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <WSFeeGroup> | AN | 1 | 10 | Code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#) (). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. WSFeeGroup allows the card to be linked to a set of web service fees that are set up on the system. **Note**: The Web Service Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <ProductRef> | AN | 1 | 50 | The physical card design reference as used by the Card Manufacturer. Identifies the *PRODUCT\_REF* field in the XML file sent to the card manufacturer. | Optional | Omit |
| <CarrierType> | AN | 1 | 30 | The Carrier Product design reference as used by the Card Manufacturer. This is the letter onto which the card is attached when sent to the cardholder. Identifies the Carrier Product type of the Card Manufacturer. | Optional | Omit |
| <Fulfil1> | AN | 1 | 50 | Free text field for transferring extra information to the card manufacturer, for example, to be printed on the Carrier. Identifies the *FULFIL1* field in the XML file sent to the card manufacturer. | Optional | Omit |
| <Fulfil2> | AN | 1 | 50 | Free text field for transferring extra information to the card manufacturer, for example, to be printed on the Carrier. Identifies the *FULFIL2* field in the XML file sent to the card manufacturer. | Optional | Omit |
| <DelvMethod> | AN | 1 | 1 | The delivery method for the card. Options include:  0 = Standard delivery;  1 = Registered mail;  2 = Direct delivery;  3 = Customized DelvMethod 1;  4 = Customized DelvMethod 2;  5 = Customized DelvMethod 3;  6= Customized DelvMethod 4;  7 = Customized DelvMethod 5;  Default value is 0 | Optional | Omit |
| <ThermalLine1> | AN | 1 | 120 | Free text field for transferring extra information to be printed on the card. For example, to add a customer service phone number. | Optional | Omit |
| <ThermalLine2> | AN | 1 | 70 | Free text field for transferring extra information to be printed on the card. For example, to add a link to your service terms and conditions. | Optional | Omit |
| <Lang> | AN | 1 | 2 | Two digit [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) Language code for card mailers (e.g., En = English; Fr = French).  **Note**: The available languages depend on the card manufacturer support.  Also used if bespoke SMS templates are set up. | Optional | Omit |
| <EmbossLine4> | AN | 1 | 27 | The cardâs embossed line 4 on the front of the card. Could be used for example, to add an account number or sort code. | Optional | Omit |
| <ImageId> | AN | 1 | 16 | Reference which identifies the card manufacturer's image file that is printed on the face of the card. | Optional | Omit |
| <LogoFrontId> | AN | 1 | 30 | Reference which identifies the card manufacturer's logo file that is printed on the face of the card. | Optional | Omit |
| <LogoBackId> | AN | 1 | 30 | Reference which identifies the card manufacturer's logo file that is printed on the back of the card, if supported. | Optional | Omit |
| <Replacement> | N | 1 | 1 | Whether the card is a new card or a replacement. The possible values are: 0 = new card; 1 = replacement card. Needs to be agreed with the card manufacturer.  **Note**: Do not use a value '1', which is for legacy usage only; to replace a card, we recommend you use [Card Renew](Card_Renew.htm): `ws_renew_card`. | Mandatory | Omit |
| <PrimaryToken> | AN | 16 | 19 | The primary cardâs public token. If it is blank then the newly created card is a primary card, otherwise it is the secondary card in a primary/secondary relationship. Cannot be the token of a card that is already linked as a secondary card. | Optional | Omit |
| <Delv\_AddrL1> | AN | 1 | 50 | Card purchaser's /delivery address line 1. Mandatory if âDelivery Addressâ fields are specified. | Optional | Omit |
| <Delv\_AddrL2> | AN | 1 | 50 | Card purchaser's/delivery address line 2. | Optional | Omit |
| <Delv\_AddrL3> | AN | 1 | 50 | Card purchaser's /delivery address line 3. | Optional | Omit |
| <Delv\_City> | AN | 1 | 50 | Card purchaser's /delivery address delivery city. Mandatory if `<Delv_AddrL1>` is present, and `<Delv_PostCode>` is not present. | Optional | Omit |
| <Delv\_Postcode> | AN | 1 | 10 | Card purchaser's /delivery address postcode. Mandatory if `<Delv_AddrL1>` is present, and `<Delv_City>` is not present. See [Postcode Permitted Characters](../Reference/String_Cleaning.htm#Postcode). | Optional | Omit |
| <Delv\_County> | AN | 1 | 20 | Card purchaser's /delivery address county. | Optional | Omit |
| <Delv\_Country> | AN | 1 | 3 | Card purchaser's /delivery address country [3-digit ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) (e.g., 826 for UK). Mandatory if `<Delv_AddrL1>` is present. | Optional | Omit |
| <Delv\_Code> | AN | 1 | 12 | The delivery code for the card. If specified, the card manufacturer sends all cards with the same delivery code to the specified delivery address. | Optional | Omit |
| <Sms\_Required> | AN | 1 | 1 | Whether an SMS is sent to the cardholder with the card's CVV. 1 = yes; 0 =No. The default is â0â. The SMS is configurable. | Optional | Omit |
| <IsLive> | N | 1 | 1 | Specifies whether the card is active or not. 1 or True = Active; 0 or False = Not Active. | Omit | Mandatory |
| <CardManufacturer> | AN | 1 | 50 | The manufacturer to send the card generation request to. For example: *TCT*, *AllPay*, *GNC*, *Gemalto*, *Nitecrest* and *Exceet*. For a full list, see [Card Manufacturers](../Reference/Card_Manufacturers.htm). If omitted, the default for the Card Scheme (payment network) will be used. | Optional | Omit |
| <CoBrand> | AN | 1 | 6 | The Co-Brand code for the card. If supplied it replaces the *PROGRAMID* field in the *Balance XML* file. | Optional | Omit |
| <ExternalAuth> | AN | 1 | 1 | External Authorisation flag. Possible values are: 0 = Do not set External Authorisation on; 1 = Set External Authorisation. Empty value defaults to 0.  **Note**: For legacy use only. Not applicable if using EHI. |  |  |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Image> | Base64 Binary |  |  | [PGPClosed Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. uses PGP for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.](#)-encrypted image of the card. Requires configuration within Smart Client. Check with your Implementation Manager. | Omit | Conditional |
| <FeeWaiver> | N | 1 | 1 | Indicates whether to waive any web service fee set up on the system: 0 = No, 1=Yes. Default is 0. | Optional | Omit |
| <BlackList> | AN | 1 | 10 | Group code of the card acceptor Deny list. See [Card Acceptor Deny list.](Card_Acceptor_Blacklist.htm) | Optional | Omit |
| <WhiteList> | AN | 1 | 10 | Group code of the card acceptor Allow list. See [Card Acceptor Allow list](Card_Acceptor_Whitelist.htm). | Optional | Omit |
| <EWALLET> | - | - | - | See [eWallet Description](#eWallet). | Omit | Mandatory |
| <PaymentTokenUsageGroup> | AN | 1 | 10 | Payment token usage group code. Defines configuration options specific to the provisioning of a digital payment token. For details, see the *Tokenisation Guide*. This is a numeric value; only digits 0-9 are valid. Leave empty if no usage group is required. | Optional | Omit |
| <VirtualCardImage> | AN | 1 | 16 | The Image ID for the virtual image for the new card. You can set up Image IDs in [Smart ClientClosed Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#) in the **Image Master** and **Virtual Card Images** screens.  **Note**: If you do not provide an image ID, the default virtual card image for the product is used. | Optional | Omit |
| <ImageSize> | N | 1 | 1 | The size of the virtual image: 1 = 100%; 2 = 200%; 3 = 300%; 4 = 400%; 5 = 500%. Default is 1. | Optional | Omit |
| <PBlock> | AN | 4 | 12 | The initial card PIN value. | Optional | Omit |
| <IsSingleUse> | AN | 1 | 5 | Enables you to specify whether the card is [single use onlyClosed Card which can only be used for a single transaction.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <IsNonReloadable> | AN | 1 | 5 | Enables you to specify whether the card is [non-reloadableClosed Card which is loaded with funds at the time of card creation, but cannot be reloaded after this.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <Url> | AN | 1 | 100 | This value is included in the Thredd Card Generation file, in the `<QRCode>` field. For example: *https://www.your-e-card.com/balance/2909680989632389*  For details, see the [Card Generation Interface Specifications](https://developer.globalprocessing.com/Card_Generation_Interface_Specification.htm). | Optional | Omit |
| <OOBAppURL> | AN | 1 | 2048 | Out Of Band app URL used in a 3D Secure authentication session. The Card Scheme (e.g., Mastercard) requires issuers using Out of Band/Biometric authentication to support the automatic redirection of cardholders from the merchant app to the authenticator app. OOBAppURL is the URL of this authenticator app. | Optional | Omit |

#### eWallet Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <IDENTITY> | AN | 1 | 9 | The Thredd 16-digit public token. Mandatory in the response. | Omit | Mandatory |
| <CARDS> |  |  |  | An array of cards. See [CARD Description](#CARD) below. | Omit | Mandatory |
| <ACCOUNTS> |  |  |  | An array of accounts. See [ACCOUNT Description](#ACCOUNT) below; may occur multiple times. | Omit | Mandatory |

#### CARD Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PAN> | AN | 1 | 9 | Card Number. Unique card identifier. | Omit | Mandatory |
| <CRDCURRCODE> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the account billing currency. | Omit | Mandatory |
| <CRDPRODUCT> | AN | 1 | 50 | The identifier of the card product, or `Product ID`, within Thredd. For details, check with your Implementation Manager. | Omit | Mandatory |
| <CUSTCODE> | AN | 1 | 50 | Customer account number. Mandatory in the response if present. Also displayed in Smart Client as *Customer Reference* and *Customer Reference Number* in Thredd Portal. | Omit | Conditional |
| <PRIMARY> | AN | 1 | 1 | Indicates if the card is the Primary card. Default value 'Y'. | Omit | Mandatory |
| <PROGRAMID> | AN | 1 | 50 | The ID of the [ProgramClosed Logical grouping of your products set up in Smart Client. This is setup with whatever the customer (issuer or program manager) wants. Can be viewed in reports or via the web services API and may also be sent to the card manufacturer.](#) this card belongs to. | Omit | Mandatory |
| <STATCODE> | AN | 2 | 2 | The status code of the card. See [Status Codes](../Reference/Status_Codes.htm). | Omit | Mandatory |
| <EXPDATE> | AN | 10 | 10 | Expiry date of the card in *YYYY-MM-DD* format. | Omit | Mandatory |

#### ACCOUNT Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <ACCNO> | AN | 1 | 9 | Account number. | Omit | Mandatory |
| <ACCTYPE> | AN | 2 | 2 | Type of card account. See [Account Types](../Reference/Account_Types.htm). | Omit | Mandatory |
| <CURRCODE> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the account billing currency. | Omit | Mandatory |
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
    <hyp:Ws_CreateWallet>  
      <hyp:WSID>2021123456789</hyp:WSID>  
      <hyp:IssCode>PMT</hyp:IssCode>  
      <hyp:TxnCode>10</hyp:TxnCode>  
      <hyp:ClientCode></hyp:ClientCode>  
      <hyp:Title>Mr</hyp:Title>  
      <hyp:LastName>Lastname</hyp:LastName>  
      <hyp:MiddleName>Middlename</hyp:MiddleName>  
      <hyp:FirstName>Firstname</hyp:FirstName>  
      <hyp:Addrl1>Office 13, Telfords Yard</hyp:Addrl1>  
      <hyp:Addrl2>6-8 The Highway, Wapping </hyp:Addrl2>  
      <hyp:City>London</hyp:City>  
      <hyp:PostCode>E1W 2BS</hyp:PostCode>  
      <hyp:Country>826</hyp:Country>  
      <hyp:Mobile></hyp:Mobile>  
      <hyp:CardDesign>123</hyp:CardDesign>  
      <hyp:DOB></hyp:DOB>  
      <hyp:LocDate>2013-01-01</hyp:LocDate>  
      <hyp:LocTime>120000</hyp:LocTime>  
      <hyp:TerminalID></hyp:TerminalID>  
      <hyp:LoadValue>10</hyp:LoadValue>  
      <hyp:CurCode>GBP</hyp:CurCode>  
      <hyp:Reason></hyp:Reason>  
      <hyp:AccCode>123456</hyp:AccCode>  
      <hyp:ItemSrc>2</hyp:ItemSrc>  
      <hyp:LoadFundsType>4</hyp:LoadFundsType>  
      <hyp:LoadSrc>10</hyp:LoadSrc>  
      <hyp:LoadFee>0.0</hyp:LoadFee>  
      <hyp:LoadedBy>Admin</hyp:LoadedBy>  
      <hyp:CreateImage>1</hyp:CreateImage>  
      <hyp:CreateType>1</hyp:CreateType>  
      <hyp:CustAccount></hyp:CustAccount>  
      <hyp:ActivateNow>0</hyp:ActivateNow>  
      <hyp:ExpDate></hyp:ExpDate>  
      <hyp:CardName>GIFT CARD</hyp:CardName>  
      <hyp:LimitsGroup>PMT-VL-002</hyp:LimitsGroup>  
      <hyp:MCCGroup></hyp:MCCGroup>  
      <hyp:PERMSGroup>PMT-CU-002</hyp:PERMSGroup>  
      <hyp:ProductRef></hyp:ProductRef>  
      <hyp:CarrierType></hyp:CarrierType>  
      <hyp:Fulfil1></hyp:Fulfil1>  
      <hyp:Fulfil2></hyp:Fulfil2>  
      <hyp:DelvMethod>0</hyp:DelvMethod>  
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
      <hyp:Sms_Required>    </hyp:Sms_Required>  
      <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
      <hyp:WSFeeGroup></hyp:WSFeeGroup>  
      <hyp:CardManufacturer></hyp:CardManufacturer>  
      <hyp:CoBrand></hyp:CoBrand>  
      <hyp:PublicToken></hyp:PublicToken>  
      <hyp:ExternalAuth></hyp:ExternalAuth>  
      <hyp:FeeWaiver></hyp:FeeWaiver>  
      <hyp:BlackList>Deny list</hyp:BlackList>  
      <hyp:WhiteList></hyp:WhiteList>      <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
      <hyp:VirtualCardImage></hyp:VirtualCardImage>        
      <hyp:ImageSize></hyp:ImageSize>  
      <hyp:PBlock>12345</hyp:PBlock>  
      <hyp:IsSingleUse>false</hyp:IsSingleUse>  
      <hyp:IsNonReloadable>false</hyp:IsNonReloadable>  
      <hyp:Url></hyp:Url>  
      <hyp:OOBAppURL>https://login.app.bank1.com/</hyp:OOBAppURL>  
    </hyp:Ws_CreateWallet>  
  </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CreateWalletResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CreateWalletResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMTD</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <LocDate>2014-02-04</LocDate>  
            <LocTime>130700</LocTime>  
            <ItemID>0</ItemID>  
            <ClientCode>0</ClientCode>  
            <SysDate>2014-08-29</SysDate>  
            <ActionCode>000</ActionCode>  
            <LoadValue>0</LoadValue>  
            <IsLive>false</IsLive>  
            <StartDate>08/14</StartDate>  
            <ExpDate>08/17</ExpDate>  
            <CVV>076</CVV>  
            <MaskedPAN>123456******7890</MaskedPAN>  
            <EWALLET>  
               <EWALLET xmlns="">  
                  <IDENTITY>9876543212345678</IDENTITY>  
                  <CARDS>  
                     <CARD>  
                        <PAN>9876543212345678</PAN>  
                        <CRDCURRCODE>GBP</CRDCURRCODE>  
                        <CRDPRODUCT>MCRD</CRDPRODUCT>  
                        <CUSTCODE/>  
                        <PRIMARY>Y</PRIMARY>  
                        <PROGRAMID>PRG123</PROGRAMID>  
                        <STATCODE>00</STATCODE>  
                        <EXPDATE>2017-08-31</EXPDATE>  
                     </CARD>  
                  </CARDS>  
                  <ACCOUNTS>  
                     <ACCOUNT>  
                        <ACCNO>9876543212345676</ACCNO>  
                        <ACCTYPE>01</ACCTYPE>  
                        <CURRCODE>EUR</CURRCODE>  
                        <FINAMT>0.00</FINAMT>  
                        <BLKAMT>0.00</BLKAMT>  
                        <AMTAVL>0.00</AMTAVL>  
                     </ACCOUNT>  
                     <ACCOUNT>  
                        <ACCNO>9876543212345677</ACCNO>  
                        <ACCTYPE>01</ACCTYPE>  
                        <CURRCODE>USD</CURRCODE>  
                        <FINAMT>0.00</FINAMT>  
                        <BLKAMT>0.00</BLKAMT>  
                        <AMTAVL>0.00</AMTAVL>  
                     </ACCOUNT>  
                     <ACCOUNT>  
                        <ACCNO>9876543212345678</ACCNO>  
                        <ACCTYPE>01</ACCTYPE>  
                        <CURRCODE>GBP</CURRCODE>  
                        <FINAMT>0.00</FINAMT>  
                        <BLKAMT>0.00</BLKAMT>  
                        <AMTAVL>0.00</AMTAVL>  
                     </ACCOUNT>  
                  </ACCOUNTS>  
               </EWALLET>  
            </EWALLET>  
         </Ws_CreateWalletResult>  
      </Ws_CreateWalletResponse>  
   </soap:Body>  
</soap:Envelope>
```