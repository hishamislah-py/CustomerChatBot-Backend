# PSD2 Test 3 - Any acquirer exemptions?

Did the acquirer send any of these exemptions with this transaction?

Transaction risk analysis exemption and the transaction value is below or equal to the *Acquirer Transaction Risk Analysis Exemption* transaction limit set for your product\*

Transaction low value exemption and the transaction value is below or equal to the **Acquirer Low-Value Exemption** transaction limit set for your product\*

The acquirer delegated authentication to the merchant

The transaction is part of a secure corporate payment transaction

The transaction has been initiated by the merchant without interacting with the cardholder (e.g., London Underground transport billing after the journey is complete)

The merchant or acquirer was unable to complete authentication due to an outage

The merchant is part of the acquirer's trusted merchant scheme

None of the above apply

The transaction is not exempt from the PSD2 rules. It looks like the transaction will be [Soft Declined![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif) A Soft Decline is a decline response to the terminal or online merchant, indicating that the transaction failed due to being non-SCA. The transaction should be re-attempted with SCA. This may include (for card present transactions) requesting that the terminal authenticates the cardholder using PIN.](#). **Go to** [PSD2 Soft Decline Check](PSD2_Soft_Decline.htm).

The transaction is exempt under the PSD2 rules. The transaction will be approved.

Submit

\* If a limit is not configured for the product, then the exemption will always be honoured.