# 9 Chip Management on the Thredd Platform

Although the chip card profile defines a card's behaviour, the host system has some limited capability to change chip transaction outcomes or chip card behaviour. See below for a list of Thredd Platform features that affect chip card transaction flows:

* [CVM result check](#CVM)
* [Contactless Magstripe](#Contactl)
* [ARC (ARPC Response Code) instructions](#ARC)

## CVM (Cardholder Verification Method) Result Check

If a Cardholder Verification Method (CVM) is disabled on cardâs usage group, any online transaction with that CVM will be declined. Those methods are listed on Usage Group settings:

| CVM Check | Description |
| --- | --- |
| Chip PAN Entry â Offline PIN verification | Normally, this setting is checked for almost all chip cards. Please refer to your chip card profile (CPV report) to ensure Offline PIN is among the CVM methods supported. |
| Chip PAN Entry â Online PIN verification | The Online PIN verification setting is normally checked for almost all chip cards. Please refer to your chip card profile (CPV report) to ensure Online PIN is among the CVM methods supported. |
| Chip PAN Entry â Signature verification | Transactions with signature could be disallowed with this setting. This is not recommended because the terminal might not support PIN Entry at all, the PIN pad might be broken, or the PIN on the card might be blocked. Most common usage of this setting could be to restrict the card usage with PIN based transactions only. |
| Chip PAN Entry â No CVM Required | Occasionally, CVM cannot be applied when there is no common CVM method between card and terminal. These transactions might be considered as risky. |
| Chip PAN Entry â No verification | This setting can be used to decline chip transactions without any valid CVM check result. |

## Contactless Magstripe

Contactless Magstripe is the inferior method for performing contactless transactions. Usage of this technology is generally restricted, but may be allowed or required in certain regions and countries. Please check with your Thredd account manager to enable this feature.

## ARC (ARPC Response Code) Instructions

ARC is a field that is sent in response messages to provide the card's instructions for current and next transactions. This feature is currently enabled for Mastercard cards only. The following instructions can be submitted to chip cards:

| CVM Check | Description |
| --- | --- |
| If declined, force next transaction online | The card will not be able to do offline transactions until a transaction is approved online. |
| Force next transaction online | This is a mechanism to disable offline transactions. Not recommended to set if the cards are expected to do offline transactions. |
| If zero or negative balance, force next transaction online | This setting also prevents offline transactions, but only if the balances on the Thredd host side is not positive. It is useful setting to prevent offline transactions for risky customers. |
| Reset EMV counters to offline limits | This is another mechanism to prevent offline transactions. Available funds on the card for doing Offline transactions effectively becomes zero. This setting is not recommended if the cards are intended for offline usage. |