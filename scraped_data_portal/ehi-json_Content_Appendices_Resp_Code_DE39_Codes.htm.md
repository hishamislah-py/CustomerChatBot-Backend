# 4.30 Resp\_Code\_DE39 Values

This field is provided in Mastercard 0120 (authorisation advice), 0400 (reversal request) and 0420 (reversal advice) messages to indicate the reason for the advice or reversal, which is sent to Thredd by the Card Scheme (Network). For more details, see [Get Transaction Message fields: Resp\_Code\_DE39](../Requirements/GetTransaction_Message.htm#Resp_Code_DE39).

For details of authorisation response status codes that are sent to Thredd through EHI, see [ResponseStatus Values](Response_Code.htm). For card status codes, see [Card Status Codes.](Card_Status_Codes.htm)

| Code | Reason for Advice or Reversal |
| --- | --- |
| 06 | Error. |
| 17 | Customer cancellation. This code is also used for reversals where other reasons in this section do not apply. For example, if doing an EMV contact transaction and the card returns an AAC (decline) after receiving an approve response from the Issuer, this code is used.  This code is also normally used if the terminal decides to reverse a transaction from the Issuer, where the Issuer approved it (but additionally stated that some authentication data such as Address or CVV2 was incorrect.) |
| 32 | Partial reversal. |
| 34 | Suspected fraud. |
| 68 | Response received too late. |
| 82 | Timeout from network to issuer. Visa/Mastercard was unable to send the original 0100 message to Thredd. |

## 4.30.1 Code values that explain the reason for the advice

Below is a list of other codes values in the `Resp_Code_DE39` field which can be used to explain the reason for the advice:

* For an 0120 advice, this indicates the response that was originally sent to the terminal.
* For an 0400 advice or 0420 reversal, this code is what was used in the original 0110 acquirer response, and does not provide information on why the reversal was created.

| Code | Description | Action |
| --- | --- | --- |
| 00 | All good | Approve |
| 01 | Refer to card issuer | Refer |
| 03 | Invalid merchant | Decline |
| 04 | Capture card | Decline and *Pickup* card |
| 05 | Do not honour | Decline |
| 06 | Unspecified error | Decline |
| 08 | Honor with identification | Approve |
| 10 | Partial approval | Approve |
| 12 | Invalid transaction | Decline |
| 13 | Invalid amount | Decline |
| 14 | Invalid card number (no such number) | Decline |
| 15 | Unable to route at IEM (Issuer's Europay Module). Card Scheme network cannot connect to Thredd. | Decline |
| 30 | Format error | Decline |
| 41 | Lost card (Capture) | Decline and *Pickup* card |
| 43 | Stolen card (Capture) | Decline and *Pickup* card |
| 46 | Account closed | Decline |
| 51 | Insufficient funds | Decline |
| 54 | Expired card | Decline |
| 55 | Incorrect PIN | Decline |
| 57 | Transaction not permitted to cardholder | Decline |
| 58 | Transaction not permitted to terminal | Decline |
| 59 | Suspected fraud | Decline |
| 61 | Exceeds withdrawal amount limit. | Decline |
| 62 | Restricted card (e.g. card invalid in region or country) | Decline |
| 63 | Security violation | Decline |
| 65 | Exceeds withdrawal frequency limit | Decline |
| 70 | Cardholder to contact issuer | Decline |
| 71 | PIN not changed | Decline |
| 72 | Account not yet activated | Decline |
| 75 | Allowable number of PIN tries exceeded | Decline |
| 76 | Wrong PIN, allowable number of PIN tries exceeded | Decline |
| 77 | Issuer does not participate in the service | Decline |
| 78 | Card is not active (including created but not yet activated) | Decline |
| 79 | Unacceptable PIN â Transaction declined. Retry. | Decline |
| 81 | Domestic debit transaction not allowed | Decline |
| 85 | Approved (used for some non-financial transactions such as a PIN Unblock request) | Approve |
| 86 | PIN validation not possible | Decline |
| 87 | Purchase amount only. No Cashback allowed. | Approve |
| 88 | Cryptographic failure | Decline |
| 89 | Authentication failure | Decline |
| 91 | Issuer or switch is inoperative | Decline |
| 92 | Unable to Route Transaction (to Issuer or EHI) | Decline |
| 94 | Duplicate transmission | Decline |
| 96 | System malfunction | Decline |
| 1A | SCA required  Thredd internal response code, cannot be used by clients. | Decline |

## 4.30.2 Using the Resp\_Code\_DE39 value in your response to Thredd

When declining a transaction, you must respond with a valid decline reason; we recommend that you use the same response code as received in the `Resp_Code_DE39` field. You should avoid declining with the generic response code *05 - Do not honour*.

The decline reason should be provided in the `ResponseStatus` field of your EHI message response. See [GetTransaction Message Fields](../Requirements/GetTransaction_Message.htm).