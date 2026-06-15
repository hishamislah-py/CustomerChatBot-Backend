# Unbind Payment Token

The Unbind Payment Token endpoint enables you to remove a payment token from a device. You can do this by making a POST request to the Unbind Payment Token endpoint. For example:

```json Example Unbind Payment Token endpoint
{{base-url}}/cards/{{publicToken}}/payment-tokens/{{token-id}}/devices/unbind
```

The body of the request must specify the paymentTokenID associated with the payment token, as well as the deviceIndex. See below for an example body:

```json Example Unbind Payment Token body
{
"paymentTokenID": 123456,
"deviceIndex": 4
}
```

A successful response will return an HTTP 200 response code.

> 👍 API Explorer
>
> See the [Unbind a Device From a Token](https://cardsapidocs.thredd.com/reference/unbind-device-from-token) endpoint.