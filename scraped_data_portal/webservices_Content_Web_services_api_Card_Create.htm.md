# Card Create

API: `Ws_CreateCard`

This web service allows you to create both virtual and physical cards.

* *For a virtual card*: the web service generates a JPEG image of the newly created card, with a PAN, Public Token and expiry date embossed on it. This image is returned in the response and encrypted via a pre-shared [PGP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. uses PGP for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.](#) key. An SMS can optionally be sent to the cardholderâs mobile phone number with the CVV of the card. [1 If you are PCI compliant, you can retrieve the full virtual card details, which will include the PAN, Expiry and CVV. SMS is not sent by default.](#)
* *For a physical card*: the web service creates an XML file for this card, to be sent to the card manufacturer. For more information on the fields in the XML file, refer to the Thredd [Card Generation Interface specification](https://docs.thredd.com/Card_Generation_Interface_Specification.htm).

To replace a card, you must use the [Card Renew](Card_Renew.htm) web service (`Ws_Renew_Card`).

You need to be [PCI DSS Compliant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes (payment networks).
All Program Managers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/](#) to receive virtual card images from Thredd.

When creating a card, we recommend that you populate the address fields (e.g., `<Addrl1>`,`<Addrl2>`, `<postcode>`) for the [Address Verification Service (AVS)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An AVS check compares the billing address used in the transaction with the issuing bankâs address information on file for that cardholder. Depending on whether they match fully, partially, or not at all, the merchant can use that information in their decision on whether or not to accept or cancel the order.
AVS is one of the most widely used fraud prevention tools in card-not-present transactions.](#) checks.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every web service request sent. For details, see the [FAQs](../FAQs.htm).  **Tip**: You could use a number based on the current date and time, as long as it is unique (e.g., *20201217145006*). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <TxnCode> | AN | 1 | 2 | The Transaction Code. See [Transaction Codes](../Reference/Transaction_Codes.htm). Default value is 10. | Mandatory | Mandatory |
| <ClientCode> | AN | 1 | 64 | User ID of the customer using the service. Only applicable to systems using member logins. Returned in the response if present in the request.  **Note**: Legacy field. Not used. | Optional | Conditional |
| <Title> | AN | 1 | 4 | Cardholderâs title. Also used as the card purchaser's title if no delivery address is supplied. | Optional | Omit |
| <LastName> | AN | 1 | 30 | Cardholder's last name. If no delivery address is supplied, this is the card purchaserâs last name. | Conditional | Omit |
| <MiddleName> | AN | 1 | 100 | Cardholder's middle name. The `<MiddleName>` is not part of the `<EmbossName>` and therefore, does not check manufacture-approved characters. If a delivery address is not supplied, the cardholder's middle name will be the card purchaser's middle name. | Optional | Omit |
| <FirstName> | AN | 1 | 30 | Cardholder's first name. Also used as the card purchaser's first name if no delivery address is supplied. Mandatory if `<lastName>` is present. | Conditional | Omit |
| <Addrl1> | AN | 1 | 50 | Cardholder's address line 1. Also used as the card purchaser's address line 1 if no delivery address is supplied. Mandatory if âAddressâ fields are specified. | Conditional | Omit |
| <Addrl2> | AN | 1 | 50 | Cardholder's address line 2. Also used as the card purchaser's address line 2 if no delivery address is supplied. | Optional | Omit |
| <Addrl3> | AN | 1 | 50 | Cardholder's address line 3. Also used as the card purchaser's address line 3 if no delivery address is supplied. | Optional | Omit |
| <City> | AN | 1 | 50 | Cardholder's home city. Also used as the card purchaser's city if no delivery address is supplied. Mandatory if `<addrL1>` is present, and `<postcode>` is not present. | Conditional | Omit |
| <PostCode> | AN | 1 | 10 | Cardholder's home postcode. Also used as the card purchaser's postcode if no postcode is supplied. Mandatory if `<addrL1>` is present, and `<city>` is not present. See [Postcode Permitted Characters](../Reference/String_Cleaning.htm#Postcode). | Conditional | Omit |
| <Country> | AN | 1 | 3 | Cardholderâs country of residence. This is represented as a 3 digit [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) (e.g. 826 for UK). Mandatory if `<addrL1>` is present. | Conditional | Omit |
| <Mobile> | AN | 1 | 15 | Cardholderâs mobile phone number (including dialing code if applicable). See [Processing of Telephone Numbers](../Reference/String_Cleaning.htm#Processi). | Optional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. The response always returns the public token of the newly-created card. | Omit | Mandatory |
| <CardDesign> | AN | 1 | 8 | The identifier of the card product, or `Product ID`, within Thredd. For details, check with your Implementation Manager. **Note**: this is not the same field as the `CrdDesign` or `ProductRef`. | Mandatory | Omit |
| <ExternalRef> | AN | 1 | 30 | External reference code for the card.  **Note**: Legacy field. Not used. | Optional | Conditional |
| <DOB> | YYYY-MM-  DD | 10 | 10 | The cardholder's date of birth. | Optional | Omit |
| <AccCode> | AN | 1 | 6 | Access code or passcode for setting a code which is validated during activation (e.g. via the Thredd [IVR systemClosed Interactive Voice Response System Typically a telephony-based system, where the user calls in and selects options via an automated voice prompt.](#)). If provided, must be 6 digits; leading zeroes are acceptable. Mandatory if the value of `<AuthType>` is â4â. Leave empty if not required. | Optional | Omit |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <ItemID> | AN | 1 | 20 | The unique item ID for the load. This field will only have a value if a load amount was specified in the request using the `LoadValue` field. Otherwise, the item ID value returned will be 0. | Omit | Mandatory |
| <TerminalID> | AN | 1 | 15 | Point of Sale (POS) or other terminal identifier, such as a hostname. | Optional | Omit |
| <LoadValue> | D | 1 | 20 | Load value to put on the card. The amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). | Mandatory | Mandatory |
| <CurCode> | AN | 3 | 3 | 3-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217) for the currency to load (e.g. EUR). This must match the cardâs currency or the action fails (**Note**: For a Multi-FX card, the card can be loaded in any of the card's currencies). If not provided, then the card uses its billing currency. See [Currency Codes](../Reference/Currency_Codes.htm). | Conditional | Omit |
| <Reason> | AN | 1 | 60 | Reason for the card's status change. Overrides default of âCard Activatedâ that is shown in the card processor. Text is shown in the Smart Client **Tracker** screen. On Thredd Portal, this information is captured in the Notes column in Transaction Search results. | Optional | Omit |
| <ItemSrc> | N | 1 | 5 | Source field to define alternate fees. Legacy field for information purposes only; see [Item Source Types.](../Reference/Item_Source_Types.htm) Suggest using 0. | Mandatory | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <LoadFundsType> | AN | 1 | 3 | Payment method for loading funds onto the card. See [Load Fund Types](../Reference/Load_Fund_Types.htm). | Optional | Omit |
| <LoadSrc> | AN | 1 | 3 | The source of the load request for determining the fee of the load, if applicable. If omitted, defaults to 14 âUnknownâ. See [Load Sources](../Reference/Load_Sources.htm). | Optional | Omit |
| <LoadFee> | D | 1 | 20 | Fixed fee amount charged to the card purchaser for handling the card purchase and load. The amount can include up to four decimal places, depending on the currency exponent (e.g., 10.99 for EUR which has a currency exponent of 2). See [Currency Codes](../Reference/Currency_Codes.htm). If no load fee is required, specify 0. The load fee does not affect the card balance. It is only reported in the XML. | Mandatory | Omit |
| <LoadedBy> | AN | 1 | 30 | User who loaded the card. | Optional | Omit |
| <CreateImage> | N | 1 | 1 | Specifies whether to create a card image. 1= yes, 0 = No. Images are returned in the `<Image>` response parameter, encrypted by a pre-shared PGP encryption key. | Mandatory | Omit |
| <CreateType> | N | 1 | 1 | This field is mandatory. There are five possible values:  1 = Create a virtual card. Can be converted to a physical card at a later stage using the [Convert Card](Card_Convert_to_Physical.htm) web service.  2 = Create physical card. Also triggers the creation of a card file which is sent to the manufacturer.  3 = Create a virtual card. Works in the same way as option 1.  4 = Create a Master Virtual Card which is a deposit account that can be used to load other cards from.  5 = Create a virtual card and convert to a physical card. Triggers the creation of a card file which is sent to the manufacturer.  **Note**: To use create type 5, the card must be created under a virtual product.  **Note**: If the virtual card is activated then the physical card will also be active, so you should consider the security implications of this. Please speak to your implementation manager.  Create types 3, 4 and 5 will not work if `Quantity` is greater than 1. | Conditional | Omit |
| <CustAccount> | AN | 1 | 25 | Cardholder account number or reference number. You can use this reference to find the cards linked to a cardholder. Also displayed in Smart Client and in Thredd Portal as *Customer Reference*. | Optional | Omit |
| <ActivateNow> | N | 1 | 1 | Whether to activate the card. 1= Yes, 0=No. When `<Quantity>` is greater than 1 then creation of `<Quantity>` numbers of identical cards will trigger a batch process that starts within minutes of the request. If `<ActivateNow>` is 1 in such requests then the issued tokens are sent to the customer already activated. This parameter only applies if the request is for a new card. | Mandatory | Omit |
| <Source\_desc> | AN | 1 | 50 | Load source description recorded on the transaction, normally the address of the website or the Point of Sale (POS) terminal. | Optional | Omit |
| <StartDate> | AN | 5 | 5 | Start date printed on the card in the format *MM/YY*. | Omit | Mandatory |
| <ExpDate> | YYYY-MM-DD | 10 | 10 | Card expiry date. If left blank, updates with the default expiry date, based on the Card Scheme's validity period in months, otherwise updates with the input value. The date returned of the actual physical expiry is in *MM/YY*. | Optional | Mandatory |
| <CVV> | AN | 3 | 3 | [Card Verification ValueClosed The Card Verification Value (CVV) on a credit card or debit card is a 3 digit number on VISA, MasterCard and Discover branded credit and debit cards. Cardholder's are typically required to enter the CVV during any online or cardholder not present transactions. CVV numbers are also known as CSC numbers (Card Security Code), as well as CVV2 numbers, which are the same as CVV numbers, except that they have been generated by a 2nd generation process that makes them harder to guess.](#), the 3-digit code printed on the back of the card. | Omit | Mandatory |
| <CardName> | AN | 1 | 27 | The embossed name on the card. If present in the request then the embossed name on the card should be the given value. If it is not available and `<Firstname>` and `<Lastname>` are available then `<Title>` + `<Firstname>` + `<Lastname>` is the embossed name. If all the above parameters are unavailable in the request then the default embossed name remains as the embossed name. If a blank embossed name is required, then pass a single space character. See [Card Name Permitted Characters](../Reference/String_Cleaning.htm#Cardname). | Optional | Omit |
| <MaskedPAN> | AN | 14 | 19 | Card number displayed as masked (e.g., 675926\*\*\*\*\*\*1234).  **Note**. The full PAN can be returned if you are PCI DSS compliant. Contact your Implementation Manager. | Omit | Mandatory |
| <LimitsGroup> | AN | 1 | 10 | Group code of the [Limits GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). If this parameter is not supplied and this is a new card request, then the default group for the card's product is used. If the default group is not required, you can remove it by passing a space character â â. **Note**: The Limits Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <MCCGroup> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. The MCC group allows the card to be linked to a list of Merchant Category Codes (MCCs) that the card is allowed to or conversely is NOT allowed to transact at. **Note**: The MCC Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <PERMSGroup> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). If this parameter is not supplied and this is a new card request then the default group for the card's product is used. If the default group is not required, you can remove it passing a space character â â. **Note**: The Usage Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <FeeGroup> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. **Note**: The Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <SchedFeeGroup> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you remove it by passing a space character â â.**Note**: The Scheduled Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <WSFeeGroup> | AN | 1 | 10 | Code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#) (). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â. WSFeeGroup allows the card to be linked to a set of web service fees that are set up on the system. **Note**: The Web Service Fee Group is set up and configured in Smart Client and in Thredd Portal. | Optional | Omit |
| <FxGroup> | AN | 1 | 10 | Group code of the [FX Fee GroupClosed Controls the rates for FX currency conversions if the purchase currency is different from the card's currency.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product is used. If the default group is not required, you can remove it by passing a space character â â.**Note**: The FX Fee Group is set up and configured via Smart Client. | Optional | Omit |
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
| <PrimaryToken> | AN | 9 | 19 | The primary cardâs public token. If it is blank then the newly created card is a primary card, otherwise it is the secondary card in a primary/secondary relationship. Cannot be the token of a card that is already linked as a secondary card. | Optional | Omit |
| <Delv\_AddrL1> | AN | 1 | 50 | Card purchaser's /delivery address line 1. Mandatory if âDelivery Addressâ fields are specified. | Optional | Omit |
| <Delv\_AddrL2> | AN | 1 | 50 | Card purchaser's/delivery address line 2. | Optional | Omit |
| <Delv\_AddrL3> | AN | 1 | 50 | Card purchaser's /delivery address line 3. | Optional | Omit |
| <Delv\_City> | AN | 1 | 50 | Card purchaser's /delivery address delivery city. Mandatory if `<Delv_AddrL1>` is present, and `<Delv_PostCode>` is not present. | Optional | Omit |
| <Delv\_PostCode> | AN | 1 | 10 | Card purchaser's /delivery address postcode. Mandatory if `<Delv_AddrL1>` is present, and `<Delv_City>` is not present. See [Postcode Permitted Characters](../Reference/String_Cleaning.htm#Postcode). | Optional | Omit |
| <Delv\_County> | AN | 1 | 20 | Card purchaser's /delivery address county. | Optional | Omit |
| <Delv\_Country> | AN | 1 | 3 | Card purchaser's /delivery address country [3-digit ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) (e.g., 826 for UK). Mandatory if `<Delv_AddrL1>` is present. | Optional | Omit |
| <Delv\_Code> | AN | 1 | 12 | The delivery code for the card. If specified, the card manufacturer sends all cards with the same delivery code to the specified delivery address. | Optional | Omit |
| <Sms\_Required> | AN | 1 | 1 | Whether an SMS is sent to the cardholder with the card's CVV. 1 = yes; 0 =No. The default is â0â. The SMS is configurable. | Optional | Omit |
| <IsLive> | N | 1 | 1 | Specifies whether the card is active or not. 1 or True = Active; 0 or False = Not Active. | Omit | Mandatory |
| <CardManufacturer> | AN | 1 | 50 | The manufacturer to send the card generation request to. For example: *TCT*, *AllPay*, *GNC*, *Gemalto*, *Nitecrest* and *Exceet*. For a full list, see [Card Manufacturers](../Reference/Card_Manufacturers.htm). If omitted, the default for the Card Scheme (payment network) will be used. | Optional | Omit |
| <CoBrand> | AN | 1 | 6 | The Co-Brand code for the card. If supplied it replaces the *PROGRAMID* field in the *Balance XML* file. | Optional | Omit |
| <ExternalAuth> | AN | 1 | 1 | External Authorisation flag. Possible values are: 0 = Do not set External Authorisation on; 1 = Set External Authorisation. Empty value defaults to 0.  **Note**: For legacy use only. Not applicable if using EHI. | Optional | Omit |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Image> | Base64 Binary |  |  | [PGPClosed Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. uses PGP for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.](#)-encrypted image of the card. Requires configuration within Smart Client. Check with your Implementation Manager. | Omit | Conditional |
| <LinkageGroup> | AN | 1 | 10 | Group code of the [Card Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#). If this parameter is not supplied and this is a new card request then the default group for the cards product will be used. If the default group is not required, you can remove it by passing a space character â â. **Note**: The Card Linkage Group is set up and configured via Smart Client. | Optional | Omit |
| <VanityName> | AN | 1 | 32 | Enables you to add an additional alternative form of title to the card, e.g. âCompany Directorâ. Can appear on *Embossed Line 4*, or *Thermal Line 1* and *Thermal Line 2*, if configured in Smart Client, and be recorded in the card purchaser details. | Optional | Omit |
| <PBlock> | AN | 4 | 12 | Initial value of the card PIN. | Optional | Omit |
| <PINMailer> | AN | 1 | 1 | Whether to send a PIN Mailer: 0 = No (default); 1 = Yes. If 1, Thredd sends instructions in the file to the manufacturer for them to create a PIN Mailer letter. | Optional | Omit |
| <Email> | AN | 1 | 50 | Email address of the cardholder. | Optional | Omit |
| <MailOrSMS> | AN | 1 | 1 | The cardholder's preferred contact method. 0 = SMS; 1 = email. 2 = SMS and email. Default value is â0â. | Optional | Omit |
| <AuthCalendarGroup> | AN | 1 | 10 | Group code of the Card Auth Calender Group (controls the time when a card can be used). If this parameter is not supplied and this is a new card request then the default group for the cards product will be used. If the default group is not desired, it can be removed by passing a space character â â. | Optional | Omit |
| <Quantity> | N | 1 | 5 | Enables you to generate the specified quantity of cards with the same cardholder details in a batch process. The issued tokens are sent in an XML file over [SFTPClosed Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). If the cards are physical, a manufacturer file is also sent to the printer. You can use the delivery address fields to specify the delivery address for the cards.  If quantity is greater than 1, then the following optional fields are not relevant and should be left blank: <Reason>, <Source\_desc>, <CardManufacturer>, <VanityName>, <PaymentTokenUsageGroup>. <VirtualCardImage>, <ImageSize> The following mandatory fields are not relevant and should be set to the default value of '0': <ItemSRC> and <CreateImage>. <CreateType> is relevant only when its value is 1 or 2.    Since bulk create (quantity greater than 1) is run as a scheduled job, Thredd recommend performing the token/ card details enquiry one day after the bulk card creation. | Optional | Omit |
| <LoadToken> | N | 1 | 9 | The 9-digit Public Token of the MVC card that the initial load amount is to be taken from. The load shows as an MVC balance transfer (Unload + Load) in [Smart ClientClosed Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#). | Optional | Omit |
| <FeeWaiver> | N | 1 | 1 | Indicates whether to waive any web service fee set up on the system: 0 = No, 1=Yes. Default is 0. | Optional | Omit |
| <BlackList> | AN | 1 | 10 | Group code of the card acceptor Deny list. See [Card Acceptor Deny list.](Card_Acceptor_Blacklist.htm) | Optional | Omit |
| <WhiteList> | AN | 1 | 10 | Group code of the card acceptor Allow list. See [Card Acceptor Allow list](Card_Acceptor_Whitelist.htm). | Optional | Omit |
| <PaymentTokenUsageGroup> | AN | 1 | 10 | Payment token usage group code. Defines configuration options specific to the provisioning of a digital payment token. For details, see the *Tokenisation Guide*. This is a numeric value; only digits 0-9 are valid. Leave empty if no usage group is required. | Optional | Omit |
| <VirtualCardImage> | AN | 1 | 16 | The Image ID for the virtual image for the new card. You can set up Image IDs in [Smart ClientClosed Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#) in the **Image Master** and **Virtual Card Images** screens.  **Note**: If you do not provide an image ID, the default virtual card image for the product is used. | Optional | Omit |
| <ImageSize> | N | 1 | 1 | The size of the virtual image: 1 = 100%; 2 = 200%; 3 = 300%; 4 = 400%; 5 = 500%. Default is 1. | Optional | Omit |
| <IsSingleUse> | AN | 1 | 5 | Enables you to specify whether the card is [single use onlyClosed Card which can only be used for a single transaction.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <IsNonReloadable> | AN | 1 | 5 | Enables you to specify whether the card is [non-reloadableClosed Card which is loaded with funds at the time of card creation, but cannot be reloaded after this.](#). Boolean values of either 1, 0 or *true*, *false* are accepted. (1= true, 0 = false).  If not specified, then the default value from the card Product is used. | Optional | Omit |
| <Url> | AN | 1 | 100 | This value is included in the Thredd Card Generation file, in the `<QRCode>` field. For example: *https://www.your-e-card.com/balance/2909680989632389*  For details, see the [Card Generation Interface Specifications](https://developer.globalprocessing.com/Card_Generation_Interface_Specification.htm). | Optional | Omit |
| <WebServiceResult> | AN |  |  | Parameter group describing the result of the Web Service call. Only has values if the current create card request returns an [action code](../Reference/Action_Codes.htm) of *868 Duplicate WSID*. See [WebServiceResult](../Reference/WebServiceResult.htm). | Omit | Mandatory |
| <OOBAppURL> | AN | 1 | 2048 | Out Of Band app URL used in a 3D Secure authentication session. The Card Scheme (e.g., Mastercard) requires issuers using Out of Band/Biometric authentication to support the automatic redirection of cardholders from the merchant app to the authenticator app. OOBAppURL is the URL of this authenticator app. | Optional | Omit |

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
    <hyp:Ws_CreateCard>  
      <hyp:WSID>2021123456789</hyp:WSID>  
      <hyp:IssCode>PMT</hyp:IssCode>  
      <hyp:TxnCode>10</hyp:TxnCode>  
      <hyp:ClientCode></hyp:ClientCode>  
      <hyp:Title>Mr</hyp:Title>  
      <hyp:LastName>Bloggs</hyp:LastName>  
      <hyp:MiddleName></hyp:MiddleName>  
      <hyp:FirstName>Joe</hyp:FirstName>  
      <hyp:Addrl1>Office 13, Telfords Yard</hyp:Addrl1>  
      <hyp:Addrl2>6-8 The Highway, Wapping </hyp:Addrl2>  
      <hyp:City>London</hyp:City>  
      <hyp:PostCode>E1W 2BS</hyp:PostCode>  
      <hyp:Country>826</hyp:Country>  
      <hyp:Mobile></hyp:Mobile>  
      <hyp:CardDesign>123</hyp:CardDesign>  
      <hyp:ExternalRef></hyp:ExternalRef>  
      <hyp:DOB></hyp:DOB>  
      <hyp:LocDate>2021-01-01</hyp:LocDate>  
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
      <hyp:Source_desc></hyp:Source_desc>  
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
      <hyp:FeeGroup></hyp:FeeGroup>  
      <hyp:PrimaryToken></hyp:PrimaryToken>  
      <hyp:Delv_AddrL1></hyp:Delv_AddrL1>  
      <hyp:Delv_AddrL2></hyp:Delv_AddrL2>  
      <hyp:Delv_AddrL3></hyp:Delv_AddrL3>  
      <hyp:Delv_City></hyp:Delv_City>  
      <hyp:Delv_County></hyp:Delv_County>  
      <hyp:Delv_PostCode></hyp:Delv_PostCode>  
      <hyp:Delv_Country></hyp:Delv_Country>  
      <hyp:Sms_Required></hyp:Sms_Required>  
      <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
      <hyp:WSFeeGroup></hyp:WSFeeGroup>  
      <hyp:CardManufacturer></hyp:CardManufacturer>  
      <hyp:CoBrand>CB1</hyp:CoBrand>        
      <hyp:ExternalAuth></hyp:ExternalAuth>  
      <hyp:LinkageGroup></hyp:LinkageGroup>  
      <hyp:VanityName>Dr Bloggs</hyp:VanityName>  
      <hyp:PBlock></hyp:PBlock>  
      <hyp:PINMailer></hyp:PINMailer>  
      <hyp:FxGroup></hyp:FxGroup>  
      <hyp:Email>joe.bloggs@google.com</hyp:Email>  
      <hyp:MailOrSMS>1</hyp:MailOrSMS>  
      <hyp:AuthCalendarGroup></hyp:AuthCalendarGroup>  
      <hyp:Quantity>10</hyp:Quantity>  
      <hyp:LoadToken>123456789</hyp:LoadToken>  
      <hyp:FeeWaiver></hyp:FeeWaiver>  
      <hyp:BlackList>Deny List</hyp:BlackList>  
      <hyp:WhiteList></hyp:WhiteList>  
      <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
      <hyp:VirtualCardImage> </hyp:VirtualCardImage>  
      <hyp:ImageSize></hyp:ImageSize>  
      <hyp:IsSingleUse>false</hyp:IsSingleUse>  
      <hyp:IsNonReloadable>false</hyp:IsNonReloadable>  
      <hyp:Url>https://www.your-e-card.com/balance/7109680989634104</hyp:Url>  
      <hyp:OOBAppURL>https://login.app.bank1.com/</hyp:OOBAppURL>  
    </hyp:Ws_CreateCard>  
  </soapenv:Body>  
</soapenv:Envelope>
```

#### Response - Successful Card Create

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_CreateCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CreateCardResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <ExternalRef/>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <ItemID>1234</ItemID>  
            <ClientCode>0</ClientCode>  
            <SysDate>2021-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <LoadValue>10</LoadValue>  
            <IsLive>false</IsLive>  
            <StartDate>01/21</StartDate>  
            <ExpDate>02/26</ExpDate>  
            <CVV>123</CVV>  
            <MaskedPAN>987654******0123</MaskedPAN>              
            <WebServiceResult/>  
         </Ws_CreateCardResult>           
      </Ws_CreateCardResponse>  
   </soap:Body>  
</soap:Envelope>
```

#### Response - Duplicate Request Example

The response returns action code 868 for a duplicate create card request (where the same WSID is used).

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
soap:Body  
 <Ws_CreateCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
    <Ws_CreateCardResult>  
    <WSID>1234567889</WSID>  
    <IssCode>PMT</IssCode>  
    <TxnCode>10</TxnCode>  
    <PublicToken>0</PublicToken>  
    <ExternalRef/>  
    <LocDate>2021:05:25</LocDate>  
    <LocTime>14:41:45</LocTime>  
    <ItemID>0</ItemID>  
    <ClientCode/>  
    <SysDate>2022-03-04</SysDate>  
    <ActionCode>868</ActionCode>  
    <LoadValue>0</LoadValue>  
    <IsLive>false</IsLive>  
    <StartDate/>  
    <ExpDate/>  
    <CVV/>  
    <MaskedPAN/>  
    <WebServiceResult>  
        <WSID>1234567889</WSID>  
        <IssCode>PMT</IssCode>  
        <PublicToken>620137544</PublicToken>  
        <Response>000</Response>  
        <Description>Normal, approve</Description>  
        <ActionCode>000</ActionCode>  
    </WebServiceResult>  
    </Ws_CreateCardResult>  
  </Ws_CreateCardResponse>  
 </soap:Body>  
</soap:Envelope>
```