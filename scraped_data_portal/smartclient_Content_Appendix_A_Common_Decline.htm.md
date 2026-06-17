# Appendix A: Common Decline Reasons

This topic provides details about common card decline reasons.

| Decline | Reason |
| --- | --- |
| DR: Auth Amount     : XX.00 Total                  : XX.00    Available Amount: Y.00       ==>        Decline! | The cardholder does not have sufficient funds to cover the transaction amount. |
| DR: Card expiry check failed with Emboss Expiry date (DE014) | The expiry date entered by the cardholder does not match the expiry date of the card. |
| DR: Exceeds Max Per Transaction limit | The attempted transaction amount exceeded the limit per single transaction amount for the card/product. |
| DR: Incorrect PIN | The cardholder entered an incorrect PIN. |
| DR: Declined due to Lost Card (Capture) (Original auth resp status 41, changed to 05) | The cardâs status was changed to âLost Card (Capture)â and the card can no longer be used. |
| DR: Declined due to CardUsageGroupCheck GroupUsageID-42 [Card Acceptance Method (A) - Card Not Present - E-Commerce - Failed] | The card/product is not permitted to be used for ecommerce transactions. |
| DR: Declined due to CardUsageGroupCheck GroupUsageID-476 [Card Acceptance Method (A) - Chip PAN Entry - Signature Verification - Failed] | The card/product is not permitted to be used for signature verification authorisations. |
| Card CVV2 not matching with cvv2 in auth request | The CVV value entered by the cardholder is not matching the CVV value of the card. |
| DR: Declined due to voided card (Original auth resp status 99, changed to 05) | The status of the card was changed to âCard Voidedâ and the card can no longer be used for authorisations. |
| DR: Declined due to GroupMCCCheck | The card/product is not permitted to use this type of merchant (MCC = Merchant Category Code). |