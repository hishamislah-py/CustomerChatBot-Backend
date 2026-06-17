# Appendix C: MNE Dispute Processing

In the U.S., Thredd supports dispute processing on co-branded cards (Visa on STAR network). Transactions are processed using the Mastercard Network Exchange (MNE). MNE has similar dispute management stages to those used for Visa and Mastercard networks.

### Raising Disputes

Disputes must be raised in Network Gateway Online Manager (NGOM), which is the User Interface of Mastercard Network Exchange (MNE).

You will need to follow the rules and procedures mandated by MNE and STAR.

Thredd does not provide clients with access to NGOM. To request access, please contact MNE.

### Viewing Disputes

MNE sends a daily XML file to Thredd which contains details of ongoing disputes. Thredd sends you details of disputes via the External Host Interface (EHI) and Transaction XML Reports. You can also view the disputes on the Smart Client Chargeback screen.

### Supported Dispute Types

Thredd processes only the following disputes from MNE:

* Chargebacks
* Chargebacks Reversals
* Representments
* Representment Reversals.

Thredd does not support processing of the following: PreArbitration, Arbitration and Adjustments. Please use Network Gateway Online Manager (NGOM) for managing these disputes types.

## Viewing Disputes on Smart Client

You can view MNE disputes in the Smart Client Chargeback screen. See the example below.

![](Resources/Images/MNE_Chargebacks.png "MNE Chargeback on Smart Client")

Figure 27: Smart Client Chargeback screen showing an MNE Chargeback

## Chargeback Reason Codes

The table below of chargeback reason codes is provided for reference only and details are subject to change. Please refer to the *STAR Network Dispute Guide* and the *STAR Network Exception Processing Rules Guide*. (You can request copies of these documents from Mastercard Network Exchange.)

| Code | Description |
| --- | --- |
| 2000 | Authorisation chargeback: acquirer did not obtain a valid authorisation for the transaction or completed the transaction after receiving a decline response from the issuer. |
| 3000 | Chargeback error |
| 4000 | Cardholder dispute |
| 5000 | Cancellations and Returns Chargeback |
| 6000 | Unauthorised/Fraud Dispute |
| 6500 | Counterfeit chip Card Fraud |

## Representment Reason Codes

The table below is provided for reference only and details are subject to change. This is the acquirer's response to the above chargeback reason codes, when the acquirer wishes to represent (dispute) the chargeback.

Depending on the type of chargeback, the acquirer will also load supporting documentation as evidence. You will need to log in to the MNE Network Gateway Online Manager (NGOM) to view any supporting documentation and respond to the representment.

| Code | Description |
| --- | --- |
| 2002 | Credit Issued |
| 2004 | Invalid Reason Code |
| 2005 | Chargeback Remedy Supplied |
| 2006 | Duplicate Chargeback |
| 3001 | Required Documentation Not Received |
| 3002 | Credit Issued |
| 3003 | Documentation Incomplete or Invalid |
| 3004 | Invalid Reason Code |
| 3005 | Chargeback Remedy Supplied |
| 3006 | Duplicate Chargeback |
| 4001 | Required Documentation Not Received |
| 4002 | Credit Issued |
| 4003 | Documentation Incomplete or Invalid |
| 4004 | Invalid Reason Code |
| 4005 | Chargeback Remedy Supplied |
| 4006 | Duplicate Chargeback |
| 5001 | Required Documentation Not Received |
| 5002 | Credit Issued |
| 5003 | Doc Incomplete or Invalid |
| 5004 | Invalid Reason Code |
| 5005 | Chargeback Remedy Supplied |
| 5006 | Duplicate Chargeback |