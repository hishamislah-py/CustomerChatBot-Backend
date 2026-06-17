# 2.4 CARD

The CARD element describes a card linked to an ACCOUNT element.

| Child Element | Description | Occurs | Data Type | Required | Constraints / Values |
| --- | --- | --- | --- | --- | --- |
| PAN | Primary Account Number. | 1 | <PAN> | Yes | See [PAN](Sub_Elements_and_Attributes.htm#PAN) |
| MASKEDPAN | Masked Primary Account Number (PAN) where six of the digits are replaced with the \* character. | 0-1 | <MASKEDPAN> | Yes | See [MASKEDPAN](Sub_Elements_and_Attributes.htm#MASKEDPA) |
| VIRTUAL | Indicates if the card is a physical or virtual card. | 1 | <VIRTUAL> | Yes | See [VIRTUAL](Sub_Elements_and_Attributes.htm#VIRTUAL) |
| PRIMARY | Indicates whether or not this is the primary card for the account. | 1 | <PRIMARY> | Yes | See [PRIMARY](Sub_Elements_and_Attributes.htm#PRIMARY) |
| MVC | Indicates whether or not the token of the card is for a Master Virtual Card (MVC) | 0-1 | <MVC> | Optional | See [MVC](Sub_Elements_and_Attributes.htm#MVC) |
| CRDPRODUCT | The Card Scheme (payment network), which is either Visa (VISA) or Mastercard (MCRD). | 1 | <CRDPRODUCT> | Yes | See [CRDPRODUCT](Sub_Elements_and_Attributes.htm#CRDPRODU) |
| PROGRAMID | The Co-Brand (i.e. Sub-Scheme) that the Program Manager operates. | 1 | <PROGRAMID> | Optional | See [PROGRAMID](Sub_Elements_and_Attributes.htm#PROGRAMI) |
| CUSTCODE | This is the reference for the card and will only have a value if a reference was included in the  `CustAccount` field. The token number can be used for this field. | 1 | <CUSTCODE> | Yes | See [CUSTCODE](Sub_Elements_and_Attributes.htm#CUSTCODE) |
| STATCODE | The status of the card. | 1 | <STATCODE> | Yes | See [STATCODE](Sub_Elements_and_Attributes.htm#STATCODE) |
| EXPDATE | The expiry date assigned when the card is created. This is either the date you specified when creating the card, or, if a date was not specified, it is based on the default Card Scheme (payment network) validity period in months (i.e., 36 months from the date of card creation). This date is embossed on the card. | 1 | <EXPDATE> | Yes | See [EXPDATE](Sub_Elements_and_Attributes.htm#EXPDATE) |
| GPSEXPDATE | The expiry date you specified on activation of the card or on card activation and load. If no expiry date is specified, this date is based on the Thredd validity period in days configured at product level (e.g., 1095 days from the date of card activation). | 1 | <GPSEXPDATE> | Yes | See [GPSEXPDATE](Sub_Elements_and_Attributes.htm#GPSEXPDATE) |
| CRDACCNO | Account number of the card. This will be the same as the PAN. | 1 | <CRDACCNO> | Yes | See [CRDACCNO](Sub_Elements_and_Attributes.htm#_Ref11083175) |
| PRIMARYTOKEN | If you are able to receive full PAN details for your cards, then this field provides the full Primary Account Number (PAN) of the card, as follows:   * If the card is a primary card, then this field will display the PAN of the primary card * If the card is a secondary card, then this field will display the PAN of the linked primary card   **Note**: This field will not be displayed if you do not receive full PAN or this is a Multi-FX card. | 1 | <PRIMARYTOKEN> | Optional | See [PRIMARYTOKEN](Sub_Elements_and_Attributes.htm#PRIMARYT) |
| CRDCURRCODE | The 3-digit ISO currency code linked to the card. | 1 | <CRDCURRCODE> | Yes | See [CRDCURRCODE](Sub_Elements_and_Attributes.htm#CRDCURRC) |
| LINKEDTOKEN | If the card is linked to another card with a different account, then this field holds the Thredd public token of the linked card. | 0-1 | <LINKEDTOKEN> | Optional | See [LINKEDTOKEN](Sub_Elements_and_Attributes.htm#LINKEDTO) |
| PRODUCTID | Indicates the ID (unique numeric identifier) of the Thredd product associated with the card. | 1 | xs:string | Yes | See [PRODUCTID](Sub_Elements_and_Attributes.htm#PRODUCTI) |
| LASTUPDATED | Timestamp indicating at what point the reported balance was in effect. This is also the date and time of the last transaction for the current card before the balance report was generated. | 1 | xs:string | Yes | Maximum 14 characters, DateTime in the format:  *YYYYMMDDHHMMSS* |

**Example**

[Copy](javascript:void(0);)

```
<ACCOUNT>  
  â¦detail ommittedâ¦  
  <CARD>  
    <PAN>1234567812345678</PAN>  
    <MASKEDPAN>123456******5678</MASKEDPAN>  
    <VIRTUAL>N</VIRTUAL>  
    <PRIMARY>Y</PRIMARY>  
    <MVC>N</MVC>  
    <CRDPRODUCT>ABCD</CRDPRODUCT>  
    <PROGRAMID>FEDCBA</PROGRAMID>  
    <CUSTCODE></CUSTCODE>  
    <STATCODE>00</STATCODE>  
    <EXPDATE>2022-01-31</EXPDATE>  
    <GPSEXPDATE>2021-01-31</GPSEXPDATE>  
    <CRDACCNO>DEF123</CRDACCNO>  
    <PRIMARYTOKEN>234321042355666</PRIMARYTOKEN>  
    <CRDCURRCODE>GBP</CRDCURRCODE>  
    <LINKEDTOKEN>6543210123456789</LINKEDTOKEN>  
    <PRODUCTID>9001</PRODUCTID>  
    <LASTUPDATED>20190307045701</LASTUPDATED>  
  </CARD>  
  <CARD>  
    <PAN>8765432187654321</PAN>  
    <VIRTUAL>N</VIRTUAL>  
    <PRIMARY>N</PRIMARY>  
    <MVC>Y</MVC>  
    <CRDPRODUCT>ABCD</CRDPRODUCT>  
    <PROGRAMID>FEDCBA</PROGRAMID>  
    <CUSTCODE></CUSTCODE>  
    <STATCODE>00</STATCODE>  
    <EXPDATE>2022-01-15</EXPDATE>  
    <GPSEXPDATE>2021-01-15</GPSEXPDATE>  
    <CRDACCNO>DEF123</CRDACCNO>  
    <PRIMARYTOKEN>234321042355666</PRIMARYTOKEN>  
    <CRDCURRCODE>GBP</CRDCURRCODE>  
    <LINKEDTOKEN>6543210123456789</LINKEDTOKEN>  
    <PRODUCTID>9001</PRODUCTID>  
    <LASTUPDATED>20181012162432</LASTUPDATED>  
  </CARD>  
</ACCOUNT>
```