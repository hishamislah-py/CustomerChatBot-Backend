# Merchant Disallow Lists

This section provides instructions on how to add a card or card group to a merchant disallow list.

Merchant lists enable you to control which merchants or merchant codes are blocked or allowed to use your service. This API enables you to manage merchant disallow lists, which can then be assigned to a single card or multiple cards. Any merchant IDs in the disallow list will see transactions declined by Thredd at the authorisation stage. The response code will be ’05 – Do not honour’.

## Add Merchant to Disallow List

The Add Merchant to Disallow List endpoint allows you to add merchants to a disallow list. You can do this by adding the List ID to the end of the Disallow Merchant endpoint. For example:

```json Example Add Merchant to Disallow List endpoint
{{base-url}}/groups/allowmerchant/{{DisallowListID}}
```

The POST body should include the merchant IDs that you want to associate with the nominated disallow list. The below is an example of what the body should look like.

```json Example Add Merchant to Disallow List body
{
    "merchantIds": [
        "Merchant5"
    ]
}
```

A successful response will return a HTTP 200 response code and the following response:

```json Example Add Merchant to Disallow List response
{
    "listId": 71,
    "listName": "LIST TEST",
    "listType": "Disallow",
    "isActive": true,
    "schemeId": null,
    "schemeName": "",
    "institutionId": 142,
    "institutionName": "INSTITUTION TEST",
    "cardAcceptors": [
        "12345",
        "Merchant5"
    ]
}
```

> 👍 API Explorer
>
> See the [Add Merchant to Disallow List](https://cardsapidocs.thredd.com/reference/add-merchant-to-disallow-list) endpoint.

## Remove Merchant from Disallow List

The Remove Merchant from Disallow List endpoint allows you to remove a merchant from a disallow list. You can do this by using the DELETE method and adding the List ID and Merchant ID to the end of the Disallow Merchant endpoint. For example:

```json Example Remove Merchant from Disallow List endpoint
{{base-url}}/groups/allowmerchant/{{DisallowListID}}/{{MerchantID}}
```

No body is required in the request. A successful response will return a HTTP 204 response code and the merchant will be removed from the disallow list.

> 👍 API Explorer
>
> See the [Remove Merchant from Disallow List](https://cardsapidocs.thredd.com/reference/remove-merchant-from-allow-list) endpoint.