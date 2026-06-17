# Glossary

This page provides a list of glossary terms used in this guide.

* Account Status Information (ASI) Service

  A standard message type which allows the merchant to check the Card Validation Code (CVC) and, if address details are provided, to optionally use the Address Verification Service (AVS). If these checks are successful Thredd responds with an 00 approval to the merchant. They normally then submit a second transaction, but with an actual transaction amount included.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Address Verification Service (AVS)

  An AVS check compares the billing address used in the transaction with the issuing bankâs address information on file for that cardholder. Depending on whether they match fully, partially, or not at all, the merchant can use that information in their decision on whether or not to accept or cancel the order. AVS is one of the most widely used fraud prevention tools in card-not-present transactions.
* API Usage Fees Group

  The API Usage Fee group defines a fee that is charged to a card on a per transaction basis for a card transaction via Thredd API (typically reflecting a payment or transfer into the card account or balance enquiry, but could be used for card renewal, replacement, lost and stolen, admin fees, and so on).
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Authorisation Fees Group

  The Authorisation Fees group defines fees that are charged to a card on a per transaction basis when the card is used (e.g., at an ATM, website or merchant terminal) or when a payment is made out of the account.
* Card Scheme (Network)

  Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.
* Card Validation Code (CVC)

  The Card Verification Code, or CVC, is an extra code printed on a debit or credit card. With most cards (Visa, Mastercard) it is the final three digits of the number printed on the signature strip on the reverse of the card.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* EMV

  EMV is an acronymn for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* External Host Interface (EHI)

  External Host Interface. This is a Thredd product providing clients either a real time feed or the ability to be involved in authorisations.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd API usage fees.
* Fee Type

  A card usage fee type that defines the fees that are applied to a specific type of transaction, such as a debit card payment or an ATM withdrawal. A Fee Group will consist of one or more fee types.
* Issuer (BIN Sponsor)

  Financial organisation and scheme member, licensed by the scheme to issue cards and process transactions using the schemeâs network.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* PAN

  The cardâs 16-digit primary account number (PAN) that is typically embossed on a physical card.
* Point Of Sale (POS) Terminal

  A hardware device for processing card payments at retail stores. The device has embedded software that is used to read the cardâs magnetic strip data.
* Presentment

  Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment. For more information, see the External Host Interface Guide.
* Product Setup Form (PSF)

  A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Recurring Fees Group

  The Recurring Fees group defines fees that are charged to a card on a recurring basis (e.g., monthly, annually or over a defined period).
* Smart Client

  Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.
* Stand In Processing (STIP)

  The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
  Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date