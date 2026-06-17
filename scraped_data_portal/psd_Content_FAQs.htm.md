# Frequently Asked Questions

## Thredd Handling of PSD2 SCA Requirements

### Q. Are Thredd systems configured not to request SCA for out of scope of SCA transactions?

Yes, Thredd Systems are configured to not request for SCA for out of scope of SCA transactions (where the PSD2 rules do not apply). See [Step 1: Check if PSD2 Rules Apply](PSD2/Step1_Do_PSD2_Rules_Apply.htm).

You can identify Thredd flagged Out-of-scope SCA transactions using the `ExemptFromSCA` indicator in EHI field `GPS_POS_Data`.

### Q. Do Thredd systems decline transactions based on the SCA status?

Yes, if PSD2 checking is enabled for the Thredd Card Product, then Thredd will [soft decline](PSD2/Soft_Declines.htm) all transactions where PSD2 rules apply and where the transaction is non-SCA and no exemption applies. See [PSD2 Transaction Flow.](PSD2/PSD2_Transaction_Flow.htm)

If PSD2 rules apply and there is no applicable exemption, then we will *soft decline* (decline asking the merchant to repeat the transaction using SCA this time). This should therefore result in a second transaction which is SCA and can therefore be approved.

### Q. How can I identify the SCA status of a transaction?

You can use messages received from the [External Host Interface (EHI)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) to identify the SCA status of a transaction. You can also use either Thredd Portal or Smart Client to view transactions. See [Identifying the SCA Status](PSD2/PSD2_Status.htm).

## PSD2 Exemptions

### Q. What is the authorisation exemption for low-value transactions?

The following exemptions apply:

* E-commerce transactions of up to EUR 30.00, and cumulatively not exceeding EUR 100.00 or 5 transactions.
* Contactless transactions of up to EUR 50.00, and cumulatively not exceeding EUR 150.00 or 5 transactions.

The exemption limits may vary, depending on the values set by your country's Financial Regulator.

### Q. What type of transactions are out of scope for SCA?

The following transactions are not included in the PSD2 rules for SCA:

* [Mail and Telephone Order (MOTO)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Transaction where payment instruction is taken over the telephone or via a mail order. Since the cardholder is not present, these are classed as "Cardholder Not Present" transactions.](#)
* One-Leg-Out transactions - occurs when one of the payment service providers (either the payer or payee) is outside the European Union (EU). If the Acquirer is from outside the EU and the payer is from the EU, the Acquirer does not need to comply with PSD2 regulations.
* Anonymous transactions - such as for prepaid gift cards where the cardholder's identify is not known
* Credit transaction - such as credit vouchers and [Original Credit Transactions (OCT)![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Transaction that can be used to send funds to a card-based account, resulting in a credit of funds to the cardholder's account.](#)
* Refunds

The following merchant initiated transactions are also exempt (where the cardholder is not present):

* Installment/prepayment

* Recurring
* Unscheduled credential on-file
* Incremental
* Delayed charges
* No-show
* Reauthorisation
* Resubmission

### Q. Which Merchant Category Codes are Exempt from SCA?

Refer to the table below for SCA exemptions.

These exemptions only apply to card present transactions (i.e., cardholder present and unattended terminal transactions) and excludes all cases where the cardholder is not present (i.e., mail-order, telephone-order, recurring and e-commerce transactions).

| MCC | Description |
| --- | --- |
| 4111 | Local and suburban commuter passenger transport, including ferries. |
| 4112 | Passenger railways. |
| 4131 | Bus lines. |
| 4784 | Tolls and bridge fees. |
| 7523 | Car parking and parking meters. |

We can optionally configure your programme to apply SCA exemptions to hotel merchants and to car rental merchants doing PAN key entry or manual, cardholder present (or unknown) transactions.

| MCC | Merchant type |
| --- | --- |
| 3501-3999, 7011 | Hotel merchants |
| 3351-3500, 7512, 7513, 7519 | Car rental merchants |