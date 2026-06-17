# PSD2 Product Settings

Thredd PSD2 settings for your card product are set up at a Product Master level. See the example below.

![](../Resources/Images/Product_Master_PSD2.png "Product Master Screen in Smart Client showing PSD2 Compliance settings")

Figure 10: PSD2 Settings on the Product Master screen in Smart Client

This screen is an internal Thredd screen available to Thredd administrators only. For further information, please contact your Account Manager.

Refer to the table below for details. These exemption checks are based on [SCA Exemptions](PSD2_Rules.htm#SCA) (EBA Articles 11, 15, 16).

| Setting | Description |
| --- | --- |
| PSD2 Compliance | Indicates whether PSD2 complance checks are enabled for this card product. |
| PSD2 Txn Count Limit | The cummulative transaction count upper limit that is exempt from PSD2 (e.g., 5). If the number of cummulative transactions is above this limit then Thredd considers the transaction as within scope of PSD2. (See [SCA Exemptions: Articles 11 and 15](PSD2_Rules.htm#SCA).)  Separate limits can be configured for Contactless and E-commerce transactions. |
| PSD2 Accum Value Limit | The accumulated transaction upper limit that is exempt from PSD2 (e.g., 100.00 EUR). If the accumulated transaction amount is above this limit then Thredd considers the transaction as within scope of PSD2. (See [SCA Exemptions: Articles 11 and 15](PSD2_Rules.htm#SCA).)  Separate limits can be configured for Contactless and E-commerce transactions. The amount limits are in the primary billing currency of the card product. |
| PSD2 Single Value Limit | The transaction amount upper limit for a single transaction that is exempt from PSD2 (e.g., 30.00 EUR). If the transaction amount is above this value then Thredd considers the transaction as within scope of PSD2. (See [SCA Exemptions: Articles 11 and 15](PSD2_Rules.htm#SCA).)  Separate limits can be configured for Contactless and E-commerce transactions. The amount limits are in the primary billing currency of the card product. |
| PSD2 Txn Risk Analysis Max exemption value | Maximum permitted transaction value (in primary billing currency of the product) up to which an Acquirer claimed *Transaction Risk Analysis* exemption will be honoured. See [Step 3: Check for PSD2 Acquirer Exemptions](Step3_PSD2_Acquirer_Exemptions.htm). |
| PSD2 Acquirer Low-Value Max exemption value | Maximum permitted transaction value (in primary billing currency of the product) up to which an Acquirer claimed *Low Value* exemption will be honoured. See [Step 3: Check for PSD2 Acquirer Exemptions](Step3_PSD2_Acquirer_Exemptions.htm).  **Note**: Thredd recommends you set this to zero (this will ensure that only Thredd does the low value exemption test). |
| 3DS is SCA only if cardholder is challenged | For e-commerce 3D Secure transactions, only consider the transaction as SCA if the cardholder is challenged (asked to authenticate during a 3D Secure session). |
| Recurring payment original must be SCA | For recurring transactions, only apply the exemption if the original transaction was SCA. |
| Exempt PAN key entry from Hotel | Treat hotel merchants (MCC 3501-3999, 7011) doing PAN key entry or manual cardholder present (or unknown) transactions as exempt from SCA. |
| Exempt pan key entry from Vehicle Rental | Treat car rental merchants (MCC 3MCC 3351-3500, 7512,7513,7519) doing PAN key entry or manual cardholder present (or unknown) transactions as exempt from SCA. |
| When Authorisation Amount is higher than Authentication Amount by:  Less than or equal to 20%  More than 20%  Currency Mismatch | This setting is used when checking the transaction amount value and currency provided during a 3D secure Authentication session with the transaction amount value and currency that has been authorised. If there is a mismatch, then Thredd can:   * Soft Decline - we return a soft decline code which indicates to the merchant to try again using SCA * Hard Decline - we return a hard decline code which indicates to the merchant not to try again * Do Nothing - Thredd does not decline the transaction   **Note**: This check is used to comply with the PSD2 SCA dynamic linking requirements (see [PSD2 Dynamic SCA Linking](PSD2_Rules.htm#PSD2)). |