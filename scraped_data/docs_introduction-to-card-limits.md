# Introduction to Card Limits

Card velocity limits, also known as limit groups, restrict the frequency and/or amount at which a card can be used for transactions such as point of sale, contactless, ATM withdrawals and ecommerce. These limits help manage and control the usage of the card to prevent excessive or unauthorized transactions.

> 📘 Note
>
> The Limit Group assigned to the Card and the Limit Group assigned to the Card Product at Thredd must be same. If the card’s Limit Group is different from the product’s Limit Group, the product’s Limit Group would be considered for limits check by Thredd. To avoid this, use the Set Card Limits endpoint to set card limits instead of assigning a different limit group to the card.

## Setting up Card Limits at a Product Level

To set up card velocity limits at card product level, you would configure these within your card program settings.  These limits can be tailored to restrict the frequency and amount of transactions, ensuring better control over card usage. These limits are listed on your Product Setup Form (PSF) and then configured by your Implementation Manager for your programme on the Thredd Platform.

## Linking a card to a Card Limit Group

When creating the card record, the card will automatically be linked to the card product (`cardProduct `field) you specified in your request (and the card usage groups for that product).  See [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

You can use the Update Card Control Groups API to change the card control groups linked to a specified card. See  [Managing Card Control Groups](https://cardsapidocs.thredd.com/docs/card-controls).

## Viewing Card Limits  (Product Level)

The Get Limits API enables you to view the card limits set at a product level. These are generic card limits that apply to all cards associated with this product. See [Get Card Limits (Product Level)](https://cardsapidocs.thredd.com/docs/get-card-limits).

## Setting Card Limits  (Card Level)

The Set Card Limits API enables you to set the card limits for a specific card. These card-level limits will override the generic card limits for the card product. See [Set Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/set-card-limits).

## Viewing Card Limits  (Card Level)

The Get Card Limits API enables you to view the override card limits set for a specific card (which were set using the Set Card Limits API). See [Get Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific).

## Contactless Limits FAQs

The following section describes FAQs related to using the Contactless Limits endpoints.

### Q: What is the Contactless Limit feature?

The Contactless Limits feature at Thredd allows issuers to set daily contactless spend limits for their cards. Issuers can also retrieve details of the spend limits already set using the Set Contactless Limits endpoint. See [Set Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/set-card-limits) for more information.

### Q: Do issuers control the refresh of the daily limit? When is this limit refreshed each day?

The daily limit is refreshed automatically at Thredd after midnight, based on the timezone configured by the client for their card product.

### Q: Can the issuer or cardholder change the daily spend limits multiple times in a day?

Yes, daily limits can be increased at any time during the day. Only the daily spend limit can be updated by the cardholder or issuer - not the daily limit counter at Thredd.

For example, if the cardholder sets the daily limit to 500 and spends 500 in a day, then increases the limit to 1000, the daily limit counter at Thredd is already 500, so the cardholder can spend an additional 500.

In another example, if the cardholder sets the daily limit to 500, spends 500, and then lowers the limit to 400, Thredd will return an error because the requested daily spend limit is lower than the current daily spend limit counter (500).

> 📘 Note
>
> The daily limit requested for the card must not exceed the card product’s daily limit.

### Q: In the Set Limits API, both the ‘POS’ category and ‘Contactless’ subcategory have configurable limits. Can these conflict? How are different daily limit values handled?

Both POS and Contactless limits can be configured separately. However, Contactless limits must be less than or equal to POS limits.

### Q: What are the default limits for all categories?

The default limit is the Group Limit of the card product. Issuers can retrieve existing limits by calling the [Get Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific) endpoint.

### Q: Are there any API usage or rate limits?

No, there are no usage or rate limits.

### Q: When using the Set Limits API, do we only set values for categories we want to change, or must we include all categories?

ll categories should be included in the request. You can update the required values and retain existing values by using those returned from the [Get Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific) endpoint.

### Q: When a user replaces or renews a card, how are their previous limits handled? Will the new card inherit these limits?

Limits are retained only if the card number remains the same. If the card number changes, it is treated as a new card and card limits are not transferred by default. However, product level limits  still apply.

### Q: For the Set Card Limit API, does the ‘Contactless’ subcategory require issuers to update the product configuration in the PSF?

In the PSF, issuers can update product and subcategory limits. Issuers or cardholders can use APIs to update card level limits. Product limits act as the parent limit, and card level limits set using the API cannot exceed product limits.

### Q: If a transaction is declined with RC61 - Exceed Amount Limit, can the user be prompted to enter their PIN to complete the transaction?

No, the transaction will be declined with a limit exceeded error. There is currently no fallback mechanism to prompt for a PIN.

### Q: How can issuers enable the contactless feature for their products at Thredd?

Issuers must submit a request to Customer Support and provide a list of products for which the feature should be enabled. This feature is not generally available for all clients.

### Q: How does the daily limit counter work at Thredd?

The daily limit counter is set automatically at Thredd. When a card is used to set contactless limits using the API for the first time, the transaction counter is reset to 0 (this is a current design limitation). After the limit is set, the counter updates based on card usage. The counter cannot be edited or reset manually, but issuers can view current usage by calling the [Get Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific) endpoint.

> 📘 Note
>
> The counter reset limitation applies only when limits are set using the API for the first time. Subsequent changes to the contactless daily limit counter is automatically reset at Thredd after midnight, according to the time zone set in the PSF.

### Q: Can the issuer enable or disable contactless limits using the Set Limits API?

Disabling and enabling contactless limits on a card is not in the scope of the Card Limit APIs. However, this can be achieved using the existing usage group control updates API available at Thredd.

To enable or disable contactless limits:

1. Request IMPS/Customer Support to create a usage group with the Contactless feature enabled for the card.
2. Use the Update Card Control Groups endpoint to update card to use the new `usageGroup `for the card. See [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) for more information.

<br />

<br />