# String Cleaning and Approved Characters

Thredd cleans any strings before adding to the database, limiting characters to the ASCII range of 33 to 122. This is aimed at stopping any unexpected characters in the core data for Authorisation, Presentments and Transactions, and to ensure data can be reliably used by EHI, Reporting, Smart Client, Thredd Portal and other systems.

These lists are subject to change over time as printing capabilities and customer requirements change. For details, check with your Implementation Manager.

## Characters Removed from Input Fields

The following special characters are removed  from input fields:

| Field | Special Characters that will be removed |
| --- | --- |
| CardName | ;:!?\<>~#%@{}|[]â |
| FirstName | ;:!?\<>~#%@{}|[]â |
| LastName | ;:!?\<>~#%@{}|[]â |
| EmbossLine4 | ;,\:!?<>~`#%^@(){}|â[]â |
| Addrl1 | ;:!?\<>~`#%^@{}|[]â |
| Addrl2 | ;:!?\<>~`#%^@{}|[]â |
| Addrl3 | ;:!?\<>~`#%^@{}|[]â |
| City | ;:!?\<>~`#%^@(){}|&[]â |
| PostCode | ;:!?\<>~`#%^@(){}|&[]â |
| Country | ;:!?\<>~`#%^@(){}|&[]â |
| Delv\_AddrL1 | ;:!?\<>~`#%^@{}|[]â |
| Delv\_AddrL2 | ;:!?\<>~`#%^@{}|[]â |
| Delv\_AddrL3 | ;:!?\<>~`#%^@{}|[]â |
| Delv\_City | ;:!?\<>~`#%^@(){}|&[]â |
| Delv\_County | ;:!?\<>~`#%^@(){}|&[]â |
| Delv\_PostCode | ;:!?\<>~`#%^@(){}|&[]â |
| Delv\_Country | ;:!?\<>~`#%^@(){}|&[]â |
| Delv\_Code | ;:!?\<>~`#%^@(){}|&[]â |
| Fulfil1 | ;,/:!?\<>~`#%^(){}|&â[]â |
| Fulfil2 | ;,/:!?\<>~`#%^(){}|&â[]â |
| ThermalLine1 | ;:!?\<>~`#%^@(){}|&[]â |
| ThermalLine2 | ;:!?\<>~`#%^@{}|&[]â |
| Title | ;:!?\<>~`#%^@(){}|&[]â |
| ImageId | ;:!?\<>~`#%^@(){}|&[]â |
| LogoFrontId | ;:!?\<>~`#%^@(){}|&[]â |
| LogoBackId | ;:!?\<>~`#%^@(){}|&[]â |
| Mobile | ;,:!?\<>~`#%^@-=\*\_$??(){}|&â[]â |
| ExternalRef | ;,.\/:!?<>~`#%^@(){}&â[]â |
| CustAccount | ;,.\/:!?<>~`#%^@(){}&â[]â |
| Email | ;,/:!?\<>~`#%^(){}|&'[]" |
| Url | <>&'" |
| Reason | ;,.\/!?<>~`#%^@(){}|&â[]â |
| Date fields (e.g. DOB, LocDate) | ;,\/:!?<>~`#%^@+\*\_$(){}|&'[]" |
| Other string fields | ;:!?\<>~`#%^@(){}|&[]â |

## Card Manufacturer Approved Characters

When submitting the *CardName* and *EmbossName* parameters (or *FirstName* and *LastName* if *CardName* is empty), note that the card manufacturer only accepts  the following approved characters:

