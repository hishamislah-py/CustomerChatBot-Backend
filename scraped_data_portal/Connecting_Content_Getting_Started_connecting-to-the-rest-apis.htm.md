# Connecting to the REST APIs

There are two main areas in which you will need to set up your connection to access Thredd REST APIs:

1. Thredd Portal: Log in to Thredd Portal and create a client application, and obtain the client credentials for your application.
2. A REST tool: Configure your REST interface, such as Postman, to interact with Thredd's identity and access management platform, so that you can access the API endpoints.

For best practice, Thredd recommends that a Super Admin first sets up your organisation's access in the UAT (User Acceptance Test) environment. This enables you to test and verify that your organisation can use the API endpoints successfully. Once an Admin has verified that your testing in the UAT environment is satisfactory, you can prepare for migrating to a Production environment.

For your Production environment, you will need to request new credentials and ensure that the environment-specific configuration is correct. Make sure that old credentials are not cached, such as a certificate or token, and that you send updated credentials to Thredd.

## Overview of set up steps

You need to complete the following steps to set up your connection to Thredd for the first time.

1. Create a client application and OAuth Client in Thredd Portal and get a Client ID. If you have already done this, see step 2.
2. Get credentials for your client application via Thredd Portal.
3. Configure your REST tool to interact with Thredd to make calls to Thredd's API that include an access token. You must obtain an access token using your client credentials. You can also download Thredd's Postman Collection and configure your client credentials as variables in Postman to test making API calls in a UAT environment.
4. Get an access token from Thredd's OAuth token endpoint to include in the Authorization header of your API request
5. Make a call to Thredd's REST API to test your setup.

### Step 1: Create a Client Application in Thredd Portal and get a Client ID

In order to call Thredd's REST APIs, you need to create an application and OAuth Client in Thredd Portal. This registers your client application with the Thredd's identity and access management platform. Make a note of the Client ID of your application.

See [Creating an Application and OAuth Client](creating-an-appliction-and-oauth-client.htm). If you have already completed this step, see step 2.

### Step 2: Get credentials for your Application via Thredd Portal

To access any Thredd API endpoint you must exchange your client credentials for a short-lived Bearer token (OAuth token).

The credentials that you require to obtain an access (OAuth) token for Thredd's REST APIs depend on the Client Authentication method that you will use; *Client Secret* or *Private Key JWT*.

Once you have obtained your credentials, you must request an OAuth token and include it in the header of your requests to the REST API endpoints. To get an OAuth token, you can either use the endpoint within the Postman Collection (when testing in a UAT environment) or call the OAuth Token endpoint directly when using a Production environment (see step 3).

Complete the following steps to obtain the information you need via Thredd Portal, based on your Client Authentication method.

#### Client Secret authentication

You need:

* Client ID of your application
* Access token from Thredd's OAuth Token endpoint
* If you use mTLS, you also require a Transport Certificate from Thredd

##### **Get the Client ID:**

1. In Thredd Portal, navigate to **System Admin**, and select **Applications**. Select the **Actions** menu (icon of three dots) and select **Review Application**. A screen appears with tabs for the **OAuth Clients** and **Certificates** for your Application.
2. On the **OAuth Clients** tab, locate the OAuth Client that you will use to connect to the Thredd REST APIs. Select the **Actions** menu (icon of three dots) and select **View Details**. The **Overview** screen for the OAuth Client appears.
3. On the **Overview** tab, locate the **Client ID** under Client Configuration. You can copy the Client ID value from here when you need to.

#### Private Key JWT authentication

You need:

* Client ID of your application
* Signing Certificate
* Access to your JWKS endpoint
* JSON Web Token, which you generate using your Signing Certificate and fetch from your JWKS endpoint
* Access token from Thredd's OAuth Token endpoint
* If you use mTLS, you also require a Transport Certificate from Thredd

##### **Get the Client ID:**

