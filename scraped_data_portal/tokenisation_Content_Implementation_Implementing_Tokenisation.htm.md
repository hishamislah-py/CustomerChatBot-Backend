# 4 Implementing a Tokenisation Project

## 4.1 Steps in Enabling the Tokenisation Service

This section provides an indicative guide to the steps that you need to complete to enable the tokenisation service:

1. Sign up for the service
2. Complete requested forms
3. Configure your Thredd settings
4. Complete testing
5. Complete the Wallet Provider certification process

### 4.1.1 Step 1: Sign up for the Service

To enable the tokenisation service, you need to sign up with each of the following participants in the tokenisation flow:

* The Token Service Provider (Visa or Mastercard); for details, see the links below:

  + Visa Token Service: [Visa.co.uk: Visa Token Service](https://www.visa.co.uk/partner-with-us/payment-technology/visa-token-service.html)
  + Mastercard Digital Enablement Service: [Mastercard.ie: Digital Commerce-solutions](https://www.mastercard.ie/en-ie/issuers/products-and-solutions/grow-manage-your-business/digital-commerce-solutions.html)
* The Mobile Wallet Token Requestor(s) of your choice (e.g., Apple, Android, Fitbit, Samsung). for details, see the links below:

  + Apple Pay: [developer.apple.com](https://developer.apple.com/) and [Apple Pay implementation](https://developer.apple.com/apple-pay/implementation/)
  + Google Pay: [pay.google.com](https://pay.google.com/)
  + Samsung Pay: [samsung.com: Samsung Pay](https://www.samsung.com/uk/samsung-pay/)
* The Issuer Host (Thredd). Contact your Thredd Account Manager

You do not require a project or any pre-existing relationship with any Online Merchant Token Requestor (such as Netflix, PayPal, Amazon). As new Online Merchant Token Requestors are added to Visa/Mastercard, Thredd will continue to add these new merchants without further input from you to ensure you remain compliant.

Thredd receives around 100-200 new Token Requestor updates a month from Visa. Mastercard add them to their generic MDES for merchant 3-digit token requestor code, so we do not need to update.

### 4.1.2 Step 2: Complete Requested Forms

Once you have signed up with Visa/Mastercard, your assigned Visa/Mastercard project manager or contact will send you a number of documents for completion. The Visa and Mastercard documents require Thredd input as they relate directly to the functionality on the Thredd platform. For details, check with your implementation Manager.

Please ensure Thredd are involved in helping you complete the documents listed below.

Examples of Visa documents:

* Visa Token Service Program Information Form (PIF)
* Visa Token Service Digital Enrolment Form (DEF))

Examples of Mastercard documents:

* MasterCard BPMS guide (Parameter Worksheet)

Wallet provider documents:

* Complete the relevant wallet provider agreements and configuration forms. Thredd does not need to be involved in this process.

### 4.1.3 Step 3: Configure your Thredd settings

Once a project is open with Thredd, your Implementation Manager will work with you to understand how you want your token service programme to work.

You must complete the Thredd Digital Wallet Product Set Up Form (PSF) to confirm your tokenisation service configuration options. For details, see [Thredd Configuration Options](Tokenisation_Configuration.htm#_GPS_Configuration_Options).

If you want to receive tokenisation messages via the Thredd External Host Interface (EHI), in your Product Setup Form (PSF), ensure you tick the option to enable TAR transaction types. For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).

### 4.1.4 Step 4: Complete your internal testing

Complete internal pilot and pavement testing in the production environment. Get to know how your tokenisation app works and test against the wallet provider test scenarios.

Mastercard provide a Mastercard Test Facility (MTF), which can be used to test your MDES integration. MTF connects to the Thredd test environment. You can add your phone to MTF to send test tokenisation messages to Thredd. Please contact Mastercard to enable this service.

Visa provide a test service sandbox, which can be used to test outbound calls. For details, please contact Visa.

Some integration work may be required on your end to integrate to the Mastercard or Visa test services. Many Thredd clients prefer to complete tests in the production environment.

### 4.1.5 Step 5: Complete the Wallet Provider certification process

Some Wallet providers, such as Apple Pay, have a formal certification process. Documentation for this is not available publicly, so Thredd recommends speaking to Apple Pay or your issuer in the first instance.

Google Pay does not have a formal certification process. Instead Google will send test scripts to you or your Issuer.

## 4.2 Implementing a Customised Token Service

Testing with Visa and Mastercard is not required if you are using the out of the box tokenisation service provided by Thredd.

If you require non-standard functionality, you will need to raise a separate Thredd project (development work is required). Check with your account manager for details.