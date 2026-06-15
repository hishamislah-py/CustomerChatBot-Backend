# Accessing the Cards API with mTLS

This page describes what you need to do to create an access token and call our APIs using our API Postman Collection.

## Pre-Requisites

Before you can use this Postman Collection, you must access Thredd's Certificate Authority called Raidiam Connect (the CA) to generate transport and signing certificates. Using Raidiam Connect, you must:

* Create an Application with appropriate Software Roles
* Create Transport and Signing Keys
* Obtain the Organisation ID (UUID), Application ID (UUID), Signing Certificate Key ID (KID), and Client ID for your Application

## Create an Application in Raidium Connect

Before creating either a Transport Certificate or a Signing Certificate, you must register a client application with the CA. Using Raidiam Connect, you provide metadata associated with the application. The steps for registration are as follows:

1. Select your organisation and then select **Applications** from the left-hand menu.
2. Click **New Application** (top-right of the screen). The New Client wizard appears. The New Client shows the roles that are available to you. The organisation determines the available roles.
3. Tick a check box for the role you require. To use the full suite of endpoints available, select **ws** and **programme-manager**.
4. Click **Next**.

   Enter your client details. Complete the form by entering details where applicable. The table below describes the fields.

   | Field Name               | Example Data                                                 | Notes                                                                                                            |
   | :----------------------- | :----------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
   | Federation Configuration | Federation Enabled                                           | It is good practice to have federation enabled for all applications.                                             |
   | Client Name              | Test Company App 1                                           | The name of the intended OAuth client application. This setting is mandatory.                                    |
   | Version                  | 1.0                                                          | Your chosen application version. This setting is mandatory.                                                      |
   | Homepage URI             | [https://example.com](https://example.com)                   | URI of the homepage. This setting is mandatory.                                                                  |
   | Upload Logo              | [https://example.com/logo.png](https://example.com/logo.png) | URI of the logo for the homepage. This must also include the file format of the logo. This setting is mandatory. |
5. Click **Next**.
6. Enter your user authentication Settings. Complete the form by entering user authentication details where applicable. The following table describes the relevant fields that you need to enter on this page. All other fields are optional.

   | Field Name   | Example Data                                                 | Notes                                                                                                                                 |
   | :----------- | :----------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
   | Redirect URI | [https://example.com/callback](https://example.com/callback) | The callback URL any Confidential Client expects to be returned. This field is mandatory and you should enter the correct URI format. |
   | Logo URI     | [https://example.com/logo.png](https://example.com/logo.png) | Company logo URL. This must also include the file format of the logo.                                                                 |
7. Click **Next**.
8. Enter any additional details. Complete the form by entering details where applicable. The following table describes the fields, all which are optional.

   <Table align={["left","left","left"]}>
     <thead>
       <tr>
         <th style={{ textAlign: "left" }}>
           Field Name
         </th>

         <th style={{ textAlign: "left" }}>
           Example Data
         </th>

         <th style={{ textAlign: "left" }}>
           Notes
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td style={{ textAlign: "left" }}>
           Description
         </td>

         <td style={{ textAlign: "left" }}>
           Test Company App 1
         </td>

         <td style={{ textAlign: "left" }}>
           Description of the app.
         </td>
       </tr>

       <tr>
         <td style={{ textAlign: "left" }}>
           API Webhook URI
         </td>

         <td style={{ textAlign: "left" }}>
           * <br />
         </td>

         <td style={{ textAlign: "left" }}>
           URI of the webhook.
         </td>
       </tr>

       <tr>
         <td style={{ textAlign: "left" }}>
           On Behalf Of
         </td>

         <td style={{ textAlign: "left" }}>
           * <br />
         </td>

         <td style={{ textAlign: "left" }}>
           On behalf of a particular user.
         </td>
       </tr>

       <tr>
         <td style={{ textAlign: "left" }}>
           Origin URI
         </td>

         <td style={{ textAlign: "left" }}>
           * <br />
         </td>

         <td style={{ textAlign: "left" }}>
           The origin URI.
         </td>
       </tr>
     </tbody>
   </Table>
9. Click **Next**.
10. Leave the following fields with their default values: **Token Signed Response Algorithm ID** and **Token Endpoint Authentication Method**. You should also leave Require Signed Request Object as enabled.
11. Click **Save**.
12. Ignore the step for adding an extra certificate.
13. Click **Done**. Your new Application appears as a tile on the Applications view

## Prepare the New Certificate

To create the transport and signing keys to use the mTLS Postman Collection:

1. In a new terminal window, create an empty directory for making and receiving the private key and CSR. The following example shows a key pair and CSR that have been created in a directory.
2. In the CA dashboard, click on your organisation’s tile.
3. In the CA dashboard, select Organisation Certificates.
4. Click New Certificate.
5. In the New Certificate window, select RESOURCE SERVER TRANSPORT in the Select Certificate Type dropdown.
6. Click Next.
7. Copy the generated CSR command and paste this into a terminal window.
8. Click Next.
9. In the terminal window, press Enter to run the OpenSSL command. A Private Key and CSR generates in the background.
10. In CA, click Select File.
11. Browse to the CSR you just created. Then click Open.
12. In the CA dashboard, click Save for the CSR you selected. This allows you to upload the CSR. When uploaded, the certificate signing happens. This takes place in a few seconds. The newly created Transport Certificate then appears, and is ready for download.
13. On the three dots menu for the generated certificate, select Download certificate.
14. Click the download link on the CA UI to download the base 64 encoded X.509 certificate that was just generated.

When you’ve completed this process, a JSON Web Key Set (JWKS) endpoint is also created with public certificate details. JWKS is a JSON notation for sharing public keys which are used to verify the signature of a signed JSON web token (JWT).

> 📘 Note
>
> If required, for example you are using Windows services, you can convert the public certificate and private key to the PKCS#12 syntax. For converting, you can use OpenSSL commands. In the PKCS#12 syntax, the files are in the .pfx format. For more details, see [RFC 7292: PKCS #12: Personal Information Exchange Syntax v1.1](https://datatracker.ietf.org/doc/html/rfc7292).

## Get Variables for the Postman Collection

Before you can start using the Postman Collection, you need to enter the following variables:

* The Organisation ID (UUID) entered into the org\_id field
* The Application ID (UUID) entered into the ssa\_id field
* The Signing Certificate (KID) entered into the kid field
* The Client ID entered into the client\_id

You can find the Variables tab by clicking on your Postman Collection and clicking Variables.

<Image align="center" alt="Variables tab location in the Postman Collection" border={true} caption="Variables tab location in the Postman Collection" src="https://files.readme.io/649d7cdde40054ad8d31462132146f364899ea28cd4bb39e8d768c6a2a524508-Variables.png" />

<br />

### Finding the Organisation ID (UUID)

To find your Organisation ID, navigate to your Organisation in CA. The Details page displays, which contains the Organisation ID. Click on the Copy button and paste into the org\_id field.

<Image align="center" alt="The Organisation ID in Radiam Connect" border={true} caption="The Organisation ID in the CA" src="https://files.readme.io/35deb7f7c41386d858bb4523a27375841a0cedd7ea8944e989d10c1fffc24b60-AppID.png" />

### Finding the Application ID

To find your Application ID, navigate to your Organisation in the CA and select Applications from the menu. Find your application and click the copy button for the application id  and paste into the ssa\_id field in your Postman Collection.

<Image align="center" alt="The Application ID in Radiam Connect." border={true} caption="The Application ID in the CA" src="https://files.readme.io/6449b978e324a0a006e8948093e26c4afd983dda3678bdad4e9d776da02cf179-AppId2.png" />

### Finding the Signing Certificate (KID)

To find your Application ID, navigate to your Organisation in the CA and select Applications from the menu. Open your organisation and open App Certificates. Click Copy for the KID associated with the rtssigning Key Type.

<Image align="center" alt="The KID in Radiam Connect" border={true} caption="The KID in the CA" src="https://files.readme.io/d8233c85bb1cd516af7e0fcf3060b20851e180b637cdcbbcd524be786631377b-KID.png" />

Paste the value from the CA into the KID variable in your Postman Collection.

### Finding your Client ID

To find your Application ID, navigate to your Organisation in the CA and select Applications from the menu. Click Copy on the Client ID field and paste it into the client\_id variable in your Postman Collection.

## Assign Transport Certificates to Postman

To use the FAPI Postman Collection, you will need to assign your transport certificates from the CA in Postman.

> 📘 Important Note
>
> This process will need to be completed four times for each of the hosts URLs, using the same certificates each time.
>
> The four hosts are:
>
> * matls-auth.directory.sandbox.threddid.com
> * uat-thredd.mtls.eu.authz.cloudentity.io
> * api.uat.threddpay.com
> * api-uat.thredd.com

To assign your certificates to the Postman Collection:

1. Click the Gears icon in the top-left corner of Postman and click **Settings**.

<Image align="center" alt="Figure 1: Settings option in the File menu" border={false} caption="Settings option in the Gears icon menu" src="https://files.readme.io/d23b0738fa4ed930d02cd9544409b0b87f3179211c7a62db25bdb23f35910ba5-Settings.png" width="50% " />

2. Click **Certificates**.
3. Click **Add Certificate**.
4. Enter the host into the Host field. See the above list for the hosts you need to enter.
5. Click **Select File** under CRT file and navigate to your PEM file. Double-click to add the file.
6. Click **Select File** under KEY file and navigate to your KEY file. Double-click to add the file.
7. Click **Add**.

When the certificates have been added, it should look something like this.

<Image align="center" alt="Figure 2: Certificates window in Postman." border={true} caption="Certificates window in Postman." src="https://files.readme.io/584d1892e35bfb74ae183577af1e0867d5a868dbd3c3597ecc1a829e0b55cf5a-Certs.png" width="50% " />

## Set Variables in Postman

There are multiple variables that you need to set up in Postman before you can use it. These are populated in the Variables tab of the Postman Collection.

<Image align="center" alt="Figure 3: Postman Collection Variables tab." border={false} caption="Figure 3: Postman Collection Variables tab." src="https://files.readme.io/f87931306790bcb6ca6132fd98da1611e3f8397289e9bf1379db1a32d835c6f4-Variables.png" width="75% " />

The following variables need to be populated to start using the Postman Collection:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Variable
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        client\_id
      </td>

      <td>
        This is either a UUID, or a URL with a UUID on the end.
        If it is an URL you must include the whole URL, for example `https://rp.directory.sandbox.threddid.com/openid_relying_party/abcdef01-0124-4567-ffaa-fedcba098731`.
        If it is a UUID, you just need to include the UUID. For example, abcdef01-0124-4567-ffaa-fedcba098731.
      </td>
    </tr>

    <tr>
      <td>
        kid
      </td>

      <td>
        The Key ID of the Signing Certificate.
      </td>
    </tr>

    <tr>
      <td>
        private\_key
      </td>

      <td>
        The Signing Certificate Private Key (which you will have created in Raidiam Connect).
        You must include the first and last lines
        \-----BEGIN PRIVATE KEY-----
        and
        \-----END PRIVATE KEY-----
      </td>
    </tr>

    <tr>
      <td>
        ssa
      </td>

      <td>
        The Software Statement Assertion (ssa) certificate, taken from Raidiam Connect.
      </td>
    </tr>
  </tbody>
</Table>

## Call Initial Setup Endpoints

The first endpoints you need to run are in the Setup folder. Cloudentity Well-Known and Raidiam Connect Well-Known only need to be run once, the first time you use the Postman Collection.

<Image align="center" alt="Figure 4: Setup folder in the Postman Collection." border={true} caption="Figure 4: Setup folder in the Postman Collection." src="https://files.readme.io/782444c8bd4a9dbbab0382f13855a9aec577d32db8f5a2683732d24ac34183e6-Setup.png" width="50% " />

Running Cloudentity Well-Known successfully returns a 200 response displaying the details of what's supported, such as the scopes that are enabled.

```json Example Cloudentity Well-Known response
{
    "issuer": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients",
    "authorization_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/authorize",
    "token_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/token",
    "jwks_uri": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/.well-known/jwks.json",
    "subject_types_supported": [
        "public",
        "pairwise"
    ],
    "response_types_supported": [
        "token"
    ],
    "claims_supported": [
        "address",
        "family_name",
        "pmid",
        "email",
        "profile",
        "updated_at",
        "picture",
        "name",
        "given_name",
        "phone_number_verified",
        "internalid",
        "gender",
        "website",
        "email_verified",
        "zoneinfo",
        "middle_name",
        "preferred_username",
        "pmcode",
        "nickname",
        "locale",
        "phone_number",
        "birthdate",
        "issuerid",
        "sub",
        "acr",
        "amr"
    ],
    "grant_types_supported": [
        "client_credentials",
        "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "urn:ietf:params:oauth:grant-type:token-exchange"
    ],
    "response_modes_supported": [
        "fragment",
        "form_post",
        "query.jwt",
        "fragment.jwt",
        "form_post.jwt",
        "jwt"
    ],
    "userinfo_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/userinfo",
    "introspection_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/introspect",
    "scopes_supported": [
        "bulkcard.read",
        "issuer.write",
        "bulkcard.write",
        "cards.sensitive",
        "fraud.write",
        "apata.write",
        "digitalchannel",
        "cards.encrypted",
        "3ds.read",
        "cards.write",
        "pin.write",
        "pin.read",
        "apata.read",
        "internal.write",
        "internal.read",
        "cards.read",
        "eds.read",
        "eds.write",
        "cts.read",
        "cts.write",
        "dcr_manage",
        "dcr_register",
        "introspect_tokens",
        "list_clients_with_access",
        "revoke_client_access",
        "revoke_tokens",
        "scamdetect",
        "ws",
        "fraud.read",
        "cvv.write",
        "cvv.read",
        "issuer.read",
        "address",
        "email",
        "offline_access",
        "openid",
        "phone",
        "profile",
        "transient_otp",
        "manage_consents",
        "manage_sessions",
        "manage_ss_profile",
        "manage_tokens",
        "view_consents",
        "view_sessions",
        "view_ss_profile"
    ],
    "token_endpoint_auth_methods_supported": [
        "private_key_jwt"
    ],
    "introspection_endpoint_auth_methods_supported": [
        "private_key_jwt"
    ],
    "introspection_endpoint_auth_signing_alg_values_supported": [
        "RS256",
        "ES256",
        "HS256",
        "PS256"
    ],
    "revocation_endpoint_auth_methods_supported": [
        "private_key_jwt"
    ],
    "revocation_endpoint_auth_signing_alg_values_supported": [
        "RS256",
        "ES256",
        "HS256",
        "PS256"
    ],
    "token_endpoint_auth_signing_alg_values_supported": [
        "RS256",
        "ES256",
        "HS256",
        "PS256"
    ],
    "userinfo_signing_alg_values_supported": [
        "none",
        "ES256"
    ],
    "id_token_signing_alg_values_supported": [
        "ES256"
    ],
    "id_token_encryption_alg_values_supported": [
        "RSA-OAEP",
        "RSA-OAEP-256"
    ],
    "id_token_encryption_enc_values_supported": [
        "A256GCM",
        "A128CBC-HS256"
    ],
    "request_parameter_supported": true,
    "request_uri_parameter_supported": true,
    "request_object_signing_alg_values_supported": [
        "RS256",
        "ES256",
        "PS256"
    ],
    "require_request_uri_registration": true,
    "claims_parameter_supported": true,
    "revocation_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/revoke",
    "registration_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/register",
    "backchannel_logout_supported": true,
    "backchannel_logout_session_supported": true,
    "frontchannel_logout_supported": false,
    "frontchannel_logout_session_supported": false,
    "end_session_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oidc/logout",
    "code_challenge_methods_supported": [
        "S256"
    ],
    "tls_client_certificate_bound_access_tokens": true,
    "backchannel_token_delivery_modes_supported": [
        "poll",
        "ping"
    ],
    "backchannel_authentication_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/backchannel/authentication",
    "backchannel_authentication_request_signing_alg_values_supported": [
        "RS256",
        "ES256",
        "PS256"
    ],
    "backchannel_user_code_parameter_supported": false,
    "mtls_endpoint_aliases": {
        "token_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/token",
        "revocation_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/revoke",
        "introspection_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/introspect",
        "pushed_authorization_request_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/par",
        "backchannel_authentication_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/backchannel/authentication",
        "userinfo_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/userinfo",
        "device_authorization_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/device/authorization",
        "registration_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/register"
    },
    "mtls_issuer": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients",
    "request_object_encryption_alg_values_supported": [
        "RSA-OAEP-256"
    ],
    "request_object_encryption_enc_values_supported": [
        "A256GCM",
        "A128CBC-HS256"
    ],
    "pushed_authorization_request_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/par",
    "require_pushed_authorization_requests": false,
    "device_authorization_endpoint": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/device/authorization",
    "authorization_signing_alg_values_supported": [
        "ES256"
    ],
    "authorization_encryption_alg_values_supported": [
        "RSA-OAEP",
        "RSA-OAEP-256"
    ],
    "authorization_encryption_enc_values_supported": [
        "A256GCM",
        "A128CBC-HS256"
    ],
    "authorization_response_iss_parameter_supported": false,
    "dpop_signing_alg_values_supported": [
        "PS256",
        "ES256"
    ],
    "verified_claims_supported": false
}
```

You also need to run the Raidiam Connect Well-Known endpoint, which retrieves essential Raidiam Connect endpoint locations. If successful, a 200 response is returned displaying the details of what's supported, such as the scopes that are enabled.

```json Example Raidiam Connect Well-Known response
{
    "acr_values_supported": [
        "urn:mace:incommon:iap:silver"
    ],
    "authorization_endpoint": "https://auth.directory.sandbox.threddid.com/auth",
    "device_authorization_endpoint": "https://auth.directory.sandbox.threddid.com/device/auth",
    "claims_parameter_supported": true,
    "claims_supported": [
        "sub",
        "email",
        "email_verified",
        "phone_number",
        "phone_number_verified",
        "address",
        "birthdate",
        "family_name",
        "gender",
        "given_name",
        "locale",
        "middle_name",
        "name",
        "nickname",
        "picture",
        "preferred_username",
        "profile",
        "updated_at",
        "website",
        "zoneinfo",
        "trust_framework_profile",
        "acr",
        "sid",
        "auth_time",
        "iss"
    ],
    "code_challenge_methods_supported": [
        "S256"
    ],
    "end_session_endpoint": "https://auth.directory.sandbox.threddid.com/session/end",
    "grant_types_supported": [
        "implicit",
        "authorization_code",
        "refresh_token",
        "client_credentials"
    ],
    "id_token_signing_alg_values_supported": [
        "PS256"
    ],
    "issuer": "https://auth.directory.sandbox.threddid.com",
    "jwks_uri": "https://auth.directory.sandbox.threddid.com/jwks",
    "registration_endpoint": "https://auth.directory.sandbox.threddid.com/reg",
    "response_modes_supported": [
        "form_post",
        "fragment",
        "query",
        "jwt",
        "query.jwt",
        "fragment.jwt",
        "form_post.jwt"
    ],
    "response_types_supported": [
        "code id_token",
        "code",
        "id_token",
        "none"
    ],
    "scopes_supported": [
        "openid",
        "offline_access",
        "profile",
        "email",
        "address",
        "phone",
        "trust_framework_profile",
        "directory:software"
    ],
    "subject_types_supported": [
        "public",
        "pairwise"
    ],
    "token_endpoint_auth_methods_supported": [
        "private_key_jwt",
        "tls_client_auth"
    ],
    "token_endpoint_auth_signing_alg_values_supported": [
        "PS256"
    ],
    "token_endpoint": "https://auth.directory.sandbox.threddid.com/token",
    "pushed_authorization_request_endpoint": "https://auth.directory.sandbox.threddid.com/request",
    "request_object_signing_alg_values_supported": [
        "PS256"
    ],
    "request_parameter_supported": true,
    "request_uri_parameter_supported": false,
    "userinfo_endpoint": "https://auth.directory.sandbox.threddid.com/me",
    "authorization_signing_alg_values_supported": [
        "PS256"
    ],
    "introspection_endpoint": "https://auth.directory.sandbox.threddid.com/token/introspection",
    "revocation_endpoint": "https://auth.directory.sandbox.threddid.com/token/revocation",
    "id_token_encryption_alg_values_supported": [
        "A128KW",
        "A256KW",
        "ECDH-ES",
        "RSA-OAEP",
        "dir"
    ],
    "id_token_encryption_enc_values_supported": [
        "A128CBC-HS256",
        "A128GCM",
        "A256CBC-HS512",
        "A256GCM"
    ],
    "authorization_encryption_alg_values_supported": [
        "A128KW",
        "A256KW",
        "ECDH-ES",
        "RSA-OAEP",
        "dir"
    ],
    "authorization_encryption_enc_values_supported": [
        "A128CBC-HS256",
        "A128GCM",
        "A256CBC-HS512",
        "A256GCM"
    ],
    "request_object_encryption_alg_values_supported": [
        "A128KW",
        "A256KW",
        "dir",
        "ECDH-ES",
        "RSA-OAEP"
    ],
    "request_object_encryption_enc_values_supported": [
        "A128CBC-HS256",
        "A128GCM",
        "A256CBC-HS512",
        "A256GCM"
    ],
    "tls_client_certificate_bound_access_tokens": true,
    "claim_types_supported": [
        "normal"
    ],
    "mtls_endpoint_aliases": {
        "token_endpoint": "https://matls-auth.directory.sandbox.threddid.com/token",
        "revocation_endpoint": "https://matls-auth.directory.sandbox.threddid.com/token/revocation",
        "introspection_endpoint": "https://matls-auth.directory.sandbox.threddid.com/token/introspection",
        "device_authorization_endpoint": "https://matls-auth.directory.sandbox.threddid.com/device/auth",
        "registration_endpoint": "https://matls-auth.directory.sandbox.threddid.com/reg",
        "userinfo_endpoint": "https://matls-auth.directory.sandbox.threddid.com/me",
        "pushed_authorization_request_endpoint": "https://matls-auth.directory.sandbox.threddid.com/request",
        "backchannel_authentication_endpoint": "https://matls-auth.directory.sandbox.threddid.com/backchannel"
    }
}
```

<br />

## Run Dynamic Client Registration (DCR)

The next step is to register your client with the authorisation server, which can be done dynamically using the Postman Collection. This enables you to register an OAuth client with CloudEntity (the authorisation server) using an API call. This requires a Software Statement Assertion (ssa), which is returned with Postman.

<Image align="center" alt="Figure 5: DCR UAT Mutual TLS endpoint." border={true} caption="Figure 5: DCR UAT Mutual TLS endpoint." src="https://files.readme.io/27eb46311ea92d86f3dd65d7988db8622ae0e66f37b1069cc1e89b00027e6f10-DCR.png" width="50% " />

> 📘 Note
>
> The SSA can be obtained from the CA.

You must execute the requests in the following order:

* Run **2.1 RC Access Token** first to retrieve the Raidiam Connect Access Token
* Run **2.2 Get RC SSA** second to obtain the Software Statement Assertion (SSA)
* Run **2.3 Dynamic Client Registration** third to register the OAuth Client in Cloudentity

If the 2.3 Dynamic Client Registration is successful, a 201 response is returned indicating that the the client has been registered successfully.

```json Example Dynamic Client Registration response
{
    "client_name": "Test Company App 1",
    "description": "Application Description",
    "client_uri": "",
    "logo_uri": "https://example.com/logo.png",
    "policy_uri": "",
    "tos_uri": "",
    "organisation_id": "",
    "client_id": "https://rp.directory.sandbox.threddid.com/openid_relying_party/38b2f9a4-1bf0-4d84-832f-853529d88ad7",
    "application_type": "service",
    "application_types": [
        "service",
        "dcr"
    ],
    "redirect_uris": [
        "https://example.com/callback"
    ],
    "grant_types": [
        "client_credentials"
    ],
    "response_types": [
        "token"
    ],
    "scope": "cards.read cards.write pin.read pin.write cvv.read cvv.write bulkcard.read bulkcard.write cards.encrypted",
    "scopes": [
        "cards.read",
        "cards.write",
        "pin.read",
        "pin.write",
        "cvv.read",
        "cvv.write",
        "bulkcard.read",
        "bulkcard.write",
        "cards.encrypted"
    ],
    "audience": [
        "https://rp.directory.sandbox.threddid.com/openid_relying_party/38b2f9a4-1bf0-4d84-832f-853529d88ad7"
    ],
    "token_endpoint_auth_method": "private_key_jwt",
    "revocation_endpoint_auth_method": "private_key_jwt",
    "introspection_endpoint_auth_method": "private_key_jwt",
    "token_exchange": {
        "actor_claims": null
    },
    "token_endpoint_auth_signing_alg": "",
    "jwks": {
        "keys": []
    },
    "jwks_uri": "https://keystore.directory.sandbox.threddid.com/fc507376-d795-45c2-bc5c-2afb3bd2bea8/38b2f9a4-1bf0-4d84-832f-853529d88ad7/application.jwks",
    "request_object_signing_alg": "RS256",
    "request_object_encryption_alg": "",
    "request_object_encryption_enc": "",
    "request_uris": [],
    "client_id_issued_at": 1727107690,
    "created_at": "2024-09-23T16:08:10.183352833Z",
    "updated_at": "2024-09-23T16:08:10.183352833Z",
    "client_secret_expires_at": 0,
    "sector_identifier_uri": "https://keystore.directory.sandbox.threddid.com/fc507376-d795-45c2-bc5c-2afb3bd2bea8/38b2f9a4-1bf0-4d84-832f-853529d88ad7/redirect_uris.json",
    "userinfo_signed_response_alg": "none",
    "id_token_signed_response_alg": "ES256",
    "id_token_encrypted_response_alg": "",
    "id_token_encrypted_response_enc": "",
    "tls_client_certificate_bound_access_tokens": true,
    "tls_client_auth_subject_dn": "",
    "tls_client_auth_san_dns": "",
    "tls_client_auth_san_uri": "",
    "tls_client_auth_san_ip": "",
    "tls_client_auth_san_email": "",
    "privacy": {
        "scopes": null
    },
    "subject_type": "pairwise",
    "backchannel_token_delivery_mode": "",
    "backchannel_client_notification_endpoint": "",
    "backchannel_authentication_request_signing_alg": "",
    "backchannel_user_code_parameter": false,
    "require_pushed_authorization_requests": false,
    "authorization_signed_response_alg": "ES256",
    "authorization_encrypted_response_alg": "",
    "authorization_encrypted_response_enc": "",
    "dpop_bound_access_tokens": false,
    "authorization_details_types": null,
    "post_logout_redirect_uris": [],
    "app_url": "",
    "backchannel_logout_uri": "",
    "backchannel_logout_session_required": false,
    "client_secret": "36ZlLSc8NOoL6Gln4-q9dn8wsuvlNIUb5ZsTTRHD7a8",
    "hashed_secret": "e99c5fa08bdedc7c87226cd5f75a07986cdc21f42abde973675a29a78fbd6ccde252bc60bf20efefaf21b691ed8162b0984b02da6cf6400d01fb782f8efadac5263d71a14290255a9869794c5ca2656819c397daf5ae2a78109637367183f7041a7cf3b78dba7b4bdb7deddc89ea1fc3304b13a7b60c489f564389efb029c648",
    "software_id": "38b2f9a4-1bf0-4d84-832f-853529d88ad7",
    "software_version": "1.00",
    "software_statement": "eyJraWQiOiJzaWduZXIiLCJ0eXAiOiJKV1QiLCJhbGciOiJQUzI1NiJ9.eyJzb2Z0d2FyZV9zdGF0ZW1lbnRfcm9sZXMiOltdLCJvcmdfandrc190cmFuc3BvcnRfdXJpIjoiaHR0cHM6Ly9rZXlzdG9yZS5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vZmM1MDczNzYtZDc5NS00NWMyLWJjNWMtMmFmYjNiZDJiZWE4L3RyYW5zcG9ydC5qd2tzIiwiYXBpX3dlYmhvb2tfdXJpcyI6W10sIm9yZ19zdGF0dXMiOiJBY3RpdmUiLCJsb2dvX3VyaSI6Imh0dHBzOi8vZXhhbXBsZS5jb20vbG9nby5wbmciLCJyb2xlcyI6W10sImlzcyI6InRocmVkZCBzYW5kYm94IFNTQSBpc3N1ZXIiLCJvcmdfandrc190cmFuc3BvcnRfaW5hY3RpdmVfdXJpIjoiaHR0cHM6Ly9rZXlzdG9yZS5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vZmM1MDczNzYtZDc5NS00NWMyLWJjNWMtMmFmYjNiZDJiZWE4L2luYWN0aXZlL3RyYW5zcG9ydC5qd2tzIiwiY2xpZW50X2lkIjoiaHR0cHM6Ly9ycC5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vb3BlbmlkX3JlbHlpbmdfcGFydHkvMzhiMmY5YTQtMWJmMC00ZDg0LTgzMmYtODUzNTI5ZDg4YWQ3IiwiY2xpZW50X2Rlc2NyaXB0aW9uIjoiQSB0ZXN0IGFwcCBmb3IgQ29tcGFueSAxIiwibW9kZSI6IkxpdmUiLCJzb2Z0d2FyZV9pZCI6IjM4YjJmOWE0LTFiZjAtNGQ4NC04MzJmLTg1MzUyOWQ4OGFkNyIsInNvZnR3YXJlX3ZlcnNpb24iOiIxLjAwIiwib3JnX25hbWUiOiJUZXN0IENvbXBhbnkgMSIsInNvZnR3YXJlX2ZsYWdzIjp7fSwib3JpZ2luX3VyaXMiOltdLCJjbGllbnRfbmFtZSI6IlRlc3QgQ29tcGFueSBBcHAgMSIsImlhdCI6MTcyNzA4MDYwOCwiandrc190cmFuc3BvcnRfdXJpIjoiaHR0cHM6Ly9rZXlzdG9yZS5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vZmM1MDczNzYtZDc5NS00NWMyLWJjNWMtMmFmYjNiZDJiZWE4LzM4YjJmOWE0LTFiZjAtNGQ4NC04MzJmLTg1MzUyOWQ4OGFkNy90cmFuc3BvcnQuandrcyIsIm9yZ2FuaXNhdGlvbl90YWdzIjpbXSwic3ViamVjdF90eXBlIjoicGFpcndpc2UiLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vZXhhbXBsZS5jb20vY2FsbGJhY2siXSwic2VjdG9yX2lkZW50aWZpZXJfdXJpIjoiaHR0cHM6Ly9rZXlzdG9yZS5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vZmM1MDczNzYtZDc5NS00NWMyLWJjNWMtMmFmYjNiZDJiZWE4LzM4YjJmOWE0LTFiZjAtNGQ4NC04MzJmLTg1MzUyOWQ4OGFkNy9yZWRpcmVjdF91cmlzLmpzb24iLCJvcmdfandrc19pbmFjdGl2ZV91cmkiOiJodHRwczovL2tleXN0b3JlLmRpcmVjdG9yeS5zYW5kYm94LnRocmVkZGlkLmNvbS9mYzUwNzM3Ni1kNzk1LTQ1YzItYmM1Yy0yYWZiM2JkMmJlYTgvaW5hY3RpdmUvYXBwbGljYXRpb24uandrcyIsIm9yZ2FuaXNhdGlvbl9mbGFncyI6e30sImp3a3NfdHJhbnNwb3J0X2luYWN0aXZlX3VyaSI6Imh0dHBzOi8va2V5c3RvcmUuZGlyZWN0b3J5LnNhbmRib3gudGhyZWRkaWQuY29tL2ZjNTA3Mzc2LWQ3OTUtNDVjMi1iYzVjLTJhZmIzYmQyYmVhOC8zOGIyZjlhNC0xYmYwLTRkODQtODMyZi04NTM1MjlkODhhZDcvaW5hY3RpdmUvdHJhbnNwb3J0Lmp3a3MiLCJlbnZpcm9ubWVudCI6IlNhbmRib3giLCJvcmdfaWQiOiJmYzUwNzM3Ni1kNzk1LTQ1YzItYmM1Yy0yYWZiM2JkMmJlYTgiLCJvcmdfandrc191cmkiOiJodHRwczovL2tleXN0b3JlLmRpcmVjdG9yeS5zYW5kYm94LnRocmVkZGlkLmNvbS9mYzUwNzM3Ni1kNzk1LTQ1YzItYmM1Yy0yYWZiM2JkMmJlYTgvYXBwbGljYXRpb24uandrcyIsImp3a3NfaW5hY3RpdmVfdXJpIjoiaHR0cHM6Ly9rZXlzdG9yZS5kaXJlY3Rvcnkuc2FuZGJveC50aHJlZGRpZC5jb20vZmM1MDczNzYtZDc5NS00NWMyLWJjNWMtMmFmYjNiZDJiZWE4LzM4YjJmOWE0LTFiZjAtNGQ4NC04MzJmLTg1MzUyOWQ4OGFkNy9pbmFjdGl2ZS9hcHBsaWNhdGlvbi5qd2tzIiwib3JnX251bWJlciI6IjAwMDAwMDAxIiwiandrc191cmkiOiJodHRwczovL2tleXN0b3JlLmRpcmVjdG9yeS5zYW5kYm94LnRocmVkZGlkLmNvbS9mYzUwNzM3Ni1kNzk1LTQ1YzItYmM1Yy0yYWZiM2JkMmJlYTgvMzhiMmY5YTQtMWJmMC00ZDg0LTgzMmYtODUzNTI5ZDg4YWQ3L2FwcGxpY2F0aW9uLmp3a3MiLCJzdGF0dXMiOiJBY3RpdmUiLCJvcmdhbmlzYXRpb25fY29tcGV0ZW50X2F1dGhvcml0eV9jbGFpbXMiOlt7ImF1dGhvcmlzYXRpb25fZG9tYWluIjoiVGhyZWRkIiwiYXV0aG9yaXNhdGlvbnMiOltdLCJyZWdpc3RyYXRpb25faWQiOiIxMjM0NTY3OCIsImF1dGhvcml0eV9uYW1lIjoiVGhyZWRkIFRlY2huaWNhbCBBdXRob3JpdHkiLCJhdXRob3JpdHlfaWQiOiI5ZjUxZmM5Yi0wMDBiLTQ1ZGEtOTkwMy04NjViZTFkYjM3NjAiLCJhdXRob3Jpc2F0aW9uX3JvbGUiOiJ0aHJlZGQtYXBpLXByb3ZpZGVyLXJvbGUiLCJhdXRob3JpdHlfY29kZSI6IlRUQSIsInN0YXR1cyI6IkFjdGl2ZSJ9XX0.R1WcW5Afap9SlG_goAM14diqeW0pkq7nDY6iUj3Xj71j4S4zB1r5qJhaTk4QiZgdI8VNdZE9pssgkB_xeDpBfvTYStOTbuvQMTDk-wJETn87z8AnhIpWWbkCa3osbQUnWsqzhB0tsNojGsHAFT4eQ3c_o2L7PmF_-6ryU3lF5RSuA-TOuCV1elQ_hOk3QuNO4v3fU1B57PJ8rmq9QU-qAWM6zmMirE4GYehETODlF0kW5a5uNlMIUxJdZQGhUk6iJaaoF6nmsFPz167e3f3OEW92HZJyRXKVOdumZikUTdkTOTReSokulmidT5vfk_ctv_cLGVrmtc6x6DrUcWNbTQ",
    "dynamically_registered": true,
    "registration_access_token": "fFaCcKimvvqhnzax4s1XhPzHIK-7YqDePeHu5Pi3ejY.pmS1Wci--v56ArNeVZz2UvIc79bdOwtgBWOCyThB0QU",
    "registration_client_uri": "https://uat-thredd.mtls.eu.authz.cloudentity.io/uat-thredd/confidential-clients/oauth2/register/https%3A%2F%2Frp.directory.sandbox.threddid.com%2Fopenid_relying_party%2F38b2f9a4-1bf0-4d84-832f-853529d88ad7",
    "registration_access_token_expires_in": 0
}
```

> 📘 Note
>
> If you update your client with the Dynamic Client Registration (DCR) endpoints, for example by using the PUT request, the metadata will be deleted and you will need to be set up by Thredd again.
>
> For more information, see [RFC7592](https://datatracker.ietf.org/doc/html/rfc7592).

## Generate an Access Token

To generate an access token using the Postman Collection, expand the Authorisation folder to expose Get Access Token endpoint

<Image align="center" className="border" border={true} width="50% " src="https://files.readme.io/2207784a1de89e520116415c4a3dfcea418d306e00394d1ea41e62c39cb987c8-AccessToken.png" />

The body of the request should be automatically generated. Click **Send** to call the token endpoint.

The access token is returned in the response and is stored in the variables of the Postman Collection. You can now use the other endpoints in the collection until the token expires.

```json Example Get Access Token response
{
    "access_token": "eyJhbGciOiJFUzI1NiIsImtpZCI6IjUzMzQ0OTcxMzg4MzYwMTA0MDE1MDE4ODMzNTYxOTI5OTgxMTIxIiwidHlwIjoiSldUIn0.eyJhaWQiOiJjb25maWRlbnRpYWwtY2xpZW50cyIsImFtciI6W10sImF1ZCI6WyJodHRwczovL3JwLmRpcmVjdG9yeS5zYW5kYm94LnRocmVkZGlkLmNvbS9vcGVuaWRfcmVseWluZ19wYXJ0eS8zOGIyZjlhNC0xYmYwLTRkODQtODMyZi04NTM1MjlkODhhZDciLCJzcGlmZmU6Ly91YXQtdGhyZWRkLmV1LmF1dGh6LmNsb3VkZW50aXR5LmlvL3VhdC10aHJlZGQvY29uZmlkZW50aWFsLWNsaWVudHMvY29uZmlkZW50aWFsLWNsaWVudHMtb2F1dGgyIl0sImNuZiI6eyJ4NXQjUzI1NiI6IlNUX28wQm9pUlRCQ3pvdWlPUHNRbDlNaE1OY0kyRENTNExPZndaOW9naEUifSwiZXhwIjoxNzI3MTA4MzQ3LCJpYXQiOjE3MjcxMDc3NDcsImlkcCI6IiIsImlzcyI6Imh0dHBzOi8vdWF0LXRocmVkZC5ldS5hdXRoei5jbG91ZGVudGl0eS5pby91YXQtdGhyZWRkL2NvbmZpZGVudGlhbC1jbGllbnRzIiwianRpIjoiMzQxYmI3NTgtNWJiNS00OWU4LThjMzctNTE1YmQ0NjU2YmQ3IiwibmJmIjoxNzI3MTA3NzQ3LCJzY3AiOlsiYnVsa2NhcmQucmVhZCIsImJ1bGtjYXJkLndyaXRlIiwiY2FyZHMuZW5jcnlwdGVkIiwiY2FyZHMucmVhZCIsImNhcmRzLndyaXRlIiwiY3Z2LnJlYWQiLCJjdnYud3JpdGUiLCJwaW4ucmVhZCIsInBpbi53cml0ZSJdLCJzdCI6InB1YmxpYyIsInN1YiI6Imh0dHBzOi8vcnAuZGlyZWN0b3J5LnNhbmRib3gudGhyZWRkaWQuY29tL29wZW5pZF9yZWx5aW5nX3BhcnR5LzM4YjJmOWE0LTFiZjAtNGQ4NC04MzJmLTg1MzUyOWQ4OGFkNyIsInRpZCI6InVhdC10aHJlZGQifQ.-7ea73vZqPJVijOeuRFzgkP3nzVTWDAXSYF7WJLWNclCb6svfh-147f2Fc5Uc-ZvKeF7r5d-o3KtBkZz9u5I8g",
    "expires_in": 599,
    "scope": "bulkcard.read bulkcard.write cards.encrypted cards.read cards.write cvv.read cvv.write pin.read pin.write",
    "token_type": "bearer"
}
```

<br />

> 📘 Note
>
> For information on Radiam Connect, see the [Connecting to Thredd](https://docs.thredd.com/Connecting_to_Thredd_Guide.htm) guide.

## Keen to get started?

You can download a sample postman collection below.

<HTMLBlock>
  {`
  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style> 
  .button {
    background-color: #0c0589;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 10px;
  }

  .button:hover {
    background-color: #63d0fb;
  }
  </style>
  </head>
  <body>
    <a href="https://docs.thredd.com/rest/Thredd_REST_FAPI_v1.12.postman_collection.json" download>
  		<button class="button">Right-click to download mTLS Postman Collection</button>
    </a>
  </body>
  </html>
  `}
</HTMLBlock>