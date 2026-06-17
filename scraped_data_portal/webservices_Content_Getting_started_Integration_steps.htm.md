# Integration Steps

To integrate using the web services API, you should complete the following steps in the order outlined below.

![](../Resources/Images/Integration_steps.png "Steps in Integrating")

Figure 2: Integration Steps

## Step 1: Start the On-boarding Process

Thredd recommend you start the on-boarding process as soon as possible, as this may take several weeks due to dependencies on external parties, such as the Card Schemes (payment network).

For project scoping and scheduling information, please refer to your Thredd Implementation Manager and to the following Thredd documentation: [Project Initiation Document (PID)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Project Initiation Document (PID) is put together at a start of a project. This document outlines the initial project requirements and parties involved.](#) , [Project Scoping Document (PSD)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Project Scoping Document (PSD) defines the scope of the project, and is typically produced before the start of the project.](#) and [Project Requirements Document (PRD)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Project Requirements Document (PRD) provides full details of the requirements of your project. Project schedules and implementation are based on the details provided in this document.](#).

#### On-boarding steps:

1. Make sure you have completed your [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup.
   The details are used to configure your Thredd account.](#), to enable us to configure your programme-specific Thredd setup.
2. Enable Thredd to exchange security keys between your card manufacturer, so that Thredd can generate the [PAN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A payment card number (PAN), primary account number, or simply a card number, is the card identifier found on payment cards, such as credit cards and debit cards, as well as stored-value cards, gift cards and other similar cards.](#) stock in our systems, which is required to create physical cards.
3. When ready to go live with your service, check that your Thredd contracts are signed and payments are up to date.

## Step 2: Set up on the Test Environment

### Access to the Thredd generic test product

Thredd provides you with access to a generic Thredd test product setup (referred to as dummy UAT or dummy setup), shared by all of our clients, where you can start exploring the web services. The test product setup provides a restricted set of card functionality, which enables you to perform basic actions such as: create and load cards, manage PINs, change card status and change card velocity groups.

### Access to your own dedicated setup

Thredd configures your dedicated programme on the test environment (ITS-Thredd), with unique credentials, based on the details agreed in your [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Product Setup Form is a spreadsheet that provides details of your Thredd account setup.
The details are used to configure your Thredd account.](#). At this stage transactions are managed within the test environment and not via the Card Scheme (payment network).

#### Test environment setup steps:

1. Ensure you have secure access to all the required Thredd systems:

   * Provide Thredd with a list of IP addresses allowed to use the web services.
   * You require secure access to Thredd in order to use the web services. For more information on Thredd's Secure Connectivity Framework, see the [Connecting to Thredd Guide](https://docs.thredd.ai/Connecting_to_Thredd_Guide.htm).
2. Ensure you have the required user credentials and codes needed to submit web service requests:

   * You need a *username* and *password*, which must be included in the authorisation header of your SOAP request. Your Implementation Manager will provide you with your credentials.
   * You will need an [Issuer Code![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Issuer (Program Manager) code,
     assigned by Thredd. Each Program Manager is assigned their own unique issuer code on the system.](#), supplied by Thredd. This must be included in the body of your SOAP request.

#### Test your Integration:

1. Decide which web services you need. This depends on the Thredd [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services.
   All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) mode you are using. For example:

   * If you are set up for Gateway Processing (mode 1 and 4) you mainly use the web services related to card creation, card management and card usage groups.
   * If you are set up for Cooperative Processing (mode 2) and Full Service Processing (mode 3), you may need to use other web services for loading/unloading cards and updating the balance on the card.
2. Test your EHI integration. For more information, refer to the *EHI Specifications*.
3. Submit test web services transactions to the Thredd test system. See [Using the API](Using_SOAP.htm). View the results and fix any errors.

   Thredd recommend you start with a simple check of the status of the web service to make sure you can connect, using `Ws_Check`. See [Check Service Availability](../Web_services_api/Check_Service_Availability.htm).
4. When you are satisfied you understand how the web service API works, build your front-end user application with the SOAP API functionality included.

See the [Use Case Scenarios](User_Scenarios.htm) section for general pointers to getting started with the Thredd API. For field validation rules that are run on specific fields, see [Field Validation](../Reference/Field_Validation.htm).

#### CHIP Profile and White Test Plastics

Create test card tokens and generate white test plastics. These are generic, non-branded cards with test keys on the card. Your Implementation Manager will work with your card manufacturer to produce test cards:

* Thredd generates a card file for any test cards that have been created and manually sends to the card manufacturer.
* The card manufacturer produces white test plastics in line with the agreed project plan. Test cards are sent to the relevant parties (e.g. the Program Manager and Visa or Mastercard).
* Testing is undertaken in line with the agreed scope.

## Step 3: Set up on Production

Once all production readiness activities are complete, Thredd provides you with production credentials and generates a limited number of PAN stock, as approved by your card issuer.

#### Production testing steps:

Additional end-to-end transaction testing is required at this stage. In particular:

* Create card tokens for automated card production.
* Thredd sends a file to the card manufacturer via sFTP (Secure File Transfer Protocol). The card manufacturer generates live physical cards and despatches to the relevant parties for testing, which include Thredd, Programme Manager and Card Schemes (payment networks).
* Thredd can provide you with a test script to run tests that cover aspects you should test, such as:

  + Test traffic through the BIN tables.
  + Test the card chip profile is working in line with how it has been configured (for example, if the card is enabled to draw out money at ATMs and charges a fee for ATM withdrawals, check this works as expected).
  + Test to ensure usage groups and velocity limits set up for your products work as expected and return the expected results.
* Make sure you understand any messages returned from the Card Schemes (payment networks) and card issuers and know how to handle.
* Test the end-to-end customer experience and confirm that the card and account are operating as expected.

## Step 4: Go Live

Thredd pavement testing approval is required in addition to any Issuer sign-off before Thredd can switch your account to *Active*.