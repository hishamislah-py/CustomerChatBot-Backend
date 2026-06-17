# Reset Counters

You can use the Thredd API to
reset transaction and amount counters (since the last strongly-cardholder-authenticated transaction) on a card or payment-token, to re-enable transactions which are blocked as a result of the transaction and amount counters exceeding the defined maximum limits for not secure enough transactions.

* To reset the counters for a contactless transaction, use the **Clear Accumulator** (`Ws_ResetAccumulator`) web service, with `AccumulatorType` = 1.
* To reset the counters for an e-commerce transaction, use the **Clear Accumulator** (`Ws_ResetAccumulator`) web service, with `AccumulatorType` = 2.

For more information, see the [Web Services Guide > Clear Accumulator](https://docs.thredd.ai/webservices/Content/Web_services_api/Clear_Accumulator.htm).