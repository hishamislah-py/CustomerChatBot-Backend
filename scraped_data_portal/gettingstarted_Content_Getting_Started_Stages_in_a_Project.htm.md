# 1 Stages in a Project

## 1.1 Before you Start

### 1.1.1 Clarify your Requirements

Speak to a member of the Business Development team to find out more about Thredd services and how we can support your project requirements.

Your business development manager will provide relevant case studies and talk you through the products and options available using Thredd.

### 1.1.2 Understanding your Customer Journey

Understanding your customer's end-to-end experience is a key part to setting up an effective card program. Mapping out the customer journey should be done as early as possible so that the Thredd system can be correctly configured to your requirements.

See the figure below, which summarises the main components in a typical customer journey:

![](../Resources/Images/Customer_journey.png "Understanding your end-to-end customer journey")

Figure 1: Customer Journey

Early analysis and preparation can save you both cost and time and help avoid potentially costly mistakes that can be hard to rectify at a later stage. Below is a list of basic questions to consider:

* Who are your customers? (age, language, profile)
* In what countries, regions, currencies and business sectors do you plan to offer your service?
* How will customers sign up for your service and open an account? What identity and verification checks do you need to run on customers before they can open an account?
* What card products will you offer and how can your customers customise them? (will you offer a physical card or just a virtual card? For a physical card, what features will it support?)
* What are the charges for using your cards? (This includes one-off setup, regular account fees and card usage fees, if applicable to your service.)
* How will customers activate their card, load their account with funds and transfer funds out of their account?
* How will customers be able to use your card?

  + Where can the card be used, with what merchants and are there any limits or restrictions you want to set on usage?
  + Can the card be used for ATM queries and withdrawals?
