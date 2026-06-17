# Set up Preparation and Steps

This guide helps you prepare and complete setting up your connection and identity and access management for Thredd services. This summary focuses on a typical setup with a TLS or mTLS connection to API Hub (REST APIs) via Thredd Secure Framework and Thredd Portal, and EHI.

To access SOAP APIs, see [Creating Client Transport Certificates for SOAP APIs](Creating_SOAP_Client_Transport_Certificates.htm). For VPN setups, see [Connecting with AWS and VPN](AWS.htm).

## Thredd Portal

Thredd Portal is the main entry point to onboard to Thredd and access Thredd services. It provides support for multiple roles, including a Super Admin and at least one Organisation Admin. It enables a Super Admin to set up and manage the identity and access management for their organisation, applications, and users. Organisation Admins have similar privileges, but do not manage users.

Thredd Portal's access management features include:

* Organisation, application and identity management â users with a Super Admin or Organisation Admin role can create and manage applications, OAuth clients, SSO details, certificates, generate and validate access tokens, and more.
* User management â Super Admin users can invite users to onboard to Thredd and manage user roles, permissions, and access.
* Supports Multi-Factor Authentication (MFA), Single Sign-On, password-based sign-on, multiple identity providers, SAML and OIDC.

A Super Admin must first successfully set up their access and log in to Thredd Portal before configuring and testing access to Thredd's API Hub and REST APIs. The set up process comprises several stages, depending on the different services that you use.

### Before you begin

You must provide the details of your organisation and the user that will operate as the Super Admin to Thredd. Your Thredd Implementation representative coordinates with you about this and registers these details with the Thredd platform.

As the Super Admin user, you can begin the process of connecting to Thredd's Secure Framework once you receive confirmation from Thredd.

### Configuring your set up in a test environment first

For best practice, Thredd recommends that you first set up your organisation's access in the UAT (User Acceptance Test) environment. This enables you to test and verify that your organisation can use Thredd applications and API endpoints successfully.

Once you have verified that your setup and testing in the UAT environment is satisfactory, you can coordinate with Thredd and prepare to set up your Production environment. You will need to repeat all of these set up steps for your Production environment. This includes requesting new certificates and ensuring that environment-specification configurations are correct.

## Summary of set up steps

Setting up access to Thredd starts with the Super Admin logging in to Thredd Portal and setting up their access to the Thredd platform. The Super Admin can then set up access for other users, but can choose to do this before or after setting up access to Thredd APIs and API Hub.

Here is an overall summary of the different stages of the set up process â use the links to visit the step-by-step guidance for each stage.

### Step 1: Set up the Super Admin in Thredd Portal

The Super Admin user will receive a welcome email inviting them to log in to Thredd Portal. They must set up their access to Thredd Portal before they can manage the access for their organisation, application and users.

As the Super Admin, you will need to add your organisation's identity provider details in Thredd Portal, enabling authentication using your own Identity Provider (IdP). If your organisation does not use an IdP, Thredd's own provision can act as the IdP.

You can choose one of the following methods for users to log in to Thredd services:

* Single Sign-On (SSO) â this involves adding an SSO configuration in Thredd Portal and inviting users via your identity provider. This is not required, but Thredd recommends it to help automate user onboarding and management.
* Email address and password â a Super Admin manually adds each user in Thredd Portal and using its invite feature to ask them to log in.

For an overview of Thredd Portal and the set up process, see [Thredd Portal overview](Thredd_Portal.htm).

This guidance outlines setting up the Super Admin for the first time and additional users. However, a Super Admin does not have to add users to Thredd Portal straight away. Instead, the Admin can choose to add the organisation's SSO details (if using SSO), create Client certificates, and test access to Thredd REST APIs first. A Super Admin can later return to this step to add the organisation's users.

### Step 2: Create a new Application and OAuth Client in Thredd Portal

Before you can access Thredd's REST API, you must create an application and an OAuth Client in Thredd Portal to register it and receive a client ID. You can then request client credentials for your application and configure your application and REST interface (such as Postman) to provide them when making API calls. This allows Thredd to verify your identity and grant access.

See [Creating an Application and OAuth Client.](creating-an-appliction-and-oauth-client.htm)

### Step 3: Create credentials to access the REST API

You need to create the necessary credentials to access Thredd's REST APIs, and configure your client application to provide these credentials when making API calls.

Thredd offers two Client Authentication methods via its Authorisation Server. The credentials you require depend on the authentication method that you have chosen to use.

