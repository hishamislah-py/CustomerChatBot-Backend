# Glossary

This page provides a list of glossary terms used in this guide.

* 3D Secure

  3D Secure (3-domain structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This
  security feature is supported by Visa and Mastercard and is branded as âVerified by Visaâ and âMastercard SecureCodeâ respectively.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* BIN

  The Bank Identification Number (BIN) is the first six to eight numbers on a payment card, which identifies the institution that issues the card.
* Card Manufacturer

  Thredd has relationships with existing card manufacturers, who we can instruct to print your cards. We use Secure FTP (sFTP) to send the card manufacturer a generated bulk XML file containing card details. This is sent on a daily basis, or at a frequency that can be customised for your service. The card manufacturer prints the cards and sends to the cardholder.
* Card Scheme (Network)

  Card network, such as MasterCard, Visa and Discover, responsible for managing transactions over the network and for arbitration of any disputes.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* EMV

  A payment card chip standard, to ensure all EMV cards work in all EMV terminals. Derived from the names of the three payment systems that wrote it: Europay, Mastercard and Visa. See www.emvco.com for more information
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.
* Flex Card

  A Flex card works like a prepaid credit or debit card and can have multiple options for use, including online purchases. It can be used to pay for certain types of items, such as healthcare and medicines.
* Issuer (BIN Sponsor)

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme (payment network).
* Luhn check digit

  The Luhn check is a simple checksum formula used to validate a variety of identification numbers. The check digit is most often the last digit.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* Open Loop Card

  A card which can be used anywhere the card scheme (payment network) is accepted, without restrictions
* PCI Compliance

  The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major card schemes (payment networks). All Program Managers who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security/
* Primary Account Number (PAN)

  The PAN is the long number (typically 16-19 digits) that is either printed or embossed on the card.
* Private-labelled

  A card which features the program managerâs card brand only (without the Visa or Mastercard logo).
* Product Setup Form (PSF)

  The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Public Token

  The 9-digit token is a unique reference for the PAN. This is used between and clients to remove the need for clients to hold actual PANs.
* sFTP

  Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.
* Smart Client

  Smart Client is Thredd's legacy desktop application for managing your account on the Thredd Platform.
* Stand In Processing (STIP)

  The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card Issuer (BIN sponsor).
  Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date
* VPay cards

  A Single Euro Payments Area (SEPA) debit card for use in Europe, issued by Visa Europe, which uses the EMV chip and PIN system and typically does not include a magnetic stripe