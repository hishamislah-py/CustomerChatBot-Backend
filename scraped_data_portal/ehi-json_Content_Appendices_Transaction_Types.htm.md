# 4.38 Transaction Types

The table below provides details of available Transaction Type (`Txn_Type`) values. (See also [Get Transaction Message fields: Txn\_Type](../Requirements/GetTransaction_Message.htm#Txn_Type))

| Value | Description | Mapping | Impacts Balance |
| --- | --- | --- | --- |
| A | Authorisation | Authorisation (if MTID=0100)  Financial (if MTID=1240) | Yes (If approved) |
| B | Balance Adjustment | Bal Adjustment/Expiry | Yes |
| C | Chargeback | Financial | Yes |
| D | Auth Reversal | Authorisation | Yes (If matching auth exists) |
| E | Financial Reversal | Financial | Yes |
| G | Payment | Load/Unload | Yes |
| H | Chargeback - Non Credit | Financial | No |
| J | Authorisation Advice | Authorisation | Yes (if approved) |
| K | Chargeback Reversal | Financial | Yes |
| L | Load | Load/Unload | Yes |
| N | Sec Presentment | Financial | Yes |
| P | Presentment | Financial | Yes |
| U | Unload | Load/Unload | Yes |
| Y | Card Expiry | Bal Adjustment/Expiry | Yes |