* Client Secret â requires an access token that you can request from Thredd's OAuth Token endpoint.
* Private Key JWT â requires an access token from Thredd, and Signing Certificate, which an Admin user can obtain from Thredd Portal, to create and register a private key. You must generate a Client Assertion, a JSON Web Token (JWT) that is signed by your private key.

If you are using an mTLS connection, your application must also present a Transport Certificate from Thredd. Thredd adopts a self-service approach, which allows an Admin user to independently request and manage certificates via Thredd Portal.

See [Connecting to the REST APIs](connecting-to-the-rest-apis.htm).

### Step 4: Configure the latest Postman collection to test Thredd's REST APIs via API Hub

You can access Thredd's API Hub and REST APIs over TLS or mTLS. Thredd provides separate Postman Collections for TLS and mTLS, which enable you to use Postman to test using the Thredd REST APIs in a UAT environment.

To use the collection, you need to configure Postman with the appropriate environment variables and credentials. Refer to the guides that matches how you are connecting to Thredd APIs:

* For TLS connections: [Using the Postman Collection to call REST APIs over TLS](setting-up-postman-to-access-rest-apis-for-tls.htm)
* For mTLS connections: [Using the Postman Collection to call REST APIs over mTLS](setting-up-postman-to-access-rest-apis-for-mtls.htm)

### Step 5: Set up access to Thredd Portal for your organisation's users

A Super Admin must invite your organisation's users to log in to Thredd applications, using either:

* Single Sign-On (SSO) â this involves inviting users to log in to Thredd Portal via your identity provider, providing you have set up SSO in Thredd Portal. Make sure that each user receives an email inviting them to activate their account. Once a user has logged in to Thredd Portal, it registers them in the system, and a Super Admin can assign the appropriate roles to the user, completing the user's profile.
* Email address and password â this involves manually adding each user, assigning an appropriate role, and sending an invite to them via Thredd Portal using its built-in tool. The user receives an email inviting them to activate their account, set a password and log in to Thredd Portal. Once complete, the user can log in to other Thredd applications.

For more information, see [Connecting to Thredd Portal](Thredd_Portal.htm).

### Step 6: Set up EHI and other Thredd applications

Secure connections are required to access the following Thredd applications:

* External Host Interface (EHI)
* SOAP API (if relevant to you)

### External Host Interface (EHI)

The External Host Interface (EHI) offers a way to exchange transactional data between the Thredd processing system and the Program Manager's externally-hosted systems. All transaction data processed by Thredd is transferred to the external host system via EHI in real time.

EHI provides two main functions:

* a real-time transaction notification data feed
* payment authorisation control

You can use EHI with either a TLS or mTLS connection. Follow the guidance that matches the connection method you will use for the EHI.

#### Set up summary for EHI with a TLS connection

1. Obtain and install a Server certificate from the Certificate Authority that you want to use.
2. Log in to Thredd Portal and obtain the details of Thredd's JWKS endpoint.
3. Integrate with the JWKS endpoint.
4. Implement signature validation logic.
5. Test your EHI endpoint for TLS communication.
6. Inform Thredd that you are ready to use the EHI application.

For more information, see [Setting up EHI for TLS connections and signed payloads](setting-up-ehi-for-tls-and-signed-payloads.htm).

#### Set up summary for EHI with an mTLS connection

1. Obtain a Server certificate from the Certificate Authority that you want to use. Install the Server and Client Certificates.
2. Download and install the EHI Trust Chain from Thredd, which contains Root Certificates and Issuing Certificates from Thredd.
3. Store the Root and Issuing Certificates on your mTLS termination point.
4. Ensure that your mTLS termination point has access to Thredd's Online Certificate Status Protocol (OCSP) responder.
5. Test the Client and Server Certificates on your EHI endpoint for mTLS communication.
6. Provide the EHI endpoint details to Thredd and inform Thredd that you are ready to use the EHI application.

For more information, see [Setting up EHI for mTLS connections](setting-up-ehi-for-mtls.htm).

Once you have set up your TLS or mTLS connection for the EHI, see the [EHI Guide (JSON version)](https://docs.thredd.com/EHI_Guide_JSON.htm) or [EHI Guide (XML version).](https://docs.thredd.com/ehi/Content/Home_XML.htm)

### SOAP API

Thredd's SOAP APIs are secured using mTLS. If you are using the SOAP APIs, you will need to create Transport Certificates. For more information, see [Creating Client Transport Certificates for SOAP APIs](Creating_SOAP_Client_Transport_Certificates.htm). Only refer to this information if Thredd has confirmed that you will use the SOAP APIs; otherwise, you can ignore this information.

### Other services

Services such as Fraud Transaction Monitoring and 3D-Secure do not require you to set up secure connections via Thredd Secure Framework.