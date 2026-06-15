# Validate Customisable Card Number - Field Descriptions

The following page details each of the fields received in the response when using the Validate Customisable Card Number endpoint.

## Header

| Description      | Type                                                                                                                                           | Status |           |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :-------- |
| X-Correlation-ID | A GUID, which is used to identify a card creation flow. Please use the same correlation ID for customised card number validation and creation. | String | Mandatory |

## Request Fields

The following table describes fields that can be included in the body of the request when validating a customisable card number.

| Field          | Description                                                       | Minimum Length | Maximum Length | Type    | Mandatory |
| :------------- | :---------------------------------------------------------------- | :------------- | :------------- | :------ | :-------- |
| productId      | The unique ID of the card product linked to the card.             | 1              | 2147483647     | integer | Yes       |
| customPan      | Last six digits of the card number used as a custom PAN.          | 6              | 6              | string  | Yes       |
| **panOptions** | Object that contains secondary Custom PAN options.                |                |                |         | Yes       |
| id             | The unique identification number of each secondary option.        | 1              | 2147483647     | integer | Yes       |
| pan            | Last six digits of the card number for the secondary option used. | 5              | 5              | string  | Yes       |

## Response Fields

A successful response for the Validate Customisable Card Number endpoint will return a 200 response.

| Field            | Description                                                                                            |
| :--------------- | :----------------------------------------------------------------------------------------------------- |
| customPan        | Last 4 digits of the card number used as a custom PAN.                                                 |
| isCustomPanValid | Indicates whether the given Custom PAN is valid or not.                                                |
| referenceNumber  | A unique random number used as a reference for the Custom PAN.                                         |
| **panOptions**   | Object that displays secondary options, Only available when the customPan in the request is not valid. |
| id               | The unique identification number of each secondary option, same as that in the request.                |
| pan              | Last 4 digits of the card number for the secondary option used.                                        |
| referenceNumber  | A unique random number used as a reference to the secondary options.                                   |