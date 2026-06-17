# Document History

This section provides details of what has changed since the previous document release.

| Version | Date | Description | Revised by |
| --- | --- | --- | --- |
| 2.3 | 14/08/2025 | Added support for Authentication using Delegated OTP. See [Cardholder Authentication Flows](3D_Secure/Cardholder_Authentication_Flows.htm). | JB |
| 2.2 | 16/04/2025 | Updates to the OTP message templates. See [Appendix 2: OTP Message Templates](Reference/OTP_Message_Templates.htm). | WS |
| 11/02/2025 | Added references to Thredd Portal, our new web application for managing your cards and transactions. | KD |
| 16/01/2025 | Reinstated old IP addresses for PRD1 and PRD2 environments. See [Authorising IP Addresses](3D_Secure/Authorising_IP_Addresses.htm#top). | KD |
| 03/01/2025 | Added a Note on 3D-Secure unenrolment in the [General FAQs](FAQs.htm). Clarified explanations of enrolment and unenrolment (see Enroling your Cards in 3D-Secure). Removed descriptions of upgrading from Batch to RDX. | KD |
| 21/12/2024 | Updated URLs for service migration to the cloud environment. See [Complete Pilot Production Testing](3D_Secure/Complete_production_testing.htm), [Using the Biometric In-App API](3D_Secure/Using_Biometric_API.htm)  and [Using the Thredd OAuth Server.](3D_Secure/Using_Oauth.htm) | KD |
| 13/11/2024 | Updated the URL details for the Live Server (Primary). Removed URL details for the Live Server (Disaster Recovery). See [Authorising IP Addresses.](3D_Secure/Authorising_IP_Addresses.htm)  Updated one of the Production URLs for PRD1 and PRD2. See [Authorising IP Addresses.](3D_Secure/Authorising_IP_Addresses.htm)  Updated Producton URLs for OAuth API endpoints. See [Using the OAuth Server.](3D_Secure/Using_Oauth.htm)  Updated the Producton URL for the NotifyValidate REST API. See [Using the Biometric/In-App Authentication API](3D_Secure/Using_Biometric_API.htm) | KD |
| 13/09/2024 | Removed references to VPN. | WS |
| 02/09/2024 | Added references to Discover Global Network. | PC |
| 26/06/2024 | Updated the [company address](Contact.htm). | PC |
| 2.1 | 21/03/2024 | Updates to content and graphics to align with taxonomy updates on our documentation portal. | KD |
| 22/08/2023 | In the section [PRD1 and PRD2 - Cloud Production Environments](3D_Secure/Authorising_IP_Addresses.htm#PRD1), updated the oAuth endpoint for PRD2 to `p1ists.globalprocessing.net`. | WS |
| 2.0 | 24/07/2023 | Added details of when you might receive the *FAILWITHFEEDBACK* status in the response to a  `NotifyValidate` API call. See the [FAQs](FAQs.htm). | WS |
| 01/06/2023 | Restructuring of guide topics. Updates to reflect changes to the Thredd 3DS Product Setup Form (PSF) and steps in a 3D Secure project. Added details of using the Cards API 3D Secure endpoints. Added details of using Compliance Manager. | WS |
| 31/05/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to new company name and brand identity. | WS |
| 1.9 | 03/01/2023 | Added additional IP addresses that need to be allowed for secure communication between Thredd and your systems when using one of our cloud production environments (PRD1 or PRD2). See [Authorising Thredd IP Addresses](3D_Secure/Authorising_IP_Addresses.htm). | WS |
| 12/12/2022 | Guide updated to reflect that the OUTOFBAND authentication type is now available.  **Note**: Please discuss with your Implementation Manager before implementing this method. | WS |
| 08/12/2022 | Added a note to indicate that your `NotifyInitiateAction` endpoint must resolve to a static IP address. See [Steps in a 3D Secure Biometric/In-app Project](3D_Secure/Steps_in_a_3D_Secure_Biometric.htm). | WS |
| 06/12/2022 | Removal of references to OTP Email, which is currently not supported. | WS |
| 01/12/2022 | Updated the Copyright Statement. | MW |
| 1.8 | 27/10/2022 | Correction to the [oAuth Introspect Example](3D_Secure/Using_Oauth.htm#OAuth) which shows how to validate a bearer token. | WS |
| 20/10/2022 | New *MerchantAppRedirectURL* field added to the  `NotifyInitiateAction` API. This field provides the callback URL to use to enable the merchant's app to redirect the cardholder back to their checkout page after completing the authentication session. See [Appendix 3: Biometric/OOB Fields](Reference/Biometric_OOB_Fields.htm). | WS |
| 12/10/2022  21/09/2022 | Fix to examples in [Appendix 4: KBA Questions](Reference/KBA_Questions.htm).  Updated Thredd UAT IP addresses. See [UAT Server](3D_Secure/Authorising_IP_Addresses.htm#UAT). Added note about response time for  `NotifyInitiateAction` response. | WS  AL |
| 1.7 | 12/08/2022 | New guide layout and HTML version now available. | PC |
| 1.6 | 18/07/2022 | Added details of Dynamic Cardholder Verification (CVV) support to [Supported Authentication Types](3D_Secure/Additional_3D_Secure_Considerations.htm#_Supported_Authentication_Types). | WS |
| 1.5 | 20/05/2022 | Added new section with details of auto-enrolment of 3D Secure credentials when an expiring card is renewed resulting in a new card PAN. See [Using the Card Enrolment API](3D_Secure/Using_Card_Enrolment_API.htm). | WS |
| 1.4 | 08/03/2022  14/04/2022 | Updates for the Out of Band (OUTOFBAND) authentication method. Added notes to clarify that the OUTOFBAND authentication type is not yet available.  Correction: the bearer token in the header of the `NotifyInitiateAction` request, should be Authorization: Bearer. | WS |
| 1.3 | 31/01/2022 | Addition of Knowledge Based Authentication (KBA).  Removal of references to OTP Email, which is currently not supported. | WS |
| 1.2 | 01/11/2021 | Removed the port number from UAT URLs. | WS |
| 1.1 | 30/09/2021 | Address updates and update to Figure 4: 3D Secure Authentication Process Using RDX and Biometrics.  New [Appendix 3: Biometric/OOB Fields](Reference/Biometric_OOB_Fields.htm#_Appendix_3:_Biometric/OOB) | WS |
| 1.0 | 28/06/2021 | First version â major rewrite and update. | WS |
| 0.1 | 22/04/2021 | Draft version | VAL |