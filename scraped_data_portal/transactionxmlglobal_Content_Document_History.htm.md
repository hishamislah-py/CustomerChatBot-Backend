# Document History

This section provides details of what has changed since the previous document release.

| Version | Date | Reason | Revised by |
| --- | --- | --- | --- |
| 2.1.5 | 06/11/2025 | The following attributes under the TXN element are now optional: `cardholderpresent`, `cardpresent`, `cardinputmethod`, `cardauthmethod`, and `cardauthentity`. These attributes under the Term element are also now optional: `inputcapability` and `authcapability`. See [Sub-elements and Attributes](Schema/Sub_Elements_and_Attributes.htm#SchemeSe). | KD |
| 23/10/2025 | Removed all references to MaskedPAN. | KD |
| 24/09/2025 | Clarified descriptions of `LocalDate` to specify that it is the date and time within the local timezone. See [Sub-elements and Attributes](Schema/Sub_Elements_and_Attributes.htm#LocalDat) as an example. | KD |
| 28/07/2025 | Added new schema where the `cardholderpresent`, `cardpresent`, and `cardinput` to include empty fields, to allow for Null support. Updated the the tables for these fields in the Attributes section. See [Transaction XML Schema](Reference/Transaction_XML_Schema.htm) and [Sub-Elements and Attributes](Schema/Sub_Elements_and_Attributes.htm#Txn) | KD |
| 12/06/2025 | Added new Transaction XML schema where country and currency codes are removed (see [Transaction XML Schema](Reference/Transaction_XML_Schema.htm)). Removed country and currency codes reference sections. | KD |
| 12/06/2025 | Added Mastercard Reason Codes 7680 and 7681. See [Message Reason Codes](Reference/Message_Reason_Codes.htm). | JB |
| 30/04/2025 | Updated the description of the SchemeSettlementDate element. See [Sub-elements and Attributes](Schema/Sub_Elements_and_Attributes.htm#SchemeSe). | WS |
| 10/04/2025 | Added currency code for the Caribbean Guilder currency (XCG) for Curacao and Sint Maartens that replaces Netherlands Antillean guilder (see [ISO Currency Codes](Reference/ISO_Currency_Codes.htm)). Added Curacao and Sint Maartens to the currency list for this new currency. | KD |
| 13/02/2025 | Added references to Thredd Portal, our new online portal for managing your cards and transactions. | KD |
| 06/02/2025 | For the [Transaction XML](Reference/Transaction_XML_Schema.htm#top) schema child elements, amended data types and removed child elements that are no longer in use. Amended and removed child elements in various records. | KD |
| 28/01/2025 | Updated the description of `LocalDateUTC` in [CardAuthorisation](Schema/CardAuthorisation.htm) and [CardFinancial](Schema/CardFinancial.htm) to indicate that it is the time and date of the matching authorisation. Added `LocalDateUTC` with examples to [Sub-Elements and Attributes](Schema/Sub_Elements_and_Attributes.htm). | KD |
| 13/12/2024 | Updated FIID Element to indicate that it is not required. See [CardChrdBackRepRes](Schema/CardChrgBackRepRes.htm) | KD |
| 11/12/2024 | Updated the maximum length of the `location` field in the `Term` element to 128 characters. See [Sub-elements and Attributes: Term](Schema/Sub_Elements_and_Attributes.htm#Term). | WS |
| 21/11/2024 | Added a new attribute called *TTI* (Transaction Type Identifier) to the *Txn* element. Updated minimum length requirement of PAN in <Card> to 14 digits.  Added new ISO currency code: 924. | KD |
| 04/11/2024 | Updated the description of the `Desc` field maximum value to 500 characters. See [Sub-elements and Attributes > Desc](Schema/Sub_Elements_and_Attributes.htm#Desc). | WS |
| 23/07/2024 | In the [CardChrgBackRepRes](Schema/CardChrgBackRepRes.htm) element, clarified that `FIID`, `RIID`, and `ChargebackRefNum` are populated only for Mastercard chargebacks. | WS |
| 02/07/2024 | Updated the [company address](Contact.htm). | PC |
| 2.1.4 | 19/06/2024 | Added descriptions of the different types of chargeback records that can be provided in the [CardChrgBackRepRes](Schema/CardChrgBackRepRes.htm) element. | WS |
| 24/05/2026 | Changed the `ReasonCode` field in the [CardFinancial](Schema/CardFinancial.htm) element from mandatory to *If Applicable*. | WS |
| 21/06/2023 | Added new values to the CashType attribute. See [Sub-elements and Attributes > CashCode](Schema/Sub_Elements_and_Attributes.htm#Cash).  Added details of Visa Dispute Reason Codes; added Mastercard Reason Codes 1403 and 1404. See [Message Reason Codes](Reference/Message_Reason_Codes.htm). | WS |
| 07/06/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to new company name and brand identity. | WS |
| 2.1.3 | 14/03/2023 | Added a new attribute called *TTI* (Transaction Type Identifier) to the *Txn* element in the [CardFinancial](Schema/CardFinancial.htm) record type. See the [Txn](Schema/Sub_Elements_and_Attributes.htm#Txn) sub-element. | WS |
| 08/03/2023 | Updates to the Transaction XML data schemas to change the data type of *PresentmentID* from *unsigned Int* to *unsigned Long*. Added a new currency code value of 157 (CNH) to the *ISOCurrencyCode* type in the schema file. See [Transaction XML Schema](Reference/Transaction_XML_Schema.htm). | WS |
| 28/02/2023 | Added Chinese Offshore Renminbi (currency code CNH) to the list of supported currencies. See [Currency Codes](Reference/ISO_Currency_Codes.htm). | WS |
| 20/02/2023 | Updated [XML Schema](Reference/Transaction_XML_Schema.htm) version. Trace *auditno* attribute changed from required to optional. See PRN-138. | WS |
| 2.1.2 | 17/02/2023 | Updated the description of the Trace element to clarify its usage. See [Trace](Schema/Sub_Elements_and_Attributes.htm#Trace).  Updated the section [Matching Transaction XML Records to EHI Records](Getting_Started/Transaction_Matching.htm) to remove reference to use of *Trace* element as a unique identifier. | WS |
| 25/01/2023 | Update to the description of the XML report file naming convention. See [Transaction Data Files](Getting_Started/Transactional_Data_Files.htm). | WS |
| 20/01/2023 | Update to description of frequency of XML reports in [FAQs](FAQs.htm) section. | WS |
| 01/12/2022 | Updated the Copyright Statement. | MW |
| 2.1.1 | 28/10/2022 | The maximum length of the *DE94\_Txn\_Orig\_ID* field has been updated to 16. See [Transaction XML Schema](Reference/Transaction_XML_Schema.htm). | WS |
| 27/10/2022 | Added a description of the [Thredd 16-digit public token](Schema/Sub_Elements_and_Attributes.htm#GPS). | WS |
| 12/10/2022 | Updates to the transaction XML filename format to include details of the applicable Production environment. See [Transactional Data Files.](Getting_Started/Transactional_Data_Files.htm) | WS |
| 23/09/2022 | Update to the table [Matching Transaction XML Records to EHI Records](Getting_Started/Transaction_Matching.htm#Matching). | WS |
| 2.1.0 | 21/09/2022 | New transaction XML schema 1.45: In the *CardAuthorisation* record, the *Apprcode* element has been updated to nillable="true"  Removed element: *FXConversion* | WS |
| 08/09/2022 | Added a new [Currency Code](Reference/ISO_Country_Codes.htm), SLE, for the new Sierra Leonean leone. | WS |
| 30/08/2022 | A new record type called *VFC* (Visa Fee Collection) has been added to the *MasterCardFee* element. See PRN-85.  The maximum length of the *DE94\_Txn\_Orig\_ID* data element has been updated to 16. See PRN-85. | WS |
| 2.0.9 | 01/09/2022 | Updated [CardEvent](Schema/CardEvent.htm) to reflect report handling for CardEvent records that exceed 2GB in size. See PRN-120. | MW |
| 27/07/2022 | In the [AgencyAccount](Schema/Sub_Elements_and_Attributes.htm#Agency) element, the *sortcode* and *bankacc* attributes have been updated to support alphanumeric characters. See PRN-118.    In the [CashCode](Schema/Sub_Elements_and_Attributes.htm#Cash) element, the *CashType* attribute has been updated to include *CHAPS*. See PRN-117. | WS |
| 05/07/2022 | Updates made to [Introduction](Getting_Started/Introduction.htm) (QMR section) and [Transactional Data Files](Getting_Started/Transactional_Data_Files.htm) (Sending of Files section). | JB |
| 2.0.8 | 09/05/2022 | Added a link to the [Downloads](https://docs.thredd.ai/Downloads.htm) page on the Documentation Portal, where you can view and download upcoming/future schema versions. | WS |
| 06/04/2022 | New [WalletTransaction](Schema/WalletTransaction.htm) element added to the transaction XML. See PRN-100.    In XSD schema file, changed the type of *AuthTxnID*  from *unsignedint* to *unsignedlong*;    Added the two-digit country code SS (South Sudan) to the *ISOCountryCode* list. See [Transaction XML Schema](Reference/Transaction_XML_Schema.htm). See PRN-111.    For MasterCardFee, ApprovedAgencyBanking, DeclinedAgencyBanking and DeclinedAgencyBanking, the [Desc](Schema/Sub_Elements_and_Attributes.htm#Desc) element can be empty (nillable="true"). See PRN-110.    Correction: the [FeeClass](Schema/Sub_Elements_and_Attributes.htm#FeeClas) type of 0 is a legacy option which will never appear in a transaction XMLrecord and reference to it has been removed from the guide.    Updated the description of `FeeAmt` in the [Card Fee](Schema/CardFee.htm) element. | WS |
| 2.0.7 | 16/03/2022 | Processing Code (*ProcCode*) = 39 is now used to identify an [Account VerificationClosed A type of authorisation transaction which is intended to confirm that the account is genuine and active. Account Verifications are always for a zero amount, so only appear in Authorisation messages and never in clearing messages.](#) transaction. See the [TxnCode](Schema/Sub_Elements_and_Attributes.htm#TxnCode) field in the *CardAuthorisation* element. See PRN-102.    Clarified that the fee amount (`FeeAmt`) in the [CardFinancial](Schema/CardFinancial.htm) record is the sum total of any rate fee and fixed fee applied to the transaction. | WS |
| 2.0.6 | 04/02/2022 | Removed reference to the *ResponseFinancial* element in the [XML Schema](Getting_Started/Transactional_Data_Schema.htm). | WS |
| 04/01/2022 | The *ReportedToSAFE* event type has been added to the transaction [XML Schema](Reference/Transaction_XML_Schema.htm) file. | WS |
| 13/12/2021 | The RecordType element has been updated to include a new Visa Fee Collection (VFC) value, and the `<DE94_Txn_Orig_ID>` element maximum length has increased from 6 to 13. See PRN-85. | AL |
| 2.0.5 | 19/10/2021 | The CardEvent primary element has been updated to include a new *ReportedToSAFE* event type; this provides a `transactionid` attribute to identify a [SAFE reportingClosed You can report fraudulent transactions to Mastercard by creating a new fraud event in Mastercom, using their SAFE reporting facility (now referred to as the Mastercard Fraud and Loss Database).](#) transaction, but will be blank for other event types. For examples, see the [Event](Schema/Sub_Elements_and_Attributes.htm#Event) sub-element. See PRN-75.    FXConversion record updated with *<FXRateBilled>* | WS |
| 2.0.4 | 04/11/2021 | For a Visa purchase with Cashback, Thredd now sends the value of *ProcCode* as 09 (instead of 00) and includes the cashback amount in the *Additional\_Amt\_DE54* field. Thredd has standardised the format of the [Additional\_Amt\_DE54](Schema/Sub_Elements_and_Attributes.htm#Addition) element to use the format provided by GCMS IPM / Visa Base 2, which contains only the data (a multiple of 20 characters). See PRN-72. | WS |
| 15/10/2021 | Added a new primary element *FXConversion* to indicate Foreign Exchange (FX) rate conversion. This contains the sub-elements BookingType and BookingStatus. | AL |
| 2.0.3 | 20/08/2021  15/09/2021 | Added a new field `<LocalDateUTC>` to [CardAuthorisation](Schema/CardAuthorisation.htm) and [CardFinancial](Schema/CardFinancial.htm) records. This field contains the *LocalDateUTC* data that Thredd receives from Mastercard and Visa. See PRN-59.  Added new appendix [Load Source](Reference/Load_Sources.htm), which provides updated details of possible values for the source of a Load or Unload request.  Removed value 0 from the `type` attribute in the [FeeClass](Schema/Sub_Elements_and_Attributes.htm#FeeClas) element, as this value is no longer supported.  Updates to [Card Status Codes](Reference/Card_Status_Codes.htm) to include new values G1-G9. See PRN-48. | WS |
| 2.0.2 | 26/07/2021 | Updates to include clarification on usage of `actioncode` and `responsecode` fields in the [Response](Schema/Sub_Elements_and_Attributes.htm#Response) element.  New `<PaymentToken>` field added to [CardAuthorisation](Schema/CardAuthorisation.htm) and [CardFinancial](Schema/CardFinancial.htm) records to help support Programme Manager Apple-Pay Reporting requirements. See PRN-49. | WS |
| 2.0.1 | 16/06/2021 | Updates to include clarification around transaction reporting times and cycle times. See [Transactional Data Files](Getting_Started/Transactional_Data_Files.htm).  Information on XML reports available for issuers. See [Introduction](Getting_Started/Introduction.htm).  New details of fields to use for matching transaction XML records to EHI records and matching financials to authorisations. See [Transaction Matching](Getting_Started/Transaction_Matching.htm)  The `BillAmt` rate and the `SettlementAmt` rate has been updated to show 9 decimal places. See PRN-44. | WS |
| 2.0 | 25/04/2021 | Major revamp to look and feel and organisation of the guide. Rewrite of content to simplify and make the guide easier to use.  Updates to description of the `<Amt>` field.  Added new element: FXConv in [CardAuthorisation](Schema/CardAuthorisation.htm) and [CardFinancial](Schema/CardFinancial.htm) primary elements. See PRN-37.  Change to the values of the `TxId` field in the [CardFee](Schema/CardFee.htm#top) record. See PRN-41. | WS |
| 1.41 | 29/12/2020 | Added new elements Sender and Receiver in [CardAuthorisation.](Schema/CardAuthorisation.htm) | DM |
| 1.40 | 24/12/2020 | Added new RecordType element and other data changes in MastercardFee. | DM |
| 1.39 | 08/12/2020 | Added new BSA element in [CardFinancial](Schema/CardFinancial.htm). | DM |
| 1.38 | 23/10/2020  18/02/2021 | Corrected value of âRepeatâ in example provided.  Updated list of cardauthmethods and cardauthentity | DM  IF |
| 1.37 | 22/10/2020 | Removed IssuerReferenceNumber, added ChargebackRefNum | DM |
| 1.36.1 | 29/09/2020 | Banking File data not mandatory. | DM |
| 1.36 | 21/08/2020 | Added new IssuerReferenceNumber element in Chargeback. | DM |
| 1.35 | 19/08/2020 | Added new value2 attribute in Financial and Chargeback. | DM |
| 1.34 | 27/07/2020 | Corrected PAN (Primary Account Number) length description. | VS |
| 1.33 | 24/07/2020 | DEV\_REPORTING-396 changes added | DM |
| 1.32 | 15/05/2020 | SettlementIndicator available for MC too. | DM |
| 1.31 | 06/05/2020 | Added new element Additional\_Amt\_DE54 | DM |
| 1.30 | 04/05/2020 | Corrected CardFianncial/AuthID description | DM |
| 1.29 | 09/04/2020 | Added new element SettlementIndicator | DM |
| 1.28 | 09/04/2020 | Added recon field in CardFee, productid in MasterCardFee. | DM |
| 1.27 | 25/03/2020 | New 5 fields added in Chargeback section: SettlementCycle, ReconciliationDate, ReconciliationCycle, Usage and Pending\_Billing\_Amount | DM |
| 1.26 | 02/03/2020 | Some fields in MasterCardFee that shows Chargeback data can be blank. Updated those details in this revision. | DM |
| 1.25 | 17/12/2019 | Updated inputcapability, authcapability, cardholderpresent, cardpresent, cardinputmethod, cardauthmethod and cardauthentity. | DM |
| 1.24 | 5/11/2019 | Updated Function\_Code\_024 of MastercardFee | DM |
| 1.23 | 24/10/2019 | Updated datatypes for AuthID, AdjustId, ChgbackRepresId, CardFeeId, TxId, FinID and LoadUnloadId, BankingId | HC |
| 1.22 | 23/11/2018 | Documented Agency Banking-related elements and attributes.  Formatting. | IF |
| 1.21 | 19/10/2018 | Clarified Mastercard-only elements CCAAmount and SettlementAmount | IF |
| 1.20 | 19/09/2018 | Added 4.2.59 - AdjustType | DM |
| 1.19 | 31/05/2018 | Added 4.2.58 - SchemeSettlementDate | SN |
| 1.18 | 16/04/2018 | Updated 4.1.4 â CardFeeId description | IF |
| 1.17 | 06/03/2018 | Updated 3.1.2 â Reporting Content. | IF |
| 1.16 | 27/02/2018 | Removed RCC attribute from Classification.  Altered proccode attribute in TxnCode | SM |
| 1.15 | 26/09/2017 | Updated the Account attribute ânoâ description    Many different elements added to the MasterCard Fee section so that it matches the current file output.    Added Recon, Settlement, PDS0105, and FunctionCode sub elements for the MasterCard Fee change above.    Changed description of CardFee TxId element. | SM  IF |
| 1.14 | 16/08/2017 | Added new Fee Class Code value 1.  Updated permitted values of Fee Class element âtypeâ and âcodeâ attributes for Card Financials.  Corrected the schedule to daily not Mon - Fri | SM      SM |
| 1.11 | 21/07/2016 | Case of XML Element âAccountâ, attributes âNoâ and âTypeâ changed to ânoâ and âtypeâ, in all recordtypes (âCardAuthorisationâ, âCardFinancialâ etc..)    Case of XML Element âResponseâ, attributes âApprovedâ, âActioncodeâ, âResponsecodeâ and âAdditionalDescâ are changed to: âapprovedâ, âactioncodeâ, âresponsecodeâ and âadditionaldescâ respectively, in the âCardAuthorisationâ record only.      Removed ResponseFinancial element description    Documented memberID attribute of FeeClass    Added CCAAmount to CardFinancial | IF |
| 1.10 | 26/05/2016 | Changed Max Length of CardLoadUnload.MerchCode from 15 to 30. | IF |
| 1.09 | 28/04/2016 | Various minor corrections | IF |
| 1.08 | 19/10/2015 | Documented Mastercard.FeeClass element, including new membered sub-element | IF |
| 1.07 | 01/06/2014 | Updated description of CardFee TxId | IF |
| 1.06 | 01/03/2014 | Added new CardFee FeeClass Code value 6000 | IF |
| 1.05 | 05/04/2013 | Clarified use of CardEvent Type element    Added VisaCard to Account Element    Clarified requirement of actioncode, responsecode and AdditionalDesc attributes of Response element.    Clarified Load Type attribute | IF |
| 1.04 | 22/03/2013 | Amended data type of Load Type element | IF |
| 1.03 | 15/03/2013 | Updated SettlementDate definition in CardChrgBackRepRes | IF |
| 1.02 | 14/03/2013 | Moved LoadUnloadId in CardFee. Added CardEvent documentation. Changed ProgramID definition. | IF |
| 1.01 | 13/03/2013 | Added CycleNumber, FeeAmt, FeeClass to CardFinancial Element. | IF |
| 1.00 | 12/10/2012 | First draft | IF |