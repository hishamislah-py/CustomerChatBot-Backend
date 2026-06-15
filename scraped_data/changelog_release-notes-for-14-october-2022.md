# Release Notes for 14 October 2022

New changes to the GPS Cards API for the week ending 14 October 2022.

* [Card Replacement endpoint added](#card-replacement-endpoint-added)
* [Get Card Control Overrides or Defaults endpoint added](#get-card-control-overrides-or-defaults-endpoint-added)

## BLC Card Replacement endpoint added

A new endpoint has been added that enables you to transfer an old card Balance, Limit, and Child cards to a newly replaced card. This enables you to support a client where they want to move all of their details to a new card card.

You can use perform a BLC card replacement by making a PUT request to the endpoint. For example:

```json Example Card Replacement endpoint
https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/{PublicToken}/complete-replacement
```

The body of the request can have five fields included:

* **moveBalance** sets whether the balance should be transferred
* **moveLimitAccumulators** sets whether the card limits should be transferred
* **moveChildCards** sets whether any child cards should be transferred
* **moveExpiryDate** sets whether the current expiry date should be transferred
* **expiryDate** sets an expiry date on the card. This can only used instead of the **moveExpiryDate** option

For each of these a value of true or false can be set against the option. For example:

```json Example Card Replacement body
{
     "moveBalance": true,
     "moveLimitAccumulators": true,
     "moveChildCards": false,
     "moveExpiryDate": true
}
```

If successful, a 200 response will be returned. The publicToken for the card will remain the same but the card details associated with the token will be updated based on the settings selected in the body.

> 👍 Documentation
>
> For more information on this endpoint, see [BLC Complete Card Replacement](https://cardsapidocs.thredd.com/docs/get-card-replacement).

## Get Card Control Overrides or Defaults endpoint added

A new endpoint has been added that enables you to compare a card's control override settings with the default values. This allows you to directly compare the card's endpoints with the default values to see how they differ.

You can get a card's control overrides by making a GET request to the endpoint. For example:

```json Example Get Card Control Overrides or Defaults endpoint
https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/{publicToken}/controls
```

If successful, a 200 response is returned with each of the different overrides with details on the card's current override value and whether the card value has been overridden. For example:

```json Example Get Card Control Overrides or Defaults endpoint
{
  "usageControls": {
    "allowContactless": {
		"value": true,
		"isOverridden": false
	},
    "allowAtmWithdrawals": {
		"value": true,
		"isOverridden": true
	},
    "allowECommerceWhereCardNotPresent": {
		"value": true,
		"isOverridden": false
	},
    "allowRecurringPaymentWhereCardNotPresent": {
		"value": false,
		"isOverridden": false
	},
    "allowUseOutsideCountry": {
		"value": true,
		"isOverridden": false
	},
  }
}
```