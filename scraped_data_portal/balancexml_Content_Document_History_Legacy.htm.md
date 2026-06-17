# Document History

This section provides details of what has changed since in each document release.

| Version | Date | Reason | Who |
| --- | --- | --- | --- |
| 2.0.6 | 14/05/2026 | Added missing STATCODES values: R0, R1, R3, 1A, 5C, 9G, Z5. See [Card Status Codes](Reference/Status_Codes.htm#top). Refer to the [Downloads](https://docs.thredd.ai/Downloads.htm) page and PRN-299. | KD |
| 20/03/2026 | Updated the description for the [CUSTCODE](Schema/Sub_Elements_and_Attributes.htm#CUSTCODE) field to state that it is the reference for the card and will only have a value if a reference was included in the `CustAccount` field. See [Sub Elements and Attributes.](Schema/Sub_Elements_and_Attributes.htm#CUSTCODE) | GF |
| 23/10/2025 | Removed all references to MaskedPAN. | KD |
| 09/09/2025 | Added a [new Balance XML schem](Reference/Balance_XML_Schema.htm)a where the following attributes include empty fields to support null values: CURRCODE, ACCTYPE, FINAMT, BLKAMT, and AMTAVL. See [Account](Schema/Account.htm) element and [Sub-elements and Attributes](Schema/Sub_Elements_and_Attributes.htm). | KD |
| 12/06/2025 | Added new Balance XML schema where country and currency codes are removed (see [Balance Report XML Schema)](Reference/Balance_XML_Schema.htm#top). Removed country and currency codes reference sections. | KD |
| 10/04/2025 | Added currency code for the Caribbean Guilder currency (XCG) for Curacao and Sint Maartens that replaces Netherlands Antillean guilder (see [ISO Currency Codes](Reference/ISO_Currency_Codes.htm)). Added Curacao and Sint Maartens to the currency list for this new currency. | KD |
| 11/02/2025 | Added references to Thredd Portal, our new web application for managing your cards and transactions. | KD |
| 03/02/2025 | Added an FAQ to explain differences between the balance reporting in the balance XML file and the balance in Smart Client for Primary and Secondary cards. See the [FAQs](FAQs.htm). | WS |
| 21/11/2024 | Updated minimum length requirement of PAN in <Card> to 14 digits. Added new ISO currency code: 924. See [PRN-196](https://docs.thredd.com/GPSPRN.htm) and [PRN-197](https://docs.thredd.com/GPSPRN.htm) | KD |
| 22/10/2024 | Added Discover card type to the ACCTYPE element within the schema. See [PRN-194.](https://docs.thredd.com/GPSPRN.htm) | KD |
| 30/07/2024 | Added Discover Global Network information | PC |
| 26/06/2024 | Updated the [company address.](Contact.htm) | PC |
| 30/05/2024 | Updated name from new Balance XML reports to Global Balance Reports. |  |
| 21/05/2024 | Added details on the time settings in [File Sending Schedule](Getting_Started/Balance_Data_Files.htm#File). | KD |
| 2.0.5 | 17/05/2024 | Changed the title of the guide to reflect that Balance XML reports are new. | KD |
| 10/05/2024 | Improved descriptions of new Balance XML reports. | KD |
| 21/03/2024 | Updates to content and graphics to align with taxonomy updates on our Documentation Portal. | KD |
| 27/02/2024 | Updated the description of the `BLKAMT` field. See the [ACCOUNT](Schema/Account.htm) element. | WS |
| 31/05/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to reflect new company name and brand identity. | WS |
| 2.0.4 | 28/02/2023 | Added Chinese Offshore Renminbi (currency code CNH) to the list of supported currencies. See [Currency Codes](Reference/ISO_Currency_Codes.htm). | WS |
| 25/01/2023 | Update to the description of the XML report file naming convention. See [Balance Data Files](Getting_Started/Balance_Data_Files.htm). | WS |
| 20/01/2023 | Update to description of frequency of XML reports in [FAQs](FAQs.htm) section. | WS |
| 01/12/2022 | Updated the Copyright Statement | MW |
| 2.0.3 | 28/10/2022 | Added a description of the [Thredd 16-digit public token](Schema/Sub_Elements_and_Attributes.htm#GPS). | WS |
| 12/10/2022 | Updates to description of when the balance XML files can be generated.  Updates to the Balance XML filename format to include details of the applicable Production environment. See [Balance Data Files](Getting_Started/Balance_Data_Files.htm). | WS |
| 29/06/2022 | Updates made to Introduction (QMR section) and Transactional Data Files (Sending of Files section). | JB |
| 2.0.2 | 08/04/2022    09/05/2022 | Added the following missing STATCODE values to the XML schema: G1,G2,G3,G4,G5,G6,G7,G8,G9,93,6P,59 & 46. See [Status Codes](Reference/Status_Codes.htm).  New field [PRIMARYTOKEN](Schema/Sub_Elements_and_Attributes.htm#PRIMARYT) added to the [CARD](Schema/Card.htm) element, which shows the full Primary Account Number (PAN) of the card; If this is a secondary card, shows the full PAN of the linked primary card. See PRN-109.  Added the ability to accept empty strings in the [GPSEXPDATE](Schema/Sub_Elements_and_Attributes.htm#GPSEXPDATE).  Added details of the *XMLCutoffUTCtime* setting, which allows you to set the equivalent local midnight cut-off time for receiving balance XML reports if the time zone in your country differs from the UK time. See [Balance Data Files](Getting_Started/Balance_Data_Files.htm). Added a link to the [Downloads](https://docs.thredd.ai/Downloads.htm) page on the Documentation Portal, where you can view and download upcoming/future schema versions. | WS |
| 2.0.1 | 23/08/2021  01/10/2021 | New *GPSEXPDATE* field added to the [CARD](Schema/Card.htm) element. See PRN-60.  Updates to [Card Satus Codes](Reference/Status_Codes.htm). See PRN-48. | WS |
| 2.0 | 09/06/2021 | Major revamp to look and feel and organisation of the guide. Rewrite of content to simplify and make the guide easier to use. | WS |
| 1.08 | 24/07/2020 | Changed SchemeID, ProgramID and statcode as per DEV\_REPORTING-396. | DM |
| 1.07 | 11/05/2020 | Updated Balance Data Files - Reporting Contents Description. | VS |
| 1.06 | 10/06/2019 | Added CRDACCNO description. | IF |
| 1.05 | 08/03/2019 | Added PRODUCTID and LASTUPDATED to the CARD element. | IF |
| 1.04 | 16/04/2018 | Updated Appendix B â Card Status Codes. | IF |
| 1.01 | 12/09/2016 | Added fields for Agency Banking and further corrections and small changes. | IF |
| 1.0 | 23/08/2010 | Initial draft. | IF |