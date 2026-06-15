# Managing Card Control Groups

Card control groups are set up in the Thredd system, based on the information you provided in your Product Setup Form (PSF). At the time of card creation, default control groups for your card program are applied to the card. After card creation, you can update these with your own groups. You can only use the List Card Control Groups and Update Card Control Groups after the groups have been setup in the PSF.

> 📘 Note
>
> You cannot change card control group settings via the REST API. If you want to change the settings of your groups, contact your Implementation Manager.

## List Card Control Groups

The List Card Control Groups API returns a list of all the card control groups in your program. You can retrieve the card control groups list by making a GET request to the endpoint. For example:

```json List Card Control Groups endpoint
{{base-url}}/groups
```

A successful response returns a HTTP 200 response code. The response displays the group type (groupType) identifier, the name of the group type (for example, authFeeGroup), and then the groups associated with the group type. In the below example, the response shows the AuthFeeGroup control group type (groupType 4) and the groups associated with the type.

For a full list of the different group types, see [Introduction to Card Usage Groups](https://cardsapidocs.thredd.com/docs/introduction-to-card-controls).

```json Example List Card Control Group body
[
    {
        "groupType": "4",
        "groupTypeName": "AuthFeeGroup",
        "groups": [
            {
                "id": 786,
                "code": "TEST",
                "description": "TEST"
            },
            {
                "id": 1063,
                "code": "TEST-1",
                "description": "TEST 1"
            },
            {
                "id": 1137,
                "code": "TEST-2",
                "description": "Tran Test"
            },
            {
                "id": 1202,
                "code": "NEW-TEST-1",
                "description": "MENA TEST 1"
            },
            {
                "id": 1221,
                "code": "TEST008",
                "description": "Test 08"
            }
        ]
    }
]
```

> 👍 API Explorer
>
> See the [List Card Control Groups](https://cardsapidocs.thredd.com/reference/list-card-control-groups-1) endpoint for more information.

## Update Card Control Groups

The Update Card Control Groups API enables you to change the card control groups linked to a specified card. You can update the card control groups linked to a card by making a PUT request to the endpoint. For example:

```json Example Update Card Control Groups endpoint
{{base-url}}/cards/{{publicToken}}/groups
```

The PUT body should include the group IDs that you want to update. These IDs must be valid IDs for your program. Note that you can use the List Card Control Groups API to retrieve the full list of valid IDs available. The below is an example of what the body could look like.

```json Update Card Control Groups body
{
    "controlGroups": {
        "limitsGroup": 3368
    }
}
```

A successful response will return a HTTP 200 response code and the following response:

```json Update Card Control Groups response
{
    "limitsGroup": 3368,
    "usageGroup": 374,
    "recurringFeeGroup": 0,
    "webServiceFeeGroup": 0,
    "authFeeGroup": 1221,
    "mccGroup": 0,
    "cardLinkageGroup": 0,
    "calendarGroup": 0,
    "fxGroup": 0,
    "paymentTokenUsageGroup": 0,
    "cardAcceptorAllowList": 1,
    "cardAcceptorDisallowList": 1,
    "limitedNetworkGroup": 0
}
```

> 👍 API Explorer
>
> See the [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) endpoint for more information.

### Remove a Control Group from a Card

Use the Update Card Control Groups endpoint to remove a control group from a card. You can do this by setting a value of `-1`  in the request body against the group you want to remove from a card. In the following example, the request body will remove the limitsGroup from the card.

```json Example Remove Control Group request
{
    "controlGroups": {
        "limitsGroup": -1
    }
}
```

If successful, a 200 response is returned with the limitsGroup set to null.

```json Example Remove Control Group response
{
    "limitsGroup": 0,
    "usageGroup": 1004,
    "recurringFeeGroup": 0,
    "webServiceFeeGroup": 0,
    "authFeeGroup": 0,
    "mccGroup": 0,
    "cardLinkageGroup": 0,
    "calendarGroup": 0,
    "fxGroup": 0,
    "paymentTokenUsageGroup": 0,
    "cardAcceptorAllowList": 0,
    "cardAcceptorDisallowList": 0,
    "limitedNetworkGroup": 0
}
```