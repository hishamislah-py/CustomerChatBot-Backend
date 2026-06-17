# Configuring SSO with Okta (OIDC)

If your organisation uses Okta, you can configure Okta as an IdP provider to provide SSO access to various Thredd services. For example, you can use SSO to access Thredd services such as Thredd Portal. This guidance describes the steps for using the OpenID Connect (OIDC) protocol for setting up SSO.

Setting up SSO is not mandatory, but Thredd recommends it.

## Overview

The steps involve:

* Creating an app and app integration.
* Setting URL and refresh token settings.
* Specifying your access control requirement.
* Sharing authentication details with Thredd, via the Client ID/Client Secret method or the `private_key_jwt` authentication method.

Thredd recommends using the `private_key_jwt` authentication method.

Thredd will provide you with a Sign-in Redirect URI for creating a web application integration.

## Configuring SSO

1. Log in to the Okta Administration console.
2. Select **Applications** from the left-hand menu.

![](../Resources/Images/okta_applications.png)

3. Select **Create Application**.
4. In **Create a new application integration**, select **OIDC - OpenID Connect** and **Web Application.**

![](../Resources/Images/oidc_appintegration.png)

5. Select **Next.**
6. Enter a name for your application integration in **Application integration name**.
7. Select the **Refresh Token** check box.
8. Enter the URL value of the sign-in redirect URIs in the **Sign-in redirect URIs** section.

![](../Resources/Images/okta_newwebapplication.png)

9. Select how you want to control access to Thredd applications from your organisation. The following example shows that access is available to all users in your organisation, and where there is immediate access.

![](../Resources/Images/sharedaccess_okta.png)

10. Share details with Thredd.
    * If you are using a Client ID/Client secret, share this detail with Thredd using your preferred secure method.
    * If you prefer Thredd's recommended authentication method of `private_key_jwt`, complete the following steps to share the private key.

### Share the Private Key JWT

1. Select the application that you have just created under **General**.
2. Select **Edit** next to **Client Credentials**.

![](../Resources/Images/edit_clientcredentials.png)

3. Select **Public Key / Private Key**, the page updates to show the public key configuration options:

![](../Resources/Images/keyoptions_okta.png)

4. Select **Add key**. The **Add a public key** screen appears.
5. Select **Generate new key**.
6. When the private key is shown, select PEM.
7. Copy the value to your clipboard and save it.

You must share the private key with Thredd. The following shows the on-screen instructions for generating and copying a private key.

![](../Resources/Images/generate_privatekey.png)

8. Select **Done**.