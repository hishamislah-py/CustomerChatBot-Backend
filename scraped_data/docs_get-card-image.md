# Get Card Image

<br />

The Get Card Image retrieves the card image configured on the Thredd platform, which can then be displayed to the cardholder. Card images are stored for both virtual cards and physical cards that have been converted from virtual cards. If the cardholder wants to see the image after card creation, you can regenerate the image by using this API.

> 📘 Note
>
> The Get Card Image endpoint must be enabled by Thredd for it to work. If you want to use the Get Card Image endpoint, contact Implementations.

You can retrieve the card image by making a GET request to the Get Card Image endpoint. For example:

```json Example Retrieve Card Image endpoint
{{base-url}}/cards/{{publicToken}}/image
```

A successful response will return a HTTP 200 response code and a base64 code that can be converted into an image.

```json Example Retrieve Card Image response
{
  "image": "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"
}
```

> 👍 API Explorer
>
> See the [Get Card Image](https://cardsapidocs.thredd.com/reference/get-card-image-1) endpoint for more information.

> 📘 Note
>
> Pretty Good Privacy (PGP) Keys are not supported in the REST API.

The base64 output can be used in a base64-to-image converter to display the image, such as [Code Beautify](https://codebeautify.org/base64-to-image-converter).