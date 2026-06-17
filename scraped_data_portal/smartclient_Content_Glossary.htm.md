# Glossary

This page provides a list of glossary terms used in this guide.

* 3D Secure (3DS)

  3D Secure is a technical standard adding an extra layer of security to payment transactions over the Internet (eCommerce)
* AccBal

  Account Balance
* ACN

  Activation Code Notification (340000)
* Acquirer

  The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.
* Act Bal

  Actual Balance
* AFD

  Automated Fuel Dispenser
* AID

  Acquiring Institution Identification Code
* API

  Application Programming Interface
* APW

  Mastercard Automated Parameter Worksheet
* ARQC

  Authorisation Request Cryptogram
* Authentication

  This includes checks to confirm the cardholder identity, such as PIN, CVV2 and CAVV.
* Authorisation

  Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.
* Automated Fuel Dispenser (AFD)

  Automatic fuel dispensers (AFDs) are used at petrol or gas stations for customer self-service fuel payments. Typically the customer inserts their card and enters a PIN number and the AFD authorises a fixed amount (e.g. Â£99).
  Once the final payment amount is known, the AFD may reverse the authorisation and/or request a second authorisation.
* AvlBal

  Available Balance
* AVS

  Address Verification Service
* Base Currency

  Typically considered the domestic currency or accounting currency for the card
* Bill Amt

  Billing Amount
* Billing Currency

  The currency you choose to be billed in
* BIN

  Bank Identification Number (First 6 digits of the 16-digit PAN)
* BlkAmt

  Blocked Amount
* Card Scheme

  Card network, such as MasterCard, Visa or Discover, responsible for managing transactions over the network and for arbitration of any disputes
* Cardholder

  Consumer or account holder who is provided with a card to enable them to make purchases
* Case filing

  A feature through which an issuer or an acquirer can raise a concern with Mastercard.
* CAVV

  Cardholder Authentication Verification Value
* CB

  Chargeback
* Chargeback

  Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.
* CIQ

  Visa Client Implementation Questionnaire
* Clearing File/Clearing Transaction

  Thredd receive batch clearing files from the card networks, containing clearing transactions, such as presentments and network fees. The card issuer transfers the requested settlement amount to the acquirer and 'clears' the amount on the card, reducing the available card balance accordingly.
* CRI

  Card Request Interface
* CS

  Customer Support
* CVC

  Card Validation Code
* DCC

  Dynamic Currency Conversion
* DE000-DE999

  Data Element (000-999) number. For full details of each element, see the card scheme customer interface specification manual
* DGN

  Discover Global Network, which consists of Discover, Diners Club International, and Pulse.
* Discover (DGN)

  Discover Global Network, which consists of Discover, Diners Club International, and Pulse.
* DPAN

  Device Primary Account Number
* EHI

  External Host Interface
* EMV

  EMV originally stood for "Europay, Mastercard, and Visa", the three companies which created the standard. EMV cards are smart cards, also called chip cards, integrated circuit cards, or IC cards which store their data on integrated circuit chips, in addition to magnetic stripes for backward compatibility.
* External Host

  The external system to which Thredd sends real-time transaction-related data. The URL to this system is configured within Thredd per programme or product.
  The Program Manager uses their external host system to hold details of the balance on the cards in their programme and perform transaction-related services, such as payment authorisation, transaction matching and reconciliation.
* F Fee

  Fixed fee
* Fee Groups

  Groups which control the card transaction authorisation fees, and other fees, such as recurring fees and Thredd web service API fees.
* FID

  Forwarding Institution Identification Code
* FPAN

  Funding Primary Account Number
* FX

  Foreign Exchange
* FX Market

  The currency market in which the FX Provider operates, such as London or the US. Currencycloud only operate in the one market
* FX Provider

  The currency conversion rate provider, such as Currencycloud
* FxPdg

  Foreign Exchange Padding â padding for currency conversion, to compensate for any fluctuations in currency exchange rates between the authorisation and the presentment
* Hanging authorisation filter

  The period of time during which Thredd waits for an approved authorisation amount to be settled. This is defined at a Thredd product level. A typical default is 7 days for an auth and 10 days for a pre-auth. For more information, see the External Host Interface Guide.
* Issuer (BIN Sponsor)

  The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.
* Mastercom

  Create and manage dispute claims in Mastercom
* MCC

  Merchant Category Code â The type of merchant
* MCC Pdg

  Merchant Category Code Padding â padding for particular merchants who do the pre-authorisations
* MDES

  Mastercard Digital Enablement Service
* Merchant

  The shop or store providing a product or service that the cardholder is purchasing. A merchant must have a merchant account, provided by their acquirer, in order to trade. Physical stores use a terminal or card reader to request authorisation for transactions. Online sites provide an online shopping basket and use a payment service provider to process their payments.
* Merchant Category Code (MCC)

  A unique identifier of the merchant, to identity the type of account provided to them by their acquirer.
* MFX

  Multi-Currency Card
* MultiFX

  A Thredd feature for seamless currency conversion. MultiFX lets customers hold different balances in different currencies simultaneously in one wallet
* MVC

  Master Virtual Card
* Offline Transaction

  This is often used in scenarios where the merchant terminal is not required to request authorisation from the card issuer (for example for certain low risk, small value transactions used by airlines and transport networks).
  The card CHIP EMV determines if the offline transaction is permitted; if not supported, the terminal declines the transaction. Note: Since the balance on the card balance is not authorised in real-time, there is a risk that the card may not have the amount required to cover the transaction.
* OTP

  One Time Passcode/ Activation code sent to the cardholder for use in authenticating
* PAN

  Primary Account Number
* PM

  Program Manager
* POS

  Point of Sale
* POSFX

  A Thredd feature which makes spending abroad easy with realtime and transparent point-of-sale FX rates
* Presentment

  The payment has been financed and taken by the merchant bank
* Program Manager

  A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.
* R Fee

  Rate fee â Fee based on the transaction amount
* SC

  Smart Client (Card Processor Front End)
* Secure Connectivity Framework

  Threddâs Secure Connectivity Framework is the combination of several components which enable secure access to Threddâs resources, using a common identity store.
* Smart Client

  Smart Client is Thredd's user interface for managing your account on the Thredd Platform. Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.
* STAN

  System Trace Audit Number
* Stand In Processing (STIP)

  The card network may perform approve or decline a transaction authorisation request on behalf of the card issuer.
  Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.
* TAR

  Token Authentication Request (330000)
* TCcy

  Transaction Currency
* TCN

  Tokenisation Complete Notification (TCN) - 350000
* TEN

  Token Event Notification (TEN) - 360000
* Token

  The obfuscated 16 or 9-digit Card Number
* Triple DES

  Triple DES (3DES or TDES), is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block to produce a more secure encryption.
* TxAmt

  Transaction Amount
* Txn

  Transaction
* Validation

  Checks to confirm the card is valid, such as CHIP cryptograms, mag-stripe data (if available) and expiry date
* VDEP

  Visa's Digital Enablement Program
* VROL System

  Visa Dispute Resolution Online system, provided by Visa for managing transaction disputes.