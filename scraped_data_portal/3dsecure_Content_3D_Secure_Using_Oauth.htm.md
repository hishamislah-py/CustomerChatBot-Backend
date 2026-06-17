# 17 Using the Thredd oAuth Server

You must authenticate against the Thredd oAuth server before you can use the 3D Secure RDX Biometric API services. The oAuth server provides you with a username (client\_ID) and a secret password (`Client_secret`) that you will need to include in your API requests in order to access the RDX API services. You can also use the oAuth server to validate any API requests received from Thredd; Thredd will provide you with another username (`client_ID`) and a secret password (`Client_secret`) for the token validation.

oAuth is a secure method that replaces TLS and does not require you to set up X509 certificates. There are no additional costs for using the Thredd oAuth server.

The oAuth server complies with the RFC 7662 standard. See: <https://tools.ietf.org/html/rfc7662>

To find out more, see the identity server documentation, available at: <https://identityserver4.readthedocs.io/en/latest/intro/specs.html>

## 17.1 oAuth API Endpoints

Thredd provides two oAuth API endpoints:

* token â you can use this to obtain a token. Whenever you use the RDX API, you should include this token in the Authorization header of your HTTP request.
* introspect â you can use this to validate the token Thredd sends to your `NotifyInitiateAction` endpoint (to notify you of a request to initiate a Biometric/In-App session)

Thredd oAuth endpoints are listed below.

#### UAT:

Token endpoint: *https://oauthuat.globalprocessing.net/connect/token*

Introspect endpoint: *https://oauthuat.globalprocessing.net/connect/introspect*

#### Production:

Token endpoint: *https://p1ists.globalprocessing.net/connect/token*

Introspect endpoint: *https://p1ists.globalprocessing.net/connect/introspect*

### 17.1.1 oAuth User Credentials

Please check with your Thredd 3DS project manager for your **client\_id** and **client\_secret** to access the oAuth server.

### 17.1.2 oAuth Token Expiry

The default lifetime of the token is 4 hours (14400 seconds).

## 17.2 oAuth Token Request Example

You can retrieve an oAuth access token from the Thredd oAuth server using the private credentials (client\_id and client\_secret) provided to you by Thredd. The oAuth server returns a token, which you must include in any 3D Secure RDX requests.

Below are examples of an oAuth Token request and response.

#### Request

[Copy](javascript:void(0);)

```
POST https://oauthuat.globalprocessing.net/connect/token  
Accept:    application/json  
Content-Type: application/x-www-form-urlencoded  
client_id=9d70c6bbad8ad20262828222fc0f3fdd  
&client_secret=a3d5566e8ca0d6da823eb7815c1c2b66  
&grant_type=client_credentials
```

#### Response (Successful)

[Copy](javascript:void(0);)

```
200 OK  
  
{  
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhNjdmOWEzZTA1OTM0ZWZjOTUzYmY1ZjI1ZjVkMDMyIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1ODI1NDExMTYsImV4cCI6MTU4MjU0NDcxNiwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NDQzMzYiLCJhdWQiOlsiaHR0cHM6Ly9sb2NhbGhvc3Q6NDQzMzYvcmVzb3VyY2VzIiwicmR4YXBpIiwicmVsYXlhcGkiXSwiY2xpZW50X2lkIjoidmNhcyIsInNjb3BlIjpbImNsaWVudF92YWxpZGF0ZSIsInJkeGFwaSIsInJlbGF5YXBpIl19.Lh5Mp0Qa82QVMzs4ylmzbB9W9Qk4qiVcODewvOq3N1_JmspKyYyhOilVj8KxNxPjiKVYnFA2hDWtlKO16l8aL1oEkBky1h4haQuqtPWaUdNirWVDs99R1VqCh3wYmYZmNHNseJvEVIrd__HQ7kTJLGO7NkebPc_QM6rTB2qfYI9nax6JQnMrk72cDzeorwUlxSf2G6p49kpgyhNJooHfptWlRtV6JWUPUVEC7oNEfYnbfjVhSUyF5_11HHi_2r0zLhFIdPH7fSUXzl8OOOCMqUvSedaAJN6SRIEnTiE5isjIMJG3T4pymqUcc6ujm3upB9UStaBXMelp7Rom7LVqQ",  
    "expires_in": 3600,  
    "token_type": "Bearer",  
    "scope": "client_validate rdxapi relayapi"  
}
```

