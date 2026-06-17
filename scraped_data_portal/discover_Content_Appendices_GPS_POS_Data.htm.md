## 9.11 GPS\_POS\_Data field

This is a Thredd field that records POS Data codes, which are specific to this transaction. Each position records a different piece of information.  Positions 25 onwards are reserved for future use.

In this section of the guide, we only reference new field position values added for Discover Global Network (highlighted in the table below). For details of all other field positions, refer to the [External Host Interface Guide > GPS\_POS\_Data field](https://docs.thredd.com/ehi/Content/Appendices/GPS_POS_Data.htm).

### 9.11.1 GPS\_POS\_Data Positions

| Position | Name | Format | Values defined in section |
| --- | --- | --- | --- |
| 15 | 3D secure authentication method | AN(1,1) | [3D-secure Authentication Method](#_Ref498356734)  New values added for Discover. |
| 28 | Merchant Initiated transaction type (or setup of) indicator | AN(1,1) | [Merchant Initiated Transaction Type Indicator](#Merchant2)  New values added for Discover. |

### 9.11.2 3D Secure Authentication Method

If 3D Secure was used to authenticate the cardholder, then this indicates what type of authentication was used.

This is the authentication method as reported by the network.

This field is only populated with an accurate value if Thredd receive this information from the network. The table below summarises this situation.

| Network | 3D-secure version | Content of this 3D-secure field on 3D-secure transactions |
| --- | --- | --- |
| Visa | 1 (all variants) | Limited, only values âxâ or â0â |
| Visa | 2.0 and up | Provided, any value may be set.  (From Base1 field 126.20) |
| Mastercard | SPA v1 | Provided: only values 0,1,2,3 are possible |
| Mastercard | SPA v2 | Provided: only values D, E, F, L, v, x, y, z are possible |
| Discover | 3DS 1.0.2 or prior | Limited, only values x and 0 |
| Discover | 2.0 and up | Provided, any value may be set.  (From Base1 field 126.20) |

Values are as follows:

| 3D-secure auth method | Discover Meaning |
| --- | --- |
| x | Unknown / not applicable |
| 0 | No cardholder authentication performed (for SPA v1 only) |
| 1 | Password (for SPA v1 only) |
| 2 | Secret Key (For example, a chip card) (for SPA v1 only) |
| 3 | PKI (for SPA v1 only) |
| 4 | 3DS 2.0 Challenge flow using OTP via app method |
| 5 | 3DS 2.0 Challenge flow using OTP via any other method |
| 6 | 3DS 2.0 Challenge flow using KBA (Knowledge-Based Authentication) method |
| 7 | 3DS 2.0 Challenge flow using OOB (Out of Band) with biometric method |
| 8 | 3DS 2.0 Challenge flow using OOB with app login method |
| 9 | 3DS 2.0 Challenge flow using OOB with any other method |
| A | 3DS 2.0 Challenge flow using any other authentication method |
| B | 3DS unrecognized authentication method |
| C | 3DS 2.0 Push Confirmation |
| D | 3DS 2.0 Frictionless flow, RBA (Risk-based authentication) review |
| E | 3DS 2.0 Attempts server responding |
| F | 3DS 2.0 Frictionless flow |
| G | 3DS 2.0 Challenge flow using Decoupled |
| H | 3DS 2.0 Challenge flow using [WebAuthnClosed WebAuthn is a web standard developed by W3C and FIDO Alliance, allowing the use of biometrics and other authenticators for secure user verification during a 3D Secure Challenge authentication scenario.](#) |
| I | 3DS 2.0 Challenge flow using [Secure Payment Confirmation (SPC)Closed SPC allows the issuer to directly authenticate the customer via FIDO (Fast IDentity Online) biometric authentication during a 3D Secure Challenge scenario.](#) |
| J | 3DS 2.0 Challenge flow using Behavioural Biometrics |
| L | Delegated authentication |
| y | 3DS 2.0 Challenge with Unknown authentication method |
| v | Authenticated by Mastercard IDCX (âIdentity Check Expressâ) service |
| z | AAV refresh transaction successfully authenticated by the ACS (Access Control Server) |

### 9.11.3 Merchant Initiated Transaction Type (or setup of) Indicator

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
| A | Re-authorize for Full Amount |
| I | Incremental Authorization |
| U | Unknown or not applicable. |