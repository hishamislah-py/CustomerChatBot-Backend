# Appendix 2 Visa Cryptogram Version Number Values

[VIS] version 1.6 redefined the Cryptogram Version Number to simplify the structure of it, by allocating different information to each nibble, as follows:

* Upper nibble: âWhat is the Format of the Issuer Application Dataâ and Issuer Scripting algorithm
* Lower nibble: âARQC algorithmâ

This table summarises all the CVN values for Visa cards up to and including VIS 1.6, VCPS 2.2 and VCP 1.8.2, showing which ones Thredd supports.  (If a value is used which is not supported, all EMV transactions will be declined.)

| CVN (hex) | CVN (decimal) | 9F10 format | ARQC algorithm | Thredd supported? | Comment |
| --- | --- | --- | --- | --- | --- |
| 0A | 10 | 0/1/3 | âAâ | Yes | Original Visa standard for VIS contact chip transactions |
| 0C | 12 | 0/1/3 | Issuer proprietary | No | Issuer proprietary cryptogram processing |
| 11 | 17 | 0/1/3 | â1â | Yes | Original Visa standard for VIS contactless chip transactions |
| 12 | 18 | 0/1/3 | â2â | Yes | New VIS 1.6 ARQC algorithm |
| 22 | 34 | 2 | â2â | Yes | New VIS 1.6 ARQC algorithm, with new â9F10â format â2â |
| 2C | 44 | 2 | Issuer proprietary | No | Issuer proprietary cryptogram processing, with new â9F10â format â2â |
| 32 to 3B | 50 to 59 | 0/1/3 | Issuer proprietary | No | Issuer proprietary cryptogram processing |
| 43 | 67 | 4 | â3â | No | For Visa Cloud-Based Token Payments  New â9F10â format â4â |
| Other | Other | Undefined | Undefined | No | RFU by Visa |

## Visa Issuer Application Data (tag â9F10â) Formats

[VIS] version 1.6 standardised the â9F10â Issuer Application data formats, which vary depending on the first byte.

See EMV [VIS] version 1.6 appendix F for extra information if needed.

This table summarises the formats, based on the first byte which determines it:

| 9F10 first byte (hex) | 9F10 first byte (decimal) | 9F10 format | Thredd supported? | Comment |
| --- | --- | --- | --- | --- |
| 06 | 6 | 0/1/3 | Yes | Original Visa 9F10 format |
| 1F | 31 | 2 or 4 | Yes | New in VIS 1.6 |
| Other | Other | Unknown | No | Not supported by Thredd |