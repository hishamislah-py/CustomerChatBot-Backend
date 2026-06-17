# 1 Introduction

The Cardholder report can be run in two modes:

* **Daily Report**: Shows cardholder details for new cards issued between the current date and the previous day, plus any cards which have had their status changed on the current report date or previous day; if there has been no new issued cards or cards with a status change, a report with empty fields is returned.
* **Weekly Report**: Shows all issued card cardholder details except cards changed to an irreversible status (Stolen, Destroyed) more than 7 days ago.

This report is currently not available to new customers. For more information, please contact our Operations team at occ@thredd.com

## 1.1 File Naming Conventions

By default, cardholder files have the following naming convention:

### 1.1.1 On-Premise Customers (P0)

`GPS-ISSUERcardholderYYYYMMDD.xml`

### 1.1.2 ThreddCloud (P1 and P2)

`GPS-ISSUERcardholderYYYYMMDD.Pn.xml`

Where:

* `ISSUER`: Is the [Issuer (BIN Sponsor)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme.](#)/[Program Manager![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) name as held by Thredd
* `YYYY`: Is the four digits of the year
* `MM`: Is the two digits of the month
* `DD`: Is the two digits of the day
* `Pn` = production environment (2 digits), such as P1 and P2. (Not applicable to customers in our UK data centre production environment)

### 1.1.3 Example

`GPS-IDTcardholder20240322.P1.xml`

The production environment variable is relevant to customers in one of our AWS Cloud-based production environments (P1 and P2) and does not apply to exisiting customers in our UK data centre production environment (P0). For details of which production environment applies to your programme, please check with your Thredd implementation manager or account manager.

## 1.2 Encoding / Type

Data files are well formed XML (UTF-8 encoded).