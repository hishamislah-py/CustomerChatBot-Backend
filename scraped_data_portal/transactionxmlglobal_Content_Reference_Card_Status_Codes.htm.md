# 4.2 Card Status Codes

This section lists the possible card status codes. These are status codes that you can set for card via web services, Smart Client, or Thredd Portal. They are also used to indicate the status of a payment token.

| Status Code | Description |
| --- | --- |
| 00 | All Good. Indicates that the card is good for use, but does not indicate whether it is active. |
| 01 | Refer to card issuer |
| 02 | Card not yet activated |
| 04 | Capture card |
| 05 | Do not honour |
| 14 | Invalid card. If you receive this status, it indicates that this card does not exist on the Thredd system and was used for a fraudulent transaction. |
| 41 | Lost card |
| 43 | Stolen card |
| 46 | Closed Account |
| 54 | Expired card |
| 57 | Transaction not permitted to cardholder |
| 59 | Suspected Fraud |
| 62 | Restricted card |
| 63 | Security violation |
| 70 | Cardholder to contact issuer |
| 75 | Allowable number of PIN tries exceeded |
| 83 | Card destroyed |
| 98 | Refund given to customer |
| 99 | Card voided |
| G1 | A short-term block which temporarily blocks card usage for all card transactions (excluding credits and refunds) for a short period. |
| G2 | Short-term full block (all transactions are blocked). |
| G3 | Long-term block (excluding credits and refunds). |
| G4 | Long-term full block (all transactions are blocked). |
| G5 | Thredd Protect: A short-term block which temporarily blocks card usage for all card transactions (excluding rredits and refunds) for a short period. |
| G6 | Thredd Protect: Short-term full block (all transactions are blocked). |
| G7 | Thredd Protect: Long-term block (excluding credits and refunds). |
| G8 | Thredd Protect: Long-term full block (all transactions are blocked). |
| G9 | IVR Lost/Stolen block. Non-reversable status, equivalent to status code 41. |