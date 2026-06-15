# Release Notes for 4th July 2024

New changes to the Thredd Cards API coming on the 4th July. These include:

* [Get Card Limits Endpoint Now Returns All Process Spend and Limits](#get-card-limits-endpoint-now-returns-all-process-spend-and-limits)
* [New Field added to Get Card Transactions endpoint](#new-field-added-to-get-card-transactions-endpoint)
* [New Field added to Update Card Control Groups endpoint](#new-field-added-to-update-card-control-groups-endpoint)
* [Added Ability to Clear Control Groups from a Card](#added-ability-to-clear-control-groups-from-a-card)
* [Behaviour Change when Updating Card Status](#behaviour-change-when-updating-card-status)
* [Bug Fix when Replacing a Secondary Card](#bug-fix-when-replacing-a-secondary-card)
* [Modified Error Message for Load/Unload Card endpoint](modified-error-message-for-load/unload-card-endpoint)
* [Bug Fix for Retrieve Card endpoint](#bug-fix-for-retrieve-card-endpoint)

## Get Card Limits Endpoint Now Returns All Process Spend and Limits

The Get Card Limits endpoint now returns all the processed spend and limits for a card. Each sub group now contains a `spent`  field, which returns how much has been spent for that card limit and replaces the `usage` field. The `limit ` field has also been updated for this release, now returning all accumulated limit values for the card (where previously it only returned `accumulatedValueLimit1`)

The below is an example response of the Get Card Limits endpoint with the fields returned.

```json Example Get Card Limits response
"availableBalance": 0,
      "maxAllowableBalance": 65000,
      "currencyCode": "GBP",
      "blockedAmount": 0,
      "cardLimits": [
        {
            "subGroup": "CASH",
            "daily": {
              "period": 1,
              "unit": "day",
              "limit": 15000,       
              "frequency": 30,
              "spent": 0,
              "transactionCount": 0,
              },
            "accumulatedPeriod1": {
              "period": 31,
              "unit": "day",
              "limit": 15000,       
              "frequency": 30,
              "spent": 0,
              "transactionCount": 0,
            },
            "accumulatedPeriod2": {
              "period": 365,
              "unit": "day",
              "limit": 15000,       
              "frequency": 30,
              "spent": 0,
              "transactionCount": 0
              }
        }
      ]  
```

## New Field added to Get Card Transactions endpoint

The `ehiMode` field has been added to the Get Card Transactions endpoint from this release.

```json Example Get Card Transactions response
[
    {
        "title": Mr,
        "firstname": Jon,
        "lastname": Smith,
        "panToken": 0,
        "pubToken": 0,
        "id": 6161679868,
        "description": "string",
        "dateTime": "2024-07-02T10:32:22.78+01:00",
        "lifeCycleId": null,
        "type": {
            "code": "L",
            "description": "Load"
        },
        "status": {
            "code": "S",
            "description": "Settled"
        },
        "amount": {
            "billingValue": 1000.00,
            "billingCurrency": "GBP",
            "transactionValue": 1000.0000,
            "transactionCurrency": "GBP",
            "settlementAmount": 1000.00,
            "settlementCurrency": "GBP",
            "actualBalance": 1000.00,
            "availableBalance": 1000.00
        },
        "fees": {
            "id": 0,
            "fixedFee": 0.00,
            "rateFee": 0.00,
            "fxPadding": 0.00,
            "mccPadding": 0.00
        },
        "productId": 10045,
        "cardNetwork": "VISA",
        "processingCode": "220000",
        "recordId": 0,
        "note": "API Load by ",
        "systemTraceAuditNumber": 0,
        "transactionCountry": "GBR",
        "transactionLink": 6161679868,
        "additionalDetail": null,
        "paymentTokenId": null,
        "paymentMethod": "None",
        "ehiMode": 3
    }
]
```

<br />

## New Field added to Update Card Control Groups endpoint

The `limitedNetworkGroup `fields have been added to the Update Card Control Groups endpoint for this release, enabling you to associate a card with the Limited Network group. A limited network group can restrict card acceptance to a limited network only. For example, a gift card may be limited to merchants in a particular shopping centre only. The rule for restricting card acceptance to a limited network is based on a merchant ID, as well as the address and postcode of where the card can be accepted.

1. DE42 – Merchant ID
2. DE43 – Address, text field for the merchant ID
3. DE61 – Postcode

See the below example of an Update Card Control Groups request.

```json Example Update Card Control Groups request
{
    "controlGroups": {
        "limitedNetworkGroup": 214748364
    }
}
```

## Added Ability to Clear Control Groups from a Card

Behaviour has been changed in this release to allow for control groups to be removed from a card using the Update Card Control Groups endpoint.

To remove a control group from a card, use the Update Card Control Groups endpoint and for the group you want to be removed from a card, enter a value of `-1`.  In the below example, the limitedNetworkGroup will be removed from the card.

```json Example Remove Control Group from a Card
{
    "controlGroups": {
        "limitedNetworkGroup": -1
    }
}
```

A successful response will return a list of the control groups that can be associated with a card, with the group you updated now showing as null.

```json Remove Control Group from a Card response
{
    "limitsGroup": 1051,
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

## Behaviour Change when Updating Card Status

From this release, you can now change a card with an inactive status (02 Inactive) to another status. For example, if the card has been lost in the post, you can update its status to (41 Lost Card). Previously, a card with an inactive status could only be set to an active status (00 Active).

## Bug Fix when Replacing a Secondary Card

A fix has been made so that when replacing a secondary card using the Replace Card endpoint from this release, the primary card details are not lost from the primaryId field. Previously, the primary card details were not being transferred when replacing a secondary card.

## Modified Error Message for Load/Unload Card endpoint

A small correction has been made to an error message when unloading funds from a card using the Load/Unload Card endpoint. If there are insufficient funds on the card, the new message is returned stating that the card "Cannot unload due to insufficient funds."

## Bug Fix for Retrieve Card endpoint

A fix has been made to the Retrieve Card endpoint so that the cardAcceptorAllowList and cardAcceptorDisallowList fields are successfully returned.