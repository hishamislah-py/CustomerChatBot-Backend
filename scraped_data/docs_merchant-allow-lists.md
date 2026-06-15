# Merchant Allow Lists

This page shows you how to add and remove allowed merchants to and from a card acceptor list.

Merchant lists enable you to control which merchants or merchant codes are blocked or allowed to use your service. This API enables you to manage merchant allow lists, which can then be assigned to a single card or multiple cards. Only merchant IDs added to the allow list will be approved by Thredd at authorisation stage.

## Add Merchant to Allow List

The Add Merchant to Allow List endpoint allows you to add merchants to the allow list. You can do this by adding the List ID to the end of the Allow Merchant endpoint. For example:

```json Example Add Merchant to Allow List endpoint
{{base-url}}/groups/allowmerchant/{{AllowListID}}
```

The POST body should include the merchant IDs that you want to associate with the nominated allow list. The below is an example of what the body should look like.

```json Example Add Merchant to Allow List body
{
    "merchantIds": [
        "Merchant5"
    ]
}
```

A successful response will return a HTTP 200 response code. Below is an example response:

```json Example Add Merchant to Allow List response
{
    "listId": 86,
    "listName": "list80",
    "listType": "Allow",
    "isActive": true,
    "schemeId": null,
    "schemeName": "",
    "institutionId": 142,
    "institutionName": "INSTITUTION TEST",
    "cardAcceptors": [
        "Merchant15",
        "Merchant19",
        "Merchant3",
        "Merchant4",
        "Merchant5",
        "Merchant7",
        "Merchant9"
    ]
}
```

> 👍 API Explorer
>
> See the [Add Merchant to Allow List](https://cardsapidocs.thredd.com/reference/add-merchant-to-allow-list-1) endpoint.

## Remove Merchant from Allow List

The Remove Merchant from Allow List endpoint allows you to remove a merchant from an allow list. You can do this by using the DELETE method and adding the List ID and Merchant ID to the end of the Allow Merchant endpoint. For example:

```json Example Remove Merchant from Allow List endpoint
{{base-url}}/groups/allowmerchant/{{AllowListID}}/{{MerchantID}}
```

No body is required in the request. A successful response will return a HTTP 204 response code and the merchant will be removed from the allow list.

> 👍 API Explorer
>
> See the [Remove Merchant from Allow List](https://cardsapidocs.thredd.com/reference/remove-merchant-from-disallow-list-1) endpoint.