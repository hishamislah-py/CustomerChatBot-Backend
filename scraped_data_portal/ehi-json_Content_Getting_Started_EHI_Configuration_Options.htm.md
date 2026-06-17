# 1.11 EHI Configuration Options

This section provides information on the available EHI configuration options. Your implementation manager will set up EHI based on the options you selected in the product setup form.

Thredd offers an optional Enhancement to Core Processing feature flag to assist in edge case scenarios where programmes receive data from multiple sources. For example, where you receive API calls and authorisation requests, you can enable this flag in order to ensure they are processed in a timely manner with additional validation checks to prevent cards from going into a negative balance.  
  
If you want to enable this flag, contact the Thredd Support Team.

| Option | Description |
| --- | --- |
| Mode | Your EHI mode (setup option, such as Gateway, Cooperative or Full Service Processing). See [EHI Operating Modes](EHI_operating_modes.htm). |
| Include Declined Transactions | Whether to include declined authorisation transactions in EHI messages (used for information purposes only). |
| Stand In | In Cooperative Processing (mode 2): If this is enabled and there is no connection to Host then we operate as we would if there was no external host at all and authorise/decline based on balance and other information we have in our system. |
| Approve with Load | In Cooperative Processing (mode 2): The authorisation can be approved with simultaneous instructing to load certain amount to a card. If this is required and the product is enabled with the âApproval with Loadâ feature, the authorisation response message of the approved transactions has to contain â0Aâ response code and amount to load. The Load will be done before the transaction amount is debited from the current balance.  **Note**: Multi-Fx cards are not supported. |
| Delay Send | Applicable in Mode 3 (Full Service Processing) only: If enabled, EHI messages only sends messages after the defined time period. If not enabled. EHI attempts to send messages in real-time first, with subsequent attempts after the defined delay. |
| Transaction Types | The transaction types you want EHI to send:  â¢ Authorisation  â¢ Financial (mandatory for modes 1 and 2 - Gateway and Cooperative Processing)  â¢ Load/ Unload  â¢ Balance Adjustment / Expiry  â¢ Authorisation advice  â¢ TAR (transaction authorisation request for a token creation request) |
| External Host URL (Single EHI Endpoint) | The URL EHI uses to send messages to your external host if you have configured a single EHI endpoint to receive all messages from Thredd. Different endpoints (URLs) can be set up for each product. |
| Decisional URL (Multiple EHI endpoints) | The URL EHI uses to send all time-critical (real-time) messages such as Authorisations, Authorisation Reversals and Advices. Different endpoints can be set up for each product.  Discontinued. |
| Informational URL (Multiple EHI endpoints) | The URL EHI uses to send non-time-critical messages such as Chargebacks, Balance Adjustments, Loads/Unloads, Fees and Presentments. Different endpoints can be set up for each product.  Discontinued. |
| Clearing URL (Multiple EHI endpoints) | The URL EHI uses to send presentments. Only First Presentments and Second Presentments are sent to this endpoint. Different endpoints can be set up for each product. This optional field can be used to receive presentments in a separate EHI endpoint.  If a Clearing URL is not provided, but an Informational URL is provided, then all presentments are sent to the Informational URL.  Discontinued. |
| Timeout after | Determines how long EHI waits for a response from the external host before timing out. The default timeout is 200 milliseconds. This can be changed to meet your system requirements. Please contact your account manager or implementations manager to discuss. |
| Repeat after | Indicates how long EHI waits to resend the message when it does receive any acknowledgement from the external host. The default is 2 minutes. |
| Times | Indicate how many times EHI needs to resend the message. Default value is 5. |
| Remove from buffer table after | Indicates the number of days your transaction data is stored in the Thredd buffer table. This can be useful in the scenario where your system is down and you need time to fix it. When the system is back up, Thredd can flush all data from the buffer. Default is 3 days. Maximum is 7 days. |
| Send Cut of Message | Whether to send a cut off message. See [Cut Off Messages](../Requirements/Cut_Off_Messages.htm). |
| Cut off Interval | The cut-off period in hours (e.g. if it is set to 4 hours EHI sends a cut-off message every 4 hours). Default is 4 hours. |
| Cut off URL | The URL EHI uses to send Cut Off messages to your external host. |
| Version | The EHI version you are using. |
| Optional fields in Authorisation request message | Select the optional fields you would like sent in Authorisation messages:  â¢ Send CVV2  â¢ Send PIN (If selected, please provide the [PIN Key File](#PIN_Key_File))  â¢ Send Expiry Date  â¢ Send PAN Sequence Number |
| Notify | The email address to notify you If EHI cannot reach the external host. |
| DR EHI URL | The URL EHI uses to send messages to your external host if the primary URL is unavailable (i.e. Disaster Recovery). |
| DR Cut off URL | The URL EHI uses to send Cut Off messages to your external host if the primary URL is unavailable (i.e. Disaster Recovery). |
| SSL Key | SSL certification key to use, where SSL is enabled on your external host. |
| PIN Key File | PIN key file to be used where the *send PIN* field is enabled for inclusion in authorisation request messages. [Triple DESClosed Triple DES (3DES or TDES), is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block to produce a more secure encryption.](#) keys are used to encrypt PINs in EHI messages. They can be generated either by Thredd or the Program Manager, and must be stored in a separate file. For details, see [PIN Block Formats](../Appendices/PIN_fields.htm#PIN). |
| JSON format | EHI can be enabled to send and receive messages in JSON format.  **Note**: You must be on EHI version 5.0 or above to receive this feature. |