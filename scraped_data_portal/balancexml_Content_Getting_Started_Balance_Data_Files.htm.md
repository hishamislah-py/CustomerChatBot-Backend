# 1.2 Balance Data Files

Thredd can supply you with daily Balance XML Report files at preset times. The balance is the amount on the card at the point when the report is generated daily (usually shortly after
midday), and includes non-working days and holidays. The generation job can take up to two hours. Balance data arrives around 5pm UK time, but this can be configured to align with your chosen cut-off time. Thredd sends Balance XML Report files through sFTP.

Thredd deletes the sFTP files from the sFTP server after two calendar days. The files are stored on Thredd's archive server for a limited period. Bear in mind that if you need to keep transaction records over time, you must follow the right business processes for maintaining the records.

For an example of a Balance XML Report file, see [Balance XML Example.](../Reference/Balance_XML_Example.htm)

## 1.2.1 File Contents

Thredd provides one Balance Report XML file per Program Manager daily.

The Balance XML file contains a snapshot of balances from the previous day, which is either the:

* Cut off of card balance up to midnight UK time from the previous day or the equivalent local midnight cut-off time in your country (if your program has the  `balance xml at midnight` setting enabled in [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop for managing your account on the Thredd Thredd Platform. Smart Client is installed as a desktop application and requires a secure connection to Thredd systems in order to be able to access your account.](#)).[1 The XMLCutoffUTCtime setting allows you to set the equivalent local midnight cut-off time in your country, if this differs from the UK time. This setting only applies if the BalanceXmlAtMidnight flag is also turned on.](#)
* Balance at the moment the XML is generated, usually around 3:30pm to 6pm UK time, depending on the import of presentment data.

### Example 1: Midnight Setting Turned Off

On the Saturday 2nd Jan 2023, a file named *GPS-PPPPbalexp20230101.P1.xml* is generated at 5pm, which contains a snapshot of balances as at the report creation time of 5pm on Saturday.

![](../Resources/Images/Balance_xml.png "Balance XML reporting Schedule")

Figure 2: Balance File Reporting Schedule and Filename

### Example 2: Midnight Setting Turned On

On the Saturday 2nd Jan 2023, a file named *GPS-PPPPbalexp20230101.P1.xml* is generated at 5pm, which contains a snapshot of balances as at midnight on Friday.

### Example 3: Midnight Setting Turned On (Australia)

On the Saturday 2nd Jan 2023, a file named *GPS-PPPPbalexp20230101.P1.xml* is generated at 3am local Australian time. This file contains a snapshot of balances as at midnight Friday UK time (10am on Saturday Australian time).

### Card Scheme Considerations

If you want the Balance XML Reports to include Visa and Mastercard transactions, you need to consider the clearing cycles for these card schemes. The clearing cycles can influence the time of day Thredd sends the balance files.

| Scheme | Cycle Description |
| --- | --- |
| Mastercard | Mastercard has 6 clearing cycles per day, seven days per week. Mastercard sends Thredd the clearing files, which contain the settlement data.  Thredd processes all 8 cycles before generating the Balance XML Report with clearing data.  Data from cycles 5-8 from the night before and 1-4 from current day form the aggregate data of a settlement day for most regions. The cycles contain all the information you need to reconcile your settlements with Mastercard.  For Asia-Pacific clients, Thredd processes cycles 2-8 for the previous day and cycle 1 from the current day, and includes them in the daily Balance XML Report. |
| Visa | Visa provides two files, Domestic and International, each day with different timings for some regions (for example, Australia and Hong Kong).  There is a maximum filesize where, for the largest clients, it is possible that more than one Domestic and/or International file is received on the same day. [2 Visa Domestic cycle starts at 9am and the International cycle begins at mid-day. Both cycles happen 7-days a week.](#)  After processing the files from the card schemes, Thredd creates the Balance XML Report file and sends it to you. |
| Discover | Clearing occurs once per day. |

## 1.2.2 File Naming Convention

The uses the following naming convention:

#### On-Premise Customers (P0)

`GPS-PPPPbalexpYYYYMMDD.xml`

#### Thredd Cloud (P1 and P2)

`GPS-PPPPbalexpYYYYMMDD.Pn.xml`

Where:

* PPP= The 3-10 letter XML file prefix set up for your programme.
* YYYY= Year (4 digits)
* MM = Month (2 digits)
* DD = Day (2 digits)
* Pn = Production environment (2 digits), such as P1and P2

For example:

`GPS-NWCtxnexp20230131.P1.xml`

The production environment variable applies to customers in one of Thredd's AWS Cloud-based production environments (P1 and P2), and does not apply to existing customers in our UK data centre production environment (P0). For details of which production environment is relevant to your programme, check with your implementation manager or account manager.

## 1.2.3 Encryption and Encoding

XML files are encrypted using [Pretty Good Privacy,![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An encryption program that provides cryptographic privacy and authentication for data communication.](#) where keys are shared. For details, contact your implementation manager.

All of the XML data files are well-formed XML (UTF-8 encoded).

As XML is case-sensitive, you should follow the correct casing for all XML elements and attribute names when processing the message.