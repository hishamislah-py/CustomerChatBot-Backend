# FAQs

This section provides answers to frequently asked questions.

## Fee Setup

#### Q. Do I need to set up my card fees on the Thredd system?

If you are using EHI modes where you maintain a register of the balance on the card for authorisation purposes, we recommend you use your own systems to charge fees to cardholders.

Where Thredd manages your transaction authorisation and maintains the card balance ledger, you can use Thredd to apply your service fees to the card.

#### Q. Can I set up default fees to apply to all my cards?

Yes. You can set up default fee groups, to apply to all cards within a card product. When creating a card using the Thredd API (SOAP web services or REST-based Cards API), if no fee is specified, then the default fee groups for the card product are used.

#### Q. How do I set up the fees for a specific card?

When setting up your card program, you must set up your fee groups on your Product Setup Form. See [Configuring your Program Fees](Fee_Setup_and_Configuration/Introduction.htm#Configur).

* Using SOAP Web Services: When creating a card using the Create Card web service (`Ws_CreateCard`), you can specify the fee groups to apply to the card. See [Applying Fees to a Card](Fee_Setup_and_Configuration/Fee_Maintenance.htm#_Applying_Fees_to_1).
* Using REST-based Cards API: When creating a card, the default fee groups for your product are linked to the card. You can use the [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) API to update the Fee groups linked to a card.

#### Q. Can I set up recurring fees?

Yes. You can apply a recurring account fee, deducted on a repeat basis (e.g., monthly or annually). You can also apply separate recurring fees for dormant accounts (i.e., where the card has not been used for a period). See [Recurring Fees](Fee_Setup_and_Configuration/Recurring_Fees.htm).

## Applying Fees

#### Q. Can I apply a one-off fee?

Yes. You can use the Generic Fees web service `<Ws_Generic_Fees>` to apply a one-off fee to the card (for example, to reflect a chargeback cost). (Note: available on Web Services only). See [Applying Fees to a Card](Fee_Setup_and_Configuration/Fee_Maintenance.htm#_Applying_Fees_to_1).

#### Q. What happens if there are insufficient funds available to apply a fee?

If you have enabled Partial Fees, Thredd will deduct a part of the fee amount and create a Pending Fee Record. See [Example of a Partial Fee](Fee_Setup_and_Configuration/Other_Fees.htm).

If you have not enabled Partial Fees, the transaction will be declined.

#### Q. How are fees applied and reported for declined transactions?

When a transaction is declined, the system applies a pre-configured decline fee. This fee is processed and reported in Thredd Portal, Smart Client and External Host Interface (EHI) messages as follows:

##### Fee Application Process

* The *Fixed Fee* and *Rate Fee* are set to 0.
* The *Note* field is updated to include details of both the *Fixed Fee* and *Rate Fee*.
* If a *Decline Fee* is defined for the specific card product:

  + This fee is deducted from the card balance.
  + The deducted amount is populated in the *Fixed fee* field in both the EHI message, Thredd Portal and Smart Client.

  This will be the only fee that is applied to the card for a declined transaction.

For more information on setting up fees for declined transactions, see [Authorisation Fees: Decline Fees](Fee_Setup_and_Configuration/Authorisation_Fees.htm#Decline_Fee).

## Fee Maintenance

#### Q. Can I change the Fee groups linked to a card?

Yes.

* Using SOAP Web Services: When creating a card using the Create Card web service (`Ws_CreateCard`), you specify the fee groups to apply to the card. You can use the **Change Card Groups** web service (`Ws_Card_Change_Groups`) to change one or more of the usage or fee groups for a specific card.
* Using REST-based Cards API: You can use the [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) API to update the Fee groups linked to a card.

#### Q. Do you provide an API to allow me to change the fee settings or amounts?

No. The implementation team manage the fee configuration on the Thredd systems. You will need to raise a JIRA request to change the fee settings, including any fee amounts.

* Using SOAP Web Services: You can use the **Change Card Groups** web service (`Ws_Card_Change_Groups`) to change one or more of the usage or fee groups for a specific card.
* Using REST-based Cards API: You can use the [Update Card Control Groups](https://cardsapidocs.thredd.com/reference/update-card-control-groups-1) API to update the Fee groups linked to a card.

## Viewing Fees

#### Q. Where are transaction Fee details provided?

Transaction fee details are provided in the daily XML reports, EHI data feeds and on Thredd Portal or Smart Client. See [Viewing Card Fees on EHI](Fee_Setup_and_Configuration/Fee_Maintenance.htm#_Viewing_Card_Fees).

#### Q. How can I find out how a transaction Fee was calculated?

First identify the type of transaction and the processing code linked to the transaction. Fees triggered by an authorisation or a web service are based on the processing code. The description field for the transaction may provide additional information about the fee.

Once you have identified the type of transaction and the processing code, check in your Product Setup Form (PSF) for the Fee group linked to that transaction type and processing code.

**Example**: Transaction type is an authorisation, with processing code: `000000`. In your PSF, under the **Authorisation** tab, find the row for `Debits (Goods and Services) [000000] Both`. Scroll across the row to view the specific fees applicable to this type of transaction.

#### Q. What if the transaction fee doesn't match the fee configuration?

If there is a discrepancy between the transaction fee that was deducted for the transaction and what you expect to see from the fee set up on the PSF, then check the following:

* Are there any additional fees you have set up that may have been triggered for this transaction? (for example, a multi-currency conversion fee, a non-domestic usage fee, reversal fee or decline fee)
* Is this a multi-currency transaction, where the transaction currency differs from the billing currency? (In this case, a conversion rate will have been applied to the transaction). For details of how fees are applied to cross-currency transactions, see [Appendix 8: Applying Fees to FX Transactions](Reference/Appendix_8_Multicurrency_fees.htm).
* Were there any other card fees (non-Thredd fees) applied to the transaction? (Such as a merchant, acquirer or network fee)

For more information, see [Introduction: Fee Application and Fee Reconciliation](Fee_Setup_and_Configuration/Introduction.htm#Fee).