| Manufacturer | Allowed Characters |
| --- | --- |
| ABNote Australasia | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^()+ |
| AB Corp | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^''&amp;\/?'' |
| AB Corp AU | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^''&amp;\/?'' |
| AB CORP NZ | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^''&amp;\/?'' |
| AllPay (ZEBIT) | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/`'()+ |
| ArrowEye | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/&amp;`'()+ |
| Austria Card | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^' |
| Borica | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^' |
| Catalyst | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^'&amp;\/?' |
| CPI | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^`' |
| CPI Card Group Canada | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ÃâÃâ¦Ãâ Ãâ¡Ãâ°ÃâÃâÃÅÃ ÃÂ¡ÃÂ¢ÃÂ¤ÃÂ¥ÃÂ¦ÃÂ§ÃÂ¨ÃÂ©ÃÂªÃÂ«ÃÂ¬ÃÂ­ÃÂ®ÃÂ¯ÃÂ±ÃÂ²ÃÂ³ÃÂ´ÃÂ¶ÃÂ¹ÃÂºÃÂ»ÃÂ¼!@#$%^&amp;\*()\_+-=/\|[]&lt;&gt;?;:'"Ãâ¬ÃÂÃâÃÆÃÂ«ÃËÃÅ Ãâ¹ÃÅÃÂÃÅ½ÃÂÃâÃâÃâÃâ¢Ãâ¢ÃÅ¡ÃâºÃÂ£ÃÂ°ÃÂµÃâ |
| CPI Group (UK) | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789($Â£â¬.,!?) |
| DZ | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^`' |
| DigiSEq | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| EVRY | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ.-^â,&\/?â |
| Exceet | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^&amp;' |
| Futurecard | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^&amp;' |
| GEMALTO | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| GNC | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^+@&amp;-'/ |
| Gemalto AU | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ.-^â,&\/?â |
| Gemalto Brazil | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ.-^â,&\/?â |
| Gemalto Czech Republic | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¡cdÃÂ©ÃÂ«eÃÂ­llnÃÂ¶oÃÂ´rÃÂ¡tÃÂ¼ÃÂºuuÃÂ½ÃÂ¾ÃâÃÂCDÃâ°EÃâ¹ÃÂLLNÃâÃâOÃâRÃ TÃÅÃÅ¡UUÃÂÃÂ½!$%&amp;'-+)(./ |
| Gemalto France | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| Gemalto â DCT | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ.-^ |
| Gemalto Poland | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ-^aAcCeElLnNÃÃ³SsZzZz |
| Gemalto Singapore | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&amp;/-''. |
| GNC | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^+@&amp;-'/ |
| Goldpac | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^'&amp;\/?' |
| GyD | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/&amp;`'()+ |
| GyD UK | ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-. â'' |
| Idemia | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^'+() |
| Incodia International | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^($ÃÂ£Ã¢âÂ¬. |
| Intaremit | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| MTL | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| Morpho Cards | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^' |
| Nagra ID | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/&amp;`''()+ |
| Nitecrest | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-^''''ÃÅ¸Ãâ¬ÃÂÃâÃÆÃâÃâ¦Ãâ Ãâ¡ÃËÃâ°ÃÅ Ãâ¹ÃÅÃÂÃÅ½ÃÂÃâÃâÃâÃâÃâ¢ÃâÃËÃ Ãâ¢ÃÅ¡ÃâºÃÅÃÂ¸ÃÂÃÂ½ÃâÃâ ÃÅÃÅ½ÃËÃÂ¹ÃÂ½ÃÂÃÆÃâ¡ÃÂÃâÃÅ¡ÃËÃÅ¡ÃÂ¤ÃÂ°ÃÂ¹ÃÂ»ÃÂ¤ÃÂ¡cdÃÂ¦ÃÂ©ÃÂ«eÃÂ­llnÃÂ¶oÃÂ¸ÃÂ´rÃÂ¡tÃÂ¼ÃÂºuuÃÂ½ÃÂ¾ÃÂ£ÃÅ½ |
| Oberthur France | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/`''()+ |
| Placard Vault Payments Solution | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789Ã¤Ã¶Ã¼ÃÃÃ.-^ |
| Rosan Finance | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^/&amp;`' |
| TAG Poland | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÄÃ¤Ã¶Ã¼ÃÃÃ.-^âââââ`â |
| TCT (Thames) | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^'/ |
| TOPPAN | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^'&amp;\/?' |
| Thredd | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-^''''ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÅ ÃÃÃÃÅ¸ÃÅ½ÄÄÄÄÄÄ¹Ä½ÅÅÅÅÅÅÈÈÅ¤Å°Å¹Å»Ã¤Ã¡cdÃ¦Ã©Ã«eÃ­llnÃ¶oÃ¸Ã´rÅ¡tÃ¼ÃºuuÃ½Å¾Ã¤Ã¶Ã¼ÃÃÃ.-^â,&\/?â |
| TrueB | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| Verisoft | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^ |
| Virtual Only | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-^''''ÃÅ¸Ãâ¬ÃÂÃâÃÆÃâÃâ¦Ãâ Ãâ¡ÃËÃâ°ÃÅ Ãâ¹ÃÅÃÂÃÅ½ÃÂÃâÃâÃâÃâÃâ¢ÃâÃËÃ Ãâ¢ÃÅ¡ÃâºÃÅÃÂ¸ÃÂÃÂ½ÃâÃâ ÃÅÃÅ½ÃËÃÂ¹ÃÂ½ÃÂÃÆÃâ¡ÃÂÃâÃÅ¡ÃËÃÅ¡ÃÂ¤ÃÂ°ÃÂ¹ÃÂ»ÃÂ¤ÃÂ¡cdÃÂ¦ÃÂ©ÃÂ«eÃÂ­llnÃÂ¶oÃÂ¸ÃÂ´rÃÂ¡tÃÂ¼ÃÂºuuÃÂ½ÃÂ¾ÃÂ¤ÃÂ¶ÃÂ¼ÃâÃâÃÅ.-^Ã¢â¬â¢&amp;\/?Ã¢â¬â¢ |

Please ensure you use the correct unicode characters supported by your card manufacturer. For example, you should use the straight apostrophe (') which is unicode character U+2019. Do not use the smart apostrophe (â) which is unicode character U+0027.

## Unicode Characters

The table below provides details of commonly used unicode characters.

| Character | Unicode value | Character | Unicode value |
| --- | --- | --- | --- |
| ! | U+0021 | Ã | U+00D8 |
| " | U+0022 | Ã | U+00D9 |
| # | U+0023 | Ã | U+00DA |
| $ | U+0024 | Ã | U+00DB |
| % | U+0025 | Ã | U+00DC |
| & | U+0026 | Ã | U+00DC |
| ' | U+0027 | Ã | U+00DF |
| ( | U+0028 | Ã | U+00E0 |
| ) | U+0029 | Ã¡ | U+00E1 |
| \* | U+002A | Ã¢ | U+00E2 |
| + | U+002B | Ã£ | U+00E3 |
| , | U+002C | Ã¤ | U+00E4 |
| - | U+002D | Ã¥ | U+00E5 |
| . | U+002E | Ã¦ | U+00E6 |
| / | U+002F | Ã§ | U+00E7 |
| / | U+002F | Ã¨ | U+00E8 |
| : | U+003A | Ã© | U+00E9 |
| ; | U+003B | Ãª | U+00EA |
| < | U+003C | Ã« | U+00EB |
| = | U+003D | Ã¬ | U+00EC |
| > | U+003E | Ã­ | U+00ED |
| ? | U+003F | Ã® | U+00EE |
| ? | U+003F | Ã± | U+00F1 |
| @ | U+0040 | Ã² | U+00F2 |
| [ | U+005B | Ã³ | U+00F3 |
| \ | U+005C | Ã´ | U+00F4 |
| ] | U+005D | Ãµ | U+00F5 |
| ^ | U+005E | Ã¶ | U+00F6 |
| \_ | U+005F | Ã¹ | U+00F9 |
| c | U+0063 | Ãº | U+00FA |
| d | U+0064 | Ã» | U+00FB |
| e | U+0065 | Ã¼ | U+00FC |
| l | U+006C | Ã½ | U+00FD |
| n | U+006E | Ã¿ | U+00FF |
| r | U+0072 | Ä | U+0103 |
| t | U+0074 | Ä | U+0106 |
| u | U+0075 | Ä | U+010C |
| | | U+007C | Ä | U+010E |
| Â£ | U+00A3 | Ä | U+0118 |
| Â¤ | U+00A4 | Ä¹ | U+0139 |
| Â° | U+00B0 | Ä½ | U+013D |
| Ã | U+00C0 | Å | U+0141 |
| Ã | U+00C1 | Å | U+0143 |
| Ã | U+00C2 | Å | U+0147 |
| Ã | U+00C3 | Å | U+0150 |
| Ã | U+00C4 | Å | U+0154 |
| Ã | U+00C5 | Å | U+015A |
| Ã | U+00C5 | Å | U+0160 |
| Ã | U+00C6 | Å¡ | U+0161 |
| Ã | U+00C7 | Å¤ | U+0164 |
| Ã | U+00C8 | Å° | U+0170 |
| Ã | U+00C9 | Å¹ | U+0179 |
| Ã | U+00CA | Å» | U+017B |
| Ã | U+00CA | Å½ | U+017D |
| Ã | U+00CB | Å¾ | U+017E |
| Ã | U+00CC | È | U+0218 |
| Ã | U+00CD | È | U+021A |
| Ã | U+00CE | â | U+2019 |
| Ã | U+00CF | â | U+201E |
| Ã | U+00D1 | â¬ | U+20AC |
| Ã | U+00D2 | Ã | U+00D6 |
| Ã | U+00D3 | Ã | U+00D8 |
| Ã | U+00D4 | Ã | U+00D9 |
| Ã | U+00D5 | Ã | U+00DA |
| Ã | U+00D6 |  |  |

## Replacement of Diacritic Letters

In addition to restricting the characters allowed, Thredd also automatically replaces common diacritic letters with Latin alphabet letters. This applies only to track data used for the manufacturer files.

| Diacritic Letter | Classic Latin Alphabet Letter |
| --- | --- |
| Ã | A |
| Ã¡ | a |
| Ã | A |
| Ã¤ | a |
| Ã | A |
| Ã | a |
| Ã | A |
| Ã¢ | a |
| Ã | A |
| Ã£ | a |
| Ã | A |
| Ã¥ | a |
| Ã | C |
| Ã§ | c |
| Ã | E |
| Ã© | e |
| Ã | E |
| Ã¨ | e |
| Ã | E |
| Ãª | e |
| Ã | E |
| Ã« | e |
| Ã | I |
| Ã­ | i |
| Ã | I |
| Ã® | i |
| Ã | I |
| Ã¯ | i |
| Ã | I |
| Ã¬ | i |
| Ã | N |
| Ã± | n |
| Ã | O |
| Ã³ | o |
| Ã | O |
| Ã´ | o |
| Ã | O |
| Ã² | o |
| Ã | O |
| Ã¶ | o |
| Ã | O |
| Ãµ | o |
| Ã | U |
| Ãº | u |
| Ã | U |
| Ã» | u |
| Ã | U |
| Ã¼ | u |
| Ã | U |
| Ã¹ | u |
| Å¸ | Y |
| Ã¿ | y |
| Ã | Y |
| Ã½ | y |
| Ã | S |
| Ã | AE |
| Ã¦ | ae |
| Å | OE |
| Å | oe |
| Ä | C |
| Ä | c |
| Ä | D |
| Ä | d |
| Ä | E |
| Ä | e |
| Ä¹ | L |
| Äº | l |
| Ä½ | L |
| Ä¾ | l |
| Å | N |
| Å | n |
| Å | O |
| Å | o |
| Å | R |
| Å | r |
| Å | S |
| Å¡ | s |
| Å¤ | T |
| Å¥ | t |
| Å° | U |
| Å± | u |
| Å® | U |
| Å¯ | u |
| Å½ | Z |
| Å¾ | z |
| Ã | O |
| Ä | A |
| Ä | a |
| Ä | C |
| Ä | c |
| Ä | E |
| Ä | e |
| Å | L |
| Å | l |
| Å | N |
| Å | n |
| Ã | O |
| Ã¸ | o |
| Å | R |
| Å | r |
| Å | S |
| Å | s |
| È | S |
| È | s |
| È | T |
| È | t |
| Å¹ | Z |
| Åº | z |
| Å» | Z |
| Å¼ | z |

## Character Support in Web Services Calls

### Postcode Permitted Characters

You can use the following characters in the `Postcode` field:

* Arabic numerals "0" to "9"
* letters of the ISO basic Latin alphabet (A-Z, a-z)
* spaces
* hyphens(-).

### Card Name Permitted Characters

You can use the following characters in the `CardName` field:

* abcdefghijklmnopqrstuvwxyz
* ABCDEFGHIJKLMNOPQRSTUVWXYZ
* 0123456789
* Some non-english characters i.e. âÃ¤Ã¶Ã¼ÃÃÃâ
* â/â (forward slash)
* â-â (hyphen)
* â^â (caret)
* â.â (full stop)
* â â (space character)
* âââ (apostrophe)

If you are using Thredd as your Card Manufacturer, for example, for Virtual cards where an external card manufacturer is not needed, the the `CardName` field permits the following additional characters in : ^''''ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÅ ÃÃÃÃÅ¸ÃÅ½ÄÄÄÄÄÄ¹Ä½ÅÅÅÅÅÅÈÈÅ¤Å°Å¹Å»Ã¤Ã¡cdÃ¦Ã©Ã«eÃ­llnÃ¶oÃ¸Ã´rÅ¡tÃ¼ÃºuuÃ½Å¾Ã¤Ã¶Ã¼ÃÃÃ.-^â,&\/?â

