# 4.6 Card Status Codes

This section lists the possible card status codes. These are status codes that you can set for card via Thredd API, Thredd Portal or Smart Client. They are also used to indicate the status of a payment token. For details of transaction response codes, see [Response Codes.](Response_Code.htm)

| Status Code | Description |
| --- | --- |
| 00 | All Good. Indicates that the card is good for use, but does not indicate whether it is active. |
| 01 | Refer to card issuer |
| 02 | Card not yet activated |
| 04 | Capture Card |
| 05 | Do not honour |
| 14 | Invalid card (if you receive this status, it indicates that this card does not exist on the Thredd system and was used for a fraudulent transaction) |
| 41 | Lost card |
| 43 | Stolen card |
| 46 | Closed Account |
| 54 | Expired card |
| 59 | Suspected Fraud |
| 62 | Restricted card |
| 63 | Security violation |
| 70 | Cardholder to contact issuer |
| 75 | Allowable number of PIN tries exceeded |
| 83 | Card destroyed |
| 98 | Refund given to customer |
| 99 | Card voided |
| G1 | A short-term block which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. |
| G2 | Short-term full block (all transactions are blocked). |
| G3 | Long-term block (excluding Credits and Refunds). |
| G4 | Long-term full block (all transactions are blocked). |
| G5 | Fraud Transaction Monitoring/Thredd Protect: A short-term block that temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. |
| G6 | Fraud Transaction Monitoring/Thredd Protect: Short-term full block (all transactions are blocked). |
| G7 | Thredd Protect: Long-term block (excluding Credits and Refunds). |
| G8 | Thredd Protect: Long-term full block (all transactions are blocked). |
| G9 | IVR Lost/Stolen block. Non-reversable status, equivalent to status code 41. |

## 4.6.1 Notes on Card Blocks (G1 - G9)

* Short-term blocks result in merchants receiving a message to try again; Visa guidelines instruct merchants to attempt up to 15 retries over 30 days.
* Long-term blocks result in merchants receiving a message not to try again. These are considered as permanent blocks. Visa expect that the card should not return to the '00 Approve' state at all, or at least not within 30 days.