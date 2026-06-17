# Appendix H: Card Status Codes

This section lists card status changes that trigger calls to theToken Service Provider (MDES/VDEP). For each card status change, the tables below list the corresponding DPAN status and the likely transaction status when the card is used.

For a full list of all card status codes and corresponding response codes, see the [Card Status and Response Codes Guide](https://docs.thredd.com/Card_Status_Response_Codes.htm).

## Web Services (SOAP) Status Codes

The following status codes can be set using the Thredd Web Services API:

| Card status | Description | DPAN Status | Transaction status |
| --- | --- | --- | --- |
| 00 | All good/active | Active | Approve |
| 04 | Capture Card | Deactivated | Decline |
| 05 | Do not honour | Suspended | Decline |
| 41 | Lost card | Suspended | Decline |
| 43 | Stolen card (Capture) | Deactivated | Decline |
| 46 | Closed Account | Deactivated | Decline |
| 57 | Transaction not permitted to cardholder. | Suspended | Decline |
| 59 | Suspected fraud. | Suspended | Decline |
| 62 | Restricted card. | Suspended | Decline |
| 63 | Security violation. | Suspended | Decline |
| 70 | Cardholder to contact issuer. | Suspended | Decline |
| 75 | Allowable Number Of PIN Tries Exceeded | Suspended | Decline |
| 83 | Card Destroyed | Deactivated | Decline |
| 98 | Refund given to customer. | Suspended | Decline |
| 99 | Card Voided | Deactivated | Decline |
| G1 | A short-term[1  Use when you want merchants to try again.  Visa guidelines instruct merchants to attempt up to 15 retries over 30 days. (If you expect the block to last longer than this, long-term may be more appropriate.)](#) block[2  A card block will block all non-credit, Balance enquiry and tokenisation transactions. Refunds and Credits will be permitted.](#) which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. | Suspended | Decline |
| G2 | Short-term full block (all transactions are blocked). | Suspended | Decline |
| G3 | Long-term[3  Use when you donât want merchants to try again.  Visa expect that the card should not return to the '00 Approve' state at all, or at least not within 30 days.](#) block (excluding Credits and Refunds). | Suspended | Decline |
| G4 | Long-term full block (all transactions are blocked). | Suspended | Decline |

For a full list of Card status codes , see the [Web Services Guide > Card Status Codes](https://docs.thredd.com/webservices/Content/Reference/Status_Codes.htm).

## Cards API (REST) Status Codes

The following status codes can be set using the Thredd REST API:

| Card status | Description | DPAN Status | Transaction status |
| --- | --- | --- | --- |
| 00 | All good/active | Active | Approve |
| 04 | Capture Card | Deactivated | Decline |
| 05 | Do not honour | Suspended | Decline |
| 14 | Invalid card | Suspended | Decline |
| 41 | Lost card | Suspended | Decline |
| 43 | Stolen card (Capture) | Deactivated | Decline |
| 46 | Closed account. | Deactivated | Decline |
| 54 | Card Expired | Deactivated | Decline |
| 57 | Transaction not permitted to cardholder. | Suspended | Decline |
| 59 | Suspected fraud. | Suspended | Decline |
| 62 | Restricted card. | Suspended | Decline |
| 63 | Security violation. | Suspended | Decline |
| 70 | Cardholder to contact issuer. | Suspended | Decline |
| 75 | Allowable Number Of PIN Tries Exceeded | Suspended | Decline |
| 83 | Card Destroyed | Deactivated | Decline |
| 98 | Refund given to customer. | Suspended | Decline |
| 99 | Card Voided | Deactivated | Decline |
| G1 | A short-term[4  Use when you want merchants to try again.  Visa guidelines instruct merchants to attempt up to 15 retries over 30 days. (If you expect the block to last longer than this, long-term may be more appropriate.)](#) block[5  A card block will block all non-credit, Balance enquiry and tokenisation transactions. Refunds and Credits will be permitted.](#) which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. | Suspended | Decline |
| G2 | Short-term full block (all transactions are blocked). | Suspended | Decline |
| G3 | Long-term[6  Use when you donât want merchants to try again.  Visa expect that the card should not return to the '00 Approve' state at all, or at least not within 30 days.](#) block (excluding Credits and Refunds). | Suspended | Decline |
| G4 | Long-term full block (all transactions are blocked). | Suspended | Decline |