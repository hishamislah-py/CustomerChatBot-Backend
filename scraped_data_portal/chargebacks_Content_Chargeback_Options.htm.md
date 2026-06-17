# 3 Chargeback Options

There are two options available for managing your chargebacks.

## 3.1 Option 1: Using the Scheme UI

If you are a card issuer, or you are a Thredd Program Manager who has been provided access via your card issuer, you can use the Mastercard and Visa online systems to raise chargebacks and manage the dispute processes.

* Mastercard offer the Mastercom Claims Manager
* Visa offer the Claims Resolution Visa system, which we refer to as the Visa Resolution Online (VROL) platform

  These systems require you to be fully PCI DSS compliant, as full PAN is used. Chargeback details will be available in XML messages.

##### Notes on using Mastercom Claims Manager

* When you are onboarded to Mastercom Claims Manager, to reduce the need to raise a chargeback claim, you can opt in for their [collaboration option](Overview.htm#_Notes). This is enabled by Mastercom.
* Thredd provide options to automatically credit the chargeback amount to the cardholder if the chargeback is accepted. In addition, it can also be configured not to apply a debit if a second presentment is received. This is configured at Thredd product level. For details, contact your Thredd account manager.

##### Notes on using the Visa VROL platform

* Visa clients can use VROL to raise a chargeback. After a chargeback is raised in VROL, Thredd obtains the clearing files and processes the chargeback in the Thredd Platform and you can view the chargeback details in Smart Client's **Chargeback** screen.

## 3.2 Option 2: Using Thredd Smart Client

If you do not have access to the Mastercard or Visa systems or are unable or prefer not to use full PAN, Thredd provides a backend integration into these systems to enable receipt of chargeback files, when chargebacks are raised and responded to. You can view chargeback transactions directly in Smart Client (the Thredd application for managing your account).

For Mastercard transactions (currently Europe/UK only), you can raise and respond to chargebacks directly in Smart Client. Support for Visa and additional Mastercard jurisdictions are being added.

##### How to Implement

You must complete the following prerequisites before the Smart Client Chargeback service can be enabled:

* Please contact your issuer to request they enable Thredd to use the Mastercom API data feed for your BIN codes.
* Costs for the service must be agreed with your Thredd account manager and added as an addendum to your Thredd contract.