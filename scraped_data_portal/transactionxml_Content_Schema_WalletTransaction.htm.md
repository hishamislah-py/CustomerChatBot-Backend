# 2.13 WalletTransaction

WalletTransaction records are linked to an existing transaction and are used to provide details of transactions on a Multi-FX wallet account.

You can use the `Id` element to uniquely identify the record and distinguish it from all other WalletTransaction records.

| Child Element | Description | Data Type | Required | Constraints/  Permitted  Values |
| --- | --- | --- | --- | --- |
| Id | Unique identifier for this wallet transaction record. | bigint | Yes | 0 to 2^64 |
| TransactionId | Identifier for the underlying transaction (e.g., authorisation or financial). | bigint | Yes | 0 to 2^64 |
| SequenceNumber | Sequence number for the transaction, starting from 1. | int | Yes | 0 to 2^32 |
| OperationType | Type of operation (e.g., 1= authorisation, 2 = Financial). | int | Yes | See the [OperationType](Sub_Elements_and_Attributes.htm#Operatio) sub-element. |
| Source | Details of the source wallet account from which funds are taken. | <Source> | Yes | See the [Source](Sub_Elements_and_Attributes.htm#Source) sub-element. |
| Destination | Details of the destination wallet account to which funds are transferred. | <Destination> | Yes | See the [Destination](Sub_Elements_and_Attributes.htm#Destinat) sub-element. |
| Other | Non-wallet amount and currency (e.g., for loads and unloads). | <Other> | Optional | See the [Other](Sub_Elements_and_Attributes.htm#Other) sub-element. |
| FxRate | The FX rate applied to this transaction. | decimal (19,8) | Yes | Decimal value: Precision = 19 digits, scale = 8 digits. |

#### Example

[Copy](javascript:void(0);)

```
<WalletTransaction>  
<Id>6</Id>  
<TransactionId>7899161819</TransactionId>  
<SequenceNumber>2</SequenceNumber>  
<OperationType>1</OperationType>  
<Source walletid="879" basecurrency="978" balancechange="10.5000" blockchange="5.5000" newbalance="5.0000" newblock="10.0000"/>  
<Destination walletid="1253" balancechange="15.5000" blockchange="5.5000" newbalance="10.0000" newblock="20.0000"/>  
<Other amount="15.5000" currency="AUD"/>  
<FxRate>1.100000000</FxRate>  
</WalletTransaction>
```