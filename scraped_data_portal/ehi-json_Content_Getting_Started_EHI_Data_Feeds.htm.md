# 1.10 EHI Data Feeds

The EHI can be used as a source of read-only transactional data. For each transaction that Thredd processed, the EHI sends a notification message to your external host system (i.e., to the external host URL endpoint you have requested for your programme). The notification message contains all key attributes of the processed transaction. As with the authorisation advice, the notifications are sent to the external host in real time.

The sections below list the most important fields for each type of message. For details of all the fields in the GetTransaction message, see [GetTransaction Messages](../Requirements/GetTransaction_Message.htm). For details of the fields in the Cut Off message, see [Cut Off Message.](../Requirements/Cut_Off_Messages.htm)

## 1.10.1 GetTransaction message: Real-time transactional data feed fields

Data that is passed to the external host in transaction messages includes the following fields:

|  |  |  |
| --- | --- | --- |
| Actual Balance (`ActBal`) | Available Balance (`Avl_Bal`) | Billing Amount (`Bill_Amt`) |
| Billing Currency (`Bill_Ccy`) | Blocked Amount (`BlkAmt`) | Customer Reference (`Cust_Ref`) |
| FX Padding (`FX_Pad`) | Fixed Fee (`Fee_Fixed`) | Rate Fee (`Fee_Rate`) |
| Merchant Category Code (`MCC_Code`) | Padding (`FX_Pad`) | Note (`Note`) |
| Settlement Amount (`Settle_Amt`) | Settlement Currency (`Settle_Ccy`) | Token (`Token`) |
| Transaction Link ID (`Trans_link`) | Transaction Amount (`Txn_Amt`) | Transaction Currency (`Txn_CCy`) |
| Transaction Country (`Txn_Ctry`) | Transaction Description (`Txn_Desc`) | Transaction ID (`TXn_ID`) |
| Transaction Date (`Txn_Thredd_Date`) | Transaction Status (`Txn_Stat_Code`) | Transaction Type (`Txn_Type`) |
| Status Code (`Status_Code`) | Processing Code (`Proc_Code`) |  |

## 1.10.2 GetTransaction message: Authorisation, presentment and financial transactions fields

Authorisation, presentment and online financial transactions include the following additional attributes:

|  |  |  |
| --- | --- | --- |
| Transmission Date and Time (`TXN_Time_DE07`) | Local Transaction Date and Time (`POS_Time_DE12`) | Acquiring Institution ID (`Acquirer_id_DE32`) |
| Authorisation Code (`Auth_Code_DE38`) | POS Terminal ID (`POS_Termnl_DE41`) | Merchant ID (`Merch_Net_id`) |
| Merchant Name (`Merch_Name`) | Card Network Reference (`Traceid_Message`) | Response Code (`Responsestatus`) |
| Point-of-Service (POS) Data (`POS_Data_DE22`) | MCC Code (`MCC_Code`) | MCC Description (`MCC_Desc`) |

## 1.10.3 Cut off message fields

In addition to the real-time transaction data feed, you can opt to receive cut off messages (Cut\_Off) at predefined intervals which contain the following data:

|  |  |  |
| --- | --- | --- |
| Product ID (`ProductID`) | Cut off Date (`CutoffDate`) | Authorisations Acknowledged (`Auths_Acknowledged`) |
| Authorisations Not Acknowledged  (`Auths_NotAcknowledged`) | Financials Acknowledged  (`Financials_Acknowledged`) | Financials Not Acknowledged  (`Financials_NotAcknowledged`) |
| Loads Acknowledged  (`LoadsUnloads_Acknowledged`) | Loads Not Acknowledged  (`LoadsUnloads_NotAcknowledged`) |  |
| Balance Adjustment Expiry Acknowledged  (`BalanceAdjustExpiry_Acknowledged`) | First Transaction ID (`FirstTxn_ID`) |  |