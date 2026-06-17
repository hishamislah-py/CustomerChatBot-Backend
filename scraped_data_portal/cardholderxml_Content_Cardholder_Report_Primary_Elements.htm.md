# 3 Primary Elements

Below are details of the primary elements included in the cardholder XML file.

| Element Name | Description | Data Type | Occurs |
| --- | --- | --- | --- |
| [Header](#_Header) | Describes processor name, file transmit date | `<Header>` | 1 |
| [CardHolderDetails](#_CardHolderDetails) | Provides cardholder details | `<CardHolderDetails>` | 0 â n |
| [Trailer](#_TRAILER) | Describes a count of the card holders | `<Trailer>` | 1 |

## 3.1 Example

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<CardHolder xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">    
  <Header>â¦detail ommittedâ¦</Header>  
  <CardHolderDetails>â¦detail ommittedâ¦</CardHolderDetails>  
  <Trailer>â¦detail ommittedâ¦</Trailer>  
</CardHolder>
```

## 3.2 Header

The Header element provides high-level details about the report:

| Child Element | Description | Attribute | Required | Constraints / Permitted  Values |
| --- | --- | --- | --- | --- |
| ProcessorName | Static data | `<ProcessorName>` | Yes | GPS |
| ReportName | Static data | `<ReportName>` | Yes | CUSTMASTER |
| FileTransmitDate | Date transmitted by Processor | `<FileTransmitDate>` | Yes | Current Date |
| WorkOfDate | Date information is referencing | `<WorkOfDate>` | Yes | Current Date |

#### Example

[Copy](javascript:void(0);)

```
<Header>  
  <ProcessorName>GPS</ProcessorName>  
  <ReportName>CUSTMASTER</ReportName>  
  <FileTransmitDate>20210322</FileTransmitDate>  
  <WorkOfDate>20210322</WorkOfDate>  
</Header>
```

## 3.3 CardHolderDetails

The CardHolderDetails element provides details of the cardholder and their linked cards.

| Child Element | Description | Attributes | Required | Maximum Length |
| --- | --- | --- | --- | --- |
| ProgramId | Unique identifier of card programme. | `<ProgramId>` | Yes | 50 |
| CardNumber | Number on the plastic issued to the cardholder. | `<CardNumber>` | Yes | bigint |
| MaskedPAN | Masked Primary Account Number (PAN) where six of the digits are replaced with the \* character. | `<MaskedPAN>` | Mandatory | 16 |
| CardIssuedDate | Date card was issued. | `<CardIssuedDate>` | Yes | 8 (smalldatetime) |
| AccountNumber | Number assigned to the customer. | `<AccountNumber>` | Yes | 28 |
| AccountExpiryDate | The expiry date you specified on activation of the card or on card activation and load. If no expiry date is specified, this date is based on the Thredd validity period in days configured at product level (e.g., 1095 days from the date of card activation). | `<AccountExpiryDate>` | Yes | 8 (smalldatetime) |
| CardId | Card ID. | `<CardId>` | Yes |  |
| CustomerCode | Customer code of the cardholder. | `<CustomerCode>` | Yes | 25 |
| BranchCode | The branch code or agent code associated with the card. | `<BranchCode >` | Yes | 8 |
| FirstName | Primary cardholder's first name. | `<FirstName >` | yes | 100 |
| LastName | Primary cardholder's last name. | `<LastName >` | yes | 100 |
| Address1 | Cardholder's residential address first line. | `<Address1>` | Yes | 100 |
| Address2 | Cardholder's residential address second line. | `<Address2>` | Yes | 100 |
| City | City of residence. | `<City>` | Yes | 50 |
| State | State of residence. | `<State>` | Yes | 20 |
| Zipcode | Residential postcode. | `<Zipcode >` | Yes | 10 |
| Country | Country of residence. | `<Country>` | Yes | 3 |
| DelvAddress1 | Cardholder's delivery address first line. | `<DelvAddress1>` | Yes | 100 |
| DelvAddress2 | Cardholder's delivery address second line. | `<DelvAddress2>` | Yes | 100 |
| DelvCity | Delivery city. | `<DelvCity>` | Yes | 50 |
| DelvState | Delivery state. | `<DelvState>` | Yes |  |
| DelvZipcode | Delivery postcode. | `<DelvZipcode>` | Yes | 10 |
| DelvCountry | Delivery country. | `<DelvCountry>` | Yes | 10 |
| Phone1 | Cardholder's primary phone number. | `<Phone1>` | Yes | 20 |
| Phone2 | Cardholder's secondary phone number. | `<Phone2>` | Yes | 20 |
| IDType1 | Type of ID (e.g., Passport, driving license, EU/EEA licence). | `<IDType1>` | Yes | LEFT BLANK |
| IDNumber1 | Number on ID. | `<IDNumber1>` | Yes | LEFT BLANK |
| CountryOfIssuance1 | Country the ID was issued by. | `<CountryOfIssuance1>` | Yes | LEFT BLANK |
| IDType2 | Type of ID (e.g., Passport, driving license, EU/EEA licence). | `<IDType2>` | Yes | LEFT BLANK |
| IDNumber2 | Number on ID. | `<IDNumber2>` | Yes | LEFT BLANK |
| CountryOfIssuance2 | Country the ID was issued by. | `<IDNumber2>` | Yes | LEFT BLANK |
| CardStatus | Status of card. | `<CardStatus >` | Yes | 2 |
| CardStatusDate | Indicates last status change date of card. | `<CardStatusDate>` | Yes | 8(smalldatetime) |
| ActualBalance | Settled balance, not available balance. | `<ActualBalance>` | Yes | 13(Decimal) |
| ActualBalanceSign | Sign if settled balance Positive or Negative. | `<ActualBalanceSign>` | Yes | 1 |
| AccountCreatedDate | Date account number created. | `<AccountCreatedDate>` | Yes | 8(smalldatetime) |
| CardActivationDate | Card activation date. | `<CardActivationDate>` | Yes | 8(smalldatetime) |
| NegBalDate | Date current balance exceeded available balance | `<NegBalDate>` | Yes | 8(smalldatetime) |
| NegBalPrincipleAmt | Negative balance amount due to transactions. | `<NegBalPrincipleAmt>` | Yes | 13 |
| NegBalFeeAmt | Negative balance amount due to fees. | `<NegBalFeeAmt>` | Yes | 13 |
| TypeOfCard | For Visa only, indicates the type of card (e.g., Payroll, Gift card, Corporate card or other). | `<TypeOfCard>` | Yes | LEFT BLANK |
| AuthenticationType | The cardâs authentication type:  SIG = Signature based  PIN = PIN based. | `<AuthenticationType>` | Yes | 3 |
| EnrollmentNumber | Unique to a specific program. N/A to all others. | `<EnrollmentNumber>` | Yes |  |
| AccountStatus | Status of account. | `<AccountStatus>` | Yes | 2 |
| AccountStatusDate | Indicates last status change date of account. | `<AccountStatusDate>` | Yes | 8 (smalldatetime) |
| DateOfBirth | Date of birth of Cardholder. | `<DateOfBirth>` | Yes | 8 (smalldatetime) |
| AvailableBalance | Available balance. | `<AvailableBalance>` | Yes | 13 (Decimal) |
| AvailableBalanceSign | Sign of available Balance: + or - | `<AvailableBalanceSign>` | Yes | 2 |
| [PrimaryCardClosed The primary card is the main card which your customer uses to load funds into their account. The primary card can be linked to one or more secondary cards, which are loaded with funds from the primary card. Typically funds are transferred from the primary card to the secondary card.](#) | If this is the Primary card, lists the first letter of card type; if not Primary (i.e., S=Secondary, I=Independent and provide comparison in the lookup file). | `<PrimaryCard>` | Yes | 2 |
| CardExpiryDate | Expiration date as at card creation and printed on the card. | `<CardExpiryDate>` | Yes | 8 (smalldatetime) |
| FirstLoadDate | Date the customer first loaded the card. | `<FirstLoadDate>` | Yes | 8 (smalldatetime) |
| LastTransactionDate | Date of the last transaction. | `<LastTransactionDate>` | Yes | 8 (smalldatetime) |
| LastReissuedDate | Date the card was reissued. | `<LastReissuedDate>` | Yes | 8 (smalldatetime) |
| NumberOfCards | Number of plastics with the same card number. | `<NumberOfCards>` | Yes | 2 |
| Email | Email address of cardholder. | `<Email>` | Yes | 128 |
| IPAddress | IP address used at the time of the account application. | `<IPAddress>` | Yes | 50 |
| FeeGroupCode | Field used to identify which fee plan is assigned to the customer. | `<FeeGroupCode>` | Yes | 10 |
| ProgramName | Program name linked to the card record. | `<ProgramName>` | Yes | 50 |
| CardCreateDate | Date the card was created. | `<CardCreateDate>` | Yes | 8 (smalldatetime) |
| PrimaryCardIndicator | System indicator which identifies the card record as a primary cardholder, authorised user or secondary user. | `<PrimaryCardIndicator>` | Yes | LEFT BLANK |
| AccountCurrency | Account currency. | `<AccountCurrency>` | Yes | 3 |
| CardProduct | Product associated with the card. | `<CardProduct>` | Yes | 50 |
| Virtual | Indicates if card is virtual:  Y = Virtual  N = Not virtual | `<Virtual>` | Yes | 1 |

#### Example

Below is an example of a typical cardholder record.

[Copy](javascript:void(0);)

```
<CardHolder xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Header>  
    <ProcessorName>GPS</ProcessorName>  
    <ReportName>CUSTMASTER</ReportName>  
    <FileTransmitDate>20210726</FileTransmitDate>  
    <WorkOfDate>20210726</WorkOfDate>  
  </Header>  
  <CardHolderDetails>  
    <ProgramId>ONEUKA</ProgramId>  
    <CardNumber>1131218142558186</CardNumber>  
    <MaskedPAN>113121******8186</MaskedPAN>  
    <CardIssuedDate>20210723</CardIssuedDate>  
    <AccountNumber>4623801132</AccountNumber>  
    <AccountExpiryDate>20240730</AccountExpiryDate>  
    <CardId>121814255</CardId>  
    <CustomerCode>4623801132</CustomerCode>  
    <BranchCode />  
    <FirstName>John</FirstName>  
    <LastName>Tester</LastName>  
    <Address1>57 Haven Meadows</Address1>  
    <Address2 />  
    <City>Boston</City>  
    <State />  
    <Zipcode>PE21 8HH</Zipcode>  
    <Country>826</Country>  
    <DelvAddress1>Taylor Made Services UK Limited</DelvAddress1>  
    <DelvAddress2>2A Pump Square</DelvAddress2>  
    <DelvCity>BOSTON</DelvCity>  
    <DelvState />  
    <DelvZipcode>PE21 6QW</DelvZipcode>  
    <DelvCountry>826</DelvCountry>  
    <Phone1>+447774478784</Phone1>  
    <Phone2 />  
    <IDType1 />  
    <IDNumber1 />  
    <CountryOfIssuance1 />  
    <IDType2 />  
    <IDNumber2 />  
    <CountryOfIssuance2 />  
    <CardStatus>02</CardStatus>  
    <CardStatusDate>20210723</CardStatusDate>  
    <ActualBalance>0.00</ActualBalance>  
    <ActualBalanceSign>-</ActualBalanceSign>  
    <AccountCreatedDate>20210706</AccountCreatedDate>  
    <CardActivationDate />  
    <CardTransferNumberFrom />  
    <NegBalDate />  
    <NegBalPrincipleAmt>0.00</NegBalPrincipleAmt>  
    <NegBalFeeAmt>0.00</NegBalFeeAmt>  
    <TypeOfCard>MCRD</TypeOfCard>  
    <AuthenticationType>PIN</AuthenticationType>  
    <EnrollmentNumber>N/A</EnrollmentNumber>  
    <AccountStatus>02</AccountStatus>  
    <AccountStatusDate>20210723</AccountStatusDate>  
    <DateOfBirth>20050116</DateOfBirth>  
    <AvailableBalance>0.00</AvailableBalance>  
    <AvailableBalanceSign>-</AvailableBalanceSign>  
    <PrimaryCard>I</PrimaryCard>  
    <CardExpiryDate>20240630</CardExpiryDate>  
    <FirstLoadDate />  
    <LastTransactionDate />  
    <LastReissuedDate>20210723</LastReissuedDate>  
    <NumberOfCards>1</NumberOfCards>  
    <Email />  
    <IPAddress />  
    <FeeGroupCode>1143</FeeGroupCode>  
    <ProgramName>ONEUKA</ProgramName>  
    <CardCreateDate>20210706</CardCreateDate>  
    <PrimaryCardIndicator />  
    <AccountCurrency>GBP</AccountCurrency>  
    <CardProduct>OnePay AllPay Payroll</CardProduct>  
    <Virtual>N</Virtual>  
  </CardHolderDetails>  
</CardHolder>
```

## 3.4 Trailer

The Trailer element is used to describe the Count record.

| Child Element | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| Count | Count of total Cardholder details | `<Count>` | Yes | int |

#### Example

[Copy](javascript:void(0);)

```
<TRAILER>  
<Count>1618</Count>  
</TRAILER>
```

## 3.5 Empty Report Example

Below is an example of an empty report, returned if there were no cards issued in the last 24 hour period.

[Copy](javascript:void(0);)

```
<CardHolder xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance%22 >  
<Header>  
<ProcessorName>GPS</ProcessorName>  
<ReportName>CUSTMASTER</ReportName>  
<FileTransmitDate>20210614</FileTransmitDate>  
<WorkOfDate>20210614</WorkOfDate>  
</Header>  
<Trailer>  
<Count>0</Count>  
</Trailer>  
</CardHolder> 
```