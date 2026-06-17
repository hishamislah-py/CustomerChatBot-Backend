# Appendix G: Realtime Token Status Change

This section provides more information on how the process of token status change works.

## Real-time Token Status Change (Visa)

The following diagram shows the process of a token status change for Visa.

![](../Resources/Images/tokenisation_flow.png)

Figure 19: Real-time Token Status Change (Visa)

1. The Program Manager uses the Thredd web service to change the token status on the Thredd platform.

2. Thredd sends a request to Visa to update payment token status on their systems.
3. Visa responds with the token status update result.
4. Thredd confirms the status update in the web service response.
5. Visa sends a Token Event Notification (TEN) with the status change.
6. Thredd confirms the status update via EHI.

## Real-time Token Status Change (Mastercard)

The following diagram shows the process of a token status change for Mastercard.

![](../Resources/Images/Managing_your_Programme_1.png)

Figure 20: Token Status Change (Mastercard)

1. The Program Manager uses the Thredd web service to change the token status on the Thredd platform.
2. Thredd sends a request to Mastercard to update payment token status on their systems.
3. Mastercard responds with the token status update result.
4. Thredd confirms the status update in the web service response.
5. Mastercard sends a Token Event Notification (TEN) with the status change.
6. Thredd confirms the status update via EHI.