1. In Thredd Portal, navigate to **System Admin**, and select **Applications**. Select the **Actions** menu (icon of three dots) and select **Review Application**. A screen appears with tabs for the **OAuth Clients** and **Certificates** for your Application.
2. On the **OAuth Clients** tab, locate the OAuth Client that you will use to connect to the Thredd REST APIs. Select the **Actions** menu (icon of three dots) and select **View Details**. The **Overview** screen for the OAuth Client appears.
3. On the **Overview** tab, locate the **Client ID** under Client Configuration. You can copy the Client ID value from here when you need to.

##### **Get a Signing Certificate:**

An Admin user can obtain a Signing Certificate from Thredd Portal to create and register a private key. You must generate a Client Assertion, a JSON Web Token (JWT) that is signed by your private key, and configure your client for Private Key JWT authentication. See [Requesting a Signing Certificate for an application.](requesting-a-signing-certificate-for-private-key-jwt.htm)

##### **Get the JSON Web Key Set via your JWKS endpoint:**

To ensure secure communication with Thredd, its Identity and Access Management (IAM) platform uses JSON Web Key Sets (JWKS). This industry-standard format allows your systems to automatically verify the authenticity of digital signatures and encrypted data.

Every organisation registered with Thredd's IAM platform is assigned a unique, public JWKS endpoint. The JWKS is a set of keys that includes your public key that you created when you requested your Signing Certificate in Thredd Portal.

Use the following URL to get your organisation's registered keys via your JWKS endpoint. The `<organisation_id>` parameter is your unique Thredd organisation identifier.

http://jwks.threddid.com/<organisation\_id>/jwks.json

##### **Get a Transport Certificate â only mTLS connections:**

If you are using an mTLS connection, your application requires a Transport Certificate for establishing mutual connections between your Client and Thredd. An Admin user can obtain a Transport Certificate from Thredd Portal. See [Requesting a Transport Certificate for applications using mTLS.](requesting-certificates-for-mtls-connections.htm)

### Step 3: Configure your REST tool to make calls to Thredd API using your client credentials

You can access Thredd's API Hub and REST APIs over TLS or mTLS. You must make sure that you configure your REST tool with the appropriate settings, for example:

* Base URL â this depends on whether you are using the UAT or Production environment, and TLS or mTLS connectivity.
* Headers â you must set the correct Authorization, Content-Type, and X-Region headers.

#### Base URL

* TLS connectivity for the UAT environment: `uat-api.thredd.com`
* TLS connectivity for the Production environment: `api.thredd.com`
* mTLS for the UAT environment: `uat-mtls.thredd.com`
* mTLS connectivity for the Production environment: `mtls.thredd.com`

#### Configuring headers

Whether you are using your own tool or the Postman Collection, you must make sure that you configure the following headers with the correct information in each API request. These headers are mandatory for all requests that you make to the API Hub.

* Authorization header â include your OAuth token in the `authorization` header as appropriate for your application's authentication method.
* X-Region header â this is mandatory and determines the region/environment you are trying to connect to. Select one of the following values to include in the `X-Region` header:

  + Use `0` for the Default environment
  + Use `1` for the EMEA environment
  + Use `2` for the APAC environment

  If you are not sure which environment to use, contact your Thredd Account Manager or Implementation team. By default, the Postman Collection is set to use the Default environment (0), but you can change this in the variables section.
* Content-Type header â specify the media type of the requested resource in the `content-type` header. Example value: `application/x-www-form-urlencoded`

For some endpoints, you can pass pagination values. Where this is relevant, this is stated in the documentation for a given endpoint in API Reference on the API Hub.

Thredd provides separate Postman Collections for TLS and mTLS, which enable you to use Postman to test using the Thredd REST APIs in a UAT environment. To use the collection, you need to configure Postman with the appropriate environment variables and credentials.

#### Postman Collection

Download the Postman Collection from the API Hub and follow the guide that matches your configuration:

