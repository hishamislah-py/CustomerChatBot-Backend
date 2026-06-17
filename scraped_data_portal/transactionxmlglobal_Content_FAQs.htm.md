# General FAQs

This section provides answers to frequently asked questions.

## XML Reports

#### What type of XML reports does Thredd provide?

Thredd provides the following reports to Programme Managers:

* Transaction XML report
* Balance XML report

For Issuers and Self-Issuers, Thredd provides two additional reports:  
 â¢ Fee Collection Report  
 â¢ Quarterly Management Report (QMR)   
For details, please contact your implementation manager or account manager.

#### Can I configure the details provided in each report?

No, the Thredd reports are standard. If you require bespoke reports, please speak to your account manager.

#### How often are reports provided? Can I change this?

The Thredd reports are provided daily. For specific details regarding report timing, please speak to your account manager.

For more frequent transaction information, we recommend you use the [External Host Interface (EHI)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) which provides transaction reporting in real-time.

#### How are reports provided to customers?

The daily XML reports are sent to you via [sFTP![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol (FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). This is on a push only basis.

#### How often do you change the fields in the report?

Thredd will add new fields to the report in line with updates from the card schemes (Visa and Mastercard) or to reflect other changes relevant to the payments industry or our service.

When we make changes to the XML reports, we will update the technical documentation and notify you of the change.

#### Are reports encrypted?

Yes. Reports are encrypted using the PGP standard.

#### How do I identify the version of the XML report?

The XML schema version is listed in the comments section of the schema, together with details of what has changed. See [Transaction XML Schema](Reference/Transaction_XML_Schema.htm). We currently do not provide the XML version within the XML report.

#### How large is a typical report?

This is based on the number of your transactions and can be anything from 1Kb to 2GB. We will split up anything larger than 2GB into smaller files: eg., *filename.001*, *filenename.002* and so on.

#### Why does the size of a report attribute appear to exceed its limit?

When receiving a report, the size of an attribute may be larger than the expected limit. For example, the location attribute in an NCLR file may be longer than the 64 character limit. The field may also show malformed XML as a result.

This is because the report contains characters in XML that are reserved, for example, the *&* character, and that your XML parser has not decoded the character to its original value. To ensure that an XML file can be parsed with the correct field length containing the decoded representation of characters. client systems need to be able to decode these reserved characters through correct parsing and validation.

#### Do you store reports and if so, for how long?

Reports are stored for up to 2 calendar days on the sFTP server, after which they are deleted from the sFTP server. We keep an archive of historical files for a limited period . For access to historical files, please raise a JIRA request.

#### How can I use the XML reports?

You can use them to do the following:

* Update to your transactions database
* For transaction reconciliation purposes