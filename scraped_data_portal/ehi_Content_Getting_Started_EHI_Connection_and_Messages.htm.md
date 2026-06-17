# 1.4 EHI Connection and Messages

The External Host Interface messaging system is based on SOAP Version 1.1.

SOAP (Simple Object Access Protocol) is a messaging protocol for exchanging structured information. It uses Extensible Markup Language (XML) for its message format and relies on application layer protocols such as HTTP for message negotiation and transmission. SOAP allows developers to invoke processes running on disparate operating systems (such as Windows, macOS, and Linux) to authenticate, authorise and communicate using XML.

See the figure below, illustrating the Thredd system components and typical message flow.

![](../Resources/Images/External_Host_auth.png "External Host Interface Architecture")

Figure 6: Thredd System Components and External Host Interface Message Flow

Below is a generic summary of this process, which may differ depending on your EHI mode. For more information, see [EHI Operating Modes](EHI_operating_modes.htm).

1. The card scheme (Visa or Mastercard) sends real-time payment [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) requests, as well as batch clearing file and financial transaction notifications to Thredd.
2. The Thredd Message Processing System (MPS) performs authentication, validation, velocity controls, fraud protection and product configuration checks.
3. The EHI server sends the card transaction requests and any financial notifications to the external host URL endpoint configured for your programme.
4. Depending on your EHI mode, Thredd may be involved in the card transaction approval decision. For example, in EHI mode 1 (Gateway Processing), mode 4 (Gateway Processing with STIP) the external host (i.e., Program Manager's systems) decides whether to approve or decline the transaction, by checking details of the balance held on the card. In EHI mode 3 (Full Service Processing) Thredd makes the approval decision.
5. The EHI server waits for an approve or decline response or a financial message acknowledgement from the external host. When received, this is processed. Card transaction decline or approve responses are forwarded to the card scheme.
6. Where Thredd maintains the balance on the card, the Program Manager can perform load and unload transactions via the Thredd web services, to update the balance (for details, refer to the *Web Services Guide*).
7. In addition to the real-time data feed, Thredd also provides a daily batch XML transactional data feed via [sFTP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Secure File Transfer Protocol. File Transfer Protocol FTP) is a popular unencrypted method of transferring files between two remote systems. SFTP (SSH File
   Transfer Protocol, or Secure File Transfer Protocol) is a separate protocol packaged with SSH that works in a similar way but over a secure connection.](#). You can use this data to support your payment reconciliation process.

Due to the real-time nature of authorisation or online financial requests, in EHI modes where your systems need to process the request, they must respond within the configured time limit for a request (see [EHI Configuration Options](EHI_Configuration_Options.htm)) or the transaction will be declined.

## 1.4.1 Types of EHI Messages

EHI sends the following types of messages to the external host (Program Manager's systems):

* **Real-time authorisation** **requests** - which require an immediate approve or decline decision and response. If not responded to in time, Thredd or the Card Scheme may provide Stand-In Processing (STIP)
* **Real-time reversal requests** - which require an immediate acknowledgement
* **Real-time advices** - which require an immediate acknowledgement (e.g, authorisation advices)
* **Financial notifications** - such as presentments and chargebacks. These require an acknowledgement. An additional response status is optional.
* **Cut off messages** (optional) - batch report showing all messages you should have received in a defined period. See [Cut Off Messages](../Requirements/Cut_Off_Messages.htm).

For most message types, EHI waits for an acknowledgement from the external host to confirm that the message has been received. If no response is received, EHI resends the message. See [Processing EHI Transactions](../Requirements/Processing_EHI_Transactions.htm).

For details of the fields included in each type of transaction, see [EHI Data Feeds](EHI_Data_Feeds.htm).

## 1.4.2 GetTransaction WSDL

The Thredd GetTransaction WSDL defines the structure of the Thredd SOAP message sent to the external host and the structure of the response expected to be returned by the external host. The message format is based largely on the [ISO 8583 standard](https://en.wikipedia.org/wiki/ISO_8583), with some differences which are unique to Thredd.

For details and exampes of GetMessages for different types of transactions, see [GetTransaction WSDL and Example Messages](../WSDL/GetTransaction_WSDL.htm).

## 1.4.3 Transmission Control Protocol (TCP) Connection

For each message sent via the EHI, the following occurs:

1. The EHI makes a TCP connection to the external host URL configured for your program.  Thredd is always the TCP client, the external host (your system) is always the TCP server.
2. Using the HTTP POST method, EHI sends an HTTP message to this TCP connection with the SOAP XML message as the message body. The message body is XML encoded to the UTF-8 format.  See <https://www.w3.org/TR/REC-xml> for specifications.
3. The response from your system must be a valid HTTP response with the HTTP response body containing the valid XML response data.
4. In the production environment EHI uses Thredd's Trust Framework, which leverages the **Mutual Transport Layer** (**mTLS**) protocol. .

## 1.4.4 mTLS Connection

EHI uses Thredd's Secure Connectivity Framework, which leverages the **Mutual Transport Layer** (**mTLS**) protocol. You will need to set up your mTLS termination point to validate the mTLS Transport Certificates. For more information, see the [Connecting to Thredd Guide](https://docs.thredd.ai/Connecting_to_Thredd_Guide.htm).