* For TLS connections: [Using the Postman Collection to call REST APIs over TLS](setting-up-postman-to-access-rest-apis-for-tls.htm)
* For mTLS connections: [Using the Postman Collection to call REST APIs over mTLS](setting-up-postman-to-access-rest-apis-for-mtls.htm)

To download the Postman Collection, see [Accessing the API Hub](https://cardsapidocs.thredd.com/v2.0/docs/accessing-api-hub).

### Step 4: Get an access token using your client credentials

You must request an access token from Thredd and include it in the Authorization header of your requests to the REST API endpoints. You can get an access token using the following methods:

* Use the endpoint within the Postman Collection (when testing in a UAT environment).
* Call the OAuth Token endpoint directly when using a Production environment.

Access tokens are valid for one hour and include the scopes that are associated with your application.

Follow the advice that match your Client Authentication method.

#### Client Secret authentication

You must provide your:

* Client ID
* Client secret

Endpoint:

POST https://threddid.com/oauth2/token

Example request body (URL-encoded):

[Copy](javascript:void(0);)

```
curl --location 'https://threddid.com/oauth2/token' \  
                --header 'Content-Type: application/x-www-form-urlencoded' \  
                --data-urlencode 'grant_type=client_credentials' \  
                --data-urlencode 'client_id=YOUR_CLIENT_ID'  
            --data-urlencode 'client_secret=YOUR_CLIENT_SECRET'
```

If you use an mTLS connection, you must also include your Transport Certificate in your request to the OAuth token endpoint. The Authorisation Server will reject all requests without this.

#### Private Key JWT authentication

You must provide your:

* Client ID
* Signed JSON Web Token

Endpoint:

POST https://threddid.com/oauth2/token

Example request body (URL-encoded):

[Copy](javascript:void(0);)

```
curl --location 'https://threddid.com/oauth2/token' \  
                --header 'Content-Type: application/x-www-form-urlencoded' \  
                --data-urlencode 'grant_type=client_credentials' \  
                --data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer'  
            --data-urlencode 'client_assertion=YOUR_SIGNED_JWT'
```

If you use an mTLS connection, you must also include your Transport Certificate in your request to the OAuth token endpoint. Thredd's Authorisation Server will reject all requests without this.

#### Example OAuth token response

```
{  
                "access_token": "eyJhbGciOi...",  
                "token_type": "Bearer",  
                "expires_in": 3600  
            }
```

Access tokens are valid for one hour and include the scopes that are associated with your application.

You must configure your application to refresh the token automatically when it expires.

### Step 5: Make a call to Thredd's REST APIs

Once you have the `access_token`, you must include it in the Authorization header of every request to Thredd's REST APIs.

The next step is to test making an API call. Refer to the documentation for the base URLs and API Reference for endpoints at the API Hub: [https://cardsapidocs.thredd.com/v2.0/docs](https://cardsapidocs.thredd.com/v2.0/docs/getting-started-1 "Thredd REST API reference and documentation website")

Remember to include the following in your requests:

* Base URL â this depends on whether you are using the UAT or Production environment, and TLS or mTLS connectivity.
* Mandatory information in your request headers.
* Correct HTTP method for the endpoint.

If you change the environment or region that you want to make API calls to, you must update the Base URL and headers that you include in your requests.

#### Example request header (TLS)

[Copy](javascript:void(0);)

```
GET /core/api/v1/products HTTP/1.1  
                Host: api.thredd.com  
                Authorization: Bearer eyJhbGciOi...  
            Content-Type: application/json
```

#### Example request header (mTLS)

[Copy](javascript:void(0);)

```
GET /core/api/v1/products HTTP/1.1  
                Host: mtls.thredd.com  
                Authorization: Bearer eyJhbGciOi...  
            Content-Type: application/json
```

For mTLS, when making your request to `uat-mtls.thredd.com` (UAT environment) or `mtls.thredd.com` (production environment) you must also include your Transport Certificate in the request. Thredd's APIs will reject all requests that do not include this.