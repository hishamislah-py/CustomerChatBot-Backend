# Renew Card - Field Descriptions

The following page details each of the fields received in the response when using the Renew Card endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when converting a card.

| Field     | Description                                                                                                                  | Minimum Length | Maximum Length | Type   | Mandatory |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------- | :------------- | :----- | :-------- |
| renewStep | Flag to denote what step the user is taking in the renewal process. Select from `Renew`, `Migrate `or `RenewWithSameExpiry`. | 5              | 19             | String | No        |
| freetext1 | Additional fulfilment data used for transferring extra information to the card manufacturer.                                 | 0              | 50             | String | No        |
| freetext2 | Additional fulfilment data used for transferring extra information to the card manufacturer.                                 | 0              | 50             | String | No        |

## Response Fields

A successful response for the Renew Card endpoint will return a 204 No Content status code. No fields are returned.