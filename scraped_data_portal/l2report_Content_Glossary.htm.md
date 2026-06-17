# Glossary

This page provides a list of glossary terms used in this guide.

* Account Verification

  A type of authorisation transaction which is intended to confirm that the account is genuine and active. Account Verifications are always for a zero amount, so only appear in Authorisation messages and never in clearing messages.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Card Scheme

  Card network, such as MasterCard, Visa, or Discover, responsible for managing transactions over the network and for arbitration of any disputes.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* Discover Global Network

  The Discover Global Network consists of a group of card networks acquired by Discover that operate in different market segments:
  - Discover: A credit card with similar operating model to American Express (i.e. a âthree party modelâ where the card network is also the issuer and acquirer) that operates predominantly in the US.
  - Diners Club International: international card network aimed predominantly at corporate use cases such as Online Travel Agents and expense cards
  - Pulse: A US domestic PIN network used for debit card processing similar to Star or Accel.
* External Host Interface (EHI)

  The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.
* ICA

  The Interbank Card Association Number (ICA) is a five-digit number assigned by MasterCard to a financial institution, third-party processor or other member to identify the member in the transaction.
* Issuer

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.
* Level 2 and 3 Data

  This is data that provides extra information on a transaction over the basic information that is covered in Level 1. Level 2/3 can include information on the products and services for that transaction.
* Mastercard clearing cycle

  Mastercard provides 6-8 clearing updates during each day, with details of financial transactions that are due for settlement.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* MNE (Mastercard Networks Exchange)

  A US PIN debit network provider for opening access to US debit networks.
* PGP

  Pretty Good Privacy (PGP) is an encryption system used for both sending encrypted emails and encrypting sensitive files.
* Presentments

  Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). Also known as Clearing.
* Programme Manager

  A Thredd customer who manages a card programme. The programme manager can create branded cards, load funds and provide other card or banking services to their end customers.
* reconciliation cycle

  Thredd receive six cycles of settlement data from Mastercard.
* reconciliation date

  The system processing date associated with the settlement of funds, as provided by Mastercard.
* SAFE Reporting

  You can report fraudulent transactions to Mastercard by creating a new fraud event in Mastercom, using their SAFE reporting facility (now referred to as the Mastercard Fraud and Loss Database).
* sFTP

  Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.
* Smart Client

  Smart Client is Thredd's user interface for managing your account on the Thredd Platform. Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.
* SSL Certification

  An SSL certificate displays important information for verifying the owner of a website and encrypting web traffic with SSL/TLS, including the public key, the issuer of the certificate, and the associated subdomains.
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform
* UTC

  Coordinated Universal Time or UTC is the primary time standard by which the world regulates clocks and time.