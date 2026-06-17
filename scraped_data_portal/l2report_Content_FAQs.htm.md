# General FAQs

This section provides answers to frequently asked questions.

## Types of Reports

#### What is a Level 2 and 3 report?

A Level 2 and 3 report includes specific product and services data that are associated with day-to-day transactions. The reports enable commercial card customers to share product and services data from the card schemes. For example, the data can include information on a specific leg of a trip for customers that used their commercial card for their journey.

#### What type of reports does Thredd provide?

Thredd provides the following reports to Program Managers:

* Clearing Report (transaction data)
* Non-Clearing Report (transaction data)
* Enhanced reports containing Level 2 and 3 data
* Balance reports

For Issuers and Self-Issuers, Thredd provides three additional reports:  
 â¢ Fee Collection Report  
 â¢ Quarterly Management Report (QMR)   
 â¢ Monthly Report (Discover only)   
For details, please contact your implementation manager or account manager.

#### When does Thredd send the reports?

As part of the Global Transaction Reporting capability, Thredd can send the reports at the local time you require.

#### Can I configure the details provided?

No, you cannot configure the Thredd reports. If you require bespoke reports, please speak to your Account Manager.

## Delivery of Reports

#### How often are reports provided? Can I change this?

By default, Thredd provides the Level 2 and 3 report once a day. You can configure the sending of the report, where Thredd can send a report up to 6 times a day, following each clearing file Thredd receives from the card schemes.

#### How are reports provided to customers?

Thredd provide daily reports to customers via [sFTP![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). This is on a push only basis.

#### How often do you change the fields in the report?

Thredd adds new fields to the report in line with updates from the card schemes (Visa, Mastercard, and Discover), or to reflect other changes relevant to the payments industry or Thredd's service.

When making changes to the reports, Thredd updates the technical documentation and notifies you of the change.

#### Are reports encrypted?

Yes. Thredd encrypts reports using the PGP standard.

#### How do I identify the version of the report?

The XML schema version is listed in the comments section of the schema, together with details of what has changed.

#### What determines the Level 2 and 3 information?

Level 2 and 3 information is determined by details that Thredd has on those transactions where there is scheme-specific data on products and services

#### Do you store reports and if so, for how long?

Thredd stores reports for up to 2 calendar days on the sFTP server, after which they are deleted from the server. Thredd archives the historical files for a limited period. For access to historical files, please raise a JIRA request.

## Using the Reports

#### How can I use the reports?

You can use the reports to do the following:

* Update your transactions database.
* Manage the transaction reconciliation.