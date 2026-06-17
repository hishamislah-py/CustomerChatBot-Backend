# 4.37 Transaction Status Codes

The table below provides details of available Transaction Status Code ([`Txn_Stat_Code`](../Requirements/GetTransaction_Message.htm#Txn_Stat_Code)) values. (See also [Get Transaction Message fields: Txn\_Stat\_Code](../Requirements/GetTransaction_Message.htm#Txn_Stat_Code))

| Value | Description | Impacts Balance? |
| --- | --- | --- |
| A | Accepted | Yes. Authorised amount is blocked. |
| C | Cleared | No |
| I | Declined | No |
| S | Settled | Yes. The actual balance is adjusted by the settled amount. |
| V | Reversed | Yes. Reversed amount is unblocked (if matching authorisation found) |

When Thredd receives a presentment which matches an existing authorisation message, the Authorisation message status is updated to *Cleared (C)* and the Presentment message status is updated at the same time to *Settled (S)*. If Thredd controls the balance, we will adjust the balance by the settlement amount. If your systems control the balance, you can adjust the balance by the settled amount.