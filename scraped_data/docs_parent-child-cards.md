# Primary and Secondary Cards

Primary and Secondary cards are two types of cards that are linked to each other. Both cards are used on their own in e-commerce and in-store transactions. However, the holder of the Secondary card typically depends on the funds from the Primary card holder.

> 📘 Note:
>
> Primary and Secondary cards are also referred to as Parent and Child cards.

Note that, with the exception of the Create Card endpoint, using the endpoints below require the `PublicToken` in the path. For example, you need the `PublicToken`  for a card replacement.

```json Example Card Replacement endpoint
https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/{PublicToken}/complete-replacement
```

## Before you Create the Secondary Cards

Before you create Secondary cards, you need to ensure the following:

* The product for creating the Primary and Secondary cards is set up with a Card Linkage group to ensure that the Secondary card(s) and the Primary card can be linked. The Card Linkage group also specifies whether the balance is separate or is shared.
* The product allows a virtual or physical card. If it is for a virtual card, the product must also allow conversion to a physical card.

When you've ensured that the correct settings exist for the product, you then create the Primary card.

Note that the Card Linkage group and the virtual card settings would been set up for you through Smart Client.

## Creating a Secondary Card

You use the [Create Card](/reference/create-card) endpoint to create one or more Secondary cards. You should ensure that the  `parentCard` field is populated with the publicToken of the Primary card in the request.

```json Example Create a Card request

{
  "cardType": "Physical",
  "cardProduct": "443",
  "designId": "New Card Brand",
  "customerReference": "CustNo12345A",
  "parentCard": "123456789",
  "cardHolder": {
         "title": "Mr",
         "firstName": "Jon",
         "lastName": "Smith",
         "dateOfBirth": "1982-11-03"
   },
   "address": {
          "addressLine1": "32 Western Drive",
          "postCode": "S25 2BZ",
          "country": "GBR"
   },
}
```

The response includes the *publicToken* of the Secondary card in the `publicToken` field.

```json Example Create a card response
{
  "publicToken": "5678901234",
  "customerReference": "sales",
  "embossName": "Joseph Bloggs",
  "maskedPan": "123456******3456",
  "startDate": "2022-06-06",
  "expiryDate": "2025-06-06"
}
```

## Managing the Balance

You can adjust the balance between Primary and Secondary cards where the balance is shared. Sharing the balance allows the holder of the Primary card to have more control over funds in the Secondary card. Keeping the balances separate allows the holder of the Secondary card to manage funds more independently.  The capability of sharing the balance is determined by the `cardLinkageGroup` and the `limitsGroup`, which you would have set in Smart Client for the product.

### Direct Funding of a Secondary Card

Balance management also enables the direct funding of a secondary card, allowing authorisations on a Secondary card to be approved by the Primary card's balance. This makes it useful in scenarios where there is not enough funds on the Secondary card, such as when its balance is zero.

## Converting the Card Type

If you have created a Secondary card that is virtual, you can convert it to a physical card. You would have used the [Create Card](/reference/create-card) endpoint to create one or more Secondary cards with the `cardType` as `Virtual`. You then do the following:

1. Use the [Update card status](/reference/update-card-status) endpoint to change the `cardStatusCode` to `00`. The `00` `cardStatusCode` is for a physical card.
2. Convert to a physical card through the [Convert Card](/reference/convert-card) endpoint. Although not mandatory, you can include an expiry date if this exists on the Primary card. To include an expiry date, you set the `moveExpiryDate` parameter to `true` (as shown in the below example). This ensures that the expiry date is the same as the physical Primary card.

```json Example Update Card Status request
{
  "cardStatusCode": "00",
  "status": "Active",
  "updatedBy": "Ken",
  "description": "Card reported lost by customer",
  "validityDate": "2023-12-06T12:59:11.929Z"
}
```

```json Example Convert Card request
{  
  "cardType": "Physical",  
  "moveExpiryDate": true
}
```

More information on converting virtual to physical cards is described in the  [Converting a Card from Virtual to Physical](https://cardsapidocs.thredd.com/docs/converting-a-card) endpoint description.

## Renewing and Replacing Cards

You can renew both virtual and physical Secondary cards. Renewing a card is useful if you want to change the expiry date. A card must be in a valid state before renewal. Invalid card statuses include:  LostCard (41), StolenCard (43), CardDestroyed (83) and CardVoided (99).

Alternatively, you can replace a Primary or Secondary card in situations where a new card is needed. For example, their original card is lost. When replacing a Primary card, you need to transfer one or more Secondary cards to the new Primary.

### Renewing a Card

Use the [Renew a card](/reference/renew-card) endpoint to send the following example request.

```json Example Renew a Card request
{  
  "renewStep": "Renew",  
}
```

### Replacing a Primary Card

Using a Balance Limit Child Cards (BLC) transfer request, you set `moveChildCards` to `true` for each Secondary card of the Primary. The BLC transfer performs dedicated operations to ensure that you can use old card data on the replaced card.

You use the [Complete a Card Replacement](/reference/complete-card-replacement) endpoint for the BLC transfer request as shown in the following example:

```json Example Complete a Card Replacement request
{
  "moveBalance": true,
  "moveLimitAccumulators": true,
  "moveChildCards": true,
  "moveExpiryDate": true,
  "expiryDate": "2024-01-26T18:17:31.735Z"
}
```

### Replacing Secondary Cards

For replacing Secondary cards, you use the [Replace a Card ](/reference/replace-card) endpoint.  When replacing Secondary cards, you set `moveChildCards` to `false`.

```json Example Replace a Card request
{
  "moveBalance": true,
  "moveLimitAccumulators": true,
  "moveChildCards": false,
  "moveExpiryDate": true,
  "expiryDate": "2024-01-25T17:27:20.644Z",
}
```

The [Update Card Status](/reference/update-card-status) endpoint lets you change the card status from inactive to active once replaced.

```json Example Update Card Status request
{
  "cardStatusCode": "00",
  "status": "Active",
  "updatedBy": "Ken",
  "description": "Card reported lost by customer",
  "validityDate": "2024-01-25T17:17:36.406Z"
}
```

## Changing Control Groups

You can update the Control groups that exist on both the Secondary and Primary cards. This enables the Secondary card to have specific restrictions, which may/may not depend on the restrictions of the Primary card.  Similarly, the Primary card can have restrictions that are different from the Secondary card.

You use the [Update Card Control Groups](/reference/update-card-control-groups-1) endpoint to change the control group for a card. In the below example, you add the authorisation fee, Merchant Category Code (MCC), and limit groups to the Secondary card.

```json Example Update Card Control Groups request
{
  "controlGroups": {
    "limitsGroup": 1,
    "usageGroup": 0,
    "recurringFeeGroup": 0,
    "webServiceFeeGroup": 0,
    "authFeeGroup": 1,
    "mccGroup": 1,
    "cardLinkageGroup": 0,
    "calendarGroup": 0,
    "fxGroup": 0,
    "paymentTokenUsageGroup": 0,
    "cardAcceptorAllowList": 0,
    "cardAcceptorDisallowList": 0
  }
}
```