# Soft Declines

Where a transaction does not meet the PSD2 SCA rules, Thredd soft declines and sends back the instruction to the merchant to authenticate the cardholder using SCA.

## Soft Decline - Card Not Present (e-Commerce)

For a card not present e-commerce transaction, the merchant should retry using 3D Secure.

The figure below summarises the transaction process, including what happpens when Thredd soft-declines.

![](../Resources/Images/e-commerce_soft_decline.png "Soft Decline: Card Not Present")

Figure 11: Soft Decline - Card Not Present Transaction

## Soft Decline Card Present (Contactless)

For a card present contactless transaction, the POS terminal either:

* asks the cardholder to insert their card and enter their PIN. The terminal then sends a new transaction that has been PIN verified

  -or-
* asks the cardholder to enter their PIN. The terminal then sends a new transaction, for the same amount and with same chip data, but this time including the online PIN.

To support the soft decline flow, the POS terminal must be able to read the card chip and accept a PIN.

The figure below summarises the transaction process, including what happpens when Thredd soft-declines.

![](../Resources/Images/Card_present_soft_decline.png "Soft Decline: Card Present")

Figure 12: Soft Decline - Card Present Transaction

## Soft Declines and Thredd Response Codes

For details of Thredd response codes for soft declines, see the table below.

| Scenario | Thredd internal response code | Mastercard response code sent | Visa response sent |
| --- | --- | --- | --- |
| Card present, terminal supports PIN | C1 | 65 requires SCA  With single tap response = Yes ((i.e., repeat transaction with online PIN) | 70 PIN required |
| Card present, terminal does not support PIN | C0 | 65 requires SCA | 1A SCA required |
| Card not present (e.g. e-commerce) | C0 | 65 requires SCA | 1A SCA required |

For Mastercard, the *single tap response = yes* (i.e. repeat transaction with online PIN) is sent if the terminal indicates it supports this and it was a contactless transaction. The single tap response can also be sent for internal response C0, if the terminal indicates it supports repeating the transaction with online PIN.