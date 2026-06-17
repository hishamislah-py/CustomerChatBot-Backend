# About this Guide

This guide describes the Thredd External Host Interface (EHI) and provides technical specifications on how to integrate your systems to EHI.

The guide provides details of how to receive and respond to EHI messages in [JSON![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attributeâvalue pairs and arrays.](#) format.

## Document Scope

You should read this guide if you are using EHI for payment transaction authorisation and/or subscription to the EHI real-time payment transaction data feed.

## Target Audience

This guide is aimed at developers who need to integrate their applications to Thredd, using EHI.

## What's Changed?

If you want to find out what's changed since the previous release, see the [Document History](../Document_history.htm) section.

For a list of EHI fields available with each of the supported EHI versions, see [EHI Versions](../Appendices/EHI_Versions.htm).

## How to use this Guide

If you are new to EHI and want to understand how EHI works, we suggest you start with following topics: [Overview](Overview.htm), [EHI Operating Modes](EHI_operating_modes.htm) and typical [Transaction Flow Scenarios](Transaction_Flow_Scenarios.htm). See also the other topics in the [Getting Started](Overview.htm) section, including our [Best Practise for Customer Implementations](Version_Control.htm#Best).

If you are an experienced EHI developer or want to find out how to process EHI messages, see [Processing EHI Transactions](../Requirements/Processing_EHI_Transactions.htm).

To view message examples for different types of transactions, see  [Example Messages](../WSDL/GetTransaction_REST.htm).

## Conventions used in this Guide

When reading the tables in this guide, note the following information may be provided.

| Element | Description |
| --- | --- |
| Usage | * **Omitted** - can be omitted (fields not included) or included with an empty value (e.g., `"Bill_Ccy": ""`) * **Optional** - can be omitted (fields not included) or included with an empty value. Can be present (e.g., `"Bill_Ccy":"0"`) * **Mandatory** - field must be present. For example: `"Bill_Ccy": "978"` |
| Key | The field name. Please pay particular attention to the capitalisation and spelling. Where a field name is used within text, this is formatted as in the following example: `Bill_Ccy` or Bill\_Ccy (when used in a table note). |
| Data Types | The type of field data type supported. For details, including minimum and maximum lengths, see [Data Types](../Requirements/Data_Types.htm). |

## Related Documents

Refer to the table below for a list of other relevant documents that should be used together with this guide.

| Document | Description |
| --- | --- |
| Web Services Guide | Provides details of the Thredd Web Services API. |
| Cards API Documentation | For customers using the Thredd REST-based [Cards APIClosed The Thredd Cards API is a new REST-based API which can be used to connect to the Thredd system in place of using the traditional Thredd SOAP-based Web Services. The REST API provides messages in JSON format. If you are interested in the Cards API, please contact your Account Manager.](#), see the [Cards API Docs Website](https://cardsapidocs.thredd.com/). |
| [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm) | Describes how to use the Thredd Portal to manage your cards and transactions. |
| Smart Client Guide | Describes how to use the legacy Thredd [Smart ClientClosed The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product. The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.](#) desktop application to manage your account. |
| Chargeback Guide | Describes the chargeback process and options for managing chargebacks. |
| Transaction XML Reporting Guide | Describes the transaction XML report sent to Program Managers. |
| 3D Secure Guide | Describes the Thredd 3D Secure service. |
| Card Transaction System Guide | Describes how to submit card test transactions in the UAT environment. |

For the latest technical documentation, see the [Documentation Portal](https://docs.thredd.ai).