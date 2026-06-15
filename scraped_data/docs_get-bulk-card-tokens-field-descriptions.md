# Get Bulk Card Tokens - Field Descriptions

The following page details each of the fields received in the response when using the Get Bulk Card Tokens endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when getting bulk card tokens.

| Field             | Description                                               | Type    | Minimum Length | Maximum Length | Mandatory |
| :---------------- | :-------------------------------------------------------- | :------ | :------------- | :------------- | :-------- |
| bulkCardRequestId | The bulk card request identifier.                         | Integer | 1              | 2147483647     | Yes       |
| pageNumber        | The page number of the response.                          | Integer | 1              | 2147483647     | Yes       |
| pageSize          | Determines the amount of tokens returned in the response. | Integer | 1              | 2147483647     | Yes       |

## Response Fields

The following table describes the field included in the response after successfully getting bulk card tokens.

| Field      | Description                                                                        |
| :--------- | :--------------------------------------------------------------------------------- |
| tokens     | The unique public tokens created as part of the Create Bulk Physical Card request. |
| pageNumber | Number of the current page.                                                        |
| total      | Total number of cards created.                                                     |
| pageSize   | The amount of public token displayed on each page.                                 |