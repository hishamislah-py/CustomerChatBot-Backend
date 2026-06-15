# Release Notes for 11 November 2022

New changes to the GPS Cards API for the week ending 11 November 2022.

* [New Update STIP Balance endpoint added](#new-update-stip-balance-endpoint-added)
* [Free text fields added to Create Card endpoint](#free-text-fields-added-to-create-card-endpoint)
* [TransferFunds Transaction Type added](#transferfunds-transaction-type-added)

## New Update STIP Balance endpoint added

*Endpoint: /cards/\{PublicToken}/balance/stip*

A new endpoint has been created for customer's using EHI Mode 4 or 5 so that they can adjust a balance for a card.

You can update the balance by making a PUT request to the endpoint. For example:

```json
https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/{PublicToken}/balance/stip
```

The body of the request can have the following fields included:

* AvailableSTIPBalanceGPS
* CurrentSTIPBalanceGPS
* CurrenceyCode
* BalanceSequenceIDExT
* UpdatedBy
* ProcessingDate
* ProcessingTime
* RequestDate
* RequestTime
* TxnCode
* IssCode
* ItemId
* ActionCode

The below is an example body for an Update STIP balance request:

```json
{
  "AvailableSTIPBalanceGPS": 150,
  "CurrentSTIPBalanceGPS": 200,
  "CurrenceyCode": "GBP",
  "BalanceSequenceIDExT": 1234,
  "UpdatedBy": "J Sims",
  "TxnCode" : 16,
  "IssCode" : "PMT",
  "RequestDate": 2022-10-09,
  "RequestTime": 11:32:32
}
```

If successful, a 200 response will be returned with details of the transaction. The below is an example response:

```json
{
  "BalanceSequenceID": 1235,
  "BalanceSequenceIDExT" : 1234,
  "CurrenceyCode": "GBP",
  "TxnCode" : 16,
  "ItemId" : 23290,
  "IssCode" : "PMT"
  "ActionCode" : 000,
  "ProcessingDate": 2022-10-09,
  "ProcessingTime" : 11:34:32
}
```

> 👍 Documentation/API Explorer
>
> * For more information on this endpoint, see [Update STIP Balance](https://cardsapidocs.thredd.com/docs/update-stip-balance)
> * To try the Update STIP Balance endpoint, navigate to [Update Card STIP Balance](https://cardsapidocs.thredd.com/reference/update-card-stip-balance) in API Explorer

## Free text fields added to Create Card endpoint

*Endpoint: /cards*

Two new fields (Freetext1 and Freetext2) have been added to the Create Card endpoint to enable users to send information to the card manufacturers. These fields are non-mandatory and have a maximum length of 50 characters.

The following example includes the new fields in a Create Card request.

```json Example Create Card request
{
    "CardType":"Physical",
    "CardProduct": 10023,
    "CustomerReference": "CustNo12345A",
    "Freetext1": "Comments for the card manufacturer can go in this field",
    "Freetext2": "And in this field too.", 
    "CardHolder": {
        "Title": "Mr.",
        "FirstName": "Bruce",
        "LastName": "Wayne",
        "DateOfBirth": "1982-02-19",
        "Mobile": "07755123456",
        "Email": "BWayne@iambatman.com"
    },
    "Address": {
        "AddressLine1": "1007",
        "AddressLine2": "Mountain Drive",
        "AddressLine3": "Worksop",
        "City": "Gotham",
        "County": "New Jersey",
        "PostCode": "GC11 2LD",
        "Country": "GBR"
    },
    "fulfillment": {
        "AddressLine1": "1007",
        "AddressLine2": "Mountain Drive",
        "AddressLine3": "Worksop",
          "city": "Gotham",
          "country": "GBR",
          "county": "Gothamshire",
          "PostCode": "GC11 2LD"
     },
     "ManufacturingDetails":
     {
       "CardManufacturer": "AB Note",
        "DeliveryMethod": 0,
        "CarrierType": "Type 1",
        "Quantity": 1,
        "Language": "HU",
        "ThermalLine1": "asdeoivh2neriuvnqkr",
        "ThermalLine2" : "asjkfnkerjnkwe",
        "EmbossLine4" : "jdwncwlkejr",
        "VanityName" : "Name Mane",
             "ImageDetails":
             {
                  "ImageId": "An image id",
                  "LogoFrontId" : "A logo ID",
                  "LogoBackId": "Another logo ID"
             },
    "nameOnCard": {
        "title": "Mr",
        "firstName": "Bruce",
        "lastName": "Wayne"
     }
     
    
    }

}
```

> 👍 Documentation/API Explorer
>
> * For more information, see [Create Card](https://cardsapidocs.thredd.com/docs/create-card-2)
> * To try the Create a Card endpoint, navigate to [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) in API Explorer

## TransferFunds Transaction Type added

*Endpoint: /cards/\{publicToken}/transactions*

A TransferFunds option has been added to the Transactions endpoint, enabling users to transfer funds between cards in the GPS system, and to facilitate loading cards from an MVC.

The below is an example body for a transaction where the **TransactionType** has been set to *TransferFunds*.

```json Example Transaction body
{
"TransactionType": "TransferFunds",
"Amount": 10.00,
"CurrencyCode": "GBP",
"ToPublicToken": "987654321",
"User": "string",
"Description": "string"
}
```

If successful, A 200 response is returned with details on the transaction.

```json
{
"Balance": {
  "CurrencyCode": "GBP",
  "ActualBalance": 10.00,
  "BlockedAmount": 0.00,
  "AvailableBalance": 10.00 
  }
"Transaction":[
  {
    "PublicToken": {publicToken}*,
    "TransactionID": "string",
    "TransactionType":"Unload",
    "Amount": 10.00,
    "CurrencyCode":"GBP"
    },
    {
    "PublicToken": {toPublicToken}*,
    "TransactionID": "string",
    "TransactionType":"Load",
    "Amount": 10.00,
    "CurrencyCode":"GBP"
    }
] 
}
```

> 👍 Documentation/API Explorer
>
> * For more information, see [Transaction Types](https://cardsapidocs.thredd.com/docs/loading-unloading-a-card)
> * To try the Create a Card endpoint, navigate to [Load or Unload Card](https://cardsapidocs.thredd.com/reference/load-or-unload-card) in API Explorer