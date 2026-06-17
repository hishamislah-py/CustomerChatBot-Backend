# 4.20 Misc\_TLV\_Data Field

The `Misc_TLV_Data` field is used for sending rarely used fields that can normally be ignored.

For the format of this field, see section [Data Types](../Requirements/Data_Types.htm): *TLV10*.

The table below lists the tag values and their meaning.

Thredd may add tags at any time (without a specification update). To avoid errors, your systems should ignore any unknown tags.

| Tag | Value Format | Description |
| --- | --- | --- |
| V125030003 | N(16,16) | Visa Original Trace ID, exactly as received from Visa.  For information only â Traceid\_Original is the recommended field to use instead, this can be used if you suspect Traceid\_Original is not as expected. |
| V1045D0082 | AN(10) | 35AN Plan Registration System Identifier. Contains the plan registration system identifier value to identify the transaction as a Visa Installment Solutions transaction. This identifier is a10-character alphanumeric unique value. (Note: ISO definition allows up to 35 characters, but Visa will send 10 characters). |
| CGBRDEBT01 | ANS(1,35) | UK Debt repayment - Recipient Last Name  (Specific to UK country) |
| CGBRDEBT02 | ANS(1,10) | UK Debt repayment - Recipient Postal Code  (Specific to UK country) |
| CGBRDEBT03 | N(8,8) | UK Debt repayment - Recipient Date of Birth YYYYMMDD  (Specific to UK country) |
| CGBRDEBT04 | ANS(1,20) | UK Debt repayment - Recipient Account Number  (Specific to UK country) |
| G00001S0*nn* | ANS(1,99) | Sender data obtained from Mastercard authorisation message field 108 and Visa fields 56 and 104. For details, see [Sender and Receiver Tags](#Sender). |
| G00001R0*nn* | ANS(1,99) | Receiver data obtained from Mastercard authorisation message field 108 and Visa fields 56 and 104. For details, see [Sender and Receiver Tags](#Sender). |
| V034xxxxxx | HEX(2,4000) | This field is used by acquirers to indicate if they have appplied any Strong Customer Authentication (SCA) acquirer exemption to the transaction; see the [PSD2 SCA Guide > PSD2 Acquirer Exemptions](https://docs.thredd.ai/psd/Content/PSD2/PSD2_Acquirer_Exemptions.htm).    **Note**: You should not normally need to extract the data in this field, as Thredd already provides this information in the [GPS\_POS\_DATA field](GPS_POS_Data.htm), position 25, [Acquirer Exempt from SCA Indicator](GPS_POS_Data.htm#Acquirer).    Visa Base1 field 34 e-commerce data (complete) is provided as hexadecimals. Each two hexadecimal digits represents one binary byte of data as Thredd received it from Visa. The first two hexadecimals will be the first dataset identifier. Example: *0100078605F14BA74BA7*  For more information on the Visa field 34, refer to the following Visa documents: *VisaNet Authorization-Only Online Messages - Technical Specification* and [Visa PSD2 SCA for Remote Electronic Transactions Implementation Guide](https://www.visa.es/dam/VCOM/regional/ve/unitedkingdom/PDF/sca/Visa-PSD2-SCA-for-Remote-Electronic-Transactions-Implementation-Guide.pdf).    **Note**: If character data is present, the hexadecimal values will be represented as an IBM EBCDIC code page 1148 character (e.g., if Visa provided the letter âxâ in 1 byte, then this is represented here as the hexadecimal value âA7â.). For more information on IBM character sets defined in the EBCDIC code page 1148, see [ibm.com: docs > Character sets.](https://www.ibm.com/docs/en/i/7.3?topic=information-character-sets) |
| Any other value | Anything | Unknown |

Where *nn* represents additional digits.

The following formats are intended for future Mastercard and Visa raw data, if they are required:

| Data Source | Tag Construction plan |
| --- | --- |
| Banknet  (Mastercard online authorisations) | âM' + 3 digit DE + 3 digit subelement + 3 digit subfield |
| Visa Base1  (visa online authorisations) | âV' + 3 digit DE + 2 hexdigit dataset ID + 4 hexdigit Tag  (if sending all datasets, âxxâ will be used as the dataset ID)  (if sending all tags, âxxxxâ will be used as the Tag) |
| GCMS  (Mastercard clearing) | âmâ + 3 digit DE + 4 digit PDS + 2 digit subfield |
| Visa Base 2  (Visa clearing) | âvâ + 2 digit TC + 1 digit TCR + 3 digit start offset + 3 digit end offset |
| Specific to a particular country | âCâ + 3-alpha-country-code + 6 char identifier |
| Other | Initial character will not be any of âMâ,âVâ,âmâ,âvâ,âCâ |

## 4.20.1 Sender and Receiver Tags

The table below provides details of Sender and Receiver data obtained from the Mastercard authorisation message field 108 and Visa fields 56 and 104.

The length of the value precedes the actual value, for example: *G00001S0030007Johnson*, where  *G00001S003* is the tag for last name, *0007* is the tag value length, and *Johnson* is the tag value.

| Misc\_TLV\_Data Tag Name | Description |
| --- | --- |
| G00001S001 | Sender first name |
| G00001S002 | Sender middle name |
| G00001S003 | Sender last name |
| G00001S004 | Sender street address |
| G00001S005 | Sender city |
| G00001S006 | Sender province |
| G00001S007 | Sender country (three character alpha ISO code) |
| G00001S008 | Sender postcode |
| G00001S009 | Sender phone number |
| G00001S010 | Sender date of birth (MMDDYYYY). For example 25011996. |
| G00001S011 | Sender account number (rightmost 4 digits) |
| G00001S012 | Sender identity document (ID) type (00 = passport; 01 = National Identification Card; 02 = Driverâs License; 03 = Government Issued; 04 = Other; 05-10 reserved for future use) |
| G00001S013 | Sender ID number |
| G00001S014 | Sender ID country; three character alpha ISO code (e.g., CYP = Cypress) |
| G00001S015 | Sender ID expiry Date (MMDDYYYY) |
| G00001S016 | Sender nationality (three character alpha ISO code) |
| G00001S017 | Sender birth country (three character alpha ISO code) |
| G00001S018 | Sender account number type. See [Account Number Type](#Account). |
| G00001S0V1 | Sender funds source. See [Source of Funds](#Source). |
| G00001S0V2 | Sender claim code |
| G00001R001 | Receiver first name |
| G00001R002 | Receiver middle name |
| G00001R003 | Receiverlast name |
| G00001R004 | Receiver street address |
| G00001R005 | Receiver city |
| G00001R006 | Receiver province |
| G00001R007 | Receiver country (3 letter country code, e.g., CYP = Cypress) |
| G00001R008 | Receiver postcode |
| G00001R009 | Receiver phone number |
| G00001R010 | Receiver date of birth (MMDDYYYY). For example 12311996. |
| G00001R011 | Receiver account number (rightmost 4 digits) |
| G00001R012 | Receiver identity type (00 = passport; 01 = National Identification Card; 02 = Driverâs License; 03 = Government Issued; 04 = Other; 05-10 reserved for future use) |
| G00001R013 | Receiver ID number |
| G00001R014 | Receiver ID country code (three character alpha ISO code) |
| G00001R015 | Receiver ID expiry date (MMDDYYYY) |
| G00001R016 | Receiver nationality (three character alpha ISO code) |
| G00001R017 | Receiver birth country (three character alpha ISO code) |
| G00001R018 | Receiver account number type. See [Account Number Type](#Account). |

### Account Number Type

| Value | Description |
| --- | --- |
| 0 | Other |
| 1 | RTN + Bank account |
| 2 | IBAN |
| 3 | Card account |
| 4 | Email |
| 5 | Phone number |
| 6 | Bank account number (BAN) + Bank Identification Ð¡ode (BIC) |
| 7 | Wallet ID |
| 8 | Social Network ID |

### Source of Funds

| Value | Description |
| --- | --- |
| 1 | Visa credit |
| 2 | Visa debit |
| 3 | Visa prepaid |
| 4 | Cash |
| 5 | Debit/deposit access accounts other than those linked to a Visacard (includes checking/savings accounts and proprietary debit/ATM cards) |
| 6 | Credit accounts other than those linked to a Visa card (includes credit cards and proprietary credit lines) |

### Example

Sender Data = *0104Adam0703ROM080511A56V10205*

Receiver Data = *0310John Smith*

MiscTLVData = *G00001S0010004AdamG00001S0070003ROMG00001S008000511A56G00001S0V1000205G00001R0030010John Smith*