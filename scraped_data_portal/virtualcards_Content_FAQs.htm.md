# Frequently Asked Questions

## Virtual Card Usage

#### Q. When I convert a virtual card to a physical card, can the virtual card still be used?

The cardholder can continue to use the virtual card until the physical card has been activated. Once the physical card is activated, the virtual card cannot be used.

#### Q. Can the cardholder view the transaction history on the virtual card after it has been converted to a physical card?

Yes, both physical and virtual cards share the same card record, so card and transaction enquiries will return transaction details.

#### Q. Can a Virtual Card PAN be used for POS transactions?

If it is added to a Digital Wallet such as Apple Pay or Google Pay then it can be used for POS transactions through a cardholders device. Otherwise Virtual card usage is restricted at the Card Scheme (payment network) level to online (ecommerce) or Mail and Telephone Order (MOTO) transactions.

The Card Scheme (payment network) sets the BIN range for virtual cards issued by your Issuer (BIN sponsor), and further usage restrictions are applied when setting up card Usage for a virtual card. The scheme is able to differentiate a device payment and allow POS transactions for the device only.

#### Q. Why issue virtual cards?

Virtual cards allow your cardholders to transact from the moment they sign up. Additionally, single use virtual cards can be issued for increased security online as the card can be blocked by the time a fraudster can use it. Finally, a virtual card can replace a costly physical card if it is added to a digital wallet.

## Virtual Card Setup

#### Q. Can I add restrictions to how the Virtual Card can be used?

Yes, you can set up card Usage Groups, which define how and where the virtual card can be used. Card usage groups are linked to a card product or can be linked to a card using the Thredd API. See [Set up your Virtual Card Usage Groups](Virtual_Cards_Setup/Virtual_Card_Setup.htm#_Set_up_VC_Groups)

## Virtual Cards and Other Thredd Digital Products

The FAQs below provide details of other Thredd products, which shouldnât be confused with virtual cards.

#### Q. What is a Master Virtual Card (MVC)? Is it a type of Virtual Card?

No, the Master Virtual Card (MVC) is not a virtual card that is provided to a cardholder. The MVC is a card record that is restricted to loading or unloading and to card-to-card transfer. Physical card production, e-commerce transactions and ATM use are not permitted.

#### Q. Whatâs the difference between a Virtual Card and a digital wallet token?

A virtual card is a real PAN that can only be used for ecommerce or MOTO transactions. A digital wallet token is a 16 digit number that is linked to the PAN of a physical or virtual card, and can be used at most POS terminals and only by the device it appears on. For more information, see the [Tokenisation Service Guide](https://docs.thredd.ai/Tokenisation_Guide.htm).

#### Q. Is it possible to set up Tokenisation (Digital Wallets) on a Virtual Card?

Yes, provided that you have set up your card BIN range at Scheme level to support dual usage and set up your Virtual Card product to match that. The virtual card can then be tokenised and bound to a mobile device or other token device in the same way as with a normal physical card. When the token is activated, make sure your card velocity and usage groups are updated to enable usage at the locations and merchants you require.