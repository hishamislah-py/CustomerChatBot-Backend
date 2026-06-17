# 4.34 SenderData and ReceiverData Fields

The `SenderData` and `ReceiverData` fields provide details of the sender and receiver in a money transfer message. Both fields are represented as a TLV with following order and lengths:

* Tag - two characters
* Length - two decimal digits
* Value - the number of characters as given by the length

The table below describes the subfields (tags).

| Tag | Field Name | Description |
| --- | --- | --- |
| 1 | FirstName | First name |
| 2 | MiddleName | Middle name |
| 3 | LastName | Last name |
| 4 | StreetAddress | Street address |
| 5 | City | City |
| 6 | Province | Province |
| 7 | Country | Three letter ISO country code (e.g., CYP = Cypress) |
| 8 | PostCode | Postcode |
| 9 | PhoneNumber | Phone number |
| 10 | DateOfBirth | Date of birth (MMDDYYYY). For example 12311996. |
| 11 | AccountNumber | Account number |
| 12 | IdType | Type of Identity Document (ID). (00 = passport; 01 = National Identification Card; 02 = Driverâs License; 03 = Government Issued; 04 = Other; 05-10 reserved for future use) |
| 13 | IdNbr | ID number |
| 14 | IdCtryCode | ID three-letter country code (e.g., MLT = Malta) |
| 15 | IdExpDate | ID expiry date (MMDDYYYY) |
| 16 | Nationality | Nationality (three character alpha ISO code) |
| 17 | BirthCtry | Country of birth (three character alpha ISO code) |
| 18 | AcctNbrType | Type of account number. See [Account Number Type](Misc_TLV_Data_field.htm#Account). |
| 19 | ReceiverOrganizationName | If a Mastercard Send transaction recipient is an organisation, this field is used to submit the company name.  Mastercard Send applies to all funding transactions including MoneySend Payment Transactions and Mastercard Gaming or Gambling Payment Transactions. |
| 20 | SenderOrganizationName | If a Mastercard Send transaction is initiated by an organisation, this field is used to submit the company name.  Mastercard Send applies to all funding transactions including MoneySend Payment Transactions and Mastercard Gaming or Gambling Payment Transactions. |
| V1 | FundsSource | Source of funds. See [Source of Funds](Misc_TLV_Data_field.htm#Source). |
| V2 | ClaimCode | Claim code |

##### Example

*0106Mickey0305Mouse0411Main Street0508Annaheim0703USA*