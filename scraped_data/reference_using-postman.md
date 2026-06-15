# Using Postman

This section provides an introduction to using the Thredd REST API collection in Postman.

## Prerequisites

* Download and install the Postman app. See [Download Postman](https://www.postman.com/downloads/).
* Download the latest Thredd REST API Collection (available on the [API Explorer](https://cardsapidocs.thredd.com/reference/introduction-1) page).
* Contact Thredd to request secure access and/or allow access from your static IP address.

## Install the Thredd Postman Collection

1. Open Postman.
2. Click the **Import** button. A window will open.
3. Navigate to the directory where the collection is saved and select the Thredd REST API file \_Thredd*Rest\_API\_External\_postman\_collection.json*. The collection will display in Postman.

## Use the Postman Collection

The Thredd REST API collection appears in the left-hand column of your Postman workspace.

### Generate the OAuth Token

Generation of the OAuth token is done at the top level of the collection so you only need to authorise a token once.

1. Select the **ThreddREST API External Postman** collection.

![](https://files.readme.io/88bfb19-Stable_Postman_Collection.png)

2. Click **Get New Access Token** button in the Authorization tab.

![](https://files.readme.io/ad703c5-Get_New_Access_Token_button.png)

3. Click **Proceed**, then click **Use Token**.

The token will be applied to every endpoint in the collection.

### Create a Card

1. Select the **CreateCard** API endpoint.
2. Select the **Body** tab and enter the details of the card, replacing the example values with your required details.
3. Click **Send**.\
   Thredd returns a 200 Ok response, containing the public token, as shown in the example below.

```json Example Create Card response
{
    "publicToken": "102759761"
}
```

The public token provides a unique identifier for your card. You can use this public token in all subsequent requests related to the card.

### Apply publicToken as a Variable

Almost all endpoints are set up to use the publicToken set in the Variables tab of the collection. To set the publicToken variable:

1: Select the **Variables** tab in the Thredd REST API External Postman collection.

![](https://files.readme.io/5983d34-Stable_Variables.png)

2: Enter the publicToken you want to use in the Initial Value and Current Value columns.

3: Click **Save**.

![](https://files.readme.io/571476c-SaveVariables.png "SaveVariables.png")

The collection is saved. All endpoints will use the variable and run using the set publicToken.

### Retrieve the Details of a Card

1. Select the **Retrieve a Card** API endpoint.
2. If required, generate a new access token.
3. Click **Send**.

Thredd returns a 200 Ok response, containing details of the card linked to the public token, as shown in the example below.

```json Example Retrieve Card Endpoint response
{
    "cardType": "Physical",
    "publicToken": "105284447",
    "status": "Inactive",
    "balance": {
        "currencyCode": "GBP",
        "cardBalance": 0,
        "pendingAmount": 0,
        "availableBalance": 0
    },
    "cardDetails": {
        "customerReference": "CustNo12345A",
        "fullNameOnCard": "Mr. John Bloggs",
        "maskedPan": "999999******3631",
        "pan": "9999999985643631",
        "startDate": "2022-06-06",
        "expiryDate": "2023-06-30"
    },
    "cardHolder": {
        "title": "Mr.",
        "firstName": "John",
        "lastName": "Bloggs",
        "dateOfBirth": "1982-02-19",
        "mobile": "07755123456",
        "email": "JBloggs@email.com"
    },
    "cardProduct": {
        "scheme": "SCHEME TEST",
        "product": 10023
    },
    "controlGroups": {
        "limitsGroup": 1051,
        "usageGroup": 374,
        "recurringFeeGroup": 0,
        "webServiceFeeGroup": 0,
        "authFeeGroup": 0,
        "mccGroup": 0,
        "cardLinkageGroup": 0,
        "calendarGroup": 0,
        "fxGroup": 0,
        "paymentTokenUsageGroup": 0
    },
    "3DS": [],
    "designId": "PMTREST"
}
```