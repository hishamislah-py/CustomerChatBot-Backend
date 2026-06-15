# Release Notes for 13th October 2023

New changes to the Thredd Cards API for the week ending 13th October 2023.

* [New Get Encrypted Data endpoint](#new-get-encrypted-data-endpoint)
* [Fixed issue with certain country codes not being accepted in Create Card endpoint](#fixed-issue-with-certain-country-codes-not-being-accepted-in-create-card-endpoint)
* [Behaviour change for Renew and Replace Card endpoints](#behaviour-change-for-renew-and-replace-card-endpoints)
* [nameOnCard changed in Create Card and Update Card endpoints](#nameoncard-changed-in-create-card-and-update-card-endpoints)

## New Get Encrypted Data endpoint

*Endpoint: /cards/\{\{PublicToken}}/encrypted*\
A new endpoint has been added that enables customers to be able to send secure data to a cardholder with or without PCI DSS compliance.

You can get encrypted data by making a POST request to the Get Encrypted Data endpoint. For example:

```json Example Get Encrypted Data endpoint
{{base-url}}/cards/{{PublicToken}}/encrypted
```

The device-generated session key must be included in the request body to the endpoint. The value of the key is a base64 encoded string, comprising of an AES key that you've encrypted with your company specific public RSA key provided to you by Thredd.

> 📘 Documentation/API Explorer
>
> * For more information on the Get Encrypted Data endpoint, see [Introduction to Sending Secure Data](https://cardsapidocs.thredd.com/docs/introduction-to-sending-secure-data)
> * To try the Get Encrypted Data endpoint, navigate to [Get Encrypted Data](https://cardsapidocs.thredd.com/reference/retrieven-encrypted-card-includes-pannd-cvv) in API Explorer.

## Fixed issue with certain country codes not being accepted in Create Card endpoint

An issue with the Create Card endpoint, where certain country codes were not being accepted, has been resolved with this release. The `country` field now uses ISO 3166-1 Alpha-3 codes for all countries.

For a full list of country codes, see the Alpha-3 list on the [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) page on Wikipedia.

## Behaviour change for Renew and Replace Card endpoints

A change to the Renew and Replace card endpoints has been made with this release, so that the new card is inactive on creation. Previously, when a new card was created from the Renew and Replace Card endpoints, the status of the card was set to Active.

## nameOnCard changed in Create Card and Update Card endpoints

From the 2nd November, as part of [PRN-160](https://cardsapidocs.thredd.com/changelog/threddprn-160), the nameOnCard object will be removed from the Create Card and Update Card endpoints, and replaced with a new nameOnCard field.

Before:

```Text Before example of nameOnCard object
{
....
 "nameOnCard": {
    "title": "string",
    "firstName": "string",
    "lastName": "string"
    }
....
}
```

After:

```json After example of nameOnCard object
{  
...
    "nameOnCard": "string"
...
}
```

For more information on these endpoints, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2) and [Updating a Card](https://cardsapidocs.thredd.com/docs/updating-a-card).