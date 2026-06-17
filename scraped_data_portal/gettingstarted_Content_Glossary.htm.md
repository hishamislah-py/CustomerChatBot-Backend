# Glossary

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
* Card Scheme

  Card network, such as MasterCard, Visa or Discover, responsible for managing transactions over the network and for arbitration of any disputes.
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* EMV

  EMV is an acronymn for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.
* Hanging Filter

  The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth.
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
* Offline Transaction

  This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
  The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card balance is not authorised in real-time, there is a risk that the card may not have the amount required to cover the transaction.
* Partial Amount Approval

  Some acquirers support a partial amount approval for Debit or Prepaid payment authorisation requests. The issuer can respond with an approval amount less than the requested amount. The cardholder then needs to pay the remainder using another form of tender.
* Pavement Testing

  End-to-end testing of the cardholder journey using real cards that have been issued, which takes place before a service is rolled-out to customers.
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Secure Connectivity Framework

  Threddâs Secure Connectivity Framework
  is the combination of several components which enable secure access to Threddâs resources, using a common identity store.
* sFTP

  Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
  Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.
* Smart Client

  Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.
* Stand In Processing (STIP)

  The card network (Visa, Mastercard or Discover) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
  Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.
* Thredd Portal

  Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.
* Triple DES

  Triple DES (3DES or TDES), is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block to produce a more secure encryption.
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date
* VROL System

  Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.