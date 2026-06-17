# Document History

| Version | Date | Description | Revised by |
| --- | --- | --- | --- |
| 12.9 | 22/05/2026 | Updated the office address to reflect the London Thredd, United Kingdom office relocation and new web address. See [Contact Us](Contact.htm). | SH |
| 31/03/2026 | Updated the maximum length of the `FNAME` and `SNAME` fields to 30 characters. See [XML Fields](Card_Generation_Interface_Specification/XML_Fields.htm). | JB |
| 01/07/2025 | Updated the maximum length of the `THERMAL_LINE1` field to 120 characters. Clarified the deadline for making amendments to the card file and how to change the frequency of the card file generation. | SH |
| 19/06/2025 | Added [FAQ](FAQs.htm) section. | KD |
| 17/06/2025 | Updated the maximum length of the `THERMAL_LINE2` field to 70 characters. | SH |
| 03/06/2025 | Added details around scheduling of the card generation file and how records are added to this file. See [About the Card Generation File](Getting_Started/About_CardGenerationFile.htm). | WS |
| 25/03/2025 | Updated the maximum length of the `TITLE` field to 4 characters, and the `SNAME` field to 20 characters. | WS |
| 11/02/2025 | Added references to Thredd Portal, our new web application for managing your cards and transactions. | JB |
| 14/11/2024 | Separated the [XML Fields](Card_Generation_Interface_Specification/XML_Fields.htm) table into sections and added examples. | PC |
| 15/08/2024 | Updated the maximum length of the `BULK_ADD1`, `BULK_ADD2` and `BULK_ADD3` fields to 100 characters. See [XML Fields](Card_Generation_Interface_Specification/XML_Fields.htm). | WS |
| 24/06/2024 | Updated the [company address](Contact.htm). | PC |
| 12.8 | 08/04/2024 | Updates to content to align with taxonomy updates on our Documentation Portal. Added details of Thredd REST-based Cards API fields which provide equivalent functionality to the web services SOAP API. | WS |
| 07/02/2024 | Added details of additional values in the `DELV_METHOD` field. See [XML Fields](Card_Generation_Interface_Specification/XML_Fields.htm). | WS |
| 26/01/2024 | Added details of changes to the available file formats. See [File Formats](Getting_Started/About_CardGenerationFile.htm#File2). | WS |
| 12.7 | 27/06/2023 | Added details of relevant ISO specifications that provide additional details on some field formats. See [About this Document](Getting_Started/About.htm). | WS |
| 31/05/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to new company name and brand identity. | JB |
| 12.6 | 07/01/2023 | Added new [Example Files](Card_Generation_Interface_Specification/Example_File.htm) of both cut-down and full file formats, and a new [File Format and File Versions](Card_Generation_Interface_Specification/File_Versions.htm) section with details of fields included with each file format and data format version. | WS |
| 21/12/2022 | Updated numbering in the Table of Contents | MW |
| 01/12/2022 | Updated Copyright Statement. | MW |
| 12.5 | 12/10/2022 | Added details of the file naming conventions for both cloud and on-premise Thredd solutions. See [File Naming Conventions](Getting_Started/About_CardGenerationFile.htm#File). | WS |
| 28/09/2022 | Clarified customer file and data format options; updates to `TYPE` and `CARRIER_TYPE` elements. | AL |
| 12.4 | 12/08/2022 | New guide layout and HTML version now available | PC |
| 12.3 | 11/08/2022 | The values in the `QRCode` field can now be updated using Web Services. Field size updated from 50 to 100 characters. | WS |
| 12.2 | 20/08/2021  07/09/2021 | `PRODUCT_REF` field maximum length updated to 50 characters.  Thredd office address update | WS |
| 12.1 | 24/05/2021 | Review and update to language. | WS |
| 12.0 | 13/05/2021 | New Guide template and layout. Added section on XML reserved markup characters. | WS |
| 11.01 | 17/12/2020 | Clarification of usage of `BULK_ADD` fields and `DELV_CODE` (bulk address and delivery code)  No change to file layout. | IF |
| 11.00 | 10/03/2020 | Added MOBILE to CARRIER section. Only appears for version 11.00 and higher. | IF |
| 10.02 | 10/03/2020 | Updated description of `TRACK2` and `CHIP_TRACK_2` for VISA. Added 00000 to each. | IF |
| 10.01 | 16/01/2020 | Clarified descriptions of all CHIP Track data fields, to aid understanding of the usage of them:  `CHIP_TRACK_1`, `CHIP_TRACK_2`, `CHIP_TRACK_1_MSD_CL`, `CHIP_TRACK_2_MSD_CL`  Corrected the description of the `PINBLOCK` field, and an example is supplied.  Clarified `COUNTRY` and `BULK_COUNTRY` code values.  Clarified `SERVICE_CODE` values.  Added description for `PAN` and `PAN_SEQ` values.  Table headings now repeated on each page and prevent rows from breaking across pages if possible. | MD |
| 10.0 | 26/03/2019 | Added `BULK_COUNTY` to the `CARRIER` section | IF |
| 9.03 | 21/03/2016 | Corrected max length of TRACK1 and updated description  Corrected max length of TRACK2 and updated description  Corrected max length of TRACK3 and updated description  Corrected max length of CHIP\_TRACK\_1  Corrected max Length of CHIP\_TRACK\_2  Corrected max length of CHIP NAME  Corrected max length of CHIP\_TRACK\_1\_MSD\_CL  Corrected max length of CHIP\_TRACK\_2\_MSD\_CL  Updated list of possible CARD TYPEs.  Updated list of possible CHIP TYPEs  No change to file layout. | MD |
| 9.02 | 4/03/2016 | Clarified file naming convention further.  No change to file layout. | IF |
| 9.01 | 18/01/2016 | Added documentation about PIN block format, no change to file layout. | IF |
| 9 | 15/12/2015 | Corrected File Naming convention  Added new optional tag CHIP\_TRACK\_1\_MSD\_CL |  |
| 8.02 | 30/04/2015 | Changed length and description of BULK\_COUNTRY  Increased length of REQUEST\_TYPE and added new options for PIN Mailers |  |
| 8.01 | 19/01/2015 | Corrections to spec:  Track1 increased to 79 |  |
| 8 | 9/10/2014 | Added PINBLOCK as an optional element in the CARD structure |  |
| 7 |  | Moved REQUEST\_TYPE from <PRODUCT> container to <RECORD>  CHIP\_TRACK\_1 will be present for Mastercard AND VISA  Detailed contents of Track data  Moved LANG to its correct position    Added new optional tag CHIP\_TRACK\_2\_MSD\_CL |  |
| 6 | 03/09/2013 | Added LANG to CARRIER element  Added CARRIER\_LOGO\_ID to CARRIER element  Added QRCODE to CARD element  Changed all CARRIER  elements to allow NULLs  Increased  maximum length of Track 1 to show maximum length Thredd will currently output . N.B. ISO specifications allow for maximum of 79 in Track 1  Added CHIP\_TRACK\_1 (only for VISA cards)  Changed COUNTRY from Varchar(20) to char(3) Numeric ISO Country code  Added CVV1 to sample Track 1 layout | IF |
| 5.01 | 26/03/2013 | Added ORDER\_REF to CARDSUM element | IF |
| 5 | 08/02/2013 | Added new fields to support Bulk Delivery Address | IF |
| 4.01 | 10/09/2012 | Replaced <ADD5> with <CITY> in the <CARRIER> element. Clarified Country ISO code.  Added XML closing tags for clarity. | IF |
| 4.0 | 28/02/2012 | Added new fields to support Bulk Delivery, Simplex Line 4, Currency, Thermal Lines 1 & 2, Front & Logo images.  Defined maximum field sizes that were not already defined. | IF |