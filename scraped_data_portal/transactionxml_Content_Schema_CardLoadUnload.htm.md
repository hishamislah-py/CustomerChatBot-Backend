# 2.7 CardLoadUnload

The CardLoadUnload primary element is used to describe the following records:

* Card Loads (loading funds onto a card account) and Card Load Reversals
* Card Unloads (discharging funds from a card account) and Card Unload Reversals

You can use the `RecordType` element to determine the type of record.

**Note**: Not primary element is not applicable to the Discover Global Network.

| Child Element | Description | Data Type | Required | Constraints / Permitted Values |
| --- | --- | --- | --- | --- |
| RecordType | Indicates whether this is a Card Load, Load Reversal, Unload or Unload reversal. | xs:string | Yes | Valid values are:  â¢ LOAD  â¢ LOADREV  â¢ UNLOAD  â¢ UNLOADREV |
| LoadUnloadId | A unique identifier for the CardLoadUnload record. | xs:unsignedLong | Yes | 0 to 2^64 |
| LocalDate | The local date and time of the Load/Unload in the local timezone. | <LocalDate> | Yes | See the [LocalDate](Sub_Elements_and_Attributes.htm#LocalDat) sub-element |
| SettlementDate | The settlement date and time for the Load/Unload. | <SettlementDate> | Yes | See the [SettlementDate](Sub_Elements_and_Attributes.htm#Settleme) sub-element |
| Card | Provides details of the card's attributes. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| Account | Details of the cardholder account. | <Account> | Yes | See the [Account](Sub_Elements_and_Attributes.htm#Account) sub-element |
| MerchCode | A unique code identifying the merchant (also know as the Card Acceptor Identifier). | <MerchCode> | No | See the [MerchCode](Sub_Elements_and_Attributes.htm#MerchCod) sub-element |
| Amount | The value of the Load, Load Reversal, Unload or Unload Reversal. | <BasicAmount> | Yes | See the [BasicAmount](Sub_Elements_and_Attributes.htm#BasicAmo) sub-element |
| Desc | Description of the card load or unload, as supplied when the card was loaded or unloaded. | <Desc> | Yes | See the [Desc](Sub_Elements_and_Attributes.htm#Desc) sub-element |
| Load | Describes Load/Unload source and type. | <LoadSource> | Yes | See the [LoadSource](Sub_Elements_and_Attributes.htm#LoadSou) sub-element |

#### Example (Load)

[Copy](javascript:void(0);)

```
<CardLoadUnload>  
    <RecordType>LOAD</RecordType>  
    <LoadUnloadId>13964492698</LoadUnloadId>  
    <LocalDate>20240213172407</LocalDate>  
    <SettlementDate>20240213</SettlementDate>  
    <Card PAN="5792883020134123" product="MCRD" programid="GPS"   
    productid="1463" branchcode="00000000" />  
    <Account no="288301830" type="01" />  
    <MerchCode />  
    <Amount value="5.05" currency="826" direction="credit" />  
    <Desc>Load from primary card: 5792883018303844</Desc>  
    <Load Source="79" Type="0" FixedFee="0.00" Rate_Fee="0.00" />  
</CardLoadUnload>
```