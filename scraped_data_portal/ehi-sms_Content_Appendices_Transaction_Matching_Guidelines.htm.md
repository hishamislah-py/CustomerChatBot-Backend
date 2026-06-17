# 4.36 Transaction Matching - Authentications and Authorisations

There are a number of the checks you can perform as part of PSD2 Dynamic SCA Linking to verify whether the details provided in the original 3D Secure authentication matches the details that were provided during the transaction authorisation. For example, matching of the authorised amount to the authenticated amount, and matching of the merchant name.

## 4.36.1 Matching the Authorised Amount

From EHI version 5.0 we provide an `AuthenticationAmountUpper` field, which can be used to determine whether the amount authorised in a 3D Secure authentication session matches the amount that was authorised in the authorisation message.

In addition to doing your own checks, you can use the value returned in the [GPS\_POS\_Data field](GPS_POS_Data.htm) position 26 to identify if the authentication amount does not match the authorisation amount.

For Visa, the amount will always be the exact amount, but for Mastercard, if the amount is above 14000 in minor units, the amount may be an estimate, due to their rounding algorithm. See the examples below.

| Currency | Amount | Value in Minor Units | Rounding? |
| --- | --- | --- | --- |
| Japanese Yen (0dp currency | 14000 | <=14000 Yen | No, exact amount |
| Japanese Yen (0dp currency) | 14011 | > 14000 Yen | Yes, Upper bound |
| GBP (2dp currency) | 140 | <= 140.00 Pounds | No, exact amount |
| GBP (2dp currency) | 140.11 | > 140.00 Pounds | Yes, Upper bound |
| Jordanian Dinar (3dp currency) | 14.000 | <= 14.000 Dinar | No, exact amount |
| Jordanian Dinar (3dp currency) | 14.010 | > 14.000 Dinar | Yes, Upper bound |

## 4.36.2 Matching Merchant Name

The merchant name hash is returned in the response to a 3D Secure authentication session. Below are guidelines for how to match the merchant name in the `Merch_Name_DE43` field of the Authorisation message to the merchant name hash returned in the `AuthenticationMerchantHash` field for a 3D Secure authentication.

#### Guidelines

Since the merchant name is provided as a hashed value, you will need to hash the `Merch_Name_DE43` field using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) algorithm and then compare it to the hashed value in the `AuthenticationMerchantHash` field.

* The merchant name field may contain '00000000' or an IP address, depending on your setup at the card scheme. In this case it will not be possible to match.
* For Mastercard, the merchant name that was hashed at authentication time might not match the name provided in the authorisation if the 3D Secure provider and the acquirer were using different naming conventions.
* The merchant name must have the same letters and Case in order for the hash to match. For example, "Microsoft\*Store" and "MICROSOFT\*STORE" will return different hashed values:   
  â¢ "Microsoft\*Store" is hashed as 3a884dcdb1bcea65c907e61d90c1c6cd4b3acf4a1b5696406cfb453743c82ccb.  
  â¢ "MICROSOFT\*STORE" is hashed as 7b7a55d1690a2f6061550fb824322b9d71f7ae0b3e9a7584fad54a970011c544.

See the examples below of common merchant name hashes:

### Mastercard Examples

| Merchant name | Hex of ASCII chars | SHA256 hash |
| --- | --- | --- |
| Microsoft | 4D6963726F736F6674 | C7BAC46904BE785CD0C965BF5659610044F0CDB4CBB02D2EC398DC56648988FD |
| Microsoft\*Store | 4D6963726F736F66742A53746F7265 | 3A884DCDB1BCEA65C907E61D90C1C6CD4B3ACF4A1B5696406CFB453743C82CCB |
| Microsoft\*Xbox | 4D6963726F736F66742A58626F78 | F32B0B5416D7C9C15A653AF18EDD52ABBF88CA2178EA0686C42F98D7F7284159 |
| MICROSOFT\*XBOX | 4D4943524F534F46542A58424F58 | EC4CFC1BBB33769BDD299E0443A652341B84144AE846C566920EED69680524DB |
| PLAYSTATIONNETWORK | 504C415953544154494F4E4E4554574F524B | B50D55B889F8B068EB8144145E2BD007C0C332BEC5284F06C8DC45C6D1AC6FC3 |
| CRV | 435256 | 0107A39935A165F3AB2A3DD226802294E2BD417A0DB8EB6B71A16420DB3FB070 |
| CRV\* | 4352562A | 1B49BAF46A3B718691623FF9E3BC9A70DF0816AB30B9305FE2A95E5EA100C48C |
| Just Eat | 4A75737420456174 | 7FBFB81FC52DFEFEF50ACA038126ABCD46505B3FB5672DAA3E473558E507EB48 |
| PADDLE.NET\* RENDRFORST | 504144444C452E4E45542A2052454E4452464F525354 | B18D1EF6F5A03AD39FBC4E8DBB94BE7A1CD5E098C3120C7CAA926A16589509B0 |
| Nintendo of Europe Gmb | 4E696E74656E646F206F66204575726F706520476D62 | 152FFDEBDC5E99FB2B44E40E02F7B2010E13D43641F7A2706CEB012FD1EA022C |
| Mango.com | 4D616E676F2E636F6D | 937ED44169DB30AAFB3F423FD24954F38BD7B2E69A397F604611240BE2565710 |

### Visa Examples

For Visa, most merchants are using the `Merchant_Name` field in UPPERCASE, after removing non-alphanumeric characters. Some merchants may use a different name to that provided in the `Merchant_Name` field (see the example of PlaystationNetwork/SONY)

| DE43 merchant name (as provided in Merchant\_Name) | AuthenticationMerchantHash | Actual merchant name used to generate the DE126.9 Merchant name hash (found by Thredd by Trial and Error) |
| --- | --- | --- |
| Play Online Solutions | 17722204 | PLAYONLINESOLUTIONS |
| PlaystationNetwork | 24837652 | SONY |
| MICROSOFT\*STORE | 36838472 | MICROSOFT |
| CK Stores B.V. | 31186286 | CKSTORESBV |
| PayU\*Allegro | 93816075 | PAYUALLEGRO |