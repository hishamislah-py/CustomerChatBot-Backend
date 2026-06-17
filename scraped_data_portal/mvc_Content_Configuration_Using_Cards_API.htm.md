# 5 Using the Cards API

This section describes how to use Thredd's REST-based Cards API to create and manage your MVCs.

The REST API uses the following base URL: *https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards*.

The Cards API does not include endpoints dedicated endpoints specifically for MVCs. However, you can use particular endpoints for cards in MVCs.

## 5.1 Creating an MVC

To create an MVC, use the [Create Card](https://cardsapidocs.thredd.com/reference/create-card) API and set `"MasterVirtual"` as the `"CardType"`.

You do not need to complete card fulfilment and other non-mandatory details in the request.

See the example body below.

#### Example Request

[Copy](javascript:void(0);)

```
{  
     "cardHolder": {  
          "title": "Mr",  
          "firstName": "Jon",  
          "lastName": "Smith",  
          "dateOfBirth": "1982-11-03"  
     },  
     "address": {  
          "addressLine1": "32 Western Drive",  
          "postCode": "S25 2BZ",  
          "country": "GBR"  
     },  
      
     "cardType": "MasterVirtual",  
     "cardProduct": 10005,  
     "designId": "New Card Brand",  
     "customerReference": "my ref 12345"  
}
```

#### Example Response

Thredd returns a `publicToken` for the MVC in the response. You should use the `publicToken` to [link cards to a Master Virtual Card](#Linking).

[Copy](javascript:void(0);)

```
{  
    "publicToken": "103170223",  
    "customerReference": "my ref 12345",  
    "embossName": "Mr Jon Smith",  
    "maskedPan": "999999******5347",  
    "startDate": "2023-11-09",  
    "expiryDate": "2028-11-30"  
}
```

## 5.2 Loading and Unloading an MVC

You can use the *Load or Unload Card* API endpoint for transactions to transfer card balances between your MVC and linked cards. In your request, your endpoint should include the `publicToken` of the MVC card in the path. Additionally, the body of the request should include the `publicToken` of the card to where you are transferring the balance. See the example body request below. For further details on using the transactions API, see the [Cards API Website > Balance Transfers](https://cardsapidocs.thredd.com/docs/loading-unloading-a-card#balance-transfers).

#### Example Request

[Copy](javascript:void(0);)

```
{  
  "transactionType": "TransferFunds",  
  "amount": 10,  
  "currencyCode": "GBP",  
  "toPublicToken": "112233445"  
}
```

#### Example Response

[Copy](javascript:void(0);)

```
{  
"Balance": {  
  "CurrencyCode": "GBP",  
  "ActualBalance": 10.00,  
  "BlockedAmount": 0.00,  
  "AvailableBalance": 10.00   
  }  
"Transaction":[  
  {  
    "PublicToken": 987654321,  
    "TransactionID": "string",  
    "TransactionType":"Unload",  
    "Amount": 10.00,  
    "CurrencyCode":"GBP"  
    },  
    {  
    "PublicToken": 112233445,  
    "TransactionID": "string",  
    "TransactionType":"Load",  
    "Amount": 10.00,  
    "CurrencyCode":"GBP"  
    }  
]   
}
```

## 5.3 Linking Cards to an MVC

When creating secondary cards which you want to link to a primary or MVC, you should enter the `publicToken` value of your MVC into the `parentCard` field. See [Create Card Field Descriptions](https://cardsapidocs.thredd.com/docs/create-card-field-descriptions) for more details.

You need to ensure that the product for the child card has an associated Card Linkage Group. You can check for the associated Linkage Group on the product by using the *Get list of products for a given Program Manager* endpoint. See [Get Product for Program Manager](https://cardsapidocs.thredd.com/docs/getting-product-data#get-product-for-program-manager) for more details.

In the example request, if the `publicToken` of your MVC is 987654321, then the `parentCard` field of the linked card you are creating should have the value of 987654321 in the example request.

[Copy](javascript:void(0);)

```
{  
    "CardType":"Physical",  
    "CardProduct": 10023,  
    "CustomerReference": "CustNo12345A",  
    "parentCard": "987654321",  
    "CardHolder": {  
        "Title": "Mr.",  
        "FirstName": "Bruce",  
        "MiddleName": "Alan",  
        "LastName": "Bloggs",  
        "DateOfBirth": "1982-02-19",  
        "Mobile": "07755123456",  
        "Email": "babloggs@email.com"  
    },  
    "Address": {  
        "AddressLine1": "1007",  
        "AddressLine2": "Mountain Drive",  
        "AddressLine3": "string",  
        "City": "London",  
        "PostCode": "GC11 2LD",  
        "Country": "GBR"  
    },  
    "fulfilment": {  
        "AddressLine1": "1007",  
        "AddressLine2": "Mountain Drive",  
        "AddressLine3": "string",  
        "City": "London",  
        "PostCode": "GC11 2LD",  
        "Country": "GBR"  
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
             }     
    }  
}
```

## 5.4 Transferring Funds to a Child Card

You can transfer funds from an MVC to a child card using the *Transactions* endpoint.
To transfer funds from the MVC to the child card, the request body must have `transferFunds` set in the `transactionType` field and the child public token set in the `toPublicToken` field. See the below example where Â£200 is being transferred from the MVC with the publicToken of 103170108 to the child card publicToken 100512652.

[Copy](javascript:void(0);)

```
{  
  "transactionType": "TransferFunds",  
  "amount": 200,  
  "currencyCode": "GBP",  
  "toPublicToken": "100512652"  
}
```