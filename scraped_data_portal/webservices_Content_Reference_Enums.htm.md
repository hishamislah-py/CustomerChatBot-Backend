# Enums and Data Structures

This section provides details of parameters with Enumerated (Enum) values and data structures.

### BankingFeaturesType

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| BankingIn | Enum | ENUM\_BankingIn | See [ENUM\_BankingInEnabled](#ENUM_BankingInEnabled) |
| BankingOut | Enum | ENUM\_BankingOut | See [ENUM\_BankingOutEnabled](#ENUM_BankingOutEnabled) |
| DirectDebitIn | Enum | DirectDebitIn | See [ENUM\_DirectDebitInEnabled](#ENUM_DirectDebitInEnable) |
| DirectDebitOut | Enum | DirectDebitOut | See [ENUM\_DirectDebitOutEnabled](#ENUM_DirectDebitOutEnabled) |
| SEPAIn | Boolean | SEPAInEnabled | Allow payments in. Set to *TRUE* or *FALSE*. |
| SEPAOut | Boolean | SEPAOutEnabled | Allow payments out. Set to *TRUE* or *FALSE*. |
| AccountName | String | AccountName | Account name. |

### Changed Banking Features

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| PublicToken | Integer | PublicToken | Public token |
| BankingFeatures | Data structure | BankingFeaturesReturnType | See BankingFeaturesReturnType |
|  | Enum | UpdateSuccess | See [ENUM\_ChangedBankingFeaturesUpdate](#ENUM_ChangedBankingFeaturesUpdat) |
| BankingFeaturesReturnType | Enum | BankingIn | See [ENUM\_BankingInEnabled](#ENUM_BankingInEnabled) |
|  | Enum | BankingOut | See [ENUM\_BankingOutEnabled](#ENUM_BankingOutEnabled) |
|  | Enum | DirectDebitIn | See [ENUM\_DirectDebitInEnabled](#ENUM_DirectDebitInEnable) |
|  | Enum | DirectDebitOut | See [ENUM\_DirectDebitOutEnabled](#ENUM_DirectDebitOutEnabled) |
|  | Enum | CardEnabled | See [ENUM\_CardEnabled](#CardEnab). |

### BankingEnabled Enums

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_BankingInEnabled | Enum | Enabled  Disabled | Enabled  Disabled |
| ENUM\_BankingOutEnabled | Enum | Enabled  Disabled | Enabled  Disabled |
| ENUM\_DirectDebitInEnabled | Enum | Enabled  Disabled | Enabled  Disabled |
| ENUM\_DirectDebitOutEnabled | Enum | Enabled  Disabled | Enabled  Disabled |
| ENUM\_ChangedBankingFeaturesUpdate | Enum | Success  Fail  DirectDebitNotAllowed | Successful  Failed  Direct Debit not allowed |

### Enum\_CardEnabled

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_CardEnabled | Enum | Enabled  Disabled | Enabled  Disabled |

### AccountStatus

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| AccountStatus | Enum | AccountStatus | See [ENUM\_AccountStatus](#ENUM_Acc). |
|  | Enum | BankingInEnabled | See [ENUM\_BankingInEnabled](#ENUM_BankingInEnabled). |
|  | Enum | BankingOutEnabled | See [ENUM\_BankingOutEnabled](#ENUM_BankingOutEnabled). |
|  | Enum | DirectDebitInEnabled | See [ENUM\_DirectDebitInEnabled](#ENUM_DirectDebitInEnable). |
|  | Enum | DirectDebitOutEnabled | See [ENUM\_DirectDebitOutEnabled](#ENUM_DirectDebitOutEnabled) |
|  | Enum | CardEnabled | See [ENUM\_CardEnabled](#CardEnab). |

### ENUM\_AccountStatus

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_AccountStatus | Enum | Open  Closed  SuspendedPaymentsInAllowed  FullySuspended  Deceased  Probate | The account is open.  The account is closed.  The account is suspended, but payments in are allowed.  The account is fully suspended.  The account holder is deceased  The account is in probate (for a deceased account holder) |

### BLAccount

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| BLAccount | Integer (long) | PublicToken | Encrypted public token |
|  | String | SortCode | String of the 6-digit sort code |
|  | String | AccountNumber | String of account number |
|  | Enum | Status | Account status. See [ENUM\_AccountStatus](#ENUM_Acc). |
|  | Number | Balance | Account balance (decimal) |
|  | String | UpdateStatusResult | String of status result |

### BankingFeatures

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ExistingToken | String | ExistingToken | Public token. |
| BankingIn | Boolean | BankingInEnabled | Allow payments in. Set to "TRUE" or "FALSE". |
| BankingOut | Boolean | BankingOutEnabled | Allow payments out. Set to "TRUE" or "FALSE". |
| DirectDebitIn | Boolean | DirectDebitInEnabled | Allow direct debit payments in. Set to "TRUE" or "FALSE". |
| DirectDebitOut | Boolean | DirectDebitOutEnabled | Allow direct debit payments out. Set to "TRUE" or "FALSE". |
| CardEnabled | Boolean | CardEnabled | Indicates whether the card is enabled. Set to "TRUE" or "FALSE". |
| Status | String | Status | Account status code. |
| CompanyName | String | CompanyName | Company name. |
| AccountName | String | AccountName | Account name. |

#### Notes

* Populating the `ExistingToken` field will add banking features onto an existing card.
* Boolean options, if not populated, will default to true.
* The status codes and their associated options are shown below (0 = false, 1 = true).

| Status Code | Description | AllowPaymentsIn | AllowPaymentsOut | AllowDirectDebitIn | AllowDirectDebitOut | Priority | BlockCard | CardStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C | Closed | 0 | 0 | 0 | 0 | 1 | 1 | 5 |
| D | Customer deceased | 1 | 0 | 0 | 0 | 1 | 1 | 5 |
| F | Full suspended | 0 | 0 | 0 | 0 | 1 | 1 | 5 |
| O | Open | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| P | Probate | 1 | 1 | 0 | 0 | 1 | 1 | 5 |
| S | Suspended payments in allowed | 1 | 0 | 0 | 0 | 1 | 1 | 5 |

\* Priority - takes precedent over any other account settings.   
\*\* When creating a card, the status is automatically set to status "O" (open).  
\*\*\* For CardStatus, see [Card Status](Status_Codes.htm).

### BankingError

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| BankingError | String | field | Error message field. |
|  | String | code | Error message code. |
|  | String | message | Error message. |
|  | String | error | Error. |

### Beneficiary

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| Beneficiary | String | AccountNumber | Account number |
|  | String | SortCode | Sort code |
|  | String | AccountName | Account name |
|  | String | IBAN | IBAN |

### SEPABeneficiaryAddress

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| SEPABeneficiaryAddress | String | AddressLine1 | First line of the address |
|  | String | AddressLine2 | Second line of the address |
|  | String | PostTown | Address town or city |
|  | String | PostCode | Address postcode |
|  | String | Country | Address country |

### ENUM\_PaymentMethod

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_PaymentMethod | Enum | FasterPaymentIn  FasterPaymentOut  BACSIn  BACSOut  DirectDebitIn  FasterPaymentReturn  PeerToPeerIn  PeerToPeerOut  SEPAOut | Faster Payment into the account  Faster Payment out of the account  BACS payment into the account  BACS payment out of the account  Direct Debit payment into the account  Faster Payment returned  Peer-To-Peer payment into the account  Peer-To- Peer payment out of the account  SEPA payment out of the account |

### ENUM\_PaymentDirection

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_PaymentDirection | Enum | Outbound  Inbound | Payment out of the account.  Payment into the account. |

### ENUM\_TransferFundsResult

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_TransferFundsResult | Enum | Success  Failure | Transfer of funds was successful.  Transfer of funds failed. |

### ENUM\_DirectDebitCancellationReason

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_DirectDebitCancellationReason | Enum | AccountClosed  CancelledByDebtor  DebtorDeceased ReferToDebtor | Account closed.  Cancelled by debtor.  The debtor is deceased. |

### ENUM\_DirectDebitCancelStatus

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_DirectDebitCancelStatus | Enum | Success  Failure | Cancel of direct debit was successful.  Cancel of direct debit failed. |

### ENUM\_DirectDebitStatus

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_DirectDebitStatus | Enum | 0  1  2  3  4  5 | Active  Suspended  Cancelled  Pending  Dormant  Expired |

### BLDirectDebit

| Type | Value | Description |
| --- | --- | --- |
| DateTime | Created | Date and time created |
| Enum | CreationMethod | Creation method. See [Enum\_CreationMethod](#ENUM_Cre) |
| String | CreditorAccountName | Creditor account name |
| String | CreditorBIC | Creditor BIC |
| String | CreditorIBAN | Creditor IBAN |
| String | CreditorReference | Creditor reference |
| String | DebtorAccountID | Debtor account ID |
| String | DerivedReference | Derived reference |
| String | IBAN | IBAN |
| Guid | ID | ID |
| Boolean | IgnoreTransactionCode | Whether to ignore the transaction code |
| Boolean | IsInstructionHeldAtBank | Whether the instruction is held at a bank |
| Boolean | IsPaperless | Whether the instruction is paperless |
| Boolean | IsThroughNotificationService | Whether the instruction is through a notification service |
| DateTime | LatChanged | Date last changed |
| String | Reference | Reference |
| String | ServiceUserNumber | ServiceUserNumber |
| Enum | Status | Direct debit status. See [ENUM\_DirectDebitStatus](#ENUM_Dir2) |
| Boolean | SuppressFirstDirectDebit | Whether to suppress the first direct debit |

### ENUM\_ChangeAccountStatus

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_ChangeAccountStatus | Enum | Success  Failure  AccountDoesNotExist  AccountInvalidStatus | Account status change successful  Account status change failed  Account does not exist  Invalid account status |

### ENUM\_CreationMethod

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_CreationMethod | Enum | Unknown  Manual  Imported | Unknown creation method  Manually entered into system  Imported into system |

### ENUM\_PendingDirectDebit

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_PendingDirectDebit | Enum | LikelySuccess  LikelyFailure | Pending Direct Debit likely to succeed.  Pending Direct Debit likely to fail. |

## 3D Secure Data Structures

### Detail

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| Detail | String | ENUM\_3DS\_Details | See [ENUM\_3DS\_Details](#ENUM_3DS). |

### ENUM\_3DS\_Details

| Value | Description |
| --- | --- |
| EmbossedName | Up to 120 characters allowed |
| Last4SSN | Four digit integer. |
| DateOfBirth | Must be in the format YYYYMMDD. |
| PANExp | Four digit integer. |
| FirstName | Up to 120 characters allowed. |
| MiddleName | Up to 120 characters allowed. |
| LastName | Up to 120 characters allowed. |
| NamePrefix | Up to 120 characters allowed. |
| NameSuffix | Up to 120 characters allowed. |
| FullSSN | Nine digit integer. |
| Last6SSN | Six digit integer. |
| MothersMaidenName | Up to 120 characters allowed. |
| HomePhone | Up to 50 digit integer. |
| BusinessPhone | Up to 50 digit integer. |
| AltPhone1 | Up to 50 digit integer. |
| AltPhone2 | Up to 50 digit integer. |
| RelationshipType | Must be one of the following primary, co-applicant, authorized) |
| CustomerID | Up to 120 characters allowed. |
| AddressLine1 | Up to 120 characters allowed. |
| AddressLine2 | Up to 120 characters allowed. |
| City | Up to 120 characters allowed. |
| StateCode | Two digits |
| ZipCode | Five digits |
| CountryCode | Two characters according to ISO 3166-1 alpha-2 standards. |
| DayOfBirth | Two digits |
| MonthOfBirth | Two digits |
| YearOfBirth | Two digits |
| CreditLimit | Nine digits |
| LastStatementDate | Must be format YYYYMMDD. |
| CompanyName | Up to 120 characters allowed |
| CompanyTel | Up to 50 digit integer |
| BranchNumber | Ten digits |
| AccountNumber | Ten digits |
| Misc1 | Up to 120 characters allowed. |
| Misc2 | Up to 120 characters allowed. |
| Misc3 | Up to 120 characters allowed. |
| Misc4 | Up to 120 characters allowed. |
| Misc5 | Up to 120 characters allowed. |
| Misc6 | Up to 120 characters allowed. |
| Misc7 | Up to 120 characters allowed. |
| Misc8 | Up to 120 characters allowed. |

### ENUM\_3DS\_Action

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| ENUM\_3DS\_Action | String | Add  Update  Delete | Add 3DS record.  Update 3DS record.  Delete 3DS record. |

### Ws\_3DS\_ReIssue

| Property | Type | Value | Description |
| --- | --- | --- | --- |
| Ws\_3DS\_ReIssue | Boolean | ReIssue | Re-issue 3DS token. |
|  | Integer | NewToken | New token value. |

## Agency Banking Data Structures

### Associate

| Property | Type | Description |
| --- | --- | --- |
| applicant | Boolean | Whether the associate is an applicant. |
| dateOfBirth | DateTime | Date of birth. |
| documentInfo | String | Document information |
| firstName | String | First name |
| lastName | String | Last name |
| middleName | String | Middle name |
| ownership | Int | Ownership |
| phone | String | Phone |
| homeAddress | Object | See [homeAddress](#homeAddr) |

### DocumentInfo

| Property | Type | Description |
| --- | --- | --- |
| filename | String | Filename of the file sent to the SFTP server. |
| filepath | String | Filepath to where the file is stored on the SFTP server. |
| uploadDate | DateTime | Date uploaded to the SFTP server. |

### homeAddress

| Property | Type | Description |
| --- | --- | --- |
| addressLine1 | String | Address line 1 |
| addressLine2 | String | Address line 2 |
| posttown | String | Town |
| postCode | String | Postcode |
| country | String | Country |

### RegisteredAddress

| Property | Type | Description |
| --- | --- | --- |
| addressLine1 | String | Address line 1 |
| addressLine2 | String | Address line 2 |
| posttown | String | Town |
| postCode | String | Postcode |
| country | String | Country |

### TradingAddress

| Property | Type | Description |
| --- | --- | --- |
| addressLine1 | String | Address line 1 |
| addressLine2 | String | Address line 2 |
| posttown | String | Town |
| postCode | String | Postcode |
| country | String | Country |

### BankingFeaturesReturnType

| Property | Type | Description |
| --- | --- | --- |
| BankingIn | Enum | See [ENUM\_BankingInEnabled](#ENUM_BankingInEnabled) |
| BankingOut | Enum | See [ENUM\_BankingOutEnabled](#ENUM_BankingOutEnabled) |
| DirectDebitIn | Enum | See [ENUM\_DirectDebitInEnabled](#ENUM_DirectDebitInEnable) |
| DirectDebitOut | Enum | See [ENUM\_DirectDebitOutEnabled](#ENUM_DirectDebitOutEnabled) |
| CardEnabled | Enum | See [ENUM\_CardEnabled](#CardEnab) |
| AccountName | String | The account name. |

### DD\_MANDATES

| Type | Value | Description |
| --- | --- | --- |
| MandateId | AN | The mandateId related to the direct debit mandate. |
| MerchantName | AN | MerchantName from the latest DD\_INCOMING\_DEBIT with the same MandateID. |
| LastScheduledAmount | N | Amount of last PAYOUT with same Mandate ID. |
| MandateStatus | AN | The NewStatus of the mandate. |
| MandateCreatedDate | Date | Date that the mandate ID was originally added to the database. |