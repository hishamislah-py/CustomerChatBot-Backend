# PSD2 & Strong Customer Authentication

The [Second Payment Services Directive![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is an EU Directive which sets requirements for firms that provide payment services. It introduces a number of requirements around how firms treat their customers and handle their complaints, and the data they must report to the FCA.](#) (PSD2), is an European Union (EU) Directive which sets requirements for firms that provide payment services. It aims to improve consumer protection, make payments safer and more secure. PSD2 came into force on 13th January 2018, with some individual countries within the EU having extensions until 2022[1 According to the Financial Conduct Authority (FCA), the deadline for enforcing PSD2 SCA requirements in the UK was extended to March 14, 2022.](#). PSD2 introduced some new requirements for card issuers and processors, such as:

* The requirement for [Strong Customer Authentication (SCA)](#Strong) on all e-commerce and contactless payments unless specific exemptions apply.
* The requirement for [[Dynamic SCA Linking](#PSD2)](#PSD2) - verifying that the details in an authentication session match the details in the subsequent payment authorisation

PSD2 rules are issued by the [European Banking Authority (EBA)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The EBA is an independent EU Authority which works to ensure effective and consistent prudential regulation and supervision across the European banking sector.](#).

## Strong Customer Authentication (SCA)

The EBA states that for a transaction to be Strong Customer Authenticated (SCA), at least two of the following must be verified during the transaction:

* Cardholder must be identified by some characteristic unique to them (e.g. fingerprint, iris scans)
* Cardholder must know something only they should know (e.g. PIN, phone unlock code)
* Cardholder must possess something (e.g. chip card, mobile phone)[2 The SCA possession test must be made with dynamic data, for example, using the EMV ARQC (Authorisation ReQuest Cryptogram), to prove the cardholder has the card. Using the magnetic stripe, for example, is not proof of possession.](#)

Thredd currently considers all 3D Secure transactions as SCA[3 We can optionally set your programme so that Thredd only considers 3DS transactions as SCA if the cardholder was challenged.](#). If the 3D Secure transaction is considered as SCA, Thredd automatically flags the possession and knowledge tests in the EHI `GPS_POS_Data` field. See [PSD2 Transaction Status](PSD2_Status.htm).

## PSD2 Dynamic Linking

PSD2 Dynamic SCA Linking requires that the details provided in a [3D Secure![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) 3D Secure (3-domain structure), also known as a payer authentication, is an authentication process involving the issuerâs authentication service provider (e.g., Cardinal or Apata) to pre-authenticate the cardholder. This process happens before the Authorisation is sent by the merchant Acquirer, and the critical details from the 3D-secure response are included in the Authorisation message to enable the issuer to prove that 3D-secure authentication was obtained.](#) authentication session matches the details that were provided during the transaction authorisation. For example, matching of the authorised amount to the authenticated amount, and matching of the merchant name.

Thredd can do this matching. Alternatively, you can perform matching using details provided in transaction messages sent from the Thredd [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) to your systems. For more information, see the [EHI Guide > Transaction Matching - Authentications and Authorisations](https://docs.thredd.ai/ehi/Content/Appendices/Transaction_Matching_Guidelines.htm).

## SCA Exemptions

All transactions must have [Strong Customer Authentication (SCA)](#Strong), unless they meet one of the following European Banking Authority (EBA) exemptions:

| Article | Description of SCA Exemption |
| --- | --- |
| Article 11 | Contactless transaction of up to EUR 50.00, and cumulatively not exceeding EUR 150.00 or 5 transactions. |
| Article 12 | Paying a transport or parking fare at an unattended terminal. |
| Article 13 | The receiver of funds is a trusted beneficiary, or this is a recurring payment transaction (but not the first instance of). |
| Article 14 | The sender and receiver of funds are the same person. |
| Article 15 | E-commerce transaction of up to EUR 30.00, and cumulatively not exceeding EUR 100.00 or 5 transactions. |
| Article 16 | E-commerce transaction classified as low-risk (as defined in the Article). |

The specific transaction limits (i.e., frequency and amount) may vary per country. Please check with your Issuer or country financial regulator for details. These limits can be set at your Thredd card Product level. See [PSD2 Product Settings](PSD2_Settings.htm).

## Transactions where the PSD2 rules do not apply

The PSD2 rules do not apply to the following types of transactions:

* The [Issuer (BIN Sponsor)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer or BIN sponsor is a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant Card Scheme.](#) or [Acquirer![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The merchant acquirer or bank that offers the merchant a trading account, to enable the merchant to take payments in store or online from cardholders.](#) is outside the EBA's jurisdiction (i.e., outside the EEA or UK):

  + The Issuing BIN range is outside the EEAor UK (your BIN range will be exempt unless you specifically request including in SCA checks)
  + The Acquirer is outside the EEA or UK
* Credit transactions - where money is paid into the card
* Transactions to create a payment token[4 The payment token setup already has approve-with-authentication, which meets the EBA's requirement.](#)
* Mail Order or Telephone Order transactions[5 The EBA is of the view that anything initiated via paper or telephone is out of the scope of SCA under PSD2.](#)
* The message from Visa/Mastercard does not count as a transaction in EBA's definition. Examples:

  + Account Verification Requests / Account Status Enquiry requests
  + Merchant tokenisation (digital wallet) requests

To understand the end-to-end transaction flow and Thredd checks related to PSD2, see [PSD2 Transaction Checks](PSD2_Transaction_Flow.htm).

## Find out more about the PSD2 Regulations

Below are links to additional information about the PSD2 and SCA regulations.

* [EBA website: Regulatory Technical Standards on strong customer authentication and secure communication under PSD2](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money/regulatory-technical-standards-on-strong-customer-authentication-and-secure-communication-under-psd2)
* [FCA website (UK only):
  Deadline extension for Strong Customer Authentication](https://www.fca.org.uk/news/statements/deadline-extension-strong-customer-authentication)