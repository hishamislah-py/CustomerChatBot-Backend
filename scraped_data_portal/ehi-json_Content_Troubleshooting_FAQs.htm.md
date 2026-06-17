# Troubleshooting FAQs

This section provides answers to common integration queries.

## System timeouts and connection issues

#### Q.How can I identify if a transaction has been timed out and view details of the response time?

You can view details in [Thredd Portal![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or in [Smart Client![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#): In the **View Transactions** screen, double-click the declined transaction.

The **Response Status (DE039)** field indicates "*92 - Unable to route*". The **difference (in Milliseconds)** field shows the response time.

#### Q. Why is the Thredd default timeout set to its current level and should I request a change for my program?

The default Thredd limit for a timeout is set to its current level to avoid potential network timeouts by the card scheme (Visa/Mastercard/Discover) as well as to reduce delays for the cardholder which may result in them abandoning their purchase. Each card scheme has different timeout rules. For details, check with your Implementation Manager. The Thredd timeout limit takes into account the full, end-to-end transaction round trip, which involves several parties and systems, each of which take a portion of the available time. See the figure below.

![](Resources/Images/EHI-transaction-flow-overview.png)

Figure 21: Parties involved in transaction authorisation

For suggestions as to how you can reduce response timeouts, see below.

#### Q. How can I reduce the number of response timeouts (where my external host does not respond within the allowed time period)?

The default permitted response time (see [EHI Configuration Options](Getting_Started/EHI_Configuration_Options.htm)) is the full round-trip time, including your processing and routing, between Thredd and your external host.

Factors that could impact on your response time include your system processing time and the network transport time. Below are some suggestions as to how you can improve your external host response times and avoid response timeouts during real-time authorisation requests:

* Make sure you have an appropriate level of monitoring and logging on your systems so that you can quickly identify potential issues affecting your service.
* Where response delays are due to slow processing on your systems, consider upgrading your hardware, software or processing logic. As a general rule, you should be processing a message and returning a decision as quickly as possible, in order to enable sufficient time for the message to pass over the network. Your system design should also take into account future traffic loads as your service grows.
* Implement a separate endpoint for your Cut-off messages (to reduce traffic going into your main data feed).
* We recommend you provide Thredd with IP addresses for your external host endpoints and do not use a DNS as this can create potential additional lookup traffic overhead prior to the authorisation being sent.
* It may be possible to request a higher limit for much longer geographical (e.g.,intercontinental) distances from the Thredd data centres. (**Note**: any permanent higher timeouts may be chargeable.)
* If you are experiencing occasional timeouts, consider moving to Gateway Processing with STIP (mode 4), where Thredd can provide the approve or decline decision for an authorisation request in the event that your external host system does not respond with the timeout limit. See [EHI Operating Modes](Getting_Started/EHI_operating_modes.htm).
* If you are experiencing consistent timeouts, try confirm the days and times when this occurs. This may help identify a possible cause.
* Consider the time it takes to connect to any external third party services you are using for your authorisation decisions, such as fraud screening and foreign exchange (FX) conversion services.
* If you are using an older version of EHI, you can reduce the number of connection timeouts by upgrading to a later version. See [Upgrading your EHI Version.](Getting_Started/Version_Control.htm#Upgradin)
* If you have high traffic volumes, you should consider requesting a dedicated session for your authorisation traffic (set up between the card scheme and Thredd). Thredd will need to negotiate this with the card scheme (Visa/Mastercard). For details, check with your Implementation Manager.

## Transactions and Matching

#### Q. I am receiving an unexpectedly high volume of repeat messages per day via EHI

This could be due to a number of reasons:

* Check that the message format of your external response matches the EHI specifications. An invalidly formatted response may result in the response message being rejected and the original advice or authorisation request message being resent to your external host.
* Make sure you remove the namespace from the response as this causes EHI to resend the messages.
* Ensure you are acknowledging all Thredd messages with a value of `acknowledge` = 1. See [Processing EHI Transactions](Requirements/Processing_EHI_Transactions.htm).
* If you do not acknowledge messages within the permitted period, this will result in EHI resending messages. This may be due to your systems processing and responded to messages slowly. See [How can I reduce the number of response timeouts?](#Q.)
* At times of peak traffic load, consider prioritising messages that require real-time decision-making, such as authorisations.

#### Q. How can I ensure the card balance is always correctly updated?

For Gateway and Cooperative Processing (modes 1, 2 and 4) where you maintain the balance, Thredd does not match advices received from the card networks; we will pass the advice through to your external host system. When you receive an advice for an approved authorisation, you should block the funds and match the subsequent presentment using appropriate matching criteria; see [Transaction Matching](Requirements/Transaction_Matching.htm).

For Full Service Processing (mode 3), since Thredd maintains the balance, Thredd matches transactions and updates the balance on your behalf.

In some circumstances, the card schemes may perform [Stand-In processing![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) on our behalf and approve an authorisation request (e.g.,where the Thredd system is unavailable and or does not respond in time). In these circumstances Thredd does not block the approved amount on the card. Once we receive the presentment, we will create an authorisation advice and send this to you, along with the presentment advice.

#### Q. How can I prevent a card balance going into negative on a card?

In certain circumstances, such as for offline transactions or where Thredd or the card scheme performs [Stand-In processing![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The card network (Visa and Mastercard) may perform approve or decline a transaction authorisation request on behalf of the card issuer.
Depending on your Thredd mode, Thredd may also provide STIP on your behalf, where your systems are unavailable.](#) this may potentially result in the card not having sufficient funds available to cover the presentment, and therefore going into a negative balance. Other examples include late presentments or where merchants send in a presentment for a declined transaction.

When Thredd receive a presentment from the merchant, we will always take the money from the card (Full Service Processing - mode 3). If you receive a presentment, you must update the balance (Gateway and Cooperative Processing - modes 1, 2 and 4). You cannot decline a presentment. If the original transaction was declined and you subsequently receive a presentment, you may have the right to a [chargeback![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Where a cardholder disputes a transaction on their account and is unable to resolve directly with the merchant, they can raise a chargeback with their card issuer. The chargeback must be for a legitimate reason, such as goods and services not received, faulty goods, or a fraudulent transaction.](#). If a late presentment is received after the original authorisation block has expired, this could result in the card going into a negative balance. In this case you *may* have the right to a chargeback.

You cannot fully prevent a card going into a negative balance. To mitigate the risks, Thredd recommends you consider the following options:

* Prevent offline transactions. This option is recommended for prepaid cards. However, note that this will also reduce the available merchant locations where the card can be used.
* Reduce the need for stand-in authorisation processing by ensuring your external host system is able to respond to authorisation requests in a timely manner.
* Consider implementing an automated reminder notification to cardholders to top up when their card balance is running low. The terms and conditions of your service may allow you to implement a service charge or a standing order instruction that debits the cardholder's linked account to cover any negative card balances.

#### Q. I cannot match the Acquirer reference in linked messages

The `Trans_link` field provides a reference which can be used to match different types of linked authorisation and financial messages; this reference contains acquirer reference data, such as the *Acquirer Reference Number (ARN)* and *Acquirer Bank Identification Number (BIN)*.

For Mastercard transactions the acquirer reference data is unique and should always match across transactions. For Visa transactions, this data may not be unique and `traceid_lifecycle` can be used as an alternative for transaction matching. In general, the  `traceid_lifecycle` field is a good field to use for matching transactions across the transaction lifecyle, as the value of this field should be identical for all messages relating to the same transaction.

Other EHI fields which contain acquirer reference data that can be used for matching include:

* `Acquirer_Reference_Data_031` â contains the Acquirer Reference Number (ARN) used for clearing messages only.
* `Acquirer_id_DE32` â the Acquiring Bank Identification Number as assigned by the network.
* `Acquirer_Forwarder_ID` â the ID of the Acquiring institution forwarding a Request or Advice message.

For more information on transaction matching criteria, see [Transaction Matching](#Transact).

In most cases, the Acquirer reference data for Authorisation and Financial messages and any linked transactions (e.g., reversals) should be the same. However, some acquirers may not follow the standard processing rules, which could result in Acquirer reference data values that are not the same in linked messages. In this case, you should contact the acquirer for clarification.

#### Q. What's the difference between the processing codes 01, 12 and 17?

The `Proc_Code` for 01, 12 and 17 are based on information received from the card scheme networks. See below for details.

On Mastercard networks:

| Processing Code | Type of Transaction | Mastercard Product | MCC |
| --- | --- | --- | --- |
| 01 | ATM cash withdrawals | All Mastercard cards | 6011 |
| 01 | Manual [cash disbursementsClosed Type of transaction where cash is given to the cardholder, for example, from a bank branch by a member of staff using a Point of Sale (POS) terminal.](#) - Authorisation transactions | Maestro cards only | 6010 |
| 12 | Manual cash disbursements - Clearing transactions | All Mastercard cards | 6010 |
| 17 | Manual cash disbursements - Authorisation transactions | Mastercard Credit, Cirrus and Mastercard Debit. | 6010 |

On Visa networks:

| Processing Code | Type of Transaction | Visa Product | MCC |
| --- | --- | --- | --- |
| 01 | ATM cash withdrawals | All Visa cards | 6011 |
| 01 | Manual cash disbursements - Authorisation and Clearing transactions | All Visa cards | 6010 |
| 12 | Not used |  |  |
| 17 | Not used |  |  |

#### Q. How to handle processing errors due to invalid characters?

Thredd receives data in the authorisation messages from the Card Scheme/Acquirer, which occasionally contains fields that have been populated with unrecognised hexadecimal characters. The inclusion of such characters is typically within String fields of type AN or ANS, such as `<Merch_Name_DE43>`, `<Txn_Desc>`, `<MCC_Desc>`, `<Merch_ID_DE42>`, `<Network_Transaction_ID>`,`<Merch_City>`, `<GPS_POS_Capability>` and `<GPS_POS_Data>`.

The Thredd Platform is able to successfully process data in these fields, irrespective of special character formats.

During conversion in EHI to the JSON format, data is encoded according to the JSON specification.

Where the converter does not recognise a character, this results in character substitution in the field, based on the conversion standard. You can find several examples below.

Substitution Examples

| Hexadecimal character | Description | Converted to in JSON | Example: Original 0100 Message | Example: Conversion to JSON Format |
| --- | --- | --- | --- | --- |
| 20 | space | \u0000 | <GPS\_POS\_Data>              </GPS\_POS\_Data> | "GPS\_POS\_Data": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000000",  "GPS\_POS\_Capability": "\u0000\u0000 \u0000\u0000\u0000\u0000\u0000\u0000\u0000", |

Your systems should be able to handle such invalid characters (for example, by using regular expressions to blank out or convert the invalid characters).

## Known Issues

For a list of known issues, please contact your Implementation Manager.