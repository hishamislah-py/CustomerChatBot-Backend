# Appendix 4: Applying a Fee to an Event

You can apply a fee to an event where a Thredd API is used to trigger that event. Below is a list of events that are initiated using either SOAP web services or REST-based Cards API , which you can configure to trigger fees. For details of how to configure the fee in the Thredd system, see [API Usage Fees](../Fee_Setup_and_Configuration/Web_Service_Fees.htm).

| Proc Code | Event | Web Service that triggers the fee | Cards API that triggers the fee |
| --- | --- | --- | --- |
| 058 | PIN Control | `WS_PinControl` | [Set PIN](https://cardsapidocs.thredd.com/reference/set-pin) |
| 070 | Balance Enquiry Fee 0 â Call Centre | `Ws_Card_BalEnq`  `Ws_Balance_Enquiry(_V2)` | [List Card Balance](https://cardsapidocs.thredd.com/reference/list-card-balance) |
| 071 | Balance Enquiry Fee 1 â Website | `Ws_Balance_Enquiry(_V2)` | [List Card Balance](https://cardsapidocs.thredd.com/reference/list-card-balance) |
| 072 | Balance Enquiry Fee 2 - IVR | `Ws_Balance_Enquiry(_V2), Ws_Card_BalEnq` | [List Card Balance](https://cardsapidocs.thredd.com/reference/list-card-balance) |
| 073 | Balance Enquiry Fee 3 - SMS | `Ws_Balance_Enquiry(_V2), Ws_Card_BalEnq` | [List Card Balance](https://cardsapidocs.thredd.com/reference/list-card-balance) |
| 080 | Card Upgrade Fee | `Ws_Convert_Card` | [Convert Card](https://cardsapidocs.thredd.com/reference/convert-card) |
| 081 | Card Closure/Redemption Fee | `Ws_StatusChange` | [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) |
| 082 | Card Issue Fee (Physical) | `Ws_CreateCard` | [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) |
| 084 | Card Replacement Fee | `Ws_Renew_Card` | [Replace a Card](https://cardsapidocs.thredd.com/reference/replace-card) |
| 085 | Card Issue Fee (Virtual) | `Ws_CreateCard` | [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) |
| 086 | Secondary Card Issue Fee | `Ws_link_cards`  `Ws_CreateCard` | [Create a Card](https://cardsapidocs.thredd.com/reference/create-card) |
| 087 | Primary Card Activation Fee | `Ws_Activate_Load`  `Ws_CreateCard` | [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) |
| 088 | Secondary Card Activation Fee | `Ws_Activate_Load Ws_CreateCard` | [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) |
| 089 | Lost & Stolen Card Fee | `Ws_Regenerate`  `Ws_RegenerateWallet` | [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status) |