# Updating Postman

You will need to update Postman if you delete an existing client application and create a new one. An Admin for your organisation must:

* For Client Secret client authentication: Request a new access token (TLS and mTLS).
* For Private Key JWT client authentication: Request a new Signing Certificate from Thredd via Thredd Portal, and request a new access token (TLS and mTLS).
* For mTLS connections only: Request a new Transport Certificate from Thredd via Thredd Portal, and request a new access token.

Users who will make calls to Thredd's APIs using the Postman Collection, must update their Postman Collection with the new credentials.

1. Update any access tokens or certificates.
2. Update the variables for the Client ID and other credentials.
3. Use the Postman Collection to obtain a new access token.

### Adding Certificates to Hosts for mTLS connections in Postman

If you use an mTLS connection to Thredd REST APIs, you must include a Transport Certificate with the individual hosts. Complete these steps:

1. Select the gears icon and **Settings**.
2. Select **Certificates** from the left-hand menu.
3. Select **Add Certificate**.

   ![Postman screen showing the Variables tab](../Resources/Images/add_certificate.png)
4. Enter a host name.
5. Add the CRT and Key files for the host.
6. Select the **Add** button.

For more details, see [Using the Postman Collection to call REST APIs over mTLS](setting-up-postman-to-access-rest-apis-for-mtls.htm).

## Base URLs

When calling Thredd endpoints, you must include the Base URLs within your REST tool. The Base URLs are the hosts that accept the certificates. The Cards API and API Hub hosts have unique URLs that are different between UAT and Production.

UAT environments use the following Base URLs:

* **Cards API**: https://api.uat.threddpay.com/api/v1
* **API Hub over TLS**: https://uat-api.thredd.com
* **API Hub over mTLS**: https://uat-mtls.thredd.com
* **Thredd Certificate Authority**: https://matls-auth.directory.sandbox.threddid.com

Production environments use the following Base URLs:

* **API Hub over TLS**: https://api.thredd.com (for all PRD environments)
* **API Hub over mTLS**: https://mtls.thredd.com (for all PRD environments)
* **Cards API**: https://coreapi.threddpay.com