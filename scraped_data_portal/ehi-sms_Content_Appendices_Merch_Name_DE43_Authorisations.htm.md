# 4.17 Merch\_Name\_DE43 Field in Authorisations

This section describes the format of the Merchant Name/Location Field (DE43) procided in authorisation messages `Merch_Name_DE43`. (See also `Get Transaction Message fields: Merch_Name_DE43`)

## 4.17.1 Mastercard Authorisation

The merchant name/location field for Mastercard is made up of various subfields.

| Positions | Length | Field Name | Description / Valid Values |
| --- | --- | --- | --- |
| 1-22 | 22 | Card Acceptor Name | Name of Card Acceptor or ATM service provider.  (Space padded on the right to make up to 22 characters.) |
| 23-23 | 1 | Separator | Space character â â |
| 24-36 | 13 | Card Acceptor City | City of the merchant/ATM  (Space padded on the right to make up to 13 characters.) |
| 37-37 | 1 | Separator | Space character â â |
| 38-40 | 3 | State or Country Code | If Card Acceptor is in the USA or Canada, this contains a 2 character US state or Canadian Province code then a space.  Otherwise, this contains a ISO 3-alpha upper case country code. |

#### Examples

Below are examples of the type of data that can arrive in `Merch_Name_DE43` in authorisation messages:

| Authorisation Message Merch\_Name\_DE43 value | Things to note |
| --- | --- |
| PAYPAL \*YIWUYUYICHE    35314369001   GBR | Normal country code |
| ROBLOX CORPORATION     888-858-2569  CA | Last 3 characters are a 2-letter US state code, followed by a space e.g. TX = Texas, NY = New York etc. |
| 3600 LAS VEGAS BLVD SO LAS VEGAS      NV | Last 3 characters are a space, followed by a 2-letter US state code e.g. TX = Texas, NY = New York etc. |
| NOOR DUBAI MALL BRANCH BAI        AE ARE | Emirate within UAE e.g. Dubai/DXB, Abu Dhabi/AUH, Ras Al Khaimah/RAK etc. |
| GOOGLE \*FiLMiC Inc     g.co/payhelp# GBR | URL in city field |
| MICROSOFT   \*XBOX      BILL.XBOX.COM IRL | Website hostname in city field |

## 4.17.2 VISA Authorisation

The merchant name/location field for Visa is made up of various subfields.

| Positions | Length | Field Name | Description / Valid Values |
| --- | --- | --- | --- |
| 1-25 | 25 | Card Acceptor Name | Name of Card Acceptor or ATM service provider.  (Space padded on the right to make up to 25 characters.) |
| 26-38 | 23 | City Name | POS: City where the customer transaction occurs.  Card-Not-Present Transactions: Instead of the city name, these positions must  contain the merchant's customer service telephone number.  ATM: City where the ATM is located. The institution name is in field 42. |
| 39-40 | 2 | Country Code | The 2-character alpha code in uppercase format for the country where the cardholder transaction occurs or the ATM is located. |

## 4.17.3 Mastercard Networks Exchange Authorisation

The merchant name/location field for Mastercard Networks Exchange is made up of various subfields.

| Positions | Length | Field Name | Description / Valid Values |
| --- | --- | --- | --- |
| 1-23 | 23 | Card Acceptor Location Address | Name or address of the card acceptor. For example, 2790 US HIGHWAY 92 E. |
| 24-36 | 12 | Card Acceptor Location City | Name of the city. For example, LAKELAND. |
| 37-38 | 2 | Card Acceptor Location State | Name of the state. For example, FL. |
| 39-40 | 2 | Card Acceptor Location  Country | Name of the country. For example,US. |