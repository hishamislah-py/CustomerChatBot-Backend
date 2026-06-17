# 2.12 FXConversion

This element is currently removed from the XSD and should not be implemented.

FXConversion records are used to indicate Foreign Exchange (FX) rate conversion.

| Child Element | Description | Data Type | Required | Constraints/  Permitted  Values |
| --- | --- | --- | --- | --- |
| TransactionId | ID of the transaction table entry | Bigint | Yes | The <AuthId>, the unique identifier of the CardAuthorsation XML record that gave rise to this FX conversion |
| WalletTransactionId | The <WalletTransactionId> of the related WalletTransaction XML record. Only present for Multi-FX transactions | Bigint | Yes | 0 for POSFX, or the <WalletTransactionId> of the related WalletTransaction XML record |
| BookingType | Transaction type that triggered the FX conversion, such as an authorisation or presentment | Char(1) | Yes | See the [BookingType](Sub_Elements_and_Attributes.htm#BookingType) sub-element |
| BookingStatus | Status of the booking | xs:string | Optional | Maximum length 1. See the [BookingStatus](Sub_Elements_and_Attributes.htm#BookingStatus) sub-element |
| FXRateBooked | FX rate sent in the presentment message | xs:decimal | Yes | No constraints |
| FXRateCardHolder | FX rate sent in the authorisation message | xs:decimal | Yes | No constraints |
| ProviderCode | FX provider source for this rate | xs:string | Yes | Maximum length 8 |
| FixedAmountFlag | FX fixed amount charge for this transaction | xs:string | Yes | Maximum length 1. Permitted values: S' - Source or 'D' - Destination' |
| SettlementDate | The settlement date as returned by the FX provider | SettlementDate | Optional | No constraints |
| SourceCurrency | Source (Card) Currency (numeric code) | Char(3) | Yes | Standard currency numeric code, e.g. 826 for GBP |
| DestinationCurrency | Destination (Transaction) Currency (numeric code) | Char(3) | Yes | Standard currency numeric code, e.g. 826 for GBP |

#### Example

[Copy](javascript:void(0);)

```
<FXConversion xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <TransactionId >6459161819</TransactionId>  
        <WalletTransactionId>278654</WalletTransactionId>  
        <BookingType>A</BookingType>  
        <BookingStatus>B</BookingStatus>   
        <FXRateBooked>1.10</FXRateBooked>  
        <FXRateCardHolder>1.11</FXRateCardHolder>  
        <ProviderCode>CCI</ProviderCode>  
        <FixedAmountFlag>S</FixedAmountFlag>  
        <SettlementDate>2020-09-02T13:00:00</SettlementDate>  
        <SourceCurrency>826</SourceCurrency>  
        <DestinationCurrency>978</DestinationCurrency>  
</FXConversion>
```