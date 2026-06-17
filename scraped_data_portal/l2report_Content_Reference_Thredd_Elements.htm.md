# 2.1 Thredd Elements

The following are Thredd elements within the Level 2 and 3 schema.

| Attribute | Description | Data Type | Required | Constraints/Permitted Values |
| --- | --- | --- | --- | --- |
| network | The Card Payment network. | xs:string | Yes | Visa, Mastercard, or Discover |
| transactionType | The type of transaction as offline or online. Offline transaction data is received in presentments, whereas Online transaction data is received in authorisations. | xs:string | Yes | Offline and Online |
| transactionId | The ID of the clearing transaction that has the enhanced data. | xs:unsignedLong | Yes | Must be a number |
| transactionLinkId | The ID of the link to the authorisation of the transaction if available. | xs:unsignedLong | Yes | If the transaction type is offline, this is the unique identification number of the corresponding online transaction. If the transaction type is online, the transactionlinkId and transactionId are the same. |