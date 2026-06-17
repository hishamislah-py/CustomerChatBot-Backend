# Discover FAQs

### Availability and suitability

#### Q. Is Discover available to all Thredd Customers?

You must be an existing Thredd customer, integrated to the Thredd Platform.
Your Issuer (BIN Sponsor) must be registered with Discover.

#### Q. Is Discover suitable for all Thredd Customers?

For phase 1, we support virtual cards only.
Please contact your account manager to discuss your requirements and suitability for phase 1 release.

### Requirements

#### Q. Are there any pre-requisites/specific requirements that need to be met?

You will need to sign a separate contract with both Thredd and Discover and complete the required documentation.

You must obtain a separate Issuer Identification Code (IIC) for each settlement currency you support.

You must have a bank account in that settlement currency, opened within 2 months of IIC registration.

#### Q. What is an Issuer Identification Code?

The Issuer Identification Number (IIN) or Issuer Identification Code (IIC) on Discover cards is the first 6-8 digits of the card number, which identify the card issuing institution.

#### Q. What's the difference between an IIC and a BIN?

The Issuer Identification Code (IIC) or Issuer Identification Number (IIN) is a more specific term that refers to the first 6-8 digits identifying the card-issuing institution, while the Bank Identification Number (BIN) is a broader term that encompasses the first 4-8 digits identifying the bank or financial institution behind the card. Both serve critical functions in the payment ecosystem, but the IIC/IIN is the more precise and standardized identifier of the card issuer.

### Integration

#### Q. Will we need to do an additional integration to support Discover?

You can use your existing EHI integration. We normalise data received from Discover (in the same way as for other card networks, such as Visa and Mastercard) and provide you with a unified message format for all networks. This means that you do not need to implement a separate integration for each additional network you want to connect to.
There are new data elements and field values which your systems may need to able to receive and process (depending on your EHI Mode). For Program managers using Full Service Processing (mode 3), Thredd performs transaction matching and balance adjustments.

For more information, see [Transaction Processing on Discover Networks](Processing/Transaction_Processing.htm).

#### Q. Are there any EHI mode considerations?

There are no restrictions.

#### Q. What is the default authorisation timeout period on Discover networks?

The default authorisation timeout period is 2 seconds (from Discover sending an authorisation message to receiving Threddâs response.