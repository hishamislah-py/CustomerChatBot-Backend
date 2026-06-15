# Release Notes for 7 July 2023

New changes to the Thredd Cards API for the week ending 7th July 2023.

* [logoFrontId and logoBackId now optional](#logofrontid-and-logobackid-now-optional)
* [Declined transactions now returned in Get Card Transactions](#declined-transactions-now-returned-in-get-card-transactions-endpoint)
* [ Update to Card Status behaviour](#update-to-card-status-behaviour)
* [ALL credential type disabled in Create 3DS Credentials endpoint](#all-credential-type-disabled-in-create-3ds-credentials-endpoint)
* [Chatbot added to Cards API documentation](#chatbot-added-to-cards-api-documentation)
* [Bug Fixes](#bug-fixes)

## logoFrontId and logoBackId now optional

The `logoFrontId` and `logoBackId` fields are now optional in the Create Card endpoint.

## Declined transactions now returned in Get Card Transactions endpoint

Transactions that have been declined now return in the response of the Get Card Transactions endpoint.

## Update to Card Status behaviour

When creating a new card without immediately activating the card (using the `ActivateNow` field), the card will now be set to 02 (Not Activated). Previously cards would be set to 00.

**Note:** This change is specific to Product environment, which has been changed to match the behaviour of the UAT environment.

## ALL credential type disabled in Create 3DS Credentials endpoint

When using the `ALL` credential type in the Create 3DS Credentials endpoint to create a new 3DS credential, a 422 Unprocessable Entity response will be returned with the following message:

```json
{
    "type": "https://tools.ietf.org/html/rfc4918#section-11.2",
    "title": "One or more validation errors occurred.",
    "status": 422,
    "traceId": "00-14140056a3ec5bbf1c685f6159d28925-821039d88dcabe4a-00",
    "errors": {
        "": [
            "Type 'ALL' is not supported for creation of credentials"
        ]
    }
}
```

## Chatbot added to Cards API documentation

An AI-powered chatbot has been added to the Cards API documentation, enabling users to ask questions and return intelligent answers. Use the **Ask a question** field in the top-right corner of the Cards API documentation to ask a question.

For example, asking the question "How do I find a product ID?" will return the following response from the chatbot.

<Image align="center" className="border" border={true} src="https://files.readme.io/ba736cd-Screenshot_2023-07-05_131958.png" />

## Bug Fixes

The following bug fixes have been made for this release:

* A bug where the ActivateNow field was not working in the Create Card endpoint has been fixed in this release.
* Updated Create Card and Update Card endpoints in the Postman Collection to correct an issue with the nameOnCard endpoint being incorrectly placed in the example body.