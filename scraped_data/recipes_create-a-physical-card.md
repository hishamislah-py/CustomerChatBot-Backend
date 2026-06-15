# Create a Physical Card

```curl cURL
curl --request POST \
     --url https://cardsapi-uat.globalprocessing.net/cards \
     --header 'Accept: application/ json' \
     --header 'Authorization: Bearer APIKEY' \
     --header 'Content-Type: application/json'
{
    "CardType":"Physical",
    "CardProduct": 10023,
    "CustomerReference": "CustNo12345A",
    "CardHolder": {
        "Title": "Mrs.",
        "FirstName": "Jane",
        "LastName": "Doe",
        "DateOfBirth": "1982-02-19",
        "Mobile": "07755123456",
        "Email": "jdoe@email.com"
    },
    "Address": {
        "AddressLine1": "1007",
        "AddressLine2": "Mountain Drive",
        "AddressLine3": "string",
        "City": "Gotham",
        "County": "New Jersey",
        "PostCode": "GC11 2LD",
        "Country": "USA"
    },
    "fulfilment": {
          "addressLine1": "32 Metropolis Ave",
          "city": "Gotham",
          "country": "USA",
          "county": "Gothamshire",
          "postCode": "GC11 3GH"
     },
     "ManufacturingDetails":
     {
       "CardManufacturer": "AB Note",
        "DeliveryMethod": 0,
        "CarrierType": "Type 1",
        "Quantity": 1,
        "Language": "HU",
        "ThermalLine1": "asdeoivh2neriuvnqkr",
        "ThermalLine2" : "asjkfnkerjnkwe",
        "EmbossLine4" : "jdwncwlkejr",
        "VanityName" : "Name Mane",
             "ImageDetails":
             {
                  "ImageId": "An image id",
                  "LogoFrontId" : "A logo ID",
                  "LogoBackId": "Another logo ID"
             }
    }




}
```

```json Response Example
{
    "publicToken": "107691132",
    "customerReference": "CustNo12345A",
    "embossName": "Mrs. Jane Doe",
    "maskedPan": "999999******8405",
    "startDate": "2022-08-25",
    "expiryDate": "2023-08-31"
}
```

# Get an Authentication Token

<!-- curl@4 -->

Before you can run the endpoint, you will need to have a valid authentication token. This token is used to access Thredd systems and must be included as part of the header.

# Set the Card Type, Product and Customer Reference

<!-- curl@7-9 -->

As well as setting the card type as "Physical", you also need to include a cardProduct and customerReference field in the body. The cardProduct field is an ID specific to your company and is shared with you as part of the Thredd implementation process. 

The customerReference field stores an ID from your system to act as a foreign key between the system and Thredd platform.

# Add the Cardholder Details

<!-- curl@10-17 -->

In this example, the details for a Mrs Jane Doe are added as the cardholder details for the new card. This must include her title, first name and last name in the appropriate fields. Additionally, you can also add her date of birth, mobile and email.

# Add the Address

<!-- curl@18-26 -->

In this example, the address details for Mrs Jane Doe are added to the new card. The addressLine1, city and country are all required fields.

# Add the Fulfilment Address

<!-- curl@27-33 -->

As the card requested by the customer is physical, a fulfilment address needs to be supplied in the body. This is the address that your designated card manufacturer will send the card to. The body must include addressLine1, city, postCode and country.

# Add the Manufacturing Details

<!-- curl@34-51 -->

Physical cards require the body to include details for the manufacturing process. The fields cardManufacturer, deliveryMethod and carrierType are all required fields.

# Send Request and Receive Response



After the body for the request has been completed and it's sent to the URL, a response is provided. This consists of several elements, but the most important is the publicToken. This is the unique identifier for the card and is used in other endpoints, such as loading currency onto a card, or renewing a card.