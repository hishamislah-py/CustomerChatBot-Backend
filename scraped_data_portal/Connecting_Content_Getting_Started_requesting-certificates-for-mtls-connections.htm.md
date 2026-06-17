# Requesting certificates for applications using mTLS

Client applications require a Transport Certificate in order for you to access Thredd's REST APIs over an mTLS connection.

Additionally, if you are using the Private Key JWT Client Authentication method, then you also require a *Signing Certificate* to create and register a private key. You must generate a Client Assertion, a JSON Web Token (JWT) that is signed by your private key. If you are using Client Secret authentication, you do not need a Signing Certificate.

Whether you want to generate a new certificate, or renew or revoke a certificate, you can manage certificates through Thredd Portal.

You must use certificates from Thredd to connect to Thredd APIs. Using self-signed or third-party certificates may result in Thredd refusing connections.

## Purpose of Transport and Signing Certificates

A *Transport Certificate* is mandatory for mTLS and is used solely for establishing the secure mutual connection between the Server and the Client. Without a valid, signed Transport Certificate, your application is unable to connect to Thredd's secure API endpoints.

A *Signing Certificate* (or Signing Key) is required if you are using the Private Key JWT Client Authentication method. To authenticate with Thredd using the Private Key JWT method, you must generate a Client Assertion in the form of a JSON Web Token (JWT) and ensure that your client presents it when requesting an access token from Thredd. You must then include the access token in any calls that you make to the Thredd REST APIs. To learn more, see [Requesting a Signing Certificate](requesting-a-signing-certificate-for-private-key-jwt.htm).

#### Certificate Lifecycle Management

Regularly rotating (refreshing) your certificates is essential to maintain secure communication between your applications and the Thredd platform. New certificates are valid for 350 days; Thredd sends an email to you when a certificate is approaching its expiry date, notifying you 60 days in advance. If you want to renew a certificate, you should request a new Transport or Signing Certificate and rotate it before the date that it expires. This ensures that your application can continue to access Thredd applications.

You can also revoke a certificate at any time by logging in to Thredd Portal and choosing the option to revoke it in the **Certificates** tab of your Application. Fulfilling a revocation request can take up to one hour for Transport Certificates and is instant for Signing Certificates.

### Summary of the steps

The steps for obtaining a certificate are as follows:

1. Log in to Thredd Portal and select or create the application that requires a certificate.
2. Create a private key and Certificate Signing Request for a new Transport Certificate.
3. Upload the Certificate Signing Request for your application.
4. Download the certificate for your application.
5. Store the private key on your client and ensure it can use the Transport Certificate.
6. Configure your Client to use the Transport Certificate in your requests.
7. Only for applications using Private Key JWT Client Authentication: Create a private key and Certificate Signing Request for a new Signing Certificate. You need to download the Signing Certificate, store the private key, and configure your Client to use JWT authentication.

#### Prerequisites

1. You must have access to Thredd Portal.
2. You must have an Admin role in Thredd Portal.
3. You must have installed OpenSSL on the machine (the Server) that will make requests to Thredd platform (the Client).

### Step 1: Log in to Thredd Portal and select or create the application that requires a certificate

Log in to Thredd Portal and select **System Admin**. From the **System Admin** menu, select **Applications**. You will have access to at least one organisation for your parent company. The **Applications** screen lists any applications that are registered in Thredd Portal.

![](../Resources/Images/thredd-portal-applications-screen.png)

If an existing application is already present and you want to create a signing certificate for it, do the following:

1. Select the **Actions** menu (three dots) and select **Review Application**.

   ![](../Resources/Images/thredd-portal-system-admin-action-menu-review-application.png)
2. The application summary screen appears and displays the **OAuth Clients** screen. Select the **Certificates** tab. See step 2 to create a certificate.

If you need to create a new application, you can do so by selecting the **Add Application** button. Follow the on-screen prompts to create the Application, and then create an OAuth Client for it. For a full guide, including an explanation of the different Application Types and their associated Security Configurations, see [Creating an Application and OAuth Client.](creating-an-appliction-and-oauth-client.htm)

### Step 2: Review the application details and create a new Transport Certificate

