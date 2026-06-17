# 1 Introduction

The [Mastercard Fraud and Loss Database![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Mastercard repository of fraud transactions submitted by issuers. It is used for reporting, monitoring, and combating card fraud. Previously know as: System to Avoid Fraud Effectively (SAFE).](#) (previously System to Avoid Fraud Effectively (SAFE)) is a Mastercard repository of fraud transactions submitted by [issuers![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The card issuer, typically a financial organisation authorised to issue cards. The issuer has a direct relationship with the relevant card scheme. For more information, see the Key Concepts Guide.](#). It is used for reporting, monitoring, and combating card fraud.

Mastercard requires issuers to report to the Fraud and Loss Database at the customer ID level all Mastercard transactions that the issuer considers to be fraudulent, even if the corresponding accounts are not closed or marked as fraud.

For issuers, Fraud and Loss Database reporting can be accessed directly via Mastercard Connect.

For other Thredd customers, Thredd provides an option on Smart Client to enable you to easily report a transaction as fraud to Mastercard. Thredd sends a message to MasterCom using the MasterCom API.

## 1.1 MasterCom API

The [MasterCom API![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Mastercom API offers Mastercard customers the ability to create and manage dispute claims in Mastercom. Mastercom is a system for dispute management. All activities for any given dispute can be tracked within a single claim using Mastercom, including Retrieval Request and Fulfilment, First Chargeback, Second Presentment, Fraud reporting, Case Filing, and Fee Collection requests. All activities for any given dispute throughout its lifecycle can be tracked within a single claim.](#) offers Mastercard customers the ability to create and manage fraud reports in MasterCom. MasterCom is a system for dispute management and fraud reporting.

The MasterCom API is available to Program Managers and card issuers. Thredd provides an interface to MasterCom via Smart Client, which means you do not need to develop your own MasterCom API integration. You need to opt in for the service with Thredd. Please contact Thredd Operations via JIRA.

This service is only available in the MasterCom Europe/UK region. If you want access for another region, please contact both Mastercard and Thredd to request this.