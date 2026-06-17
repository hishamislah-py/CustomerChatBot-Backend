# 4.27 Processing Codes

The Processing code (`Proc_Code`) is a 6 digit field made up of:

* 2 characters transaction code. See [Transaction Codes.](#Transact)
* 2 characters source account type code. See [Account Type Codes](#Account).
* 2 characters destination account type code. See [Account Type Codes](#Account).

For transactions initiated via web services or the Cards API, the processing code is formed of:

* 3 digits load source supplied in the request
* 3 digits â999â

## 4.27.1 Transaction Codes

The first two characters of the processing code is the transaction code, as follows:

| Value | Description | Impacts Balance |
| --- | --- | --- |
| 00 | Debits (goods and services) | Yes |
| 01 | Debits for ATM cash withdrawals (on Visa and Mastercard networks)  May also be used for manual [cash disbursementsClosed Type of transaction where cash is given to the cardholder, for example, from a bank branch by a member of staff using a Point of Sale (POS) terminal.](#) as follows:  â¢ Mastercard *Authorisation* transactions on Maestro cards only â¢ Visa *Authorisation* and *Clearing* transactions on Visa cards | Yes |
| 02 | Adjustment Credits  Indicates a Credit adjustment. | Yes |
| 09 | Debits (goods with cash back) | Yes |
| 10 | Account Funding | Yes |
| 11 | Quasi-Cash  Visa-specific quasi-cash transaction. This is used for specific merchants where the purchased items could be converted to cash (e.g., gaming chips, money orders, wire-transfer). | Yes |
| 12 | Debits (for manual cash disbursements).  Type of transaction where cash is given to the cardholder, for example, from a bank branch by a member of staff using a Point of Sale (POS) terminal.  **Note**: Used for *Clearing* transactions on Mastercard Credit, Cirrus, Maestro and Mastercard Debit. | Yes |
| 17 | Debits (for manual cash disbursements).  Type of transaction where cash is given to the cardholder, for example, from a bank branch by a member of staff using a Point of Sale (POS) terminal.  **Note**: Used for *Authorisation* transactions on Mastercard Credit, Cirrus and Mastercard Debit. | Yes |
| 18 | Unique Transaction (requires unique MCC)  Mastercard-specific transaction category. Similar to Visa's quasi-cash, this is used for specific merchants where the purchased items could be converted to cash (e.g., gaming chips, money orders). | Yes |
| 19 | Debit Adjustments  May be received for non-card money transfers (out), manual or one-off balance adjustments or additional fees. | Yes |
| 20 | Credits (for refund) / Credit voucher or merchandise return authorisation | Yes |
| 21 | Credits (for deposit) | Yes |
| 22 | Credits - Card Load | Yes |
| 23 | Debits - Card Unload | Yes |
| 26 | Original Credits  Visa-specific Money Send transaction. Also called an Original Credit Transaction (OCT). | Yes |
| 28 | Credits (for Payment Transaction)  Mastercard-specific Money Send transaction. | Yes |
| 30 | Balance inquiry service (supported by both Visa and Mastercard) | No |
| 32 | Visa Tokenisation - Tokenisation Eligibility. Only used by Visa. | No |
| 33 | MDES / Visa Tokenisation â Tokenisation Authorisation | No |
| 34 | MDES/ Visa Tokenisation â Activation Code Notification | No |
| 35 | MDES / Visa Tokenisation â Tokenisation Complete Notification | No |
| 36 | MDES / Visa Tokenisation â Token Event Notification.  See the âMessage\_Sourceâ field for which system originated the Token Event.  See the âMessage\_Whyâ field for what sort of Token Event occurred. | No |
| 37 | Visa Tokenisation - Get Supported Cardholder Authentication Methods (for Approve with Authentication). Only used by Visa. | No |
| 38 | Visa Tokenisation - Device Binding. Only used by Visa. | No |
| 39 | Indicates an [Account VerificationClosed A type of authorisation transaction which is intended to confirm that the account is genuine and active. Account Verifications are always for a zero amount, so only appear in Authorisation messages and never in clearing messages.](#) transaction (eligibility inquiry) for a Debit Account Status Inquiry (ASI). A Debit ASI is a Visa service that checks if an amount can be debited from an account, Thredd uses this code for mapping from a debit transaction (authorisation code 00). | No |
| 70 | PIN change (Visa only) | No |
| 71 | Card Data File Action (e.g., new PAN or `expdate`) | No |
| 72 | PIN unblock (Visa only) | No |
| 89 | A Credit ASI that checks if an account is open and able to receive funds for a credit transaction. | No |
| 91 | PIN unblock (Mastercard only) | No |
| 92 | PIN change (Mastercard only) | No |

## 4.27.2 Account Type Codes

The 3rd & 4th digits in Processing code is the Source account type code.

The 5th and 6th digits in Processing code is the Destination account type code.

Both codes are from the following list of account type codes (based on [ISO 8583:2003 Account Type Codes](https://www.iso.org/obp/ui/#iso:std:iso:8583:-1:ed-1:v1:en)).

| Value | Description |
| --- | --- |
| 00 | Default Account (not specified or not applicable) |
| 10 | Savings Account |
| 20 | Cheque Account |
| 30 | Credit Card Account |
| 35 | Deferred debit account |
| 36 | Charge account |
| 38 | Credit Line Account |
| 39 | Corporate Account |
| 40 | Universal Account |
| 50 | Money Market Investment Account |
| 58 | IRA Investment Account |
| 60 | Prepaid or Stored Value Account |
| 90 | Revolving Loan Account |
| 91 | Instalment Loan Account |
| 92 | Real Estate Loan Account |