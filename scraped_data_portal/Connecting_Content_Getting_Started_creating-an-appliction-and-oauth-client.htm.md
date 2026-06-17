# Creating an Application and OAuth Client

Before you can access Thredd's REST API, you must create an application and an OAuth Client in Thredd Portal to register it and receive a Client ID. You can then request client credentials for your application, and configure it and a REST interface (such as Postman) to provide credentials when making API calls. Think of the Client ID as the passport for your OAuth Client, and therefore your application. Combined with the credentials you need for your chosen Client Authentication method, it allows Thredd to verify your identity and grant access.

### Summary of the steps

The steps for creating a new application and OAuth Client are as follows:

1. Log in to Thredd Portal.
2. Create a new client application, adding a name and description.
3. Create a new OAuth Client for the application.
4. Ask Thredd to add a PMID to your OAuth Client.

#### Prerequisites

1. You must have access to Thredd Portal.
2. You must be an Admin for your organisation.
3. You must have installed OpenSSL on the machine (the Server) that will make requests to Thredd platform (the Client).

### Step 1: Log in to Thredd Portal

Log in to Thredd Portal and select **System Admin**. In **System Admin** menu, select **Organisation**, then **Applications**.

![Thredd Portal System Admin menu](../Resources/Images/thredd-portal-menu-applications.png)

### Step 2: Create a new client application

The **Applications** screen lists any applications that are registered in Thredd Portal.

If an existing application is already present (and you do not need to create a new one), then check whether an OAuth Client already exists for it. Select the **Actions** menu and select **Review Application**. Check the **OAuth Clients** screen; if an OAuth Client is not present, see step 3.

To create a new application:

1. Select the **Add Application** button.
2. The **Create New Application** screen appears. Enter the basic information, such as a name and description, for the application.

   Thredd recommends that you use an application name that you can easily identify for any application management activities. For example, to distinguish it from other applications when you need to obtain credentials, such as a Client ID, access token or certificate.
3. Select **Next** and review the new application summary; select **Back** to make changes or select **Create Application** to save it.
4. Your new application now appears in the **Applications** screen. Select the menu (three dots) under **Actions** and select **Review Application**. The application summary opens on the **OAuth Clients** tab by default. See *Step 3. Create a new OAuth Client*.

![Applications screen in the System Admin area of Thredd Portal](../Resources/Images/thredd-portal-applications-screen.png)

### Step 3: Create a new OAuth Client

The application details has two tabs; **OAuth Clients** and **Certificates**. The steps to create an OAuth Client are as follows:

1. In the **OAuth Clients** tab, select **Create Client**.
2. The **Create OAuth Client** screen appears, starting with the **Basic information** stage. Enter the basic information, such as the **Client Name** and **Description**, and choose the **Application Type**. Select **Next**. The Application Type choices are:
   * **Native App (Mobile/Desktop)**: iOS, Android, or desktop applications that cannot securely store credentials
   * **Single Page Applications (SPA):**  React, Vue, Angular web applications
   * **Web Application**: Traditional server-side web applications
   * **Machine to Machine**: APIs, microservices, backend services

   ![Create new OAuth Client screen for an Application in the System Admin area of Thredd Portal](../Resources/Images/thredd-portal-create-new-oauth-client.png)
3. The **Authentication** stage summarises the recommended **Security Configuration** based on the Application Type that you selected. To continue, select **Next**. To change the information, select **Back**. The security configurations for each Application Type are as follows:
   * **Native App (Mobile/Desktop)**: Grant Types are authorization\_code, refresh\_token, and PKCE is Required (Recommended). Note: A Native App is a mobile or desktop application that cannot securely store credentials.
   * **Single Page Applications (SPA)**: Grant Types are authorization\_code, refresh\_token, and PKCE is Required (Recommended).
   * **Web Application**: Grant Types are authorization\_code, refresh\_token, and PKCE is Optional.
   * **Machine to Machine**: Grant Types are client\_credentials, and PKCE is Optional.
4. The **Token Configuration** stage allows you to configure how long tokens remain valid. Shorter lifetimes are more secure but may require more frequent re-authentication. Once you have reviewed the default settings or made changes, select **Next**.
5. The **Review** stage allows you to review your configuration, based on the information that you entered in Basic Information, Authentication, and Token Configuration. You can view the list of available **Scopes** for your application in the **Authentication** section. To proceed, select **Submit**; to make changes select **Back** and then submit the details to finish creating the OAuth Client.

You have now registered a new OAuth Client, with a unique Client ID for your application. You can view it in the **OAuth Clients** screen of your application's details in Thredd Portal.

![Review Create OAuth Client screen for an Application in the System Admin area of Thredd Portal](../Resources/Images/thredd-portal-create-new-oauth-client-review.png)

### Step 4: Ask Thredd to add a PMID to your OAuth Client

Now that you have created the application and OAuth Client, you need to associate a PMID with your OAuth Client. This PMID is passed in your OAuth token.

To do this, raise an IAM support ticket with Thredd for the IAM team and request that Thredd adds the specific PMID for accessing the API Hub to your OAuth Client.

Make sure that your request clearly specifies the exact PMID needed to avoid delays.

Only Thredd's internal Identity and Access Management team users can assign or modify PMIDs.

### Next steps

You must make sure that you request and provide the necessary credentials from Thredd to access Thredd's REST APIs.

These credentials depend on the Client Authentication method that your Super Admin selected when setting up your organisation in Thredd Portal, as either:

* Client Secret
* Private Key JWT

If you are using an mTLS connection, your application must also present a Transport Certificate from Thredd. Thredd adopts a self-service approach, which allows an Admin user to independently request and manage certificates via Thredd Portal.

See [Connecting to the REST APIs](connecting-to-the-rest-apis.htm).