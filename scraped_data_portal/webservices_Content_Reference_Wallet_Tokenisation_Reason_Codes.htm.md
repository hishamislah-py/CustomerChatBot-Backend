# Wallet Tokenisation Reason Codes

The wallet service provider tokenisation reason codes are a string of 24 ASCII characters which are '0' or '1':

* 0 = this reason is not set
* 1 = reason set

The first reason is in the last character, the second reason in the second last character, and so on. For example, if reasons 1, 5 and 16 were set, then `wallet_reasons` would be the string "*000000001000000000010001*".

#### Wallet\_Reasons

Refer to the table below for a list of reason codes.

| Reason | Offset in wallet\_reasons | Meaning (common for all wallets) | Apple Pay Description |
| --- | --- | --- | --- |
| 1 | 24 | Account too new since launch | Apple ID was created 40 days or less prior to launch. |
| 2 | 23 | Account too new | Apple ID was created 40 days or less prior to provisioning request. |
| 3 | 22 | Account Card too new | Apple ID / card pair is less than 20 days old. |
| 4 | 21 | Account Data recently changed | Changes have been made to the account settings for the Apple ID in the last 20 days. |
| 5 | 20 | Suspicious activity | Suspicious transactions linked to this account. |
| 6 | 19 | Inactive account | The account has not had activity in the last year. |
| 7 | 18 | Device has suspended tokens | Suspended cards in the secure element |
| 8 | 17 | Device recently lost | The phone was put in lost mode in the last 7 days for longer than the duration threshold (1 hour). |
| 9 | 16 | Too many recent attempts to digitise a payment token | The number of provisioning attempts for this card on this device in 72 hours exceeds the threshold (3 attempts). |
| 10 | 15 | Digitisations too frequent | There have been more than the threshold number of different cards attempted at provisioning to this phone in 24 hours (5 different cards). |
| 11 | 14 | Too many different cardholders | The card provisioning request contains a distinct name in excess of the permitted threshold (2 distinct names). |
| 12 | 13 | Low device score | Device score is less than 3. |
| 13 | 12 | Low account score | Account score is less than 4. |
| 14 | 11 | Digitisation attempted outside home territory or country | Device provisioning location outside of device region. |
| 15 | 10 | Recommendation system inoperative | Model rules not available at this time (in cases where back end systems time out). |
| 16 | 9 | High risk detected | Apple algorithm identified high fraud risk, enhanced verification recommended. |
| 17 | 8 | ? | Phone number score is less than 3. |
| 18 | 7 | RFU | Reserved for Future Use |
| 19 | 6 | RFU | Reserved for Future Use |
| 20 | 5 | RFU | Reserved for Future Use |
| 21 | 4 | RFU | Reserved for Future Use |
| 22 | 3 | RFU | Reserved for Future Use |
| 23 | 2 | RFU | Reserved for Future Use |
| 24 | 1 | RFU | Reserved for Future Use |