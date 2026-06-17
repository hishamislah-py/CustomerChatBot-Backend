# 4.41 POS\_Data\_DE22 in Mastercard Financial Messages

The `POS_Data_DE22` field applies to Mastercard Financial Clearing messages only (i.e., MTID=1240, MTID=1442). For Visa, use `GPS_POS_Data`. (See also [Get Transaction Message fields: POS\_Data\_DE22](../Requirements/GetTransaction_Message.htm#POS_Data_DE22) and [GPS\_POS\_Data](../Requirements/GetTransaction_Message.htm#GPS_POS_Data))

The POS Data codes (`POS_Data_DE22`) field is made up of various subfields. Its format is based on ISO8583:1993 DE 22 specification, and consists of both:

* Terminal capabilities (what the terminal can do)
* Terminal methods (what the terminal did do, or what actually happened)

| Positions | Length | Field Name | Description / Valid Values |
| --- | --- | --- | --- |
| 1 | 1 | Card Data Input Capability | 0 = Unknown  1 = Manual, no terminal; server  2 = Magnetic stripe reader (MSR)  3 = Barcode  4 = OCR  5 = ICC  6 = PAN Key entry (PKE) only  A = Contactless MSR (possibility also optionally including ICC, MSR or PKE)  B = MSR + PKE  C = MSR, ICC, PKE  D = MSR + ICC  E = ICC + PKE  M = Contactless ICC + Contactless MSR (possibly also optionally including ICC, MSR or PKE)  V = Other |
| 2 | 1 | Cardholder Authentication Capability | 0 = No electronic authentication capability  1 = PIN  2 = Electronic signature analysis capability  3 = Biometrics  4 = Biographic  5 = Electronic authentication capability is inoperative  9 = Unknown |
| 3 | 1 | Card Capture Capability | 0 = No capture capability  1 = Card Capture capability  9 = Unknown |
| 4 | 1 | Terminal Operating Environment | 0 = No Terminal used  1 = On card acceptor premises, attended  2 = On card acceptor premises, unattended  3 = Off card acceptor premises, attended  4 = Off card acceptor premises, unattended  5 = On cardholder premises, unattended  6 = Off cardholder premises, unattended  9 = Unknown |
| 5 | 1 | Cardholder present data | 0 = Cardholder present  1 = Cardholder not present (unspecified)  2 = Cardholder not present (mail order)  3 = Cardholder not present (telephone order)  4 = Cardholder not present (standing order or recurring transaction)  5 = Cardholder not present (e-commerce) |
| 6 | 1 | Card Present Data | 0 = Card not present  1 = Card Present |
| 7 | 1 | Card Data Input Method | 0 = Unknown or no terminal  1 = Manual Input (no terminal used)  2 = Partial Magnetic Stripe Read  3 = Barcode  4 = OCR  5 = Contact EMV ICC  6 = PAN Key Entry  A = Contactless Magnetic Stripe  B = Magnetic Stripe Read  C = Contact EMV ICC, Online Transaction  F = Contact EMV ICC, Offline Transaction  M = Contactless EMV ICC  N = Contactless EMV ICC or Contactless Magnetic Stripe (PAN mapping service applied by Network)  O = e-commerce with EMV ICC.  Mastercard Digital Enablement Service Applied.  R = e-commerce with EMV ICC  S = e-commerce  T = Pan auto-entry via server (issuer, acquirer or third party vendor system)  V = e-commerce or PAN auto-entry by server. Card on File service applied by Network. |
| 8 | 1 | Cardholder authentication Method | 0 = Not authenticated  1 = PIN  2 = Electronic Signature Analysis  3 = Biometrics  4 = Biographic  5 = Manual signature verification  6 = Other Manual verification (e.g. drivers licence)  9 = Unknown  S = Other systematic verification (including biometrics + biographic) |
| 9 | 1 | Cardholder authentication entity | Identifies who verified the cardholder (using the method described in the *Cardholder authentication method* field above).  0 = Not authenticated  1 = ICC  2 = Terminal  3 = Authorising Agent  4 = Merchant  5 = Other  9 = Unknown |
| 10 | 1 | Card Data Output Capability | This is rarely used.  10 = Unknown  1 = None  2 = Magnetic Stripe writer  3 = ICC  S = Other |
| 11 | 1 | Terminal Data Output Capability | This is rarely used.  0 = Unknown  1 = None  2 = Printing only  3 = Display only  4 = Printing and Display |
| 12 | 1 | PIN Capture Capability | 0 = No PIN capture capability  1 = Unknown  4 = PIN capture up to 4 digits max  5 = PIN capture up to 5 digits max  6 = PIN capture up to 6 digits max  7 = PIN capture up to 7 digits max  8 = PIN capture up to 8 digits max  9 = PIN capture up to 9 digits max  A = PIN capture up to 10 digits max  B = PIN capture up to 11 digits max  C = PIN capture up to 12 digits max |