# 4.9 CVV2 Indicators

## 4.9.1 CVV2 Presence Type Indicator

If the `CVV2` field has 6 characters, then the first character is the `CVV2 Presence Type indicator`.

This has the following values:

| CVV2 Presence Type indicator | Description | Comment |
| --- | --- | --- |
| 0 | CVV2 value not provided | Nothing to validate. |
| 1 | CVV2 present | CVV2 will be present in positions 4 to 6 inclusive in the âCVV2â field.  If you have chosen to validate CVV2 yourself, then check the CVV2. |
| 2 | CVV2 value on card but not legible | Nothing to validate.  You may want to consider declining the transaction if you expect CVV2 to be present on the card. |
| 3 | Dynamic CVV2 present | You should never receive this (only for issuers that subscribe to CVV2 fallback service from Visa) |
| 9 | No CVV2 value on card | Nothing to validate.  You may want to consider declining the transaction if you expect CVV2 to be present on the card. |

## 4.9.2 CVV2 Response Type Indicator

If the `CVV2` field has 6 characters, then the second character is the `CVV2 Response Type indicator`.

This has the following values:

| CVV2 Response Type indicator | Description | Comment |
| --- | --- | --- |
| 0 | Visa do not expect field 44.9 result of CVV2 validation | Ignore â Thredd will handle this |
| 1 | Visa expect field 44.9 result of CVV2 validation | Ignore â Thredd will handle this |