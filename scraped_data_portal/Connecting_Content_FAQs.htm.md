# General FAQs

The following detailed list of FAQs focuses on the Thredd Secure Framework and its components, and related topics. These components include Thredd Portal and Thredd CA.

## Overview

#### What is the Secure Framework?

The Thredd Secure Framework is a combination of components that enable secure access to Thredd's resources using a common identity store. These include Thredd Portal, Thredd CA, and mTLS termination (for those clients using mTLS). It ensures secure communication and access control through features like mTLS, OAuth, and certificate-based authentication. For more information, see [Thredd Secure Framework](Getting_Started/thredd-secure-framework.htm).

#### What is mTLS and how is it used in the Secure Framework?

mTLS (Mutual Transport Layer Security) is a security protocol used to establish trust between clients and servers.

* Transport Certificates issued by Thredd CA are used to establish secure connections.
* mTLS Termination requires on-premise infrastructure to establish Trust Chains to ensure certificates originate from legitimate sources.
* It is used in the External Host Interface (EHI) setup, and works in the background for the SOAP and REST API setups.

For more information about Mutual TLS, see [Mutual TLS explained](Getting_Started/mutual-tls-explained.htm).

#### What is the role of Cloudentity in the Secure Framework?

Thredd previously used Cloudentity as a Software as a Service (SaaS) capability to act as an Identity Provider (IdP), OAuth OpenID Provider (OP), and Policy Decision Point (PDP). However, Thredd has enhanced its Secure Framework to allow clients to manage access to Thredd services via Thredd Portal. As a result, Thredd has phased out use of Cloudentity within the Thredd Secure Framework. For more information, see [Thredd Secure Framework](Getting_Started/thredd-secure-framework.htm).

#### Can I still use or request a VPN setup?

No, Thredd does not support new VPN setups. You must connect securely to Thredd using the Secure Framework.

## Certificates

#### What is Thredd CA, and what certificates does it provide?

Thredd CA is Threddâs Certificate Authority responsible for creating and managing certificates. Users with an Admin role can request and revoke certificates from within Thredd Portal. It provides:

* **Transport Certificates:** For secure connections between resources.
* **Signing Certificates:** For private\_key\_jwt authentication, signed messages, and non-repudiation.
* **Root and Issuing Certificates:** Bundled in the EHI Trust Chain, for verifying Transport Certificates in EHI setups that use mTLS.

#### What certificates are required for different Thredd applications?

The certificates required for various Thredd applications are as follows:

* **REST API:** Requires Signing Certificates for TLS and mTLS connections; mTLS also requires Transport Certificates.
* **SOAP API:** Requires only Transport Certificates.
* **External Host Interface (EHI):** Requires Root and Issuing Certificates (available in Thredd Trust Chain).
* **Thredd Portal:** Pre-installed Transport Certificates.
* **Smart Client:** Bundled Transport Certificates in the installer.

For more information, see the following sections that are related to requesting certificates in the Connecting to Thredd Guide:

* [Creating an Application and OAuth Client](Getting_Started/creating-an-appliction-and-oauth-client.htm)
* [Requesting certificates for applications using TLS](Getting_Started/requesting-a-signing-certificate-for-private-key-jwt.htm)
* [Requesting certificates for applications using mTLS](Getting_Started/requesting-certificates-for-mtls-connections.htm)
* [Setting up EHI for mTLS connections](Getting_Started/setting-up-ehi-for-mtls.htm)

## Single Sign-On

#### How does SSO work in the Secure Framework?

SSO capabilities are provided through Thredd Portal, allowing federated authentication. This enables users to authenticate once and gain access to multiple Thredd resources instead of logging in separately for each service. You can also configure your own IdP provider for SSO.

See the following section within the Connecting to Thredd Guide: [Setting up Single Sign-On access for users](Getting_Started/setting-up-sso-and-users.htm)

## External Host Interface

#### How do I set up mTLS for EHI?

**Step 1:** Set up certificates.

You need a Server Certificate and the EHI Trust Chain to enable mTLS.

1. Set up Server Certificates:
   1. Obtain a Server Certificate from a trusted Certificate Authority (CA) vendor, such as Verizon, Digicert, or Amazon Web Services.
   2. Install the following certificates on your EHI listening endpoint:
      * Server or Leaf Certificate: Issued to individual servers by a CA. This certificate is the "leaf" of the hierarchical tree of trust.
      * Intermediate or Issuing Certificate: Represents the CA that issued the server certificate.
      * Root Certificate: The trusted root of the CA chain.

2. Set up Client certificates. Thredd presents its Transport Certificate during the connection handshake. Your system must validate this certificate against the CA Thredd Trust Chain (Root and Issuing Certificates).

**Step 2:** Test the mTLS Connection.

1. Test the connection to ensure the mTLS handshake is successful.
2. Verify that your system can receive and process EHI messages securely.

**Step 3:** Add Optional Security Enhancements

To further secure your mTLS setup, consider implementing the following:

1. IP Address Allowlist: Add Thredd's fixed IP address to your allow list to ensure only authorised traffic is accepted.
2. Certificate Pinning: Implement certificate pinning to block requests made with incorrect certificates.

For more information, see [Setting up EHI for mTLS connections](Getting_Started/setting-up-ehi-for-mtls.htm).

## Postman Setup

#### How do I use Postman to test the Secure Framework?

**Prerequisites**

* Install Postman on your system.
* Create an application in Thredd Portal.

**Main steps**

1. Ensure that you have the necessary certificates generated and signed by the Thredd Certificate Authority (CA).
2. Add variables from Thredd CA to the variables section in the Postman collection. You can obtain this information from your application's details in Thredd Portal.
3. If using mTLS, add certificates for mTLS and repeat this process for all required hosts.
4. Set the variables in the **Variables** tab.
5. Check your settings and finish setting up.
6. Test making an API call using the Postman Collection.

For a full step-by-step guidance, see one of the following:

* [Using the Postman Collection to call REST APIs over TLS](Getting_Started/setting-up-postman-to-access-rest-apis-for-tls.htm)
* [Using the Postman Collection to call REST APIs over mTLS](Getting_Started/setting-up-postman-to-access-rest-apis-for-mtls.htm)

## More information

#### Where can I find more information?

For more details, refer to the following resources:

* [Setup preparation and steps](Getting_Started/Setup_Steps.htm) â for connecting to Thredd API Hub (REST APIs) and Thredd Portal via TLS or mTLS connections
* [API Hub website](https://cardsapidocs.thredd.com/v2.0/) â API Reference and guides for Thredd's REST APIs
* [Thredd Portal: Card and Transaction Management Guide](https://docs.thredd.com/Thredd_Portal_Guide.htm)
* [External Interface (EHI) Guide (JSON)](https://docs.thredd.com/EHI_Guide_JSON.htm)
* [External Interface (EHI) Guide (XML)](https://docs.thredd.com/EHI_Guide.htm)