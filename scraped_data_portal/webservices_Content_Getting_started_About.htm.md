# About this Guide

This guide is intended as a reference guide, to provide information on the available Thredd web services and fields in each web service.

## Target audience

This guide is aimed at developers who need to integrate their applications to Thredd, using our SOAP-based web services. You should know how to implement SOAP-based calls and handle the response.

## What's changed?

If you want to find out what's changed since the previous release, see the [Document History](../Reference/Document_History.htm) section.

## How to use this Guide

Before you start:

* Make sure you have read the [Integration Steps](Integration_steps.htm) section and understand what information and system access you will need to be able to use the web service sandbox and test environments.
* Read the [Use Case Scenarios](User_Scenarios.htm) section, which explains how to implement the most common user scenarios and provides recommendations as to which web services to use.
* Make sure you can connect to the Thredd web service, by implementing a simple call, as explained in [Using the API](Using_SOAP.htm).

If you are an experienced user and don't want to read through the Getting Started sections, you can go directly to the [Web Services API](../Web_services_api/Introduction_to_API.htm) section.

### Implementing web service calls

* When implementing a web service request, you must at a minimum include the mandatory request fields and handle the fields that are mandatory in the response.
* Where a field requires you to submit a code value or returns a code value, the guide provides links to the relevant appendix for details. If in doubt as to which code to include in your request, you should use the default or recommended value.
* Do not change the default `xmlns` attributes (XML namespaces) in the SOAP request.
* Don't use spaces in xml tags.
* Please pay particular attention to XML tag name spelling and capitalisation. Different web services may sometimes adopt different case and naming conventions. If in doubt, always refer to the Thredd-provided SOAP [WSDL![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Web Service Definition Language (WSDL) is an XML format for describing network services as a set of endpoints operating on messages containing either document-oriented or procedure-oriented information.
  WSDL files are central to testing SOAP-based services. SoapUI uses WSDL files to generate test requests, assertions and mock services.](#). See [Using the API](Using_SOAP.htm).

## Conventions used in this Guide

When reading the tables in this guide, note the following information is provided for each XML field:

| Element | Description |
| --- | --- |
| Tag | The XML tag name. Please pay particular attention to the capitalisation and spelling. Where a tag name is used within text, this is formatted as in the following example: `<ActionCode>` |
| Type | The type of field value supported. Options include:  N = number  AN = alpha-numeric  YYYY-MM-DD = date format: Year-Month-Date  HHMMSS = time format: Hour-Minute-Second  D = decimal  B = boolean |
| Minimum / Maximum Length | The allowed minimum and maximum field length. If in doubt, refer to the WSDL or examples provided in the guide. |
| Request / Response | The status of the field in the request and response. Options are:  Mandatory = must be included in the request and will be in the response  Conditional = this field is mandatory under specified conditions. Refer to the description for details.  Optional = can be included. May be in the response.  Omit = you should omit this field. Will not be in the response |

## Related Documents

Refer to the table below for a list of other relevant documents that should be used together with this guide.

| Document | Description |
| --- | --- |
| [EHI Guide](https://docs.thredd.aiEHI_Guide.htm) | Provides details of the Thredd [External Host Interface (EHI)Closed External Host Interface (EHI) is a Thredd facility that enables exchange of data between the Thredd processing centre and external systems using online web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions such as Authorisations, the External Host can participate in payment transaction authorisation.](#). |
| [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm) | Describes how to use the Thredd [Smart ClientClosed Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#) to manage your account. |
| [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm) | Describes how to use the Thredd Portal to manage your cards and transactions. |
| [Card Generation Interface Specification](https://docs.thredd.ai/Card_Generation_Interface_Specification.htm) | Provides detailed specifications for card manufacturers on Thredd card creation. |
| [3D Secure Guide (Apata)](https://docs.thredd.ai/3D_Secure_Apata.htm) | Describes the Thredd 3D Secure Apata service. |
| [3D Secure Guide (Cardinal)](https://docs.thredd.ai/3D_Secure_RDX.htm) | Describes the Thredd 3D Secure Cardinal service. |
| [Fraud Transaction Monitoring Guides](https://docs.thredd.ai/Fraud_Transaction_Monitoring.htm) | Describes the Thredd fraud protection service. |

For the latest technical documentation, see the [Documentation Portal](https://docs.thredd.ai).