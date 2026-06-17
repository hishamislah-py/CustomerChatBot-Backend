# 3.1 Cut-Off Message Example

This section provides an example of a cut off message and response.

If you are set up to receive EHI in JSON format, you will also receive cut-off messages in JSON format.

EHI\_JSON\_Guide\_5.5 The EHI feed does not send JSON fields to externally-hosted systems where the values for the field data are blank. This is different from EHI feeds with XML fields where the feed can send blank values.

## 3.1.1 Example Cut-Off Request Message

[Copy](javascript:void(0);)

```
  {  
   "CutOffId":38077,  
   "ProductId":99883,  
   "CutOffDate":"2022-11-29 13:00:01.837",  
   "FirstTransactionId":6154805771,  
   "LastTransactionId":6154805771,  
   "AuthsAcknowledged":1,  
   "AuthsNotAcknowledged":0,  
   "FinancialsAcknowledged":0,  
   "FinancialsNotAcknowledged":0,  
   "LoadsUnloadsAcknowledged":0,  
   "LoadsUnloadsNotAcknowledged":0,  
   "BalanceAdjustExpiryAcknowledged":0,  
   "BalanceAdjustExpiryNotAcknowledged":0  
   }
```

## 3.1.2 Example Cut-Off Response Message

This is an example response to the above example request message, showing the HTTP Response body data:

[Copy](javascript:void(0);)

```
{"Acknowledgement":"1"}
```