# Card Acceptors

Acceptor lists enable you to control which merchants or merchant code are blocked or allowed to use your service. You can set up multiple acceptor lists and link cards to a list.

The Get Card Acceptor endpoint enables you to return the allow and disallow lists associated with a card.

You can retrieve the card acceptors for a card by making a GET request to the Get Card Acceptor endpoint. For example:

```json Example Get Card Acceptor endpoint
{{base-url}}/cards/{publicToken}/card-acceptor
```

A successful response will return a HTTP 200 response code. Below is an example response:

```json Example Get Card Acceptor response
{
	"cardAcceptorAllowList":
	{
		"id": 2323,
		"name":"TEST",
		"merchantIds":
		[
			"Merchant1",
			"Merchant2"
		],
	},
	"cardAcceptorDisallowList":
	{
		"id":23232,
		"name":"TEST2",
		"merchantIds":
		[
			"Merchant3",
			"Merchant4"
		],
	}
}
```

> 👍 API Explorer
>
> For more information, see [Get Card Acceptors](https://cardsapidocs.thredd.com/reference/returnllowdisallow-listed-cardcceptors-groupnd-merchants-under-the-group).