# Overview

The Thredd Cards API is based on RESTful principles. The API accepts JSON-encoded request bodies and returns JSON-encoded responses. The API uses standard HTTP Response codes and verbs. All requests to the API must be made over HTTPS.

The figure below describes how customers can integrate the API to use Thredd systems.

<Image alt="REST API Architecture Overview" align="center" border={true} src="https://files.readme.io/a6905d7-API_architecture.png">
  REST API Architecture Overview
</Image>

## Before you start

* Make sure you have read the [Set up on the Test Environment](https://cardsapidocs.thredd.com/docs/getting-started) section and understand what information and system access you need to use the test environment.
* Read the [Introduction to Cards](https://cardsapidocs.thredd.com/docs/introduction-to-cards-2) section, which provides an introduction to key concepts around creating cards using Thredd.
* Make sure you can connect to Thredd using the API, by implementing a simple call, as explained in [Set up on the Test Environment](https://cardsapidocs.thredd.com/docs/getting-started).
* If you are an experienced user and don't want to read through the Getting Started sections, you can go directly to the [API Explorer](../reference).

## Best practice

* When implementing an API call, you must at a minimum include the mandatory request fields and handle the fields that are mandatory in the response.
* Where a field requires you to submit a code value or returns a code value, our documentation provides links to the relevant appendix for details. If in doubt as to which code to include in your request, use the default or recommended value.
* Don't use spaces in field names.