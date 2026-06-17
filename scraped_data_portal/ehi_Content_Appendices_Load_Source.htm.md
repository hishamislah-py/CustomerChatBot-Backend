# 4.14 Load Source

The table below lists the valid values for the `LoadSRC` field, identifying the source of a Load. (See also [Get Transaction Message fields: LoadSRC](../Requirements/GetTransaction_Message.htm#LoadSRC))

| ID | Source | Notes |
| --- | --- | --- |
| 1 | POS standard |  |
| 2 | Thredd Kiosk |  |
| 3 | Thredd Website |  |
| 4 | Card Processor |  |
| 5 | Standard Web Service or Cards API |  |
| 6 | Agent |  |
| 7 | Head Office |  |
| 8 | Call Centre |  |
| 9 | Customer Web site |  |
| 10 | Wirecard |  |
| 11 | Customer kiosk |  |
| 12 | Customer mobile app |  |
| 13 | Thredd IVR |  |
| 14 | Unknown |  |
| 16 | Load From Card Request File |  |
| 17 | Corporate |  |
| 18 | epay |  |
| 19 | HOCA Verifiable |  |
| 20 | Post Office |  |
| 21 | HOCA Non Verifiable |  |
| 22 | Paypoint |  |
| 23 | DXB POS Reload |  |
| 24 | TCC Web Report |  |
| 25 | TCC Online |  |
| 26 | VIRGIN POS Reload |  |
| 27 | TCC POS Reload |  |
| 28 | TCC Promotion |  |
| 29 | DXB Zero Load |  |
| 30 | AlFardan Reload |  |
| 31 | UAEx Reload |  |
| 32 | AlAnsari Reload |  |
| 33 | 14 day Cool Off |  |
| 34 | Unload to Repatriate |  |
| 35 | Loan Repayment |  |
| 36 | DXB Online |  |
| 37 | Payzone |  |
| 38 | VIRGIN Zero Load |  |
| 39 | VIRGIN POS standard |  |
| 40 | JADE Web Report |  |
| 41 | JADE POS standard |  |
| 42 | JADE POS Reload |  |
| 43 | JADE Zero Load |  |
| 44 | Wirecard-Cadooz |  |
| 45 | Crunch POS Standard |  |
| 46 | CRUNCH POS Reload |  |
| 47 | Unload Fee Test |  |
| 48 | Balance Transfer Fee Test |  |
| 49 | Sofort Banking |  |
| 50 | Wirecard e-commerce |  |
| 51 | UAExAirport POS Standard |  |
| 52 | UAExAirport Reload |  |
| 53 | Cadooz Load |  |
| 54 | Cadooz Reload |  |
| 55 | Cadooz web unload |  |
| 56 | Sofort Bank Transfer Load |  |
| 57 | Billpay Payment |  |
| 60 | Post Office and Paypoint |  |
| 61 | Credit Limit |  |
| 62 | Credit Card Payment |  |
| 63 | Ukash Payment |  |
| 64 | Bank Transfer | For Bank transfers, the following fields will be present in the request message:  `source_bank_ctry`  `source_bank_account_format`  `source_bank_account`  `dest_bank_ctry`  `dest_bank_account_format`  `dest_bank_account` |
| 65 | Giropay |  |
| 66 | SofortÃ¼berweisung |  |
| 67 | Debit Card |  |
| 68 | Primary Card |  |
| 74 | Master Virtual Card |  |
| 75 | Micropayment |  |
| 76 | MVC Load |  |
| 77 | iMVC Load |  |