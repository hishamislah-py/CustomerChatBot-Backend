# 2 How to Set Up Card Fees

Your implementation manager will set up your card usage groups and **fee groups** on the Thredd system, based on the details in your [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#).

Once they have set up your fee groups, you can use the Thredd API (Thredd REST-based Cards API or SOAP Web Services) to view the available fee groups, link a card to a relevant fee groups and change the fee groups linked to a card. You can also use the Thredd API to return details of any pending fees on a card and query details of card transaction fees over a defined period.

## 2.1 Steps in Setting up Card Fees

Below is a high-level summary of the steps in setting up and managing the fees linked to the cards in your program.

### 2.1.1 Setting up Fee Groups and Linking Cards to Fees

1. Consult with your implementation manager, who will complete your Product Setup Form (PSF) with details of the fee groups and fees you want to configure for your program. Fee configuration is described in the following topics:

   * [Authorisation Fees](Authorisation_Fees.htm)
   * [Recurring Fees](Recurring_Fees.htm)
   * [API usage Fees](Web_Service_Fees.htm)
2. Your implementation manager sets up your fees on the Thredd system.
3. When you create a card using the Thredd API, you specify a product code (`CardDesign` in Web Services or `designId` in REST API), which links the card to any default usage and fee groups configured for this product (if set up). You can override the default card product fee groups and specify specific fee groups to link to the card. See [Linking Cards to Fee Groups (SOAP Web Services)](Fee_Maintenance.htm#_Linking_a_card) or [Linking Cards to Fee Groups (REST Cards API)](Fee_Maintenance_REST.htm#_Linking_a_card).

### 2.1.2 Viewing and Maintaining Card Fees

Refer to the table below for details of options available via Web Services or Cards API.

| Web Services | REST API |
| --- | --- |
| * Query the fee groups linked to a specific card. See [Listing Fee Groups](Fee_Maintenance.htm#_Listing_Fee_Groups). * Change the fee groups linked to a specific card. See [Changing the Fees Groups linked to a card](Fee_Maintenance.htm#_Changing_the_Fees). * View pending fees on a specified card. See [Querying Pending Fees](Fee_Maintenance.htm#_Querying_Pending_Fees). * Query details of card transaction fees over a defined period. [Querying card transaction fees](Fee_Maintenance.htm#_Querying_card_transaction). | * Query the fee groups linked to a specific card. See [Listing Card Control Groups](Fee_Maintenance_REST.htm#Listing). * Change the fee groups linked to a specific card. See [Updating Card Fees Groups](Fee_Maintenance_REST.htm#Updating). * Query details of card transaction fees over a defined period. [Listing Card Transaction Fees](Fee_Maintenance_REST.htm#_Querying_card_transaction). |

If you need to change any of the fee options, including fee amounts, that are set up within a fee group, please contact your account manager or raise a JIRA change request. You will need to sign off any changes to your [Product Setup Form (PSF)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A spreadsheet that provides details of your Thredd account setup. The details are used to configure your Thredd account.](#) before these changes can be implemented on the Thredd system.

Details of fees charged on a per transaction basis are available from the following sources:

* The daily XML transaction report. See [Viewing Card Fees in the XML Report](Viewing_Fees.htm#_Viewing_Card_Fees_1).
* Authorisation and financial notifications sent via the [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) External Host Interface. This is a Thredd product providing clients either a real time feed or the ability to be involved in authorisations.](#). See [Viewing Card Fees on EHI](Viewing_Fees.htm#_Viewing_Card_Fees).
* Thredd Portal enables you to view details of transaction fees charged to a card or for a specific transaction. See [Viewing Card Fees on Thredd Portal](Viewing_Fees.htm#Viewing).
* Smart Client enables you to view details of transaction fees charged to a card or for a specific transaction. See [Viewing Card Fees on Smart Client](Viewing_Fees.htm#_Viewing_Card_Fees_2).