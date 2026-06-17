# 4.5 Calculating the Total Transaction Cost

When the External Host decides whether to approve or decline the transaction, it takes into account the total cost of the transaction, which is the sum of:

* Billing amount (`Bill_Amt` field)
* Fixed Fees (`Fee_Fixed` field)
* Rate variable Fees (`Fee_Rate` field)
* Foreign Exchange Padding (`Fx_Pad` field)
* MCC Padding (`MCC_Pad` field)

Example:

| Bill\_Amt | Fee\_Fixed | Fee\_Rate | Fx\_Pad | MCC\_Pad | Total amount blocked |
| --- | --- | --- | --- | --- | --- |
| 109.45 | 1.41 | 0.92 | 2.04 | 5.08 | 118.90 |

For use of this calculation in payment authorisation, see [EHI Operating Modes.](../Getting_Started/EHI_operating_modes.htm)