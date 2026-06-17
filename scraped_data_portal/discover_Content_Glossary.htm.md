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
* Automated Fuel Dispenser (AFD)

  Automatic fuel dispensers (AFDs) are used at petrol or gas stations for customer self-service fuel payments. Typically the customer inserts their card and enters a PIN number and the AFD authorises a fixed amount (e.g. Â£99).
  Once the final payment amount is known, the AFD may reverse the authorisation and/or request a second authorisation.
* Card Scheme (network)

  Card network, such as MasterCard, Visa or Discover, responsible for managing transactions over the network and for arbitration of any disputes.
* Card Transaction System (CTS)

  The Card Transaction System (CTS) enables you to test the integration of your card processing systems and validate the setup of your External Host Interface (EHI).
* Cards API

  The Thredd Cards API is a new REST-based API which can be used to connect to the Thredd system in place of using the traditional Thredd SOAP-based Web Services. The REST API provides messages in JSON format. If you are interested in the Cards API, please contact your Account Manager.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* Discover Global Network (DGN)

  The Discover Global Network consists of a group of card networks acquired by Discover. This includes: Discover, Diners Club International and Pulse.
* EMV

  EMV originally stood for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* EMV 3D Secure

  EMV 3-D Secure (3DS) is a new 3D Secure specification that supports app-based authentication and integration with digital wallets, as well as traditional browser-based e-commerce transactions. See: https://www.emvco.com/emv-technologies/3d-secure/
* External Host

  The external system to which sends real-time transaction-related data. The URL to this system is configured within per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and web service API fees.
* Form Factor

  A payment device's physical design features which define the size, shape and other physical specifications of the device.
* Hanging Filter

  The period of time during which waits for an approved authorisation amount to be settled. This is defined at a product level. A typical default is 7 days for an auth and 10 days for a pre-auth.
* IIC

  Issuer/Aquirer Institution Identification Code (IIC). A unique 11-digit code to designate a specific Institution.
* IIN

  Issuer Identification Number, a field in the ISO/IEC 7812 specification for ID cards.
  The first six or eight digits, including the major industry identifier, compose the issuer identifier number (IIN) which identifies the issuing organization. The IIN is sometimes referred to as a "bank identification number" (BIN). The IIN's use is much broader than identification of a bank. IINs are used by companies other than banks.
* Incremental Authorisation

  A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation.
  For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.
* Issuer (BIN Sponsor)

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* MIP

  Mastercard Interface Processor (MIP)
  The processing hardware and software system that interfaces with Mastercard's Global Payment System communications network.
* Network Reference ID

  The Network Reference ID is a numeric ID generated by DCI and remains unchanged for the life of the Card Transaction.
* Network Reference ID (NRID)

  The Network Reference ID is a numeric ID generated by DCI and remains unchanged for the life of the Card Transaction.
* Offline Transaction

  This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by vending machines, commuting and transport networks).
  The card chip and terminal determine if the offline transaction is permitted under EMV/Scheme rules; if not supported, the terminal declines the transaction. Note: Since the balance on the card balance is not authorised in real-time, there is a risk that the card may not have the amount required to cover the transaction.
* Partial Amount Approval

  Some acquirers support a partial amount approval for Debit or Prepaid payment authorisation requests. The issuer can respond with an approval amount less than the requested amount. The cardholder then needs to pay the remainder using another form of tender.
* Payments Service Directive Two (PSD2)

  PSD2 is a European regulation for payment services that has the purpose of making payments more secure in Europe. It introduces legislation to improve the payment service authentication process.
* PGP

  Pretty Good Privacy (PGP) is an encryption system used for both sending encrypted emails and encrypting sensitive files.
* Presentment

  Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment.
* Program Manager

  A customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Secure Payment Confirmation (SPC)

  SPC allows the issuer to directly authenticate the customer via FIDO (Fast IDentity Online) biometric authentication during a 3D Secure Challenge scenario.
* sFTP

  Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.
* Smart Client

  Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.
* SSL Certification

  An SSL certificate displays important information for verifying the owner of a website and encrypting web traffic with SSL/TLS, including the public key, the issuer of the certificate, and the associated subdomains.
* Stand In Processing (STIP)

  The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
  Depending on your mode, may also provide STIP on your behalf, where your systems are unavailable.
* Tag-Length-Value (TLV)

  TLV is an encoding scheme. A TLV-encoded record contains the record type (tag), followed by record Length, and finally the Value itself. Example: 0104John where: tag type = 01 (first name) tag length = 4 digits tag value = John
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.
* Triple DES

  Triple DES (3DES or TDES), is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block to produce a more secure encryption.
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date
* VROL System

  Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.
* WebAuthn

  WebAuthn is a web standard developed by W3C and FIDO Alliance, allowing the use of biometrics and other authenticators for secure user verification during a 3D Secure Challenge authentication scenario.