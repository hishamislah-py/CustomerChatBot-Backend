# 2 XML Fields

This section provides details of the fields included in the XML file.

## 2.1 <CARDGEN>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| [<CARDSUM>](#%3CCARDSUM) | sub-section tag | n/a | Contains a block of XML TAGS for the [<CARDSUM>](#%3CCARDSUM) section. | ? |
| [<PRODUCT>](#%3CPRODUCT) | sub-section tag | n/a | Contains a block of XML TAGS for [<PRODUCT>](#%3CPRODUCT) section. | N/A |

## 2.2 <CARDSUM>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <DATA\_FORMAT\_VERSION> | Varchar | 5 | File version | No |
| <FILEDATE> | dd-mm-yyyy | 10 | File date | No |
| <FILETIME> | hh-mm-ss | 10 | File time | No |
| <NO\_OF\_CARRIERS> | Integer |  | Number of carriers | No |
| <NO\_OF\_CARDS> | Integer |  | Number of cards | No |
| <NO\_OF\_PRODUCTS> | Integer |  | Number of different products in the file (Mag stripe/chip etc) | No |
| <TXREF> | varchar | 30 | Transmission\_Reference  This is an incrementing reference number and may not be consecutive. | No |
| <ORDER\_REF> | varchar | 30 | Customer order reference number | Yes |

<CARDSUM> example:

[Copy](javascript:void(0);)

```
    <CARDSUM>  
        <DATA_FORMAT_VERSION>12</DATA_FORMAT_VERSION>  
        <FILEDATE>02-01-2023</FILEDATE>  
        <FILETIME>09-15-55</FILETIME>  
        <NO_OF_CARRIERS>2</NO_OF_CARRIERS>  
        <NO_OF_CARDS>2</NO_OF_CARDS>  
        <NO_OF_PRODUCTS>1</NO_OF_PRODUCTS>  
        <TXREF>1001</TXREF>  
        <ORDER_REF>ABC-123</ORDER_REF>  
    </CARDSUM>
```

## 2.3 <PRODUCT>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <PRODUCT\_REF> | varchar | 50 | Identifies the product.    **Note**: This is the physical card Design reference as used by the card printer. | No |
| [<RECORD>](#%3CRECORD%3E) | sub-section tag |  | Defines a record within a Product | N/A |

## 2.4 <RECORD>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <REQUEST\_TYPE> | varchar | 15 | Indicates whether the card is a âNewâ or âReplacementâ card request  For PIN Mailers, can be one of:  PIN\_MAILER  NEW\_WITH\_PINM  REPL\_WITH\_PINM | No |
| <UID> | Varchar | 20 | Unique identifier to identify the record. You can use this in error tracking. | No |
| [<CARRIER>](#%3CCARRIER) | sub-section tag |  | Defines the Carrier section within a Record | N/A |
| [<CARD>](#%3CCARD%3E) | sub-section tag |  | Card definition opening tag within a Record | N/A |
| [<CHIP>](#%3CCHIP%3E) | sub-section tag |  | Defines the chip details within a Record. This element may not be present, depending on Card Type. | N/A |

<RECORD> Example:

[Copy](javascript:void(0);)

```
        <RECORD>  
            <REQUEST_TYPE>New</REQUEST_TYPE>  
            <UID>123456789</UID>  
            <CARRIER>  
            </CARRIER>  
            <CARD>  
            </CARD>  
            <CHIP>  
            </CHIP>  
        </RECORD>
```

## 2.5 <CARRIER>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <TITLE> | Varchar | 4 | Cardholder title | Yes |
| <FNAME> | Varchar | 30 | Cardholder first name | Yes |
| <SNAME> | Varchar | 30 | Cardholder surname | Yes |
| <ADD1> | Varchar | 50 | Cardholder address line 1 | Yes |
| <ADD2> | Varchar | 50 | Cardholder address line 2 | Yes |
| <ADD3> | Varchar | 50 | Cardholder address line 3 | Yes |
| <ADD4> | Varchar | 50 | Cardholder address line 4 | Yes |
| <CITY> | Varchar | 50 | Cardholder address city | Yes |
| <POSTCODE> | Varchar | 10 | Cardholder address postcode | Yes |
| <MOBILE> | Varchar | 50 | Mobile phone number linked to the card | Yes |
| <COUNTRY> | Varchar | 3 | Cardholder address country. Numeric 3-digit ISO 3166-1 Country code (e.g. 052 for Barbados). (Always 3 digits, use leading zeros if needed.) | Yes |
| <BULK\_ADD1> | Varchar | 100 | Alternative delivery address line 1. If present, should be used in preference to carrier address. | Yes |
| <BULK\_ADD2> | Varchar | 100 | Alternative delivery address line | Yes |
| <BULK\_ADD3> | Varchar | 100 | Alternative delivery address line 3 | Yes |
| <BULK\_CITY> | Varchar | 50 | Alternative delivery address city | Yes |
| <BULK\_COUNTY> | Varchar | 20 | Alternative delivery address count | Yes |
| <BULK\_POSTCODE> | Varchar | 10 | Alternative delivery address postcode | Yes |
| <BULK\_COUNTRY> | Varchar | 3 | Alternative address country. Numeric 3-digit ISO 3166-1 Country code (e.g. 052 for Barbados). (Always 3 digits, use leading zeros if needed.) | Yes |
| <CARRIER\_TYPE> | Varchar | 30 | Defines carrier product.    **Note**: This is the Carrier Product Design reference as used by the card printer. | No |
| <CARRIER\_LOGO\_ID > | Varchar | 20 | Defines an optional carrier logo. | Yes |
| <DELV\_METHOD> | Char | 1 | The delivery method for the card:  0 = Standard mail (default)  1 = Registered mail  2 = Direct delivery (Courier)  3 = Customized Delivery Method 1  4 = Customized Delivery Method 2  5 = Customized Delivery Method 3  6= Customized Delivery Method 4  7 = Customized Delivery Method 5 | No |
| <DELV\_CODE> | Varchar | 12 | The delivery code for the card:  If specified, all cards with the same delivery code are to be sent together to the specified BULK delivery address.  Carriers with the same DELV\_CODE will be grouped together in the file. | Yes |
| <FULFIL1> | Varchar | 50 | RFU (Reserved for Future Use) | Yes |
| <FULFIL2> | Varchar | 50 | RFU | Yes |
| <LANG> | Char | 2 | Defines the language of the carrier product, if it is not already defined by the `<CARRIER_TYPE>` elements. Uses ISO 639-1 language code.  **Examples:**  English is âenâ, French is âfrâ | Yes |

<CARRIER> example:

[Copy](javascript:void(0);)

```
            <CARRIER>  
                <TITLE>Mr.</TITLE>  
                <FNAME>Fred</FNAME>  
                <SNAME>Jones</SNAME>  
                <ADD1>Sample Company</ADD1>  
                <ADD2>1 Sample Street </ADD2>  
                <ADD3>Sample Borough </ADD3>  
                <ADD4>Sample Address Line 4</ADD4>  
                <CITY>Sample City</CITY>  
                <POSTCODE>E1W2BS</POSTCODE>  
                <MOBILE>44123456789</MOBILE>  
                <COUNTRY>UK</COUNTRY>  
                <BULK_ADD1></BULK_ADD1>  
                <BULK_ADD2></BULK_ADD2>  
                <BULK_ADD3></BULK_ADD3>  
                <BULK_CITY></BULK_CITY>  
                <BULK_COUNTY></BULK_COUNTY>  
                <BULK_POSTCODE></BULK_POSTCODE>  
                <BULK_COUNTRY></BULK_COUNTRY>  
                <CARRIER_TYPE>CAR_1</CARRIER_TYPE>  
                <CARRIER_LOGO_ID></CARRIER_LOGO_ID>  
                <DELV_METHOD>0</DELV_METHOD>  
                <DELV_CODE></DELV_CODE>  
                <FULFIL1></FULFIL1>  
                <FULFIL2></FULFIL2>  
                <LANG>en</LANG>  
            </CARRIER>
```

## 2.6 <CARD>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <TYPE> | varchar | 20 | Defines the product:  âMagâ  âChip&PINâ  âChip&PIN&Contactlessâ | No |
| <CURRENCY> | Char | 4 | 4-digit ISO currency code. For example: â0826â= GBP | No |
| <TRACK1> | Varchar | 76 | Track 1 data for magnetic stripe, excluding the Start Sentinel, End Sentinel and LRC characters.    **Note**: The ISO standard allows for maximum of 76 (excluding the Start Sentinel, End Sentinel and LRC characters).    Track Layout    **MASTERCARD:**  B + PAN + ^ + Name + ^ + Expiry date in âyyMMâ format + Service Code + 00000 + CVV1 + 0000000    **VISA:**  B + PAN + ^ + Name + ^ + Expiry in "yyMM" format + Service Code + 00 + CVV1 + 000000 | No |
| <TRACK2> | Varchar | 37 | Track 2 data for the magnetic stripe, excluding Start Sentinel, End Sentinel and LRC characters.    **MASTERCARD:**  `PAN + = + Expiry date` in "yyMM" format `+ Service Code + 000000 + Validity in months + CVV1 + PAN Sequence No`    **VISA:**  `PAN + = + Expiry Date in "yyMM" format + Service Code + CVV1 + 00000` | No |
| <TRACK3> | Varchar | 104 | Track 3 data for the magnetic stripe, excluding Start Sentinel, End Sentinel and LRC characters.    ISO standard allows for a maximum of 104 characters (excluding Start Sentinel, End Sentinel and LRC).  By default, Thredd will put the Card 9-digit token in this element. | Yes |
| <EMBOSS\_PAN> | Integer | 19 | Embossed card Primary Account Number (PAN) | No |
| <EMBOSS\_NAME> | varchar | 27 | Embossed card name. Actual maximum length will depend on the card design. | Yes |
| <EMBOSS\_START> | Varchar | 10 | Embossed card start date (MM/YY) | No |
| <EMBOSS\_EXPIRY> | Varchar | 10 | Embossed card expiry date (MM/YY) | No |
| <EMBOSS\_CVC2> | varchar | 10 | Embossed card Verification Code 2 (CVC2) | No |
| <EMBOSS\_LINE4> | Varchar | 27 | Embossed card line 4. Actual maximum length will depend on the card design. | Yes |
| <THERMAL\_LINE1> | Varchar | 120 | Example, Company name | Yes |
| <THERMAL\_LINE2> | Varchar | 70 | RFU | Yes |
| <IMAGE\_ID> | Varchar | 20 | Identifies the image file that will be printed on the face of the card. | Yes |
| <LOGO\_FRONT\_ID> | Varchar | 30 | Identifies the logo file that will be printed on the face of the card. | Yes |
| <LOGO\_BACK\_ID> | Varchar | 30 | Identifies the image file that will be printed on the back of the card, if supported. | Yes |
| <QRCODE> | Varchar | 100 | Identifies the QR code that will be printed on the card, if supported. You can add separate values to each card using Thredd API. For details, see the `Url` field in the SOAP [Web Services Guide > Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm). (**Note**: functionality currently not available if using our REST-based Cards API). | Yes |
| <PINBLOCK> | Hexadecimal | 16 | Optional. Will only be present if the card is Mag stripe and the card requester requires online PIN. Used for PIN mailers.    Format is the same as `<PINBLOCK>` in the `<CHIP>` section; see below. | Yes |

<CARD> example:

[Copy](javascript:void(0);)

```
            <CARD>  
                <TYPE>Mag</TYPE>  
                <CURRENCY>0826</CURRENCY>  
                <TRACK1>B1234567812345678^GIFTCARD/CORPORATE^1811122000009830000000</TRACK1>  
                <TRACK2>1234567812345678=16102210000006064400</TRACK2>  
                <TRACK3>953171211</TRACK3>  
                <EMBOSS_PAN>1234 5678 1234 5678</EMBOSS_PAN>  
                <EMBOSS_NAME>MR A B SAMPLE</EMBOSS_NAME>  
                <EMBOSS_START>11/11</EMBOSS_START>  
                <EMBOSS_EXPIRY>10/16</EMBOSS_EXPIRY>  
                <EMBOSS_CVC2>1234 135</EMBOSS_CVC2>  
                <EMBOSS_LINE4>A123 REG</EMBOSS_LINE4>  
                <THERMAL_LINE1>Possible Company Name here</THERMAL_LINE1>  
                <THERMAL_LINE2></THERMAL_LINE2>  
                <IMAGE_ID></IMAGE_ID>  
                <LOGO_FRONT_ID></LOGO_FRONT_ID>  
                <LOGO_BACK_ID></LOGO_BACK_ID>  
                <QRCODE>https://www.flex-e-card.com/balance/2909680989632389</QRCODE>  
                <PINBLOCK>3A56DFF541C12197</PINBLOCK>  
            </CARD>
```

## 2.7 <CHIP>

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <TYPE> | varchar | 10 | Possible values:  Maestro  Mastercard  VisaCard  Euro Cirrus  EuroCard  Cirrus Maestro  PLUS Card | Yes |
| <PAN> | Integer | 16-19 | Primary Account Number ISO 8583 bit 2 | Yes |
| <PAN\_SEQ> | Integer | 2 | PAN Sequence number.  ISO 8583 bit 23.  Value from 00 to 99. | Yes |
| <NAME> | Varchar | 26 | Must match name embedded in Track 1 | Yes |
| <START\_DATE> | Integer | 6 | YYMMDD | Yes |
| <EXPIRY\_DATE> | Integer | 6 | YYMMDD | Yes |
| <SERVICE\_CODE> | Integer | 3 | Three decimal digits as defined in ISO 7813.    First digit: Use and Technology:  1 = International  2 = International, Chip  5 = National Use Only  6 = National Use Only, Chip  7 = Private Label  9 = Test Card    Second digit: Authorisation requirements:  0 = Normal  2 = Online Authorisation Required  4 = Online Authorisation required unless special agreement    Third digit: Service and PIN requirements:  0 = PIN Required  1 = No restrictions  2 = Purchases only  3 = ATM Only, PIN required  4 = Cash only  5 = Purchases only, PIN required  6 = Use PIN if possible  7 = Purchases only, use PIN if possible | Yes |
| <CHIP\_TRACK\_1> | varchar | 76 | This is the entire chip track 1 for EMV transactions.  It permits the derivation of EMV tag hex 9F1F (track 1 discretionary data as defined in ISO 7813) which is part of this.    **MASTERCARD:**  B + PAN + ^ + Name + ^ + Expiry date in âyyMMâ format + Service Code + 00000 + iCVV + 0000000    **VISA:**  B + PAN + ^ + Name + ^ + Expiry Date in "yyMM" format + Service Code + 00 + iCVV + 000000 | Yes |
| <CHIP\_TRACK\_2> | varchar | 38 | This is the EMV Track 2 equivalent data, for EMV tag hex 57. It is for EMV-based (including qVSDC) transactions (both contact and contactless).    **MASTERCARD:**  PAN + D + Expiry in "yyMM" format + Service Code + 000000 + Validity in months + iCVV + PAN Sequence No (If the length of CHIP\_TRACK\_2 is odd then will add âFâ at the end)    **VISA:**  PAN + D + Expiry Date in "yyMM" format + Service Code + iCVV + 00000 (If the length of CHIP\_TRACK\_2 is odd then will add âFâ at the end) | Yes |
| <CHIP\_TRACK\_1\_MSD\_CL> | Varchar | 76 | Optional. This element will only be present if the product type supports Contactless Magnetic Stripe Transactions.  It is the base Track 1 for Contactless Magnetic Stripe (which is not EMV) transactions.    **MASTERCARD:**  For Mastercard, this is for tag hex 56 (PayPass Magstripe Track 1 Data.)  (See Mastercard âPayPass MagStripe Technical Specifications v3.2 Oct 2006â.)    **VISA:**  For Visa, if there is a separate data item on the ICC for the Track 1 exclusively for Magnetic Stripe Data (not EMV or qVSDC) then use this for it.    Format is same as `<CHIP_TRACK_1>` except Name is replaced with space and forward slash i.e. â /â, and discretionary data may be different. | Yes |
| <CHIP\_TRACK\_2\_MSD\_CL> | Varchar | 37 | Optional. This element will only be present if the product type supports Contactless Magnetic Stripe transactions.  It is the base Track 2 for contactless Magnetic Stripe (which is not EMV) transactions.    **MASTERCARD:**  For Mastercard, this is for tag hex 9F6B (PayPass Magstripe Track 2 Data.) (See Mastercard âPayPass MagStripe Technical Specifications v3.2 Oct 2006â.)    **VISA:**  For Visa, if there is a separate data item on the ICC for the Track 2 exclusively for Magnetic Stripe Data (not EMV or qVSDC) then use this for it.    Format is same as `<CHIP_TRACK_2>` but discretionary data may be different. | Yes |
| <PINBLOCK> | Hexadecimal | 16 | Holds the encrypted PIN to be placed on the chip card.  Format is ISO 9564-1 Format 0 (same as ANSI X9.8 Format 0), triple DES encrypted with the double-length Zone PIN Key, expressed as 16 hex digits (with 2 hex digits representing 1 binary byte.)    This is formed as:  Plaintext PIN field = â0â+ PIN length (4-C) + PIN + âFâs padding to 16 hex digits.    Account number field = â0000â + rightmost 12 digits of the PAN excluding the check digit.    Then XOR the âPlaintext PIN fieldâ and âAccount number fieldâ.    This is 16 hex digits representing 8 binary bytes.  Then Triple-DES encrypt the resultant 8 binary bytes with the double length Zone PIN Key.    **Example**:  PAN = 5299887766554439  PIN = 223344  Zone PIN Key = 3B6870987613107CFB1F4C6EC17F3483    Plaintext PIN field = 06223344FFFFFFFF  Account Number Field = 0000988776655443  Result of XOR = 0622ABC3899AABBC  Encrypting this with the Zone PIN key gives result:  7553DAA289620533    So PINBLOCK is 7553DAA289620533 | Yes |

## 2.8 Additional Fields (In Cut-Down File Version for Program Manager)

| XMLTAG | Type | Length | Description | Nulls Allowed |
| --- | --- | --- | --- | --- |
| <CUST\_ACCNO> | Varchar | 25 | Cardholder account number or reference number. You can use this reference to find the cards linked to a cardholder. Also displayed in Thredd Portal as *Customer Reference Number*, and in Smart Client as *Customer Reference*. (**Note**: This corresponds to the `customerReference` parameter set using the Thredd REST-based Cards API or the `CustAccount` parameter set using Thredd SOAP web services (SOAP API).  See the [Cards API Website > Create a Card](https://cardsapidocs.thredd.com/reference/create-card) or the [Web Services Guide > Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm). | Yes |
| <PASSCODE> | Varchar | 6 | Code which can be used to validate the card when a card activation request is received from the cardholder. (**Note**: This corresponds to the parameter set using the `AccCode` parameter in Thredd web services (SOAP API). See the [Web Services Guide > Card Create](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Create.htm). (**Note**: equivalent functionality is currently not available in the REST-based Cards API). | Yes |

## 2.9 XML Markup

Please note that certain characters are reserved for XML markup. When an XML parser encounters a reserved character, it assumes it has encountered an element, entity or markup statement. The following examples of reserved characters, and what you should replace this with if you need to include that character as data in the XML file:

| Reserved character | What you should use |
| --- | --- |
| < | &lt; |
| > | &gt; |
| & | &amp; |
| ' | &apos; |
| " | &quot; |