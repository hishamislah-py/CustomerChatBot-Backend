# General FAQs

This section provides answers to frequently asked questions.

## Smart Client Setup

#### Q. Does Smart Client work on a Mac?

Smart Client is not currently supported on Apple OSX. For more information, see [System Requirements](Installing_SC.htm#System).

#### Q. Why canât I see a function in Smart Client?

What you can see and do in Smart Client depends on your role and permissions. If you cannot see a menu option, this may be because you do not have the appropriate permissions. For more information, see [About roles and permissions](Launching_SC.htm#About).

#### Searching and Filtering

#### Q. Why canât I see a transaction in Smart Client?

If the authentication process fails before a transaction reaches the Thredd system, the transaction will not show up in Smart Client. For example, if a cardholder is authenticated through 3D Secure checks and fails, it will not appear in Smart Client. Similarly, if a customer removes their card from a card reader too quickly, the authentication process fails, and the transaction will not show up.

Archived tokens and transactions also do not appear within Smart Client â see below for more information.

#### Q. How do I retrieve archived tokens and transactions?

Depending on product set up, transactions are typically archived after 90 days. Dormant cards with a particular status (such as card destroyed or expired) are also archived after a period of inactivity.

To retrieve tokens and transactions from the archive so you can view information about them using Smart Client, raise a ticket with Thredd.

#### Q. How do I match transactions?

You can match transactions such as authorisations to presentments using the **Show transaction lifecycle** option. This displays all transactions that match the one you have selected.

This option appears only if there is a matching transaction. If Smart Client does not find a matching transaction, this option is not visible.

* Select a transaction, right click, and choose **More details** > **Show transaction lifecycle**.

Alternatively, to find matching transactions in Smart Client, search on fields such as the System Trace Audit Number (STAN), Trace-id or Approval ID. Avoid trying to match fields that can change across transactions, such as location. For more information about matching logic, see the [External Host Interface (EHI) Guide](https://docs.thredd.com/EHI_Guide.htm).

If more than 30 days has elapsed between the authorisation and presentment, you will be unable to match these.

## Managing Tokens and Transactions

#### Q. Can I reset card limits?

You can view the limits that apply to a card which were configured during product setup; however, you cannot change these limits in Smart Client. To change card limits, contact your Account Manager.

#### Q. What do I do if I suspect a BIN attack?

The BIN is the first 6 digits of a card number which correspond to a card scheme (payment network). A BIN attack is when a fraudster attempts to identify a valid card by using the BIN, randomly changing the remaining ten digits, and flooding the system with transactions. If a response (such as âincorrect expiry dateâ) is returned, this indicates a genuine card, and the fraudster may attempt to use this card number to access funds illegitimately.

In the event of a BIN attack, Smart Client displays a high volume of declined transactions with a Response Status (DE039) â14 - Invalid card number (no such number)â. Typically, these transactions have the same BIN, merchant name, and Acquirer ID (AID) and the Notes field shows the reason for the decline as unknown card number, unknown PAN, and unknown token.

Where a specific merchant location is used for BIN attacks, although no valid transactions are observed there across the entire Thredd client portfolio, Thredd blocks the merchant location. This will prevent successful transactions should a fraudster generate valid card details as part of a BIN attack using that merchant location.

#### Notes

* Thredd will not block merchant locations where there is a mix of fraudulent and valid transactions as this would impact legitimate cardholder transactions.
* Thredd will also not block merchant locations where only a small volume of transactions synonymous with a BIN attack are observed.
* Fraudsters are likely to switch merchant locations, but this measure will frustrate their efforts as it will affect merchants where controls are weakest or where there may be collusion.
* Thredd pro-actively completes an additional step on exceptional occasions based on dual review. This should not in any way reduce the fraud prevention tools and practices Issuers and Program Managers have in place, nor does it imply any responsibility on the part of Thredd for fraud prevention outside of the normal processor remit.
* This block will apply across all Thredd client programmes.

Thredd recommends the use of Thredd's real-time Fraud Transaction Monitoring to help guard against fraud. Thredd can also offer 3D Secure using Adaptive Authentication which reduces friction in the transaction process versus traditional 3D Secure. For information about these products, contact your Thredd Account Manager.

#### Q. How do I change the status of a card to Card Destroyed?

You can change the status of a card to prevent it from being used by setting the card status to 83âCard Destroyed. You can set the status in Smart Client or by using the Thredd API: SOAP Web Services [Card Change Status](https://docs.thredd.ai/webservices/Content/Web_services_api/Card_Change_Status.htm) or Cards API [Update Card Status](https://cardsapidocs.thredd.com/reference/update-card-status). For example, you may want to destroy a card if you suspect fraudulent behaviour. This will block most functions on the card, such as authorisations and loads, rendering the card unusable. However, presentments and refunds, because they are part of the financial record, will continue to process on cards with this status.

Changing a cardâs status to â83âCard Destroyedâ is not reversible.