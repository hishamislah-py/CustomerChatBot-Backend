# 2 Managing Change

Your integration journey does not stop once you go live. You will need to provide resources to handle issues, manage system changes and enhancements, and add new features and services to your card program.

## 2.1 Dealing with Issues

For clarification of system functionality or information provided to you during the implementation phase, please contact your Thredd implementation manager.

For persistent issues affecting a live service and for change requests, please raise a JIRA ticket.

## 2.2 System Changes

Thredd provides [Pre-Release Notifications (PRNs)](https://docs.thredd.ai/GPSPRN.htm) to inform you of any system changes that may affect your service. Advance notification is provided 4-6 weeks in advance.

Depending on the type of change, we may not notify you via the PRN process (e.g., where you do not need to change your systems). For example, External Host Interface (EHI) field value updates.

### 2.2.1 Regulatory and Scheme Changes

Thredd will implement mandatory financial services regulations and card scheme mandates.

Regulatory changes affecting financial services and payments are region and country specific. For example, the European union issue directives which all financial firms operating in the European Union must follow, such as the [Second Payment Services Directive (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Threddâs Secure Connectivity Framework
is the combination of several components which enable secure access to Threddâs resources, using a common identity store.](#). The UK and other countries may enact specific local regulations relating to payment processing in their country. Thredd will endeavour to update our systems where required to comply with these regulations and provide you with advance warning.

Visa and Mastercard operate a 6-month Business Enhancement Release process (with major releases in April and October). Changes are communicated to Thredd and issuers via Mastercard *Announcement Notification (ANs)* and Visa *Articles*.

We will notify you of these changes, where they affect our systems, via our PRN process. Some changes require that you also update your system and processes.

### 2.2.2 Adding New Features

Thredd adopts an agile development process, with four builds and one planned release per month. These changes include regular patches, fixes and enhancements to our systems, software and infrastructure.

Where a change impacts on your service or requires you to update your systems, we will notify you of these changes via our PRN process.

#### Best implementation practise

* EHI changes can be implemented without breaking your systems if you program your systems to ignore new fields.
* To support changes to web services fields, your development team should provide a service architecture that supports quick updates.

## 2.3 Product Upgrades

Thredd recommends that you to start with a basic setup and add additional Thredd products and services after your service is live. Examples of additional products that can be integrated include 3D Secure, Tokenisation (Digital Wallet programmes such as MDES or VDEP) and Fraud Transaction Monitoring.

### 2.3.1 Configuration Upgrades

For any configuration changes to your setup post-live, please raise a Jira request or discuss with your Account Manager.

### 2.3.2 Integrating new Products

If you are interested in integrating additional Thredd products, please contact your Account Manager to discuss.

Your Account Manager will provide details of any related product fees and send you an addendum to your Thredd contract for you to sign.

The new project is assigned to an Implementation Manager, who can set up your product on the Thredd system and provide you with further details of the timescales and integration steps.

### 2.3.3 EHI Version Upgrades

You can upgrade to the latest version of EHI to receive the latest EHI fields. Upgrades may require some development work on your systems in order to process the new fields. Please contact your Account Manager to discuss.