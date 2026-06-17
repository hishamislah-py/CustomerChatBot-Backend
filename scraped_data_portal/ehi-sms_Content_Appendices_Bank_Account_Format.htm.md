# 4.4 Bank Account Formats

This section describes the valid values for the `source_bank_account_format` and `dest_bank_account_format` fields. (See also `Get Transaction Message fields: source_bank_account_format` and [dest\_bank\_account\_format](../Requirements/GetTransaction_Message.htm#dest_bank_account_format))

| Value | Description | Examples |
| --- | --- | --- |
| IBAN | International Bank Account Number.  **Note**: must not contain spaces. | GR1601101250000000012300695  GB29NWBK60161331926819 |
| GBR | 6 digit sort code  1 space character  8 digit account number | 601613 31926819 |

Thredd plan to use the ISO 3-alpha country code in uppercase for the âvalueâ to identify bank account number formats which are specific to that country.