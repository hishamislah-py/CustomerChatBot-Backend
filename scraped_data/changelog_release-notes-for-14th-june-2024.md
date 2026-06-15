# Release Notes for 14th June 2024

New changes to the Thredd Cards API for the week ending 14th June 2024. These include:

* [New fields added to Retrieve Card response](#new-fields-added-to-retrieve-card-response)
* [groupTypeName field added to List Card Control Groups response](#grouptypename-field-added-to-list-card-control-groups-response)
* [Limit Checks for Balance Adjustment Transaction Type](#limit-checks-for-balance-adjustment-transaction-type)
* [Cache-Control Added to Header Response](#cache-control-added-to-header-response)

## New fields added to Retrieve Card response

Three new fields have been added to the response of the Retrieve Card endpoint.

* `ehiMode `returns the EHI mode of the product the card is associated with
* `programManagerID` returns the program manager identifier
* `programManagerCode` returns the program manager code

See the below example of a successful Retrieve Card response with the new fields included.

```json Example Retrieve Card response
{
    "cardType": "Physical",
    "publicToken": "638050230",
  	"status": "Active",
    "cardStatusCode": "00",
    "cardStatusDescription": "00 (Active)",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 300.67,
        "pendingAmount": -74,
        "availableBalance": 226.67
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr. Bruce Simms",
        "maskedPan": "531610******0462",
        "startDate": "2023-10-23",
        "expiryDate": "2028-10-31",
        "clearPan": null,
        "cvv": null,
        "activationDate": "2024-05-14 08:31:33Z"
    },
    "cardHolder": {
        "title": "Mr",
        "firstName": "John",
        "middleName": "",
        "lastName": "Smith",
        "dateOfBirth": "1963-11-22",
        "mobile": "",
        "email": ""
    },
    "cardProduct": {
        "scheme": "Sandbox Scheme",
        "product": 1234,
      	"productShortName": "Sandbox",
        "ehiMode": 1
    },
    "controlGroups": {
        "limitsGroup": 1,
        "usageGroup": 0,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": -1,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": -1,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0
    },
    "3DS": [],
    "designId": "Sandbox",
  	"childCards": [],
    "siblingCards": [],
    "address": {
        "addressLine1": "32 Eastern Lane",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": "",
        "county": "",
        "postCode": "S11 7AA",
        "country": "826"
    },
    "fulfilment": {
        "addressLine1": "32 Eastern Lane",
        "addressLine2": "",
        "addressLine3": "",
        "city": "",
        "state": "",
        "county": "",
        "postCode": "S11 7AA",
        "country": "826"
    },
 	 "freetext1": "Comments for the card manufacturer here",
   "freetext2": "And in this field too.",
   "IsSingleUse" : "true",
   "IsNonReloadable" : "false",
   "cardAcceptorIds": {
        "allowCardAcceptors": [],
        "disallowCardAcceptors": []
    },
    "language3ds": null,
 	  "programManagerID": 78,
    "programManagerCode": "PMT"
}
```

## groupTypeName field added to List Card Control Groups response

This field describes the name of the card control group, enabling you to identify the group type. Previously, only the ID for the group was returned (in the groupType field). See the below example of a response with the groupTypeName field returned.

```json Example List Card Control Groups response
[
    {
        "groupType": 4,
        "groupTypeName": "AuthFeeGroup",
        "groups": [
            {
                "id": 786,
                "code": "GPS-TEST",
                "description": "GPS-TEST"
            }
          ]
    }
]
```

## Limit Checks for Balance Adjustment Transaction Type

Most limit checks have now been removed when using the Balance Adjustment transaction type on the Load/Unload Card endpoint. Balance Adjustments can now be performed on a card for any amount and for any reason, such as to credit a settled Chargeback amount, or to correct the balance of a card due to timeouts or bug. The only check that is performed is to see whether a balance adjustment (credit) would result in Max allowed balance on a card (as per the velocity limit group). If this exceeds the max balance allowed on a card, then the balance adjustment should be declined.

See the below example 422 error response where the balance adjustment would exceed the maximum allowed balance.

```json Example Balance Adjustment response
{
    "type": "https://tools.ietf.org/html/rfc4918#section-11.2",
    "title": "One or more validation errors occurred.",
    "status": 422,
    "traceId": "00-bc13ff2ac4c2ab2f22a41dc766f5da25-65dac3d72a71615e-00",
    "errors": {
        "Messages": [
            "BalanceAdjustment Failed. The maximum allowed balance is 5000"
        ]
    }
}
```

## Cache Control Added to Header Response

The Cache-Control header has been added to all endpoints from this release. This header, included in the response for every endpoint, ensures that no confidential data is stored in a user's browser cache.

The header contains the following response directives:

| Directive       | Description                                                                                                                                                                                   |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| no-cache        | Indicates that the response can be stored in caches, but the response must be validated with the origin server before each reuse, even when the cache is disconnected from the origin server. |
| no-store        | Indicates that any caches of any kind (private or shared) should not store this response.                                                                                                     |
| must-revalidate | Indicates that the response can be stored in caches and can be reused while fresh.                                                                                                            |
| max-age=0       | Indicates that the response doesn't remain fresh after the response is generated.                                                                                                             |
| s-maxage=0      | Indicates that the response doesn't remain fresh in a shared cache.                                                                                                                           |

See the below image for an example of the Cache-Control header successfully returned in a response.

![](https://files.readme.io/07ddd6b-image.png)