The **Applications** screen lists an entry for your application once it is registered in Thredd Portal. To request a Transport Certificate:

1. Select the Action menu (three dots) under **Actions** and select **Review Application**.
2. The **OAuth Clients** screen appears; it displays a summary of your application details and permissions. Check that these details are correct, and only update any details if you need to. Specific configuration details are under **Client Configuration**, such as the Client ID. The **Permissions** tab lists the available **Scopes** for your organisation.
3. Next, select the **Certificates** tab and select **New Certificate** button. The **New Certificate** screen appears.

   ![](../Resources/Images/thredd-portal-certificates-tab.png)

### Step 3: Create a private key and Certificate Signing Request for a Transport Certificate

1. Select **Transport** from the **Certificate Type** dropdown menu, and then select **Next**.

   ![](../Resources/Images/thredd-porta-request-transport-certificate.png)
2. Copy the OpenSSL command from the clipboard and run the command on the machine that you have installed OpenSSL on. This command creates a private key and a Certificate Signing Request (CSR). This command is unique to generate a Transport Certificate with the unique `-rtstransport.csr` and `-rtstransport.key` values.
3. You must store the private key securely. Once you have successfully created the private key (.key) and CSR (.csr) files, select **Next**.

   Example:

   ```
   openssl req -new -newkey rsa:2048 -nodes   -out MyUniqueFileName-rtstransport.csr   -keyout MyUniqueFileName-rtstransport.key   -subj "/C=MyCountry/O=MyOrganization/OU=MyOrganizationalUnit/CN=MyUniqueFileName"   -sha256
   ```

   The following example contains placeholder values, but the command that you copy contains your unique file name for .csr (-out) and .key (-keyout), and organisation information in the certificate subject (-subj).

   ![](../Resources/Images/thredd-porta-request-transport-certificate-csr.png)

### Step 4: Upload the Certificate Signing Request for your application

1. Select the **Upload CSR** button and select your Certificate Signing Request file. This uploads your Certificate Signing request onto the Thredd platform, so that it can use the file to request the Transport Certificate from the Thredd Certificate Authority (CA).
2. Select **Save**.

   ![](../Resources/Images/thredd-portal-request-certificate-upload-csr.png)

If this is successful, Thredd's system adds the newly-issued Transport Certificate to your application. You can verify this in the **App Certificates** screen of the **Certificates** tab for your application.

### Step 5: Download the certificate for your application

Next, download the certificate from the **App Certificates** screen. Select the **Actions** menu (three dots) next to the TRANSPORT certificate, and select **Download Certificate**.

![](../Resources/Images/thredd-portal-certificate-download.png)

### Step 6: Configure your Client to use the Transport Certificate in your requests

You must configure your Client to ensure that it includes the Transport Certificate in all calls that it makes to the Thredd platform. To understand how to do this in your specific case, refer to your Client library documentation.

The domain for mTLS connections is: `mtls.thredd.com`

### Step 7: Request a new Signing Certificate (Private Key JWT authentication only)

If you are using Private Key JWT Client Authentication, then your client application also requires a Signing Certificate for signing assertions sent to the Authorisation Server.

If you are using Client Secret authentication, you do not need a Signing Certificate. See [Using the Postman Collection to call REST APIs over mTLS.](setting-up-postman-to-access-rest-apis-for-mtls.htm)

For Private Key JWT Client Authentication, creating a Signing Certificate is an essential step for enabling access for OAuth 2.0 client applications that connect to Thredd's REST APIs.

There are a few steps that you need to complete after you have requested the Signing Certificate. For example, you must generate a Client Assertion in the form of a JSON Web Token (JWT) and ensure that your client presents it in all calls that it makes to the Thredd REST APIs.

For a guide to requesting a Signing Certificate and configuring your client to use Private Key JWT, see [Requesting a Signing Certificate](requesting-a-signing-certificate-for-private-key-jwt.htm).

### Next steps

Once you have obtained the necessary credentials for your Client application, you can begin setting up your connection to the API Hub using the latest Postman Collection. See [Using the Postman Collection to call REST APIs over mTLS.](setting-up-postman-to-access-rest-apis-for-mtls.htm)