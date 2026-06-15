# General FAQs

## Cards API

### Q. What is the Cards API Website?

This website provides details of our REST-based cards API. Thredd provides two options to connect to our systems to create and manage cards:

* **Cards API** - our new, modern API based on RESTful principles as described on this website
* **Thredd API** - our traditional SOAP-based API, as described on our main [Documentation Portal](https://docs.thredd.com/) website.

### Q. How can I try out the Cards API?

The [API Explorer](https://cardsapidocs.thredd.com/reference/introduction-1) section on this website provides the API endpoints, code examples and field details you need to submit requests.  We provide a Postman Collection, which you can download and use for trying the Cards API.

> 📘 Note
>
> Thredd treats security of our environments as a priority, and for this reason we provide restricted access to our API.\
> To use the cards API, please contact Thredd to request secure access to
> \<BrandName> systems and/or allow requests to be made from your static IP address.

> 📘 Note
>
> We are currently developing the integrated functionality that will enable you to automatically generate a secure access token and submit transactions directly from the API Explorer section of this website.

### Q. Are there additional Cards API not listed on this website?

Yes, the Thredd cards API is still a fairly new addition to the Thredd product portfolio and is currently undergoing significant development. You can expect to see additional API added to this website as Thredd release new API endpoints.

> 📘 Note
>
> If you want to get an overview of the full set of functionality available within Thredd for creating and managing the cards in your program, please see our SOAP-based [Web Services Guide](https://docs.thredd.com/Web_Services_Guide.htm).

### Q. How do I emulate a payment transaction using REST?

There is currently no way of emulating a payment transaction in the UAT Cards API.

### Q. How can I change the limit groups for a card?

You can change the limit groups associated with a card by using the Update Card Control Groups endpoint. For more information on this, see [Managing Card Usage Groups.](https://cardsapidocs.thredd.com/docs/card-controls)

### Q. Do I need to be PCI Compliant to use the Get PIN endpoint?

You do not need to be PCI Compliant to use the Get PIN (and other associated PIN endpoints) endpoint.

### Q. Do we have an SDK for the Cards API?

Thredd does not currently support an SDK for the Cards API.

### Q. Do you have a list of currency codes?

You can find a list of valid currency codes in the [Web Services Guide](https://docs.thredd.com/webservices/Content/Reference/Currency_Codes.htm).

### Q. What is Card Fulfilment?

Card fulfilment is the creation of a physical card (sent to a Card Manufacturer for printing). Creating a physical card requires you to set a fulfilment address which the card manufacturer can send the card to.

For more information on creating a physical card, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

### Q. What is SOAP?

SOAP (Simple Object Access Protocol), which is a messaging protocol for exchanging structured information in the implementation of web services. It uses Extensible Markup Language (XML) for its message format and relies on application layer protocols such as HTTP for message negotiation and transmission. SOAP allows developers to invoke processes running on disparate operating systems (such as Windows, macOS, and Linux) to authenticate, authorise and communicate using XML.

For more information on our Thredd API, see the [Web Services Guide](https://docs.thredd.com/Web_Services_Guide.htm).

### How do I issue cards (BIN Sponsor)?

To issue cards, you must be set up on our systems and have an issuer, or be a self issuer. When you are set up in our systems you can create a card, but you will need a card manufacturer to physically create a card. For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

### How much does it cost to issue a card?

Contact your account manager to learn the cost of issuing a card.

### Why do some fields provide a maximum limit of 2147483647?

The limitation of 2,147,483,647 arises from the constraints of 32-bit signed integers in computing. It is widely adopted across programming languages and database systems to ensure consistent handling of numerical data/integers and to avoid overflow errors.

## Card Configuration

### Q. How do I block MCC?

Merchant Category Codes (MCC) are four-digit numbers that describe a merchant's primary business activities. MCCs are used by credit card issuers to identify the type of business in which a merchant is engaged. You can configure your card products to control card usage, for example to allow or deny card usage based on the MCC and limit usage of the card to the domestic country. For example: you can block card usage on gambling and adult sites, based on the MCC.

The Smart Client application can be used to set a block on an MCC group. For more information, see the [Smart Client Guide](https://docs.thredd.com/Smart_Client_Guide.htm).

### Q. How do I set limits?

You can set card limits using the Update Card Control Groups endpoint. For more information on this endpoint, see [Managing Card Usage Groups](https://cardsapidocs.thredd.com/docs/card-controls).

### Q. Do you support single use cards?

Thredd supports single use cards. For more information, see the [Virtual Cards Guide](https://docs.thredd.com/Virtual_Cards_Guide.htm).

### Q. How do I freeze a card?

To freeze a card using Cards API, use the Update Card Status and in the body set the `cardStatusCode` field to `G2`. For example:

```json Example Card Freeze Status body
{
  "cardStatusCode": "G2",
  "updatedBy": "John Bloggs",
  "description": "Card Frozen",
  "validityDate": "2023-08"
}
```

For more information, see [Card Status](https://cardsapidocs.thredd.com/docs/card-status).

### Q. How do I use push provisioning?

Push provisioning (also referred to as in-app authentication) is a process where the Program Manager (i.e., your systems) pre-authenticates the cardholder before the first token provisioning message is sent to the token service provider (Visa/Mastercard/MNE). For information on the requirements for push provisioning cardholder authentication, please discuss with your mobile wallet token requestor.

Push provisioning requires you to share sensitive card data held on your system with the token service provider (without the cardholder needing to manually enter the PAN details into their mobile application). The cardholder must be logged into their account (i.e., logged in to their mobile application) in order to be able to authenticate.

To implement push provisioning, you can either do this directly with the token service provider or via a [Thredd Supported Third Party for Push Provisioning](https://docs.thredd.com/tokenisation/Content/Getting_Started/How_Tokenisation_Works.htm#_GPS-Meawallet_Integration_for).

### Q. What is CVV2?

Card Verification Value 2 (CVV2) is a three or four digit code printed on the back of a card. It is used to help prevent fake magnetic stripe transactions, but is vulnerable to copying if someone can see the original magnetic stripe data.

For more information, see the [Physical Card Configuration Guide](https://docs.thredd.com/Physical_Cards_Guide.htm).

### How can I configure cards to support an ecommerce transaction?

To use a card for an ecommerce transaction, the card must be associated with a usage group that has the *Card not present (ecommerce)* Card Acceptance Method. You can check which card usage group is associated with your card by using the [List Card Control Groups](https://cardsapidocs.thredd.com/reference/list-card-control-groups-1) endpoint.

For information on how to configure cards, see the [Physical Card Configuration Guide](https://docs.thredd.com/Physical_Cards_Guide.htm).

## 3DS/Tokenisation

### Q. How can I enrol a card in 3DS?

You can create a 3D Secure credential for a card using the Create a 3D Secure Credential endpoint. For more information, see [Managing 3D Secure Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials).

### Q. What is OTP?

Cardinal generates a single-use One-Time Password (OTP). Thredd sends the OTP in a SMS text message to the cardholder’s mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction. For more information see [3D Secure Guide (Apata)](https://docs.thredd.com/3D_Secure_Apata.htm), or [3D Secure Guide (Cardinal)](https://docs.thredd.com/3D_Secure_RDX.htm)

## Transaction Management

### Q. Which EHI modes support Thredd maintaining the balance?

There are two EHI modes where Thredd can maintain the balance.

* Cooperative Processing (Mode 2), where Thredd maintains the balance and performs authorisation. You can override an approval decision.
* Full Service Processing (Mode 3), where Thredd maintains the balance and performs authorisation. You receive a read-only response.

For more information, see the [EHI Guide](https://docs.thredd.com/EHI_Guide.htm).

### Q. What is Cooperative Auth?

A cooperative authorisation is an authorisation where both Thredd UK Ltd. and the Program Manager collaborate during the authorisation process to approve or decline a payment authorisation request. This option is supported using certain modes on the External Host Interface (EHI), such as Cooperative Processing (Mode 2).  For more information, see the [EHI Guide](https://docs.thredd.com/EHI_Guide.htm).

### Q. What is a hanging filter?

A hanging filter is the period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth. For more information, see the [EHI Guide](https://docs.thredd.com/EHI_Guide.htm).

### Q. What is PCI DSS?

The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major card schemes (payment network). All Program Managers who handle customer card data must be compliant with this standard. See: [https://www.pcisecuritystandards.org/pci\_security/](https://www.pcisecuritystandards.org/pci_security/)\
For more information, see the [Key Concepts Guide](https://docs.thredd.com/Key_Concepts_Guide.htm).

## General Questions

### Q. Where can I get information on pricing?

For information on pricing, contact your Account Manager.

### Q. What is SFTP?

Secure File Transfer Protocol (SFTP) is a file protocol for transferring large files over the web. It builds on the File Transfer Protocol (FTP) and includes Secure Shell (SSH) security components. Thredd UK Ltd. uses SFTP for our balance and transaction reporting. For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.com/Transaction_XML_Reporting_Guide.htm), and the [Balance XML Reporting Guide](https://docs.thredd.com/Balance_XML_Reporting_Guide.htm).

### How do I launch a card program?

For information on how to launch a card program, see the [Getting Started Guide](https://docs.thredd.com/Getting_Started_Guide.htm).

### What types of card products do you offer?

We provide virtual cards, physical cards and master virtual cards. For more information, refer to [Thredd Cards](https://docs.thredd.com/More_Information/Cards.htm).

### What credit products do you offer?

We do not offer any credit products. We can process credit BINs and help enable credit products through virtual cards.

### Who controls the card balance (ledger)?

Who controls the card balance depends on the EHI Mode that you're using. See the below table to see who controls the card balance for each EHI Mode.

| EHI Mode                              | Who controls the card balance (ledger)? |
| :------------------------------------ | :-------------------------------------- |
| Gateway Processing (Mode 1)           | You control the card balance.           |
| Cooperative Processing (Mode 2)       | Thredd controls the card balance.       |
| Full Service Processing (Mode 3)      | Thredd controls the card balance.       |
| Gateway Processing with STIP (Mode 4) | You control the card balance.           |
| Gateway Processing with STIP (Mode 5) | You control the card balance.           |

For more information on EHI Modes, see the [EHI Guide](https://docs.thredd.com/EHI_Guide.htm).

### What is a Program Manager?

A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.

### What kind of fraud protection do you offer?

We offer a range of transaction monitoring and fraud protection services. For more information, see [Managing Risk](https://docs.thredd.com/More_Information/Managing_Risk.htm).