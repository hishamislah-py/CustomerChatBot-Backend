# Industry-Specific Codes for Discover

The following are industry-specific codes for Discover. These are used within ADRs. For more details on the generic codes and examples for Discover, see [Core Message](Scheme_Elements-New.htm#Core) fields in Scheme Elements.

## XA: Airline Additional Record

| Code | Description |
| --- | --- |
| AIRCD | Ticketâissuing airline Code |
| AIRRF | Booking Reference Number |
| AGAFE | Agent Fees |
| AGARF | Agent Fee Reference |
| AGADS | Agent Fee Description |
| IATCD | IATA Agent code (includes check digit) |
| IATNM | IATA Agent Trading name |
| AGAD1 | Agent Address Line 1 |
| AGAD2 | Agent Address Line 2 |
| AGAD3 | Agent Address Line 3 |
| AGCTY | Agent City |
| AGSTA | Agent State/County |
| AGZIP | Agent Zip Code |
| AGGCD | Agent Geographic Code |
| PNODC | Agent International dialling code |
| PNOAC | Agent Area Code |
| PNONO | Agent Telephone Number |
| RESSY | Computerized Reservation System Code (e.g., AB = Abacus, AM = Amadeus,  A = Apollo, etc.) |

## XB: Airline Routing Detail Record

| Code | Description |
| --- | --- |
| TICNO | Sequential part of the Ticket number |
| TICCD | Ticket Check Digit |
| PASNG | Passenger Name |
| CARR1 | First leg Carrier code (first part of flight number) |
| FLNO1 | First leg Numeric Flight Number |
| DAPC1 | First leg Departure Airport Code |
| DDTE1 | First leg Departure Date (YYMMDD,OPEN or VOID) |
| DTIM1 | First leg Departure Time (HHMM) blank if DDTE1 is either OPEN or VOID |
| AAPC1 | First leg Arrival Airport Code |
| ADTE1 | First leg Arrival date (YYMMDD, OPEN or VOID) |
| ATIM1 | First leg Arrival time (HHMM) blank if ADTE1 is either OPEN or VOID |
| FAM1 | First leg Fare Amount |
| BASI1 | First leg Fare Basis |
| CLAS1 | First leg Class of Travel |
| STOA1 | First leg Stop over allowed (Y=Yes, N=No) |
| XXXX2 | Second legâall fields as per first leg |
| XXXX3 | Third legâall fields as per first leg |
| XXXX4 | Fourth legâall fields as per first leg |

## XC: ATM Additional Detail Record

| Code | Description |
| --- | --- |
| UTCTM | Diners Club/Acquirer Time (HHMMSS)\*\* |
| UTCDT | Diners Club/Acquirer Date (YYMMDD)\*\* |
| LCTIM | Local Terminal Time (HHMMSS) |
| LCDAT | Local Terminal Date (YYMMDD) |
| ATMID | ATM ID Number |

## XV: Car Rental Additional Detail

| Code | Description |
| --- | --- |
| RENMO | Rental Agreement Number |
| RENNM | Renter Name |
| RENCY | Car Pickup City |
| RENST | Car Pickup State or County or Province |
| RENCO | Car Pickup Country |
| RENDT | Car Pickup Date (YYMMDD) |
| REMTM | Car Pickup time (HHMM) |
| RETCY | City of car return |
| RETST | State, County or Province of Return |
| RETCO | Country of Return |
| RETDT | Date of Return (YYMMDD) |
| RETTM | Time of Return (HHMM) |
| RCCAR | Class of car |
| RWRTE | Weekly Rental Rate |
| RDRTE | Daily Rental Rate |
| RMRTE | Rate per mile/km |
| RDIST | Total Rental distance (i.e., miles driven) |
| RFREM | Free mile/km |
| RINSC | Insurance Charges |
| RFUEC | Fuel Charges |
| RMORK | Miles or Kilometers (K or M) |
| ROWDC | One way drop charge |
| RAUTC | Auto towing charge |
| RRMIC | Regular mileage charge |
| REMIC | Extra mileage charge |
| RLRTC | Late return charge |
| RTELC | Telephone charge |
| ROTHC | Other charges |
| RNOSH | No show charges flag (0: Not applicable; 1: No show) |

## XG: Gasoline Additional Detail

| Code | Description |
| --- | --- |
| GVLPN | Vehicle/License Plate Number |
| GVID | Vehicle ID |
| GODOR | Odometer Reading |
| GODUN | Odometer Unit (MâMiles, KâKilometers) |
| GDRID | Driver ID Number, Driver license Number or other ID number |
| GFUUP | Fuel Units Dispensed |
| GFUPU | Fuel Price per Unit |
| GFUUN | Fuel Unit (GâGallons, LâLiters) |
| GFUPD | Fuel Product Type |
| GFUAM | Total Fuel Amount |
| GOIUP | OilâNumber of Units |
| GOIUN | Oil Units (PâPints, GâGallons, LâLiters) |
| GOIAM | Total Oil Purchase Amount |
| GMEPT | Merchandise Product Type |
| GMEAM | Other Merchandise Charges |
| GCONO | Contract Number |
| GFLEE | Fleet Transaction (YâYes, NâNo) |

## XH: Hotel Additional Detail Record

| Code | Description |
| --- | --- |
| HCIDT | Date of Checkâin (YYMMDD) |
| HCODT | Date of Checkâout (YYMMDD) |
| HNOPT | Number in party |
| HNAME | Guest Name |
| HRMTY | Room type |
| HPROG | Program Code |
| HFOLI | Folio Reference Number |
| HCRES | Confirmed Reservation Indicator (âYââConfirmed, âNâânot confirmed) |
| HRMRT | Daily Room Rate |
| HRMTX | Room Tax |
| HNRTX | Non-Room Tax |
| HPHAM | Phone charges |
| HRSAM | Room service charges |
| HMBAM | Mini bar charges |
| HRBAM | Bar charges |
| HGSAM | Gift shop charges |
| HLAAM | Laundry/dry cleaning charges |
| HPPAM | Prepaid expenses |
| HREAM | Restaurant charges |
| HCAAM | Cash advances |
| HPKAM | Parking/Valet/Transportation charges |
| HHCAM | Health club charges |
| HBCAM | Business Centre charges |
| HMVAM | Movie charges |
| HOTAM | Other service charges |
| HTIPS | Gratuities |
| HCONF | Conference Charges |
| HAUDI | Audio Visual Charges |
| HBANQ | Banquet Charges |
| HINTE | Internet Charges |
| HDEPA | Early Arrival or Departure Charges |
| HBAIN | Billing Adjustment (0âNo additional charges; 1âAdditional charges added) |
| HBAAM | Billing Adjustment amount |

## XR: Rail Additional Detail

| Code | Description |
| --- | --- |
| RISTK | Railway that issued the ticket |
| TICNO | Ticket Number |
| TICCD | Ticket Check Digit |
| RAGCD | Agent Code |
| RAGNM | Agent Name |
| AGAD1 | Agent Address line 1 |
| AGAD2 | Agent Addressâline 2 |
| AGAD3 | Agent Addressâline 3 |
| AGCTY | Agent City |
| AGSTA | Agent State/County |
| AGZIP | Agent Zip Code |
| AGGCD | Agent Geographic Code |
| PNODC | Agent International Dialling Code |
| PNOAC | Agent Area Code |
| PNONO | Agent Telephone Number |
| RRESY | Computerized Reservation System Code |
| PASNG | Passenger Name |

## XL: Rail Routing Detail Record

| Code | Description |
| --- | --- |
| RCACD1 | First Leg Carrier Code |
| RJNNO1 | First Leg Journey Number (numeric) |
| RDECY1 | First Leg Departure City/Station Code |
| RDEDT1 | First Leg Departure Date (YYMMDD) |
| RDETM1 | First Leg Departure Time (HHMM) |
| RARCY1 | First Leg Arrival City/Station Code |
| RARDT1 | First Leg Arrival Date (YYMMDD) |
| RARTM1 | First Leg Arrival Time (HHMM) |
| RFAAM1 | First Leg Fare Amount |
| RBASI1 | First Leg Fare Basis |
| RCLAS1 | First Leg Class of Travel |
| XXXXX2 | 2nd Legâall fields as per first leg |
| XXXXX3 | 3rd Legâall fields as per first leg |
| XXXXX4 | 4th Legâall fields as per first leg |

## XE: Restaurant Additional Detail

| Code | Description |
| --- | --- |
| RFDAM | Restaurant Food Amount |
| RBVAM | Restaurant Beverage Amount |
| ROTAM | Restaurant Other Amount |
| RTPAM | Restaurant Tip Amount |

## XT: Telephone Additional Detail

| Code | Description |
| --- | --- |
| TCLDT | Date Of Call (YYMMDD) |
| TCLTM | Time Of Call (HHMM) |
| TCLDU | Call Duration (MMMSS) |
| TFRNO | From Phone Number |
| TFRCY | From LocationâCity |
| TFRCO | From LocationâCountry |
| TTONO | To Phone Number |
| TTOCY | To LocationâCity |
| TTOCO | To LocationâCountry |
| TCLAM | Original Charge Amount |
| TDIAM | Discount Amount |

## XM: Chip Card Additonal Detail

| Code | Description |
| --- | --- |
| CPANSQN | Application PAN Sequence Number |
| CAIDT | Application Identifier Terminal |
| CAIPFL | Application Interchange Profile (AIP) |
| CATCTR | Application Transaction Counter (ATC) |
| CACRG | Application Cryptogram (AC) |
| CAUCN | Application Usage Control (AUC) |
| CAMTA | Amount Authorized (Fixed Numeric with no decimal places). Front  padded with zeros (0) Last two digits imply minor units of currency. |
| CAMTO | Amount Other (Fixed Numeric with no decimal places). Front padded  with zeros (0) Last two digits imply minor units of currency. |
| CCRIF | Cryptogram Information Data (CID) |
| CCVMR | Cardholder Verification Results (CVM) Results |
| CDEDF | Dedicated File (DF) Name |
| CIDSN | Interface Device (IFD)Serial Number |
| CADA1 | Issuer Application Data |
| CADAT | Issuer Authentication Data (IAD) |
| CISRT | Issuer Script Results |
| CTRMG | Terminal Country Code |
| CTAVN | Terminal Application Version Number |
| CTRMC | Terminal Capabilities |
| CTRMT | Terminal Type |
| CTRMR | Terminal Verification Results |
| CTRND | Transaction Date |
| CTRNT | Transaction Type |
| CTRNC | Transaction Currency Code |
| CUNPN | Unpredictable Number |