# Release Notes for 12 August 2022

New changes to the GPS Cards API for the week ending 12th August 2022.

* [Added Update Card Control Overrides Endpoint](#added-update-card-control-overrides-endpoint)
* [Added Get Card Control Overrides Endpoint](#added-get-card-control-overrides-endpoint)
* [Added Contactless Purchase Transactions Endpoint](#added-contactless-purchase-transactions-endpoint)

## Added Update Card Control Overrides Endpoint

The **Update the Card Control Overrides** endpoint has been added to the REST API. This enables you to update control overrides for a card, such as whether the card can be used for contactless payments.

<Image align="center" className="border" border={true} src="https://files.readme.io/5956a59-Screenshot_2022-08-17_130953.png" />

## Added Get Card Control Overrides Endpoint

The **Get Card Control Overrides** endpoint has been added to the REST API. This enables you to retrieve the current control overrides for a card, displaying the status of each of the different overrides available.

## Added Contactless Purchase Transactions Endpoint

The **Contactless Purchase Transactions** endpoint has been added to the REST API. This enables a cardholder to perform contactless payments through an API, rather than through CTS. For more details on how this endpoint works, see [Contactless Purchase Transaction](https://cardsapidocs.thredd.com/docs/contactless-purchase-transaction).

> 📘 Example
>
> See below for an example of the body created in API Explorer. Navigate to [Perform contactless purchase transaction](https://cardsapidocs.thredd.com/reference/post_api-pos-contactlesspurchase) to try the endpoint in the API Explorer.

![](https://files.readme.io/f6f9768-Screenshot_2022-08-17_133629.png "Screenshot 2022-08-17 133629.png")