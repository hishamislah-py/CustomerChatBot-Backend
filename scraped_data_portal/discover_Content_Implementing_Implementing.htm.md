# 5 Implementing a Discover Network Programme

This section provides details of the steps involved in implementing a Discover Network card programme.

## 5.1 Stages in a Discover Network Project

Discover provides resources and support to help issuers and their processors integrate. This includes access to the Discover EASI Portal for onboarding, testing, and ongoing communication. For more information, see the [Discover EASI Portal](https://discovereasi.com/).

The figure below provides a high-level overview of the typical stages in a Discover Network project.

![](../Resources/Images/Project_stages.png "Stages in a Discover Project")

Figure 11: Stages in a Discover Network Project

The typical steps in a project are described in further detail below.

##### Project Scoping and Registration

1. Define your Discover Network Card Programme requirements, including implementation options and scope. See [Discover Project Requirements](Discover_requirements.htm).
2. Complete Discover card programme setup and configuration options. See [Issuer Documentation and Certification](Discover_requirements.htm#Issuer).
3. Register your Issuer Identification Code (IIC) for each settlement currency you are supporting. Talk to your Discover representative.

   Each time you add a new Settlement Currency, you must complete a new request for a separate Issuer Identification Code (IIC).

##### Thredd Setup

4. Complete your Thredd Product Setup Form (PSF). Your implementation Manager will provide guidance and ensure your account and card product configuration options are set up on the Thredd Platform. For more information, see [Thredd Setup and Configuration](Discover_requirements.htm#Setup).
5. Create/issue test cards using your existing Thredd API (SOAP Web Services or REST-based Cards API), with your Discover card product. (For existing Thredd Program Managers, all API details, such as your credentials, will be the same). For more information, see [Card Management](Managing.htm#Card).
6. Complete your External Host Interface (EHI) integration. Existing Thredd Program Managers can either use the same EHI endpoint or request a separate external host endpoint for Discover.

You can use your existing integration to EHI. There are some changes to field values you can expect to receive for Discover Network transactions.

##### Testing and Go live

7. Use the Thredd [Card Transaction System (CTS)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Card Transaction System (CTS) enables you to test the integration of your card processing systems and validate the setup of your External Host Interface (EHI).](#) to test Discover Network transactions. For more information, see [Testing Transactions](Testing_Transactions.htm).
8. View your transactions on [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#). For more information, see [Viewing Transactions](Viewing_Transactions.htm).
9. Complete Discover certification testing.
10. Complete pavement testing. This involves using some live Discover BINs to make payments and process transactions.
11. Go live.