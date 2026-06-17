# Glossary

This page provides a list of glossary terms used in this guide.

* 3D Secure

  3D Secure (3-domain structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as âVerified by Visa/Visa Secureâ and âMastercard SecureCode/Mastercard Identity Checkâ respectively.
* Account Funding Transaction (AFT)

  Card Scheme transaction to debit funds from a card account. It is used to "pull" funds from a card account in order to fund a real-time "push" OCT to a different account, which can be either the cardholder's or another person's account.
* Account Status Inquiry (ASI)

  A standard message type which allows the merchant to check the Card Validation Code (CVC) and, if address details are provided, to optionally use the Address Verification Service (AVS). If these checks are successful Thredd responds with an 00 approval to the merchant. They normally then submit a second transaction, but with an actual transaction amount included.
* Account Verification

  A type of authorisation transaction which is intended to confirm that the account is genuine and active. Account Verifications are always for a zero amount, so only appear in Authorisation messages and never in clearing messages.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Adjustment Credits

  Indicates a Credit adjustment.
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Authorisation Reversal

  An authorisation reversal occurs when a merchant wants to reverse a previously submitted authorisation request (e.g., because the authorised amount was entered incorrectly or the customer cancelled the order). The authorisation reversal normally occurs very soon after the original authorisation and can be matched to the original authorisation using the traceid\_lifecycle.
* Automated Fuel Dispenser (AFD)

  Automatic fuel dispensers (AFDs) are used at petrol or gas stations for customer self-service fuel payments. Typically the customer inserts their card and enters a PIN number and the AFD authorises a fixed amount (e.g. Â£99).
  Once the final payment amount is known, the AFD may reverse the authorisation and/or request a second authorisation.
* Card Scheme

  Card network, such as MasterCard or Visa, responsible for managing transactions over the network and for arbitration of any disputes.
* Cards API

  The Thredd Cards API is a new REST-based API which can be used to connect to the Thredd system in place of using the traditional Thredd SOAP-based Web Services. The REST API provides messages in JSON format. If you are interested in the Cards API, please contact your Account Manager.
* Cash Disbursement

  Type of transaction where cash is given to the cardholder, for example, from a bank branch by a member of staff using a Point of Sale (POS) terminal.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* Credits (for deposit)

  Credit transaction for deposit. Not supported in Dual Message System networks.
* Credits (for Payment Transaction)

  Mastercard-specific Money Send transaction.
* Debit Adjustments

  May be received for non-card money transfers (out), manual/one-off balance adjustments or additional fees.
* EMV

  EMV originally stood for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* EMV 3D Secure

  EMV 3-D Secure (3DS) is a new 3D Secure specification that supports app-based authentication and integration with digital wallets, as well as traditional browser-based e-commerce transactions. See: https://www.emvco.com/emv-technologies/3d-secure/
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.
* Financial Reversal

  A financial reversal occurs when the acquirer cancels all or part of a prior transaction (which may be a purchase, refund, cashback, cash, PIN change, or any other transaction type).
  For example, if the acquirer has already taken the funds and are aware of a processing error (e.g., double charging), they can submit an 1240 Financial Reversal.
* Form Factor

  A payment device's physical design features which define the size, shape and other physical specifications of the device.
* Hanging Filter

  The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.
* Incremental Authorisation

  A request for an additional amount on a prior authorisation. An incremental authorisation is used when the final amount for a transaction is greater than the amount of the original authorisation.
  For example, a hotel guest might register for one night, but then decide to extend the reservation for additional night. In that case, an incremental authorisation might be performed in order to get approval for additional charges pertaining to the second night.
* Issuer

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.
* JSON

  JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attributeâvalue pairs and arrays.
* Mastercard Debit Switch (MDS)

  This is a Single Message System at Mastercard for sending online financial messages (e.g., 0200). It includes transactions from Mastercard, Cirrus and Maestro cards. Thredd supports processing messages from this system.
* Mastercard Network Exchange

  Enables smaller networks to use Mastercard as a routing platform for payments. Can also be referred to as MNEX or MNGS.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* MIP

  Mastercard Interface Processor (MIP)
  The processing hardware and software system that interfaces with Mastercard's Global Payment System communications network.
* Offline Transaction

  This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
  The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card is not checked in realtime, there is a risk that the card may not have the amount required to cover the transaction.
* Online Financial Message

  In Single Message Systems operated in some regions (such as the US and some Asia Pacific countries), the card scheme sends realtime financial messages for payment authorisations. Examples of online financial messages include: Online Financial Request, Online Financial Advice and Online Financial Reversal.
* Original Credit Transaction (OCT)

  Card Scheme transaction to credit funds to a card account. It can be used to send or "push" funds to an eligible card account, resulting in a real-time credit of funds to the cardholder's account.
* Original Credits

  Visa-specific Money Send transaction. Also called an Original Credit Transaction (OCT).
* Partial Amount Approval

  Some acquirers support a partial amount approval for Debit or Prepaid payment authorisation requests. The issuer can respond with an approval amount less than the requested amount. The cardholder then needs to pay the remainder using another form of tender.
* Payments Service Directive Two (PSD2)

  PSD2 is a European regulation for payment services that has the purpose of making payments more secure in Europe. It introduces legislation to improve the payment service authentication process.
* Presentment

  Stage in a transaction where the funds authorised on a card are captured (deducted from the cardholderâs account). See also Clearing. Also referred to as the First presentment.
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Quasi-Cash

  Visa-specific quasi-cash transaction. This is used for specific merchants where the purchased items could be converted to cash (e.g., gaming chips, money orders). Identified by the (11xxxx) processing code.
* Refund

  A refund transaction occurs when a merchant refunds a customer part or all of a previously purchased item. Refunds are standalone transactions that have their own lifecycle (financial message and possibly authorisation message). The refunds may be linked with a previous purchase or not, as there is no strict linking requirement for refunds against previous purchases.
* sFTP

  Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.
* Smart Client

  Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.
* SOAP

  SOAP (Simple Object Access Protocol) SOAP is a messaging protocol for exchanging structured information. It uses Extensible Markup Language (XML) for its message format and relies on application layer protocols such as HTTP for message negotiation and transmission. SOAP allows developers to invoke processes running on disparate operating systems (such as Windows, macOS, and Linux) to authenticate, authorise and communicate using XML.
* SSL Certification

  An SSL certificate displays important information for verifying the owner of a website and encrypting web traffic with SSL/TLS, including the public key, the issuer of the certificate, and the associated subdomains.
* Stand In Processing (STIP)

  The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
  Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.
* Strong Customer Authentication (SCA)

  When the cardholder is authenticated during a payment transaction using a combination of at least two of the following authentication methods: Knowledge (Something the cardholder knows, such as a password), Possession (Something the cardholder has access to, such as a phone number or email account) and Biometrics (such as a fingerprint, face or voice)
  Under the Payment Service Directive 2 (PSD2), strong customer authentication is required on all cardholder-initiated transactions when both the card issuer and acquirer are within the European Economic Area (EEA).
* Tag-Length-Value (TLV)

  TLV is an encoding scheme. A TLV-encoded record contains the record type (tag), followed by record Length, and finally the Value itself. Example:
  0104John
  where:
  tag type = 01 (first name)
  tag length = 4 digits
  tag value = John
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.
* Triple DES

  Triple DES (3DES or TDES), is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block to produce a more secure encryption.
* Unique Transaction (requires unique MCC)

  Mastercard-specific transaction category. Similar to Visa's quasi-cash, this is used for specific merchants where the purchased items could be converted to cash (e.g., gaming chips, money orders). Identified by the (18xxxx) processing code.
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date
* Visa DPS

  This is a processing network for US issuers, where messages are processing based on Single Message System flow. Thredd supports messages from this system.
* VROL System

  Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.