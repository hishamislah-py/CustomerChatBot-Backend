# Release Notes for 25th June 2024

New changes to the Thredd Cards API coming on the 25th June. These include:

* [New Fields Added to Retrieve Card endpoint](#new-fields-added-to-retrieve-card-endpoint)
* [Update to groupType in List Card Control Groups endpoint](#update-to-grouptype-in-list-card-control-groups-endpoint)
* [Fixed Issue with Create Bulk Cards endpoint](#fixed-issue-with-creat-bulk-cards-endpoint)

## New Fields Added to Retrieve Card endpoint

Two new fields have been added to the Retrieve Card endpoint. cardAcceptorAllowList and cardAcceptorDisallowList are included in the controlGroups object and return the cardAcceptorAllowList and cardAcceptorDisallowList identifiers the card is associated with. This enables you to see what card acceptor groups the card is associated with.

The below example shows a Retrieve Card response with the new fields included.

```json Example Retrieve Card Response
{
  "cardType": "Virtual",
  "publicToken": "4321567890",
  "status": "Active",
  "cardStatusCode": "00",
  "cardStatusDescription": "00 (Active)",
  "balance": {
    "currencyCode": "GBP",
    "cardBalance": 1000,
    "pendingAmount": 0,
    "availableBalance": 1000
  },
  "cardDetails": {
    "customerReference": "string",
    "fullNameOnCard": "string",
    "maskedPan": "string",
    "startDate": "string",
    "expiryDate": "string",
    "clearPan": "string",
    "cvv": "string",
    "activationDate": "string",
    "gpsExpiryDate": "string"
  },
  "cardHolder": {
    "title": "Mr",
    "firstName": "John",
    "middleName": "string",
    "lastName": "Smith",
    "dateOfBirth": "1963-11-22",
    "mobile": "07471234567",
    "email": "john.smith@example.com"
  },
  "cardProduct": {
    "scheme": "Example Scheme",
    "product": 45,
    "productShortName": "string",
    "ehiMode": 2
  },
  "controlGroups": {
    "limitsGroup": 0,
    "usageGroup": 0,
    "recurringFeeGroup": 0,
    "webServiceFeeGroup": 0,
    "authFeeGroup": 0,
    "mccGroup": 0,
    "cardLinkageGroup": 0,
    "calendarGroup": 0,
    "fxGroup": 0,
    "paymentTokenUsageGroup": 0,
    "cardAcceptorAllowList": 0,
    "cardAcceptorDisallowList": 0
  },
  "3DS": [
    {
      "configuration": "string",
      "defaultCredentials": [
        {
          "type": "OTPSMS",
          "value": "07723849948",
          "id": 0
        }
      ],
      "fallbackCredentials": {
        "type": "OTPSMS",
        "value": "07723849948",
        "id": 0
      }
    }
  ],
  "designId": "string",
  "parentCard": 987654321054321,
  "childCards": [
    0
  ],
  "siblingCards": [
    987654322454321,
    987651221054320
  ],
  "address": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "state": "string",
    "county": "string",
    "postCode": "string",
    "country": "string"
  },
  "fulfilment": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "state": "string",
    "county": "string",
    "postCode": "string",
    "country": "string"
  },
  "freetext1": "string",
  "freetext2": "string",
  "isSingleUse": true,
  "isNonReloadable": true,
  "cardAcceptorIds": {
    "allowCardAcceptors": [
      "string"
    ],
    "disallowCardAcceptors": [
      "string"
    ]
  },
  "language3ds": "string",
  "programManagerID": 0,
  "programManagerCode": "string"
}
```

<br />

## Update to groupType in List Card Control Groups endpoint

The groupType field, returned in the response for the List Card Control Groups endpoint, has been updated to return as an integer, not a string.

## Fixed Issue with Create Bulk Cards endpoint

A fix has been made to the Create Bulks Cards endpoint in this release to resolve an issue where requests would incorrectly fail if they were shorter than the request frequency limit.