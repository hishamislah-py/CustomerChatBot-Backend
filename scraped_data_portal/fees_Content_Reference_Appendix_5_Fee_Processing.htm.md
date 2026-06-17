# Appendix 5: Fee Processing Flows

This section provides examples of how card fees are processed on the Thredd system.

## Authorisation Fee Processing Flow

[Figure 1](#Authoris) below describes the steps in processing an authorisation fee on the Thredd system. The transaction processing code (`Proc_Code`) returned from the Card Scheme (Visa/Mastercard/Discover) is used to determine which fee to charge, based on the Authorisation Fee Group linked to the card record.

![](../Resources/Images/Auth_fee_flow.png)

Figure 14: Authorisation Fee Processing Flow

For details of how to configure your Authorisation fee groups, see [Authorisation Fees](../Fee_Setup_and_Configuration/Authorisation_Fees.htm).

## Thredd API Usage Fee Processing Flow

Fees for using the Thredd API (SOAP web services or RESP API) are triggered in one of two scenarios:

* **Automatically triggered** â when a Thredd API is used, a fee is triggered automatically if a fee for this API has been set up in an API Usage Fee group. See [API Usage Fees](../Fee_Setup_and_Configuration/Web_Service_Fees.htm).
* **Manually applied** â when you apply an ad-hoc fee using the Generic Fees (`Ws_Generic_Fees`) web service (e.g., one-off Administration Fee). See [Applying Fees to a Card](../Fee_Setup_and_Configuration/Fee_Maintenance.htm#_Applying_Fees_to_1). (**Note**: the manual fee option is only available when using SOAP Web Services)

[Figure 2](#Web) below describes the steps in processing an API usage fee on the Thredd system, where the fee is automatically triggered via a fee group. Thredd use the transaction processing code (`Proc_Code`) to determine which fee to charge, based on the API Usage Fee Group linked to the card record.

![](../Resources/Images/API_usage_fee.png)

Figure 15: Thredd API Usage Fee Processing Flow

For details of how to configure your API Usage fee groups, see [API Usage Fees](../Fee_Setup_and_Configuration/Web_Service_Fees.htm).

## Recurring Fee Processing Flow

[Figure 3](#Recurrin) below describes the steps in processing a Recurring fee on the Thredd system. The fee is triggered when a daily scheduled job that is run on the cardâs database identifies a recurring fee is due on a card. Thredd use the Recurring Fee Group linked to the card record to determine when to apply a fee and which fee to charge.

![](../Resources/Images/Recurring_fee.png)

Figure 16: Recurring Fee Processing Flow

For details of how to configure your Recurring Fee groups, see [Recurring Fees](../Fee_Setup_and_Configuration/Recurring_Fees.htm).

## Recurring Fee Configuration Options

Refer to the table below for recurring fee configuration options.

### Monthly Fees

The following fees can be applied on a monthly basis.

| Recurring Fee Name | Trigger | When does the fee start? | When is the fee applied? | How does fee end? |
| --- | --- | --- | --- | --- |
| Monthly Fee - Activation | Activation - Monthly Activation Fee (cards activated after 15th of previous month up to 15 of current month, and fee will only take on Last day of current month) | End of current month or end of next month | If the card is activated before 15th of a month then the fee is taken on that month. If the card is activated after 15th of the month, then the fee is taken on the next month. | No balance, Card Expiry |
| Monthly fee - activation fee taken on 5th | Activation | 5th day of every month | When card is activated, 5th day of every month. | No balance, Card Expiry |
| Monthly fee after load | First load | Day after 1st Load | Day after 1st Load and on same day each month thereafter. | No balance, Card Expiry |
| Monthly Fee - Following reload | Reload | Day after the reload | Day after the reload and on same day each month thereafter. | No balance, Card Expiry |
| Monthly service fee | Activation | 1st day of month or 5th day of month | When card is activated, fee taken is on 1st day or 5th day of every month. | No balance, Card Expiry |
| Monthly fee 8th of every month | 8th DAY of every month | 8th day of every month | 8th day of every month. | No balance, Card Expiry |
| Monthly fee | Last day of current month | Last day of current month | Last day of every month. | No balance, Card Expiry |

### Annual Fee

The following fee can be applied on an annual basis.

| Recurring Fee Name | Trigger | When does the fee start? | When is the fee applied? | How does fee end? |
| --- | --- | --- | --- | --- |
| Annual Fee | Annual | Activation | 365 days after the card activation. | Every 365 days after activation. |

### Card Expiry Fee

The following fee can be applied to expired cards.

| Recurring Fee Name | Trigger | When does the fee start? | When is the fee applied? | How does fee end? |
| --- | --- | --- | --- | --- |
| Card Expiry | Monthly dormancy Fee - After Card Expires | Card Expiry | 3 days (It can be configured) after Card Expires. | 3 days after Card Expires and on same day each month thereafter. |

### Dormancy Fees

The following fees can be applied to dormant accounts.

| Recurring Fee Name | Trigger | When does the fee start? | When is the recurring fee applied? | How does fee end? |
| --- | --- | --- | --- | --- |
| Dormancy fee 2 months | 2 months after last transaction | 2 months after the date of the last balance changing transaction | On same day each month | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Dormancy fee 3 months | No transaction in 3 months | 3 months after the date of the last balance changing transaction | On same day each month | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Dormancy fee 6 months | No transaction in 6 months | 6 months after the date of the last balance changing transaction | On same day each month | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Dormancy 12 months | No transaction in 12 months | 12 months after the date of the last balance changing transaction | On same day each month | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Monthly Fee - No transaction in last 90 days | No transactions in last 90 days | 90 days after last balance changing transaction | Every 90 days | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Dormancy 90 | No transactions in last 90 days | 90 days after last balance changing transaction | Every 90 days | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |
| Inactivity fee - no transaction in last 90 days | No transactions in last 90 days on inactive card | Issue date = NOT Null; Activation date = NULL No balance changing transactions after 90 days after Issue Date | Every month | Activation date = NOT Null No Balance Card Expiry |
| No transaction in last 120 days | No transactions in last 120 days | 120 days after last balance changing transaction | Every 120 days | When a balance changing transaction occurs (includes loads)  No Balance Card Expiry |

## Fee Processing of ASI Transactions

Account Status Inquiry (ASI) Service is a type of authorisation transaction, supported by Mastercard, which allows a merchant to check the [Card Validation Code (CVC)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Card Verification Code, or CVC, is an extra code printed on a debit or credit card. With most cards (Visa, Mastercard) it is the final three digits of the number printed on the signature strip on the reverse of the card.](#) and, if address details are provided, to optionally use the [Address Verification Service (AVS)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) An AVS check compares the billing address used in the transaction with the issuing bankâs address information on file for that cardholder. Depending on whether they match fully, partially, or not at all, the merchant can use that information in their decision on whether or not to accept or cancel the order. AVS is one of the most widely used fraud prevention tools in card-not-present transactions.](#). If these checks are successful, Thredd responds to the merchant with 00 (approve). The merchant typically then submits a second authorisation transaction, with an actual transaction amount included.

When the Thredd system receives an authorisation request for an ASI transaction[1  ASI transactions usually have 0 bill amount. You can identify a transaction as ASI in Thredd Portal or in Smart Client, in the Notes field for the transaction. For more information on identifying an ASI transaction in EHI messages, see the FAQ section in the External Host Interface (EHI) Guide.](#), it performs the AVS and CVC checks, and if the ASI request is declined, decides whether to apply a fee for thew decline, in the following sequence:

1. Run AVS check
2. Run CVC check
3. Apply fees if applicable

A fee is applied if the transaction is declined at the AVS check stage, but not if the transaction is declined at the CVC check stage. See [Figure 4](#Decline) below.

![](../Resources/Images/Fee_Processing_Rules_for_ASI_Transactions.png)

Figure 17: Decline Fees for ASI Transactions