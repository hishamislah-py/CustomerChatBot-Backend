# Action Codes

The following action codes may be returned in the `<ActionCode>` tag of a web service response.

| Code | Description | How is it used? |
| --- | --- | --- |
| 000 | Normal, approve | Indicates success of the web service transaction. |
| 100 | Do not Honour, deny | As required by Issuer. Also used for example in Card Load when the currency in the request does not match the card currency. |
| 101 | Card expired, deny | Checks expiry status of card before allowing certain operations e.g. Load. |
| 104 | Restricted card, deny | Indicates that the card is not in the required status for that service. For example: for [Card Convert](../Web_services_api/Card_Convert_to_Physical.htm), Thredd returns a 104 action code if the status is not â00â ; for [Card PIN Control](../Web_services_api/Card_PIN_Control.htm), Thredd returns a 104 action code if the card status is 41,43,62,83 or 14. |
| 116 | Insufficient funds, deny | Indicates lack of funds to the account, e.g., to cover the fee associated with the request. |
| 118 | No card record, deny | Indicates the PAN/Pubtoken/CustAccount/AccountID in the request has no associated card record in the database. |
| 119 | Transaction not allowed to cardholder, deny | Indicates that the cardholder is not allowed to perform that particular transaction type due to an invalid input value. |
| 120 | Action will exceed allowed system limit | Indicates that any of the card or account amount system limits are exceeded. |
| 121 | Amount limits exceeded or outside valid load range, deny | Indicates that any of the card or account amount limits are exceeded or a load amount falls outside the valid range. |
| 122 | Invalid ExternalAuth | Incorrect External Authorisation (`ExternalAuth`) value. Possible values are: 0 and 1. Empty value defaults to 0. See [Card Create > ExternalAuth](../Web_services_api/Card_Create.htm#ExternalAuth). |
| 123 | Frequency limits exceeded, deny | Indicates that any of the card or account frequency limits are exceeded. |
| 124 | Card already active, deny. | Indicates that an active card is tried to be activated again. |
| 126 | Invalid PIN, deny | Indicates that the supplied PIN does not match our records. |
| 130 | External API unreachable | Indicates when an external API is called e.g. ws\_PINControl when Func=06. |
| 131 | External API returned an error | Indicates when an external API is called e.g. ws\_PINControl when Func=06, and an error is returned. For the actual error, contact Thredd or the external API provider. |
| 140 | Invalid Currency. Currency doesn't match with product configuration. | Indicates when there is a product and currency mismatch for a SEPA payment (when using the Modulr Agency Banking service). |
| 141 | MandateId is missing. | Modulr (Agency Banking Service) |
| 142 | Cancellation Code is missing or invalid. | Modulr (Agency Banking Service) |
| 144 | No entry in the database for the input MandateId. | Modulr (Agency Banking Service) |
| 145 | No mandate details found. | Modulr (Agency Banking Service) |
| 184 | PIN confirmation failed, deny | Indicates when the PIN confirmation does not match the new PIN when attempting to change the PIN. |
| 200 | Card closed, deny & pickup | As required by Issuer |
| 202 | Fraudulent use, deny & pickup | As required by Issuer |
| 208 | Card lost, deny & pickup | Indicates that the card is in Lost status (41). |
| 209 | Card stolen, deny & pickup | Indicates that the card is in Stolen status (43). |
| 210 | Invalid DPAN | Indicates that the supplied tokenised PAN is invalid. |
| 211 | Invalid Payment Token Id | Indicates that the supplied Payment Token id is invalid. |
| 212 | Card and Payment Token details do not match | Indicates that the supplied Card details and Payment Token do not relate. |
| 213 | FPAN status change is successful. DPANs are ignored as they are in irreversible status. | The [FPANClosed Funding PAN. The true 16-digit PAN of the card, which Mastercard/Visa converts when authorisations come through to them from Acquirers on the DPAN.](#) was successfully updated, but the [DPANClosed Device PAN. The PAN value set up on the cardholderâs device. This is not visible to the cardholder, but is the PAN used for the transactions as far as the merchant is concerned.](#) was not updated, as it is in an irreversible status. |
| 214 | No associated Payment Token for the card details supplied | There is no associated Payment Token for the card details supplied. |
| 216 | Either DPAN or PaymentTokenId must be provided | Provide a valid DPAN or `PaymentTokenId` |
| 217 | Invalid `Func` value | Provide a valid value, such as: 00 and 01. |
| 218 | Payment token has no device in the list | No associated device in the system. |
| 219 | Specified device index is not in the list | No Visa device index exists that matches the supplied value of `<DeviceIndex>`. |
| 220 | The device is already in unbound status | You made can attempt to unbind a device that is not bound to any DPAN, |
| 221 | `DeviceIndex` is mandatory when value of `Func` is â01â. | For [Token Device Management](../Web_services_api/Token_Device_Management.htm) (`Ws_Token_Device_Management`), when the token device function requested is to unbind the device, then the Visa device index should be provided. |
| 250 | Banking balance transfer not allowed on account status | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 400 | Addrl1 is missing, Addrl1 is mandatory if âAddressâ fields are being specified. | Reserved for future use |
| 401 | Invalid PostCode | Postcode is not formed from alphanumerics or hyphens |
| 402 | dlvaddr1 is missing, dlvaddr1 is mandatory if âDelivery Addressâ fields are being specified. | Reserved for future use |
| 403 | Invalid dlvpostcode | Postcode is not formed from alphanumerics or hyphens. |
| 404 | Workaddr1 is missing, Workaddr1 is mandatory if âWork Addressâ fields are being specified. | Reserved for future use |
| 405 | Invalid Workpostcode | Postcode is not formed from alphanumerics or hyphens. |
| 406 | Invalid IssCode | IssCode does not match the credentials supplied. |
| 409 | Invalid PAN, PAN must be composed of digits | Indicates that the PAN is not a valid number composed of digits. |
| 410 | Invalid PublicToken, PublicToken must be composed of digits | Indicates that the PublicToken is not a valid number composed of digits. |
| 411 | Invalid NewPAN, NewPAN must be composed of digits | Indicates that the PAN is not a valid number composed of digits. |
| 412 | Invalid NewToken, NewToken must be composed of digits | Indicates that the NewToken is not a valid number composed of digits. |
| 413 | Invalid PrimaryToken, PrimaryToken must be composed of digits | Indicates that the PrimaryToken is not a valid number composed of digits. |
| 414 | Invalid MVCToken, MVCToken must be composed of digits | Indicates that the MVCToken is not a valid number composed of digits. |
| 415 | Invalid CardDesign, CardDesign must be composed of digits | Indicates that the CardDesign is not a valid number composed of digits. |
| 416 | Could not complete request, partial results returned | Indicates that not all requests within a bulk operation could be completed. |
| 418 | Both allow list and deny list are present in the request. Customer can only assign either allow list or deny list to a card | Indicates when both request parameters are supplied, only one is allowed. |
| 419 | Invalid RenewOptions | Indicates an invalid RenewOption was supplied. |
| 420 | NewProductID not present in the request | Indicates the request parameter was missing. |
| 421 | Invalid ExpiryDate format, it should be YYYY-MM-DD | Indicates the request parameter was in an invalid format. |
| 422 | Card request has been taken into account by the system. The production files are not yet generated. | Indicates a card renewal is already in progress. |
| 423 | This card request has been already processed and the production files are successfully generated. | Indicates a card renewal is already in progress. |
| 424 | This card has an expiry less than one month, which is less than minimum validity. Please select a RenewOptions other than 0,2 and 4. | Indicates an attempt to renew card thar is about to expire, without supplying a new expiry date. |
| 425 | Invalid AccumulatorType | Indicates the supplied parameter was an invalid value. |
| 426 | New available to spend balance on card is greater than new current balance on the card. The new available to spend balance should be less than new current balance. | Indicates the supplied parameter was an invalid value. |
| 427 | Balance stand-in not enabled in External Host Settings | Indicates the card is not valid for the operation. |
| 431 | Invalid PaymentTokenUsageGroup has been supplied, should be numeric. | Indicates the supplied parameter was an invalid value. |
| 432 | Incorrect PaymentTokenUsageGroup. (Returns when the group code is not present in Thredd database) | Indicates the supplied parameter was an invalid value |
| 433 | Invalid Delivery Method has been supplied, should be numeric. | Indicates the supplied parameter was an invalid value |
| 434 | Credential Value is missing, should be supplied when `Action` is add or update. | Returned in a 3D Secure request to add a credential to a card. See [3D Secure RDX Credentials (Cardinal).](../Web_services_api/3D_Secure_RDX_Credentials.htm) |
| 435 | Incorrect Virtual Card Image. | Returned when the Virtual Card Image ID is not present in Thredd database. |
| 436 | Incorrect Image Size. | Returned when the Size is not present in Thredd database. |
| 437 | No credentials found for the token. | Returned in response to a GET request for the 3D Secure credentials linked to a card if no credentials are found. See [3D Secure RDX Credentials (Cardinal).](../Web_services_api/3D_Secure_RDX_Credentials.htm) |
| 438 | Credential type already exists for this token. | Returned in response to an Add request if the credential type already exists for this card. |
| 439 | Value supplied is not valid | Returned in response to requests where an invalid value is provided. |
| 440 | Archived card, deny | If the request relates to an archived card record, the request is denied. (Applies to the following web services: `Create_Card`, `Create_Wallet`, `Regenerate, Regenerate_Wallet` and `ws_Renew`.) |
| 441 | Value not supplied for mandatory field | Returned in response to a service request where a mandatory field is empty. |
| 444 | Conversion to a physical card failed | Indicates that the create card request was successful, but the conversion to a physical card failed. The created card will be a virtual card. |
| 447 | Cannot change status to expired. Expiry should be a system driven change. | The card expiry status is driven by the expiry date set in the system and cannot be manually applied to the card using the status code of 54. See [Status Codes](Status_Codes.htm). |
| 450 | Token limit exceeded | Request is over the maximum number of card records (currently 1000 records) that can be cleared of cardholder data in a single web service call when using the [Remove Cardholder Data](../Web_services_api/Remove_Cardholder_Data.htm) (*Ws\_Remove\_CardHolder\_Data*) web service. |
| 500 | Function not allowed by Institution | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 501 | Invalid Status Code | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 502 | Token Not Found | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 503 | Account Closed | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 504 | Account status was not updated successfully | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 505 | Apply to Account was not updated successfully | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 506 | Bank Transaction does not exists. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 507 | Payment failed sanctions check. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 508 | Payment to an Institution defined as a deny-listed account. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 509 | BankingIn not allowed at Institution level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 510 | BankingOut not allowed at Institution level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 511 | DirectDebitIn not allowed at Institution level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 512 | DirectDebitOut not allowed at Institution level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 513 | BankingIn not switched on. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 514 | Account in ânot openâ status but account status is a priority. BankingIn switched off. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 515 | BankingOut not switched on. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 516 | Account in ânot openâ status but account status is a priority. BankingOut switched off. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 517 | DirectDebitIn not switched on. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 518 | Account in ânot openâ status but account status is a priority. DirectDebitIn switched off. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 519 | DirectDebitOut not switched on. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 520 | Account in ânot openâ status but account status is a priority. DirectDebitOut switched off. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 521 | Attempt to change account to disallowed status | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 522 | Amount to transfer must be a positive amount | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 523 | Sortcode cannot be empty | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 524 | Account number cannot be empty | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 525 | No available bank account numbers. Contact Thredd | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 526 | Error creating bank account with required features | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 527 | Banking not allowed for this product | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 528 | No account associated with this token | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 529 | Payment from an Institution defined deny-listed account. | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 530 | Inbound processing payment code not allowed by Institution | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 531 | Inbound payment has error code. Processing not allowed by Institution | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 532 | Reversal not present | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 533 | Generic DDA Agency error | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 534 | Unknown DDA account number | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 535 | Direct debit was not cancelled | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 536 | BankingIn not allowed at Issuer level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 537 | BankingOut not allowed at Issuer level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 538 | DirectDebitIn not allowed at Issuer level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 539 | DirectDebitOut not allowed at Issuer level | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 540 | Bottomline C series API not configured | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 541 | Combination of banking features not allowed | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 542 | DDA vales not configured | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 543 | Balance Sequence External Host is missing | Indicates the supplied parameter was an invalid value. |
| 544 | Invalid EHI Mode | Indicates the EHI mode of the Product is not valid for the operation. |
| 545 | Balance Sequence number is higner that the one inputted | Indicates the supplied parameter was an invalid value. |
| 546 | No direct debit found | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 547 | Issue connecting to Bottomline V Series | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 548 | Cannot close account with balance | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 549 | BACS payment cancelled by User | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 550 | BACS Error Code Q in file | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 551 | Peer to Peer transfer failed | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 552 | Peer to Peer reversal failed | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 553 | Peer to Peer not allowed between different PM | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 554 | Invalid character in reference field | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 555 | âBanking transaction already processed | BOTTOM LINE (AGENCY BANKING SOLUTION) |
| 556 | Expected spend cannot be 0 | Modulr (Agency Banking Service) |
| 557 | Must have at least 1 associate for the account | Modulr (Agency Banking Service) |
| 558 | Document must include a filename | Modulr (Agency Banking Service) |
| 559 | Document must have a filepath | Modulr (Agency Banking Service) |
| 560 | Document must have an uploaded date | Modulr (Agency Banking Service) |
| 561 | Associate must have an email | Modulr (Agency Banking Service) |
| 562 | Associate must have a first name | Modulr (Agency Banking Service) |
| 563 | Associate must have a last name | Modulr (Agency Banking Service) |
| 564 | Associate must have a phone number | Modulr (Agency Banking Service) |
| 565 | Associate phone number is not a recognised number | Modulr (Agency Banking Service) |
| 566 | Address line 1 is empty | Modulr (Agency Banking Service) |
| 567 | Address town is empty | Modulr (Agency Banking Service) |
| 568 | Address postcode is empty | Modulr (Agency Banking Service) |
| 569 | Address has invalid country code | Modulr (Agency Banking Service) |
| 570 | Product is not a Modulr product. Cannot create a customer | Modulr (Agency Banking Service) |
| 571 | Customer ID is not associated with this product | Modulr (Agency Banking Service) |
| 572 | Failed to save Modulr bank details | Modulr (Agency Banking Service) |
| 573 | Destination information provided with WEBHOOK call. Not needed | Modulr (Agency Banking Service) |
| 574 | No emails supplied when specifying EMAIL | Modulr (Agency Banking Service) |
| 575 | Customer ID is empty | Modulr (Agency Banking Service) |
| 576 | Passback Modurl Error | Modulr (Agency Banking Service) |
| 577 | Notfication already exists | Modulr (Agency Banking Service) |
| 581 | Modulr Payment unsuccessful | Modulr (Agency Banking Service) |
| 583 | IBAN is not valid | When the beneficiary IBAN is not provided in the request for a SEPA outbound payment (Modulr Agency Banking Service). |
| 584 | SEPAOut not allowed at Issuer level | When `SEPAOut` settings are not enabled at Issuer level (Modulr Agency Banking Service). |
| 585 | SEPAOut not allowed at Institution level | When `SEPAOut` settings not enabled at Institution level (Modulr Agency Banking Service). |
| 588 | Currency not supported | When any currency other than EUR is used for making SEPA Outbound payment. Only EUR currency is supported in SEPA (Modulr Agency Banking Service). |
| 589 | SEPAIn not allowed at Issuer level | When SEPAIn settings are not enabled at Issuer level (Modulr Agency Banking Service). |
| 590 | SEPAIn not allowed at Institution level | When SEPAIn settings are not enabled at Institution level (Modulr Agency Banking Service). |
| 591 | ComplianceData is not properly handled | The `ComplianceData` field is expected when `Type` is *PREQUALIFIED*(Modulr Agency Banking Service). See [Register a Customer for Banking](../Web_services_api/Register_Customer_for_Banking.htm). |
| 593 | Module not enabled for this product. Please contact Thredd support | When making a SEPA Outbound payment using a product which is not enabled for the Module Agency Banking Service). |
| 594 | KBA answer not provided | The 3D Secure *Add* or *Update* failed because the `Type` chosen is *KBA*, but `KBA_Answer` is not provided. |
| 595 | KBA question ID does not exist | The 3D Secure *Add* or *Update* failed because the `Type` chosen is *KBA*, but the KBA `Value` provided (question ID) does not exist. |
| 596 | Some conditions have not been met to remove cardholder data | The following conditions must be met before cardholder data can be deleted:  â¢ The number of years since the card was created must be greater than 6 years.  â¢ The actual or blocked amount on the card must be zero.  â¢ The card must be in the status of *Destroyed* or *Expired* card and the card must not be linked to an eWallet account. |
| 598 | Token does not have 3D Secure entries | Request to delete a 3D Secure credential for a card that does not have any credential entries in the 3D Secure tables. |
| 599 | Credential and token do not match | The 3D Secure Add/Update/Delete failed because the provided credentials do not belong to the provided public token.  For an Update request for a KBA credential, this error is returned if the `<KBA_AnswerOldValue>` provided does not match the existing KBA credential value. |
| 600 | Invalid AuthCalendarGroup | Indicates the supplied value could not be found. |
| 603 | Quantity exceed the max limit | Quantity exceed the max limit. |
| 604 | Invalid Event ID | Indicates supplied event ID is invalid. |
| 605 | MVC token is missing or invalid | Indicates MVC token is missing or invalid. |
| 606 | Product of MVC token and destination token are not from same | Indicates MVC token and destination token do not belong to same product. |
| 607 | Source token is not MVC | Indicates source token is not MVC. |
| 609 | Invalid FeeWaiver | Indicates FeeWaiver is invalid. |
| 610 | Partial fee is taken, remaining amount is stored for later | Partial fee is taken, remaining amount is stored for later. |
| 611 | No fee is taken, whole amount is stored for later | No fee is taken, whole amount is stored for later. |
| 613 | Invalid WSID specified in the request | Indicates supplied WSID is invalid. |
| 614 | Invalid Deny List | Indicates the supplied value could not be found. |
| 615 | Invalid Allow List | Indicates the supplied parameter value was not correct. |
| 621 | SFTP Is missing | SendCardFiles:SFTP Missing. |
| 622 | Invalid SMSBalance | Indicates the supplied parameter value was not correct. |
| 623 | Invalid load token, deny | Indicates the supplied parameter value was not correct. |
| 624 | Invalid Auth Type | Indicates the supplied parameter value was not correct. |
| 625 | Invalid ActMethod | Indicates the supplied parameter value was not correct. |
| 628 | Token already exist in the table | 3D Secure |
| 629 | Token is not configured to use the 3D secure web service | 3D Secure |
| 630 | Token details set for delete. | 3D Secure |
| 631 | LastModifiedType is missing | 3D Secure |
| 633 | Invalid CheckLevel | Sanction PEP |
| 646 | IssCode not configured for 3d secure | 3D Secure |
| 647 | Invalid MatchItems | Sanction PEP |
| 649 | Update is Applicable only after processing of Insert (File is not yet processed) | Indicates when an attempt is made to update 3D Secure details before the initial details have been sent to the 3D Secure processing bureau. |
| 650 | Public token and new token have different billing currencies. | Primary and secondary cards should have same billing currency. |
| 651 | Invalid Sms\_Required | Indicates the parameter value was invalid. |
| 652 | Invalid Sms\_Content | Indicates the parameter value was invalid. |
| 653 | CSN is empty or badly formatted | Gemalto : CSN â given in custom1 field â is null, empty or badly formatted. |
| 654 | Card status cannot be changed, current status of the card is not reversible | Indicates when card is in an irreversible status: 43 or 83. |
| 655 | CSN is already associated with a card request in progress (i.e. a card request that has not yet reached a definitive status) | Gemalto : CSN â given in custom1 field â is already associated with a card request in progress (i.e. a card request that has not yet reached a definitive status) |
| 656 | Invalid DataSrc | Invalid data source |
| 657 | Authentication code is null, empty or badly formatted | Gemalto : Authentication code â given in custom2 field â is null, empty or badly formatted. |
| 658 | ExtAPICardID is missed in the request | Indicates the parameter value was missing. |
| 659 | Invalid load source is used in the request. | Please use load source Primary card (68) to transfer fund from primary to secondary and vice versa. |
| 660 | Invalid passcode (AccCode), it should be 6 digit number. | Leading zero is acceptable. |
| 662 | LockMode is invalid or missing | Indicates the parameter value was missing or an invalid value. |
| 663 | Invalid DOB | Indicates the parameter value was missing or an invalid value. |
| 664 | Invalid Fee, it should be decimal/integer | Indicates the parameter value was an invalid value. |
| 665 | Invalid ProductID | Indicates the parameter value was missing or an invalid value. |
| 666 | ProductID not belongs to the client | Indicates the parameter value was an invalid value for the PAN/Token supplied. |
| 667 | Forbidden load source(LoadSrc), this program manager has no right to use the selected load source. | Indicates the parameter value was an invalid value. |
| 668 | RSA â Invalid NamePrefix | Up to 120 characters allowed |
| 669 | RSA â Invalid NameSuffix | Up to 120 characters allowed |
| 670 | RSA â Invalid MothersMaidenName | Up to 120 characters allowed |
| 671 | RSA â Invalid CustomerID | Up to 120 characters allowed |
| 672 | RSA â Invalid AddressLine1 | Up to 120 characters allowed |
| 673 | RSA â Invalid AddressLine2 | Up to 120 characters allowed |
| 674 | RSA â Invalid City | Up to 120 characters allowed |
| 675 | RSA â Invalid StateCode | Two digits |
| 676 | RSA â Invalid CountryCode | Two characters according to ISO 3166-1 alpha-2 standards. |
| 677 | RSA â Invalid CompanyName | Up to 120 characters allowed |
| 678 | RSA â Invalid Misc1 | Up to 120 characters allowed |
| 679 | RSA â Invalid Misc2 | Up to 120 characters allowed |
| 680 | RSA â Invalid Misc3 | Up to 120 characters allowed |
| 681 | RSA â Invalid Misc4 | Up to 120 characters allowed |
| 682 | RSA â Invalid Misc5 | Up to 120 characters allowed |
| 683 | RSA â Invalid Misc6 | Up to 120 characters allowed |
| 684 | RSA â Invalid Misc7 | Up to 120 characters allowed |
| 685 | RSA â Invalid Misc8 | Up to 120 characters allowed |
| 686 | RSA â Invalid Last4SSN | Four digit integer |
| 687 | RSA â Invalid PANExp | Four digit integer |
| 688 | RSA â Invalid FullSSN | Nine digits |
| 689 | RSA â Invalid Last6SSN | Six digits |
| 690 | RSA â Invalid HomePhone | Up to 50 digit integer |
| 691 | RSA â Invalid BusinessPhone | Up to 50 digit integer |
| 692 | RSA â Invalid AltPhone1 | Up to 50 digit integer. Also known as Mobile phone number. |
| 693 | RSA â Invalid AltPhone2 | Up to 50 digit integer |
| 694 | RSA â Invalid ZipCode | Five digits |
| 695 | RSA â Invalid DayOfBirth | Two digits |
| 697 | RSA â Invalid MonthOfBirth | Two digits |
| 698 | RSA â Invalid YearOfBirth | Two digits |
| 699 | RSA â Invalid CreditLimit | Nine digits |
| 700 | Invalid ISO language code | Indicates the parameter value was missing or an invalid value. |
| 701 | Invalid CreateType | Indicates the parameter value was missing or an invalid value. |
| 702 | Invalid Currency Buy Rate. | Must be non-negative |
| 703 | Invalid Currency Sell Rate. | Must be non-negative |
| 704 | Invalid Currency Mid Rate. | Must be non-negative |
| 705 | Invalid source currency code | Indicates the parameter value was missing or an invalid value. |
| 706 | Invalid destination currency code | Indicates the parameter value was missing or an invalid value. |
| 707 | Invalid FX Group ID | Indicates the parameter value was missing or an invalid value. |
| 708 | Invalid Card Design, its a MutliFX product | Indicates the parameter value was missing or an invalid value. |
| 710 | This Card Design does not support MultiFX | Indicates the parameter value was an invalid value. |
| 711 | This Card Design does not support External Authorisation | Indicates the parameter value was an invalid value for the operation. |
| 712 | Invalid Filter | Indicates the parameter value was missing or an invalid value. |
| 713 | Invalid Group Type | Indicates the parameter value was an invalid value. |
| 714 | Invalid load source | Indicates the parameter value was an invalid value. |
| 715 | invalid load fund type | Indicates the parameter value was an invalid value. |
| 716 | Invalid Linkage Group | Indicates the parameter value was an invalid value. |
| 717 | The specified PrimaryToken is not a primary card. | Secondary cards cannot be chosen as the Primary Card of another card. |
| 718 | Invalid PIN | PIN should be numeric and contain 4-12 digits. |
| 719 | Duplicate ExternalRef | Gemalto : requestUID value already exists for a card that is currently in production, or already produced. |
| 720 | Invalid TerminalID | Gemalto : satelliteUID value doesnât exists in Dexxis I2 (Central Base canât retrieve any Satellite with this ID). |
| 721 | Invalid ProductRef | Gemalto : cardTypeUID value doesnât exists in Dexxis I2 (Central Base canât retrieve any card type with this ID). |
| 722 | ExternalRef is empty | Gemalto : Null or empty string, or default value for parameter requestUID. |
| 723 | TerminalID is empty | Gemalto : Null or empty string for parameter satelliteUID. |
| 724 | ProductRef is empty | Gemalto : Null or empty string for parameter cardTypeUID. |
| 725 | CardName is empty | Gemalto : Null or empty string for parameter cardHolderName. |
| 726 | Some graphical data are empty | Gemalto : Null or empty array, or wrong size for parameter cardGraphicalData. |
| 727 | Some magnetic data are empty | Gemalto : Null or empty array, or wrong size for parameter cardMagneticalData. |
| 728 | Some carrier data are empty | Gemalto : Null or empty array or wrong size for parameter cardCarrierData. |
| 729 | Electric data is empty | Gemalto : Null or empty string for parameter cardElectricalData. |
| 730 | Illegal character in ExternalRef | Gemalto : requestUID contains characters that are not compatible with allowed charset/requestUID contains characters that are not alphanumerical. |
| 731 | Illegal character in TerminalID | Gemalto : satelliteUID contains characters that are not compatible with allowed charset/satelliteUID contains characters that are not alphanumerical. |
| 732 | Illegal character in ProductRef | Gemalto : cardTypeUID contains characters that are not compatible with allowed charset/cardTypeUID contains characters that are not alphanumerical. |
| 733 | Illegal character in graphical data | Gemalto : cardGraphicalData contains characters that are not compatible with allowed charset. |
| 734 | Illegal character in magnetic data | Gemalto : cardMagneticalData contains characters that are not compatible with allowed charset. |
| 735 | Illegal character in carrier data | Gemalto : cardCarrierData contains characters that are not compatible with allowed charset. |
| 736 | Grapical data type is empty or size is incorrect | Gemalto : Null or empty array, or wrong size for parameter cardGraphicalDataType. |
| 737 | Unknown graphical data type | Gemalto : cardGraphicalDataType contains at least one unknown graphical data type. |
| 738 | Size of graphical data and graphical data type arenât identical | Gemalto : cardGraphicalDataType doesnât contain the same number of values than cardGraphicalData. |
| 739 | Graphical data type doesnât specified | Gemalto : At least one cardGraphicalData doesnât have a cardGraphicalDataType specified. |
| 740 | Illegal character in electric data | Gemalto : cardElectricalData contains characters that are not compatible with allowed charset. |
| 741 | Custom data 1 is empty | Gemalto : Null or empty string, or default value for parameter cardRequestCustomData1. |
| 742 | Illegal character in custom data 1 | Gemalto : cardRequestCustomData1 contains characters that are not compatible with allowed charset. |
| 743 | Custom data 2 is empty | Gemalto : Null or empty string, or default value for parameter cardRequestCustomData1. |
| 744 | Illegal character in custom data 2 | Gemalto : cardRequestCustomData1 contains characters that are not compatible with allowed charset. |
| 745 | Custom data 3 is empty | Gemalto : Null or empty string, or default value for parameter cardRequestCustomData1. |
| 746 | Illegal character in custom data 3 | Gemalto : cardRequestCustomData1 contains characters that are not compatible with allowed charset. |
| 747 | Custom data 4 is empty | Gemalto : Null or empty string, or default value for parameter cardRequestCustomData1. |
| 748 | Illegal character in custom data 4 | Gemalto : cardRequestCustomData1 contains characters that are not compatible with allowed charset. |
| 749 | Custom data 5 is empty | Gemalto : Null or empty string, or default value for parameter cardRequestCustomData1. |
| 750 | Illegal character in custom data 5 | Gemalto : cardRequestCustomData1 contains characters that are not compatible with allowed charset. |
| 751 | Illegal character in custom map file | Gemalto : cardRequestCustomMapFile contains characters that are not compatible with allowed encoding. |
| 752 | Incorrect custom map file XML format | Gemalto : XML file(s) contained into cardRequestCustomMapFile archive doesnât have the required XML format. |
| 753 | Empty custom map file MD5 hash | Gemalto : Null or empty string for parameter cardProductionCustomMapFileMd5Hash. |
| 754 | Illegal character in custom map file MD5 hash | Gemalto : cardRequestCustomMapFileMd5Hash contains characters that are not compatible with allowed encoding. Hash result must be base64 encoded. |
| 755 | Comparison failed | Gemalto : cardRequestCustomMapFile archive transmission failure: MD5 hash comparison failed. |
| 756 | Unpack failed | Gemalto : cardRequestCustomMapFile archive canât be unpacked or files canât be retrieved from it. Probably an archive format error. |
| 757 | Map file data is not compactable with encoding | Gemalto : XML file(s) contained into cardRequestCustomMapFile archive contains at least one value that is not compatible with allowed encoding. |
| 758 | Invalid PIN Block | Gemalto : cipheredPin must contain 16 characters/cipheredPin parameter contains characters that are not compatible with allowed charset/cipheredPin parameter contains characters that are not allowed. cipheredPin must only be composed of digits or letters from A to F. |
| 759 | Invalid PIN Block format | Gemalto : cipheredPinFormat parameter is null or default values whereas it is mandatory since cipheredPin is set/cipheredPinFormat has not an attempted value (only âISO0â and âISO2â values are correct). |
| 760 | PIN block doesnot match PIN Block format | Gemalto : cipheredPin does not match given cipheredPinFormat. |
| 761 | PAN is empty | Gemalto : pan parameter is null or empty or default values whereas it is mandatory (given Ciphered PIN format is ISO0). |
| 762 | Invalid character in PAN | Gemalto : pan parameter contains characters that are not compatible with allowed charset/pan parameter contains characters that are not allowed. Pan must only be composed of digits. |
| 763 | Illegal character in PIN mailer data | Gemalto : At least one pinMailerData element contains characters that are not compatible with allowed charset. |
| 764 | Card request creation is forbidden | Gemalto : Card request creation is forbidden since standard Instant Issuance mode is deactivated on Central Base. |
| 765 | PIN cannot be verified | Gemalto : cipheredPin cannot been verified since KMS server is unreachable. |
| 766 | PIN delivery mode is empty | Gemalto : Null, empty or default string for parameter PinDeliveryMode whereas Pin or pinMailerData are provided. |
| 767 | Unknown PIN delivery mode | Gemalto : Unknown value for parameter PinDeliveryMode. Only NONE, PIN\_MAILER and PIN\_SELECTION are allowed. |
| 768 | Illegal character in PIN delivery mode | Gemalto : PinDeliveryMode parameter contains characters that are not compatible with allowed charset. |
| 769 | PIN Block is empty, chosen PIN delivery mode required PIN Block | Gemalto : cipheredPin parameter is null, empty or default value whereas it MUST contain a value because the chosen pinDeliveryMode requires it. |
| 770 | Data preparation failed | Gemalto : Data preparation failed (synchronous DP call) or data preparation launch failed (asynchronous DP call). |
| 771 | System is busy | Gemalto : The system is busy and canât accept any new request for the moment. Either too many concurrent requests have been sent, or too many requests are currently waiting for data preparation. The system refuses new requests to remain stable and to keep acceptable performances. Please try again later and check the system health. |
| 772 | Request not found | Gemalto : Card Request not fount in Gemalto system. |
| 774 | Limit Group not assigned to the input secondary card | Indicates the parameter value is not correctly configured. |
| 775 | Load source limit setting not found in the secondary card | Indicates the parameter value is not correctly configured. |
| 777 | Invalid func | Indicates the parameter value was invalid. |
| 778 | Invalid PIN Mailer | Indicates the parameter value was invalid. |
| 779 | Deny list is empty | Indicates the parameter value was empty and is required. |
| 780 | Allow List is empty | Indicates the parameter value was empty and is required. |
| 781 | CardAcceptorId is empty | Indicates the parameter value was empty and is required. |
| 782 | Invalid Action | Indicates the parameter value was invalid. |
| 783 | CardAcceptorID not found | Indicates the parameter value was not found. |
| 784 | The requested product is virtual but the request is for physical card generation | Indicates the CreateType parameter value was invalid for the specified Product. |
| 785 | The requested product is physical  but the request is for virtual  card generation | Indicates the CreateType parameter value was invalid for the specified Product. |
| 786 | Invalid e-mail address | Indicates the parameter value was in an invalid format. |
| 787 | e-mail address is missing | Indicates the parameter value was empty and is required. |
| 788 | Invalid MailOrSMS | Indicates the parameter value was invalid. |
| 789 | Cannot convert card, card is already physical | Indicates the card has already been converted. |
| 790 | The card is physical, only virtual can convert | Indicates the card is already physical. |
| 793 | Wrong or insufficient credentials | The credentials were not properly supplied. |
| 798 | Quantity entered is invalid, it should be numeric and greater than one | Indicates the parameter value was invalid format. |
| 799 | This card acceptor is already added to the deny list/allow list of the given scheme | Indicates the card acceptor is already added to the deny list/allow list of the given scheme. |
| 800 | WSID is missing in the request. | Parameter was not supplied but is required. |
| 801 | IssCode is missing. | Parameter was not supplied but is required. |
| 802 | TxnCode is missing | Parameter was not supplied but is required. |
| 803 | AuthType is missing | Parameter was not supplied but is required. |
| 804 | LocDate is missing | Parameter was not supplied but is required. |
| 805 | LocTime is missing | Parameter was not supplied but is required. |
| 806 | CurCode is missing in the request. | Parameter was not supplied but is required. |
| 807 | DebOrCred is missing in the request. | Parameter was not supplied but is required. |
| 808 | Description is missing in the request. | Parameter was not supplied but is required. |
| 810 | PAN, PublicToken or CardDesign is missing in the request. | Parameter was not supplied but is required. |
| 811 | DOB is missing in the request. | Parameter was not supplied but is required. |
| 812 | CVV is missing. | Parameter was not supplied but is required. |
| 813 | AccCode is missing or invalid. | Parameter was not supplied but is required. |
| 814 | ClientCode is missing when AuthType is 5 | Parameter was not supplied but is required. |
| 815 | LastName is missing when AuthType is 6 | Parameter was not supplied but is required. |
| 816 | Track2 is missing when AuthType is 7 | Track2 is mandatory when `ActMethod` is 4 or `AuthMethod` is 7 or when both `PAN` and  `PubToken` are not provided. |
| 819 | ActMethod is missing in the request. | Parameter was not supplied but is required. |
| 820 | City or Postcode is missing in the request. | Parameter was not supplied but is required. |
| 821 | Country is missing | Parameter was not supplied but is required. |
| 822 | FirstName is missing in the request. | Parameter was not supplied but is required. |
| 823 | AccNo is missing in the request. | Parameter was not supplied but is required. |
| 824 | ExpDate is missing in the request. | Parameter was not supplied but is required. |
| 825 | StatCode or NewStatCode is missing or invalid in the request. | Parameter was not supplied but is required. |
| 829 | SvcSrc is missing in the request. | Parameter was not supplied but is required. |
| 830 | SvcTye is missing in the request. | Parameter was not supplied but is required. |
| 831 | Work city or Work Postcode is missing in the request. | Parameter was not supplied but is required. |
| 832 | Work country is missing | Parameter was not supplied but is required. |
| 833 | Dlvcity or DlvPostcode is missing in the request. | Parameter was not supplied but is required. |
| 834 | DlvCountry is missing. | Parameter was not supplied but is required. |
| 835 | DlvFirstName is missing in the request. | Parameter was not supplied but is required. |
| 846 | ItemId is missing. | Parameter was not supplied but is required |
| 850 | Func is missing. | Parameter was not supplied but is required |
| 851 | Current Pin is missing | Parameter was not supplied but is required |
| 852 | New Pin is missing | Parameter was not supplied but is required |
| 853 | Confirm Pin is missing | Parameter was not supplied but is required |
| 854 | Key ref is missing. | Parameter was not supplied but is required |
| 857 | LoadSrc is missing. | Parameter was not supplied but is required |
| 864 | Invalid Limit group code. | Parameter was supplied but is invalid |
| 865 | Invalid MCC group code. | Parameter was supplied but is invalid |
| 866 | Invalid Usage group code. | Parameter was supplied but is invalid |
| 867 | ProcCode is missing in the request or invalid. | Parameter was either supplied but is invalid, or is missing and required |
| 868 | Duplicate WSID in the request, deny. | The WSID has already been used on a previous request. WSIDs should be unique. |
| 869 | Invalid Fee Group Code | Parameter was supplied but is invalid |
| 870 | Invalid Primary Token, deny | Parameter was supplied but is invalid |
| 871 | Balance transfer from primary card to seconday or vice vers, deny | Not in use |
| 872 | Source and destination card has same PAN, deny | Attempt to balance transfer to and from same card is invalid |
| 873 | CardSelector is missing or invalid. | Parameter was not supplied but is required, or is an invalid value |
| 874 | CardSelectorValue is missing or invalid. | Parameter was not supplied but is required, or is an invalid value |
| 875 | Fee structure is not set for the given process code. | No fee structure is configured for the process code supplied during an attempt to take generic fees |
| 876 | RegenType/Replace is empty or invalid. | Parameter was not supplied but is required, or is an invalid value |
| 877 | Invalid expiry date. | An attempt was made to update the logical expiry date to either a past date, or a date that is beyond the physical expiry date |
| 878 | Invalid character in Card Name. | Non - european characters are not allowed in Card Name |
| 879 | Invalid character in First Name. | If Card Name is empty then non â european characters are not allowed in First Name. |
| 880 | Invalid character in Last Name. | If Card Name is empty then non â european characters are not allowed in Last Name. |
| 881 | Invalid recurring/scheduled fee group code. | Parameter was supplied but is invalid |
| 882 | Invalid web service fee group code. | Parameter was supplied but is invalid |
| 883 | Invalid Card Manufacturer Code | Parameter was supplied but is invalid |
| 884 | Customer mobile phone number is not set for this card. | An attempt was made to send an SMS, but no mobile number is registered for this card |
| 893 | Invalid DebOrCred, | It should be 1(Credit) or -1(Debit). |
| 894 | Invalid DOB format | Format should be YYYY-MM-DD |
| 895 | Invalid Start Date | Format should be YYYY-MM-DD |
| 896 | Invalid EndDate | Format should be YYYY-MM-DD |
| 897 | Invalid amount | Amount should be non-negative and no more decimal places than the currency will allow. |
| 898 | Invalid BIN/Manufacturer combination | The selected card manufacturer is not associated with the programme scheme |
| 899 | Invalid Country/Delv\_Country, it should be ISO numeric code. | Parameter was supplied in incorrect format |
| 900 | Restricted web method, this client is not allowed to use this method | Client is not configured to call this web service |
| 902 | Invalid Transaction | The selected transaction is not valid for this operation |
| 904 | Format error, deny | Generic format error condition eg used by Account Enquiry to indicate invalid format in âtxnfilterâ value received in request or when the security details do not match with the selected authMethod |
| 908 | Transaction destination cannot be found for routing | As required by Issuer |
| 909 | System malfunction, deny | Generic âcatch-allâ error condition |
| 911 | Card issuer timed out | As required by Issuer |
| 913 | Duplicate transaction, deny | To indicate the received request is a duplicate of a previous request.  In some calls the ID of the original request (that this request duplicates) may also be returned in the response. |
| 914 | Unable to trace original transaction, deny | Indicates that the item a Void transaction seeks to cancel cannot be found |
| 915 | Reconcilliation cutover or checkpoint error | As required by Issuer |
| 920 | Security error â authentication failed, deny | Failed to authenticate the cardholder |
| 932 | Recurring data error | As required by Issuer |
| 933 | 3DS Update not allowed | Cardholder update completed successfully, but the 3D Secure update was not performed as the cardholder is not configured for 3D Secure. |
| 951 | Web service call successful, but failed to send Network Message due to internal error (i.e. 0302 service call did not return) | As required by Issuer |
| 952 | Web service call successful, but failed Fraud API update | As required by Issuer |
| 953 | Activation of Card successful, but updating MDES Card Mapping failed | As required by Issuer |
| 954 | Web service call successful, but 3DS Credential Update failed. | Cardholder update completed successfully, but the 3D Secure update was not performed as certain conditions were not met. |
| 996 | Retired Web Service | Retired |
| 997 | Soap username is null or empty | SOAP authentication |
| 998 | Soap password is null or empty | SOAP authentication |
| 999 | Security error â SOAP authentication failed. Deny | Indicates the SOAP authentication user name or password is incorrect. |

## MVC Action Codes

The following action codes are relevant to a Master Virtual Card (MVC) .

| Code | Description |
| --- | --- |
| 000 | Normal, approve. |
| 100 | Do not Honour, deny. |
| 116 | Insufficient funds, deny. |
| 118 | No card record, deny. |
| 121 | Amount limits exceeded or outside valid load range, deny. |
| 123 | Frequency limits exceeded, deny. |
| 605 | MVC token is missing or invalid. |
| 606 | Source (MVC) and destination (new) tokens aren't belonging to same scheme. |
| 607 | Source token is not MVC. |
| 661 | MVC token and new token have different billing currencies. MVC load doesnât support inter currency fund transfer. |
| 801 | IssCode is missing. |
| 806 | CurCode is missing in the request. |
| 810 | PublicToken is missing in the request. |
| 897 | Invalid amount, amount should be non-negative. |
| 909 | System malfunction, deny. |
| 997 | Soap username is null or empty. |
| 998 | Soap password is null or empty. |
| 999 | Security error. SOAP authentication failed. Deny. |