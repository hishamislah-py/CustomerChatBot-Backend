# What is Idempotency?

Idempotency enables consistency of data in REST API, meaning that sending a request repeatedly generates the same result no matter how times it is sent.

Some request types are inherently idempotent. These are requests that either don’t modify anything (such as a GET request), or replace data without the initial state being important. The reason these are usually idempotent, is because the requests can be repeated many times and the outcome would always be the same.

For requests which are not inherently idempotent, such as a PUT request, idempotency must be achieved through the use of unique keys and request consistency. Idempotent endpoints require the request to contain a unique ID (idempotency key) in the header. The idea being that if an API generates a unique key for a particular request, the information in the request is static. The API or system can send the request to a customer multiple times. The customer caches the response given for the first instance, then subsequent hits with an identical key and request body would return the cached response so the action is never performed twice.

The key is valid for an hour after initial use. If another attempt to use the same key is done within the hour, a 200 response is returned but the idempotent behaviour will be present. If the same key is used for a different endpoint, a 400 response is returned with the following message.

```Text Example Idempotent error response
The Idempotency header key value 'fce6e10c-4311-413d-a302-47c90442b9c4' was used in a different request.
```

<br />

# How Thredd uses Idempotency in Cards API

For endpoints that use idempotency, a unique key must be included in the request header. The key, called `IdempotencyKey`, allows you to enter a unique GUID that is used to identify the request.

In the below example, you can see the `IdempotencyKey` in the header for the Update Card Status endpoint.

```json Example Update Card Status header with IdempotencyKey
curl --request PATCH \
     --url https://cardsapi-uat-pub.globalprocessing.net/api/v1/cards/publicToken/status \
     --header 'accept: application/json' \
     --header 'content-type: application/*+json' \
     --header 'idempotencyKey: 3196f682-62ea-4122-830e-b4a21a4d832f'
```

The first time the system returns a response it sends a GUID. If the same GUID value is used in another request, a 400 error is returned stating that Idempotency header key value was used in a different request.

# Endpoints that Support Idempotency

All our endpoints support idempotency with the following exceptions.

* All GET endpoints
* The PUT Update Card endpoint
* All DELETE endpoints