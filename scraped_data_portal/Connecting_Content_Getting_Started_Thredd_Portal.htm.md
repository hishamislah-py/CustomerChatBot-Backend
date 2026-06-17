# Thredd Portal overview

Thredd Portal is the main entry point to Thredd services and is the main component that is related to the API Hub; before you can use the API Hub, your organisation must be set up on Thredd Portal and Thredd Secure Framework. These combine several components that enable secure access to Threddâs resources, using a common identity store.

Thredd Portal provides a number of features, including:

* Organisation and application management â Super Admin and Organisation Admin users. Manage access for your organisation's applications, edit/add SSO details, create and manage certificates, generate and validate access tokens and certificates, and more.
* User management â Super Admin users. Invite users to onboard to Thredd and manage user roles, permissions, and access, including the option to deactivate and reactivate users.
* Cards and transaction management, and other related functionality â for users with the appropriate roles.
* Access to Webhook management in Thredd Portal â for users with the Developer role.

You can learn more about the cards and transaction management features of Thredd Portal in [Thredd Portal Guide: Getting Started](https://docs.thredd.com/Thredd_Portal/Content/Getting_Started/Getting_Started.htm).

## Identity and Access Management

Thredd Portal provides identity and access management functionality at an organisation, application, and user level. Thredd Portal functions as a *Confidential Client*, where Thredd's own application infrastructure undertakes authentication and authorisation activity on behalf of the user.

Once a user is registered and has logged in to Thredd Portal, they can access other Thredd services. Thredd Portal also operates behind-the-scenes as an authentication server, enabling a single sign-on journey and access to Thredd's REST APIs.

Thredd Portal also provides access to Thredd's Certificate Authority for setting up and managing certificates to connect to Thredd services, including the REST APIs via API Hub.

To learn more, see [Thredd Secure Framework](thredd-secure-framework.htm).

## Connecting to Thredd Portal

Thredd Portal provides support for multiple roles, with Admin access available to a Super Admin and at least one Organisation Admin. A Super Admin user can set up and manage the settings for your organisation's applications, certificates, SSO configuration, and users through Thredd Portal. Organisation Admin users have a similar level of access, except they do not manage users.

This guidance focuses on the initial set up by a user with the Super Admin role in Thredd Portal.

You can choose one of the following methods for users to log in to Thredd services:

* Single Sign-On (SSO) â this involves adding an SSO configuration for SAML or OIDC in Thredd Portal and inviting users via your identity provider. This is not required, but Thredd recommends it to help automate user onboarding and management.
* Email address and password â this involves manually adding details for each user in Thredd Portal and sending an invite using its built-in invitation feature.

#### About Single Sign-On access (optional)

Thredd's Secure Framework allows you to optionally set up SSO, using *SAML* (Security Assertion Markup Language) or *OIDC* (OpenID Connect), to access Thredd services, for example Thredd Portal. This not mandatory but Thredd recommends that your users log in using SSO instead of using a password because it offers the following benefits:

* An enhanced user experience for users as it removes the hassle of remembering passwords.
* Companies to save time on maintenance.
* Reductions in overheads when managing accounts.

This enables a Single Sign-On journey by linking your IdP with Thredd's own provision. If you do not use an IdP, Thredd can act as the IdP.

This Single Sign-On journey is involved with:

* Accessing the organisation and user management features of Thredd Portal for Super Admin users, such as creating certificates with Thredd's CA, and the user management functionality to set up access for other users.
* Accessing the card and transaction management features of Thredd Portal.
* Managing access behind-the-scenes to the REST API.

### Setting up access to Thredd Portal for the first time

A Super Admin user at your organisation must first register and log in to Thredd Portal before other users within your organisation can access Thredd Portal and other services.

You can begin this process when Thredd has registered your organisation and your Super Admin user, and has sent an email inviting them to log in to Thredd Portal.

The set up guidance outlines the full process of setting up the Super Admin for the first time and setting up additional users. However, a Super Admin does not have to invite/add users to register with Thredd Portal straight away. Instead, the Admin can choose to add the organisation's SSO details (if using SSO), create Client certificates, and test access to Thredd REST APIs and API Hub first. A Super Admin can later return to this step to set up the SSO or password-based access for the organisation's users.

#### Set up guides

To learn more about setting up access for your organisation, applications and users in Thredd Portal, see:

* [Setting up Single Sign-On access and users on the Thredd platform](setting-up-sso-and-users.htm)
* [Setting up password-based access to Thredd Portal](setting-up-password-based-user-access.htm)
* [Understanding Roles](understanding-roles.htm)
* [Creating an Application and OAuth Client](creating-an-appliction-and-oauth-client.htm)
* [Understanding Scopes](understanding-scopes.htm)

If your organisation will use Single Sign-On to access Thredd services, the following guides will help you to configure your SSO provider:

* [Configuring SSO with Okta (SAML)](../Appendices/Configuring SSO with Okta (SAML).htm)
* [Configuring SSO with Google (SAML)](../Appendices/Configuring SSO with Google (SAML).htm)
* [Configuring SSO with Okta (OIDC)](../Appendices/Configuring SSO with Okta (OIDC).htm)