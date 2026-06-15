# Release Notes for 19th January 2024

New change to the Thredd Cards API for the week ending 19th January 2024.

* [Cards can no longer be converted if not active](#cards-can-no-longer-be-converted-if-not-active)
* [Quantity field removed from the Create Card endpoint](#quantity-field-removed-from-the-create-card-endpoint)

## Cards can no longer be converted if not active

Cards can now no longer be converted from physical to virtual (using the [Convert Card](https://cardsapidocs.thredd.com/reference/convert-card) endpoint) unless the card has an active (00) status. If the status of the card is not active, an error message will be returned.

## Quantity field removed from the Create Card endpoint

The Quantity field, part of the ManufacturingDetails object, has been removed as of this release.