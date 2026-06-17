# 1 Introduction

## 1.1 What is the Discover Network?

The Discover Global Network is dedicated to enabling millions of businesses to expand their customer base through seamless global payments.

The Discover Global Network consists of a group of card networks acquired by Discover that operate in different market segments:

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Discover: A credit card with similar operating model to American Express (i.e. a âthree party modelâ where the card network is also the issuer and acquirer) that operates predominantly in the US. | Diners Club International: international card network aimed predominantly at corporate use cases such as Online Travel Agents and expense cards | Pulse: A US domestic PIN network used for debit card processing similar to Star or Accel. |

The Discover Global Network stands out by offering benefits rooted in operational efficiency and network reach. It is the third largest payments network globally, expanding its footprint through strategic partnerships with regional card networks like RuPay in India, UnionPay in China, JCB in Japan, BC Card in South Korea, and others.

### 1.1.1 Key Features and Benefits

* Grow your business and attract new cardholders by becoming an issuer for Diners ClubÂ®
* Extend your reach. Accept 305M+ global cardholders. Open your business to more cardholders from more parts of the world ready to spend
* Tap into one of the fastest growing global payments networks with 25+ Network Alliances

* Access to a wider network reach, enhanced commerce experiences, and the ability to leverage Discover's expertise and capabilities.
* This connection allows domestic operators to expand their reach beyond their territories, avoid reinventing the wheel, and quickly implement new services by leveraging Discover's assets and solutions
* Discover's expertise and capabilities, stemming from acquisitions like Diners Club International, offer issuers the foundation for international acceptance footprints, enabling them to grow exponentially through global partnerships

* Discover offers a combined fee structure that is generally lower than other networks.
* Discover's offers cardholders a no annual fee policy, 24/7 customer service, and Cashback Bonus program

## 1.2 Threddâs Integration to Discover

Thredd is integrated to the Discover Global Network as an issuer-processor. Phase 1 of the integration provides card issuance with Diners Club International. The rollout will be multi-phased starting with Discover Virtual Cards and Tokenisation (Mobile Wallet) in selected markets.

### 1.2.1 Current Supported Services

Refer to the section below for details of Thredd products and services currently supported on Discover networks:

#### Supported for Phase 1

* Virtual cards (from valid Account Ranges: BIN ranges starting with â36â and PAN lengths of 14 digits)
* Diners Club International Network across all platform instances
* Standard transaction processing: Authorisation, Clearing and Chargebacks
* Transaction XML reports
* Fees Module: Authorisation fees (recurring and web-services are not included)
* Disallow MCC list
* Web Services

Only six digit BINs will be used/ validated

Discover will only be tested on Threddâs on-premise environment (PRD0)

#### Not supported for Phase 1

* Physical Cards
* Tokenisation
* QR Payments via Single Message
* Integration to other parts of the Discover Global Network:

### 1.2.2 Discover Network Considerations

You must set up a separate commercial agreement with the Discover Card Scheme (Network).

You must obtain a separate Issuer Identification Code (IIC) from Discover for each issuer and issuer settlement currency you support.

You must have a bank account in each settlement currency you support, opened within two months of IIC registration.

Visa and Mastercard BINs are referred to as Cycle Ranges in Discover.

#### Completing Issuer Documentation

Please contact your Discover representative for further information.

Your Thredd implementation manager will support you when completing the Discover Network documentation.