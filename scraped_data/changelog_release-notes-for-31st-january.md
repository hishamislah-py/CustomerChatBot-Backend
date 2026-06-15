# Release Notes for 31st January

The following change has been made to the Cards API:

## String Cleaning Added for Cardholder Details

String cleaning has been added to cardholder details when using the [Create Card](https://cardsapidocs.thredd.com/reference/create-card) and [Update Card](https://cardsapidocs.thredd.com/reference/update-card) endpoints. String cleaning deletes unpermitted characters from fields when they're submitted to the Cards API.

String cleaning is done for the following fields in the `cardholder` object:

* firstName
* middleName
* lastName

Any unpermitted characters included in the above fields are now removed before validating the max length limit. The value is saved if the length is within the limit. If it still exceeds, a 422 error is returned explaining the field has exceeded the max limit.

> 📘 Information
>
> For more information on these fields, see [Create Card - Field Descriptions](https://cardsapidocs.thredd.com/docs/create-card-field-descriptions) and [Update Card - Field Descriptions](https://cardsapidocs.thredd.com/docs/update-card-field-descriptions).