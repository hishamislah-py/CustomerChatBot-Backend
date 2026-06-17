# Appendix B: Card Status Codes

This topic provides details about card status codes.

| Status Code | Description | Who can set? | Functions permitted for the card | Functions blocked for the card | Example of use | Reversible |
| --- | --- | --- | --- | --- | --- | --- |
| 00 | All Good | PM | All | None | Normal operation | YES |
| 04 | Capture Card | PM |  | Auths | Stolen or fraudulent use | YES |
| 05 | Do not honour | PM | Balance Adjustment | Auths | Generally, set by issuer request | YES |
| 41 | Lost card | PM |  | Auths, Activation | Card was lost but not stolen | YES |
| 43 | Stolen card | PM |  | Auths, Activation | Card was stolen | NO |
| 46 | Closed account | PM |  | Auths, Activation | PM closes the account | YES |
| 54 | Expired card | Thredd Only |  | Auths, Activation | Expiry date has passed | YES |
| 57 | Transaction not permitted to cardholder | PM |  | Auths | POS and/or ATM can be prohibited in system settings | YES |
| 59 | Suspected fraud | PM |  | Auths, Activation | Suspected fraudulent use | YES |
| 62 | Restricted card | PM | Balance Adjustment | Load, Auths, Activation | Can be restricted due to rules from the PM or Issuer | YES |
| 63 | Security Violation | PM, Issuers | None | Load, Balance Adjustment, Auths | AML, KYC issue for the cardholder | YES |
| 70 | Cardholder to contact issuer | Issuer | Load, Balance Adjustment | Auths | Set by the issuer for compliance reasons | YES |
| 83 | Card Destroyed | Issuer, PM | NONE 1 | Auths, Activation, Load, Balance Adjustment | Set by PM | NO |
| 98 | Refund given to Customer | PM |  | All (check if it can be loaded) | Gift cards | YES |
| 99 | Card Voided | PM |  | Auths | Account is fine but card voided | YES |
| G1 | Short-term debit block | PM | Credits | Auths (except credits)2 | PM chooses this card status | YES |
| G2 | Short-term full block | PM |  | Auths2 | PM chooses this card status | YES |
| G3 | Long-term debit block | PM | Credits | Auths (except credits)3 | PM chooses this card status | YES |
| G4 | Long-term full block | PM |  | Auths3 | PM chooses this card status | YES |
| G5 | Thredd Protect short-term debit block | Thredd Only | Credits | Auths (except credits)2 | Thredd Protect sets this status based on various criteria | YES |
| G6 | Thredd Protect short-term full block | Thredd Only |  | Auths2 | Thredd Protect sets this status based on various criteria | YES |
| G7 | Thredd Protect long-term debit block | Thredd Only | Credits | Auths (except credits)3 | Thredd Protect sets this status based on various criteria | YES |
| G8 | Thredd Protect long-term full block | Thredd Only |  | Auths3 | Thredd Protect sets this status based on various criteria | YES |
| G9 | Interactive Voice Response (IVR) Lost/Stolen Block (like 41 Lost) | IVR |  | Auths, Activation | Cardholder phoned the IVR automated phone line to block their card | YES |

3.6

1. For card status 83 - Card Destroyed; presentments and refunds, because they are part of the financial record, will continue to process on cards with this status.
2. Merchants told to retry
3. Merchants told not to retry