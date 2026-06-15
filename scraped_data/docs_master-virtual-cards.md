# Master Virtual Cards

A *Master Virtual Card (MVC)* is a card that is restricted to loading and unloading to a physical or virtual card and cannot be used for e-commerce or in-store transactions. An MVC is used to reflect the value of the ‘actual’ money in the Issuer's bank account. An MVC guarantees that the load is limited to the amount prefunded (i.e. loaded onto MVC) and gives the Programme Manager the ability to distribute funds immediately rather than having to wait for notification of each individual load into the Issuer Bank account.

MVCs in the REST API are restricted to loading and unloading the balance onto the card.

## Creating an MVC

Use the Create Card endpoint to create an MVC, setting the `CardType` field to *MasterVirtual*. See the below example of a Create MVC card request body.

```json Example Create MVC request body
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
    
     "virtualCardImageDetails": {
          "virtualCardImageId": "4155",
          "imageSize": 1
     },
     "cardType": "MasterVirtual",
     "cardProduct": 10005,
     "designId": "New Card Brand",
     "customerReference": "my ref 12345"
}

```

## Activating an MVC

An MVC should only use the card status *Restricted* (status code `62`). This is because this status only allows for balance adjustments.

After creating an MVC, use the [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) endpoint to set your MVC card status (the MVC will be inactive at creation). See the below example request body.

```json Example Update Card Status body for activating MVC
{
  "cardStatusCode": "62"
}
```

A 200 OK response will be returned confirmed the status of the card has been changed to *Restricted*.

## Linking a Child Card to an MVC

To associate child cards with the MVC, you will need to ensure that the product associated with the child card has the Card Linkage Group associated with it. You can check to see whether a product has a Linkage Group associated with it by using the [Get Product for Program Manager](https://cardsapidocs.thredd.com/docs/getting-product-data#get-product-for-program-manager) endpoint.

To create a child card and associate it with the parent, the MVC *publicToken* must be included in the request using the `parentCard` field. See the below for an example:

```json Example Create Card request with parentCard populated
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
     "virtualCardImageDetails": {
          "virtualCardImageId": "4155",
          "imageSize": 1
     },
     "cardType": "Virtual",
     "cardProduct": 10005,
     "parentCard": "103170108",
     "designId": "New Card Brand",
     "customerReference": "my ref 12345"
}
```

## Loading funds to an MVC

You can load funds onto an MVC using the [Transactions ](https://cardsapidocs.thredd.com/reference/load-or-unload-card) endpoint. The MVC token should be included in the endpoint URL. For example:

```json Example Transactions endpoint for Master Virtual Card
{{base-url}}/cards/103170108/transactions
```

To load funds onto an MVC, the request body must have load set in the `transactionType ` field. See the below example:

```json Example Transactions body for loading an MVC
{
  "transactionType": "Load",
  "amount": 200,
  "currencyCode": "GBP"
}
```

## Transferring funds from an MVC to a child card

You can transfer funds from your MVC to a child card using the [Transactions ](https://cardsapidocs.thredd.com/reference/load-or-unload-card) endpoint. The MVC token should be included in the endpoint URL. For example:

```json Example Transactions endpoint for Master Virtual Card
{{base-url}}/cards/103170108/transactions
```

To transfer funds from the MVC to the child card, the request body must have *transferFunds* set in the `transactionType `field and the child *publicToken* set in the `toPublicToken `field. See the below example where £200 is being transferred from the MVC publicToken 103170108 to the child card publicToken 100512652:

```json Example Transactions endpoint for transferring from MVC to child card
{
  "transactionType": "TransferFunds",
  "amount": 200,
  "currencyCode": "GBP",
  "toPublicToken": "100512652"
}
```

## Unloading an MVC with Insufficient Balance

The behaviour of how MVCs deal with transactions that exceed the amount of the balance is dependant on an Product level setting. By default, this is enabled. For example, if an MVC that has a balance of £800, an unload request of £1000 will be successful and the value of the MVC will be unloaded to £0.

It is possible to prevent unloading from a child card associated with an MVC if there is not enough balance on the MVC  to cover the transaction by disabling the Product level setting. For example, if the MVC has a balance of £800 and you try to unload £1000 from the MVC, the below error message is returned in a 400 response.

```Text Example Insufficient Funds response
{
		Cannot unload due to insufficient fund.
}
```

> 📘 Information
>
> This behaviour must be enabled before it can be used. Please contact application support via your implementations manager to discuss enabling this functionality.