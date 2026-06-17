# 1.12 Integration Steps

This section describes the steps in integrating your external host system to the External Host Interface (EHI).

## 1.12.1 Setting up in the Test Environment

1. Complete your Thredd product setup form. See [EHI Configuration Options](EHI_Configuration_Options.htm).
2. Provide Thredd with a list of static IP addresses to your external host server for Thredd to allow access to.
3. Your implementation manager will set you up on the Thredd Test system and will:

   * Provide you with your user credentials to access the Thredd Test system.
   * Set up your External Host URL on EHI for sending GetTransaction messages.
   * Set up your External Host URL on EHI for sending CutOff messages.
   * Provide you with details of how to access [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#), where you can manage your cards and transactions.

     The External Host URLs you provide need to resolve to the static IP addresses you provided to Thredd.
4. You will need to be set up with secure access to Thredd systems.
5. Integrate to Thredd using the Web Services API (SOAP) or Cards API (REST), in order to create cards and load them with funds. For details, see the Web Services Guide or the [Cards API Website](https://cardsapidocs.thredd.com//).
6. Set up your external host systems to be able to receive and process messages from EHI. Your systems should be able to:

   * Check for duplicate messages, respond to and acknowledge EHI messages. See [Processing EHI Transactions](../Requirements/Processing_EHI_Transactions.htm).
   * Match and process transactions. See [Transaction Matching](../Requirements/Transaction_Matching.htm).
   * Process GetMessage fields. See [GetTransaction Messages](../Requirements/GetTransaction_Message.htm).
   * Receive CutOf messages. See [CutOff messages](../Requirements/Cut_Off_Messages.htm).
7. For EHI modes 1, 2 and 4 (Gateway and Cooperative Processing) where you provide the approve or decline decision for an authorisation transaction, make sure your systems can process the GetTransaction messages and block the available card balance accordingly.
8. For EHI modes 1, 2 and 4 (Gateway and Cooperative Processing) where you maintain the balance, make sure your systems can process the GetTransaction financial messages and update the card balance accordingly.
9. Submit test authorisation and financial transactions to the test environment:

   * You can requests test transactions from your implementation manager.
   * You can use the Card Transaction System (CTS) to create test transactions for different use case scenarios (e.g., POS, ATM, ecommerce and MOTO payments). See the Card Transaction System (CTS) User Guide.

## 1.12.2 Setting up in Production

When you have completed your integration and your card issuer has approved your Product Setup Form (PSF), we can set you up in the live environment.

1. A secure connection to Thredd is required to connect to the production system.
2. You will need to generate some live cards (i.e., internal pilot cards) from your card manufacturer in order to run live transactions. For more information on how to generate cards, see the Web Services Guide or contact your Implementation Manager.
3. Run card tests on live cards for different use case scenarios and check the end-to-end process. See [Testing Use Case Scenarios](#Testing) below.   
   Make sure your service works before rolling out!

Your first live cards should be for internal, pilot use only and Thredd recommend you complete your programme testing first before launching your service to cardholders and investors.

### Testing Use Case Scenarios

Below are details of the type of test scenarios which Thredd recommends you complete:

* Do the cards support the functionality and behaviour you expect?
* Are the CHIP profiles on the cards correctly set up? (i.e., is the card working and card validation working as expected.)
* Is your mobile app behaving as expected? (e.g., displaying real-time details of card status, card transactions and account balances.)
* If you are using mobile tokenisation services such as VDEP and MDES have you tested different use case scenarios?
* Have you tested other components of your card service, such as:

  + Recurring payments
  + Fees
  + Cardholder authentication (3D Secure)
  + Exception flows, such as reversals, refunds and chargebacks.
* Have you checked the cardholder journey from an end-to-end perspective?

### Thredd Card Tests

Thredd runs a set of generic pavement tests where we check a range of card functionality, such as:

* Keys are set up correctly
* Both contact and contactless card transactions are working
* The card usage groups set up for your programme are declining as expected
* General authorisations are being received, refunds are working correctly, authorisation requests are being declined and approved as expected.

In order to check the Thredd platform is behaving according to how configured in your product setup form, we require a selection of cards per programme. Cards should be loaded with sufficient funds to enable testing.

## 1.12.3 Troubleshooting

Below are examples of some of the types of issues your systems need to be able to handle:

* System timeouts and connection issues
* Duplicate transactions and unmatchable transactions
* Reversals (0400 messages), where you need to approve and unblock funds
* Balance enquiries and issues relating to the card balance
* Cryptogram failures on the CHIP for a new chip profile being launched; this is normally resolved by the Card Manufacturer

For more information see the [Troubleshooting FAQs](../Troubleshooting_FAQs.htm).