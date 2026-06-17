# Appendix 1: Mastercard Cryptogram Version Number Values

## CVN Bit Positions

This table summarises all the CVN bit positions:

| CVN bit position(hex) | Meaning | Value (binary) | Value meaning | Thredd supported? |
| --- | --- | --- | --- | --- |
| 8-5 | Cryptogram Version | 0001 | Fixed for M/Chip 4 and M/Chip Advance | Yes |
| 4-4 | RFU | 0 | Reserved for future use | Yes |
| 3-2 | Session key algorithm | 00 | Mastercard SKD | Yes |
| 10 | EMV CSK | Yes |
| 1-1 | Counters included in AC data? | 0 | No | Yes |
| 1 | Yes | Yes |

## CVN Values

This table summarises the resultant CVN values:

| CVN (hex) | CVN (binary) | CVN (decimal) | Value meaning | Thredd supported? |
| --- | --- | --- | --- | --- |
| â10â | 00010000 | 16 | Mastercard SKD, counters not in AC data | Yes |
| â11â | 00010001 | 17 | Mastercard SKD, counters in AC data | Yes |
| â14â | 00010100 | 20 | EMV CSK, counters not in AC data | Yes |
| â15â | 00010101 | 21 | EMV CSK, counters in AC data | Yes |
| All other values | All other values | All other values | Reserved for Future Use | No |