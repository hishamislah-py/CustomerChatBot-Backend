# 2.4 Card Scheme Elements Under <dataset>

Scheme-specific elements are addendum data that exist in the Level 2 and 3 reports. There can be one or more `<dataset>` elements containing addendum data and codes that form the `<``datasets>` element.

The sections below show you example elements, and how you can look up codes in the latest scheme documentation (for [Mastercard,](#Mastercard) [Visa](#Visa), and [Discover)](L2-L3_Report_Example.htm#top).

If you do not have access to the scheme-specific documentation, refer to your BIN sponsor who may be able to assist.

| Attribute | Description | Data Type | Required |
| --- | --- | --- | --- |
| name | This is the name of the dataset as provided by the scheme. | xs:string | Yes |
| code | This is the code of the dataset. **Note**: The code attribute under dataset is applicable to Visa only. | xs:string | No |
| element | The name of the element for the dataset that describe a category of information. | <element> | Yes |

## 2.4.1 Element

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

## 2.4.2 Looking Up Codes in Mastercard Documentation

You can look up the descriptions of Level 2 and 3 data within datasets in the *IPM Clearing Formats* manual.

If you do not have access to this manual, contact your Issuer.

1. Go to the following section in the guide: **PDS 0501 (Transaction Description)**.

   ![](../Resources/Images/PDS0501_page.png)

2. Scroll down to look up the Usage Code in **Subfield 1 (Usage Code)** which indicates the type of addendum data.
3. Scroll down to look up the Industry Record Number in **Subfield 2 (Industry Record Number)**. Both the Usage Code and the Industry Record Number identify the type of industry for the transaction.
4. Scroll down to look up the Occurrence Indicator in **Subfield 3 (Occurrence Number)**. This value identifies the occurrence of any addendum data for the specific Usage Code.

![](../Resources/Images/Occurance_indicator.png)

A dataset also includes the Associated First Presentment Number. This value corresponds to the presentment number in DE71. You will not need to look up this number in the Mastercard documentation

### Example for Mastercard Documentation

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

#### Look Up Codes for Corporate Detail

1. Go to the following section in the guide: **PDS 0501 (Transaction Description)**.

2. Scroll down and find information on Code **98**. This is the code for corporate details.
3. Scroll down and find information for **Occurrence Indicator** This is set to 001, where the value for Usage Code is 98 and Industry Record Number is 000.

## 2.4.3 Looking Up Codes in the Visa Documentation

You can look up the descriptions of Level 2 and 3 data within datasets in the *BASE II Clearing Interchange Formats*[1 If you do not have access to this Visa manual, consult your Issuer.](#) manual, sections *TC 01* to *TC 49*.

If you do not have access to this manual, contact your Issuer.

1. Go to the following section in the guide: **TC05 -TCR3 (Industry-Specific Data)**

![](../Resources/Images/visa_data.png)

2. Scroll down to relevant subsections after **TC 05 - TCR3 (Industry-Specific Data)**.
3. Scroll down to find the codes for the relevant industry. For example Airline, Passenger Itinerary includes different codes to Car Rental.

You may need to scroll down to check further information on the addendum data under the section titled Chapter 12: 33.B Capture Transactions Merchant.

### Example for Visa Documentation

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

#### Look Up Codes for Passenger Itinery Data

1. Search for **Passenger Itinerary Data**. The page has the following information: **TC 05 - TCR 3 Passenger-Itinerary
   Data**.

![](../Resources/Images/visa_doc.png)

2. Scroll down within the section and observe details for:

   | Element Name | Description |
   | --- | --- |
   | Transaction Code Qualifier | A type of identifier for the transaction code |
   | Transaction Code Sequence Number | The sequence of the transaction code |
   | Business Format Code | Indicates Airline, Passenger Itinerary |
   | Passenger Name | Name of the passenger |
   | Departure Date | Date of the departure |
   | Origination City/Airport Code | The code for the city/airport where the flight originated from |
   | Travel Agency Code | Code for the travel agency |
   | Travel Agency Name | Name for the travel agency |
   | Restricted Ticket Indicator | Indicates whether or not the ticket is refundable or non-refundable |
   | Fare Basis Code | This is an alphanumeric code for the fare status of a trip. There is a unique code for each leg of the trip. |
   | Computerized Reservation System | The system that handled the reservation. |
   | Flight Number | The flight number for each leg of the journey. |
   | Credit Reason Indicator | The reason for a cardholder to be credited in a transaction, such as a through a partial refund |
   | Ticket change indicator | The reason why a ticket was changed |

3. Scroll down to the section titled **TC 33.B - CP 55 TCR 2 Passenger Itinerary Data (Cont'd)**and observe details that include:

   | Element Name | Description |
   | --- | --- |
   | Trip Leg 4 Information | Details on the specific leg of the trip. |
   | Carrier Code | The name of the carrier for the specific leg of the trip. |
   | Service Class | The service class for the specific leg of the trip, e.g., first class. |
   | Destination City/Airport Code | Destination city or airport code for the specific leg of the trip. |

## 2.4.4 Looking Up Codes in the Discover Documentation

You can look up data in the *Electronic Interchange Manual - Issuer (Release 22.1)*.

If you do not have access to this manual, contact your Issuer.

1. Refer to the section with the following title: **Section 3 Interchange Charge-Type Specific Message**.

![](../Resources/Images/Discover_documentation.png)

2. From the introductory section, click on a cross-reference to the appropriate subsection.

Each subsection includes the following core data:

* Transaction Code
* Function Code
* Sending Institution Identification Code
* Recap Number
* Receiving Institution Identification Code
* Batch Number
* Sequence Number
* Subsequence Number

There are also Additional Data Records (ADRs), which include specific information for the addendum data.

For a summary of the codes, you can also refer to the [Discover Interchange Specific Data (Level 2 and 3 Data)](Discover_Interchange_Specifications.htm#top) page in this guide.

### Example for Discover Documentation

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

#### Look Up Codes for Airline Additional Detail

* To find information on the Airline Additional Record detail, search for the **Airline Additional Detail Record** section. This section contains information on the data within the above example, such as the IATA Agent Trading Name. The table within the page appears as follows:

![](../Resources/Images/airlineadditional_details.png)