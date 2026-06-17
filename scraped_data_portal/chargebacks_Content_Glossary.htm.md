# Glossary

This page provides a list of glossary terms used in this guide.

* 3D Secure (3DS)

  3 Domain Secure is a cardholder authentication scheme provided by the card schemes, which is used to verify the identity of a cardholder during an online transaction. The cardholder typically enters a password or authenticated by submitting a passcode from their mobile device.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Arbitration

  Process of managing disputes raised between merchants and cardholders, where the dispute cannot be resolved. The arbitration process is managed by the card scheme, who will make the final decision.
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Card Scheme (Network)

  Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.
* Cardholder

  Consumer or account holder who is provided with a card to enable them to make purchases.
* Case Filing

  A feature through which an issuer or an acquirer can raise a concern with Mastercard.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* EHI

  The Thredd External Host Interface (EHI) is a system which provides Program Managers with real-time transactional data and control over their transaction authorisations.
* EMV

  EMV originally stood for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.
* Issuer (BIN Sponsor)

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.
* Mastercard Network Exchange (MNE)

  Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* Out-of-band (OOB) authentication

  A type of two-factor authentication that requires a secondary verification method through a separate communication channel along with the typical ID and password.
* PCI DSS

  The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major card schemes. All merchants who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/
* Presentment

  Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment.
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Representment

  Process of responding to a chargeback raised by an issuer, where the acquirer or merchant do not agree with the chargeback and wish to dispute it via the card scheme.
* Second presentment

  When a merchant resubmits the transaction with evidence to counter the chargeback.
* Smart Client

  Smart Client is Thredd's user interface for managing your account on the Thredd Platform.
  Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.