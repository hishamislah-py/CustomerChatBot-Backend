# Document History

This section provides details of what has changed since in each document release.

| Version | Date | Reason | Revised by |
| --- | --- | --- | --- |
| 1.3 | 13/03/2026 | Updated the description for the [CUSTCODE](Schema/Sub_Elements_and_Attributes.htm#CUSTCODE) field to state that it is the reference for the card and will only have a value if a reference was included in the `CustAccount` field. See [Sub Elements and Attributes.](Schema/Sub_Elements_and_Attributes.htm#CUSTCODE) | GF |
| 09/09/2025 | Added a [new Balance XML schema](Reference/Balance_XML_Schema.htm) where the following attributes include empty fields to support null values: CURRCODE, ACCTYPE, FINAMT, BLKAMT, and AMTAVL. See [Account](Schema/Account.htm) element and [Sub-elements and Attributes](Schema/Sub_Elements_and_Attributes.htm). | KD |
| 12/06/2025 | Added new [Balance XML schema](Reference/Balance_XML_Schema.htm#top) where country and currency codes are removed (see Balance Report XML Schema). Removed country and currency codes reference sections. | KD |
| 01/05/2025 | Added the `MaskedPAN` to the [Card](Schema/Sub_Elements_and_Attributes.htm#MASKEDPA) sub-element. Changed the Balance Report XML schema, and included new examples. See [PRN-222](https://docs.thredd.com/GPSPRN.htm) | KD |
| 10/04/2025 | Added currency code for the Caribbean Guilder currency (XCG) for Curacao and Sint Maartens that replaces Netherlands Antillean guilder (see [ISO Currency Codes](Reference/ISO_Currency_Codes.htm)). Added Curacao and Sint Maartens to the currency list for this new currency. | KD |
| 07/03/2025 | Ensured that all relevant references to the Discover Network are included. | KD |
| 11/02/2025 | Added references to Thredd Portal, our new web application for managing your cards and transactions. | KD |
| 03/02/2025 | Added an FAQ to explain differences between the balance reporting in the balance XML file and the balance in Smart Client for Primary and Secondary cards. See the [FAQs](FAQs.htm). | WS |
| 09/01/2025 | Added descriptions on the REG suffix used in filenames of regenerated reports. See [File Naming Convention](Getting_Started/Balance_Data_Files.htm#File2) | KD |
| 21/11/2024 | Updated minimum length requirement of PAN in <Card> to 14 digits. Added new ISO currency code: 924. See [PRN-196](https://docs.thredd.com/GPSPRN.htm) and [PRN-197](https://docs.thredd.com/GPSPRN.htm) | KD |
| 22/10/2024 | Added Discover card type to the ACCTYPE element in the schema and in the list of [Subelements and Attributes](Schema/Sub_Elements_and_Attributes.htm). See [PRN-194.](https://docs.thredd.com/GPSPRN.htm) | KD |
| 10/10/2024 | Added the MVC token indicator to the [Card](Schema/Card.htm) sub-element, and included a new schema file, and updated examples. See [PRN-192](https://docs.thredd.com/GPSPRN.htm) | KD |
| 1.2 | 05/09/2024 | First version available on the Documentation Portal in HTML | KD |
| 1.1 | 26/06/2024 | Updated the [company address.](Contact.htm) | PC |
| 03/06/2024 | Description change to remove unneeded references to UTC | KD |
| 17/05/2024 | Improved descriptions for UTC Balance XML Reports. Note that the guide has been renamed from Balance XML Reporting guide to distinguish it from the new version where you can receive reports at any time you prefer. | KD |
| 21/03/2024 | Updates to content and graphics to align with taxonomy updates on our Documentation Portal. | KD |
| 31/05/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to reflect new company name and brand identity. | WS |
| 1.0 | 03/02/2023 | First version | WS |