## 9.9 Transaction Report Sub-elements and Attributes

This section describes the message [sub-elements](#Sub-elem) and [attributes](#Attribut).

### 9.9.1 Sub-elements

Sub-elements are listed below in alphabetical order.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [Account](#Account)  [Additional\_Amt\_DE54](#Addition)  [AdjustType](#AdjustTy)  [AgencyAccount](#Agency)  [Amount](#Amount)  [Amt](#Amt)  [ApprCode](#ApprCode)  [ARN](#ARN)  [BasicAmount](#BasicAmo)  [BillAmt](#BillAmt)  [BookingType](#BookingT)  [BookingStatus](#BookingS) | [[[BSA](#BSA)](#Card)](#Cash2)  [[Card](#Card)](#Cash2)  [CashAmt](#Cash2)  [CashbackAmt](#Cashback)  [CashCode](#Cash)  [CCAAmount](#CCAAmou)  [ChargebackRefNum](#Chargeba)  [Classification](#Classifi)  [CommissionAmt](#Commissi)  [CycleNumber](#CycleNum)  [DeclineReason](#Decline)  [Desc](#Desc) | [Destination](#Destinat)  [External](#External)  [Event](#Event)  [Fee](#Fee)  [FeeAmt](#FeeAmt)  [FeeClass](#FeeClas)  [FIID](#FIID)  [File](#File)  [FunctionCode](#Function)  [LoadSource](#LoadSou)  [LoadType](#LoadTyp) | [LocalDate](#LocalDat)  [MastercardFeeClass](#MasterC)  [MerchCode](#MerchCod)  [MsgSource](#MsgSourc)  [OperationType](#Operatio)  [OrigTxnAmt](#OrigTxnA)  [Other](#Other)  [PaddingAmt](#PaddingA)  [Pending\_Billing\_Amount](#Pending_)  [Recon](#Recon)  [Receiver](#Receiver)  [ReconciliationDate](#Reconcil) | [ReconciliationCycle](#Reconcil2)  [[[RecordType](#RecType)](#RecType)](#Response)  [[RecType](#RecType)](#Response)  [Response](#Response)  [ReversalReason](#Reversal)  [RIID](#RIID)  [Schema](#Schema)  [Sender](#Sender)  [Settlement](#Settleme2)  [SettlementAmt](#Settleme5) (Mastercard only)  [SettlementCycle](#Settleme4)  [SettlementDate](#SchemeSe) | [SettlementIndicator](#Settleme3)  [SettlementRecapID](#Settleme6)  [[SchemeSettlementDate](#SchemeSe)](#Source)  [Source](#Source)  [[Term](#Term)](#Trace)  [Trace](#Trace)  [Txn](#Txn)  [TxnAmt](#TxnAmt)  [TxnCode](#TxnCode)  [UniqueTransactionReference](#UniqueTr)  [Usage](#Usage) |

### Account

The `Account` element describes a card account.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| no | The 9 digit Thredd public token linked to the card Primary Account Number (PAN). | xs:string | Yes | Alphanumeric, maximum 28 characters. |
| type | Card type | xs:string | Yes | Numeric string, maximum 2 characters. Valid values are:     | Value | Description | | --- | --- | | 00 | Domestic Maestro | | 01 | MasterCard | | 02 | VisaCard | | 07 | Discover Global Network | |

#### Example

[Copy](javascript:void(0);)

```
<Account no="123456789"type="07"></Account>
```

### Additional\_Amt\_DE54

The `Additional_Amt_DE54` element contains additional amount information about the transaction, if relevant. For example, for purchase with cashback transactions, the additional amounts field displays the cashback amount.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Additional fees data | xs:string | Alphanumeric, maximum 123 characters. |

#### Example

[Copy](javascript:void(0);)

```
<Additional_Amt_DE54>0040985D000000020000</Additional_Amt_DE54>
```

### AdjustType

The `AdjustType` element shows the type of balance adjustment â either *Actual* (the money was deducted) or *Blocked* (the amount on the card has been blocked).

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Type of balance adjustment | xs:string | Maximum length 6 characters. |

#### Example

[Copy](javascript:void(0);)

```
<AdjustType>Actual</AdjustType>
```

### AgencyAccount

The `AgencyAccount` element describes a card account and the related agency bank account.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| no | Cardholder Account Number | xs:string | Yes | Alphanumeric, maximum 28 characters. |
| type | Account type | xs:string | Yes | Numeric string, maximum 2 characters  Valid values are: 00 = Domestic Maestro; 01 = MasterCard |
| sortcode | Agency sort code | xs:string |  | Alphanumeric, maximum 6 characters. |
| bankacc | Allocated agency bank account | xs:string |  | Alphanumeric, maximum 8 characters. |
| name | Cardholder name | xs:string |  | Alphanumeric, maximum 28 characters. |

#### Example

[Copy](javascript:void(0);)

```
<AgencyAccount no="123456789" type="01" sortcode="123456" bankacc="12345678" name="John Smith"></AgencyAccount>
```

### Amount

The `Amount` element describes a monetary amount.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the cash movement. | <Direction> | Yes | See [direction.](#directio) |
| value | The monetary amount. | xs:decimal | Yes | Decimal value. |
| currency | The 3 character ISO currency code. | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |

#### Example

[Copy](javascript:void(0);)

```
<Amount direction="debit"value="0.95"currency="826"></Amount>
```

### Amt

The `Amt` element describes the net transaction amount of the original transaction, as reported by Mastercard.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the cash movement. | <Direction> | Yes | See [direction.](#directio) |
| value | The net transaction value. | xs:decimal | Yes | Decimal value. |
| currency | The 3-character ISO currency code. | xs:unsigned  short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |

#### Example

[Copy](javascript:void(0);)

```
<Amt direction="debit"value="0.95"currency="826"></Amt>
```

### ApprCode

The `ApprCode` element describes the approval or authorisation code from the Issuer. This is the 6 digit number printed on the customer's receipt to indicate a successful payment.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Approval Code | xs:string | Alphanumeric, maximum 6 characters. |

#### Example

[Copy](javascript:void(0);)

```
<ApprCode>123456</ApprCode>
```

### ARN

The `ARN` element indicates the Acquirer Reference Number as generated by the [acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#).

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Acquirer Reference Number | xs:string | Alphanumeric, maximum 23 characters. |

#### Example

[Copy](javascript:void(0);)

```
<ARN>12345678901234567890123</ARN>
```

### BasicAmount

The `BasicAmount` data type describes a monetary amount loaded or unloaded from a card.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The monetary value. | xs:decimal | Yes | Decimal value (6 decimal places). |
| value2 | The 4-decimal place version of the value. (optional) | xs:decimal | Yes | Decimal value (4 decimal places) |
| currency | The ISO 3-character currency code. | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |

#### Example

[Copy](javascript:void(0);)

```
<BasicAmount value="0.95"currency="826"></BasicAmount>
```

### BillAmt

The `BillAmt` element describes the amount billed. Not that the `BillAmt` element does not include interchange.

| Attribute | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the billing amount. | xs:decimal | Yes | Decimal value. |
| currency | The currency of the transaction (3 digit ISO currency code). | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |
| rate | The conversion rate used to calculate the billing amount value. | <RateAmount> | Yes | Decimal value, maximum 9 decimal places, using conventional rounding down (1-4) and up (5-9). |

#### Example

The `BillAmt` shown below represents 10 GBP at an exchange rate of 1:1.

[Copy](javascript:void(0);)

```
<BillAmt value="10.00"currency="826"rate="1.000000000"></BillAmt>
```

### BookingType

The `BookingType` element shows the transaction type that triggered the FX conversion, such as an authorisation or presentment.

| Code | Description |
| --- | --- |
| A | A normal Authorisation has triggered this |
| C | Credit to cardholder (refund or Payment Out) |
| E | Auth Expiry Reversal |
| M | Manual, back office foreign exchange (for future use) |
| P | Unauthorised Presentment |
| R | Triggered by an Auth Reversal |
| Q | Presentment Reversal |
| S | Surplus, returned funds after a presentment |
| T | Topup, additional funds required after a presentment |
| U | Partial Authorisation Reversal |
| W | Inter-Wallet transfer |

#### Example

The `BookingType` shown below represents a normal authorisation.

[Copy](javascript:void(0);)

```
<BookingType>A</BookingType>
```

### BookingStatus

The `BookingStatus` element shows the status of the booking.

| Code | Description |
| --- | --- |
| B | Booked |
| R | Reversed |
| X | Retries exceeded |
| E | Error other than a timeout |

#### Example

The `BookingStatus` shown below represents a booked transaction.

[Copy](javascript:void(0);)

```
<BookingStatus>B</BookingStatus>
```

### BSA

The `BSA` element describes the Business Service Arrangement (BSA) type code, which is provided by Mastercard. This field can have values of:

1 = Inter-regional

2 = Intra-regional

3 = Inter-country\* (also called subregional)

4 = Intra-country (also called domestic)

8 = Member-to-member (also called bilateral)

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Business Service Arrangement type code. | xs:string | Numeric, maximum 1 character. |

#### Example

[Copy](javascript:void(0);)

```
<BSA>4</BSA>
```

### Card

The `Card` element describes the key attributes of a payment card.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| PAN | Primary Account Number if PCI DSS Compliant. Alternatively, this number is the Thredd 16-digit public token. | <PAN> | Yes | See [PAN.](#PAN) |
| product | The Card Scheme associated with the card. For example:  MCRD - Mastercard; VISA - Visa; MAES - Maestro | xs:string | Optional | Alphanumeric, maximum 4 characters. |
| programid | Program identifier, which is the co-brand (i.e. Thredd Sub-Scheme) that the Program Manager operates. | xs:string | Optional | Alphanumeric, maximum 50 characters. |
| branchcode | The branch code (or Agent Code) associated with the card. | xs:string | Optional | Alphanumeric, maximum 8 characters. |
| productID | The Thredd product ID associated with the card. | numeric | Optional | Numeric, maximum 5 characters. |

#### Example

[Copy](javascript:void(0);)

```
<Card PAN="12345678123456"product=""programid=""branchcode=""productID=""></Card>
```

### CashAmt

The `CashAmt` element describes the cash amount of the receipt or payment before any bank charges are deducted.

| Attribute | Description | Data Type | Required | Constraints /  Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the cash amount. | xs:decimal | Yes | Decimal value. |
| currency | The currency of the transaction (3 digit ISO currency code). | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |

#### Example

[Copy](javascript:void(0);)

```
<CashAmt value="10.00" currency="826"></CashAmt>
```

### CashbackAmt

The `CashbackAmt` element describes the cashback amount requested by the cardholder. If no cashback has been requested, then the element is presented with the *value* attribute set at zero and the *currency* attribute value defaulted to the transaction currency.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The transaction value. | xs:decimal | Yes | Decimal value. |
| currency | The currency of the transaction (3 digit ISO currency code). | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |

#### Example

[Copy](javascript:void(0);)

```
<CashbackAmt value="10.00"currency="826"></CashbackAmt>
```

### CashCode

The `CashCode` element describes transaction type and direction.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the transaction. | <Direction> | Yes | See [direction.](#directio) |
| CashType | The type of transaction. | xs:string | Yes | Accepts one of the following values:     | CashType | Description | | --- | --- | | bac | BACS | | CHAPS | CHAPS | | fpy | Faster Payment (Receipt or payment) | | ddp | Direct Debit Payment setup, authorisation and initiation | | cbt | Cardholder initiated balance transfer between own accounts | | ipp | Inter program payment between two customers within same agency sort code | | p2p | Peer-to-peer payment between two cardholders | | FasterPayment Reject | Faster Payment which is rejected by the Card Scheme.  (In this case, an inbound payment will be created to move money from the customer's account to holding account.) | | ModulrReturn | An outbound return received from Modulr which is processed as inbound payment. | | SEPAIn | Inbound SEPA (Single European Payment Area) payment | | SEPAOut | Outbound SEPA payment | | SEPAPayment Return | SEPA payment which is rejected by the Card Scheme. | | DirectDebitOut Notification | Direct Debit payment notification, indicating that a direct debit transaction has been initiated. | | DirectDebitOut Payout | Direct debit payout, indicating that the actual transfer of funds to the payee's account has occurred. | |  | Space or an empty value | |
| CashGroup | The summary group type of the transaction. | xs:string | Yes | Takes one of the following values:     | CashType | Description | | --- | --- | | rcp | Receipt | | pay | Payment | |

#### Example

[Copy](javascript:void(0);)

```
<CashCode direction="debit" CashType="fpy" CashGroup="pay"></CashCode>
```

### CCAAmount (Mastercard only)

The `CCAAmount` element describes the Currency Conversion Assessment (CCA) amount as calculated by the network (Mastercard only). The `currency` attribute value defaults to the CardFinancial (Presentment) billing currency.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The Currency Conversion Assessment value. | xs:decimal | Yes | Decimal value. |
| currency | The Currency transaction described in ISO Standard Currency code. | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |
| included | Clarifies whether the CCA amount has been included in the FX fee, which is a product-level configuration option. | <YesNoString> | Yes | Valid values are: â¢ yes â¢ no |

#### Example

[Copy](javascript:void(0);)

```
<CCAAmount value="0.01"currency="826" included="no"></CCAAmount>
```

### ChargebackRefNum

The `ChargebackRefNum` element holds the chargeback CycleID value and is shown as *Chargeback Ref Num* in Smart Client.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Unique for a Chargeback record. Normally 10 characters long. | xs:string | Numeric. Maximum 50 characters. |

#### Example

[Copy](javascript:void(0);)

```
<ChargebackRefNum>9034102149</ChargebackRefNum>
```

### Classification

The `Classification` element describes the Merchant Category Code (MCC), which is used to classify the type of business service provided by the merchant.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| MCC | Merchant Category Code | <MCC> | Yes | See [MCC](#MCC). |

#### Example

[Copy](javascript:void(0);)

```
<Classification MCC="5659"></Classification>
```

### CommissionAmt

The `CommissionAmt` element describes the value of the commission applied to a Card Authorisation only. The *commission* is the fees that Thredd applies to the card, based on the Fee configuration for the card (combination of the rate fee and fixed fee). For more information, see the Thredd Fees Guide.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the commission amount. | xs:decimal | Yes | Decimal value. |
| currency | The three-digit ISO currency code. | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |

#### Example

[Copy](javascript:void(0);)

```
<CommissionAmt value="0.95"currency="826"></CommissionAmt>
```

### CycleNumber

The `CycleNumber` element is the sub-group for daily reconciliation/settlement activities based on timing.

For Discover, `CycleNumber`will be always 01 as there will be no division in daily reconciliation/settlement.

The CycleNumber is not applicable to Visa transactions, as Visa do not have the concept of settlement or reconciliation cycles.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 01 | Cycle number 01 | xs:string |
| 02 | Cycle number 02 | xs:string |
| 03 | Cycle number 03 | xs:string |
| 04 | Cycle number 04 | xs:string |
| 05 | Cycle number 05 | xs:string |
| 06 | Cycle number 06 | xs:string |

#### Example

[Copy](javascript:void(0);)

```
<CycleNumber>03</CycleNumber>
```

### DeclineReason

The `DeclineReason` element describes the reason a receipt was rejected and returned to source, or a payment request was declined and not processed.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| The reason a receipt or payment was declined. | xs:string | Maximum length two chararacters:     | Value | Description | | --- | --- | | 00 | Not specified | | 01 | Insufficient funds | | 02 | Maximum number of transactions exceeded | | 03 | Transaction exceeds maximum permitted value | | 04 | Maximum account balance exceeded | | 05 | Black listed destination | | 06 | Not a valid account | | 07 | Account closed | | 08 | Cardholder deceased | | 09 | No valid Direct Debit instruction | |

#### Example

[Copy](javascript:void(0);)

```
<DeclineReason>01</DeclineReason>
```

### Desc

The `Desc` element provides descriptive text to provide a comment on a transaction. You can supply this value when initiating a card load or unload via web services. Alternatively, Thredd provides the description when the load occurs as a result of a balance transfer between primary and secondary cards.

For Agency banking transactions, this element can be empty.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Descriptive text or reference | xs:string | Maximum length 127 characters. |

#### Example

[Copy](javascript:void(0);)

```
<Desc>Some Descriptive Text</Desc>
```

### Destination

The `Destination` element provides details of the destination wallet account to which funds are transferred in a Multi-FX wallet transaction.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| walletid | ID of the destination wallet account. | bigint | Yes | 0 to 2^64 |
| balancechange | Change in destination wallet account balance amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| blockchange | Change in destination wallet account blocked amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| newbalance | New destination wallet account balance. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| newblock | New destination wallet account blocked amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |

#### Example

[Copy](javascript:void(0);)

```
<Destination walletid="1253" balancechange="15.5000" blockchange="5.5000" newbalance="10.0000" newblock="20.0000"/>
```

### External

The `External` element describes the other bank account in a payment transfer transaction.

| Attribute | Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- | --- |
| sortcode | Source or destination sort code. | xs:string | Numeric 6 characters. |
| bankacc | Source or destination bank account. | xs:string | Numeric 8 characters. |
| name | Sender or recipient's name. | xs:string | Alphanumeric, maximum 28 characters. |

#### Example

[Copy](javascript:void(0);)

```
<External sortcode="123456" bankacc="12345678" name="John Bloggs"></External>
```

### Event

The `Event` element describes an event that has changed a card's status.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| Type | The type of event. | xs:string | Yes | Valid values are:   * Upgraded * Renewed * Lost * Stolen * Cancelled * PINTriesExceeded * Voided * Expired, * Activation * UnBlocked * StatusChange * ReportedToSAFE |
| Source | The item source (`ItemSrc`) of a card activation. Only applies to card activations. | xs:unsignedbyte | If applicable | See `ItemSrc` in the Web Services Guide.  Defaults to 0. |
| ActivationDate | The date of activation. Only applies to card activations. | xs:string | If applicable |  |
| ConvertedDate | The date of conversion from a virtual to a physical card. | xs:string | If applicable |  |
| StatCode | Status code of the card after the event. | xs:string | Yes | See *Status Codes* in the Web Services Guide. |
| OldStatCode | Status code of the card before the event. | xs:string | Yes | See *Status Codes* in the Web Services Guide. |
| Date | Date and time of the event (UK daylight savings time). | xs:string | Yes | Format: YYYYMMDDHHMMSS |
| transactionid | The unique transaction ID for a *ReportedToSafe* event. This event can be used to track Mastercard [SAFE reportingClosed The period of time during which waits for an approved authorisation amount to be settled. This is defined at a product level. A typical default is 7 days for an auth and 10 days for a pre-auth.](#) transactions. | xs:string | If applicable | Numeric. Only applicable if the event `Type` is *ReportedToSAFE*. |

#### Example - StatusChange

[Copy](javascript:void(0);)

```
<Event Type="StatusChange" Source="0" StatCode="62" OldStatCode="00" Date="20210307153523" transactionid="" ></Event>
```

#### Example - ReportedToSafe

[Copy](javascript:void(0);)

```
<Event Type="ReportedToSAFE" Source="0" StatCode="" OldStatCode="" Date="20210307153523" transactionid="1234567890" ></Event>
```

### Fee

The `Fee` element describes a fee amount.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the fee. | <Direction> | Yes | See [direction.](#directio) |
| value | The value of the fee amount(PDS0147). | xs:decimal | Yes | Decimal value. |
| currency | The 3 digit ISO standard currency code. | xs:unsigned  short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |
| value2 | The value of the fee amount(PDS0146). Only for Mastercard records.  Not applicable to Visa or Discover. | xs:decimal | Optional | Decimal value. |

#### Example

[Copy](javascript:void(0);)

```
<Fee direction="debit" value="3.330000" currency="826" value2="3.3300" ></Fee>
```

### FeeAmt

The `FeeAmt` element describes the fee amount as received from Mastercard.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the fee. | <Direction> | Yes | See [direction.](#directio) |
| value | The value of the fee. For Programme Manager fees, this is the sum total of any rate fee, fixed fee or other fee applied to the transaction (see `Rate_Fee` and `Fixed_Fee` in the [CardAuthorisation](CardAuthorisation.htm#LoadSou) record). For Scheme fees, it is the fee amount as received from the Scheme. | xs:decimal | Yes | Decimal value. |
| currency | The 3-digit ISO standard currency code. | xs:unsigned  short | Yes | See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |

#### Example

[Copy](javascript:void(0);)

```
<FeeAmt direction="debit"value="0.95"currency="826"></FeeAmt>
```

### FeeClass

The `FeeClass` element describes the nature of a fee.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| interchangeTransaction | Valid values are *yes* and *no*  Note: The value is yes when the FeeClass type is 4 or 5 | <YesNoString> | Yes | Valid values are:  â¢ yes  â¢ no |
| type | Describes the type of the fee. | xs:string | Yes | Valid values are:     | Value | Description | Fee Type | | --- | --- | --- | | 1 | Cardholder fee: In this case the account number in the fee message refers to the cardholderâs account. | Cardholder Fee | | 2 | MasterCard funds transfer settlement fee | Settlement Fee | | 4 | MasterCard interchange received fee | Settlement Fee | | 5 | MasterCard interchange fee to be paid | Settlement Fee |     For a CardFinancial, `FeeClass` element record, the `type` attribute always has a value of 1. |
| code | Specifies the type of cardholder fee. | xs:string | Yes | The value specified below depends upon the message code (fee identifier).  Where the `FeeClass` `type` attribute is 0,2,4 or 5, then the `code` attribute is 0.  For a card Financial, `FeeClass` element record, the `code`attribute always has a value of 1. |
| memberID | Specifies the [ICAClosed Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.](#) | xs:string | No | Only applicable to `MastercardFee`. |

#### Example

[Copy](javascript:void(0);)

```
<FeeClass interchangeTransaction="no"type="1"code="1"></FeeClass>
```

### FIID

The `FIID` element describes the Forwarding Institution Identification Code (FIID).

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| A code identifying the forwarding institution | xs:string | Alphanumeric, maximum 11 characters. |

#### Example

[Copy](javascript:void(0);)

```
<FIID>0123456</FIID>
```

### File

The `File` element describes the file in which the receipt was notified or the outbound payment was submitted for processing. This element is used for outbound file-based processing with Agency banking.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| filedate | Date and time of file containing receipt or date the payment file is generated. | xs:string | Yes | Maximum 14 characters, date and time in the format: YYYYMMDDHHMMSS |
| filename | Name of file containing receipt or payment. | xs:string | Yes | Alphanumeric, maximum 100 characters. |

#### Example

[Copy](javascript:void(0);)

```
<File filedate="20100824155111" filename="ABC123xyz"></File>
```

### FunctionCode

The `FunctionCode` element is used by Mastercard to describe the transaction functions the clearing system performs.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 400 | Denotes âFullâ. Used for Mastercom Chargebacks. | integer |
| 451 | Denotes âPartialâ. Used for Mastercom Chargebacks. | integer |
| 603 | Retrieval Request. | integer |
| 605 | Retrieval Request Acknowledgement. | integer |
| 685 | Financial Position Detail (Chargeback -Mastercom). | integer |
| 700 | Fee Collection (Member-generated) / For Mastercom pre-arbitration or arbitration case filing. | integer |
| 780 | Fee Collection Return (Member-generated). | integer |
| 781 | Fee Collection Resubmission (Member-generated). | integer |
| 782 | Fee Collection Arbitration Return (Member-generated). | integer |
| 783 | Fee Collection (Clearing System-generated). | integer |
| 790 | Fee Collection (Funds Transfer) â applies only in the IPM Pre-edit system to UK Domestic Maestro transactions. | integer |

### LoadSource

The `LoadSource` element describes the source of the Card Load or Unload.

| Attribute | Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- | --- |
| Source | The source of the Load / Unload request. | xs:string | Maximum length 3 characters.  For more information, see [EHI Guide > Load Sources](https://docs.thredd.com/ehi/Content/Appendices/Load_Source.htm). |
| Type | The type of the Load/Unload request. Payment method of funds for the load. | xs:string | 0 = Unknown  1 = Cash  2 = Debit card  3 = Credit card  4 = e-Wallet  5 = Bank account |
| FixedFee | The amount of any Fixed Fee that was applied. | xs:decimal |  |
| Rate\_Fee | The amount of any Rate Fee that was applied. | xs:decimal |  |

#### Example

[Copy](javascript:void(0);)

```
<LoadSource source="9"Type="1"FixedFee="0.00"Rate_Fee="0.00"/></LoadSource
```

### LoadType

The `LoadType` element describes the type of funds used in a Card Load or Unload transaction.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| The type of fund used in the Card Load or Unload. | xs:string | Maximum length 2 characters.     | Value | Description | | --- | --- | | 0 | Not Specified | | 1 | Cash | | 2 | Debit card | | 3 | Credit Card | | 4 | Import | | 5 | Savings Stamps | | 6 | Cheque | | 7 | Standing Order | | 8 | Export | | 9 | Transfer | | 10 | Funding Card | | 11 | From/To Offline Balance | |

#### Example

[Copy](javascript:void(0);)

```
<LoadType>6</LoadType>
```

### LocalDate

The `LocalDate` element describes the date and time when the message was received from the card network in local UK time.

| Description | BaseType | Constraints / Permitted Values |
| --- | --- | --- |
| Date and time. | xs:string | Maximum 14 characters, date and time in the format: YYYYMMDDHHMMSS |

#### Example

The example below shows a date/time of 2:20.33pm on 25th Jan 2021.

[Copy](javascript:void(0);)

```
<LocalDate>20210125142033</LocalDate>
```

### MastercardFeeClass

The `MastercardFeeClass` data type describes the type of Mastercard fee.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| interchangeTransaction | Valid values are *yes* and *no*  Note: The value is yes when the FeeClass type is 4 or 5 | <YesNoString> | Yes | Valid values are:  â¢ yes  â¢ no |
| type | Describes the type of the fee. | xs:string | Yes | Valid values are:     | Value | Description | Fee Type | | --- | --- | --- | | 0 | Network fee: These are fees generated by Thredd or MasterCard clearing. In this case the account number in the fee message refers to the fee account for Thredd. | Settlement Fee | | 2 | MasterCard funds transfer settlement fee | Settlement Fee | | 4 | MasterCard interchange received fee | Settlement Fee | | 5 | MasterCard interchange fee to be paid | Settlement Fee | |
| code | Specifies the type of cardholder fee. | xs:string | Yes | 0 |
| memberid | Specifies the Mastercard Member ID ( i.e. [ICAClosed Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.](#)) | xs:string | Yes | Maximum 6 characters.  **Note**: This element is only present when the container element of FeeClass is âMastercardFeeâ. |

#### Example

[Copy](javascript:void(0);)

```
<MastercardFeeClass interchangeTransaction="no"type="0"code="0"memberid="012345"></MastercardFeeClass>
```

### MerchCode

The `MerchCode` element is the Card Acceptor Merchant Identifier supplied by the acquirer. This a unique number that is used to identify the merchant or originator of the transaction.

| Expected Value | BaseType | Constraints / Permitted Values |
| --- | --- | --- |
| Merchant Code / Card Acceptor Identifier. | xs:string | Alphanumeric, maximum 15 characters. |

#### Example

[Copy](javascript:void(0);)

```
<MerchCode>ABCD12345678</MerchCode>
```

### MsgSource

The `MsgSource` element describes the source from which the message is derived.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The source from which this message is derived. | xs:decimal | Yes | Maximum length two; must be one of the following values:     | Value | Description | | --- | --- | | 12 | Outgoing fees to Visa. | | 17 | Outgoing fees to Mastercard. This must be applied to all outgoing settlement fees. | | 62 | This value is applicable on CardAuthorisation records only. | | 66 | ECCEDD or GCMS using the ECCF file format (Mastercard International). | | 67 | GCMS using IPM file format (Mastercard International). | | 74 | UK Domestic Maestro using the IPM file format. | | 54 | Visa International. | | 70 | Discover Global Network | |
| domesticMaestro | Indicates Domestic Maestro. | <domestic  Maestro> | Yes | See [domesticMaestro.](#domestic) |

#### Example

[Copy](javascript:void(0);)

```
<MsgSource value="67"domesticMaestro="no"></MsgSource>
```

### OperationType

The `OperationType` sub-element describes the type of wallet transaction.

| ID | Name | Description |
| --- | --- | --- |
| 1 | Authorisation | Authorisation transaction (Point of Sale, e-commerce or ATM). |
| 2 | Financial | Financial transaction type (e.g., presentment). |
| 3 | Fees | All kinds of non-transaction based fees, such as recurring fees and card usage fees. |
| 4 | Loads | Funds loaded to the wallet account using a Thredd web service. |
| 5 | Unloads | Funds unloaded from the wallet account using a Thredd web service. |
| 6 | Wallet Transfer | Funds transferred between wallet accounts. |
| 7 | Balance Recalculation | Balance recalculation. Certain operations will cause the balance to be recalculated without otherwise affecting the balance. |
| 8 | Closure Requested | Request to close the wallet account. |
| 9 | Closure Complete | The wallet account is closed after all pending authorisations have been dealt with. |
| 10 | Wallet Opening | Used to record the (re-)opening of a wallet account. |
| 11 | Authorisation Expiry | Indicates either a forced or automatic authorisation expiry. |

#### Example

[Copy](javascript:void(0);)

```
<OperationType>1</OperationType>
```

### OrigTxnAmt

This `OrigTxnAmt` element describes the original transaction amount requested by the cardholder.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the original transaction. | xs:decimal | Yes | Decimal value. |
| currency | The currency code of the original transaction. | xs:unsignedShort | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |
| partial | Indicates a partial amount. | <YesNoString> | If applicable | Valid values are:  â¢ yes  â¢ no  If not supplied, assumes ânoâ. |
| origItemId | The system trace audit number of the original authorisation, as assigned by the message originator. This can be used to link an authorisation reversal to the original authorisation. | xs:unsignedInt | If applicable | 0 to 4,294,967,295 |

#### Example

[Copy](javascript:void(0);)

```
<OrigTxnAmt value="0.95"currency="826" partial="yes"origItemId="123456"></OrigTxnAmt>
```

### Other

The `Other` element describes the Non-wallet amount and currency (e.g., for loads and unloads)..

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the amount. | decimal (19,8) | Yes | Decimal value: Precision = 19 digits, scale = 8 digits. |
| currency | The 3 digit ISO standard currency code. | xs:unsignedShort | Yes | Currency in ISO 3-digit number format. See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |

#### Example

[Copy](javascript:void(0);)

```
<Other amount="15.5000" currency="AUD"/>
```

### PaddingAmt

The `PaddingAmt` element describes the value of any padding amount applied to an authorisation. This is typically used to mitigate against FX rate fluctuations between the authorisation and the settlement.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the padding amount. | xs:decimal | Yes | Decimal value. |
| currency | The 3 digit ISO standard currency code. | xs:unsignedShort | Yes | Short value. |

#### Example

[Copy](javascript:void(0);)

```
<PaddingAmt value="0.95"currency="826"></PaddingAmt>
```

### PaymentToken

The `PaymentToken` element is populated from payment token data when a payment token was used for the transaction. If no payment token was used, then the `PaymentToken` element is omitted.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| id | Unique Thredd ID of the payment token. Only present if transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes |  |
| creator | Identifies which system created the payment token. Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | MDES or VDEP |
| expdate | Expiry date of the payment token. Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | Format YYYY-MM-DD |
| type | The type of system the payment token is encoded onto (defines how the payment token PAN is held). Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | See [type.](../Appendices/Payment_Token_Fields.htm#type) |
| status | Current status of the payment token as set by Thredd. Only present if transaction relates to a payment token (for example, Apple Pay). Please note this can differ from the status of the PAN. | xs:string | Yes | 00 = authorised. |
| creatorstatus | Current status of the payment token as set by the creator of the payment token. Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | See [creatorstatus](../Appendices/Payment_Token_Fields.htm#creatorS) . |
| wallet | Wallet that the payment token belongs to. Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | See [wallet](../Appendices/Payment_Token_Fields.htm#wallet). |
| devicetype | Indicates the type of the device in which the payment token is held. Only present if the transaction relates to a payment token (for example, Apple Pay). | xs:string | Yes | See [devicetype](../Appendices/Payment_Token_Fields.htm#deviceTy). |
| lang | The ISO 639-1 2 character alpha language code reported by the payment token device at digitisation time. Only present if the transaction relates to a payment token (for example, Apple Pay). For a list of ISO 639-1 language codes, see http://www.iso.org  **Note**: The code may not be known, in which case the field will be empty. | xs:string | Yes |  |
| activationexpiry | The Date and Time in UTC (GMT) when the activation code in the field PaymentToken activationCode expires. Only present if the first two characters of ProcCode=â34â (payment token activation notification).  **Note**: Milliseconds are present, but will always be zero. For Mastercard, seconds will always be zero. | xs:string | Yes |  |
| activationmethod | The method by which the cardholder should obtain the Activation Code (in the field PaymentToken\_activationCode) They must enter the activation code into the device holding the payment token in order to activate it. Only present if first two characters of ProcCode=â34â (payment token activation notification). | xs:string | Yes | See [activationmethod](../Appendices/Payment_Token_Fields.htm#activati) |

#### Example

[Copy](javascript:void(0);)

```
<PaymentToken id="26025313" creator="MC-MDES" expdate="2024-04-30" type="SE" status="00" creatorstatus="A" wallet="APPLE" devicetype="M" lang="" activationexpiry="2021-03-02 11:52:00" activationmethod="1" />
```

### Pending\_Billing\_Amount

The `Pending_Billing_Amount` element shows the value of the pending Chargeback amount.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Chargeback amount. | xs:decimal | Decimal value. |

#### Example

[Copy](javascript:void(0);)

```
<Pending_Billing_Amount>10.25</Pending_Billing_Amount>
```

### Recon

The `Recon` element provides details of the [reconciliation date![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date](#) and clearing cycle.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| date | Date the original  transaction was reconciled. | xs:string | Optional | Maximum 8 characters. Date in the format: YYYYMMDD |
| cycle | Indicates which of the Mastercard clearing cycles the transaction was processed in. | xs:string | Optional | Values 01 - 06. |

#### Example

An example of a settlement which occurred in cycle 1 on 11th September 2021 is shown below.

[Copy](javascript:void(0);)

```
<Recon date="20210911" cycle="01"/></recon>
```

### Receiver

The `Receiver` element provides details of the receiver of the payment where there is a money transfer. See also [Sender](#Sender).

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| firstname | FirstName | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| middlename | Middle Name | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| lastname | Last Name | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| streetaddress | Street Address | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| city | City | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| provincecode | Province code | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| country | Country | xs:string | Optional | Normally 3-character alpha ISO code |
| postcode | Postcode | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| dateofbirth | Date of birth | xs:string | Optional | Format: MMDDYYYY |
| accountnumber | Account Number | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idtype | Id type | xs:string | Optional | | Value | Description | | --- | --- | | 00 | Passport | | 01 | National Identification Card | | 02 | Driverâs License | | 03 | Government Issued | | 04 | Other | | 05â10 | Reserved | |
| idnbr | Id number | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idctrycode | ID Country Code | xs:string | Optional | Normally 3-character alpha ISO code |
| nationality | Nationality | xs:string | Optional | Normally 3-character alpha ISO code |
| phonenumber | Phone Number | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idexpdate | ID expiry Date | xs:string | Optional | Format: MMDDYYYY |
| acctnbrtype | Account Number Type | xs:string | Optional | | Values | Description | | --- | --- | | 00 | Other | | 01 | RTN + Bank Account | | 02 | IBAN | | 03 | Card Account | | 04 | Email | | 05 | Phone Number | | 06 | Bank account number (BAN) + Bank Identification Ð¡ode (BIC) | | 07 | Wallet ID | | 08 | Social Network ID | |
| birthctry | Birth Country | xs:string | Optional | Normally 3-character alpha ISO code |
| fundssource | Fund Source | xs:string | Optional | | Code | Meaning | | --- | --- | | 01 | Visa credit | | 02 | Visa debit | | 03 | Visa prepaid | | 04 | Cash | | 05 | Debit/deposit access accounts other than those linked to a Visacard (includes checking/savings accounts and proprietary debit/ATM cards) | | 06 | Credit accounts other than those linked to a Visa card (includes credit cards and proprietary credit lines) | |
| claimcode | Claim Code | xs:string | Optional | Alphanumeric, maximum 99 characters. |

#### Example

[Copy](javascript:void(0);)

```
<Receiver firstname="FRST" middlename="M" lastname="LST NME" streetaddress="RM R STREET S STREETI " city="MAIN" provincecode="MD" country="MDA"   
postcode="00000" dateofbirth="07051999" accountnumber="4779300008363000" idtype="04" idnbr="2014011000399" idctrycode="MDA" nationality="MDA"   
phonenumber="2811131" idexpdate="102020" acctnbrtype="08" birthctry="MDA" fundssource="04" claimcode="TST"></Receiver>
```

### ReconciliationDate

The `ReconciliationDate` element shows the [reconciliation date![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date](#) of a Chargeback record.

| Description | Data Type | Constraints / Per |
| --- | --- | --- |
| Reconciliation date of Chargeback record. | xs:string | Maximum 8 characters, Date in the format:  YYYYMMDD |

#### Example

[Copy](javascript:void(0);)

```
<ReconciliationDate>20200325</ReconciliationDate>
```

### ReconciliationCycle

The `ReconciliationCycle` element shows the [reconciliation cycle![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your mode, may also provide STIP on your behalf, where your systems are unavailable.](#) of the Chargeback record.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Reconciliation cycle of Chargeback record. | xs:string | Maximum 2 characters, Possible values are 01,02,03,04,05 and 06. |

#### Example

[Copy](javascript:void(0);)

```
<ReconciliationCycle>03</ReconciliationCycle>
```

### RecordType

The `RecordType` element is used to distinguish between different fee types. (Relevant to Mastercard only)

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| This can have different values depending on the primary element. For example:  For a chargeback, where the value of RecordType is *MCB*.  To find out the chargeback fee amount, refer to the fee amount (`<FeeAmt>`) of the [MasterCardFee](MasterCardFee.htm) record.  To view the original chargeback amount, refer to the `<BillAmt>` in the [CardChrgBackRepRes](CardChrgBackRepRes.htm#top) record.  For case filing where the value of RecordType is *MCF*, refer to the [MasterCardFee](MasterCardFee.htm) record for details of pre-aribtration and arbitration case filing fees. | xs:string | Maximum length 3.     | Value | Description | | --- | --- | | FC | From FeeCollection. | | MCB | Mastercom Chargebacks. Raised either via Mastercom UI or Mastercom SmartClient API. | | MCF | Mastercom pre-arbitration or arbitration case filing.  Raised either via Mastercom UI or Mastercom Smartclient API. | | VFC | Visa Fee Collection. | | DGN | Discover Group Network | |

#### Example

[Copy](javascript:void(0);)

```
<RecordType>DGN</RecordType >
```

### RecType

The `RecType` element describes whether this record is an advice or a reversal.

| Permitted Value | Description | DataType |
| --- | --- | --- |
| ADV | Advice Record | xs:string |
| REV | Reversal Record | xs:string |

#### Example

[Copy](javascript:void(0);)

```
<RecType>ADV</RecType>
```

### Response

The `Response` element describes the approval status of a transaction request.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| approved | Approval component. | <approved> | Yes | See [approved](#approved). |
| actioncode | Describes the transaction status, which can be either 4 or 0:  4 = indicates a decline or where the transaction type is an authorisation advice  0 = indicates a transaction status that is not a decline or an authorisation advice  For a CardFinancial, `ActionCode` is always zero. | xs:string | If applicable | Applies to [CardAuthorisation](CardAuthorisation.htm) and [CardFinancial](CardFinancial.htm) only. |
| responsecode | Holds the *ResponseStatus* field from the authorisation record in the Thredd database (as sent to the card scheme). This is a 2 digit Response Code which is based on the ISO 8583:1987 standard. It corresponds to the DE39 response code field that Thredd sent in the response message.    In most cases, the `responsecode` field should match the authorisation *ResponseStatus* you provided in your [EHIClosed The Card Transaction System (CTS) enables you to test the integration of your card processing systems and validate the setup of your External Host Interface (EHI).](#) response. The exception is for EHI modes where:   * Thredd did not receive your EHI response and made a Stand-In Processing (STIP) decision * Thredd received your EHI response, but determined the *ResponseStatus* was not valid * The EHI response you sent was an internal Thredd response code (such as 'C0' or 'C1'). In this case the `responsecode` field will reflect the response actually sent to the card scheme (after mapping from an internal Thredd EHI ResponseStatus value) | xs:string | If applicable | Applies to [CardAuthorisation](CardAuthorisation.htm) and [CardFinancial](CardFinancial.htm) only. |
| additionaldesc | Extra information. | xs:string | If applicable | Maximum 500 characters. Applies to [CardAuthorisation](CardAuthorisation.htm) only. |

#### Example

[Copy](javascript:void(0);)

```
<Response approved="yes"actioncode="0"responsecode="00"></Response>
```

### ReversalReason

The `ReversalReason` element describes the reason for a reversal.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Original authorisation was matched. This is where the original Authorisation value from the BLKAMT field was cancelled. This increases the AMTAVL balance because a settlement transaction has been matched and processed.  This code would be used if the CardAuthorisationâs AuthId is populated in the matching CardFinancialâs Child Element AuthId. | xs:string |
| 1 | Original authorisation has expired. This is where the original Authorisation value from the BLKAMT field was cancelled.This increases the AMTAVL balance even though a settlement transaction has not been identified before the expiry of the Authorisation time limit.  This code would be used if the CardAuthorisationâs AuthId is not present in any CardFinancialâs Child Element AuthId. | xs:string |
| 2 | Manually deleted, where the erroneously processed authorisation and reversal for a merchant is processed directly into the processorâs system. | xs:string |
| 3 | Online reversal, where the erroneously processed authorisation and reversal for a merchant is entered via the processorâs online portal. | xs:string |

#### Example

[Copy](javascript:void(0);)

```
<ReversalReason>0</ReversalReason>
```

### RIID

The `RIID` element describes the Receiving Institution Identification Code (RIID). This is the Program Manager's [ICA![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.](#) as provided by Mastercard or the equivalent account code from Visa.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Receiving Institution Identification Code. | xs:string | Alphanumeric, maximum 11 characters. |

#### Example

[Copy](javascript:void(0);)

```
<RIID>00000000123</RIID>
```

### Schema

The `Schema` element describes the name of the card scheme processing the transaction. For example: Visa (VISA), Mastercard (MCRD).

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| CIRR | Euro Cirrus | xs:string |
| ECRD | EuroCard | xs:string |
| MAES | Maestro | xs:string |
| CIMA | Cirrus Maestro | xs:string |
| MCRD | Mastercard | xs:string |
| VISA | Visa | xs:string |
| PLUS | PLUS Card | xs:string |
| DGN | Discover Global Network | xs:string |

#### Example

[Copy](javascript:void(0);)

```
<Schema>DGN</Schema>
```

### Sender

The `Sender` element provides details of the sender of the payment, where there is a money transfer. See also [Receiver](#Receiver).

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| firstname | FirstName | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| middlename | Middle Name | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| lastname | Last Name | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| streetaddress | Street Address | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| city | City | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| provincecode | Province code | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| country | Country | xs:string | Optional | Normally 3-character alpha ISO code. |
| postcode | Postcode | xs:string | Optional | Alphanumeric, maximum 99 characters.. |
| dateofbirth | Date of birth | xs:string | Optional | Format: MMDDYYYY |
| accountnumber | Account Number | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idtype | The type of identification provided by the user. | xs:string | Optional | Values are:     | Value | Description | | --- | --- | | 00 | Passport | | 01 | National Identification Card | | 02 | Driverâs License | | 03 | Government Issued | | 04 | Other | | 05â10 | Reserved | |
| idnbr | Identification number (e.g. passport or driver license number) | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idctrycode | ID country code (e.g. 826) | xs:string | Optional | Normally 3-character alpha ISO code. |
| nationality | Nationality | xs:string | Optional | Normally 3-character alpha ISO code. |
| phonenumber | Phone number | xs:string | Optional | Alphanumeric, maximum 99 characters. |
| idexpdate | Identification expiry date | xs:string | Optional | Format: MMDDYYYY |
| acctnbrtype | The type of account number | xs:string | Optional | | Values | Description | | --- | --- | | 00 | Other | | 01 | RTN + Bank Account | | 02 | IBAN | | 03 | Card Account | | 04 | Email | | 05 | Phone Number | | 06 | Bank account number (BAN) + Bank Identification Ð¡ode (BIC) | | 07 | Wallet ID | | 08 | Social Network ID | |
| birthctry | Country of birth | xs:string | Optional | Normally 3-character alpha ISO code. |
| fundssource | Source of funds | xs:string | Optional | | Code | Meaning | | --- | --- | | 01 | Visa credit | | 02 | Visa debit | | 03 | Visa prepaid | | 04 | Cash | | 05 | Debit/deposit access accounts other than those linked to a Visacard (includes checking/savings accounts and proprietary debit/ATM cards) | | 06 | Credit accounts other than those linked to a Visa card (includes credit cards and proprietary credit lines) | |
| claimcode | Claim code | xs:string | Optional | Alphanumeric, maximum 99 characters. |

#### Example

[Copy](javascript:void(0);)

```
<Sender firstname="FRST" middlename="M" lastname="LST NME" streetaddress="RM R STREET S STREETI " city="MAIN" provincecode="MD" country="MDA"   
postcode="00000" dateofbirth="07051999" accountnumber="4779300008363000" idtype="04" idnbr="2014011000399" idctrycode="MDA" nationality="MDA"   
phonenumber="2811131" idexpdate="102020" acctnbrtype="08" birthctry="MDA" fundssource="04" claimcode="TST"></Sender>
```

### Settlement

The `Settlement` element describes the Settlement details.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| date | Date the original  transaction was settled. | xs:string | Optional | Maximum 8 characters, Date in the format: YYYYMMDD |
| cycle | Indicates which of the Mastercard clearing cycles the transaction was processed in. | xs:string | Optional | Values 01 - 06. |

#### Example

An example of a Settlement which occurred in cycle 1 on 9th September 2017 is shown below.

[Copy](javascript:void(0);)

```
<Settlement date="20170911" cycle="01"/></Settlement>
```

### SettlementAmt

The `SettlementAmt` element describes the settlement amount.

For Visa, the SettlementAmt is set by Thredd to the same as the Cardholder Billing amount (`BillAmt`).

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the settlement amount. | xs:decimal | Yes | Decimal value. |
| currency | The 3 digit ISO code of currency that the transaction will be settled in. | xs:unsigned  Short | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |
| rate | The conversion rate used to calculate the settlement amount value.  Not applicable to Discover. | <Rate> | Yes | Decimal value, maximum 9 decimal places, using conventional rounding down (1-4) and up (5-9). |
| date | Date the original transaction was settled. | xs:string | If applicable | Maximum 8 characters, Date in the format: YYYYMMDD  Only required for chargebacks and representments. |

#### Example

The example below represents 10 GBP at an exchange rate of 1:1.

[Copy](javascript:void(0);)

```
<SettlementAmt value="10.00"currency="826"rate="1.000000000"  
date="20100825"></SettlementAmt>
```

### SettlementCycle

The `SettlementCycle` element describes the settlement cycle of the Chargeback record.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Settlement cycle of a Chargeback record. | xs:string | Maximum length 2 characters. Possible value: 01. |

#### Example

[Copy](javascript:void(0);)

```
<SettlementCycle>01</SettlementCycle>
```

### SettlementDate

The `SettlementDate` element describes the date when the transaction is settled.

In the `CardAuthorisation` element, this field only provides the Thredd transaction date.

| Description | BaseType | Constraints / Permitted Values |
| --- | --- | --- |
| Date (UTC) | xs:string | Maximum 8 characters, date in the format: YYYYMMDD |

#### Example

[Copy](javascript:void(0);)

```
<SettlementDate>20210125</SettlementDate>
```

### SettlementIndicator

The `SettlementIndicator` element describes the type of settlement service, for example whether this is International or clearing-only.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| The type of settlement service. | xs:string | Maximum length 1. Values are:     | Value | Description | | --- | --- | | 0 | International settlement service. | | 3 | Clearing-only (valid only for countries with defined service). | | 4 | Bilateral settlement. (Mastercard Only) | | 8 | National Net settlement service (valid only for countries with defined service). | | 9 | BASEII selects the appropriate settlement service based on routing and country-defined default. (Visa Only) | |

#### Example

[Copy](javascript:void(0);)

```
<SettlementIndicator>0</SettlementIndicator>
```

### SettlementRecapID

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Settlement Recap ID is a Discover Global Network specific data element. Discover members send financial transaction data grouped under recaps separately for each member. Settlement Recap ID defines the recap breakdown to help members for their reconciliation with Discover. | xs:string | Possible values are:     | Value | Description | | --- | --- | | RecapDate | Settlement group date | | RecapNumber | Settlement group number | | SendingIIC | Sending Issuer Identification Code (IIC) | | ReceivingIIC | Receiving Issuer Identification Code (IIC) | | CurrencyCode | 3 Digit transaction currency code | |

#### Example

[Copy](javascript:void(0);)

```
<SettlementRecapID RecapDate="20240531" RecapNumber="092" SendingIIC="00000361641" ReceivingIIC="00000361603" CurrencyCode="GBP"/SettlementRecapID>
```

### SchemeSettlementDate

The `SchemeSettlementDate` element describes the scheme first presentment settlement date in a financial advice or reversal. The data contained in this element is taken from the following data sources received from Mastercard and set by Thredd for Visa:

* Mastercard -  DE48 PDS0159 subfield 8
* Visa - Thredd settlement date

| Description | BaseType | Constraints / Permitted Values |
| --- | --- | --- |
| Date (UTC) | xs:string | Maximum 8 characters, date in the format: YYYYMMDD. |

#### Example

[Copy](javascript:void(0);)

```
<SchemeSettlementDate>20240125</SchemeSettlementDate>
```

### Source

The `Source` element provides details of the source wallet account from which funds are taken.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| walletid | ID of the source wallet account. | bigint | Yes | 0 to 2^64 |
| basecurrency | Base currency of the source wallet account. | int | Yes | Currency in ISO 3-digit number format. See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |
| balancechange | Change in source wallet account balance amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| blockchange | Change in source wallet account blocked amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| newbalance | New source wallet account balance. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |
| newblock | New source wallet account blocked amount. | decimal (19,4) | Yes | Precision = 19 digits, scale = 4 digits. |

#### Example

[Copy](javascript:void(0);)

```
<Source walletid="879" basecurrency="978" balancechange="10.5000" blockchange="5.5000" newbalance="5.0000" newblock="10.0000"/>
```

### Term

The `Term` element provides details of the terminal used in a POS card transaction.

| Attribute | Description | Data Type | Required | Constraints/Permitted Values. |
| --- | --- | --- | --- | --- |
| code | Card acceptor terminal ID (Mastercard DE 41 field). This is a unique code identifying a terminal at the card acceptor location. | <code> | Yes | See [code](#code) |
| location | Defines the site where the terminal is located, either a branch code or a store name. | xs:string | Yes | Maximum 64 characters |
| street | Description of the terminal street location. | xs:string | Yes | Maximum 64 characters |
| city | City | xs:string | Yes | Maximum 64 characters |
| country | Country code â ISO code. | xs:string | Yes | Must be 2 Characters.  See [EHI Guide > ISO Country Codes.](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm) |
| inputcapability | The primary capability of the terminal for entering card information. | <inputcapability> | Yes | See [PDS0105](#PDS0105) |
| authcapability | This is the method available to verify the cardholder at this terminal. | <authcapability> | Optional | See [authcapability](#authcapa) |

#### Example

[Copy](javascript:void(0);)

```
<Term code="N376131"location="A BANK"street="A STREET"city="A CITY"  
country="GB"inputcapability="5"authcapability="1"></Term>
```

### Trace

The `Trace` element provides an audit number that can be used in combination with other elements to identify a transaction.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| auditno | Card scheme System Trace Audit Number (STAN). The STAN is a 6 digit acquirer reference number between 000001 and 999999, generated sequentially by each acquirer. After reaching 999999 the acquirer repeats the STAN from 000001. The audit number remains unchanged for all messages within the life of the transaction (i.e. original and reversal). For partial reversals, a new Audit Number is required.    **Note**: The STAN is typically only unique per Card Scheme network, per Acquirer, per day. Acquirers who process more than 1000000 transactions per day will repeat the STAN. Therefore, auditno cannot be used to provide a unique reference.  **Tip**: You can use the AuthId element to uniquely identify a transaction. | xs:string | Optional | Alphanumeric, maximum 6 characters |
| origauditno | This is only populated if the containing record is a reversal, and represents information regarding the original transaction. | xs:string | Optional | Alphanumeric, maximum 6 characters |
| Retrefno | Retrieval Reference Number. Contains a document reference supplied by the system retaining the original source information (ATM acquirer) and is used to assist in locating that information or its copy | xs:string | Yes | Alphanumeric, maximum 12 characters |

#### Example

[Copy](javascript:void(0);)

```
<Trace auditno="1234"origauditno="345"Retrefno="AN1234"></Trace>
```

### Txn

The `Txn` element describes how a transaction was validated and authenticated.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| cardholderpresent | Indicates whether the cardholder was present during the transaction. | <cardholderpresent> | Yes | See [cardholderpresent.](#cardhold) |
| cardpresent | Indicates whether the card was present during the transaction. | <cardpresent> | Yes | See [cardpresent.](#cardpres) |
| cardinputmethod | The method used to input the information from the card to the terminal. | <cardinputmethod> | Yes | See [cardinputmethod.](#cardinpu) |
| cardauthmethod | The cardholder authentication method used in a card transaction. | <cardauthmethod> | Yes | See [cardauthmethod.](#cardauth) |
| cardauthentity | The component or person who verified the cardholder identity as reported in the `cardauthmethod` field. | <cardauthentity> | Yes | See [cardauthentity.](#cardauth2) |
| TVR | Terminal Verification Results. This is the 10 hexadecimal characters representing the TVR 5 binary bytes.  This field should only be interpreted for EMV transactions (`Cardauthentity` and `Cardinputmethod`).  Not applicable for Discover phase 1 | xs:unsigned  Long | If applicable | This field is only present in financial advices if the Acquirer systems provide Chip data  Default value is zero. |
| TTI | Three-digit Transaction Type Identifier (Mastercard DE 048, PDS 0043 field). This is populated whenever it is found in the source presentment data for a [CardFinancial](CardFinancial.htm) record. Not applicable to other record types.  Not applicable for Discover phase 1 | <TTI> | Optional | This field can be used to support Mastercard QMR Reporting. For details of possible values, see the Mastercard IPM Clearing Formats manual, |

#### Example

[Copy](javascript:void(0);)

```
<Txn cardholderpresent="0"cardpresent="1"cardinputmethod="2"  
cardauthmethod="3"cardauthentity="3"TVR="0"TTI="C07"></Txn>
```

### TxnAmt

The `TxnAmt` element describes a transaction amount (value and currency).

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| value | The value of the transaction amount. | xs:decimal | Yes | Decimal value. |
| currency | The transacted currency code. | xs:unsignedShort | Yes | See [EHI Guide > ISO Country Codes](https://docs.thredd.com/ehi/Content/Appendices/Country_Codes.htm). |

#### Example

[Copy](javascript:void(0);)

```
<TxnAmt value="10.00"currency="826"></TxnAmt>
```

### TxnCode

The `TxnCode` element describes the transaction type and direction.

| Attribute | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| direction | The direction of the transaction. | <Direction> | Yes | See [direction](#directio) |
| Type | Details of the type of transaction. | xs:string | Yes | Must be one of the following values     | Value | Description | | --- | --- | | pos | Point of Sale transaction. | | atm | Automated Teller Machine transaction (Cash Withdrawal/Advance) | | pos\_cb | Point of Sale transaction with cashback. | | pos\_re | Purchase refund. | | fee | Fee collection.  If direction is a debit the fee is a credit to the transaction originator.  If the direction is a credit then the fee is a debit to the transaction originator. | | tfr | Cardholder funds transfer. | |
| Group | The summary group type of the transaction. | <Group> | Yes | See [Group](#Group). |
| ProcCode | The first two digits of the Processing Code + the two digits of the AccountType + Two digits of the Destination Account. See [Processing Codes](../Appendices/Processing_Codes.htm). | xs:string | If applicable | For example: "000000", "003000", "010000"  **Note**: "390000" is used to identify an [Account VerificationClosed A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation. For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.](#) transaction. |
| Partial | If a fee was charged, indicates whether the fee was partial.  Not applicable for Discover. | xs:string | If applicable | Default:âNAâ |
| FeeWaivedOff | If a fee was charged and the fee was partial, shows the amount of the fee that was not charged.  Not applicable for Discover. | xs:decimal | If applicable | Default:0 |

#### Example

[Copy](javascript:void(0);)

```
<TxnCode direction="debit"Type="atm"Group="atm"ProcCode="000000"></TxnCode>
```

### UniqueTransactionReference

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Unique reference for the transaction, from Discover. | xs:string | Alphanumeric, maximum 15 characters, may be null. |

#### Example

[Copy](javascript:void(0);)

```
<UniqueTransactionReference>073679876543210</TxnCode>
```

### Usage

The `Usage` element indicates whether the Chargeback was credited to a card.

| Description | Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Indicates whether the Chargeback is manually credited to card. | xs:string | Maximum 1-character. Possible values are:     | Value | Description | | --- | --- | | 0 | Credit acknowledged, cleared and not credited to a card. | | 1 | Credit acknowledged, cleared and credited to a card for arbitration Chargeback. | | M | Mastercard, Credit acknowledged, cleared and credited to a card. | | S | Related to a Visa card. | |

#### Example

[Copy](javascript:void(0);)

```
<Usage>1</Usage>
```

### 9.9.2 Attributes

Attributes are listed below in alphabetical order.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [approved](#approved)  [authcapability](#authcapa)  [cardholderpresent](#cardhold) | [cardauthentity](#cardauth2)  [cardauthmethod](#cardauth)  [cardinputmethod](#cardinpu) | [cardpresent](#cardpres)  [code](#code)  [direction](#directio) | [domesticMaestro](#domestic)  [Group](#Group)  [inputcapability](#inputcap) | [MCC](#MCC)  [PAN](#PAN)  [PDS0105](#PDS0105) |

### approved

The `approved` attribute describes whether a transaction was approved.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| yes | Approved | xs:string |
| no | Not Approved | xs:string |

#### Example

[Copy](javascript:void(0);)

```
approved="yes"
```

### authcapability

The `authcapability` attribute describes the capabilties of the terminal.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | No electronic authentication | xs:string |
| 1 | PIN | xs:string |
| 2 | Electronic Signature Analysis | xs:string |
| 3 | Biometrics | xs:string |
| 4 | Biographs | xs:string |
| 5 | Manual signature verification | xs:string |
| 6 | Manual other | xs:string |
| 7 | Offline PIN | xs:string |
| 8 | Online PIN | xs:string |
| 9 | 3D-Secure | xs:string |
| 10 | Account based digital signature | xs:string |
| 11 | Public key based digital signature | xs:string |
| 12 | Unknown | xs:string |
| 13 | RFU | xs:string |
| 14 | RFU | xs:string |
| 15 | RFU | xs:string |
| 16 | RFU | xs:string |
| 17 | RFU | xs:string |
| 18 | RFU | xs:string |
| 19 | RFU | xs:string |

#### Example

[Copy](javascript:void(0);)

```
authcapability="1"
```

### cardholderpresent

The `cardholderpresent` attribute describes whether a cardholder was present during a transaction.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Cardholder present | xs:string |
| 1 | Not present, unspecified | xs:string |
| 2 | Not present, mail order | xs:string |
| 3 | Not present, telephone | xs:string |
| 4 | Not present, standing authorisation | xs:string |
| 5 | Not present, electronic order | xs:string |
| 6 | Not present, instalment transaction | xs:string |
| 9 | Unknown | xs:string |

#### Example

[Copy](javascript:void(0);)

```
cardholderpresent="3"
```

### cardauthentity

The `cardauthentity` attribute describes the entity that authenticated the cardholder.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Not Authenticated | xs:string |
| 1 | Integrated Chip Card | xs:string |
| 2 | ISO10202 = Terminal | xs:string |
| 3 | Authorising Agent | xs:string |
| 4 | Merchant | xs:string |
| 5 | Other | xs:string |
| 6 | Cardholder device | xs:string |
| 7 | Wallet Provider / Token Requestor | xs:string |
| 8 | Unknown | xs:string |

#### Example

[Copy](javascript:void(0);)

```
cardauthentity="8"
```

### cardauthmethod

The `cardauthmethod` attribute describes the authentication method used in a card transaction.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Not authenticated | xs:string |
| 1 | PIN | xs:string |
| 2 | electronic signature analysis | xs:string |
| 3 | Biometrics | xs:string |
| 4 | Biographic | xs:string |
| 5 | Manual Signature Verification | xs:string |
| 6 | Manual Other (e.g. Licence) | xs:string |
| 7 | Other | xs:string |
| 8 | Unknown | xs:string |
| 9 | Passcode/Password (e.g mobile phone unlock code, or One-Time-Passcode sent to cardholder) | xs:string |
| A | Pattern (e.g. mobile phone device unlock pattern) | xs:string |
| B | Possession of hardware device (eg phone, number generating keyfob) | xs:string |
| C | As 'B' but additionally with user verification | xs:string |
| D | Possession of software application (e.g. passcode generating program) | xs:string |
| E | As 'D' but additionally with user verification | xs:string |
| S | 3D-secure cardholder authentication | xs:string |

#### Example

[Copy](javascript:void(0);)

```
cardauthmethod="1"
```

### cardinputmethod

The `cardinputmethod` attribute describes the method used to input the card data (e.g.,PAN) into the point of sale terminal.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | unspecified | xs:string |
| 1 | manual, no terminal | xs:string |
| 2 | magnetic stripe read | xs:string |
| 3 | bar code | xs:string |
| 4 | OCR | xs:string |
| 5 | integrated circuit card (ICC) | xs:string |
| 6 | key entered | xs:string |
| 7 | contactless ICC | xs:string |
| C | E-Commerce with channel encryption and chip cryptogram used | xs:string |
| E | Contactless magnetic stripe | xs:string |
| F | Account Data on file | xs:string |
| G | Key entered by acquirer | xs:string |
| M | MICR reader | xs:string |
| P | Mobile banking application | xs:string |
| Q | QR code | xs:string |
| V | E-Commerce | xs:string |
| W | DPAN | xs:string |

#### Example

[Copy](javascript:void(0);)

```
cardinputmethod="5"
```

### cardpresent

The `cardpresent` attribute indicates whether a card was present during a transaction.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Card not present | xs:string |
| 1 | Card present | xs:string |
| 9 | Unknown | xs:string |

#### Example

[Copy](javascript:void(0);)

```
cardpresent="1"
```

### code

The `Code` attribute describes the card acceptor terminal ID (Mastercard DE 41 field). This is a unique code identifying a terminal at the card acceptor location.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Terminal Code | xs:string | Maximum 8 Characters |

#### Example

[Copy](javascript:void(0);)

```
code="12345678"
```

### direction

The `Direction` attribute describes the direction of a cash movement.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| credit | Describes a credit transaction. | xs:string |
| debit | Describes a debit transaction. | xs:string |

#### Example

[Copy](javascript:void(0);)

```
direction="debit"
```

### domesticMaestro

The `domesticMaestro` attribute indicates whether a transaction originates from a Domestic Maestro card.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| yes | Used to indicate that the transaction originates from a domestic Maestro card. | xs:string |
| no | Used to indicate that the transaction does not originate from a domestic Maestro card. | xs:string |

#### Example

[Copy](javascript:void(0);)

```
domesticMaestro="yes"
```

### Group

The `Group` attribute describes the high-level transaction type.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| pos | Point of Sale Transactions (including reversals). | xs:string |
| atm | Automated Teller Machine transactions (including reversals). | xs:string |
| fee | Fees. | xs:string |

#### Example

[Copy](javascript:void(0);)

```
Group="atm"
```

### inputcapability

The `inputcapability` attribute describes the card input capability.

| Permitted Value | Description | Data Type |
| --- | --- | --- |
| 0 | Unknown | xs:string |
| 1 | Manual - no Location | xs:string |
| 2 | Magnetic Stripe Read | xs:string |
| 3 | Bar Code | xs:string |
| 4 | OCR | xs:string |
| 5 | EMV contact | xs:string |
| 6 | Key Entered | xs:string |
| 7 | Contactless Magnetic Stripe | xs:string |
| 8 | EMV contactless | xs:string |
| 9 | Account Data on file | xs:string |
| 10 | QR code | xs:string |
| 11 | E-Commerce | xs:string |
| 12 | E-Commerce with EMV cryptogram | xs:string |
| 13 | MICR reader | xs:string |
| 14 | Mobile Banking | xs:string |
| 15 | RFU | xs:string |
| 16 | RFU | xs:string |
| 17 | RFU | xs:string |
| 18 | RFU | xs:string |
| 19 | RFU | xs:string |

#### Example

[Copy](javascript:void(0);)

```
inputcapability="6"
```

### MCC

The `MCC` attribute describes the [Merchant Category Code![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.](#) (MCC).

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| Merchant category code. | xs:string | Maximum 4 characters.  Permissible values as per Mastercard  Global Rules for Merchant Classification Codes. |

#### Example

[Copy](javascript:void(0);)

```
MCC="5921"
```

### PAN

The `PAN` attribute contains the Primary Account Number if you are PCI DSS Compliant or otherwise the [Thredd 16-digit public token](#GPS).

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| PAN (Primary Account Number). | xs:string | Minimum 12 characters, maximum 19 characters |

#### Example

[Copy](javascript:void(0);)

```
PAN="12345678123456"
```

#### Thredd 16-digit public token

The format of the 16-digit Thredd public token is as follows:

*xxxYYYYYYYYYzzzz*

where:

* *xxx* â is the 3 digits derived from the Thredd internal scheme ID
* *YYYYYYYYY* â is the 9-digit Thredd public token
* *zzzz* â is the last 4 digits of the card's PAN

### PDS0105

The `PDS0105` attribute describes the name of the financial advice file received from Mastercard.

| Description | Base Data Type | Constraints / Permitted Values |
| --- | --- | --- |
| File\_ID\_PDS0105 | xs:string | Format as follows :  âT112.001â + âYYMMDDâ + â00000012181â + XXYZZ  Where XX = Clearing cycle indicator  Y = delivery cycle  ZZ = file number in the given clearing cycle |