# Using the Postman Collection to call REST APIs over TLS

Follow these steps to configure Postman with your client credentials so that you can obtain an access token. You must include an access token in all requests to Thredd's REST APIs.

The instructions to obtain an access token are slightly different depending on the Client Authentication method that you have chosen to use.

* Client Secret â requires an access token that you can request from Thredd's OAuth endpoint and within the Postman Collection. You do not require a Signing Certificate.
* Private Key JWT â requires an access token and a JSON Web Token (JWT). You can request the access token from Thredd's OAuth endpoint and within the Postman Collection. To obtain a JWT, you require a Signing Certificate, which an Admin user can obtain from Thredd Portal to create and register a private key. You must generate a Client Assertion, a JSON Web Token (JWT) that is signed by your private key.

### Set up summary

You need to complete the following steps to set up Postman to use the Thredd Postman Collection for TLS connections for the first time.

1. Download the Postman Collection.
2. Get variables for the Postman Collection.
3. Set variables in Postman.
4. Test making an API call using the Postman Collection.

#### Prerequisites

* An Admin user at your organisation must have set up your application that requires access to Thredd APIs in Thredd Portal.
* An Admin user must have requested any certificates that you require from within Thredd Portal.
* You must be able to confirm that you have access by logging in to Thredd Portal.

### Step 1: Download the Postman Collection

The Thredd TLS Postman Collection is available for you to download from the Thredd API Hub at: <https://cardsapidocs.thredd.com/v2.0/docs>

Visit the website and make sure that you download the Postman Collection for TLS connections.

### Step 2: Get variables for the Postman Collection

Before you can start using the Postman Collection, you must obtain the following variables and enter them in the **Variables** tab in Postman:

* Application ID (UUID) â to enter into the **ssa\_id** field
* Client ID â to enter into the **client\_id** field
* Signing Certificate (KID) â to enter into the **kid** field ONLY if you using Private Key JWT authentication. If you are using Client Secret authentication leave this blank.

Thredd Portal contains the details for your applications. A Super Admin can get this information from the following areas in Thredd Portal.

#### Get the Application ID from Thredd Portal

1. Select **System Admin** from the main menu, and then **Applications**. The **Applications** screen displays the applications that you have registered with Thredd.

   If the **Applications** list is empty, you need to create an application. See [Creating an Application and OAuth Client](creating-an-appliction-and-oauth-client.htm).
2. Locate your application, and use the copy icon to copy the value under **App ID**.
3. Paste the App ID value into the **ssa\_id** field in your Postman Collection.

#### Get the Client ID from the Overview tab of your application in Thredd Portal

1. Locate the application that you copied the **App ID** from in the **Applications** screen of Thredd Portal in the previous step.
2. Select the **Actions** menu and select **Review Application**. A screen appears with **OAuth Clients** and **Certificates** tabs for your application.
3. Remain on the **OAuth Clients** tab and locate the OAuth Client that you will use to connect to the Thredd REST APIs via the API Hub. Select the **Actions** menu (icon of three dots) and select **View Details**. The **Overview** screen for the OAuth Client appears.
4. On the **Overview** tab, locate the **Client ID** under Client Configuration, and copy the Client ID value. Next, paste it into the **client\_id** variable field in your Postman Collection.

#### Get the KID from the Certificates tab of your application Thredd Portal (Private Key JWT)

If you are using Private Key JWT authentication, you will have requested a Signing Certificate, which generates a KID.

If you are using Client Secret authentication, you do not need a Signing Certificate, which means you do not have or need a KID.

1. Ensure that you are in the details screen for the application that corresponds with the **App ID** and **Client ID** that you copied in the **Applications** screen of Thredd Portal in the previous steps.
2. Select the **Certificates** tab. The Certificates screen displays any certificates available for your application and the **Status**, **KID**, **Key Type** such as **SIGNING**, and **Issued** and **Expiry** dates.
3. Locate the certificate that is the **SIGNING** Key Type, locate the corresponding **KID**, and use the copy icon to copy the KID value. Next, paste it into the **kid** variable field in your Postman Collection.

### Step 3: Set variables in Postman

Before you can use the Postman Collection, you must set the following variables in Postman. This ensures that when you make an API call, Postman references these variables and uses the stored values in your API calls. You must not hard-code static values in your API calls.

| Variable | Description |
| --- | --- |
| `client_id` | This is either a UUID or a URL with a UUID on the end.  If it is an URL you must include the full URL. Example: `https://{{domain}}/{restOfUrl}}`  If it is a UUID, you must include only the UUID. Example: `abcdef01-0124-4567-ffaa-fedcba098731` |
| `kid` | The Key ID of the Signing Certificate â only if you are using Private Key JWT authentication.  If you are using Client Secret authentication, then leave this blank. |
| `private_key` | The Signing Certificate Private Key â only if you are using Private Key JWT authentication. You will have created this when you requested the Signing Certificate in Thredd Portal.  You must include the first and last lines: `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----`  If you are using Client Secret authentication, then leave this blank. |

### Step 4: Check your settings and finish setting up

Make sure that you have configured the following settings for your API calls:

* You have set the correct Base URLs for the API Hub.
* You have obtained an access token.
* Including the access token in the authorisation header.
* Adding an X-Region header â this is mandatory and determines the region that you want to connect to; select one of the following options:

  + `0` for the default environment
  + `1` for the EMEA environment
  + `2` for the APAC environment

Once you have completed these steps, you are ready to make your first API call. For more information, see the [Thredd API Hub](https://cardsapidocs.thredd.com/v2.0/docs).

### Preparing your Production environment

Once an Admin has verified that your testing in the UAT environment is satisfactory, you can prepare for migrating to a Production environment. You will need to repeat all of these steps for Production, such as requesting new certificates or access tokens, and ensuring that environment-specification configurations are correct. See [Updating Postman](updating-postman.htm).