## Processing of Phone Numbers

Thredd processes phone numbers in web services as follows:

* Allows up to a maximum of 15 digits.
* Deletes all special characters, left and right parenthesis (i.e. brackets), spaces and hyphens â-â.
* Deletes all leading non-numeric characters except â+â. Non-leading non-numeric characters (e.g. â-â) are deleted.
* If the phone number has any letters then the number is rejected.
* Depending on the country, the national (domestic/inter-regional within a country) dialling prefix (e.g. single zero for many countries such as the UK, France, Spain, Australia) is dropped. The "+" and the IDD (International Direct Dialing) number is prefixed. For example:

  + London, UK: 020 7292 2400 is changed to `+442072922400`
  + Lyon, France: 04 72 12 34 56 78 is changed to `+3347212345678`
  + Kuala Lumpur, Malaysia: 03 2123 4567 is changed to `+60321234567`
  + Mobile number, Spain: 0612 345 678 is changed to `+34612345678`
  + Sydney, Australia: 02 7010 1111 is changed to `+61270101111`

  IDD number prefixing is used across all endpoints that handle phone numbers.
* If there is a "+" prefix, Thredd checks if the digits which follow match the IDD number of the specified country. If they don't match, nothing is done. If they do match, Thredd checks if the digits which follow match the national dialling prefix (e.g. single zero for many countries such as UK, France, Spain, Australia). If they do match, the national dialling prefix is dropped. For example:

  + London, UK: +44 020 7292 2400 is changed to `+442072922400`
  + Lyon, France: +33 04 72 12 34 56 78 is changed to `+3347212345678`
  + Kuala Lumpur, Malaysia: +60 03 2123 4567 is changed to `+60321234567`
  + Mobile number, Spain: +34 0612 345 678 is changed to `+34612345678`
  + Sydney, Australia: +61 02 7010 1111 is changed to `+61270101111`
* If there is no leading "+" or national dialling prefix, the phone number is stored as it is.

If invalid values such as alphabetic characters, alphanumeric characters or numbers exceeding 15 digits are provided, the service returns Action Code 439.