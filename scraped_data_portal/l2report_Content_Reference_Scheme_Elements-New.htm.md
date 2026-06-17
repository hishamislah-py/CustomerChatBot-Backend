# 2.2 Scheme Elements

Scheme-specific elements are addendum data that exist in the Level 2 and 3 reports. There can be one or more `<dataset>` elements containing addendum data and codes that form the `<``datasets>` element.

The sections below show you a worked example how you can look up codes in the latest scheme documentation (for [Mastercard,](#Mastercard) [Visa](#Visa), and [Discover)](L2-L3_Report_Example.htm#top). The sections also include the complete set of codes that are available for the respective schemes.

If you do not have access to the scheme-specific documentation, refer to your BIN sponsor who may be able to assist.

| Attribute | Description | Data Type | Required |
| --- | --- | --- | --- |
| name | This is the name of the dataset as provided by the scheme. | xs:string | Yes |
| code | This is the code of the dataset. **Note**: The code attribute under dataset is applicable to Visa only. | xs:string | No |
| element | The name of the element for the dataset that describe a category of information. | <element> | Yes |

## 2.2.1 Element

| Attribute | Description | Data Type | Required |
| --- | --- | --- | --- |
| name | This is the name of the element as provided by the scheme. | xs:string | Yes |
| code | This is the code for the transaction used by the different schemes, and determines the data that appears in the sub-elements.  **Note**: The code attribute under element is applicable to Mastercard only. | xs:string | No |
| data | The hexadecimal digits that hold the data for the element. | xs:string | No |
| subelement | The subelement under the element, which contain more Level 2 and 3 information. | <subelement> | No |

### Sub-Element

| Attribute | Description | Data Type |
| --- | --- | --- |
| name | The name of the subelement for the code in the element. | xs:string |
| data | The hexadecimal digits that hold the data for the element. | xs:string |

## 2.2.2 Mastercard Data

Mastercard data consists of the following:

* A standard 0501 code for transaction description.
* Usage Code â identifies the type of industry.
* Industry Record Number
* Occurrence Indicator

There is also a specific code for the First Presentment Number, which is associated with the transaction.

The information in this section is taken from the *IPM Clearing Formats documentation* from Mastercard. As the scheme may update the content periodically, you should always refer to the latest version of this documentation.

### Example Steps and XML Syntax

1. Go to the following section in the guide: PDS 0501 (Transaction Description).
2. Refer to information on Code 98. This is the code for corporate details.
3. Refer to information for the Occurrence Indicator This is set to 001, where the value for Usage Code is 98 and Industry Record Number is 000.

The following is an example based on a dataset for Corporate details, Corporate card common data requirements.

[Copy](javascript:void(0);)

```
    <dataset>  
                <name>Corporate detail, Corporate card common data requirements</name>  
                <elements>  
                <element>  
                <name>Transaction Description</name>  
                <code>0501</code>  
                <subElement>  
                <name>Usage Code</name>  
                <data>98</data>  
                </subElement>  
                <subElement>  
                <name>Industry Record Number</name>  
                <data>000</data>  
                </subElement>  
                <subElement>  
                <name>Occurence Indicator</name>  
                <data>001</data>  
                </subElement>  
                <subElement>  
                <name>Associated First Presentment Number</name>  
                <data>00000140</data>  
                </subElement>  
                </subElements>  
                </element>  
                </elements>  
    </dataset>        
```

### Usage Codes

| Code | Description |
| --- | --- |
| 01 | Passenger Transport Detail |
| 05 | Vehicle Rental Detail |
| 06 | Lodging Summary |
| 07 | Temporary Services |
| 08 | Shipping/Courier Services |
| 09 | Electronic Invoice, Transaction Data/  Party Information |
| 10 | Payment Transaction Details (e.g. from money transfer agents). |
| 11 | Telephony Billing, Detail/Summary |
| 12 | Travel Agency Detail |
| 13 | Lodged Account Detail (stored account detail from preferred travel agencies) |
| 14 | Private Label (new business opportunities unique to using private label cards) |
| 15 | Healthcare |
| 98 | Commercial detail (new business opportunities unique to  the corporate environment) |
| 99 | Generic Detail for other business opportunities |

### Industry Record Number

This is used in combination with the Usage Code.

| Usage Code | Industry Record Number | Industry |
| --- | --- | --- |
| 01 | 000 | Passenger Transport Detail, General Ticket Information |
| 01 | 001 | Passenger Transport Detail, Trip Leg Data |
| 01 | 002 | Passenger Transport Detail, Rail Data |
| 05 | 000 | Vehicle Rental Detail |
| 06 | 000 | Lodging Summary |
| 07 | 000 | Temporary Services |
| 08 | 000 | Shipping Courier Services |
| 09 | 000 | Electronic Invoice, Transaction Data |
| 09 | 001 | Electronic Invoice, Party Information |
| 10 | 000 | Payment Transaction Detail |
| 11 | 000 | Telephony Billing, Summary |
| 11 | 001 | Telephony Billing, Detail |
| 12 | 000 | Travel Agency Detail |
| 13 | 000 | Lodged Account Detail |
| 14 | 000 | Private Label Common Data |
| 14 | 001 | Private Line Item Detail |
| 15 | 000 | Healthcare IIAS detail |
| 98 | 000 | Corporate Detail, Corporate Card Common Data Requirements |
| 98 | 002 | Corporate Detail, Corporate Fleet Transaction Information |
| 98 | 950 | Corporate Detail, Corporate Line Item Detail |
| 99 | 000 | Generic Detail |

### Occurrence Indicator (Subfield 3)

This is the number of occurrences in which the message can occur in a transaction. For example, an Occurrence Indicator of 001-003, means that it can occur up to 3 times per transaction. The Occurrence Indicator corresponds to the Industry, Industry Record Number and Usage Code.

| Usage Code | Industry Record Number | Industry | Occurrence Indicator |
| --- | --- | --- | --- |
| 01 | 000 | Passenger Transport, General Ticket Information | 001 |
| 01 | 001 | Passenger Transport, Trip Leg Data | 002 to 999 |
| 01 | 002 | Passenger Transport Detail, Rail Data | 001 to 999 or 002 to 999 |
| 05 | 003 | Vehicle Rental Detail | 001 to 999 |
| 06 | 000 | Lodging Summary | 001 to 999 |
| 07 | 000 | Temporary Services | 001 to 999 |
| 08 | 000 | Shipping Courier Services | 001 to 999 |
| 09 | 000 | Electronic Invoice/Transaction Data | 001 to 999 |
| 09 | 001 | Electronic Invoice, Party Information | 002 to 999 |
| 10 | 000 | Payment Transaction Detail | 001 |
| 11 | 000 | Telephony Billing Summary | 001 |
| 11 | 001 | Telephony Billing Detail | 002 to 999 |
| 12 | 000 | Travel Agency Detail | 001 to 999 |
| 13 | 000 | Lodged Account, Detail | 001 to 999 |
| 14 | 000 | Private Label Common Data | 001 |
| 14 | 001 | Private Label Line Item Detail | 002 to 999 |
| 15 | 000 | Healthcare | 001 to 999 |
| 98 | 000 | Corporate Card Common Data Requirements | 001 |
| 98 | 002 | Corporate Fleet Transaction Information | 001 to 003 |
| 98 | 950 | Corporate Line Item Detail | 002 to 999 |
| 99 | 000 | Generic Detail | 001 to 999 |

## 2.2.3 Visa Data

Visa data consists of generic codes that are common for all industries, as well as specific data depending on the industry.

The information in this section is taken from the *BASE II Clearing Interchange Formats* manual. As the scheme may update the content periodically, you should always refer to the latest version of the documentation.

### Example Steps and XML Syntax

1. Search for Passenger Itinerary Data. The page has the following information: **TC 05 - TCR 3 Passenger-Itinerary Data.**
2. Observe details of the codes for Passenger Itinerary Data within the section.
3. Access the section titled **TC 33.B - CP 55 TCR 2 Passenger Itinerary Data (Cont'd)**  and observe further code details for the specific leg of the trip.

The following dataset shows an example for Airline, Passenger Itinery.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8" ?>  
<transactions>  
    <transaction>  
        <network>Visa</network>  
        <transactionType>Offline</transactionType>  
        <transactionId>6150991175</transactionId>  
        <transactionLinkId>2147505941</transactionLinkId>  
        <datasets>  
            <dataset>  
                <code>AI</code>  
                <name>Airline, Passenger Itinerary</name>  
                <elements>  
                    <element>  
                        <name>Transaction Code</name>  
                        <data>  </data>  
                    </element>  
                    <element>  
                        <name>Transaction Code Qualifier</name>  
                        <data>0</data>  
                    </element>  
                    <element>  
                        <name>Transaction Component Sequence Number</name>  
                        <data>3</data>  
                    </element>  
                    <element>  
                        <name>Business Application ID</name>  
                        <data>  </data>  
                    </element>  
                    <element>  
                        <name>Business Format Code</name>  
                        <data>AI</data>  
                    </element>  
                    <element>  
                        <name>Passenger Name</name>  
                        <data>AN/YUGYEONG         </data>  
                    </element>  
                    <element>  
                        <name>Departure Date</name>  
                        <data>060719</data>  
                    </element>  
                    <element>  
                        <name>Origination City/Airport Code</name>  
                        <data>XAA</data>  
                    </element>  
                    <element>  
                        <name>Trip Leg 1 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data>WS</data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data>Y</data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data>XAA</data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Trip Leg 2 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data>  </data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data>   </data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Trip Leg 3 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data>  </data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data>   </data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Trip Leg 4 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data>  </data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data> </data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data>   </data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Travel Agency Code</name>  
                        <data>        </data>  
                    </element>  
                    <element>  
                        <name>Travel Agency Name</name>  
                        <data>                         </data>  
                    </element>  
                    <element>  
                        <name>Restricted Ticket Indicator</name>  
                        <data>0</data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 1</name>  
                        <data>      </data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 2</name>  
                        <data>      </data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 3</name>  
                        <data>      </data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 4</name>  
                        <data>      </data>  
                    </element>  
                    <element>  
                        <name>Computerized Reservation System</name>  
                        <data>    </data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 1</name>  
                        <data>     </data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 2</name>  
                        <data>     </data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 3</name>  
                        <data>     </data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 4</name>  
                        <data>     </data>  
                    </element>  
                    <element>  
                        <name>Credit Reason Indicator</name>  
                        <data> </data>  
                    </element>  
                    <element>  
                        <name>Ticket Change Indicator</name>  
                        <data> </data>  
                    </element>  
                </elements>  
            </dataset>  
        </datasets>  
    </transaction>  
</transactions>
```

### Generic Codes

| Code | Description |
| --- | --- |
| Transaction Code | The code for the transaction. This is:  05 = Sales draft or dispute response financial  06 = Credit voucher or dispute response financial  07 = Cash disbursement or dispute response financial  15 = Sales draft dispute financial  16 = Credit voucher dispute financial  17 = Cash disbursement dispute financial  25 = Sales draft reversal  26 = Credit voucher reversal  27 = Cash disbursement reversal  35 = Sales draft dispute financial reversal  36 = Credit voucher dispute financial reversal  37 = Cash disbursement dispute financial reversal  Dispute response financial transactions must have the original transaction code. |
| Transaction Code Qualifier | This field must contain one of these values:  0 = Default  1 = Account Funding  2 = Original Credit |
| Transaction Component Sequence Number | The field must contain a 0 (zero). |
| Business Application ID | This field provides additional information regarding the usage and application of the transaction.  Business Application ID is not used for Loan Detail data. |
| Business Format Code | Code indicating the type of business that is applicable to this transaction. If the Merchant Category Code on the TCR 0 indicates an airline or a passenger railway, this field must contain AI (Passenger Itinerary) format. This entry is not valid for cash disbursement transactions. |
| Reserved | Reserved for Future Use |

### Specific Industry Data

The following describes the industry-specific data that is included in each `<name>` element. The `<data>` element contains values for that `<name>`.

| Passenger-Itinerary Data | |
| --- | --- |
| Passenger Name | Departure Date (MMDDYY) |
| Origination City/Airport Code | Trip Leg 1 Information |
| Trip Leg 2 Information | Trip Leg 3 Information |
| Trip Leg 4 Information | Travel Agency Code |
| Travel Agency Name | Restricted Ticket Indicator |
| Fare Basis Code Leg 1 | Fare Basis Code Leg 2 |
| Fare Basis Code Leg 3 | Fare Basis Code Leg 4 |
| Computerised Reservation System | Flight Number Leg 1 |
| Flight Number Leg 2 | Flight Number Leg 3 |
| Flight Number Leg 4 | Credit Reason Indicator |
| Ticket Change Indicator | Carrier Code |
| Service Class | Stop-over Code |
| Destination City/Airport Code |  |

| Passenger Transport Ancillary Data | |
| --- | --- |
| Ancillary Ticket Document Number | Ancillary Service Category 1 |
| Ancillary Service Sub-Category 1 | Ancillary Service Category 2 |
| Ancillary Service Sub-Category 2 | Ancillary Service Category 3 |
| Ancillary Service Sub-Category 3 | Ancillary Service Category 4 |
| Ancillary Service Sub-Category 4 | Passenger Name |
| Issued in Connection With Ticket Number | Credit Reason Indicator |

| Lodging | |
| --- | --- |
| Lodging No-Show Indicator | Lodging Extra Charges |
| Lodging Check-In Date (YYMMDD) | Daily Room Rate |
| Total Tax | Prepaid Expenses |
| Food/Beverage Charges | Folio Cash Advances |
| Room Nights | Total Room Tax |

| Car Rental | |
| --- | --- |
| Days Rented | Car Rental No-Show Indicator |
| Car Rental Extra Charges | Car Rental Check-out Date (YYMMDD) |
| Daily Rental Rate | Weekly Rental Rate |
| Insurance Charges | Fuel Charges |
| Car Class Code | One-Way Drop-off Charges |
| Renter Name |  |

| EMV Fleet Service | |
| --- | --- |
| Fleet Employee Number | Type of Purchase |
| Expanded Fuel Type | Service Type |
| Unit of Measure | Quantity |
| Unit Cost | Gross Fuel Price |
| Net Fuel Price | Gross Non-Fuel Price |
| Net Non-Fuel Price | Odometer Reading |
| VAT/Tax Rate | Fleet Trailer Number |
| Fleet Additional Prompted Data 1 | Fleet Additional Prompted Data 2 |

| Fleet Service | |
| --- | --- |
| Expanded Fuel Type | Type of Purchase |
| Fuel Type | Unit of Measure |
| Quantity | Unit Cost |
| Gross Fuel Price | Net Fuel Price |
| Gross Non-Fuel Price | Net Non-Fuel Price |
| Odometer Reading | VAT/Tax Rate |
| Miscellaneous Fuel Tax | Product Qualifier |
| Miscellaneous Non-Fuel Tax | Service Type |
| Miscellaneous Fuel Tax Exemption Status | Miscellaneous Non-Fuel Tax Exemption Status |

| Loan Detail | |
| --- | --- |
| Cardholder Tax ID Type | Cardholder Tax ID |
| Asset Indicator | Loan Type |
| Merchant Program Identifier |  |

| Business Application Data | |
| --- | --- |
| Service Processing Type | Fast Funds Indicator |
| Source of Funds | Payment Reversal Reason Code |
| Sender Reference Number | Sender Account Number |
| Sender Name | Sender Address |
| Sender City | Sender State |
| Sender Country |  |

## 2.2.4 Discover Data

Discover consists of core and industry-specific data. Core transaction records by incorporating Additional Detail Records (ADRs), which provide granular data for the various industries.

The information in this section is taken from the Electronic Interchange Manual - Issuer (Release 22.1). As the scheme may update the content periodically. You should always refer to the latest version of the manual.

### Example Steps and XML Syntax

1. Refer to the section titled **Section 3 Interchange Charge-Type Specific Message**.
2. From the introductory section, refer to the appropriate subsections.
3. Observe details on the core message fields followed by the ADR information on **Airline Additional Records**.

The following dataset shows an example for Airline Additional Detail Records.

[Copy](javascript:void(0);)

```
  <dataset>  
        <code>XA</code>  
        <name>Airline Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XA</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>601</data>  
          </element>  
          <element>  
            <name>Receiving Institution Identification Code</name>  
            <code>DFTER</code>  
            <data>I7</data>  
          </element>  
          <element>  
            <name>Batch Number</name>  
            <code>BATCH</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Sequence Number within the batch</name>  
            <code>SEQNO</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Sub-Sequence within the charge</name>  
            <code>SUSEQ</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Ticket-issuing airline Code</name>  
            <code>AIRCD</code>  
            <data>110</data>  
          </element>  
          <element>  
            <name>Booking Reference Number</name>  
            <code>AIRRF</code>  
            <data>AIRLINE.REF</data>  
          </element>  
          <element>  
            <name>Agent Fees</name>  
            <code>AGAFE</code>  
            <data>10.00</data>  
          </element>  
          <element>  
            <name>Agent Fee Reference</name>  
            <code>AGARF</code>  
            <data>AGENCY.REF</data>  
          </element>  
          <element>  
            <name>Agent Fee Description</name>  
            <code>AGADS</code>  
            <data>BOOKING.FEE</data>  
          </element>  
          <element>  
            <name>IATA Agent code (includes check digit)</name>  
            <code>IATCD</code>  
            <data>86105301</data>  
          </element>  
          <element>  
            <name>IATA Agent Trading name</name>  
            <code>IATNM</code>  
            <data>MALTESE.TRAVEL</data>  
          </element>  
          <element>  
            <name>Agent Address Line 1</name>  
            <code>AGAD1</code>  
            <data>897 BUGIBBA ROAD</data>  
          </element>  
          <element>  
            <name>Agent Address Line 2</name>  
            <code>AGAD2</code>  
            <data />  
          </element>  
          <element>  
            <name>Agent Address Line 3</name>  
            <code>AGAD3</code>  
            <data />  
          </element>  
          <element>  
            <name>Agent City</name>  
            <code>AGCTY</code>  
            <data>VALLETTA</data>  
          </element>  
          <element>  
            <name>Agent State/County</name>  
            <code>AGSTA</code>  
            <data>COUNTY</data>  
          </element>  
          <element>  
            <name>Agent Zip Code</name>  
            <code>AGZIP</code>  
            <data>BK1 7DF</data>  
          </element>  
          <element>  
            <name>Agent Geographic Code</name>  
            <code>AGGCD</code>  
            <data>470</data>  
          </element>  
          <element>  
            <name>Agent International dialing code</name>  
            <code>PNODC</code>  
            <data>44</data>  
          </element>  
          <element>  
            <name>Agent Area Code</name>  
            <code>PNOAC</code>  
            <data>1189</data>  
          </element>  
          <element>  
            <name>Agent Telephone Number</name>  
            <code>PNONO</code>  
            <data>227528</data>  
          </element>  
          <element>  
            <name>Computerized Reservation System Code</name>  
            <code>RESSY</code>  
            <data>AB</data>  
          </element>  
        </elements>  
  </dataset>
```

### Core Message Fields

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

### Travel & Entertainment Additional Detail Records (ADRs)

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

For more details on the codes within the ADR function codes, see [Industry-Specific Codes for Discover](Industry-Specific Codes for Discover.htm).