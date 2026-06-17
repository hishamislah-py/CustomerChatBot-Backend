# 4.3 FeeClass Element

| Code | Description | Fee Category |
| --- | --- | --- |
| 0 | This value must be used when the FeeClass âtypeâ attribute is 0, 2, 4 or 5. This is when it is a settlement fee. | Settlement Fee |
| 1 | For Card Financial Fee Class element record,  The âcodeâ attribute always has a value of â1â | Settlement Fee |
| 1000 | Cash | Card transaction |
| 1010 | Sale/sale with tip | Card transaction |
| 1020 | Sale with cashback | Card transaction |
| 1030 | Declined transaction | Card transaction |
| 1040 | Other transaction ( e.g. PIN change ) | Card transaction |
| 1060 | Currency exchange mark-up percentage | Card transaction |
| 1061 | Foreign exchange due to markup on network rate | Card transaction |
| 1062 | Currency exchange rate mark-up percentage for authorisation padding | Card transaction |
| 1063 | Currency Conversion Assessment(CCA) | Card transaction |
| 1100 | Retail club out-of-club fee | Card transaction |
| 2010 | Card issue | Card production |
| 2011 | Card reissue (renewal) | Card production |
| 2012 | Damaged card replacement | Card production |
| 2013 | Lost/stolen card replacement | Card production |
| 2014 | Card restriction | Card production |
| 2015 | Changing card limit | Card production |
| 2016 | Authorisation override | Card production |
| 2110 | PIN issue | Card production |
| 2111 | PIN reissue (new PIN) | Card production |
| 2112 | PIN reminder (same PIN) | Card production |
| 2300 | Card value load | Card operation |
| 2301 | Card activation | Card operation |
| 2302 | Status change | Card operation |
| 2303 | Balance enquiry | Card operation |
| 2304 | Account enquiry | Card operation |
| 2306 | Card transfer | Card operation |
| 2307 | Card value unload | Card operation |
| 2308 | Cardholder registration | Card operation |
| 2309 | Card value unload and status change | Card operation |
| 2310 | Cardholder details update | Card operation |
| 2311 | Set PIN real-time | Card operation |
| 2312 | Get PIN real-time | Card operation |
| 2313 | Change PIN real-time | Card operation |
| 2314 | Generate and Get PIN real-time | Card operation |
| 2320 | SMS miscellaneous service fee | Card operation |
| 2401 | Card dormancy | Card management |
| 2402 | Card management | Card management |
| 2441 | Card expiry breakage | Card management |
| 2442 | Card lost/stolen breakage | Card management |
| 2443 | Account end-of-life breakage | Card management |
| 6000 | Non-Domestic Fee | Card transaction |