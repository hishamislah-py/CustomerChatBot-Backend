# Document History

| Version | Date | Description | Revised by |
| --- | --- | --- | --- |
| 2.2 | 27/11/2025 | Added support for Mastercard Click to Pay. See [Click to Pay.](Implementation/ClickToPay.htm) | JB |
| 20/11/2025 | Included a description on [Mastercard Provisioning Velocity Limits](Implementation/Token_Provisioning_Message.htm#Masterca). | KD |
| 21/08/2025 | Added support for Samsung Pay to In-App Provisioning. See [Implementing In App Provisioning](Implementation/Implementing_In_App_Provisioning.htm). | JB |
| 31/07/2025 | Updated [Event Notifications](Implementation/Tokenisation_Configuration.htm#_External_host_interface) to include information on how to use webhooks for event notifications. | JB |
| 12/06/2025 | Updated the [Tokenisation Configuration](Implementation/Tokenisation_Configuration.htm) page, including updating guidance on Payment Token groups, removing the Visa/Mastercard Rules section, updating references on the Mastercard Portal, and adding new device binding logic. | JB |
| 02/05/2025 | New [Click to Pay](Implementation/ClickToPay.htm) section added. | JB |
| 2.1 | 25/02/2025 | Updated the example request body for Apple In-App Provisioning. See [Implementing In App Provisioning](Implementation/Implementing_In_App_Provisioning.htm). | JB |
| 12/02/2025 | Added references to Thredd Portal, our new web application for managing your cards and transactions. | JB |
| 30/01/2024 | Added [Orange Flow](Getting_Started/How_Tokenisation_Works.htm) section to How Tokenisation Works page. Added Orange Flow to [Glossary](Glossary.htm). | JB |
| 27/01/2025 | New [Appendix H: Card Status Codes](References/Card_status.htm) â lists card status changes that trigger calls to Token Service Provider (MDES/VDEP). | WS |
| 16/01/2025 | Corrections to JSON tokenisation examples: ACN, TCN and TEN messages should have `Txn_Type` = J. ACN messages should have an `MTID` = 0120, while TCN and TEN messages have an `MTID` = 0620. See [Appendix C: EHI Tokenisation Fields](References/EHI_Tokenisation.htm). | WS |
| 16/10/2024 | Rewrite to section [Managing your Program](Implementation/Managing_your_Programme.htm), introducing new use cases and details of how to implement using either SOAP API or REST API. New [Appendix G: Realtime Token Status Change](References/Realtime_token_status_change.htm).  Revision to [FAQ](FAQs.htm) on using Thredd's In-app provisioning service. | WS |
| 21/08/2024 | Added a new section with important information on [Configuring Token Sub-Bin Ranges](Implementation/Tokenisation_Configuration.htm#Configur). | WS |
| 19/07/2024 | Added section on [implementing In-App provisioning](Implementation/Implementing_In_App_Provisioning.htm). Updated [Managing your Programme](Implementation/Managing_your_Programme.htm) and [How Tokenisation Works](Getting_Started/How_Tokenisation_Works.htm) to support these changes. | JB |
| 02/07/2024 | Updated [Managing your Programme](Implementation/Managing_your_Programme.htm) to update Mastercard update file frequency.  Updated the [company address](Contact.htm). | JB |
| 2.0 | 27/06/2024 | Correction - updated JSON format 36000 tokenisation message from Mastercard to Visa. See [Appendix C: EHI Tokenisation Fields](References/EHI_Tokenisation.htm). | JB |
| 10/06/2024 | Added examples of EHI 34000, 35000 and 36000 tokenisation messages in JSON format. See [Appendix C: EHI Tokenisation Fields](References/EHI_Tokenisation.htm). | WS |
| 04/04/2024 | Updates to content to align with taxonomy updates on our Documentation Portal. Added details of using Thredd's REST-based Cards API to manage tokenised cards. | WS |
| 05/10/2023 | Correction to text in Scenario 1 in [Appendix E: Mastercard Tokenisation Messages](References/Mastercard_Tokenisation_Messages.htm). The EHI `ProcCode` received in Green Flow should be "350000 (TCN)". | WS |
| 29/09/2023 | Updated Smart Client screen shot in [Appendix B: View the OTP on Smart Client.](References/View_One_Time_Password.htm) | MW |
| 21/09/2023 | Added details to clarify that the EHI field `PaymentToken_creatorStatus` can contain â â or be empty when no value has been provided. See [Appendix C: EHI Tokenisation Fields](References/EHI_Tokenisation.htm). | WS |
| 01/09/2023 | New response codes table and details added to the section [Changing the status of a Payment Token](Implementation/Managing_your_Programme.htm#_Changing_Status). | WS |
| 1.9 | 14/08/2023 | Correction to the list of Visa documents that must be completed when implementing a tokenisation project through Visa. See [Implementing a Tokenisation Project](Implementation/Implementing_Tokenisation.htm). | WS |
| 08/08/2023 | Added a note to clarify that the Token Device Management web service (`Ws_Token_Device_Management`) is for use on the Visa (VDEP) service only. See [Managing your Programme](Implementation/Managing_your_Programme.htm). | WS |
| 04/08/2023 | Added JSON example EHI TAR Message. See [Appendix C: EHI Tokenisation Fields](References/EHI_Tokenisation.htm). | JB |
| 07/06/2023 | Updated Operations email address to be occ@thredd.com | MW |
| 27/04/2023 | Guide rebrand to new company name and brand identity. | WS |
| 1.8 | 13/02/2023 | Revised wording around Apple Pay Orange flow support. See [Appendix F: Apple Pay Tokens](References/Apple_Pay_Tokens.htm). | WS |
| 21/12/2022 | Updated numbering in Table of Contents. | MW |
| 1.8 | 22/12/2022 | Added details of the real-time API for Mastercard clients. See [Real-time Token Status Change (Mastercard)](Implementation/Managing_your_Programme.htm#_Token_Status_Change) and [FPAN Reissue and Replacement](References/Apple_Pay_Tokens.htm#FPAN) | MW |
| 01/12/2022 | Updated the Copyright Statement. |
| 1.7 | 07/11/2022 | Correction: In the [Visa Tokenisation](References/Visa_Tokenisation.htm) yellow flow, the final message *PaymentToken\_creatorStatus* status should be "*I*" when provisioning was unsuccessful. | WS |
| 12/10/2022 | Added a new section on [Updating the Card Profile Linked to a Token](Implementation/Managing_your_Programme.htm#Updating).  New *Payment-Token Transactions* setting enables you to decide whether the Thredd card status should be checked or ignored during transaction authorisations. See [Thredd Configuration Options](Implementation/Tokenisation_Configuration.htm#_GPS_Configuration_Options). | WS |
| 1.6 | 03/08/2022 | Updated the PDF page layout. | MW |
| 21/07/2022 | New online version of the Tokenisation Service Guide is now available. | PC |
| 28/4/2022 | Added details of Mastercard Real-Time Token to Token and PAN Lifecycle Management. See [Real-time Token Status Change (Mastercard)](Implementation/Managing_your_Programme.htm#_Token_Status_Change). | MW |
| 1.5 | 14/04/2022  28/04/2022 | Addition of Digiseq as a [third-party push provisioning service provider](Getting_Started/How_Tokenisation_Works.htm#_GPS-Meawallet_Integration_for).  Correction: If the DPAN over FPAN setting is **enabled**, then you must separately set the statuses of both the FPAN and DPAN. See [DPAN over FPAN Status.](Implementation/Tokenisation_Configuration.htm#_DPAN_over_FPAN) | WS |
| 1.4 | 08/02/2022  02/02/2022  01/04/2022 | Added information on the [DPAN over FPAN Status](Implementation/Tokenisation_Configuration.htm#_DPAN_over_FPAN) option.  Added note to clarify usage of cards status codes for temporary blocks. See [Status Codes to use for Card Blocks](Implementation/Managing_your_Programme.htm#_Status_codes_card_blocks).  Added details of MRCHTOKEN and Apple Pay Orange flow. Added new Appendix on [ApplePay Tokens](References/Apple_Pay_Tokens.htm). Added details of enabling Manual Key Entry in the [Card Usage Groups](Implementation/Tokenisation_Configuration.htm#_Card_Usage_Groups) used by tokenised cards. | WS |
| 1.3 | 9/08/2021  25/08/2021  03/09/2021 | New advice on [Status Codes to use for Card Blocks.](Implementation/Managing_your_Programme.htm#_Status_codes_card_blocks)  Updates to diagram and description in Section [Message flow for Visa Token Provisioning (Yellow Flow).](Implementation/Token_Provisioning_Message.htm#_Message_flow_for_mastercard)  Note added to section [Token Provisioning Message Flows](Implementation/Token_Provisioning_Message.htm) to highlight that tokenisation messages receive via EHI are advices only and should never be used for payment authorisation approval or decline decisions. | WS |
| 1.2 | 28/06/2021 | New [Mastercard Tokenisation Messages.](References/Mastercard_Tokenisation_Messages.htm) | WS |
| 1.1 | 14/05/2021 | Changes to section [Thredd Configuration Options](Implementation/Tokenisation_Configuration.htm#_GPS_Configuration_Options), and updates to Figures 9 and 10. | WS |
| 1.0 | 29/03/2021 | First version | WS |
| 0.1 | 4/11/2020 | Initial draft | SB |