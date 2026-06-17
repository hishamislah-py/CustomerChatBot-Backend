# 2.3 ACCOUNT

The ACCOUNT element describes an account, balance and currency information. Cards linked to this account are described inside the CARD element.

An account is included in the Balance report if any of the conditions below are met:

* the account has a non-zero balance
* the account has blocked funds
* the account had a non-zero balance or blocked funds within the last two days

Accounts with a zero balance and no blocked funds will be excluded from the Balance report.

Account Number (`ACCNO`) and Currency Code (`CURRCODE`) combine to form a unique record key.  Only one instance of an ACCNO/CURRCODE combination can appear in the ACCOUNT element in a Balance report file.

For example:

* You can have two accounts with the same account numbers but different currency codes.

* You cannot have the same account number and the same currency code more than once.

| Child Element | Description | Occurs | Data Type | Required | Constraints / Permitted  Values |
| --- | --- | --- | --- | --- | --- |
| ACCNO | Account number. | 1 | <ACCNO> | Yes | See [ACCNO](Sub_Elements_and_Attributes.htm#ACCNO) |
| CURRCODE | Account 3-letter ISO currency code. | 1 | <CRDCURRCODE> | Yes | See [CRDCURRCODE](Sub_Elements_and_Attributes.htm#CRDCURRC) |
| ACCTYPE | Account type. | 1 | <ACCTYPE> | Yes | See [ACCTYPE](Sub_Elements_and_Attributes.htm#ACCTYPE) |
| SORTCODE | Agency Banking sort code (if applicable). | 0-1 | <SORTCODE> | Optional | See [SORTCODE](Sub_Elements_and_Attributes.htm#SORTCODE) |
| BANKACC | Agency Banking account number assigned to the card account (if applicable). | 0-1 | <BANKACC> | Optional | See [BANKACC](Sub_Elements_and_Attributes.htm#BANKACC) |
| FEEBAND | Agency Banking Auth Fee Group code (if applicable). | 0-1 | xs:string | Optional | Alpha, maximum. 10 characters |
| PAYMENT | Additional payment options activated by card account holder. | 0-1 | <PAYMENT> | Optional | See [PAYMENT](Sub_Elements_and_Attributes.htm#PAYMENT) |
| FINAMT | Full account balance. (If negative, will be signed, e.g., -7.00)  See the following description on [FINAMT](#FINAMT) | 1 | xs:decimal | Yes | Decimal value  Empty fields allowed to support null values. |
| BLKAMT | Pending authorisations amount. (If negative, will be signed)  See the following description on [BLKAMT](#BLKAMT) | 1 | xs:decimal | Yes | Decimal value Empty fields allowed to support null values. |
| AMTAVL | Account balance amount available (i.e., *AMTAVL = FINAMT â BLKAMT*).  (If negative, will be signed)  See the following description on [AMTVAL](#AMTAVL) | 1 | xs:decimal | Yes | Decimal value Empty fields allowed to support null values. |
| LINKEDTOKEN | If the card is linked to another card with a different account, then the field holds the Thredd public token of the linked card. | 0-1 | <LINKEDTOKEN> | Optional | See [LINKEDTOKEN](Sub_Elements_and_Attributes.htm#LINKEDTO) |
| CARD | A card linked to this account. | 0-n | <CARD> | Optional | See [CARD](Card.htm#_CARD) |

Each of the three Account Balance child elements (FINAMT, BLKAMT and AMTAVL) can be updated by the following transaction types:

For details of the transaction type records below, refer to the Transaction XML Reporting Guide.

## 2.3.1 FINAMT

* CardFinancial transactions (RecordType ADV & REV)
* CardChrgBackRepRes transactions (RecordType CB, CBREV, REPRES & REPRESREV)
* CardLoadUnload transactions (RecordType LOAD, LOADREV, UNLOAD & UNLOADREV)
* CardFee transactions
* CardBalAdjust (RecType ADV & REV)
* Approved AgencyBanking transactions

## 2.3.2 BLKAMT

The BLKAMT element

* CardAuthorisation transactions (RecType ADV)
* A subsequent matching CardAuthorisation Reversal (RecType REV)

## 2.3.3 AMTAVL

AMTAVL = sum of FINAMT less BLKAMT

##### Example

[Copy](javascript:void(0);)

```
<ACCOUNT>  
  <ACCNO>1234567891012145</ACCNO>  
  <CURRCODE>GBP</CURRCODE>  
  <ACCTYPE>00</ACCTYPE>  
  <FINAMT>238.76</FINAMT>  
  <BLKAMT>10.00</BLKAMT>  
  <AMTAVL>228.76</AMTAVL>  
  <CARD>â¦detail ommittedâ¦</CARD>  
  <CARD>â¦detail ommittedâ¦</CARD>  
</ACCOUNT>
```