* How will payments and ATM withdrawal requests be authorised? Will you do this, or will Thredd manage this?
* How do you want cardholders to authenticate (i.e., verify their identity) if asked to during an online transaction? (For example, via your mobile phone app, biometric or One-Time password.)
* How will you provide information to your customers? (i.e., on card transactions, card balances, statements and fees.)
* How will customers manage their cards? (e.g., block or unblock, replace a lost or expired card and change their PIN.)
* How will customers be able to contact you? How will you manage disputes and chargebacks? How will you communicate to customers in the event of an outage affecting their service?
* Once the service is live, how are you planning to maintain it and ensure your integration is updated with the latest Thredd system changes and regulatory requirements? (For details see [Managing Change](Managing_Change.htm#_Managing_Change))

### 1.1.3 Selecting your Partners

#### Selecting an Issuer or Go Self-Issuing

An Issuer is a regulated organisation that has local regulatory authority and card scheme approval to issue prepaid, debit or credit cards. Decide whether you will be self-issuing or using the services of an existing issuer to support your card program.

Self-issuing requires a contractual relationship with their Card Scheme (e.g., Visa, Mastercard or Discover) and additional regulatory authority requirements, and therefore adds time and costs to the implementation phase. For new Thredd customers starting out on a card program with Thredd, speed to market is quicker and easier when using an existing issuer already set up with Thredd, compared to setting yourself up as a new issuer. You can upgrade to self-issuing at a later stage without any impact on your transactions[1  Migrating to self-Issuing requires changes to reporting and BIN setup with the card scheme. If you want to find out more about how to become self-issuing, please check with your business development manager.](#).

Please talk to your Thredd business development manager, who can provide you with information on issuers suitable to your trading region and payment processing requirements.

#### Selecting a Card Scheme (Payment Network)

The card scheme provides the network over which card payments can take place. Thredd currently support Visa, Mastercard and Discover, which provide global networks, as well as smaller networks that use the Mastercard Network Exchange (MNE), such as STAR and Pulse[2 Please contact your account manager for information on Discover network availability and restrictions. Mastercard Network Exchange enables smaller networks to use Mastercard as a
routing platform for payments.](#). We are also working to support other global card schemes as well as local schemes, specific to your region.

If you are using the services of an existing issuer, you do not need to have a separate agreement with the card scheme they support.

The card scheme networks have variations in how they process and report payments. When Thredd receives and processes information from the different networks, we provide this to our customers in a consistent format.

#### Selecting a Payment Service Provider (Payment Gateway)

You will need to provide a facility to enable your customers to fund their accounts via a credit or debit card. This typically requires the service of an online payment service provider (PSP). This is a service outside of Thredd. Check with your Thredd business development manager for details.

Alternatively, you can use a third party Agency Banking service that enables banking payments via bank transfer (BACS, CHAPS, Faster Payments and SEPA).

## 1.2 Setting up a Typical Card Program

The figure below provides an overview of the stages in a project and the responsibilities of the parties involved. Timescales are subject to full project scoping; timescales for some components may be dependent on third parties, such as card manufacturers, issuers and schemes.

![](../Resources/Images/Implementation_Process.png "Stages in a typical project")

Figure 2:  Stages in a Thredd Project

The above figure shows the main parties involves at each stage: issuer, Thredd, Program Manager and Card Manufacturer. [Step 1: Scope Project](#Step) and [Step 2: Confirm Business Requirements](#Step2) are pre-requisites before you can start integrating.

Steps 3-5 cover the [integration](#Step3), [testing](#Step4) and [go-live](#Step5) stages.

Each of these steps is described in further detail below.

### 1.2.1 Step 1: Scope Project

A number of documents need to be completed at this stage.

#### Statement of Work (SOW)

This document provides a summary of the technical solution to be provided by Thredd. Your Thredd business development manager should provide this document, which includes:

* Components and services of your solution
* Relevant service providers (e.g., BIN sponsor, card manufacturer)
* Project stages and responsibilities
* Anticipated go-live date and target market

### 1.2.2 Step 2: Confirm Business Requirements

Thredd will assign an business development manager to provide you with support for commercial queries and act in an account management capacity. Any changes to the intended scope of service â either taking on additional functionality or changing functionality (such as switching External Host Interface (EHI) Mode) â will be managed commercially by your business development manager.

Your business development manager will send you a copy of the Project Initiation Document (PID). This is a reference document with a generic description of high-level project stages and responsibilities.

Thredd will assign an implementation manager, to support you during the onboarding process in setting up your service on the Thredd system.

Your Thredd implementation manager will arrange a meeting to understand what you want to deliver and discuss your requirements. They will provide you with copies of the following documents:

* Project Requirements Document (PRD) â offers a more detailed description of the components and services of your solution, as well as the project stages and responsibilities
* Project plan â specifies milestones and preliminary dates for implementation.

Please review these documents carefully and indicate any changes you require. You should also provide them to your issuer to review. You will need to sign off these documents.

#### Issuer Requirements

If you are using the services of an issuer, they will need to set up your BIN range and specify their requirements for how they will be supporting your service. You will need to complete any documentation requested by your issuer.

Your issuer may also ask you to complete documents required by the card scheme (e., Visa, Mastercard or Discover) to set up the card product on their systems.

Thredd can provide input into your issuer and card scheme documents where relevant and appropriate (e.g., provide you with endpoint information, Mastercard session or Visa Process Control Record (PRC) details and keys information).

#### Selecting a Card Manufacturer (Card Bureau)

If you are going to be issuing physical cards, you should select a card manufacturer at this stage. Thredd has existing partner relationships and plug-ins to over 40 card manufacturers worldwide and can support local card creation programs in regions worldwide. Check with your business development manager or implementations manager for details.

You must have a separate commercial agreement with your card manufacturer.

#### Sandbox

You can sign up for developer access to our sandbox system where you can try out our API and explore the system functionality.

The sandbox provides a restricted set of card functionality, which enables you to perform basic actions such as: create and load cards, manage PINs, change card status and change card velocity groups.

Access to the Thredd sandbox enables you to make an early start on your integration to Thredd via the Thredd API.

### 1.2.3 Step 3: Specification and Integration

At this stage, your implementation manager will set up your card program on the Thredd system. There are a number of key tasks to complete:

#### Complete Thredd Product Setup Forms

Your implementation manager will work with you to complete the main Thredd Product Setup Form (PSF). This document provides details of your card program setup and field-level configuration on the Thredd system.

There are additional product setup forms to complete for other Thredd products, such as 3D Secure and Tokenisation (Digital Wallets).

You and your issuer will need to sign off the Product Setup forms.

#### Thredd Provides Systems Access

You will be given access to firewalls, Thredd API and other systems.

Thredd will manage the security key exchange with your card manufacturer and the card scheme if required, so that we can generate the PAN stock in our systems to create your card product.

#### Set up on the Test Environment

Thredd configures your dedicated program on the test environment, with unique credentials, based on the details agreed in your Product Setup Form (PSF). At this stage transactions are managed within the test environment and not via the card scheme network.

Ensure you have the following:

* Secure access to all the required Thredd systems:

  + Provide Thredd with a list of IP addresses allowed to use the Thredd API. Note that Thredd only supports static IP addresses for permission listing.
  + You require setup with secure access to the Thredd systems. For more information, see the [Connecting to Thredd Guide](https://docs.thredd.ai/Connecting_to_Thredd_Guide.htm).
* The required user credentials and codes needed to submit Thredd API requests. For details, see the [Cards API Website (REST)](https://cardsapidocs.thredd.com/) or [Web Service Guide (SOAP)](https://docs.thredd.ai/webservices/Default.htm).

#### Test your Integration

Decide which Thredd API you need. This depends on the Thredd External Host Interface (EHI) mode you are using. For example:

If you are set up for Gateway Processing (modes 1, 4 or 5) you mainly use the Thredd API related to card creation, card management and authorisation. If you are set up for Cooperative Processing (mode 2) and Full Service Processing (mode 3), you may need to use other Thredd API for updating the balance on the card.

For more information, refer to the [External Host Interface (EHI) Guide](https://docs.thredd.ai/ehi/Default.htm).

Submit test Thredd API transactions to the Thredd test system. View the results and fix any errors.

When you are satisfied you understand how the Thredd API works, build your front-end user application with the Thredd API functionality included.

Test your EHI integration. You can submit test transactions, using the Card Transaction System (CTS) to view the end-to-end transaction process.[3 Thredd will need to enable access to CTS based on your IP address.](#) For more information, see the [Card Transaction System (CTS) Guide](https://docs.thredd.ai/Card_Transaction_System_Guide.htm).

### 1.2.4 Step 4: Configuration and Testing

Once you have successfully integrated, you can start configuration and testing.

#### Create Chip Profile and White Test Plastics

Create test card tokens and ask Thredd to generate white test plastics, if required. These are generic, non-branded cards with test keys on the card that can be used to check that the card Chip profiles are working correctly[4  White test plastics are required for testing new Chip profiles, which need to be signed off by the card scheme.  They are typically printed in bulk quantities. Live Chip keys should never be used on test card plastics since these cards lack some security elements.](#). Your implementation manager will work with your card manufacturer to produce test cards:

* Thredd generates a card file for any test cards that have been created and manually sends to the card manufacturer.
* The card manufacturer produces white test plastics in line with the agreed project plan. Test cards are sent to the relevant parties (e.g., the Program Manager and Visa or Mastercard).
* Testing is undertaken in line with the agreed scope.

#### Get your Card Design Approved by the Scheme

New card designs, which include the schemeâs brand, need to be signed off by the scheme. You need to do this directly with the scheme or via your issuer, as Thredd is not involved in this process.

#### Order Base Plastics

Live base cards, with your branded image can now be ordered from the card manufacturer. These cards contain the default Chip and Magstripe data, but do not have any personalised data and do not yet contain the printed cardholder details.

Your card manufacturer will confirm how long it will take before your base plastics are ready to be personalised and printed.

#### Set up on Production

Once all production readiness activities are complete, let Thredd known that you are ready to migrate to the Production environment and start pavement testing.

Thredd provides you with production credentials and generates a limited number of PAN stock, as approved by your card issuer.

Additional end-to-end transaction testing is required at this stage. In particular:

* Create card tokens for automated card production. Thredd will send a file to the card manufacturer via [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). The card manufacturer prints live physical cards containing the personalised cardholder data and despatches to the relevant parties for testing (Thredd, Programme Manager and Card Schemes).
* Thredd can provide you with a test script to run tests that cover aspects you should test. Below are examples of what you should test:

* Test traffic through the BIN tables.[5  Visa and Mastercard send out a daily file to all acquirers with details of new BINs. Acquirers must add these BINs to their BIN tables to enable transactions on these BINs; this can take up to 2 weeks.](#)
* Test the card chip profile is working in line with how it has been configured (for example, if the card is enabled to draw out money at ATMs and charges a fee for ATM withdrawals, check this works as expected).
* Test to ensure usage groups and velocity limits set up for your products work as expected and return the expected results.
* Validate how you process and handle card scheme authorisation and financial messages which Thredd sends to your external host.
* If you are using an EHI mode where you authorise the transaction, then check how long it takes to respond to an EHI authorisation request on a live production transaction.
* Test the end-to-end cardholder experience and confirm that the card and account are operating as expected.

### 1.2.5 Step 5: Go Live

When ready to go live with your service, check that your Thredd contracts are signed and payments are up to date, and then let your implementation manager know you are ready to go live.

Thredd [pavement testing![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) End-to-end testing of the cardholder journey using real cards that have been issued, which takes place before a service is rolled-out to customers.](#) approval is required in addition to any Issuer sign-off before we can switch your products to *Active* and generate full production PAN stock.

Thredd will provide you with access to JIRA (for raising issues) and to Thredd Portal (for viewing and managing cards and transactions). Thredd can add up to five users for each service; additional users require purchasing additional licenses.

#### Handover to Operations and Account Management

Once you are live, your business development manager will arrange a handover session with the relevant customer care representative and/or appropriate heads of department (e.g., Head of Operations or Global VP of Customer Success)

* The Thredd Operations teams will be available for post-live product support and program maintenance.
* Thredd will provide you with a dedicated account manager for ongoing requests and queries.

The figure below summarises how Thredd supports you through the different phases of your project.

![](../Resources/Images/Support_Roles.png "Support During your Project")

Figure 3: Thredd support during your project