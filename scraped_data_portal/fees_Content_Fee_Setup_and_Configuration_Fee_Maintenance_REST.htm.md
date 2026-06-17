# 7 Fee Maintenance (Cards API)

This section describes the options for viewing and maintaining fees for your program using the Thredd REST-based Cards API. For more information on the Thredd API described in this section, see the [Cards API Website (REST)](https://cardsapidocs.thredd.com/).

If you are using the Thredd SOAP Web Services, please read the section [Fee Maintenance (SOAP Web Services)](Fee_Maintenance.htm).

## 7.1 Managing Fee Groups

You can use the Thredd API to query and update the fee groups linked to a card and to apply additional fees to a card.

### 7.1.1 Listing Card Control Groups

You can use the [List Card Control Groups API](https://cardsapidocs.thredd.com/reference/list-card-control-groups-1) to list all groups. This will include your fee groups.

#### Request

[Copy](javascript:void(0);)

JSON

```
curl --request GET \  
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/groups \  
     --header 'accept: application/json'
```

#### Response

[Copy](javascript:void(0);)

JSON

```
[  
    {  
        "groupType": "AuthFeeGroup",  
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

### 7.1.2 Updating Card Fee Groups

When creating a card using the [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) API, the default groups for the card product associated with the card are used.

You can use the [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) API to update the Fee groups linked to a card. See the example below:

You must enter the Thredd code of an existing a Fee group, as defined in your Product Setup Form (PSF).

#### Request

[Copy](javascript:void(0);)

JSON

```
curl --request PATCH \  
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/publicToken/groups \  
     --header 'accept: application/json' \  
     --header 'content-type: application/*+json' \  
     --data '  
{  
  "controlGroups": {  
    "webServiceFeeGroup": 1234,  
    "authFeeGroup": 2345,  
    "recurringFeeGroup": 3456  
  }  
}  
'
```

#### Response

A successful response will return a HTTP 200 response code and the following response:

[Copy](javascript:void(0);)

JSON

```
{  
    "limitsGroup": 3368,  
    "usageGroup": 374,  
    "recurringFeeGroup": 3456,  
    "webServiceFeeGroup": 1234,  
    "authFeeGroup": 2345,  
    "mccGroup": 0,  
    "cardLinkageGroup": 0,  
    "calendarGroup": 0,  
    "fxGroup": 0,  
    "paymentTokenUsageGroup": 0,  
    "cardAcceptorAllowList": 1,  
    "cardAcceptorDisallowList": 1   
}
```

### 7.1.3 Listing Card Transaction Fees

You can use the [Get card Transaction API](https://cardsapidocs.thredd.com/reference/get-card-transactions) to retrieve details of card transactions, including fees, over a defined period.

We recommend you use the EHI data feed for viewing details of your fees. Using the Thredd API to query card fees may incur additional charges. Please ensure you abide by the Thredd Fair Usage Policy for Thredd API (refer to your Letter of Intent or Contract).

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

JSON

```
curl --request GET \  
     --url 'https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/12345677/transactions?fromDate=20240101&toDate=20240131' \  
     --header 'accept: application/json'
```

#### Response

[Copy](javascript:void(0);)

JSON

```
[  
    {  
        "id": 6160502008,  
        "description": "string",  
        "dateTime": "2024-02-20T14:16:18.34Z",  
        "lifeCycleId": null,  
        "type": {  
            "code": "U",  
            "description": "Unload"  
        },  
        "status": {  
            "code": "S",  
            "description": "Settled"  
        },  
        "amount": {  
            "billingValue": 50.00,  
            "billingCurrency": "GBP",  
            "transactionValue": 50.0000,  
            "transactionCurrency": "GBP",  
            "settlementAmount": 50.00,  
            "settlementCurrency": "GBP",  
            "actualBalance": 1950.00,  
            "availableBalance": 1950.00  
        },  
        "fees": {  
            "id": 0,  
            "fixedFee": 0.05,  
            "rateFee": 0.00,  
            "fxPadding": 0.00,  
            "mccPadding": 0.00  
        },  
        "productId": 10023,  
        "cardNetwork": "MASTERCARD",  
        "processingCode": "230000",  
        "recordId": 0,  
        "note": "API Load by ",  
        "systemTraceAuditNumber": 0,  
        "transactionCountry": "GBR",  
        "transactionLink": 6160502008,  
        "additionalDetail": null,  
        "paymentTokenId": null,  
        "paymentMethod": "None"  
    }  
  ]
```

#### Notes

The Fee amount =

[Copy](javascript:void(0);)

```
},  
        "fees": {  
            "id": 0,  
            "fixedFee": 0.05,  
            "rateFee": 0.00,  
            "fxPadding": 0.00,  
            "mccPadding": 0.00  
        },
```

You can use the processing code (DE003) and note to determine the source of the fee:

Transaction-related fees are listed in your daily XML transaction report and in real-time EHI messages. Transaction-related fees can also be viewed on Thredd Portal and Smart Client.

### 7.1.4 Add One-off Fee

Use the [Load or Unload Card](https://cardsapidocs.thredd.com/docs/loading-unloading-a-card) endpoint to apply one-off fees to a card by setting the transactionType field to `Fee` in the request body. When the transactionType is set to `Fee`, the following fields must be included in the request.

* currencyCode
* feeAmount
* feeType

The following example displays the payload of a fee of Â£20 for transferring funds.

[Copy](javascript:void(0);)

```
{  
  "transactionType": "Fee",  
  "feeType": "FundsTransferFee",  
  "currencyCode": "GBP",  
  "feeAmount": 20  
}
```

If successful, a 200 response is returned with details of the transaction and the updated balance on the card.

[Copy](javascript:void(0);)

```
{  
    "transaction": [  
        {  
            "transactionType": "Fee",  
            "transactionId": 6161692763,  
            "amount": 20,  
            "currencyCode": "GBP",  
            "publicToken": "116611859"  
        }  
    ],  
    "balance": {  
        "currencyCode": "GBP",  
        "cardBalance": 910,  
        "pendingAmount": 0,  
        "availableBalance": 910  
    }  
}
```

The following table describes each of the fee types available.

| Fee Type | Description |
| --- | --- |
| undefined | An undefined fee. |
| FundsTransferFee | Bank Transfer. |
| PINCVVServiceFee | Service Fee for PIN and CVV. |
| MonthlyServiceFee | Monthly Service Fee. |
| ReloadFromMVCFee | MVC Load. |
| CardConversionFee | Card Conversion Fee. |
| PhysicalCardIssuingFee | Card Issue Fee (Physical). |
| AdministrationFee | Administration Fee. |
| CardReplacementFee | Card Replacement Fee. |
| VirtualCardIssuingFee | Card Issue Fee (Virtual). |
| ParentCardActivationFee | Primary Card Activation Fee. |
| ChildCardActivationFee | Secondary Card Activation Fee. |
| FirstLoadFromMVCFee | First Load from MVC. |
| RecurringFee | Recurring Fee. |