# Appendix C: Usage Groups

The table below describes the different types of Card Acceptance Methods available in the form of Usage groups. Rules can be set to dictate levels of Card Acceptance, such as MCC Group acceptance.

| Group Type | Purpose |
| --- | --- |
| Card Acceptor List | You can specify at the merchant ID level where authorisations will be accepted. (Based on DE42). For example, you can allow a card to be used only in specific shops or locations.  For details, see: [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Cards API Website (REST)](https://cardsapidocs.thredd.com/docs/create-card-2)   [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Web Services Guide (SOAP).](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Create.htm?Highlight=Ws_CreateCard) |
| Card Disallow List | You can specify at the merchant ID level where authorisations will be declined. (Based on DE42). For example, you can prevent a card from being used in specific shops or locations.  For details, see: [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Cards API Website (REST)](https://cardsapidocs.thredd.com/docs/create-card-2)   [â¢](https://cardsapidocs.thredd.com/docs/create-card-2) [Web Services Guide (SOAP).](https://docs.thredd.com/webservices/Content/Web_services_api/Card_Create.htm?Highlight=Ws_CreateCard) |
| Group Web | You can charge a fee for specific web services such as a PIN change request. |
| Card FX Group | You can upload and manage your own Foreign Exchange rates which can be applied to authorisations and presentments. |
| Calendar Group | You can restrict card acceptance based on specific time and date parameters. For example, a trucking company may restrict card use to weekdays from 9 until 5 to allow employees to pay for fuel. Usage cases include religious observances or working hours. |
| Card Linkage | Used to link primary and secondary cards. You can apply card linkage on a shared balance or a separate balance. |
| Group Usage | You can apply the specific âCard Usage Rulesâ which dictate card behaviour such as PAN entry method rules, cardholder verification, regional based rules, and transaction types.  Check the usage rules if a card has been declined, for example, to show if transactions are prevented from going through on an unknown acceptance method. |
| Group MCC | You can allow or disallow card acceptance (auths) based on one or more merchant category codes (MCC). For example, you can disallow gambling sites. |
| Group Limit | Displays specific limits assigned to that token, for example, the maximum balance permitted to be held on the card. |
| Group Auth | You can apply a fee to Authorisations based on the processing code, for example, an authorisation to check a balance. |
| Limited Network | You can restrict card acceptance to a limited network only, for example, a gift card may be limited to merchants in a particular shopping centre only. This rule is based on 3 different data elements:   1. DE42 â Merchant ID 2. DE43 â Address, text field for the merchant ID 3. DE61 â Postcode |
| Rec Fee | You can apply fees based on rules or actions you set on the card. For example: inactivity fees, and/or dormancy fees. These are configured by Thredd. |