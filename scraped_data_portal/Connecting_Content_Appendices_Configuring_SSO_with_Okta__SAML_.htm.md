# Configuring SSO with Okta (SAML)

If your organisation uses Okta as an IdP, you can use Okta for configuring SSO for accessing various Thredd services, for example, Thredd Portal. This guidance describes the steps for using the 2.0 version of Security Assertion Markup Language (SAML) protocol for setting up SSO.

As a client, you would already have an account on the Okta Administration Console.

Setting up SSO is not mandatory, but Thredd recommends it.

## Summary of the steps

The steps involve:

* Creating a SAML app for your SSO connection to Thredd services.
* Adding configurations from Thredd including the SSO URLs and the Entity ID.
* Mapping fields associated with the users defined by Okta with those used by your app.
* Sharing the Metadata URL with Thredd.

## Configuring SSO

1. Log in to the Okta Administration console.
2. From the left-hand menu, select **Applications**.

![](../Resources/Images/applications.png)

3. Select **Create Application**.
4. Select **SAML 2.0** and select **Next**. The next page appears.

![](../Resources/Images/okta_newappintegration.png)

6. Enter a name for the app that accesses Thredd services in **App name** and select **Next**. The next page appears.

7. Add the provided URLs in **Single Sign-on URL (ACS URL)** and **Audience URL (entity ID)**.

![](../Resources/Images/okta_urls.png)

8. Scroll down on the same page and configure the following Attribute Statements:

   1. Enter an attribute name in the **Name** column.
   2. Select a value in the **Value** column.
   3. To add another entry, select the **Add Another** button.
   4. Repeat steps a and b.

![](../Resources/Images/attributestatements_oktasaml.png)

9. Select **Next**.
10. In the displayed page, select **This is an internal app that we created** and select **Finish**.
11. In the displayed **Metadata Data** details that appear, share the Metadata URL with Thredd.

You can then assign the application to the users or groups who will be using the Thredd services.