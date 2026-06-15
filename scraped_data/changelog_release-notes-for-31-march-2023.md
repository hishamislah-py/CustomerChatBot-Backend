# Release Notes for 31 March 2023

New changes to the GPS Cards API for the week ending 31st March 2023.

* [New Get Card Stock endpoint](#new-get-card-stock-endpoint)
* [New fields added to Convert Card endpoint](#new-fields-added-to-convert-card-endpoint)

## New Get Card Stock endpoint

*Endpoint: /products/\{\{product-id}}/stock*\
A new endpoint has been added that enables customers to check the current levels of available card stock for a specified product id.

You can retrieve a product's card stock by making a GET request to the Get Card Stock endpoint. For example:

```json Example Get Card Stock endpoint
{{base-url}}/products/{{product-id}}/stock
```

A successful response will return an HTTP 200 response code and the currently available stock for the card and the product id. Below is an example response:

```json Example Get Card Stock response
{
    "productId": 10023,
    "availableStock": 1034
}
```

> 👍 Documentation/API Explorer
>
> * For more information on the Get Card Stock endpoint, see [Getting Card Stock Data](https://cardsapidocs.thredd.com/docs/getting-card-stock-data).
> * To try the Get Card Stock endpoint, navigate to [Get's a products' available stock count](https://cardsapidocs.thredd.com/reference/gets-productsvailable-stock-count)in API Explorer.

## New fields added to Convert Card endpoint

Two new fields have been added to the Convert Card endpoint, enabling users to either move the expiry date from the original card or to be able to set a new expiry date.

* The **moveExpiryDate** field, if set to true. will move the expiry date to the new card.
* The **newExpiryDate** field enables you to set a new expiry date in a YYYY-MM format.

> 📘 Note
>
> The moveExpiryDate and newExpiryDate fields cannot be used as part of the same API call.

See the following examples of the Convert Card body that includes the new fields.

```json Example Convert Card body with moveExpiryDate
{
    "cardType": "Physical",
    "moveExpiryDate": true
}
```

```json Example Convert Card body with newExpiryDate
{
  "cardType": "Physical",
  "newExpiryDate": "2025-05"
}
```

> 👍 Documentation/API Explorer
>
> * For more information on this endpoint, see [Converting a Card from Virtual to Physical](https://cardsapidocs.thredd.com/docs/converting-a-card)
> * To try the Convert Card endpoint, navigate to [Convert Card](https://cardsapidocs.thredd.com/reference/convert-card) in API Explorer