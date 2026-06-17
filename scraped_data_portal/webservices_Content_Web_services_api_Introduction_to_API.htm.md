# List of Web Services API

The table below lists the available web services (ordered alphabetically).

| API | Description |
| --- | --- |
| [Ws\_Activate](Card_Activate.htm) | Sets the status of the card to âactiveâ to enable Mastercard/Visa network transactions. Used to activate cards issued in an inactive state. |
| [Ws\_Activate\_Load](Card_Activate_and_Load.htm) | Enables simultaneous load and activation of a card. This is a common requirement for cards sold from kiosks or from retail stores. For cards ordered over the internet, delayed activation provides added security by ensuring that any card stolen or lost in the post cannot be used. |
| [Ws\_Activate\_MVCLoad](MVC_Card_Activation_and_Load.htm) | Enables simultaneous load from Master Virtual Card (MVC) and activation of cards. Ws\_Activate\_MVCLoad effectively combines the functions of Ws\_BalanceTransfer and Ws\_Activate for clients that are using MVCs (Master Virtual Card). |
| [Ws\_AddUpDelCredentials](3D_Secure_RDX_Credentials.htm) | Enables you to collect the cardholders' 3D Secure credentials and insert, update or delete those credentials using the Real-Time Data Exchange interface for Cardinal and Apata. |
| [Ws\_ApataCardLevelConfigurations](3D_Secure_Apata_Configuration.htm) | Enables you to add, update or delete card level configurations for 3D Secure via Apata, such as the language of the Apata Challenge screens and the Challenge Profile to use. |
| [Ws\_Balance\_Enquiry (V2)](Card_Balance_Enquiry.htm) | Returns the current available balance on the card. |
| [Ws\_Balance\_Enquiry Wallet](Card_Balance_Enquiry.htm) | Returns the current available balance on each of the available currency wallets for a multi-FX card. |
| [Ws\_BalanceAdjustment](Card_Balance_Adjustment.htm) | Enables you to apply a debit or credit to a card record. |
| [Ws\_BalanceTransfer](Card_Balance_Transfer.htm) | Used to transfer an amount from one card to another. |
| [Ws\_BalanceUpdate](Card_Balance_Update.htm) | Updates the available and current (STIP) balance for Program Managers set up for EHI Processing with STIP (Stand-in processing mode 4). For details, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm). |
| [Ws\_Banking\_AccountModulusCheck](Bank_Account_Check_Number.htm) | Validates that a sort code and account number (UK Bank Accounts provided through programmes using Thredd Bottomline Agency Banking) are valid via a modulus check. |
| [Ws\_Banking\_CancelDirectDebitBankingEnabledCard](Cancel_Direct_Debit.htm) | Marks a direct debit as cancelled where a card has an associated UK Bank Account (provided through programmes using Agency Banking). The GUID (Globally Unique ID) for the direct debit is required and can be obtained by calling |
| [Ws\_Banking\_Card\_Statement\_V2](Card_Statement_v2.htm) | This web service is an enhancement to `Ws_Card_Statement` and returns all statement details for this card and previous cards if the card has been replaced for various reasons |
| [Ws\_Banking\_ChangeAccountBankingFeaturesStatus](Bank_Account_Change.htm) | Changes the features of the banking enabled card and allow the user to switch functionality on or off. |
| [Ws\_Banking\_CreateCustomer](Register_Customer_for_Banking.htm) | Enables you to register customer details without creating associated bank accounts or cards. |
| [Ws\_Banking\_DD\_CancelMandate](Cancel_Direct_Debit_Mandate.htm) | Cancels a specific mandate for a specific mandateId and token. |
| [Ws\_Banking\_DD\_GetMandate](Retrieve_Direct_Bank_Mandates.htm) | Retrieves all mandates for a given token. |
| [Ws\_Banking\_GetDirectDebitInstructionsBanking EnabledCard](Get_Direct_Debits.htm) | Returns a list of all direct debits for a given token (with or without sub accounts). Note: Only for programmes using Agency Banking. |
| [Ws\_Banking\_GetPendingDirectDebits](Get_Pending_Direct_Debits.htm) | Returns a list of all direct debits that are due for payment today for a given token (with or without sub accounts). Note: Only for programmes using Agency Banking. |
| [Ws\_Banking\_RegisterNotification](Register_Customer_for_Banking_1.htm) | For some banking integrations, once you have called Ws\_CreateCard\_V2 to create the bank account and card, you need to make additional calls to allow payments to be processed on and off the card. There are a number of options, but as a minimum, you should switch on PAYIN and PAYOUT to facilitate payments. Note: All notifications work at a customer level, so if a customer has more than one account, the notification will apply to all of the customers accounts |
| [Ws\_Banking\_ReturnBankDetailsFromToken](Return_Sort_Code_and_Account.htm) | Returns the sort code and account number (UK Bank Accounts provided through programmes using Agency Banking) from a token. |
| [Ws\_Banking\_StatusQueryBankingEnabledCard](Return_Card_Enabled_Option.htm) | Returns the Agency Banking features (UK Bank Accounts provided through programmes using Agency Banking) that are enabled on a card and the status of the card. |
| [Ws\_Banking\_TransferFunds](Make_External_Payment.htm) | Makes an external payment via the Faster Payment banking network where a card has an associated UK Bank Account (provided through programmes using Agency Banking). Note that the money is queued and has not necessarily entered the banking network. |
| [Ws\_Banking\_UpdateBankingEnabledCard](Update_Card_Status.htm) | Updates the status of Banking services for a card depending on the current status. |
| [Ws\_BulkCreation](Card_Bulk_Create.htm) | Creates a bulk number of virtual as well as physical cards in a single request. This web service takes an XML document as the input parameter with the information needed to create virtual or physical cards. It produces an XML document with the list of newly created virtual or physical cards as the response. Card images will be created in the web service directory when creating a virtual card. |
| [Ws\_BulkWalletCreation](Wallet_Bulk_Create.htm) | Creates multiple wallets in a single request. This web service takes an XML document as its input parameter with the information needed to create wallets and produces another XML document with the list of newly created wallets as a response. |
| [Ws\_Card\_BalEnq](Card_Balance_Enquiry_1.htm) | Returns the available balance of a card and the sum of any blocked amounts. |
| [Ws\_Card\_Change\_Cardacceptor\_List](Card_Change_Acceptor_List.htm) | Updates the card acceptor lists such as Allow and Deny lists that a card makes use of. |
| [Ws\_Card\_Change\_Groups](Card_Change_Groups.htm) | Changes one or more of the usage groups for a specific card within any of those configured for your programme (e.g. Limit Groups, MCC Group, Fee Group and Usage Group). |
| [Ws\_Card\_Statement](Card_Statement_v1.htm) | Returns a list of transactions performed by the cardholder since a specified date, together with the starting balance and current balance. Typically you should specify a date range of within the last 7 days. If the date is omitted, then all transactions are returned. Current actual and available balance is also returned. |
| [Ws\_CardAcceptorBlacklist](Card_Acceptor_Blacklist.htm) | Used to maintain Card Acceptor (MerchantID) Deny lists, which can then be assigned to a card or group of cards. Thredd will decline authorization transactions belonging to any merchant IDs on the Deny list. The response code will be â05 â Do not honourâ. |
| [Ws\_CardAcceptorWhiteList](Card_Acceptor_Whitelist.htm) | Used to maintain Card Acceptor (MerchantID) Allow lists which can then be assigned to a card or group of cards. Only merchant IDs on the Allow list will be approved by Thredd at authorisation stage. |
| [Ws\_CardHolder\_Details\_Enquiry](Cardholder_Enquiry.htm) | Returns the details of a cardholder. |
| [Ws\_Change\_Cardacceptor\_List](Card_Change_Acceptor List_1.htm) | Updates the card acceptor lists such as Allow and Deny lists that a group of cards belong to. |
| [Ws\_Change\_Groups](Card_Change_Groups_1.htm) | Changes groups such as Group Limits, MCC Group and Usage Group of cards within a product or a customer account. |
| [Ws\_Check](Check_Service_Availability.htm) | Checks web service availability. It validates the SOAP credentials and Issuer Code by calling database procedures. |
| [Ws\_Client\_FX](Apply_FX_Rate.htm) | Enables you to send your own foreign exchange (FX) rates to Thredd. You can stream in FX rates at your chosen frequency (e.g. hourly, daily). The rates can be used for multi-FX wallet functions or for provisioning of fixed rate FX cards. |
| [Ws\_Convert\_Card](Card_Convert_to_Physical.htm) | Upgrades a virtual card to a physical card. |
| [Ws\_CreateCard](Card_Create.htm) | Creates both a virtual card and a physical card. |
| [Ws\_CreateCard\_V2](Create_Card_with_Agency_Banking.htm) | Creates a card with Agency Banking features enabled. It will also upgrade an existing card to have banking features. Applies only to programmes using Agency Banking. |
| [Ws\_CreateWallet](Wallet_Create.htm) | Used to create virtual wallets as well as physical card wallets. |
| [Ws\_Customer\_Enquiry](Card_Customer_Enquiry.htm) | Returns the list of cards associated with a specified customer name. |
| [Ws\_Delete3DSecureDetails](3D_Secure_Delete_Details_Cardinal.htm) | Deletes 3D secure enrolment details for a card. ( Cardinal Batch File Interface; Legacy use only). |
| [Ws\_Enquiry](Card_Enquiry.htm) | Returns the details of a card, such as: Token, Expiry Date, Status, Cardholder name. |
| [Ws\_ExtendExpiry](Card_Extend_Expiry_Date.htm) | Changes the Thredd expiry date of cards by the specified value. |
| [Ws\_Generic\_Fees](Card_Apply_Fees.htm) | Applies fees with a comment to a particular card. |
| [Ws\_Get\_Card\_ExpireSoon](Cards_Get_Expiring_Soon.htm) | Returns the details of cards that are going to expire within the month. The response will return all cards due to expire, regardless of the volume. |
| [Ws\_GetApataCardLevelConfigurations](3D_Secure_Get_Apata_Configuration.htm) | Retrieves the card level configuration for 3D Secure (using Apata). |
| [Ws\_Get\_Passcode](Card_Get_Passcode.htm) | Used to retrieve the Access Code (also known as pass code or activation code) of cards. |
| [Ws\_Insert3DSecureDetails](3D_Secure_Enrol_Cardinal.htm) | Enrols a specified cardholder onto 3D Secure using the Cardinal Batch File Interface 3D Secure service. (Legacy use only) |
| [Ws\_link\_cards](Cards_Link.htm) | Links cards in a Primary and Secondary relationship, and can be used when the primary card with existing secondary card linkage(s) needs to be replaced with a new token. The secondary cards can be linked to the new token via this web service call. |
| [Ws\_list\_group](List_Groups.htm) | Lists the codes and descriptions of all groups of a certain type (e.g. Fee Groups, Limit Groups). |
| [Ws\_List\_Pending\_Fees](Card_List_Pending_Fees.htm) | Lists service lists details of pending fees that relate to a particular card. |
| [Ws\_List\_Products](List_Products.htm) | Lists products your programme has on the Thredd systems and their descriptions. |
| [Ws\_Load](Card_Load.htm) | Loads or re-loads a card with a specified amount. |
| [Ws\_MVCLoad](MVC_Load.htm) | Loads funds from Master Virtual Cards (MVC) only. This is similar to balance transfer, the only difference is that the source is always an MVC token. |
| [Ws\_MVCUnload](MVC_Unload.htm) | Enables customers to unload back to Master Virtual Card (MVC) only. |
| [Ws\_Payment\_Token\_Get](Payment_Token_Get.htm) | Gets the details for MDES (Mastercard Digital Enablement Service) Payment Token Cards. |
| [Ws\_Payment\_Token\_StatusChange](Payment_Token_Status_Change.htm) | Changes the status of an MDES (Mastercard Digital Enablement Service) Payment Token Card. |
| [Ws\_Phone\_Activation](Card_Phone_Activation.htm) | Enables activation of a card by phone. It also returns the PIN and the PIN status of that card. |
| [WS\_PinControl](Card_PIN_Control.htm) | Enables you to set, retrieve, unblock and change the PIN associated with the card. |
| [Ws\_Query3DSecureDetails](3D_Secure_Query_Details_Cardinal.htm) | Used to view the phone number of a particular userâs token that has been enroled for 3D secure and gets the details from Thredd 3DS table. (Cardinal Batch File Interface; Legacy use only). |
| [Ws\_Regenerate](Card_Regenerate_Image.htm) | Retrieves the card image configured in the Thredd platform for virtual and physical cards that have been converted which can then be displayed to the cardholder. If a customer wants to see the image some time after card creation you can regenerate the image. This web service can also be used to replace Lost or Stolen cards; the customer will be issued with a new PAN, CVV2 and Expiry Date. |
| [Ws\_RegenerateWallet](Regenerate_Wallet.htm) | Regenerates MFX cards. |
| [Ws\_Remove\_CardHolder\_Data](Remove_Cardholder_Data.htm) | Removes personally identifying cardholder data (cardholder name, address, email and phone number) from the specified card. You can remove data from multiple cards in a single request. |
| [Ws\_Renew\_Card](Card_Renew.htm) | Enables you to renew or replace cards. Combines the functionality of card replacement and card renewal. The replacement card will automatically have the same balance as the original card at the time when the replacement card is activated. Any linked cards will still point to the correct card. |
| [Ws\_ResetAccumulator](Clear_Accumulator.htm) | Allows you to reset transaction and amount counters (since the last authenticated transaction) on a card to re-enable contactless devices and wearables, where a Secure Cardholder Authentication cannot be performed by the terminal (i.e. those that do not offer PIN). |
| [Ws\_SendMessage](Cardholder_Send_Message.htm) | Used to send a predefined message to the cardholder via SMS or Email. Thredd can configure the message using a selection of variables. |
| [Ws\_Simple Check](Check_Web_Service_Availability.htm) | Checks web service availability. Can be called over HTTPS GET. |
| [Ws\_StatusChange](Card_Change_Status.htm) | Enables the status of a card record to be changed. For example to: Do not honour, lost, stolen or Card Destroyed. |
| [WS\_Token\_Device\_Management](Token_Device_Management.htm) | Allows you to retrieve a list of devices bound to a DPAN. Can be used to unbind a device by initiating an Unbind API call to Visa. |
| [Ws\_Transaction\_Void](Transaction_Void.htm) | Enables cancellation of any transaction which has been implemented via a web service, and also allows you to remove uncleared authorizations. |
| [Ws\_UnLoad](Card_Unload.htm) | Unloads a card. Note that any outstanding, unsettled authorisations on the card may result in the card going into a negative balance. |
| [Ws\_UnLoad\_StatusChange](Card_Unload_and_Change_Status.htm) | Simultaneously unloads the card and changes the card status (e.g. to expired). |
| [Ws\_Update\_Cardholder\_Details](Update_Cardholder_Details_v1.htm) | Enables cardholder details to be updated. For example: name and address. |
| [Ws\_Update\_Cardholder\_Details\_V2](Update_Cardholder_Details_v2.htm) | This web service is an enhancement to Ws\_Update\_Cardholder\_Details. It allows further cardholder details to be updated such as EmbossLine4, ProductRef, ThermalLine1 etc. |
| [Ws\_UpdateLastModifiedType](3D_Secure_Update_Last_Modified_Type.htm) | Used to update the last modified type of 3D secure action for a card. (Cardinal Batch File Interface; Legacy use only). |
| [Ws\_Update3DSecureDetails](3D_Secure_Update_Details_Cardinal.htm) | 3D Secure service to amends 3D secure details for a card; this web service can be used to update the phone number used for authentication SMS. (Cardinal Batch File Interface; Legacy use only). |

The next sections in this guide are organised based on common tasks performed using the API, in the order in which we expect most users will use them. Please use the left-hand menu options to find the section and API you are interested in.