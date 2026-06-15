# Create Bulk Physical Cards - Field Descriptions

The following page details each of the fields received in the response when using the Create Bulk Physical Cards endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when creating bulk physical cards.

| Field                 | Description                                                                                                      | Minimum Length | Maximum Length | Type    | Mandatory |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------- | :------------- | :------------- | :------ | :-------- |
| cardProduct           | The unique ID of the card product linked to the card.                                                            | 1              | 255            | Integer | Yes       |
| quantity              | The number of cards to be created.                                                                               | 1              | 1000           | Integer | Yes       |
| nameOnCard            | Name embossed on card. This name will be applied to every card created.                                          | 0              | 26             | String  | No        |
| imageId               | The image ID used for every card created.                                                                        | 0              | 16             | String  | No        |
| deliveryMethod        | The delivery method for every card created.                                                                      | 0              | 21             | String  | No        |
| **fulfilmentAddress** | An object that contains information for the fulfilment address.                                                  |                |                |         |           |
| addressLine1          | First line of the address.                                                                                       | 1              | 100            | String  | Yes       |
| addressLine2          | Second line of the address.                                                                                      | 0              | 100            | String  | No        |
| addressLine3          | Third line of the address.                                                                                       | 0              | 100            | String  | No        |
| city                  | City name.                                                                                                       | 0              | 100            | String  | No        |
| county                | The county, region or province.                                                                                  | 0              | 100            | String  | No        |
| postcode              | Postcode / zip code of the address.                                                                              | 0              | 10             | String  | Yes       |
| country               | Country of residence. This is represented as a 3-letter alphanumeric ISO country code (For example, GBR for UK). | 3              | 3              | String  | Yes       |

<br />

## Response Fields

If successful, a 202 response returns with the batch request id included.