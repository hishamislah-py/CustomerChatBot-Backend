# Status Codes

Refer to the table below for status codes that you can use within the `<NewStatCode>` tag. The codes enable you to set the status of a card using the [Card Change Status](../Web_services_api/Card_Change_Status.htm) (`Ws_Status_Change`) web service, and the Card Unload and Change Status (`Ws_UnLoad_StatusChange`). These statuses are set as **Can be changed** in the table below. Scheme DPAN (Digital PAN) status refers to the corresponding DPAN status in MDES/VDEP when a card is set to the matching Status Code in Thredd's systems. Other statuses can be returned in a response to a card status request.

The service returns an action code of 654 if an attempt is made to change the status of a card with an irreversible status.

The service returns an action code of 825 if an attempt is made to change the status of a card to a non-editable status.

| Status Code | Description | Scheme DPAN Status | Can be changed |
| --- | --- | --- | --- |
| 00 | All Good. Indicates that the card is good for use, but does not indicate whether it is active.  **Tip**: A card must have its `<IsLive>` flag changed to 1 to be considered active. You cannot activate a card by changing its status to 00. To activate a card, use `Ws_Activated`. | Activated / Re-activated | Yes |
| 01 | Refer to card issuer.  Do not use status 01. This is for Thredd use only. | Call Issuer | No |
| 02 | Card not yet activated or card is inactive.  May be used for newly issued cards before activation. | Suspended | No |
| 03 | Invalid merchant. | Suspended | No |
| 04 | Capture Card.  This status is irreversible. | Deactivated / Deleted | No |
| 05 | Do not honour. | Suspended | Yes |
| 06 | Unspecified Error. | Suspended | No |
| 08 | Honour with identification. | Activated | No |
| 10 | Partial Approval. | Activated | No |
| 12 | Invalid Transaction. | Suspended | No |
| 13 | Invalid Amount. | Suspended | No |
| 14 | Invalid card number (no such number).  This status is irreversible. | Suspended | No |
| 15 | No such issuer. | Suspended | No |
| 17 | Customer cancellation. | Suspended | No |
| 1A | Strong Cardholder Authentication (SCA) required. | Suspended | No |
| 30 | Format error. | Suspended | No |
| 31 | Issuer sign-off. | Suspended | No |
| 32 | Completed partially. | Suspended | No |
| 33 | Expired card (Capture). Made non-editable for removing the status from Smart Client.  This status is irreversible. | Deactivated / Delete | No |
| 36 | Restricted card (Capture). Made non-editable for removing the status from Smart Client.  This status is irreversible. | Deactivated / Delete | No |
| 37 | Card acceptor call acquirer security (Capture). Made non-editable for removing the status from Smart Client.  This status is irreversible. | Deactivated / Delete | No |
| 38 | Allowable PIN tries exceeded (Capture).  This status is irreversible. | Deactivated | No |
| 41 | Lost card .  This status is irreversible.  Do not use if temporarily blocking a card or a tokenised digital PAN (DPAN). We recommend you use status code G1 instead. | Suspended | No |
| 43 | Stolen card.  This status is irreversible. | Deactivated / Delete | No |
| 46 | Closed Account.  This status is irreversible. | Deactivated / Delete | No |
| 51 | Insufficient funds. | Suspended | No |
| 54 | Expired card.  Do not use status 54. | Suspended | No |
| 55 | Incorrect PIN. | Suspended | No |
| 58 | Transaction not permitted to terminal. | Suspended | No |
| 59 | Suspected Fraud. | Suspended | Yes |
| 61 | Exceeds withdrawal amount limit. | Suspended | No |
| 62 | Restricted card. | Suspended | Yes |
| 63 | Security violation. | Suspended | Yes |
| 64 | Original amount incorrect. | Suspended | No |
| 65 | Exceeds withdrawal frequency limit. | Suspended | No |
| 66 | Card acceptor call acquirerâs security department. | Suspended | No |
| 67 | Card to be picked up at ATM.  This status is irreversible. | Deactivated / Delete | No |
| 68 | Response received too late. | Suspended | No |
| 69 | Invalid or missing data to verify card, cardholder or other. | Suspended | No |
| 70 | Cardholder to contact issuer. | Suspended | Yes |
| 71 | PIN not changed. | Suspended | No |
| 75 | Allowable number of PIN tries exceeded. | Suspended | Yes |
| 76 | Invalid <To> Account in Field 3. | Suspended | No |
| 77 | Invalid <From> Account in Field 3. | Suspended | No |
| 78 | Card not activated yet. | Suspended | No |
| 79 | Unacceptable PIN â Transaction declined Retry. | Suspended | No |
| 80 | Network error. | Suspended | No |
| 81 | Foreign network failure. | Suspended | No |
| 82 | Timeout at IEM. | Suspended | No |
| 83 | Card destroyed  This status is irreversible. | Deactivated / Delete | No |
| 85 | Approved (special). | Activated | No |
| 86 | PIN validation not possible. | Suspended | No |
| 87 | Purchase Amount Only, No Cash Back Allowed. | Suspended | No |
| 88 | Cryptographic failure. | Suspended | No |
| 89 | Unacceptable PIN. | Suspended | No |
| 90 | Invalid ARQC/CVV1/CVV2/CVV3/iCVV. | Suspended | No |
| 91 | Issuer or switch is inoperative. | Suspended | No |
| 92 | Unable to route. | Suspended | No |
| 93 | Violation of Law. | Suspended | No |
| 94 | Duplicate transmission. | Suspended | No |
| 95 | Reconcile error. | Suspended | No |
| 96 | System malfunction. | Suspended | No |
| 98 | Refund given to customer.  This status is irreversible. | Suspended | No |
| 99 | Card voided.  This status is irreversible. | Deactivated / Delete | No |
| C0 | Requires SCA, Card. | Suspended | No |
| C1 | Requires SCA, non-card. | Suspended | No |
| G1 | A short-term block which temporarily blocks card usage for all card transactions (excluding Credits and Refunds) for a short period. | Suspended | Yes |
| G2 | Short-term full block (all transactions are blocked). | Suspended | Yes |
| G3 | Long-term block (excluding Credits and Refunds). | Suspended | Yes |
| G4 | Long-term full block (all transactions are blocked). | Suspended | Yes |
| G5 | Thredd Protect Short-term Debit Block. | Suspended | Yes |
| G6 | Thredd Protect Short-term Full Block. | Suspended | Yes |
| G7 | Thredd Protect Long-term Debit Block. | Suspended | Yes |
| G8 | Thredd Protect Long-term Full Block. | Suspended | Yes |
| G9 | IVR Lost/Stolen Block (like 41 Lost).  This status is irreversible. | Deactivated / Delete | No |
| N0 | Force STIP. | Suspended | No |
| N7 | Decline for CVV2 failure. | Suspended | No |
| P5 | PIN Change/Unblock request declined. | Suspended | No |
| P6 | Unsafe PIN. | Suspended | No |
| 5C | Transaction not supported/blocked by issuer. | Live - status can be changed. | Yes |
| 9G | Blocked by cardholder/contact cardholder. | Live - status can be changed. | Yes |

#### Notes

* Status codes 04, 14, 33, 36, 37, 38, 41, 43, 46, 67, 83, 98, 99, and G9 are irreversible. You should only use these statuses if you intend to set a permanent block on the card. All other status codes are reversible.  
  For more information on how to manage cards reported as lost, stolen or destroyed (irreversible status's), see [Use Case Scenarios: Updating a Card Status to Lost, Stolen or Destroyed](../Getting_started/User_Scenarios.htm#Updating).
* Do not use status 01 (refer to Card Issuer or 54 (expired card) as these are for Thredd use only.
* Changing the status to 99 (card voided) or 98 (refund to customer) automatically generates a card balance adjustment down to 0.00.
* You should use the following status codes for blocks:

  + Temporary Block: G1 or G2.

    Use when you want merchants to try again. Visa guidelines instruct merchants to attempt up to 15 retries over 30 days. A card block takes place for all non-credit, Balance enquiry and tokenisation (digital wallet) transactions. Refunds and Credits are permitted.
  + Permanent Block: G3 or G4. Use when you donât want merchants to try again. Visa expect that the card should not return to the '00 Approve' state at all, or at least not within 30 days.