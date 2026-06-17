# 4 File Format and File Versions

The table below lists the fields supported in each data format version and file format type of the card generation file.

| XMLTAG | V10 | V11 | V12 | Included in Full File? | Null Values Allowed? | Included in Customer Cut-down File ? \*\* |
| --- | --- | --- | --- | --- | --- | --- |
| <CARDGEN> |  |  |  | Yes | N/A | Yes |
| [<CARDSUM>](XML_Fields.htm#%3CCARDSUM) |  |  |  | Yes | N/A | Yes |
| <DATA\_FORMAT\_VERSION> |  |  |  | Yes | No | Yes |
| <FILEDATE> |  |  |  | Yes | No | Yes |
| <FILETIME> |  |  |  | Yes | No | Yes |
| <NO\_OF\_CARRIERS> |  |  |  | Yes | No | Yes |
| <NO\_OF\_CARDS> |  |  |  | Yes | No | Yes |
| <NO\_OF\_PRODUCTS> |  |  |  | Yes | No | Yes |
| <TXREF> |  |  |  | Yes | No | Yes |
| <ORDER\_REF> |  |  |  | Yes | Yes | Yes |
| [<PRODUCT>](XML_Fields.htm#%3CPRODUCT) |  |  |  | Yes | N/A | Yes |
| <PRODUCT\_REF> |  |  |  | Yes | No | Yes |
| [<RECORD>](XML_Fields.htm#%3CRECORD%3E) |  |  |  | Yes | N/A | Yes |
| <REQUEST\_TYPE> |  |  |  | Yes | No | Yes |
| <UID> |  |  |  | Yes | No | Yes |
| <CUST\_ACCNO> |  |  |  | No | Yes | Yes |
| [<CARRIER>](XML_Fields.htm#%3CCARRIER) |  |  |  | Yes | N/A | Yes |
| <TITLE> |  |  |  | Yes | Yes | Yes |
| <FNAME> |  |  |  | Yes | Yes | Yes |
| <SNAME> |  |  |  | Yes | Yes | Yes |
| <ADD1> |  |  |  | Yes | Yes | Yes |
| <ADD2> |  |  |  | Yes | Yes | Yes |
| <ADD3> |  |  |  | Yes | Yes | Yes |
| <ADD4> |  |  |  | Yes | Yes | Yes |
| <CITY> |  |  |  | Yes | Yes | Yes |
| <POSTCODE> |  |  |  | Yes | Yes | Yes |
| <MOBILE> |  |  |  | Yes | Yes | No |
| <COUNTRY> |  |  |  | Yes | Yes | Yes |
| <BULK\_ADD1> |  |  |  | Yes | Yes | Yes |
| <BULK\_ADD2> |  |  |  | Yes | Yes | Yes |
| <BULK\_ADD3> |  |  |  | Yes | Yes | Yes |
| <BULK\_CITY> |  |  |  | Yes | Yes | Yes |
| <BULK\_COUNTY> |  |  |  | Yes | Yes | Yes |
| <BULK\_POSTCODE> |  |  |  | Yes | Yes | Yes |
| <BULK\_COUNTRY> |  |  |  | Yes | Yes | Yes |
| <CARRIER\_TYPE> |  |  |  | Yes | No | Yes |
| <CARRIER\_LOGO\_ID > |  |  |  | Yes | Yes | Yes |
| <DELV\_METHOD> |  |  |  | Yes | No | Yes |
| <DELV\_CODE> |  |  |  | Yes | Yes | Yes |
| <FULFIL1> |  |  |  | Yes | Yes | Yes |
| <FULFIL2> |  |  |  | Yes | Yes | Yes |
| <LANG> |  |  |  | Yes | Yes | Yes |
| [<CARD>](XML_Fields.htm#%3CCARD%3E) |  |  |  | Yes | N/A | Yes |
| <TYPE> |  |  |  | Yes | No | Yes |
| <CURRENCY> |  |  |  | Yes | No | Yes |
| <TRACK1> |  |  |  | Yes | No | No |
| <TRACK2> |  |  |  | Yes | No | No |
| <TRACK3> |  |  |  | Yes | Yes | Yes |
| <EMBOSS\_PAN> |  |  |  | Yes | No | Yes\*\*\* |
| <PASSCODE> |  |  |  | No | No | Yes |
| <EMBOSS\_NAME> |  |  |  | Yes | Yes | Yes |
| <EMBOSS\_START> |  |  |  | Yes | No | Yes |
| <EMBOSS\_EXPIRY> |  |  |  | Yes | No | Yes |
| <EMBOSS\_CVC2> |  |  |  | Yes | No | No |
| <EMBOSS\_LINE4> |  |  |  | Yes | Yes | Yes |
| <THERMAL\_LINE1> |  |  |  | Yes | Yes | Yes |
| <THERMAL\_LINE2> |  |  |  | Yes | Yes | Yes |
| <IMAGE\_ID> |  |  |  | Yes | Yes | Yes |
| <LOGO\_FRONT\_ID> |  |  |  | Yes | Yes | Yes |
| <LOGO\_BACK\_ID> |  |  |  | Yes | Yes | Yes |
| <QRCODE> |  |  |  | Yes | Yes | Yes |
| <PINBLOCK> |  |  |  | Optional | Yes | No |
| [<CHIP>](XML_Fields.htm#%3CCHIP%3E) |  |  |  | Conditional \* | N/A | No |
| <TYPE> |  |  |  | Conditional \* | Yes | No |
| <PAN> |  |  |  | Conditional \* | Yes | No |
| <PAN\_SEQ> |  |  |  | Conditional \* | Yes | No |
| <NAME> |  |  |  | Conditional \* | Yes | No |
| <START\_DATE> |  |  |  | Conditional \* | Yes | No |
| <EXPIRY\_DATE> |  |  |  | Conditional \* | Yes | No |
| <SERVICE\_CODE> |  |  |  | Conditional \* | Yes | No |
| <CHIP\_TRACK\_1> |  |  |  | Conditional \* | Yes | No |
| <CHIP\_TRACK\_2> |  |  |  | Conditional \* | Yes | No |
| <CHIP\_TRACK\_1\_MSD\_CL> |  |  |  | Conditional \* | Yes | No |
| <CHIP\_TRACK\_2\_MSD\_CL> |  |  |  | Conditional \* | Yes | No |
| <PINBLOCK> |  |  |  | Conditional \* | Yes | No |

\* Conditional - depends on the card type whether present. Will not be present for Magstripe only cards.

\*\* Cut-down file - sent on request to the Program Manager, excludes fields containing cardholder sensitive data. This file may contain an additional `<CUST_ACCNO >` field.

\*\*\* The `<EMBOSS_PAN>` field is only included in the *cut-down format with clear PAN*. See [File Formats](../Getting_Started/About_CardGenerationFile.htm#File2).