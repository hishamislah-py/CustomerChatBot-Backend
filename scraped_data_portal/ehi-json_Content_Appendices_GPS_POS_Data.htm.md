# 4.13 GPS\_POS\_Data field

This is a Thredd field that records POS Data codes, which are specific to this transaction. Each position records a different piece of information.  Positions 33 onwards are reserved for future use.

All subfields are concatenated together in order. Subfields begin at 1. You may only receive the leading subfields (i.e. 1 or more.)

## 4.13.1 GPS\_POS\_Data Positions

| Position | Name | Format | Values defined in section |
| --- | --- | --- | --- |
| 1 | Cardholder Present | AN(1,1) | [Cardholder Present Indicator](#Cardhold) |
| 2 | Card Present | AN(1,1) | [Card Present Indicator](#_Ref498356634) |
| 3 | Card Data Input Method | AN(1,1) | [Card Data Input Method](#_Ref498356645) |
| 4 | Cardholder authentication method 1 | AN(1,1) | [Cardholder authentication Method](#_Ref498356652) |
| 5 | Cardholder authentication method 2 | AN(1,1) | [Cardholder authentication Method](#_Ref498356652) |
| 6 | Cardholder authentication method 3 | AN(1,1) | [Cardholder authentication Method](#_Ref498356652) |
| 7 | Cardholder authentication method 4 | AN(1,1) | [Cardholder authentication Method](#_Ref498356652) |
| 8 | Cardholder authentication entity 1 | AN(1,1) | [Cardholder authentication Entity](#_Ref498356685) |
| 9 | Cardholder authentication entity 2 | AN(1,1) | [Cardholder authentication Entity](#_Ref498356685) |
| 10 | Cardholder authentication entity 3 | AN(1,1) | [Cardholder authentication Entity](#_Ref498356685) |
| 11 | Cardholder authentication entity 4 | AN(1,1) | [Cardholder authentication Entity](#_Ref498356685) |
| 12 | Chip fallback indicator | AN(1,1) | [Chip Fallback Indicator](#_Ref498356714) |
| 13 | Fraud indicator | AN(1,1) | [POS Fraud Indicator](#_Ref498356719) |
| 14 | Security protocol in the cardholder->merchant interaction | AN(1,1) | [Security Protocol (between cardholder device and merchant)](#_Ref498356727) |
| 15 | 3D secure authentication method | AN(1,1) | [3D-secure Authentication Method](#_Ref498356734) |
| 16 | InstantFunding\_Network | N(1,1) | [InstantFunding\_Network](#_Ref31017443) |
| 17 | InstantFunding\_GPS | N(1,1) | [InstantFunding\_GPS](#_Ref31017411) |
| 18 | ExemptFromSCA | AN(1,1) | [ExemptFromSCA](#_Ref31017464) |
| 19 | SCA assessment result | AN(1,1) | [SCA assessment result](#SCA) |
| 20 | SCA test: Knowledge | AN(1,1) | [SCA test: Knowledge](#SCA2) |
| 21 | SCA test: Possession | AN(1,1) | [SCA test: Possession](#SCATest:) |
| 22 | SCA test: Biometric (inherence) | AN(1,1) | [SCA test: Biometric (inherence)](#SCA3) |
| 23 | Thredd Exempt from SCA Indicator | AN(1,1) | [Thredd Exempt from SCA Indcator](#4.14.18) |
| 24 | Card/device type (form factor) | AN(1,1) | [Card/Device Type (Form Factor)](#4.14.19) |
| 25 | Acquirer Exempt from SCA Indicator (specifies if the acquirer sent an exemption indicator in the incoming message) | AN(1,1) | [Acquirer Exempt from SCA Indicator](#Acquirer) |
| 26 | Result of the Authentication Amount and Currency comparison (applicable for 3D Secure transactions only). | AN(1,1) | [Authentication Amount and Currency Comparison](#Authenti) |
| 27 | Merchant or cardholder initiated indicator | AN(1,1) | [Merchant or Cardholder Initiated Indicator](#Merchant) |
| 28 | Merchant Initiated transaction type (or setup of) indicator | AN(1,1) | [Merchant Initiated Transaction Type Indicator](#Merchant2) |
| 29 | Original transaction SCA exempt indicator | AN(1,1) | [Original Transaction SCA Exempt Indicator](#Original) |
| 30 | Original transaction SCA assessment result | AN(1,1) | [Original Transaction SCA Assessment Result](#Original2) |
| 31 | Original transaction status value | AN(1,1) | [Original Transaction Status Value](#Original3) |
| 32 | Extended Authorization indicator | AN(1,1) | [Extended Authorization Indicator](#Extended) |
| 33 | Reserved for future use | AN | Ignore this, if arrives. |

Any positions not received should be treated as âUnknownâ.

## 4.13.2 Cardholder Present Indicator

This field describes if the cardholder was present at the point of sale, or if not, why not. Values are as follows:

| Cardholder Present value | Meaning |
| --- | --- |
| 0 | Cardholder present |
| 1 | Cardholder not present, unspecified |
| 2 | Cardholder not present, mail order |
| 3 | Cardholder not present, telephone order |
| 4 | Cardholder not present, standing auth/recurring transaction (could recur forever) |
| 5 | Cardholder not present, e-commerce |
| 6 | Cardholder not present, installment transaction (like recurring but fixed number of installments) |
| 9 | Unknown |

## 4.13.3 Card Present Indicator

This field describes if the card was present at the point of sale, or if not, why not. Values are as follows:

| Cardholder Present value | Meaning |
| --- | --- |
| 0 | Card not present |
| 1 | Card present |
| 9 | Unknown |

## 4.13.4 Card Data Input Method

This field describes how the card data (eg PAN) was provided to the terminal. Values are as follows:

| Card Data Input Method value | Meaning |
| --- | --- |
| 0 | Information not provided |
| 1 | Manual, no terminal |
| 2 | Magnetic stripe read |
| 3 | Bar code |
| 4 | Optical Character Recognition |
| 5 | Chip dip (i.e. EMV contact) |
| 6 | Key entered / added manually |
| 7 | EMV contactless or VSDC contactless |
| V | E-Commerce |
| C | E-Commerce with EMV cryptogram |
| E | Contactless magnetic stripe |
| F | Account Data on File |
| G | Key entered by Acquirer (merchant phoned acquirer with card data) |
| M | MICR reader |
| Q | QR code |

## 4.13.5 Cardholder Authentication Method

There are four cardholder authentication methods recorded in `GPS_POS_Data`. The table below describes the possible cardholder authentication method values.

| Value | Meaning |
| --- | --- |
| 0 | Not authenticated. |
| 1 | PIN. |
| 2 | Electronic signature analysis. |
| 3 | Biometrics (eg fingerprint, vein scan). |
| 4 | Biographic (eg date-of-birth, other data). |
| 5 | Manual signature verification. |
| 6 | Other manual verification (e.g. drivers licence). |
| 7 | Other. |
| 8 | Unknown. |
| 9 | Passcode/Password (e.g. to unlock a smartphone). |
| A | Pattern (e.g. to unlock a smartphone). |
| B | Possession of Hardware device (e.g. number generating key fob). |
| C | Possession of Hardware device with user verification (as 'B', but additionally the cardholder was verified too). |
| D | Possession of software application (e.g. passcode generating program). |
| E | Possession of software application with user verification (as 'D', but additionally the cardholder was verified too). |
| S | 3D-Secure. |
| T | Tokenization Authentication Framework. |

It is possible for a merchant to specify two cardholder authentication methods. For example, a merchant could apply both PIN verification and Signature verification to an authorisation. Where a method is more secure (such as PIN vs signature), Thredd will put the more secure method in `GPS_POS_Data` position 4 and the less secure in `GPS_POS_Data` position 5. Note that `GPS_POS_Data` positions 6 and 7 are reserved for future use.

Values 7,9,A,B,C,D,E as of 06/01/2021 Thredd expect to see from Visa only, and initially only for transactions on a payment-token (e.g. a smartphone).

## 4.13.6 Cardholder Authentication Entity

There are four cardholder authentication methods recorded in `GPS_POS_Data`.

For each authentication method, the entity performing that authentication method is recorded in the four cardholder authentication entity values.

For example: âCardholder authentication entity 2â describes which entity performed the âCardholder authentication method 2â test.

The table below describes the possible values for cardholder authentication entities.

| Value | Meaning |
| --- | --- |
| 0 | Not authenticated |
| 1 | Chip Card |
| 2 | Card Acceptance Device / Terminal |
| 3 | Authorising Agent |
| 4 | Merchant |
| 5 | Other |
| 6 | Cardholder device (e.g. mobile phone) |
| 7 | Wallet Provider and/or Token Requestor. (E.g. Apple Pay) |
| 8 | Unknown |

## 4.13.7 Chip Fallback Indicator

This is used by Visa to indicate the likely cause of the fallback (e.g., a terminal or card problem).

This is done by noting if the previous chip transaction at the same terminal (which would 99% be on a completely different card) was also a fallback.

The table below describes the possible values for the Chips Fallback Indicator:

| Value | Meaning |
| --- | --- |
| 0 | n/a (This transaction is not a chip fallback transaction, or unknown). |
| 1 | Previous transaction at same terminal was not fallback from chip. |
| 2 | Previous transaction at same terminal was fallback from chip. |

## 4.13.8 POS Fraud Indicator

This is used by the merchant to indicate if the merchant thought the transaction was suspicious.  Not all networks, acquirers or terminals may support this.

Values are as follows:

| Fraud Indicator | Meaning |
| --- | --- |
| 0 | No problem |
| 1 | Merchant suspicious (in UK, this is a code 10 call) |
| 2 | Merchant verified the cardholder ID |

## 4.13.9 Security Protocol (between cardholder device and merchant)

This describes, for an e-commerce or equivalent card data input method, what security was in place between the cardholder device and merchant system.

Values are as follows:

| Security Protocol value | Meaning |
| --- | --- |
| 0 | None |
| 1 | Channel encryption (https) |
| N | Not applicable |

## 4.13.10 3D Secure Authentication Method

If 3D Secure was used to authenticate the cardholder, then this indicates what type of authentication was used.

This is the authentication method as reported by the network.

This field is only populated with an accurate value if Thredd receive this information from the network. The table below summarises this situation.

| Network | 3D-secure version | Content of this 3D Secure field on 3D Secure transactions |
| --- | --- | --- |
| Visa | 1 (all variants) | Limited, only values âxâ or â0â |
| Visa | 2.0 and up | Provided, any value may be set.  (From Base1 field 126.20) |
| Mastercard | SPA v1 | Provided: only values 0,1,2,3 are possible |
| Mastercard | SPA v2 | Provided: only values D, E, F, L, v, x, y, z are possible |

Values are as follows:

| 3D-secure auth method | Visa Meaning | Mastercard Meaning |
| --- | --- | --- |
| x | Unknown / not applicable | Unknown / not applicable |
| 0 | 3DS 1.0.2 or prior (all authentication methods), or 3DS 1.0.2 frictionless flow. | No cardholder authentication performed (for SPA v1 only) |
| 1 | Challenge flow using static Passcode | Password (for SPA v1 only) |
| 2 | Challenge flow using OTP (One-Time Password) via SMS method | Secret Key (For example, a chip card) (for SPA v1 only) |
| 3 | Challenge flow using OTP via key fob or card reader method | PKI (for SPA v1 only) |
| 4 | 3DS 2.0 Challenge flow using OTP via app method | 3DS 2.0 Challenge flow using OTP via app method |
| 5 | 3DS 2.0 Challenge flow using OTP via any other method | 3DS 2.0 Challenge flow using OTP via any other method |
| 6 | 3DS 2.0 Challenge flow using KBA (Knowledge-Based Authentication) method | 3DS 2.0 Challenge flow using KBA (Knowledge-Based Authentication) method |
| 7 | 3DS 2.0 Challenge flow using OOB (Out of Band) with biometric method | 3DS 2.0 Challenge flow using OOB (Out of Band) with biometric method |
| 8 | 3DS 2.0 Challenge flow using OOB with app login method | 3DS 2.0 Challenge flow using OOB with app login method |
| 9 | 3DS 2.0 Challenge flow using OOB with any other method | 3DS 2.0 Challenge flow using OOB with any other method |
| A | 3DS 2.0 Challenge flow using any other authentication method | 3DS 2.0 Challenge flow using any other authentication method |
| B | 3DS unrecognized authentication method | 3DS unrecognised authentication method |
| C | 3DS 2.0 Push Confirmation | 3DS 2.0 Push Confirmation |
| D | 3DS 2.0 Frictionless flow, RBA (Risk-based authentication) review | 3DS 2.0 Frictionless flow, RBA (Risk-based authentication) review |
| E | 3DS 2.0 Attempts server responding | 3DS 2.0 Attempts server responding |
| F | 3DS 2.0 Frictionless flow | 3DS 2.0 Frictionless flow |
| L | Delegated authentication | Delegated authentication |
| S | Frictionless flow, Smart attempts | Not applicable - only available on Visa networks |
| y | 3DS 2.0 Challenge with Unknown authentication method | 3DS 2.0 Challenge with Unknown authentication method |
| v | Authenticated by Mastercard IDCX (âIdentity Check Expressâ) service (or a Visa similar equivalent) | Authenticated by Mastercard IDCX (âIdentity Check Expressâ) service |
| z | AAV refresh transaction successfully authenticated by the ACS (Access Control Server) | AAV refresh transaction successfully authenticated by the ACS (Access Control Server) |

## 4.13.11 InstantFunding\_Network

Network flag to indicate the transaction uses instant funding (MoneySend or Visa Direct). Values are as follows:

| InstantFunding\_Network value | Meaning |
| --- | --- |
| 0 | Normal transaction |
| 1 | Instant Funding Transaction |

## 4.13.12 InstantFunding\_GPS

Thredd flag to indicate the transaction uses instant funding (MoneySend or Visa Direct). Values are as follows:

| InstantFunding\_GPS value | Meaning |
| --- | --- |
| 0 | Normal transaction |
| 1 | Instant Funding Transaction |

## 4.13.13 ExemptFromSCA

Indicates if the transaction is exempt from [Strong Customer Authentication (SCA)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) When the cardholder is authenticated during a payment transaction using a combination of at least two of the following authentication methods: Knowledge (Something the cardholder knows, such as a password), Possession (Something the cardholder has access to, such as a phone number or email account) and Biometrics (such as a fingerprint, face or voice)
Under the Payment Service Directive 2 (PSD2), strong customer authentication is required on all cardholder-initiated transactions when both the card issuer and acquirer are within the European Economic Area (EEA).](#) as per the [Payments Service Directive Two (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for payment services that has the purpose of making payments more secure in Europe. It introduces legislation to improve the payment service authentication process.](#). Values are as follows:

| ExemptfromSCA value | Description |
| --- | --- |
| 0 | Transaction not exempt from SCA or unknown. |
| 1 | Transaction is exempt from SCA due to being on an exempt Merchant Category Code (MCC).  (Acquirer did not provide an SCA exemption indicator.)  (As of 11/02/2020, exempt MCCs are: 4111, 4112, 4131, 4784, 7523) |
| 2 | Contactless transaction under low-value limits (identified by Thredd). |
| 3 | E-commerce transaction under low-value limits (identified by Thredd). |
| 4 | Recurring/installment transaction (identified by Thredd). |
| 5 | Credit (identified by Thredd). Visa expects credit transactions to be out-of-scope. |
| 6 | Mail Order, Telephone Order or other cardholder-not-present transaction (except recurring which is above) which is excluded from SCA requirements (identified by Thredd). This means `GPS_POS_Data` position 1 (cardholder present indicator) will have any value except for 0 (present), 4 (recurring) or 5 (e-commerce). |
| 7 | Acquirer is exempt (located in a country outside of the EEA or UK, so do not fall under the PSD2 jurisdiction). |
| 8 | Not a transaction under PSD2 rules |
| 9 | Reserved for a possible future Thredd detected exemption |
| A | Acquirer transaction risk analysis. |
| C | Secure corporate payment. |
| D | SCA delegation. |
| M | Merchant initiated transaction. |
| O | Authentication outage exemption. |
| R | Recurring payment. |
| T | Trusted merchant. |
| V | Low value payment. |

## 4.13.14 SCA Assessment Result

Indicates if Thredd tested whether the transaction met the criteria for Strong Customer Authentication (SCA), and if so, what was the basis for the assessment decision.

Thredd only does SCA assessments for authorisation requests; for all other transaction types (authorisation advices, clearing, reversals) this will always be âNâ. For a clearing transaction, always check the matching authorisation request(s) to determine if SCA was done.

SCA assessment result values are as follows:

| Value | Description |
| --- | --- |
| 0 | Thredd tested for SCA and the transaction did not meet the criteria for SCA. |
| 1 | Thredd tested for SCA and the transaction met the criteria for SCA.The card/payment token performed SCA. |
| 2 | Thredd tested for SCA and the transaction met the criteria for SCA. At least two of the three SCA tests were performed ([Knowledge](#SCA2), [Possession](#SCATest:) and [Biometric](#SCA3) tests passed). |
| 3 | Thredd tested for SCA and the transaction met the criteria for SCA. Passed the SCA tests in both '1' (payment token performed SCA) and '2' (two of the three biometric, knowledge, possession tests). |
| D | Thredd did not test for SCA. When Thredd assessed the transaction, it was detected that PSD2 checks were delegated to the card/payment token. No further PSD2 assessment was required of Thredd. |
| N | Thredd did not test for SCA. SCA not performed or not applicable (and value âDâ not appropriate). For example, the transaction was declined or PSD2 checks were not turned on for the product. |

## 4.13.15 SCA Test: Knowledge

Indicates whether Thredd detected that the SCA Knowledge test was performed, and if so, what was the result.

The Knowledge test checks if the cardholder knew some information known only to them (e.g. provided a PIN or Passcode.)

Thredd only does SCA assessment for authorisation requests; for all other transactions (authorisation advices, clearing, reversals) this will always be âNâ.

Values are as follows:

| Value | Description |
| --- | --- |
| N | Not performed or not applicable |
| 0 | Failed test |
| 1 | Passed test |

## 4.13.16 SCA Test: Possession

Indicates whether Thredd detected that the SCA Possession test was performed, and if so, what was the result.

The Possession test checks that the cardholder has something that only they should possess (e.g. a physical chip card.)

Thredd only does SCA assessment for authorisation requests; for all other transactions (authorisation advices, clearing, reversals) this will always be âNâ.

Values are as follows:

| Value | Description |
| --- | --- |
| N | Not performed or not applicable |
| 0 | Failed test |
| 1 | Passed test |

## 4.13.17 SCA Test: Biometric (inherence)

Indicates whether Thredd detected that the SCA Biometric (inherence) test was performed, and if so, what was the result.

Biometric testing includes authentication via methods such as fingerprint, iris and facical scans.

Thredd only does SCA assessment for authorisation requests; for all other transactions (authorisation advices, clearing, reversals) this will always be âNâ.

Values are as follows:

| Value | Description |
| --- | --- |
| N | Not performed or not applicable |
| 0 | Failed test |
| 1 | Passed test |

## 4.13.18 Thredd Exempt from SCA Indicator

Indicates whether Thredd detected an SCA exemption. (**Note**: Thredd exemption is only loaded in position 18 if no Acquirer exemption exists)

This position has the same values as position 18, but, no Acquirer values will be present. See [ExemptFromSCA](#_Ref31017464).

## 4.13.19 Card/Device Type (Form Factor)

Indicates the type ([form factor![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A payment device's physical design features which define the size, shape and other physical specifications of the device.](#)) of the card or payment token used to perform the transaction. Only available if present on the chip and sent by the acquirer. See [PaymentToken\_deviceType.](PaymentToken_fields.htm#PaymentT3)

You can use this field to identify the type of payment device and capabilities it supports (e.g., to determine if EMV contact is possible).

## 4.13.20 Acquirer Exempt from SCA Indicator

Indicates whether the transaction is exempt from the EU's'Payment Services Directive 2 (PSD2) Strong Cardholder Authentication (SCA) requirement. This position contains:

* The acquirer's exemption, if it exists
* '0' (not exempt)

Only online authorisation transactions set these exemption flags. Values are as listed below.

| Value | Description |
| --- | --- |
| 0 | Transaction not exempt from SCA or unknown. |
| A | Acquirer Transaction Risk Analysis (identified by Acquirer). |
| C | Secure Corporate Payment (identified by Acquirer). |
| D | SCA Delegation (identified by Acquirer). |
| M | Merchant Initiated Transaction (identified by Acquirer). |
| O | (15th letter of the alphabet) ; Authentication Outage Exemption (identified by Acquirer). |
| R | Recurring Payment (identified by Acquirer). |
| T | Trusted Merchant (identified by Acquirer). |
| V | Low Value Payment (identified by Acquirer). |

## 4.13.21 Authentication Amount and Currency Comparison

This position indicates the results of the *amount* and *currency* comparison between a 3D Secure authentication transaction and the linked authorisation transaction. You can use this result to determine whether the amount authenticated during a 3D Secure session matches the final authorised amount. (Applicable for [EMV 3D Secure![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) EMV 3-D Secure (3DS) is a new 3D Secure specification that supports app-based authentication and integration with digital wallets, as well as traditional browser-based e-commerce transactions. See: https://www.emvco.com/emv-technologies/3d-secure/](#) transactions only).

Values are as listed below.

| Value | Description |
| --- | --- |
| N | Test not performed (e.g., not a 3D Secure transaction, or not performed since the transaction was already declined for another reason). |
| U | Unknown; 3D Secure transaction, but currencies not available. |
| C | Transaction currency different to Authentication currency. |
| 0 | Currencies match: amounts not compared. |
| 1 | Currencies match: Authorisation amount is less than or equal to the Authentication amount. |
| 2 | Currencies match: Authorisation amount is higher than the Authentication amount; difference is less than or equal to 20%. |
| 3 | Currencies match: Authorisation amount is higher than the Authentication amount; difference is greater than 20%. |

## 4.13.22 Merchant or Cardholder Initiated Indicator

Indicates who initiated the transaction.

| Value | Meaning |
| --- | --- |
| C | Cardholder initiated. |
| M | Merchant Initiated. |
| U | Unknown (other information in the transaction may imply one of the above two, but nothing directly indicated either). |

## 4.13.23 Merchant Initiated Transaction Type (or setup of) Indicator

From Banknet DE48.22.05 (introduced in Mastercard announcement AN 5524, live on 07-06-2022) the 4th character (1 to 8) or U=Unknown, so:

| Value | Meaning |
| --- | --- |
| 1 | Credential on file. |
| 2 | Standing Order (variable amount, fixed frequency). |
| 3 | Subscription (fixed amount, fixed frequency). |
| 4 | Instalment (known amount over a specified duration based on a single purchase). |
| 5 | Partial Shipment (for when e-commerce ordered goods are not all available at the time of shipment. Each shipment is a separate transaction). |
| 6 | Related / Delayed Charge (An additional charge after initial services have been paid for. (For example: mini-bar charge in hotel.) |
| 7 | No Show Charge (a penalty charge permitted by the merchant's cancellation policy). |
| 8 | Resubmission (previous authorisation was declined, but merchant can try again. (For example: transit debt recovery.) |
| U | Unknown or not applicable. |

## 4.13.24 Original Transaction SCA Exempt Indicator

Either the `GPS_POS_Data` position 18 value from the original transaction or:

| Value | Meaning |
| --- | --- |
| L | Lookup of original transaction attempted, but original not found. |
| X | Not applicable (original transaction not applicable or lookup was not attempted). |

## 4.13.25 Original Transaction SCA Assessment Result

Either the `GPS_POS_Data` position 19 value from the original transaction or:

| Value | Meaning |
| --- | --- |
| L | Lookup of original transaction attempted, but original not found. |
| X | Not applicable (original transaction not applicable or lookup was not attempted). |

## 4.13.26 Original Transaction Status Value

Either the Transaction Status `Txn_Stat_Code` from the original transaction (for values, see [Transaction Status Codes](Transaction_Status_Codes.htm)) or:

| Value | Meaning |
| --- | --- |
| U | Original transaction status not known or not applicable |

## 4.13.27 Extended Authorisation Indicator

For cardholder-initiated card-not-present transactions, indicates whether the acquirer has requested a 30-day clearing extension. If requested, then the acquirer will have up to 30 days to submit the linked presentment transaction.

Applicable to Visa network transactions only.

| Value | Description |
| --- | --- |
| 0 | No clearing extension requested. |
| 1 | Acquirer requested a 30-day clearing extension. If you receive this value, then note that this will extend the number of days the transaction funds remain blocked on the card, up to 30 days. If you manage the balance ledger, then you should keep the transaction amount block in place for the 30-day period or until you receive the linked presentment. |

## 4.13.28 GPS\_POS\_Data Example

Below is an example of `GPS_POS_Data.`

#### Example 1 â Length of 18 characters

If GPS\_POS\_Data = â0151500340002Nx000â

Then this indicates:

| Position | Value | Meaning |
| --- | --- | --- |
| 1 | 0 | Cardholder is present |
| 2 | 1 | Card is present |
| 3 | 5 | EMV contact |
| 4 | 1 | 1st cardholder authentication method was PIN |
| 5 | 5 | 2nd cardholder authentication method was signature |
| 6 | 0 | No 3rd cardholder authentication method was used |
| 7 | 0 | No 4th cardholder authentication method was used |
| 8 | 3 | PIN (1st cardholder authentication method) was checked by the authorising Agent (i.e. Network, Thredd or EHI) |
| 9 | 4 | Signature (2nd cardholder authentication method) was checked by the Merchant |
| 10 | 0 | n/a (as no 3rd cardholder authentication method) |
| 11 | 0 | n/a (as no 4th cardholder authentication method) |
| 12 | 0 | Not a chip fallback transaction |
| 13 | 2 | Merchant verified the cardholder ID |
| 14 | N | Security protocol (cardholder to merchant) not applicable |
| 15 | x | 3D-secure not applicable |
| 16 | 0 | Instant Funding (Thredd indicator) not applicable |
| 17 | 0 | Instant Funding (Network indicator) not applicable |
| 18 | 9 | ExemptFromSCA not applicable or unknown |

Positions 19 onwards are not present and can be treated as âUnknownâ.

#### Example 2 â Length of 32 characters

If GPS\_POS\_Data = â0151500340002Nx00031109C01MU93U1â

Then this indicates:

| Position | Value | Meaning |
| --- | --- | --- |
| 1 | 0 | Cardholder is present |
| 2 | 1 | Card is present |
| 3 | 5 | EMV contact |
| 4 | 1 | 1st cardholder authentication method was PIN |
| 5 | 5 | 2nd cardholder authentication method was signature |
| 6 | 0 | No 3rd cardholder authentication method was used |
| 7 | 0 | No 4th cardholder authentication method was used |
| 8 | 3 | PIN (1st cardholder authentication method) was checked by the authorising Agent (i.e. Network, Thredd or EHI) |
| 9 | 4 | Signature (2nd cardholder authentication method) was checked by the Merchant |
| 10 | 0 | n/a (as no 3rd cardholder authentication method) |
| 11 | 0 | n/a (as no 4th cardholder authentication method) |
| 12 | 0 | Not a chip fallback transaction |
| 13 | 2 | Merchant verified the cardholder ID |
| 14 | N | Security protocol (cardholder to merchant) not applicable |
| 15 | x | 3D-secure not applicable |
| 16 | 0 | Instant Funding (Thredd indicator) not applicable. |
| 17 | 0 | Instant Funding (Network indicator) not applicable. |
| 18 | 9 | ExemptFromSCA not applicable or unknown. |
| 19 | 3 | Transaction is SCA, as passed 2+ of the knowledge, possession & biometric tests. |
| 20 | 1 | SCA Knowledge test passed. |
| 21 | 1 | SCA Possession test passed. |
| 22 | 0 | SCA Biometric (inherence) test failed. |
| 23 | 9 | Thredd Exempt from SCA Indicator not applicable or unknown. |
| 24 | C | Card or device type is card. |
| 25 | 0 | Acquirer Exempt from SCA Indicator: Transaction not exempt from SCA or unknown. |
| 26 | 1 | Currencies match, Authorisation amount is less than or equal to Authentication amount. |
| 27 | M | Merchant initiated. |
| 28 | U | Unknown or not applicable. |
| 29 | 9 | GPS\_POS\_Data Position 18 value from the original transaction. |
| 30 | 3 | GPS\_POS\_Data Position 19 value from the original transaction. |
| 31 | U | Original Transaction status not known or not applicable. |
| 32 | 1 | Acquirer requested a 30-day clearing extension. |