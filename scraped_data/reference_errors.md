# Errors

The Thredd Cards API uses standard HTTP response status codes to indicate whether a request was successful or not.

If a request is unsuccessful, the response body contains details of the error within an error object to provide more information about what went wrong with the request.

In the example below, a user has tried to use the Thredd `/cards/{publicToken}/pin` endpoint and has passed an PIN in the request body. The result of the request is a 400 response with the following response body:

```json Sample Error Message - Invalid PIN
{
  "type": "https://docs-gps.readme.io/docs/card-personal-identification-number-pin"
  "title": "One or more validation errors occured",
  "status": 400,
  "traceId": "00-9228fab9562d2f4f821cc6511b121faa-7c5a55c30acf1d48-00",
  "errors": {
  	"resource": [
      	"Errors description"
   	 ]
  }
}
```

See below for details of error message fields:

* `type`: passes a URI to Thredd Documentation that could be relevant to the error
* `title`: contains a short human-readable summary of the error
* `status`: returns the HTTP code of the error
* `traceId`: returns a trace ID that can be used for debugging with Thredd support teams
* `errors`: this object contains an array of specific instances in which the error occurs

## Response Error Codes

| Response Code | Error                 | Description                                                                                                                                       |
| :------------ | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400           | Bad Request           | This error status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error.  |
| 401           | Unauthorised          | This error status code indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403           | Forbidden             | This error status code indicates that the server understood the request but refuses to authorise it.                                              |
| 404           | Not Found             | This error code indicates that the server cannot find the requested resource.                                                                     |
| 405           | Method Not Allowed    | This error code indicates that the request method is known by the server but is not supported by the target resource.                             |
| 409           | Conflict              | This error code indicates a request conflict with current state of the target resource.                                                           |
| 500           | Internal Server Error | This error code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.                      |