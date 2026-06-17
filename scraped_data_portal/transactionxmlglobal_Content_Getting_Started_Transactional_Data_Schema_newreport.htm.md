# 1.4 Reports Data Schema

The data schemas for the Non-Clearing Report and Clearing Report in Global Transaction Reporting describe their structure and possible data values within those reports.

You can validate each transaction XML file you receive from Thredd against the provided Schema (XSD file). This ensures that the transaction file is in the correct format.

The data schemas for the Non-Clearing Report and Clearing Report are subject to change as the standard evolves. When Thredd updates either XSD report file, Thredd implements a new version and notifies you.

## 1.4.1 Schema Versions

Schema files are versioned according to changes in the schemas. The schema filename indicates the schema version number. There is a comments section in each schema file that provides details of the version changes. Thredd sends schema files when a new version of the XML is published.

For an example of the current data schema, see the [Non-Clearing Report XML Data Schema](../Reference/Non-Clearing_Report_XML_Schema.htm) and [Clearing Report XML Data Schema](../Reference/Clearing_Report_XML_Schema.htm).

## 1.4.2 Schema Elements

An XML file conforming to the schema consists of the following elements:

* [Primary elements](../Schema/Primary_Elements_newreport.htm)
* [Sub-elements and attributes](../Schema/Sub_Elements_and_Attributes.htm)