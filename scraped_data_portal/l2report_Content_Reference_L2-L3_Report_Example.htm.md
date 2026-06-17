# 2.3 Level 2 and 3 Report Examples

The following are example Level 2 and 3 reports for Mastercard and Visa.

## 2.3.1 Mastercard Example

[Copy](javascript:void(0);)

```
<transactions>  
    <transaction>  
        <network>Mastercard</network>  
        <transactionType>Offline</transactionType>  
        <transactionId>6150932738</transactionId>  
        <transactionLinkId>2147488665</transactionLinkId>  
        <datasets>  
            <dataset>  
                <name>Corporate Detail, Corporate Card Common Data Requirements</name>  
                <elements>  
                    <element>  
                        <name>Transaction Description</name>  
                        <code>0501</code>  
                        <subElements>  
                            <subElement>  
                                <name>Usage Code</name>  
                                <data>98</data>  
                            </subElement>  
                            <subElement>  
                                <name>Industry Record Number</name>  
                                <data>000</data>  
                            </subElement>  
                            <subElement>  
                                <name>Occurrence Indicator </name>  
                                <data>001</data>  
                            </subElement>  
                            <subElement>  
                                <name>Associated First Presentment Number</name>  
                                <data>00000140</data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Card Acceptor Type</name>  
                        <code>0595</code>  
                        <subElements>  
                            <subElement>  
                                <name>Business Type</name>  
                                <data>2</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Owner Type</name>  
                                <data>0</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Certification Type</name>  
                                <data>0</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Racial/Ethnic Type</name>  
                                <data>0</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Type Provided Code</name>  
                                <data>R</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Owner Type Provided Code</name>  
                                <data>N</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Certification Type Provided Code</name>  
                                <data>N</data>  
                            </subElement>  
                            <subElement>  
                                <name>Business Racial/Ethnic Type Provided Code</name>  
                                <data>N</data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Card Acceptor Tax ID</name>  
                        <code>0596</code>  
                        <subElements>  
                            <subElement>  
                                <name>Acceptor Tax ID</name>  
                                <data/>  
                            </subElement>  
                            <subElement>  
                                <name>Acceptor Tax ID Provided Code</name>  
                                <data>N</data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Total Tax Collected Indicator</name>  
                        <code>0598</code>  
                        <data></data>  
                    </element>  
                </elements>  
            </dataset>  
        </datasets>  
    </transaction>  
    <transaction>  
        <network>Visa</network>  
        <transactionType>Online</transactionType>  
        <transactionId>6151300962</transactionId>  
        <transactionLinkId>2147921713</transactionLinkId>  
        <datasets>  
            <dataset>  
                <code>56</code>  
                <name>Payment Facilitator Data</name>  
                <elements>  
                    <element>  
                        <name>Acceptor Legal Business Name</name>  
                        <code>81</code>  
                        <data>CRV* billing descriptor|</data>  
                    </element>  
                </elements>  
            </dataset>  
            <dataset>  
                <code>57</code>  
                <name>Business Application Identifier</name>  
                <elements>  
                    <element>  
                        <name>Business Application Identifier</name>  
                        <code>01</code>  
                        <data>AA</data>  
                    </element>  
                    <element>  
                        <name>Service Processing Type</name>  
                        <code>80</code>  
                        <data>0B</data>  
                    </element>  
                    <element>  
                        <name>Purpose of Payment</name>  
                        <code>82</code>  
                        <data>0</data>  
                    </element>  
                </elements>  
            </dataset>  
            <dataset>  
                <code>5F</code>  
                <name>Sender Data</name>  
                <elements>  
                    <element>  
                        <name>Sender Account Number</name>  
                        <code>02</code>  
                        <data>4658303943710702</data>  
                    </element>  
                    <element>  
                        <name>Sender Name</name>  
                        <code>03</code>  
                        <data>Francisco Fernandes</data>  
                    </element>  
                    <element>  
                        <name>Sender Address</name>  
                        <code>04</code>  
                        <data>7 Rua Poca Da Horta</data>  
                    </element>  
                    <element>  
                        <name>Sender City</name>  
                        <code>05</code>  
                        <data>Cheira</data>  
                    </element>  
                    <element>  
                        <name>Sender Country</name>  
                        <code>07</code>  
                        <data>620</data>  
                    </element>  
                    <element>  
                        <name>Recipient Name</name>  
                        <code>0A</code>  
                        <data>Fernandes Francisco</data>  
                    </element>  
                </elements>  
            </dataset>  
            <dataset>  
                <code>64</code>  
                <name>Visa Advanced Authorisation Data, VAA data</name>  
                <elements>  
                    <element>  
                        <name>Compromised Account Risk Condition Code (CARCC)</name>  
                        <code>01</code>  
                        <data>00 </data>  
                    </element>  
                    <element>  
                        <name>VAA Risk Score (001-099)</name>  
                        <code>02</code>  
                        <data>005</data>  
                    </element>  
                </elements>  
            </dataset>  
        </datasets>  
    </transaction>  
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
                        <data></data>  
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
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Business Format Code</name>  
                        <data>AI</data>  
                    </element>  
                    <element>  
                        <name>Passenger Name</name>  
                        <data>AN/YUGYEONG </data>  
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
                                <data></data>  
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
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data></data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Trip Leg 3 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data></data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Trip Leg 4 Information</name>  
                        <subElements>  
                            <subElement>  
                                <name>Carrier Code</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Service Class</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Stop-Over Code</name>  
                                <data></data>  
                            </subElement>  
                            <subElement>  
                                <name>Destination City/Airport Code</name>  
                                <data></data>  
                            </subElement>  
                        </subElements>  
                    </element>  
                    <element>  
                        <name>Travel Agency Code</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Travel Agency Name</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Restricted Ticket Indicator</name>  
                        <data>0</data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 1</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 2</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 3</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Fare Basis Code - Leg 4</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Computerized Reservation System</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 1</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 2</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 3</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Flight Number - Leg 4</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Credit Reason Indicator</name>  
                        <data></data>  
                    </element>  
                    <element>  
                        <name>Ticket Change Indicator</name>  
                        <data></data>  
                    </element>  
                </elements>  
            </dataset>  
        </datasets>  
    </transaction>  
</transactions>
```

