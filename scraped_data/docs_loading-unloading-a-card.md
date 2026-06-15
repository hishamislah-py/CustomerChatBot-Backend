# Transaction Types

This section provides instructions on how to load or unload card funds in your card's currency and perform balance adjustments. If Thredd maintains the balance on cards on your behalf, you can manage balances using the Load / Unload card & adjust balance endpoint.

> 📘 Note
>
> Loads, unloads and balance adjustments are relevant to customers using *External Host Interface (EHI)* mode 3, where Thredd maintains the card balance and performs transaction authorisation.

Thredd can support the following transaction types:

* **Load** - used to add a positive balance onto a card
* **Unload** - used to remove or partially remove a balance from a card
* **BalanceAdjustment** - used to adjust the balance on a card up or down
* **TransferFunds** - used to transfer funds from one card to another
* **Fees** - used to apply one-off fees to a card

## Loading or Unloading a Card

### Step 1: Retrieve card details

Before loading a card, identify the corresponding Public Token for the card to be used.\
A card's public token is returned in the response to creating a card within the `publicToken` object.

### Step 2: Unload or load a card

After identifying the <Glossary>Public Token</Glossary> for the card and the amount you want to load onto the card, you can create a transaction to move the balance on or off the card. To do this, execute a POST request to the *transactions* endpoint with the corresponding `TransactionType`.

```json Example Load/Unload Card endpoint
{{base-url}}/cards/{{publicToken}}/transactions
```

> 📘 Note
>
> Certain card status values will not allow you to load a balance onto a card. For more information on card status values, see [Card Status](card-status).

Below are examples of a load and unload payload requests for the value of £10.00 GBP

```json Example Card load request payload
{
	"transactionType": "Load",
	"amount": 10.00,
	"currencyCode": "GBP",
	"loadedBy": "System",
	"description": "Card Top up for Lunch"
}
```

```json Example Card unload request payload
{
	"transactionType": "Unload",
	"amount": 10.00,
	"currencyCode": "GBP",
	"loadedBy": "System",
	"description": "Moving of funds"
}
```

```json Example Card balance adjustment payload
{
	"transactionType": "BalanceAdjustment",
	"amount": 5.23,
	"currencyCode": "GBP",
	"loadedBy": "System",
	"description": "Credit Adjustment"
}
```

A successful response will return a 200 with the card's load transaction and the updated balance in the response.

```json Example Load Card response
{
    "transaction": [
        {
            "transactionType": "Load",
            "transactionId": 6157564898,
            "amount": 1000,
            "currencyCode": "GBP",
            "publicToken": "103169969"
        }
    ],
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 1000,
        "pendingAmount": 0,
        "availableBalance": 1000
    }
}
```

> 👍 API Explorer
>
> See the [Load / Unload card & adjust balance](https://cardsapidocs.thredd.com/reference/load-or-unload-card) endpoint for more information.

## Balance Transfers

The *TransferFunds* transaction type enables you to transfer funds from the card specified in the Transaction endpoint, to a card specified in the body of the request. This enables users to transfer funds between cards in the Thredd system, and to facilitate loading cards from <Glossary>Master Virtual Cards</Glossary>.

```json Example Balance Transfer endpoint
{{base-url}}/cards/{{publicToken}}/transactions
```

The below is an example body for a transaction where the **TransactionType** has been set to *TransferFunds*.

```json Example TransferFunds body
{
"transactionType": "TransferFunds",
"amount": 10.00,
"currencyCode": "GBP",
"toPublicToken": "987654321",
"user": "string",
"description": "string"
}
```

If successful, A 200 response is returned with details on the transaction. In this example, a transfer of £10 has been made from the publicToken 123456789 (indicated by the **Unload** transactionType nest) to the 987654321 publicToken (indicated by the **Load** transactionType nest).

```json Example TransferFunds response
{
"balance": {
  "currencyCode": "GBP",
  "actualBalance": 10.00,
  "blockedAmount": 0.00,
  "availableBalance": 10.00 
  }
"transaction":[
  {
    "publicToken": 123456789,
    "transactionID": "string",
    "transactionType":"Unload",
    "amount": 10.00,
    "currencyCode":"GBP"
    },
    {
    "publicToken": 987654321,
    "transactionID": "string",
    "transactionType":"Load",
    "amount": 10.00,
    "currencyCode":"GBP"
    }
] 
}
```

> 📘 Note
>
> Balance Adjustments can be performed on a card for any amount and for any reason, such as to credit a settled Chargeback amount, or to correct the balance of a card due to timeouts or bug. The only check that is performed is to see whether a balance adjustment (credit) would result in Max allowed balance on a card (as per the velocity limit group).

## Balance Adjustment

Use this endpoint to adjust the balance on a card. Use the amount field to either adjust the balance positively or negatively.

The following examples display how to adjust the balance positively or negatively.

```json Example Positive Balance Adjustment
{
  "transactionType": "BalanceAdjustment",
  "amount": 20,
  "currencyCode": "GBP"
}
```

```json Example Negative Balance Adjustment
{
  "transactionType": "BalanceAdjustment",
  "amount": -20,
  "currencyCode": "GBP"
}
```

If successful, a 200 response is returned with details on the transaction and an updated balance based on the transaction. In the below example, £20 has been removed from the balance of publictoken 116611859, leaving an available balance on the card of £80.

```json Example Adjust Balance Response
{
    "transaction": [
        {
            "transactionType": "BalanceAdjustment",
            "transactionId": 6161692754,
            "amount": -20,
            "currencyCode": "GBP",
            "publicToken": "116611859"
        }
    ],
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 80,
        "pendingAmount": 0,
        "availableBalance": 80
    }
}
```

## Applying Fees

Use this endpoint to apply one-off fees to a card by setting the transactionType field to `Fee `in the request body. When the transactionType is set to Fee, the following fields must be included in the request.

* currencyCode
* feeAmount
* feeType

The following example displays the payload of a fee of £20 for transferring funds.

```json Example Add Fee request
{
  "transactionType": "Fee",
  "feeType": "FundsTransferFee",
  "currencyCode": "GBP",
  "feeAmount": 20
}
```

The following table describes each of the fee types available.

| Fee Type                | Description                   |
| :---------------------- | :---------------------------- |
| undefined               | An undefined fee.             |
| FundsTransferFee        | Bank Transfer                 |
| PINCVVServiceFee        | Service Fee for PIN and CVV   |
| MonthlyServiceFee       | Monthly Service Fee           |
| ReloadFromMVCFee        | MVC Load                      |
| CardConversionFee       | Card Conversion Fee           |
| PhysicalCardIssuingFee  | Card Issue Fee (Physical)     |
| AdministrationFee       | Administration Fee            |
| CardReplacementFee      | Card Replacement Fee          |
| VirtualCardIssuingFee   | Card Issue Fee (Virtual)      |
| ParentCardActivationFee | Primary Card Activation Fee   |
| ChildCardActivationFee  | Secondary Card Activation Fee |
| FirstLoadFromMVCFee     | First Load from MVC           |
| RecurringFee            | Recurring Fee                 |

If successful, a 200 response is returned with details of the transaction and the updated balance on the card.

```json Example Apply Fee Response
{
    "transaction": [
        {
            "transactionType": "Fee",
            "transactionId": 6161692763,
            "amount": 20,
            "currencyCode": "GBP",
            "publicToken": "116611859"
        }
    ],
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 910,
        "pendingAmount": 0,
        "availableBalance": 910
    }
}
```