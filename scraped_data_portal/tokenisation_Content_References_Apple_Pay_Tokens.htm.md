# Appendix F: Apple Pay Tokens

Apple technology enables you to offer your customers an option to use their Apple devices to make contactless and secure e-commerce payments.

Your Mobile App can use an iOS API to view cards youâve issued that have been provisioned onto the Apple device. You can use the Apple API to present your customer with their chosen card for payment. The cardholder can then provide consent for the transaction using Touch ID / Face ID or a passcode to make a payment. Upon completion of the payment, the cardholder is automatically returned back to your Mobile App.

Apple require certification to use their service, which must be done directly with them. For further information, please refer to the Apple document: Functional Requirements Direct NFC Access and Apple Pay.

For more information on Apple Pay services for developers, see the [Apple Pay Developer Website](https://developer.apple.com/).

## Apple Pay Token Provisioning

For details of token provisioning flows supported by Thredd, see [Token Provisioning Message Flows](../Implementation/Token_Provisioning_Message.htm).

Token provisioning requests that are flagged as Apple Orange Flow and/or a Device Score = 1 indicate that more rigorous authentication of the cardholder is required. See [Apple Pay Orange Flow](#_ApplePay_Orange_Flow) below.

## FPAN Reissue and Replacement

Apple Pay require that when the FPAN is reissued (due to expiration or lost/fraud replacement), the DPAN should continue to work without the need to re-provision the new physical card. The card in the Wallet displays the new FPAN number, if it has changed.

By default, the FPAN and DPAN are connected, so if the FPAN is lost and the card status is changed this will also change the status of the DPAN. If you need the DPAN to continue to work while the FPAN is replaced you must split them, by enabling the DPAN\_over\_FPAN option. For details, see [DPAN over FPAN Status](../Implementation/Tokenisation_Configuration.htm#_DPAN_over_FPAN).

When replacing a card, you should always use the Card Renew (`Ws_Renew`) web service or the [Replace a Card](https://cardsapidocs.thredd.com/reference/replace-card) endpoint (REST). For details, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm) or the [Cards API Website](https://cardsapidocs.thredd.com/).

Once the new card is activated, the update to the FPAN/DPAN details will be immediate.

## FPAN Reissue and Replacement

Apple Pay require that when the FPAN is reissued (due to expiration or lost/fraud replacement), the DPAN should continue to work without the need to re-provision the new physical card. The card in the Wallet displays the new FPAN number, if it has changed.

By default, the FPAN and DPAN are connected, so if the FPAN is lost and the card status is changed this will also change the status of the DPAN. If you need the DPAN to continue to work while the FPAN is replaced you must split them, by enabling the DPAN\_over\_FPAN option. For details, see [DPAN over FPAN Status](../Implementation/Tokenisation_Configuration.htm#_DPAN_over_FPAN).

When replacing a card, you should always use the Card Renew (`Ws_Renew`) web service or the [Replace a Card](https://cardsapidocs.thredd.com/reference/replace-card) endpoint (REST). For details, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm) or the [Cards API Website](https://cardsapidocs.thredd.com/).

Once the new card is activated, the update to the FPAN/DPAN details will be immediate.