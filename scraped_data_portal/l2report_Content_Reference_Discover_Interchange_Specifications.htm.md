# Discover Interchange Data

This section is only applicable to data processed on the Discover Global Network (DGN).

## Overview

In the Discover Electronic Interchange environment, Interchange Charge-Type Specific Messages are structured electronic messages for transmitting transaction-level data among Acquirers, Issuers, Diners Club, International Member Establishments, and other entities recognised as Interchange Institutions. These messages allow:

* Transaction settlement
* Payment reconciliation
* Regulatory compliance
* Dispute resolution and chargeback support

Discover enhances core transaction records by incorporating Additional Detail Records (ADRs). These records provide granular, industry-specific data related to airline tickets, hotel stays, car rentals, and more, which assist in corporate reporting, expense management, and fraud mitigation. Some transactions, particularly travel agency purchases, may include multiple ADRs linked together. These are transmitted sequentially following the main Charge Detail (XD) message. The following is an example of the sequence:

* XD â Charge Detail Message
* XA â Airline Additional Detail
* XB â Airline Routing
* XV â Car Rental
* XH â Hotel Stay
* XR â Rail Ticket
* XL â Rail Routing

## Core Message Fields

The following are core message fields in ADRs. These are populated regardless of the provided industry data.

| Field Name | Description | Format/Type |
| --- | --- | --- |
| Transaction Code | This code identifies the type of transaction (e.g., RFRC for charge records). | 4-character string |
| Function Code | This code specifies the type of ADR (e.g., XA, XB). | 2-character code |
| Sending Institution ID | The ID of the institution that is sending the message. | 3-digit numeric |
| Recap Number | An internal tracking number for the message. | 3-digit numeric |
| Receiving Institution ID | The ID of the institution that is receiving the message. | 3-digit numeric |
| Batch Number | A unique identifier for the batch of transactions. | 3-digit numeric |
| Sequence Number | Indicates the order of the record within the batch. | 3-digit numeric |
| Sub-Sequence Number | Indicates the order of the record within the transaction where there are multiple ADRs. | 3-digit numeric |
| Additional Detail Fields | Specific fields related to the Function Code (e.g., XA, XB). | Varies |

## Travel & Entertainment Additional Detail Records (ADRs)

The following is a list of supported ADR Function Codes, along with their record names and descriptions:

| Function Code | Record Name | Description |
| --- | --- | --- |
| XA | Airline Additional Detail Record | Includes ticket issuer infomation, booking references, travel agent, and reservation data. |
| XB | Airline Routing Detail Record | Includes carrier, flight number, airports, fare class, and flight segments. |
| XC | ATM Additional Detail Record | Captures ATM ID, terminal location, transaction time. |
| XV | Car Rental Additional Detail | Captures rental agency, duration, contract, rates. |
| XG | Gasoline Additional Detail | Vehicle details, fuel amount, pricing, pump ID. |
| XH | Hotel Additional Detail Record | Hotel name, location, folio number, stay dates, rate. |
| XR | Rail Additional Detail Record | Rail ticket details, passenger info, travel agent data. |
| XL | Rail Routing Detail Record | Train numbers, classes, origin/destination stations, fare class. |
| XE | Restaurant Additional Detail | Itemised expense breakdown (food, beverage, gratuity, tax). |
| XT | Telephone Additional Detail | Origin/destination, duration, time/date, surcharge/discount. |
| XM | Chip Card Additional Detail | EMV chip data: Application ID, cryptograms, transaction certificate. |

If an XM (Chip Card) record is present, it must immediately follow the base transaction detail message (XD), before any other ADRs.