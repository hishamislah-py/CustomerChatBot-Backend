# Release Notes for 14 July 2023

New changes to the Thredd Cards API for the week ending 4th July 2023.

* [Get Full PAN endpoint added](#get-full-pan-endpoint-added)

## Get Full PAN endpoint added

\_*Endpoint: /cards/\{\{publicToken}}/showpan*

A Get Full PAN endpoint has been added for PCI compliant customers so they can retrieve a card's details with the full PAN exposed.

You can retrieve card details that include the full PAN by making a GET request to the Get Full PAN endpoint. For example:

```json Example Get Full PAN endpoint
{{base-url}}/cards/{{publicToken}}/showpan
```

A successful response will return an HTTP 200 response code with full details of the card, including a full PAN.

> 👍 Documentation/API Explorer
>
> * For more information on the Get Full PAN endpoint, see [Get Full PAN](https://cardsapidocs.thredd.com/docs/get-full-pan).
> * To try the Get Full PAN endpoint, navigate to [Get Full PAN](https://cardsapidocs.thredd.com/reference/retrieve-card-with-unmasked-pan) in API Explorer.