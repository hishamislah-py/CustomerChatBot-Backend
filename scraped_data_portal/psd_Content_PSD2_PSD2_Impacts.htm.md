# Impact of the PSD2 Rules

For card products that are enabled for PSD2 checking, the table below describes the impact on transactions if the PSD2 rules apply.

The rows highlighted below indicate the types of transactions where you should expect to see declines.

| Card Data Input Method | Cardholder Verification Method | Impact on card approvals and declines if the PSD2 rules apply |
| --- | --- | --- |
| PAN Key Entry (with cardholder present at merchant) \* | Any | Nearly all transactions will be declined, as few exemptions apply. |
| Mail Order / Telephone order / Recurring | Any or none | PSD2 rules do not apply: transactions should be approved (provided there are no other reasons to decline). |
| Magnetic Stripe \* | Any | Nearly all transactions will be declined, as few exemptions apply. |
| EMV contactless | No verification | Transactions will only be approved if an exemption applies.  For example: low value contactless exemption. To reset the low value contactless counters, an EMV contact + PIN transaction is required. |
| EMV contact \*\* | None or signature | Nearly all transactions will be declined, as few exemptions apply. |
| EMV contact | PIN | Will always pass SCA checks, therefore will not be declined due to PSD2 rules. |
| e-commerce (including Credential-on-file) | None | Transactions will be approved, but only up to the configured e-commerce limits. A 3D-secure transaction is required to reset the counters. |

\* PAN Key Entry and Magnetic Stripe methods do not pass the possession test, which normally means the transaction cannot be SCA.  
\*\* EMV contact with âNoneâ or âsignatureâ cardholder verification methods does not pass the Knowledge test, which normally means the transaction cannot be SCA.

## Dealing with a Decline

What happens when there is a soft decline depends on the reason for the decline. For example:

| Reason for decline | Actions you can take |
| --- | --- |
| PAN Key Entry (with cardholder present at merchant) | Raise with your Card Scheme or the Merchant to double-check whether the cardholder was actually present. If not, then the acquirer should update how they flag the transaction. The cardholder would then need to try again.    Advise the cardholder/merchant to repeat the transaction using Chip and PIN. |
| Magnetic Stripe | Advise the cardholder/merchant to repeat the transaction using Chip and PIN or Contactless. |
| EMV contact with none or signature cardholder verification | Advise the cardholder/merchant to repeat the transaction using Chip and PIN or Contactless. |
| EMV contactless with no cardholder verification | Advise the cardholder/merchant to repeat the transaction using Chip and PIN.  Alternatively, if the Program Manager has verified that the real cardholder is still in possession of the card and this transaction is within the Contactless single value limit, then they can use the [Clear Accumulator](https://docs.thredd.ai/webservices/Content/Web_services_api/Clear_Accumulator.htm) (`Ws_ResetAccumulator`) web service call to reset the Contactless counters for the card. |
| E-commerce where the Merchant did not do 3D Secure | If the Program Manager has verified that the real cardholder is attempting the transaction, and this transaction is within the e-commerce single value limit, then they can use the [Clear Accumulator](https://docs.thredd.ai/webservices/Content/Web_services_api/Clear_Accumulator.htm) (`Ws_ResetAccumulator`) web service call to reset the e-commerce counters for the card. The cardholder would then need to try again. |

For more information on soft declines, see [Soft Declines](Soft_Declines.htm).