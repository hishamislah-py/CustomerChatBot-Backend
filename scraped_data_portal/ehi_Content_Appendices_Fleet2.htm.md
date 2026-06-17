# 4.11 Fleet 2.0 Data Fields

The following table lists the Fleet Data available for the `FleetData` field.

| Field | EHI Tag | Atttribute | Description |
| --- | --- | --- | --- |
| Type of Purchase | FL01 | AN(1,1) | The type of purchase:   * 1 = Fuel purchase (single fuel code) * 2 = Non-fuel purchase * 3 = Fuel and non-fuel purchase * 4 = Fuel purchase (multiple fuel codes) |
| Service Type | FL02 | AN(1,1) | The service type.   * F = Full service * S = Self-service * H = High-speed dispense |
| Fuel Type | FL03 | AN(2,2) | The fuel type of the purchase.   * 01 = Regular * 02 = Mid\Plus * 03 = Premium\Super   Refer to VISA Fleet 2.0 Implementation Guide Appendix H for the list of types. |
| Expanded Fuel Type | FL04 | AN(4,4) | The same values are used as in Fuel Type, but with spaces padded to the right |
| Unit of Measure | FL05 | AN(1,1) | The measurement unit.   * C = CM (charging minutes) * G = U.S. gallon * I = Imperial gallon * K = Kilo * L = Liter * P = Pound * W = kWh (kilowatt per hour) |
| Quantity | FL06 | N(12,12) | Quantity of the fuel. Four decimal places applied. For example, 000000123987 in the quantity field means 12.3897 unit. |
| Unit Cost | FL07 | N(12,12) | Unit cost in transaction currency. Four decimal places implied. |
| Gross Fuel Price | FL08 | N(12,12) | Gross fuel price in transaction currency. Four decimal places implied. |
| Net Fuel Price | FL09 | N(12,12) | Net fuel price in transaction currency. Four decimal places implied. |
| Gross non-Fuel Price | FL10 | N(12,12) | Gross non-fuel price in transaction currency. Four decimal places implied. |
| Net non-Fuel Price | FL11 | N(12,12) | Net non-fuel price in transaction currency. Four decimal places implied. |
| Local Tax Included | FL12 | AN(1,1) | Whether local tax is included.   * 0 = Tax not included * 1 = State or provincial tax included * 2 = Transaction is not subject to tax |
| Local Tax | FL13 | N(12,12) | Local Tax Amount. Two decimal places implied. |
| National Tax Included | FL14 | AN(1,1) | Whether national tax is included.   * 0 = Not subject to tax * 1 = Subject to tax |
| National Tax | FL15 | N(12,12) | National Tax. Two decimal places implied. |
| Other Tax | FL16 | N(12,12) | Any other tax amount. Two decimal places implied. |
| VAT Tax Rate | FL17 | N(4,4) | Value-added tax or local tax rate (in percentage) for fuel purchased. Two decimal places are implied. |
| Odometer Reading | FL18 | AN(7,7) | Vehicleâs odometer reading at time of transaction. |
| Non-Fuel Product Code 1 | FL19 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 2 | FL20 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 3 | FL21 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 4 | FL22 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 5 | FL23 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 6 | FL24 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 7 | FL25 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Non-Fuel Product Code 8 | FL26 | AN(2,2) | Applicable non-fuel product that is part of the purchase. |
| Visa Fleet Service ID | FL27 | ANS(1,20) | Vehicle ID, Driver ID or Generic ID used in the transaction. |
| Fleet Work Order Number | FL28 | AN(1,30) | Prompted Fleet Work Order Number or Prompted Invoice Number. |
| Fleet Employee Number | FL29 | AN(1,12) | VISA Fleet Cardholder Employee Number. |
| Fleet Trailer Number | FL30 | AN(1,16) | Contains the trailer number for the Visa Fleet cardholder or vehicle-assigned card. |
| Fleet Additional Prompt Data 1 | FL31 | AN(1,20) | Contains information that the cardholder is prompted to provide at the POS for issuer and fleet employer purposes. |
| Fleet Additional Prompt Data 2 | FL32 | AN(1,20) | Contains information that the cardholder is prompted to provide at the POS for issuer and fleet employer purposes. |
| Purchase Restrictions Flag | FL33 | AN(1,1) | This tag allows merchants to indicate via a flag in the incoming authorisation request the controls they can support at the POS. |
| Host Based Purchase Restrictions | FL34 | AN(1,16) | This tag allows an issuer to dynamically control the purchase and only allow the restriction they are passing back in the authorisation response message  This field is normally a part of the response message. It is added into the spec for future usage. |
| Charging Power Output Capacity | FL35 | N(1,6) | Contains the charging station power output capacity in kW. |
| Charging Reason Code | FL36 | N(1,6) | Contains a specific charging reason code for the transaction. Refer to the Visa Fleet Card 2.0 Implementation Guide for a list of valid codes. |
| Maximum Power Dispensed | FL37 | N(1,6) | Contains maximum power dispensed during specific charge session from the charging station. This can be different from the power output capacity of the station based on power management by the site operator. |
| Connector Type | FL38 | AN(3,3) | Contains a Visa defined code for a specific connector type to identify the connection for the charge session. Refer to the Visa Fleet Card 2.0 Implementation Guide for a list of valid codes. |
| Total Time Plugged In | FL39 | N(1,6) | Contains the total time the vehicle was plugged in. Format is hhmmss, where:   * hh = Hours (00â23) * mm = Minutes(00â59) * ss = Seconds (00â59) |
| Total Charging Time | FL40 | N(1,6) | Contains the actual time taken to charge the vehicle. Format is hhmmss, where:   * hh = Hours (00â23) * mm = Minutes(00â59) * ss = Seconds (00â59) |
| Start Time of Charge | FL41 | N(1,6) | Contains the start time of the charge (expressed in local time of the card acceptor location). Format is hhmmss, where:   * hh = Hours (00â23) * mm = Minutes(00â59) * ss = Seconds (00â59) |
| Finish Time of Charge | FL42 | N(1,6) | Contains the finishing time of the charge (expressed in local time of the card acceptor location). Format is hhmmss, where:   * hh = Hours (00â23) * mm = Minutes(00â59) * ss = Seconds (00â59) |
| Estimated KM\Miles Added | FL43 | N(1,6) | Contains an estimate of the total distance added, in km/miles, based on the kWh added, and the type of vehicle engine charged. |
| Carbon Footprint | FL44 | N(1,12) | Contains carbon footprint avoidance (how much was saved from this charge) measurement for the purchase on the transaction - measured in grams of carbon dioxide equivalent (CO2e). |
| Estimated KM\Miles Available | FL45 | N(1,6) | Contains estimated mileage that the car has, after completion of charge, when the electric vehicle leaves the charging station. |