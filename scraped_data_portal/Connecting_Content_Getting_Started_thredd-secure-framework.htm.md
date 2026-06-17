# Thredd Secure Framework

Thredd*'s Secure Framework* is the combination of several components which enables clients to access Thredd's resources securely over TLS (Transport Level Security) or mTLS (Mutual Transport Level Security). Thredd *Portal* sits at the centre of this, enabling Admins to manage their organisation's applications, users, and credentials to access Thredd services through a single user interface and dashboard.

Thredd supports industry standards for authentication, identity and access management, and secure network and API-level connectivity.

#### Key features

Identity and Access Management through Thredd Portal

* Standards-based authentication â support for OpenID Connect (OIDC), SAML, and JWT.
* Single-Sign On (SSO), self-service onboarding, and token lifecycle management.
* Secure Access Control â role-based access (RBAC) and user management.

Connectivity Services

* Secure network and API-level connectivity via VPN, TLS and mTLS, and PKI and JWKS token validation.
* Certificate lifecycle management â request, revoke and renew certificates issued by [Thredd's Certificate Authority](#ThreddCA) through Thredd Portal.
* mTLS Termination for mTLS connections in an EHI mTLS setup.

Developer Tooling

* Access Thredd REST APIs via API Hub over TLS or mTLS.
* Test connectivity to Thredd REST APIs and API Hub using the Postman Collection in a UAT environment.

#### Identity and Access Management through Thredd Portal

Thredd provides a Software as a Service (SaaS) capability that acts as the *Identity Provider (IDP)* to authenticate user access to Thredd's interfaces through logging in to Thredd Portal. It also acts as an *OAuth OpenID Provider (OP)* for the registration and management of customer applications, generation and validation of access tokens, and for the enforcement of access control policies.

Thredd supports the following Client Authentication methods for connecting to the REST APIs:

* Client Secret â requires an access token from Thredd.
* Private Key JWT â requires an access token from Thredd, and a Signing Certificate to generate a JSON Web Token (JWT).

#### Thredd Certificate Authority through Thredd Portal

Thredd adopts a self-service approach that enables Admin users to independently request and manage certificates for their applications from Thredd's Certificate Authority (CA) through Thredd Portal.

Client applications require the following certificates to connect to services, depending on the configuration you choose:

* Signing Certificates â required for Private Key JWT client authentication, for creating a signed JWT for an access token.
* Transport Certificates â required for mTLS connections for establishing connections between resources.

| Thredd Application | Certificates Required |
| --- | --- |
| REST API over TLS | Private Key JWT authentication requires a Signing Certificate.  Client Secret authentication does not require a Signing Certificate. |
| REST API over mTLS | Transport Certificate for the mTLS connection, which you obtain from Thredd Portal.  Private Key JWT authentication requires a Signing Certificate.  Client Secret authentication does not require a Signing Certificate. |
| SOAP API | Transport Certificate, which you obtain from Thredd. |
| External Host Interface (EHI) | Server Certificate (which you obtain separately), Thredd EHI Trust Chain (that you download from Thredd Portal), and a Transport Certificate (which Thredd presents). |
| Thredd Portal | Certificates that are pre-installed by Thredd. |