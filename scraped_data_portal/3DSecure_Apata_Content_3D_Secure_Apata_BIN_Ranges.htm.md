## 5.3 BIN ranges by card program

Please select the required exemptions and risk features required for card program and associated BIN ranges.

| Field | Description |
| --- | --- |
| BIN Range(s) Low | Include the 16 digit lower range of Bank Identification Numbers (BINs) without spaces (e.g., 4579123400000000). |
| BIN Range(s) High | Include the 16 digit upper range of Bank Identification Numbers (BINs) without spaces (e.g., 4579123499999999). |
| Card Program Name | A card program is a grouping of card ranges. Card Programs can be configured with unique Challenge Profiles and Risk Profiles.  Provide the name to apply to each card program. |
| Trust list | Allows exemptions under the card program and associated card ranges if the merchant was previously whitelisted by the cardholder.   * Mastercard prerequisites: when enrolling card/BIN ranges in Mastercard ISSM tool, âWhitelisting supported by ACSâ under âAdditional Serviceâ must be turned on in order to support trust list exemptions via Apata. * Visa prerequisites: Issuers (BIN sponsors) need to be enabled for EMV 3DS 2.2 to use the indicators applicable to trusted beneficiaries. Issuers (BIN sponsors) are required to register their account ranges with Visa's Directory Server to indicate their support for the trusted beneficiaries' indicators. Support should be indicated by selecting YES in the Card Range File under field "TRUSTED LISTING SUPPORTED?". |
| PSD2 Low Value | Applies the low-value payment exemption under PSD2 if the following conditions are met:  â¢ Transaction value is less than â¬30.00 (or equivalent in local currency e.g., SEK, CZK, PLN).  â¢ The cumulative spend since the last challenge is less than â¬100.00.  â¢ The number of transactions since the last challenge is less than 5. |
| Secure Corporate Payment | Permits the secure corporate payment exemption to be used. Payment is made with an eligible commercial card through a dedicated secure corporate process that meets the security protocols set by the National Competent Authority (NCA). |
| Merchant Initiated Transaction | Identifies the merchant-initiated transactions where previous transaction from same merchant was authenticated with SCA. |
| Acquirer Exemption | Configure a list of merchants to either allow or disallow the exemption request. If these merchants request an exemption then accept/deny exemption based on presence on this list. If YES is selected, the configuration will accept all acquirer exemptions. |
| One Leg Transaction | Used for handling transactions where the issuer (BIN sponsor) and acquirer are located in the EEA, then SCA is enforced.  If the issuer (BIN sponsor) or acquirer is not within the EEA, SCA is exempted as one leg out. |
| Recurring Payment | If the payment is recurring, then it does not require SCA and an exemption is applied. First recurring transaction must be SCA. |

All the above exemptions are applicable to EEA and UK issuers (BIN sponsors).