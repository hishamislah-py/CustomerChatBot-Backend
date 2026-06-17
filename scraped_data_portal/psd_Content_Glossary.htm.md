# Glossary

* 3D Secure

  3D Secure (3-domain structure), also known as a payer authentication, is an authentication process involving the issuerâs authentication service provider (e.g., Cardinal or Apata) to pre-authenticate the cardholder. This process happens before the Authorisation is sent by the merchant Acquirer, and the critical details from the 3D-secure response are included in the Authorisation message to enable the issuer to prove that 3D-secure authentication was obtained.
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Anonymous Transactions

  Transactions such as for prepaid gift cards where the cardholder's identify is not known
* Authentication

  This includes checks to verify the cardholder's identity, such as PIN, CVV2 and CAVV, as well as 3D Secure authentication.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Bank Identification Number (BIN)

  The Bank Identification Number (BIN) is the first six numbers on a payment card, which identifies the institution that issues the card. Visa and Mastercard are changing to an eight digit BIN from April 2022.
* Biometric Authentication

  Biometrics are body measurements and calculations related to human characteristics that are unique to each person (such as face, eyes, voice and fingerprints). Biometrics authentication is used as a form of identification and access control. In practice, this mainly happens on a payment token/DPAN such as a mobile phone, and the cardholder does biometric by the phone checking their fingerprint, before using the phone to do a contactless transaction with it.
* Card Scheme (Network)

  Card network, such as MasterCard, Visa or Discover, responsible for managing transactions over the network and for arbitration of any disputes.
* Cardholder

  Consumer or account holder who is provided with a card to enable them to make purchases.
* Cardinal Commerce

  Cardinal Commerce provide an Access Control Server (ACS) that enables support for the 3D Secure cardholder authentication scheme. Cardinal is now owned by Visa. See: https://www.cardinalcommerce.com
* Chip and PIN

  Chip and PIN is a verification method used by payment cards which comply with the EMV standard. The cardholder enters a personal identification number (PIN), typically of 4 to 6 digits in length. This number must correspond to the information stored on the chip. This improves the security of the card, since only the cardholder should know the PIN.
* European Banking Authority (EBA)

  The EBA is an independent EU Authority which works to ensure effective and consistent prudential regulation and supervision across the European banking sector.
* External Host Interface (EHI)

  The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.
* Financial PAN (FPAN)

  The PAN of the card (normally 16 digits), which the Card Scheme (Network) converts when authorisations come through to them from Acquirers on the DPAN. For more information, see the Tokenisation Service Guide.
* Fraud Rate

  The fraud rate is the percentages of transactions received by the acquirer which are identified as fraudulent.
  For example, if 10,000 transactions per day are received, and 10 of these are identified as fraudulent, the fraud rate would be 0.01.
* Hard Decline

  A transaction decline which indicates that the card was declined by the issuing bank or card processor due to the card not being valid (e.g., lost, stolen or expired). It indicates to the merchant that they should not retry the transaction on the card.
* Issuer (BIN Sponsor)

  The card issuer or BIN sponsor is a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant Card Scheme.
* Mail and Telephone Order (MOTO)

  Transaction where payment instruction is taken over the telephone or via a mail order. Since the cardholder is not present, these are classed as "Cardholder Not Present" transactions.
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. MCCs are used by credit card issuers to identify the type of business in which a merchant is engaged.
* One-Leg-Out transactions

  Occurs when one of the payment service providers (either the payer or payee) is outside the European Union (EU). If the Acquirer is from outside the EU and the payer is from the EU, the Acquirer does not need to comply with PSD2 regulations
* Online PIN

  With online PIN, the PIN is encrypted and verified online by the card issuer. This is in contrast to offline PIN, where the PIN is verified offline by the EMV chip card.
* Original Credit Transactions (OCT)

  Transaction that can be used to send funds to a card-based account, resulting in a credit of funds to the cardholder's account.
* Payment Services Directive 2 (PSD2)

  PSD2 is an EU Directive which sets requirements for firms that provide payment services. It introduces a number of requirements around how firms treat their customers and handle their complaints, and the data they must report to the FCA.
* Point of Sale (POS) Terminal

  A hardware device for processing card payments at retail stores. The device has embedded software that is used to read the cardâs magnetic strip data.
* Primary Account Number (PAN)

  The cardâs 16-digit permanent account number (PAN) that is typically embossed on a physical card.
* Product Setup Form (PSF)

  The Product Setup Form is a spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.
* Program Manager

  A Thredd customer who manages a card program. The Program Manager can create branded cards, load funds and provide other card or banking services to their end customers.
* Recurring Transaction

  Recurring transactions are multiple transactions processed at predetermined intervals, representing an agreement between a customer and a merchant to take payments over a period of time. Typically, SCA is performed on the first transaction, while subsquent transactions are treated as cardholder not present and not subject to SCA.
* Soft Decline

  A Soft Decline is a decline response to the terminal or online merchant, indicating that the transaction failed due to being non-SCA. The transaction should be re-attempted with SCA. This may include (for card present transactions) requesting that the terminal authenticates the cardholder using PIN.
* Strong Customer Authentication (SCA)

  Type of cardholder authentication process where the cardholder is authenticated using a combination of at least two of the following tests: Possession (something the cardholder has), Knowledge (something the cardholder knows) and something they are (such as a fingerprint, face recognition or voice recognition).
* Usage Group

  Group that controls where a card can be used. For example: POS or ATM. For more information, see the Web Services Guide.
* Wallet Provider

  These are providers such as Apple, Android (Google), Samsung etc. who supply the payment apps (also known as Mobile Wallet token requestors).