## 2.3.2 Visa Example

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

## 2.3.3 Discover Example

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<transactions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <transaction>  
    <network>Discover</network>  
    <transactionType>Offline</transactionType>  
    <transactionId>6150631638</transactionId>  
    <transactionLinkId>59179686</transactionLinkId>  
    <datasets>  
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
      <dataset>  
        <code>XB</code>  
        <name>Airline Routing Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XB</data>  
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
            <data>2</data>  
          </element>  
          <element>  
            <name>Sequential part of the Ticket number</name>  
            <code>TICNO</code>  
            <data>1000333331</data>  
          </element>  
          <element>  
            <name>Ticket Check Digit</name>  
            <code>TICCD</code>  
            <data>4</data>  
          </element>  
          <element>  
            <name>Passenger Name</name>  
            <code>PASNG</code>  
            <data>HIDDINK/JOHN</data>  
          </element>  
          <element>  
            <name>First leg Carrier code</name>  
            <code>CARR1</code>  
            <data>BA</data>  
          </element>  
          <element>  
            <name>First leg Numeric Flight Number</name>  
            <code>FLNO1</code>  
            <data>7024</data>  
          </element>  
          <element>  
            <name>First leg Departure Airport Code</name>  
            <code>DAPC1</code>  
            <data>MLA</data>  
          </element>  
          <element>  
            <name>First leg Departure Date</name>  
            <code>DDTE1</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>First leg Departure Time</name>  
            <code>DTIM1</code>  
            <data>1220</data>  
          </element>  
          <element>  
            <name>First leg Arrival Airport Code</name>  
            <code>AAPC1</code>  
            <data>FRA</data>  
          </element>  
          <element>  
            <name>First leg Arrival date</name>  
            <code>ADTE1</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>First leg Arrival time</name>  
            <code>ATIM1</code>  
            <data>1430</data>  
          </element>  
          <element>  
            <name>First leg Fare Amount</name>  
            <code>FAMT1</code>  
            <data>105.50</data>  
          </element>  
          <element>  
            <name>First leg Fare Basis</name>  
            <code>BASI1</code>  
            <data>SL</data>  
          </element>  
          <element>  
            <name>First leg Class of Travel</name>  
            <code>CLAS1</code>  
            <data>S</data>  
          </element>  
          <element>  
            <name>First leg Stop over allowed</name>  
            <code>STOA1</code>  
            <data>N</data>  
          </element>  
          <element>  
            <name>Second leg Carrier code</name>  
            <code>CARR2</code>  
            <data>BA</data>  
          </element>  
          <element>  
            <name>Second leg Numeric Flight Number</name>  
            <code>FLNO2</code>  
            <data>7025</data>  
          </element>  
          <element>  
            <name>Second leg Departure Airport Code</name>  
            <code>DAPC2</code>  
            <data>FRA</data>  
          </element>  
          <element>  
            <name>Second leg Departure Date</name>  
            <code>DDTE2</code>  
            <data>110313</data>  
          </element>  
          <element>  
            <name>Second leg Departure Time</name>  
            <code>DTIM2</code>  
            <data>1930</data>  
          </element>  
          <element>  
            <name>Second leg Arrival Airport Code</name>  
            <code>AAPC2</code>  
            <data>MLA</data>  
          </element>  
          <element>  
            <name>Second leg Arrival date</name>  
            <code>ADTE2</code>  
            <data>110313</data>  
          </element>  
          <element>  
            <name>Second leg Arrival time</name>  
            <code>ATIM2</code>  
            <data>2045</data>  
          </element>  
          <element>  
            <name>Second leg Fare Amount</name>  
            <code>FAMT2</code>  
            <data />  
          </element>  
          <element>  
            <name>Second leg Fare Basis</name>  
            <code>BASI2</code>  
            <data>SL</data>  
          </element>  
          <element>  
            <name>Second leg Class of Travel</name>  
            <code>CLAS2</code>  
            <data>S</data>  
          </element>  
          <element>  
            <name>Second leg Stop over allowed</name>  
            <code>STOA2</code>  
            <data>N</data>  
          </element>  
          <element>  
            <name>Third leg Carrier code</name>  
            <code>CARR3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third leg Numeric Flight Number</name>  
            <code>FLNO3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Departure Airport Code</name>  
            <code>DAPC3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Departure Date</name>  
            <code>DDTE3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Departure Time</name>  
            <code>DTIM3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Arrival Airport Code</name>  
            <code>AAPC3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Arrival date</name>  
            <code>ADTE3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Arrival time</name>  
            <code>ATIM3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Fare Amount</name>  
            <code>FAMT3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third leg Fare Basis</name>  
            <code>BASI3</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Third leg Class of Travel</name>  
            <code>CLAS3</code>  
            <data>S</data>  
          </element>  
          <element>  
            <name>Third leg Stop over allowed</name>  
            <code>STOA3</code>  
            <data>Y</data>  
          </element>  
          <element>  
            <name>Fourth leg Carrier code</name>  
            <code>CARR4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Numeric Flight Number</name>  
            <code>FLNO4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Departure Airport Code</name>  
            <code>DAPC4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Departure Date</name>  
            <code>DDTE4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Departure Time</name>  
            <code>DTIM4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Arrival Airport Code</name>  
            <code>AAPC4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Arrival date</name>  
            <code>ADTE4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Arrival time</name>  
            <code>ATIM4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Fare Amount</name>  
            <code>FAMT4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth leg Fare Basis</name>  
            <code>BASI4</code>  
            <data>NULL</data>  
          </element>  
          <element>  
            <name>Fourth leg Class of Travel</name>  
            <code>CLAS4</code>  
            <data>NU</data>  
          </element>  
          <element>  
            <name>Fourth leg Stop over allowed</name>  
            <code>STOA4</code>  
            <data>NU</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XC</code>  
        <name>ATM Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XC</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>604</data>  
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
            <name>Diners Club/Acquirer Time</name>  
            <code>UTCTM</code>  
            <data>152308</data>  
          </element>  
          <element>  
            <name>Diners Club/Acquirer Date</name>  
            <code>UTCDT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Local Terminal Time</name>  
            <code>LCTIM</code>  
            <data>152347</data>  
          </element>  
          <element>  
            <name>Local Terminal Date</name>  
            <code>LCDAT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>ATM ID Number</name>  
            <code>ATMID</code>  
            <data>12228392</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XV</code>  
        <name>Car Rental Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XV</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>605</data>  
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
            <name>Rental Agreement Number</name>  
            <code>RENNO</code>  
            <data>AGM1234</data>  
          </element>  
          <element>  
            <name>Renter Name</name>  
            <code>RENNM</code>  
            <data>STEVEN.GREEN</data>  
          </element>  
          <element>  
            <name>Car Pickup City</name>  
            <code>RENCY</code>  
            <data>VALETTA</data>  
          </element>  
          <element>  
            <name>Car Pickup State or County or Province</name>  
            <code>RENST</code>  
            <data>VALLETTA</data>  
          </element>  
          <element>  
            <name>Car Pickup Country</name>  
            <code>RENCO</code>  
            <data>470</data>  
          </element>  
          <element>  
            <name>Car Pickup Date</name>  
            <code>RENDT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Car Pickup time</name>  
            <code>REMTM</code>  
            <data>1015</data>  
          </element>  
          <element>  
            <name>City of car return</name>  
            <code>RETCY</code>  
            <data>BUGIBBA</data>  
          </element>  
          <element>  
            <name>State, County or Province of Return</name>  
            <code>RETST</code>  
            <data>VALLETTA</data>  
          </element>  
          <element>  
            <name>Country of Return</name>  
            <code>RETCO</code>  
            <data>470</data>  
          </element>  
          <element>  
            <name>Date of Return</name>  
            <code>RETDT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Time of Return</name>  
            <code>RETTM</code>  
            <data>1600</data>  
          </element>  
          <element>  
            <name>Class of car</name>  
            <code>RCCAR</code>  
            <data>COMP</data>  
          </element>  
          <element>  
            <name>Weekly Rental Rate</name>  
            <code>RWRTE</code>  
            <data>180.00</data>  
          </element>  
          <element>  
            <name>Daily Rental Rate</name>  
            <code>RDRTE</code>  
            <data>30.00</data>  
          </element>  
          <element>  
            <name>Rate per mile/km</name>  
            <code>RMRTE</code>  
            <data>0.50</data>  
          </element>  
          <element>  
            <name>Total Rental distance</name>  
            <code>RDIST</code>  
            <data>300</data>  
          </element>  
          <element>  
            <name>Free mile/km</name>  
            <code>RFREM</code>  
            <data>50</data>  
          </element>  
          <element>  
            <name>Insurance Charges</name>  
            <code>RINSC</code>  
            <data>37.50</data>  
          </element>  
          <element>  
            <name>Fuel Charges</name>  
            <code>RFUEC</code>  
            <data>30.00</data>  
          </element>  
          <element>  
            <name>Miles or Kilometers</name>  
            <code>RMORK</code>  
            <data>M</data>  
          </element>  
          <element>  
            <name>One way drop charge</name>  
            <code>ROWDC</code>  
            <data>23.00</data>  
          </element>  
          <element>  
            <name>Auto towing charge</name>  
            <code>RAUTC</code>  
            <data />  
          </element>  
          <element>  
            <name>Regular mileage charge</name>  
            <code>RRMIC</code>  
            <data>0.00</data>  
          </element>  
          <element>  
            <name>Extra mileage charge</name>  
            <code>REMIC</code>  
            <data>125.00</data>  
          </element>  
          <element>  
            <name>Late return charge</name>  
            <code>RLRTC</code>  
            <data />  
          </element>  
          <element>  
            <name>Telephone charge</name>  
            <code>RTELC</code>  
            <data />  
          </element>  
          <element>  
            <name>Other charges</name>  
            <code>ROTHC</code>  
            <data>10.00</data>  
          </element>  
          <element>  
            <name>No show charges flag</name>  
            <code>RNOSH</code>  
            <data>1</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XM</code>  
        <name>Chip Card Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XM</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>XB</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>019</data>  
          </element>  
          <element>  
            <name>Receiving Institution Identification Code</name>  
            <code>DFTER</code>  
            <data>UJ</data>  
          </element>  
          <element>  
            <name>Batch Number</name>  
            <code>BATCH</code>  
            <data>001</data>  
          </element>  
          <element>  
            <name>Sequence Number within the batch</name>  
            <code>SEQNO</code>  
            <data>001</data>  
          </element>  
          <element>  
            <name>Sub-Sequence within the charge</name>  
            <code>SUSEQ</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Application PAN Sequence Number</name>  
            <code>CPANSQN</code>  
            <data>001</data>  
          </element>  
          <element>  
            <name>Application Identifier Terminal</name>  
            <code>CAIDT</code>  
            <data>A0000001523010</data>  
          </element>  
          <element>  
            <name>Application Interchange Profile (AIP)</name>  
            <code>CAIPFL</code>  
            <data>1800</data>  
          </element>  
          <element>  
            <name>Application Transaction Counter (ATC)</name>  
            <code>CATCTR</code>  
            <data>002D</data>  
          </element>  
          <element>  
            <name>Application Cryptogram (AC)</name>  
            <code>CACRG</code>  
            <data>AF664E90863FD2E3</data>  
          </element>  
          <element>  
            <name>Application Usage Control (AUC)</name>  
            <code>CAUCN</code>  
            <data>FF00</data>  
          </element>  
          <element>  
            <name>Amount Authorized</name>  
            <code>CAMTA</code>  
            <data>000000100100</data>  
          </element>  
          <element>  
            <name>Amount Other</name>  
            <code>CAMTO</code>  
            <data>000000000000</data>  
          </element>  
          <element>  
            <name>Cryptogram Information Data (CID)</name>  
            <code>CCRIF</code>  
            <data>80</data>  
          </element>  
          <element>  
            <name>Card Holder Verification Results (CVM) Results</name>  
            <code>CCVMR</code>  
            <data>5E0300</data>  
          </element>  
          <element>  
            <name>Dedicated File (DF) Name</name>  
            <code>CDEDF</code>  
            <data>A0000001523010</data>  
          </element>  
          <element>  
            <name>Interface Device (IFD) Serial Number</name>  
            <code>CIDSN</code>  
            <data>3D992920</data>  
          </element>  
          <element>  
            <name>Issuer Application Data</name>  
            <code>CADA1</code>  
            <data>0105A00013100000</data>  
          </element>  
          <element>  
            <name>Issuer Authentication Data (IAD)</name>  
            <code>CADAT</code>  
            <data />  
          </element>  
          <element>  
            <name>Issuer Script Results</name>  
            <code>CISRT</code>  
            <data />  
          </element>  
          <element>  
            <name>Terminal Country Code</name>  
            <code>CTRMG</code>  
            <data>156</data>  
          </element>  
          <element>  
            <name>Terminal Application Version Number</name>  
            <code>CTAVN</code>  
            <data>0001</data>  
          </element>  
          <element>  
            <name>Terminal Capabilities</name>  
            <code>CTRMC</code>  
            <data>E0B9C8</data>  
          </element>  
          <element>  
            <name>Terminal Type</name>  
            <code>CTRMT</code>  
            <data>22</data>  
          </element>  
          <element>  
            <name>Terminal Verification Results (TVR)</name>  
            <code>CTRMR</code>  
            <data>8000008000</data>  
          </element>  
          <element>  
            <name>Transaction Date</name>  
            <code>CTRND</code>  
            <data>170619</data>  
          </element>  
          <element>  
            <name>Transaction Type</name>  
            <code>CTRNT</code>  
            <data>00</data>  
          </element>  
          <element>  
            <name>Transaction Currency Code</name>  
            <code>CTRNC</code>  
            <data>156</data>  
          </element>  
          <element>  
            <name>Unpredictable Number (UN)</name>  
            <code>CUNPN</code>  
            <data>6EE3B683</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XG</code>  
        <name>Gasoline Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XG</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>606</data>  
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
            <name>Vehicle/License Plate Number</name>  
            <code>GVLPN</code>  
            <data>SJ52HGK</data>  
          </element>  
          <element>  
            <name>Vehicle ID</name>  
            <code>GVID</code>  
            <data>GSHEUDJHYG7483625536</data>  
          </element>  
          <element>  
            <name>Odometer Reading</name>  
            <code>GODOR</code>  
            <data>3400</data>  
          </element>  
          <element>  
            <name>Odometer Unit</name>  
            <code>GODUN</code>  
            <data>M</data>  
          </element>  
          <element>  
            <name>Driver ID Number, Driver license Number or other ID number</name>  
            <code>GDRID</code>  
            <data />  
          </element>  
          <element>  
            <name>Fuel Units Dispensed</name>  
            <code>GFUUP</code>  
            <data>45</data>  
          </element>  
          <element>  
            <name>Fuel Price per Unit</name>  
            <code>GFUPU</code>  
            <data>0.00</data>  
          </element>  
          <element>  
            <name>Fuel Unit</name>  
            <code>GFUUN</code>  
            <data>L</data>  
          </element>  
          <element>  
            <name>Fuel Product Type</name>  
            <code>GFUPD</code>  
            <data>DIESEL</data>  
          </element>  
          <element>  
            <name>Total Fuel Amount</name>  
            <code>GFUAM</code>  
            <data>36.00</data>  
          </element>  
          <element>  
            <name>Oil-Number of Units</name>  
            <code>GOIUP</code>  
            <data>5</data>  
          </element>  
          <element>  
            <name>Oil Units</name>  
            <code>GOIUN</code>  
            <data>L</data>  
          </element>  
          <element>  
            <name>Total Oil Purchase Amount</name>  
            <code>GOIAM</code>  
            <data>12.00</data>  
          </element>  
          <element>  
            <name>Merchandise Product Type</name>  
            <code>GMEPT</code>  
            <data>RXV425</data>  
          </element>  
          <element>  
            <name>Other Merchandise Charges</name>  
            <code>GMEAM</code>  
            <data>3.00</data>  
          </element>  
          <element>  
            <name>Contract Number</name>  
            <code>GCONO</code>  
            <data />  
          </element>  
          <element>  
            <name>Fleet Transaction</name>  
            <code>GFLEE</code>  
            <data>Y</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XH</code>  
        <name>Hotel Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XH</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>612</data>  
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
            <data>5</data>  
          </element>  
          <element>  
            <name>Date of Check-in</name>  
            <code>HCIDT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Date of Check-out</name>  
            <code>HCODT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Number in party</name>  
            <code>HNOPT</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Guest Name</name>  
            <code>HNAME</code>  
            <data>WILKINS/JOHN</data>  
          </element>  
          <element>  
            <name>Room type</name>  
            <code>HRMTY</code>  
            <data>STD</data>  
          </element>  
          <element>  
            <name>Program Code</name>  
            <code>HPROG</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Folio Reference Number</name>  
            <code>HFOLI</code>  
            <data>FL012567</data>  
          </element>  
          <element>  
            <name>Confirmed Reservation Indicator</name>  
            <code>HCRES</code>  
            <data>Y</data>  
          </element>  
          <element>  
            <name>Daily Room Rate</name>  
            <code>HRMRT</code>  
            <data>100.00</data>  
          </element>  
          <element>  
            <name>Room Tax</name>  
            <code>HRMTX</code>  
            <data>17.50</data>  
          </element>  
          <element>  
            <name>Non-Room Tax</name>  
            <code>HNRTX</code>  
            <data />  
          </element>  
          <element>  
            <name>Phone charges</name>  
            <code>HPHAM</code>  
            <data>10.00</data>  
          </element>  
          <element>  
            <name>Room service charges</name>  
            <code>HRSAM</code>  
            <data>20.00</data>  
          </element>  
          <element>  
            <name>Mini bar charges</name>  
            <code>HMBAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Bar charges</name>  
            <code>HRBAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Gift shop charges</name>  
            <code>HGSAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Laundry/dry cleaning charges</name>  
            <code>HLAAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Prepaid expenses</name>  
            <code>HPPAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Restaurant charges</name>  
            <code>HREAM</code>  
            <data>56.50</data>  
          </element>  
          <element>  
            <name>Cash advances</name>  
            <code>HCAAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Parking/Valet/Transportation charges</name>  
            <code>HPKAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Health club charges</name>  
            <code>HHCAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Business Center charges</name>  
            <code>HBCAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Movie charges</name>  
            <code>HMVAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Other service charges</name>  
            <code>HOTAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Gratuities</name>  
            <code>HTIPS</code>  
            <data>20.00</data>  
          </element>  
          <element>  
            <name>Conference Charges</name>  
            <code>HCONF</code>  
            <data />  
          </element>  
          <element>  
            <name>Audio Visual Charges</name>  
            <code>HAUDI</code>  
            <data />  
          </element>  
          <element>  
            <name>Banquet Charges</name>  
            <code>HBANQ</code>  
            <data />  
          </element>  
          <element>  
            <name>Internet Charges</name>  
            <code>HINTE</code>  
            <data />  
          </element>  
          <element>  
            <name>Early Arrival or Departure Charges</name>  
            <code>HDEPA</code>  
            <data />  
          </element>  
          <element>  
            <name>Billing Adjustment</name>  
            <code>HBAIN</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Billing Adjustment amount</name>  
            <code>HBAAM</code>  
            <data>12.00</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XR</code>  
        <name>Rail Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XR</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>608</data>  
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
            <name>Railway that issued the ticket</name>  
            <code>RISTK</code>  
            <data>234</data>  
          </element>  
          <element>  
            <name>Ticket Number</name>  
            <code>TICNO</code>  
            <data>1020089</data>  
          </element>  
          <element>  
            <name>Ticket Check Digit</name>  
            <code>TICCD</code>  
            <data>7</data>  
          </element>  
          <element>  
            <name>Agent Code</name>  
            <code>RAGCD</code>  
            <data>606548</data>  
          </element>  
          <element>  
            <name>Agent Name</name>  
            <code>RAGNM</code>  
            <data>TRAIN CO AGENT</data>  
          </element>  
          <element>  
            <name>Agent Address Line 1</name>  
            <code>AGAD1</code>  
            <data>MAIN.STREET</data>  
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
            <data>VL147PT</data>  
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
            <data>1252</data>  
          </element>  
          <element>  
            <name>Agent Telephone Number</name>  
            <code>PNONO</code>  
            <data>7763421</data>  
          </element>  
          <element>  
            <name>Computerized Reservation System Code</name>  
            <code>RRESY</code>  
            <data />  
          </element>  
          <element>  
            <name>Passenger Name</name>  
            <code>PASNG</code>  
            <data>IVANOVIC BOB MR</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XL</code>  
        <name>Rail Routing Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XL</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>608</data>  
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
            <data>2</data>  
          </element>  
          <element>  
            <name>First Leg Carrier Code</name>  
            <code>RCACD1</code>  
            <data>NSE</data>  
          </element>  
          <element>  
            <name>First Leg Journey Number</name>  
            <code>RJNNO1</code>  
            <data>810</data>  
          </element>  
          <element>  
            <name>First Leg Departure City/Station Code</name>  
            <code>RDECY1</code>  
            <data>FRB</data>  
          </element>  
          <element>  
            <name>First Leg Departure Date</name>  
            <code>RDEDT1</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>First Leg Departure Time</name>  
            <code>RDETM1</code>  
            <data>810</data>  
          </element>  
          <element>  
            <name>First Leg Arrival City/Station Code</name>  
            <code>RARCY1</code>  
            <data>YRK</data>  
          </element>  
          <element>  
            <name>First Leg Arrival Date</name>  
            <code>RARDT1</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>First Leg Arrival Time</name>  
            <code>RARTM1</code>  
            <data>1135</data>  
          </element>  
          <element>  
            <name>First Leg Fare Amount</name>  
            <code>RFAAM1</code>  
            <data>20.00</data>  
          </element>  
          <element>  
            <name>First Leg Fare Basis</name>  
            <code>RBASI1</code>  
            <data />  
          </element>  
          <element>  
            <name>First Leg Class of Travel</name>  
            <code>RCLAS1</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Second Leg Carrier Code</name>  
            <code>RCACD2</code>  
            <data>NSE</data>  
          </element>  
          <element>  
            <name>Second Leg Journey Number</name>  
            <code>RJNNO2</code>  
            <data>1810</data>  
          </element>  
          <element>  
            <name>Second Leg Departure City/Station Code</name>  
            <code>RDECY2</code>  
            <data>YRK</data>  
          </element>  
          <element>  
            <name>Second Leg Departure Date</name>  
            <code>RDEDT2</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Second Leg Departure Time</name>  
            <code>RDETM2</code>  
            <data>1810</data>  
          </element>  
          <element>  
            <name>Second Leg Arrival City/Station Code</name>  
            <code>RARCY2</code>  
            <data>FRB</data>  
          </element>  
          <element>  
            <name>Second Leg Arrival Date</name>  
            <code>RARDT2</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Second Leg Arrival Time</name>  
            <code>RARTM2</code>  
            <data>2245</data>  
          </element>  
          <element>  
            <name>Second Leg Fare Amount</name>  
            <code>RFAAM2</code>  
            <data>20.00</data>  
          </element>  
          <element>  
            <name>Second Leg Fare Basis</name>  
            <code>RBASI2</code>  
            <data />  
          </element>  
          <element>  
            <name>Second Leg Class of Travel</name>  
            <code>RCLAS2</code>  
            <data>1</data>  
          </element>  
          <element>  
            <name>Third Leg Carrier Code</name>  
            <code>RCACD3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Journey Number</name>  
            <code>RJNNO3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Departure City/Station Code</name>  
            <code>RDECY3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Departure Date</name>  
            <code>RDEDT3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Departure Time</name>  
            <code>RDETM3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Arrival City/Station Code</name>  
            <code>RARCY3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Arrival Date</name>  
            <code>RARDT3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Arrival Time</name>  
            <code>RARTM3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Fare Amount</name>  
            <code>RFAAM3</code>  
            <data>0.00</data>  
          </element>  
          <element>  
            <name>Third Leg Fare Basis</name>  
            <code>RBASI3</code>  
            <data />  
          </element>  
          <element>  
            <name>Third Leg Class of Travel</name>  
            <code>RCLAS3</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Carrier Code</name>  
            <code>RCACD4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Journey Number</name>  
            <code>RJNNO4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Departure City/Station Code</name>  
            <code>RDECY4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Departure Date</name>  
            <code>RDEDT4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Departure Time</name>  
            <code>RDETM4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Arrival City/Station Code</name>  
            <code>RARCY4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Arrival Date</name>  
            <code>RARDT4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Arrival Time</name>  
            <code>RARTM4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Fare Amount</name>  
            <code>RFAAM4</code>  
            <data>0.00</data>  
          </element>  
          <element>  
            <name>Fourth Leg Fare Basis</name>  
            <code>RBASI4</code>  
            <data />  
          </element>  
          <element>  
            <name>Fourth Leg Class of Travel</name>  
            <code>RCLAS4</code>  
            <data />  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XE</code>  
        <name>Restaurant Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XE</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>610</data>  
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
            <name>Restaurant Food Amount</name>  
            <code>RFDAM</code>  
            <data>123.00</data>  
          </element>  
          <element>  
            <name>Restaurant Beverage Amount</name>  
            <code>RBVAM</code>  
            <data>75.00</data>  
          </element>  
          <element>  
            <name>Restaurant Other Amount</name>  
            <code>ROTAM</code>  
            <data />  
          </element>  
          <element>  
            <name>Restaurant Tip Amount</name>  
            <code>RTPAM</code>  
            <data>38.00</data>  
          </element>  
        </elements>  
      </dataset>  
      <dataset>  
        <code>XT</code>  
        <name>Telephone Additional Detail Record</name>  
        <elements>  
          <element>  
            <name>Transaction Code</name>  
            <code>TRANS</code>  
            <data>RFRC</data>  
          </element>  
          <element>  
            <name>Function Code</name>  
            <code>FUNCD</code>  
            <data>XT</data>  
          </element>  
          <element>  
            <name>Sending Institution Identification Code</name>  
            <code>SFTER</code>  
            <data>YT</data>  
          </element>  
          <element>  
            <name>Recap Number</name>  
            <code>RCPNO</code>  
            <data>611</data>  
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
            <name>Date Of Call</name>  
            <code>TCLDT</code>  
            <data>250402</data>  
          </element>  
          <element>  
            <name>Time Of Call</name>  
            <code>TCLTM</code>  
            <data>1645</data>  
          </element>  
          <element>  
            <name>Call Duration</name>  
            <code>TCLDU</code>  
            <data>12001</data>  
          </element>  
          <element>  
            <name>From Phone Number</name>  
            <code>TFRNO</code>  
            <data>4401252675494</data>  
          </element>  
          <element>  
            <name>From Location-City</name>  
            <code>TFRCY</code>  
            <data>ST JULIANS</data>  
          </element>  
          <element>  
            <name>From Location-Country</name>  
            <code>TFRCO</code>  
            <data>470</data>  
          </element>  
          <element>  
            <name>To Phone Number</name>  
            <code>TTONO</code>  
            <data>44018348765284</data>  
          </element>  
          <element>  
            <name>To Location-City</name>  
            <code>TTOCY</code>  
            <data>BUGIBBA</data>  
          </element>  
          <element>  
            <name>To Location-Country</name>  
            <code>TTOCO</code>  
            <data>470</data>  
          </element>  
          <element>  
            <name>Original Charge Amount</name>  
            <code>TCLAM</code>  
            <data>15.45</data>  
          </element>  
          <element>  
            <name>Discount Amount</name>  
            <code>TDIAM</code>  
            <data>12.37</data>  
          </element>  
        </elements>  
      </dataset>  
    </datasets>  
  </transaction>  
</transactions>
```