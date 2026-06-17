# Appendix D: Visa Tokenisation Messages

The scenarios below describe how you can determine the end of the tokenisation flow on Visa.

When you get a message with payment token status of A, this means the token is active and ready to do transactions and should be the last message in the flow.

#### Scenario 1: Online Merchant Token Request â Green flow

Look for this information in the following EHI fields to identify the message flow and when you need to send a notification to your cardholder of successful provisioning.

| Message Order | PaymentToken \_Type | ProcCode | Resp\_Code \_DE39 | PaymentToken \_creatorStatus | Message \_Why | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | BW or CF | 330000 (TAR) | 00 | (omitted) | 71 | Approve |
| 2 | BW or CF | 360000 (TEN) | 00 | A | 71 | Indicates end of Green flow. Do not notify cardholder[1  These are used by e-commerce merchants who tokenise PANs for storage (e.g. Netflix) and the cardholder is not necessarily present so would be confused by a message confirming tokenisation and likely to consider it fraudulent.](#). |

#### Scenario 2: Mobile Wallet Token Requests with Green flow

For a mobile wallet: Look for this information in the following EHI fields to identify the message flow and what you need to do.

| Message Order | PaymentToken \_Type | ProcCode | Resp\_Code \_DE39 | PaymentToken \_creatorStatus | Message \_Why | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SE or CL | 330000 (TAR) | 00 | (omitted) | 71 | Approve |
| 2 | SE or CL | 360000 (TEN) | 00 | A | 71 |  |
| 3 | SE or CL | 350000 (TCN) | 00 | A | 72 | Last message in flow. Cardholder notification of successful provisioning can be sent here. |

#### Scenario 3: Mobile Wallet Token Requests Yellow flow with successful authentication

| Message Order | PaymentToken \_Type | ProcCode | Resp\_Code \_DE39 | PaymentToken \_creatorStatus | Message \_Why | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SE or CL | 330000 (TAR) | 85 | (omitted) | 71 | Approve with authentication |
| 2 | SE or CL | 360000 (TEN) | 00 | I | 71 | Token Event Notification |
| 3 | SE or CL | 340000  (ACN) | 00 | I | 0 | Activation Code Network Message. Contains the OTP to verify the cardholder. |
| 4 | SE or CL | 350000 (TCN) | 00 | I | 72 | In yellow flow â do not send messages using the TCN. |
| 5 | SE or CL | 360000 (TEN) | 00 | A | 73/74/75 | Last message in flow. Cardholder notification of successful provisioning can be sent here. |

#### Scenario 4: Mobile Wallet Token Requests with Yellow flow with unsuccessful authentication

| Message Order | PaymentToken \_Type | ProcCode | Resp\_Code \_DE39 | PaymentToken \_creatorStatus | Message \_Why | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SE or CL | 330000 (TAR) | 85 | (omitted) | 71 | Approve with authentication |
| 2 | SE or CL | 360000 (TEN) | 00 | I | 71 | Token Event Notification |
| 3 | SE or CL | 340000  (ACN) | 00 | I | 0 | Activation Code Network Message. Contains the OTP to verify the cardholder. |
| 4 | SE or CL | 350000 (TCN) | 00 | I | 72 | In yellow flow â do not send messages using the TCN. |
| 5 | SE or CL | 360000 (TEN) | 00 or 06 | I | 53/54/55 | Last message in flow. No notification of tokenisation completion as authentication was unsuccessful. |