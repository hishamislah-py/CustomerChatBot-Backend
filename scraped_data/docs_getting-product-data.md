# Getting Product Data

The Get Product and Get Product for Program Manager endpoints enable you to list products your program has on Thredd systems and view the details of each product. The Get Product endpoint enables you to view a list of all products associated with your program, while the Get Product for Program Manager enables you to view detailed information for a specific product.

## Get Product

The Get Product endpoint allows you to retrieve a list of products for your program. You can retrieve the list by making a GET request to the Get Product endpoint. For example:

```json Example Get Product endpoint
{{base-url}}/products
```

A successful response will return a HTTP 200 response code. Below is an example response:

```json Example Get Product response
[
    {
        "productID": 8591,
        "productName": "Test Session",
        "accountCode": "01",
        "schemeName": "SCHEME TEST",
        "currencyCode": "GBP"
    }
]
```

> 👍 API Explorer
>
> See the [Get list of Products for a given Program Manager](https://cardsapidocs.thredd.com/reference/get-list-of-products-for-given-program-manager-1) endpoint.

## Get Product for Program Manager

The Get Product for Program Manager endpoint allows you to retrieve details for a specified product id. This id must be specified in the endpoint. You can retrieve details for your program manager by making a GET request to the Get Product for Program Manager endpoint. For example:

```json Example Get Product for Program Manager endpoint
{{base-url}}/products/{{productId}}
```

> 📘 Note
>
> You can get the product id from the Get Product endpoint response.

A successful response will return a HTTP 200 response code. Below is an example response:

```json Example Get Product for Program Manager response
{
    "supportedCredentialTypesCsv": null,
    "supportedCredentialTypes": [],
    "defaultCredentialTypeId": null,
    "fallbackCredentialTypeId": null,
    "productId": 10023,
    "accountCode": "01",
    "schemeId": 644,
    "schemeName": "GPS SCHEME TEST",
    "currencyCode": "GBP",
    "groupFeeTranCode": "",
    "groupFeeMasterCode": "",
    "groupFeeWebCode": "",
    "groupMCCCode": "",
    "groupUsageCode": "PMT-CU-001",
    "ehiMode": 3,
    "supplier3DS": "4",
    "supplier3DSName": null,
    "supplier3DSVersion": "Apata",
    "fraudManagement": 0,
    "cardDefaultIsSingleUse": null,
    "cardDefaultIsNonReloadable": null,
    "fraudNotificationMethod": 0,
    "config3dSecure": {
        "language": "en-EN",
        "apata": {
            "cardProgramId": "sudbhcfndjfncvfhgn",
            "challengeProfileId": "rshgbvbhmbhverdctgvrwe",
            "kbaNumberOfQuestionsToAnswer": 0,
            "kbaNumberOfIncorrectPermissible": 0
        }
    }
}
```

> 👍 API Explorer
>
> See the [Get Product](https://cardsapidocs.thredd.com/reference/get-product-1) endpoint.