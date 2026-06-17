# 1.9 Regulation of Card Network Participants

## 1.9.1 Regulation by Region

| Region | Description of Regulations |
| --- | --- |
| **Europe** | Regulated by the national regulator. Legislation is created by the European Central Bank (ECB). Note that individual EU member countries have their own regulators which align rules to ECB, but may have additional requirements. |
| **UK** | Regulated by the Financial Conduct Authority (FCA). |
| **Singapore** | Regulated by the Monetary Authority of Singapore (MAS). |
| **Malaysia** | Regulated by Bank Negara Malaysia (BNM) |
| **Australia** | Regulated by the Australian Prudential Regulatory Authority (APRA) |
| **New Zealand** | Regulated by the Financial Markets Authority (FMA) |
| **Hong Kong** | Regulated by the Hong Kong Monetary Authority (HKMA) |
| **Japan** | Regulated by the Financial Services Agency of Japan (FSA) |
| **Philippines** | Regulated by the Bangko Sentral ng Pilipinas (BSP) |
| **Dubai** | Regulated by the DFSA, The Independent Regulator of Financial Services |
| **Egypt** | Regulated by the Financial Regulatory Authority (FRA) |

## 1.9.2 Recent Important Areas of Legislation

Below are examples of recent areas of legislation relating to card payments.

Issuers are responsible for meeting card payment regulations. Please contact your issuer for further details.

### Open banking and cardholder security

The majority of countries and regions implement open banking legislation to protect customers.

The Second Payment Services Directive (PSD2) is a European Union Directive from the European Central Bank (ECB) which introduced some important new rules related to open banking, to enhance the security of card payments by requiring additional levels of cardholder authentication during a payment transaction. The PSD2 rules have been widely adopted across Europe and the UK. Other regions have implemented similar legislation.

Thredd systems have been enhanced to support open banking rules around card processing. For more information, see the Thredd [PSD2 and SCA Guide](https://docs.thredd.ai/PSD2_Guide.htm).

Thredd recommends you consider implementing these rules for the cards in your programme to enhance your cardholder security.

### Data Protection

The majority of countries and regions implement data protection legislation covering data privacy and security of user data, designed to ensure that customer data is only collected, stored and processed for legitimate business purposes, with the consent of the customer.

Examples of legislation include the General Data Protection Regulation (GDPR) in Europe, the Personal Data Protection Act (PDPA) in Singapore, the Privacy Act 1988 and Information Privacy Act 2014 in Australia, the Federal Law on the Protection of Personal Data in the United Arab Emirates (UAE) and the Act on the Protection of Personal Information (APPI) in Japan.

Your organisation should be compliant with data protection regulations in your country or region.

Under GDPR rules, Thredd is considered a data processor.

### Anti-Money Laundering (AML)

Anti-money laundering (AML) is a set of regulations aimed to monitor and prevent money gained in illegal ways from entering the regulated financial system. Examples of recent regulation include the Anti Money Laundering (AML 5) EU Directive, Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 in the UK and the Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (AML/CTF Act) in Australia.

Program managers and issuers accepting customer money must be able to verify the identity of the customer and their source of funds. Know your Customer (KYC) checks are a set of verification checks to identify and screen customers.

The nature of your card programme and limits associated, along with local regulations, will determine the level of KYC checks you need to do on your customers when signing them up for an account. In some cases, for example on a restricted use gift card, you may just capture information such as cardholder name, date of birth and address. For most programmes you will capture those details and verify them against different sources. For some cardholders or products, you may have to perform enhanced checks such as additional identity verification or confirming the source of their funds.

### Cryptocurrency

Issuers and program managers offering [cryptocurrency![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A digital currency in which transactions are verified and records maintained by a decentralised system using cryptography, rather than by a centralised authority.](#) solutions should be aware of the changing local regulations around cryptocurrency usage.

Cryptocurrency regulation differs per country and region. Many countries require licensing and support registration of cryptocurrency exchanges. Some countries do not consider cryptocurrency a form of legal tender[1  Australia and Japan recognise cryptocurrency as legal tender, while other countries such as Singapore consider it a form of goods and service.](#) so cardholders will not benefit from the same rights and protections as with other forms of legal tender. In Europe and the UK, you must have a licenced local entity to offer cryptocurrency. Earnings on cryptocurrency are subject to Capital Gains Tax (CGT). In some countries, such as China (excluding Hong Kong), cryptocurrency is illegal.

For more information, see <https://complyadvantage.com/insights/cryptocurrency-regulations-around-world/>.

Visa and Mastercard currently do not allow Cryptocurrency for spend on cards; such programmes may require additional review and programme approvals.

## 1.9.3 Payment Card Industry (PCI) Compliance

Topics covered: What is it? How do we get it? Who do we speak to?

The Payment Card Industry Data Security Standards Council is a global organisation that provides standards for security policies, technologies and ongoing processes that protect payment systems from breaches and theft of cardholder data. The Council was founded in 2006 by American Express, Discover, JCB International, Mastercard and Visa Inc.

The Council promotes a number of security standards, aimed to protect cardholder sensitive data:

* The **Payment Card Industry Data Security Standard (PCI DSS)** is an information security standard for organisations that handle credit cards from the major card schemes. All program managers who handle customer card data must be compliant with this standard and compliance must be validated annually[2  PCI DSS validation must be done using a qualified security assessor, approved scanning vendor or, for organisations not required to compliance report, by completing a Self-Assessment Questionnaire.](#).
* The **Payment Application Data Security Standard (PA-DSS)** is applicable to any payment applications you develop or use which store, process or transmit cardholder data and/or sensitive authentication data as part of authorisation and settlement. You should only use tested and approved applications.

For more information on the standards and requirements around protecting cardholder data, see: <https://www.pcisecuritystandards.org/pci_security/>

There are four levels of PCI compliance, which depend on the volume of transactions processed by your organisation. For example: Level One applies to organisations processing over six million transactions a year.  Level Four applies to organisations who process less than 20,000 e-commerce transactions or up to one million in-store or telephone transactions annually.

The time and costs of implementing PCI Compliance rules, together with the annual auditing costs, can be a barrier when just starting out a card programme if you do not have the business systems and processes in place to meet PCI DSS standards.

## 1.9.4 Regulatory Reporting

Issuers need to submit regular safeguarding reports (indicating the amount of cardholder money held in safeguarded accounts) and other financial reports to the regulators. For UK and European Union issuers, this format must comply with the [European Single Electronic Format (ESEF)](https://www.esma.europa.eu/policy-activities/corporate-disclosure/european-single-electronic-format) regulations.

Please confirm with your issuer or regulator in your region for details.