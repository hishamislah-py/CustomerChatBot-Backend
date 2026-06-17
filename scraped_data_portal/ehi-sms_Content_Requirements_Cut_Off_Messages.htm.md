# 2.5 Cut\_Off Messages

You can optionally enable receiving batch cut-off messages which provide summary information of the data sent via EHI. The frequency of cut-off messages is configurable.

The recommended frequency is 2-3 times per day.

## 2.5.1 Message Fields

The following fields are included in the *Cut\_Off* message:

| Field | Description | Data type  (min, max) | Sample Data | Usage |
| --- | --- | --- | --- | --- |
| CutoffID | A unique identifier of the cut\_off message. | N(1,9) | 12 | Mandatory |
| ProductID | The Product ID of the card. | N(1,9) | 1504 | Mandatory |
| CutoffDate | Date and time of this cut\_off message. | Datetime  (Y\_to\_nnn) | 2021-03-02 13:16:42.999 | Mandatory |
| FirstTxn\_ID | First Txn\_ID in this cut\_off period.  Maximum is 2^63-1. | N(1,19) | 1234564 | Mandatory |
| LastTxn\_ID | Last Txn\_ID in this cut\_off period.  Maximum is 2^63-1. | N(1,19) | 4523587 | Mandatory |
| Auths\_Acknowledged | Number of acknowledged Authorisations during this cut\_off | N(1,9) | 5000 | Mandatory |
| Auths\_NotAcknowledged | Number of un-acknowledged Authorisations during this cut\_off | N(1,9) | 100 | Mandatory |
| Financials\_Acknowledged | Number of acknowledged Financials during this cut\_off | N(1,9) | 5000 | Mandatory |
| Financials\_NotAcknowledged | Number of un-acknowledged Financials during this cut\_off | N(1,9) | 100 | Mandatory |
| LoadsUnloads\_Acknowledged | Number of acknowledged Loads/Unloads during this cut\_off | N(1,9) | 5000 | Mandatory |
| LoadsUnloads\_NotAcknowledged | Number of un-acknowledged Loads/Unloads during this cut\_off | N(1,9) | 100 | Mandatory |
| BalanceAdjustExpiry\_Acknowledged | Number of acknowledged Balance Adjustment and Expiry during this cut\_off | N(1,9) | 5000 | Mandatory |
| BalanceAdjustExpiry\_NotAcknowledged | Number of un-acknowledged Balance Adjustment and Expiry during this cut\_off | N(1,9) | 100 | Mandatory |

## 2.5.2 Response Message Fields

The following fields must be present in the Cut\_off response message:

| Field | Description | Data type  (min,max) | Sample Data | Usage |
| --- | --- | --- | --- | --- |
| Cut\_OffResult | Valid values:  0 = Not Acknowledged (in a future release, Thredd may re-transmit the cut off message.)  1 = Acknowledged | N(1,1) | 1 | Mandatory |