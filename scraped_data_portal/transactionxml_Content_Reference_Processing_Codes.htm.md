# 4.6 Processing Codes

The Processing code (`ProcCode`) is a 6 digit field made up of:

* 2 characters transaction code. See [[Transaction Codes.](#Transact)](#_Ref443406243)
* 2 characters source account type code. See [[Account Type Codes](#Account)](#_Ref443406386).
* 2 characters destination account type code. See [[Account Type Codes](#Account)](#_Ref443406386).

For transactions initiated via web services or the Cards API, the processing code is formed of:

* 3 digits load source supplied in the request
* 3 digits â999â

## 4.6.1 Transaction Codes

The first two characters of the processing code is the transaction code as follows:

| Value | Description | Impacts Balance |
| --- | --- | --- |
| 00 | Debits (goods and services) | Yes |
| 01 | Debits (for ATM withdrawals, or for cash disbursements using Maestro cards) | Yes |
| 02 | Adjustment Credits | Yes |
| 09 | Debits (goods with cash back) | Yes |
| 10 | Account Funding | Yes |
| 11 | Quasi-Cash (e.g., gambling chips, money order, wire-transfer) | Yes |
| 12 | Debits (for cash advances) | Yes |
| 17 | Debits (for cash advances) | Yes |
| 18 | Unique Transaction (requires unique MCC) | Yes |
| 19 | Debit Adjustments | Yes |
| 20 | Credits (for refund) | Yes |
| 21 | Credits (for deposit) | Yes |
| 22 | Credits (Card Load) | Yes |
| 23 | Debits (Card Unload\_ | Yes |
| 26 | Original Credits | Yes |
| 28 | Credits (for payment transaction) | Yes |
| 30 | Balance inquiry service | No |
| 32 | Visa Tokenisation (Tokenisation Eligibility). Only used by Visa. | No |
| 33 | MDES / Visa Tokenisation (Tokenisation Authorisation) | No |
| 34 | MDES/ Visa Tokenisation (Activation Code Notification) | No |
| 35 | MDES / Visa Tokenisation (Tokenisation Complete Notification) | No |
| 36 | MDES / Visa Tokenisation (Token Event Notification.  See the âMessage\_Sourceâ field for which system originated the Token Event.  See the âMessage\_Whyâ field for the Token Event that occurred. | No |
| 37 | Visa Tokenisation. Get Supported Cardholder Authentication Methods (for Approve with Authentication). Only used by Visa. | No |
| 38 | Visa Tokenisation (Device Binding). Only used by Visa. | No |
| 39 | Indicates an [Account VerificationClosed A type of authorisation transaction which is intended to confirm that the account is genuine and active. Account Verifications are always for a zero amount, so only appear in Authorisation messages and never in clearing messages.](#) transaction. | No |
| 70 | PIN change | No |
| 71 | Card Data File Action (eg new PAN or expdate) | No |
| 72 | PIN unblock | No |
| 91 | PIN unblock | No |
| 92 | PIN change | No |

## 4.6.2 Account Type Codes

The 3rd & 4th digits in Processing code is the Source account type code.

The 5th and 6th digits in Processing code is the Destination account type code.

Both codes are from the following list of account type codes (based on [ISO 8583:2003 Account Type Codes](https://www.iso.org/obp/ui/#iso:std:iso:8583:-1:ed-1:v1:en)).

| Value | Description |
| --- | --- |
| 00 | Default Account (not specified or not applicable) |
| 10 | Savings Account |
| 20 | Cheque Account |
| 30 | Credit Card Account |
| 38 | Credit Line Account |
| 39 | Corporate Account |
| 40 | Universal Account |
| 50 | Money Market Investment Account |
| 58 | IRA Investment Account |
| 60 | Stored Value Account |
| 90 | Revolving Loan Account |
| 91 | Instalment Loan Account |
| 92 | Real Estate Loan Account |