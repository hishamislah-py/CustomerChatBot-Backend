# 2.9 CardEvent

CardEvent records indicate status changes to a given card.

**Note**: These element is not applicable to the Discover Global Network.

| Child Element | Description | Data Type | Required | Constraints/  Permitted  Values |
| --- | --- | --- | --- | --- |
| Card | Details of the card used in the transaction. | <Card> | Yes | See the [Card](Sub_Elements_and_Attributes.htm#Card) sub-element |
| Event | Details of the event. | <Event> | Yes | See the [Event](Sub_Elements_and_Attributes.htm#Event) sub-element |

#### Example

[Copy](javascript:void(0);)

```
<CardEvent>  
    <Card PAN="5793048251657123" productid="1463" />  
    <Event Type="Activation" Source="2" ActivationDate="20240213161108" StatCode="" OldStatCode="" Date="20240213161108" transactionid="" />  
</CardEvent>
```