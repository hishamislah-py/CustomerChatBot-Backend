# 4.2 Card Status Codes

The table below provides details of possible card status codes. These are status values that you can set for a card via Smart Client, Thredd Portal, the Thredd API or the Cards API. For more details, refer to the *Web Services Guide* *SOAP* or the [Cards API](https://cardsapidocs.thredd.com/) website).

| Status Code | Description |
| --- | --- |
| 00 | All Good. Indicates that the card is good for use, but does not indicate whether it is active. |
| 02 | Card not yet activated |
| 04 | Capture card |
| 05 | Do not honour |
| 14 | Invalid card (if you receive this status, it indicates that this card does not exist on the Thredd system and was used for a fraudulent transaction) |
| 41 | Lost card |
| 43 | Stolen card |
| 46 | Closed account |
| 54 | Expired card |
| 57 | Transaction not permitted to cardholder |
| 59 | Suspected fraud |
| 62 | Restricted card |
| 63 | Security violation |
| 70 | Cardholder to contact Issuer (BIN sponsor). |
| 83 | Card destroyed |
| 98 | Refund given to customer |
| 99 | Card voided |
| G1 | A short-term block which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. |
| G2 | Short-term full block (all transactions are blocked). |
| G3 | Long-term block (excluding Credits and Refunds). |
| G4 | Long-term full block (all transactions are blocked). |
| G5 | Thredd Protect: A short-term block which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. |
| G6 | Thredd Protect: Short-term full block (all transactions are blocked). |
| G7 | Thredd Protect: Long-term block (excluding Credits and Refunds). |
| G8 | Thredd Protect: Long-term full block (all transactions are blocked). |
| G9 | IVR Lost/Stolen block. Non-reversable status, equivalent to status code 41. |