# General FAQs

This section provides answers to frequently asked questions.

## Types of Reports

#### What type of reports does Thredd provide?

Thredd provides the following reports to Program Managers:

* Clearing Report (transaction data)
* Non-Clearing Report (transaction data)
* UTC Balance reports

For Issuers and Self-Issuers, Thredd provides two additional reports:  
 â¢ Fee Collection Report  
 â¢ Quarterly Management Report (QMR)   
For details, please contact your implementation manager or account manager.

#### When does Thredd send the reports?

As part of the Global Transaction Reporting capability, Thredd can send the reports at the local time you require.

#### Can I configure the details provided in each report?

No, you cannot configure the Thredd reports. If you require bespoke reports, please speak to your Account Manager.

## Delivery of Reports

#### How often are reports provided? Can I change this?

Thredd provides the Non-Clearing Report once a day. You can configure the sending of the Clearing Report, where Thredd can send a report up to 6 times a day, following each clearing file Thredd receives from the card schemes.

#### How are reports provided to customers?

Thredd provide daily reports to customers via [sFTP![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). This is on a push only basis.

#### How often do you change the fields in the report?

Thredd adds new fields to the report in line with updates from the card schemes (Visa and Mastercard), or to reflect other changes relevant to the payments industry or Thredd's service.

When making changes to the reports, Thredd updates the technical documentation and notifies you of the change.

#### What report file formats are available?

Thredd currently supports XML and Comma Separated Variable (CSV) formats.

#### Are reports encrypted?

Yes. Thredd encrypts reports using the PGP standard.

#### How do I identify the version of the report?

The XML schema version is listed in the comments section of the schema, together with details of what has changed.

#### How large is a typical report?

The size is based on the number of your transactions and can be anything from 1KB to 2GB. Thredd splits up anything larger than 2GB into smaller files, for example,, *filename.001*, *filenename.002* and *filename.003*.

#### Do you store reports and if so, for how long?

Thredd stores reports for up to 2 calendar days on the sFTP server, after which they are deleted from the server. Thredd archives the historical files for a limited period. For access to historical files, please raise a JIRA request.

## Using the Reports

#### How can I use the reports?

You can use reports to do the following:

* Update your transactions database.
* Manage the transaction reconciliation.