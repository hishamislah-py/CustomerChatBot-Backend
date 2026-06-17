# 3.4 The Payment Lifecycle

## 3.4.1 Regional Variations

Depending on the region in which your card program operates, the payment transaction message cycle may differ. There are two main types of messaging standards or systems, referred to as Dual Message System and Single Message System:

* **Dual Message System** â follows a payment messaging standard which provides separate messages for the authorisation and clearing (presentment) stages. It is the prominent method in Europe and also used in other regions.
* **Single Message System** â is a transaction processing message standard which combines authorisation and presentment in a single message. It is more common in regions such as the US and Asia Pacific and within those regions, for certain types of transactions, such as those where payment is captured at the same time as authorisation.

For more information, see [Dual vs Single Message Systems](https://docs.thredd.ai/More_Information/Dual_vs_Single_Message.htm).

In this guide, we will be referring to messages processed using the Dual Message System.

## 3.4.2 Basic Transaction Flow (Dual Message)

A single card payment request may consist of multiple transactions that relate to the same payment request. For example:

|  | Message Type | From | MTID | Description |
| --- | --- | --- | --- | --- |
| 1 | Authorisation request | Acquirer | 0100 | A message from the acquirer to approve or decline a payment. |
| 2 | Authorisation response | Issuer | 0110 | A message response from the issuer of approve or decline. |
| 3 | Financial notification (presentment) | Acquirer | 1240 | A message from the acquirer to indicate that an authorised payment has been taken. This will only be sent if the authorisation response was approve. |

See the figure below.

![](../Resources/Images/Intro_card_payments/Payment_Lifecycle.png)

Figure 12: Multiple Transactions in a Cards Payment

The above is a simplified example. During the life cycle of a typical payment there are many other types of transaction messages that may be generated and sent over a card payment network.  Letâs take a look at some common examples.

In these examples, we have simplified the message flow to show only the interaction between the acquirer and the issuer.

If you are using Thredd, then Thredd acts as the [issuer-processor![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Third party agent certified by the card scheme to accept and process card network transactions on behalf of the issuer.](#), receiving messages from the card scheme. Thredd provides initial card checks and processing and can either authorise the transaction or forward to the program managerâs systems for approval. The program manager can either maintain the card balance or Thredd can maintain this.

In the examples below, where we mention issuer, in practise this will be either Thredd or the program manager.

## 3.4.3 Example 1: Purchasing in store followed by a refund

In this example, a customer purchases an item in store and later on requests a refund.

### Message Flow

|  | Message Type | From | MTID | Proc Code[1  First two digits only of the processing code. 00 = purchase; 20 = refund.](#) | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | Authorisation request | Acquirer | 0100 | 00 | A message from the acquirer to approve or decline a payment. |
| 2 | Authorisation response | Issuer | 0110 | 00 | A message response from the issuer of approve or decline. |
| 3 | Financial presentment | Acquirer | 1240 | 00 | A message from the acquirer to indicate that an authorised payment has been taken. |
| 4 | Authorisation request | Acquirer | 0100 | 20 | A message from the acquirer to approve or decline a payment refund. This may be for the full amount or a partial amount. |
| 5 | Authorisation response | Issuer | 0110 | 20 | A message from the issuer of approve or decline. |
| 6 | Financial presentment | Acquirer | 1240 | 20 | A message from the acquirer to indicate that the refund has been processed. |

### Transaction Flow

A cardholder purchases an item in store and the merchant submits a payment authorisation request. The message flow between acquirer and issuer is as follows:

1. The acquirer sends an initial payment authorisation request (0100 authorisation request message) through the card scheme network to the issuer to authorise (approve or decline) the payment. This authorisation request message is processed in real-time (within milliseconds).
2. The issuer sends a response (0110 message) to the acquirer to approve the transaction (the issuer checks the available balance on the card and can either approve, decline or provide a partial amount approval; this response must be processed in real-time). The issuer blocks any approved funds on the card, so that the amount cannot be used for other transactions.
3. On the same day, the acquirer sends a financial message (1240 message) to indicate that an authorised payment has been processed.

   The issuer receives this as part of the schemeâs daily clearing files. The issuer can now deduct the funds from the card.
4. A few days later, the cardholder returns the purchased item to the merchantâs store and requests a refund. The acquirer sends an 0100 authorisation request message for a refund to the issuer.
5. The issuer sends a response (0110 authorisation response message).
6. On the same day the acquirer sends a financial message (1240 message) to indicate that the refund has been processed.

   The issuer adds the refunded amount back on to the cardâs available balance.

## 3.4.4 Example 2: Booking hotel accommodation

In this example, a hotel sends an Account Status Inquiry, which has a billing amount of zero, to check the status of the card. This is followed by an authorisation request for the full amount.

### Message Flow

|  | Message Type | From | MTID | Proc Code | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | Account Status Inquiry | Acquirer | 0100 | 00 | A message from the acquirer to check the status of the card. (The hotel does not know the final amount at this stage.) |
| 2 | Authorisation response | Issuer | 0110 | 00 | A message response from the issuer of approve or decline. |
| 3 | Authorisation request | Acquirer | 0100 | 00 | An authorisation request from the acquirer to approve or decline the full payment amount. |
| 4 | Authorisation response | Issuer | 0110 | 00 | A message response from the issuer of approve or decline. |
| 5 | Financial presentment | Acquirer | 1240 | 00 | A message from the acquirer to indicate that the full payment has been taken, |

### Transaction Flow

A cardholder books a hotel on a hotel booking website and the merchant website submits a payment authorisation request to check that the card is valid.

1. The acquirer sends an Account Status Inquiry, which has amount of zero, to check the status of the card.
2. The issuer sends a response (0110 message) to approve the transaction.
3. The hotel requests an authorisation for the full amount, after calculating costs for all hotel services used.
4. The issuer sends a response (0110 message) to approve the transaction.   
   The issuer updates the cardâs available balance.
5. The acquirer sends a message (1240 message) to the issuer to indicate that an authorised payment has been processed. This message is received as part of the daily clearing files.

## 3.4.5 Example 3: Low value card chip payment in a shop (offline authorisation)

In offline authorisation, the card terminal verifies the card chip and the chip card approves the transaction, with no [online authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An authorisation message that requires real-time and immediate processing via the card payment network and an immediate response from the issuer.](#).

### Message Flow

|  | Message Type | From | MTID | Proc Code | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | Financial presentment | Acquirer | 1240 | 00 | A message from the acquirer to indicate that an authorised payment has been taken. |

### Transaction Flow

A cardholder makes a purchase in a shop using their card which authorises the purchase offline. At the end of the day, the acquirer sends a financial notification for the final amount. There will not be a matching authorisation.

The issuer must update the cardâs available balance.

The program manager can configure their card chips to permit or disallow offline transactions.

## 3.4.6 Example 4: Purchasing Petrol at an Automated Fuel Dispenser

Generally, Automated Fuel Dispenser (AFD) messages are received with an initial amount. The acquirer then sends a second authorisation advice message as an advice, which contains the exact transaction amount.

### Message Flow

|  | Message Type | From | MTID | Proc Code | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | Authorisation request | Acquirer | 0100 | 00 | A message from the acquirer to approve or decline a payment. (The final amount is unknown, so either a nominal one unit of currency or a maximum amount may be specified, depending on the scheme rules for the region.) |
| 2 | Authorisation response | Issuer | 0110 | 00 | A message from the issuer of approve or decline. |
| 3 | Authorisation advice | Acquirer | 0120 | 00 | A message from the acquirer to notify the issuer of the final billing amount. |
| 4 | Authorisation response | Issuer | 0130 | 00 | A message from the issuer. |
| 5 | Financial presentment | Acquirer | 1240 | 00 | A message from the acquirer to indicate that an authorised payment has been taken. |

### Transaction Flow

1. The acquirer sends an initial payment authorisation request (100 message).
2. The issuer responds with approve or decline (0110 message).
3. The acquirer sends an authorisation advice (0120 message) to notify the issuer of the final billing amount.
4. The issuer responds with an acknowledgement (0130 message).  
   The issuer updates the cardâs available balance.
5. The acquirer sends a financial notification (presentment) for the final amount.

Thredd provides additional authorisation advice messages to program managers:

* If the final amount is more than the initial authorised amount, then Thredd sends an authorisation advice of type J to the program manager.
* If the final amount is less than the initial authorised amount, then Thredd sends an authorisation reversal advice of type D to the program manager.