# General FAQs

This section provides answers to frequently asked questions.

## Types of Reports

#### What type of reports does Thredd provide?

Thredd provides the following reports to Program Managers:

* Clearing Reports and Non-Clearing Reports for transactions
* Balance reports

For Issuers (BIN sponsors) and Self-Issuers, Thredd provides two additional reports:  
 â¢ Fee Collection Report  
 â¢ Quarterly Management Report (QMR)   
For details, please contact your implementation manager or account manager

#### Can I configure the details provided in each report?

No, the Thredd reports are standard. If you require bespoke reports, please speak to your account manager.

#### How often are reports provided? Can I change this?

The Thredd reports are provided daily. For specific details regarding report timing, please speak to your account manager.

For more frequent transaction information, we recommend you use the [External Host Interface (EHI)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) which provides transaction reporting in real-time.

#### How are reports provided to customers?

The daily reports are provided via [sFTP![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). This is on a push only basis.

#### How often do you change the fields in the report?

Thredd will add new fields to the report in line with updates from the Card Schemes (payment network) or to reflect other changes relevant to the payments industry or our service. Currently the payment networks are Visa and Mastercard.

When we make changes to the reports, we will update the technical documentation and notify you of the change.

#### Are reports encrypted?

Yes. Reports are encrypted using the PGP standard.

#### How do I identify the version of the report?

The XML schema version is listed in the comments section of the schema, together with details of what has changed. See [Balance Report XML Schema](Reference/Balance_XML_Schema.htm). We currently do not provide the XML version within the XML report.

#### How large is a typical report?

This is based on the number of your transactions and can be anything from 1Kb to 2GB. We will split up anything larger than 2GB into smaller files: eg., *filename.001*, *filenename.002* and so on.

#### Do you store reports and if so, for how long?

Reports are stored for up to 2 calendar days on the sFTP server, after which they are deleted from the sFTP server. We keep an archive of historical files for a limited period. For access to historical files, please raise a JIRA request.

#### How can I use the reports?

You can use them to do the following:

* Update to your card balance/transaction database
* For card balance/transaction reconciliation purposes

#### Why is there a difference between the balance reported in the balance XML file and that in Smart Client?

For balance XML reports, a primary card shares the balance with secondary cards. In these scenarios, Thredd shows the combined balance of the primary card and all of its secondary cards. However, in Smart Client, a cardâs balance is its own balance only. This means Smart Client does not include the balance of any linked secondary cards.

For example, reported balance on a primary card:

* In Balance XML file: EUR 10,245.55
* In Smart Client: EUR 10,176.55
* Discrepancy: EUR 69.00

The difference of 69 EUR is the balance of the secondary token.

This behaviour does not apply to Thredd portal as Thredd portal can share the balance between Primary and Secondary cards.