# 7 Visa Contactless EMV Settings

This section describes the [Visa Contactless Payment Specification (VCPS)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Outlines the requirements for conducting secure contactless transactions at point-of-sale (POS) devices.](#) settings relevant to Thredd for the Visa Contactless application.

The Tag values are as mentioned in the *VIS table A-1 âData Element Descriptionsâ*.

Additionally, for each tag, as per [VCPS] manual, each tag will be noted as:

* Shared â shared with [VIS].  This means the parameter exists once on the card, and is used for both Contact and Contactless.
* Independent â value independent to [VIS].  This means the parameter exists twice: once for contact, and once for contactless. Values are separate, (but they can be configured to have the same value if desired.)
* Exclusive to VCPS â value does not exist for [VIS].  Parameter only exists for contactless.

This table only includes the parameter/tag settings that are relevant to Thredd.

| Tag & Name | Byte / Bit (s) | Description | Thredd comment |
| --- | --- | --- | --- |
| Application Default Action  â9F52â  [VCPS] and [VIS]  (Shared) | All Bytes | This is shared with VIS. | See VIS comments above. |
| Application Interchange Profile  â82â  [EMV], [VCPS], [VIS]  (Independent) | Byte 2  bit 8 | 1b = Is Contactless Magnetic Stripe supported? | Thredd recommend You SHOULD set this to b0.  This is because Thredd does not support validation of the dCVV, which is required to validate genuine contactless magnetic stripe transactions.  You can set this to ANY, but should be aware that fraudulent contactless magnetic stripe transactions could be approved. |
| Card Additional Processes  â9F68â  (Shared) | All | Indicates card processing requirements and preferences (for contactless application). | You can set this to ANY. |
| Card CVM Limit  â9F6Bâ  [VCPS]  (Exclusive to VCPS) | all | Visa proprietary data element indicating that for domestic contactless transactions where this value is exceeded, a CVM is required by the card.    Online PIN and Signature are the CVMs supported by cards compliant to this specification. | You can set this to ANY (including not personalising it, which is Visaâs recommendation.)  Note that Thredd would need to assist (via Issuer Script) if you need the value changed for a large number of cards (for example, if the limit changed.) |
| Card Transaction Qualifiers  â9F6Câ  [VCPS]  (Exclusive to VCPS) | All | Indicates card CVM requirements, issuer preferences, and card capabilities. | You can set this to ANY. |
| Cryptogram Version Number  Part of â9F10â  [VCPS]  (Independent) | Byte 1 | (See [VIS] above) | See [Appendix 1: Mastercard Cryptogram Version Number Values](../Appendices/Appendix 1.htm).  It MUST only be set to an algorithm in Appendix A.1 where âThredd Supported = Yesâ.  (Any other CVN value will result in a decline.)  â11â is normally used for contactless (but Thredd does not require this.) |
| Issuer Application Data  Tag â9F10â  [VIS], [EMV], [VCPS] | All bytes | Data from the card as defined in [VIS]/[VCPS] to be sent to the issuer online. | See comment in [VIS] |
| Issuer Authentication Data  Tag â91â  [VIS], [EMV], [VCPS] | All bytes | Data from the Issuer (Thredd here) to be sent back to the card in an online transaction response. | See comment in [VIS] |
| Log Entry  Tag â9F4Dâ  [EMV] | Byte 2 | Maximum number of records in the transaction log file. | See comment in [VIS] |