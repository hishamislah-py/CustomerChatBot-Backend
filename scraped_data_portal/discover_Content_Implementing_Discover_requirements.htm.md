# 6 Discover Project Requirements

Delete this text and replace it with your own content.

## 6.1 Card Issuing on Discover

### 6.1.1 Issuer Documentation and Certification

You must work with a certified Issuer-Processor, such as Thredd, to access the Discover Network.

Issuers or their processors must complete a certification process with Discover to enable acceptance of Discover cards and products. This requires integrating with Discover's Deliver product and completing the necessary testing and validation.

The Xpress Participant Information Document (PID) should be completed by your Thredd Implementation Manager with your support.

### 6.1.2 Issuing BINs

The Bank Identification Number (BIN) is the first 6-8 digits of the card number.

For Thredd Program Managers, the BIN ranges provided start with â36â and PAN length of 14 digits.

Discover provides resources and testing kits to help partners integrate and enable support for the full range of Discover BINs, ensuring a seamless payment experience for all Discover cardholders.

Discover acts as the network provider, facilitating the acceptance and processing of transactions across a diverse set of BIN ranges.

For more information, see [discoverglobalnetwork.com: bin-ranges](https://www.discoverglobalnetwork.com/resources/payments-providers/bin-ranges/)

### 6.1.3 Scheme Stand-In Processing (STIP)

Thredd can support Discover Scheme Stand-in Processing (STIP) if required. If enabled, the Discover Network will handle transaction authorisation requests if Thredd or your systems are unavailable or unable to respond to a transaction authorisation request within the required time.

For information on how the Discover Xpress system handles STIP authorisations and the circumstances which can result in a decline and a *Do Not Honour* response, refer to the *Discover Xpress Guide to System Use > Section 4, Xpress Network Stand-in Authorization Processing*.

For further details, please contact your Thredd account manager.

### 6.1.4 Issuer Identification Code

The Issuer Identification Number (IIN) identifies the Issuer Settlement Currencies and can be 11 digits long, also known as the BIN. The Issuer Identification Code (IIC) identifies the card issuing institution and is the first 6-8 digits of the card number.

This information is crucial for routing the transaction to the correct payment network and initiating the necessary communication between the various parties involved. The structured format of the IIC/IIN facilitates efficient routing, settlement, and reconciliation of transactions across the payment ecosystem.

The IIC identifies issuer and the IIN (BIN) identifies card allows payment processors and merchants to quickly verify the authenticity of a card and detect potential fraudulent activities.

By identifying the issuing institution, the IIC/IIN enables real-time monitoring of card usage patterns and triggers alerts for any unauthorised transactions.

## 6.2 Working with Issuers

For Program Managers who are not self-issuing on Discover Networks, your issuer will need to have completed Discover Network certification and IIC registration.

Your issuer will also need to approve your account setup on Thredd and the Discover Network, and provide you with access to relevant Discover Network tools, Portals and documentation.

## 6.3 Thredd Setup and Configuration

### 6.3.1 Completing the Product Setup Form (PSF)

Your Thredd Implementation Manager will guide you through fields and settings that are relevant to Discover.

### 6.3.2 EHI Setup and Integration

The Thredd External Host Interface (EHI) is a system which coordinates payment authorisation and financial messages, processed on the Thredd Platform, and communicates with your external systems in real-time, to support the payment authentication process.

For details of setup options for receiving your Discover transaction messages through EHI, see the [External Host Interface (EHI) Guide > EHI Configuration Options.](https://docs.thredd.com/ehi/Content/Getting_Started/EHI_Configuration_Options.htm)

#### Already Integrated to EHI?

For Program Managers with an existing EHI integration:

* You can use the same EHI endpoint for receiving your EHI messages or you can set up a separate external host endpoint to receive authorisation and financial messages.
* The message fields are the same as used with other Card Scheme networks (e.g., Visa and Mastercard). Your systems will need to process some new field values. There are new fields you will need to support. For details, see [GetTransaction Message Fields](../Appendices/GetTransaction_Message.htm) in this guide.
* Please check the sample data and example messages provided in this guide, for a flavour of the type of data your systems will receive from Discover Networks. See [Discover Message Examples](../Appendices/Discover_message_examples.htm).

#### Not Integrated to EHI?

For Program Managers who do not have an existing EHI integration, please refer to the [External Host Interface Guide](https://docs.thredd.com/EHI_Guide.htm).

Notes

* Thredd support both XML and JSON formats of EHI messages.
* There are no restrictions on usage of EHI mode with Discover. For details of available modes, see the [External Host Interface (EHI) Guide > EHI Operating Modes](https://docs.thredd.com/ehi/Content/Getting_Started/EHI_operating_modes.htm).