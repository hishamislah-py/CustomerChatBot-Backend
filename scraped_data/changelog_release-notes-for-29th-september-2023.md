# Release Notes for 29th September 2023

New changes to the Thredd Cards API for the week ending 29th September 2023.

## Changed behaviour when performing Balance Adjustment behaviour for Card Status 63

The behaviour for cards with the status of 63 (Security Violation) has been changed so that they are now restricted from being able to perform a balance adjustment using the Transactions endpoint. Previously there was no restriction on being able to do this.

> 👍 Documentation
>
> For more information, see [Card Status Codes](https://cardsapidocs.thredd.com/docs/card-status-codes).

## Field length validation added for Create Card endpoint

The following fields have had field length validation added in the Create Card endpoint:

* customerReference
* language (from the manufacturingDetails object)

Exceeding this value will return a 422 response with a message detailing that the field length is too long.

<Image align="center" className="border" border={true} src="https://files.readme.io/a7c9714-image.png" />

## Automatic balance adjustment when cards are updated to statuses 98 and 99

When using the Update Card Status endpoint and changing the card status code to either 98 (Refund to customer)or 99 (card voided), the card balance will be automatically adjusted to 0.00. This is to match the behaviour when using our SOAP Web Services.

> 👍 Documentation
>
> For more information, see [Card Status Codes](https://cardsapidocs.thredd.com/docs/card-status-codes).