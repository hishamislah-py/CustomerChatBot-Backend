# Release Notes for 16 September

New changes to the GPS Cards API for the week ending 16th September 2022.

* [Get List of Cards for Cardholder endpoint added](#get-list-of-cards-for-cardholder-endpoint-added)
* [Get List of Cardholders endpoint added](#get-list-of-cardholders-endpoint-added)
* [renewWithSameExpiry option added to Renew Card endpoint](#renewwithsameexpiry-option-added-to-renew-card-endpoint)

## Get List of Cards for Cardholder endpoint added

A new endpoint has been added that enables you to view a list of cards associated with a cardholder. For more details on how this endpoint works, see [Get Card Details for Program](https://cardsapidocs.thredd.com/docs/get-cardholder-details-for-program).

The endpoint can contain various options in which you can filter cardholder information. You can use the following options to search by:

* title
* firstName
* lastName
* dateOfBirth
* email
* mobile

See below for an example where a first name and last name have been added to the endpoint to search for cards belonging to John Smith:

```json
https://cardsapi-uat-pub.globalprocessing.net/api/v1/program-manager/search/cards?FirstName=john&LastName=smith
```

This will return a 200 response that will return the details of all cards for a cardholder with that name.

```json
[
    {
        "publicToken": "308795420",
        "expirationDate": null,
        "productType": null,
        "schemeId": 644,
        "schemeName": "GPS SCHEME TEST",
        "status": "54",
        "balanceCurrency": "EUR",
        "balanceAmount": 0,
        "product": "VISA"
    }
]
```

> 👍 API Explorer
>
> To try this endpoint, click [here](https://cardsapidocs.thredd.com/reference/get-list-of-cards-belonging-to-given-cardholder).

## Get List of Cardholders endpoint added

A new endpoint has been added that enables you to view a list of cardholders for a program. For more details on how this endpoint works, see [Get Cardholder Details for Program](https://cardsapidocs.thredd.com/docs/get-cardholder-details-for-program).

The endpoint can contain various options in which you can filter cardholder information. You can use the following options to search by:

* title
* firstName
* lastName
* dateOfBirth
* email
* mobile

See below for an example of the endpoint where a first name and last name have been added to the endpoint to search for cardholders called John Smith:

```json
https://cardsapi-uat-pub.globalprocessing.net/api/v1/program-manager/search/cardholders?FirstName=John&LastName=Smith
```

This will return a 200 response that will return the details of all cardholders for the program with that name.

```json
[
    {
        "title": "Mr.",
        "firstName": "John",
        "lastName": "Smithe",
        "dateOfBirth": "02/19/1982 00:00:00",
        "email": "jsmith@gps.com",
        "mobile": "07755123456"
    }
]
```

> 👍 API Explorer
>
> To try this endpoint, click [here](https://cardsapidocs.thredd.com/reference/get-list-of-cardholders).

## renewWithSameExpiry option added to Renew Card endpoint

The renewWithSameExpiry option has been added to the Renew Card endpoint for this release. This enables you to replace a card (for example, if it has been damaged) with the same details it had before.

The below is an example of the body text required to use the new option in the Renew Card endpoint.

```json
{
     "renewStep": "RenewWithSameExpiry"
}
```

> 👍 API Explorer
>
> To try the Renew Card endpoint, click [here](https://cardsapidocs.thredd.com/reference/renew-card).