The Thredd oAuth server supports basic HTTP status codes. See the table below:

| Status | Description. |
| --- | --- |
| 200 | The request was successful. |
| 400 | The server could not understand the request due to invalid syntax. |
| 401 | The client must authenticate itself to get the requested response. |
| 403 | The client does not have access rights to the content. |
| 404 | The server cannot find the requested resource. |
| 500 | The server has encountered a situation it doesn't know how to handle. |

When your Client application has obtained the access token, it must be passed on every request made to the Thredd RDX service. The access token is included in the standard Authorization header of the HTTP request.

#### Example:

[Copy](javascript:void(0);)

```
Authorization: Bearer XXXXXX_ACCESS_TOKEN_XXXXX
```

### 17.2.1 oAuth Introspect Example

Thredd includes a token in the header of the request sent to your `NotifyInitiateAction` endpoint. You can optionally use the Introspect endpoint to validate this token (i.e., check that it is active).  Below are examples of an oAuth Introspect request and response.

#### Request

[Copy](javascript:void(0);)

```
POST https://oauthuat.globalprocessing.net/connect/introspect  
Accept:    application/json  
Content-Type: application/x-www-form-urlencoded  
token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjE5ODI3Q0E4M0NEMkNGNUUzMTAxMUVBQkQ0N0ZDNTg4RkMyRjQ3RTIiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJHWUo4cUR6U3oxNHhBUjZyMUhfRmlQd3ZSLUkifQ.eyJuYmYiOjE2MDc1MzM1NzksImV4cCI6MTYwNzU0Nzk3OSwiaXNzIjoiaHR0cHM6Ly9vYXV0aHVhdC5nbG9iYWxwcm9jZXNzaW5nLm5ldCIsImF1ZCI6WyJyZHhhcGkiLCJmaXJiaW9tZXRyaWNhcGkiXSwiY2xpZW50X2lkIjoiZmlyYmlvIiwic2NvcGUiOlsiY2xpZW50X3ZhbGlkYXRlIiwiZmlyYmlvbWV0cmljYXBpIl19.owfqYt7Rf6zHMLY2HT3j0RH7Lti05oWkp-bJ41QF1LZyqxaRMZWJAUxuRXJwIWrG2wtC0Q1KFzVPbZhpwKAwJvQTIymJFhryEvRUGTQqM61Nwu_Dnsx8H-Jpi7_0PjQk4MaAhqFv6MEgDMHvxUZ2_Q6vYj_-h2rRDunHjBvhvA55-yGLdqxeHRtNvHJQCsaVZHdLBngUpeFpWcvrbhk1SYbNlGlflYBm5aAX_YDwpWt4p_M6w7TAYJZQvc4Hi_NqAZwUOY7xOlhVD69onUmd74k6nt0ncowGgC3naWQieqcVMd3B1kCAnnYZfLlXMhSxeN_XqWtjKTK3WMavYj6vrw
```

#### Notes

* In the request body, the Content-Type should be **application/x-www-form-urlencoded**
* `token` is the bearer token value you received in the header of a `NotifyIniateAction` request from Thredd.)
* The authorization header should be in the following format: Basic (hashed value). The hashed value needs to be `resourceid:password` and must be base64 encoded.

#### Response (Successful)

[Copy](javascript:void(0);)

```
{   
 "nbf":1616170152,   
 "exp":1616184602,   
 "iss":https://stsdemo.globalprocessing.net,   
 "aud":[   
  "coreapi",   
  "relayapi"   
 ],   
 "client_id":"coreapidev",   
 "active":true,   
 "scope":"coreapi"   
} 
```

#### Notes

Indicates the bearer token is active:

> [Copy](javascript:void(0);)
>
> ```
>  "active":true, 
> ```

#### Response (Failure)

[Copy](javascript:void(0);)

```
{   
"active":false   
} 
```

#### Notes

Indicates the bearer token is **not** active:

> [Copy](javascript:void(0);)
>
> ```
> "active":false 
> ```

#### Notes

* The `scope` field indicates your application permissions. It is sufficient to check that the bearer token is `active`. You can optionally also check the scope.
* If you are using .net, Thredd recommends using the Identity Model middleware software package. For more information, see <https://identitymodel.readthedocs.io/en/latest/>