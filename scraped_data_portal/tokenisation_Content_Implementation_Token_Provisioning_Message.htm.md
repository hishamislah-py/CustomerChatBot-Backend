# 7 Token Provisioning Message Flows

For token provisioning there are several messages that are sent between the Token Service Provider and Thredd. These are a mixture of ISO 8583 (for VDEP and MDES) and JSON API (for VDEP only) formats. All ISO 8583 messages and One Time Passwords (OTPs) obtained are sent over EHI to the Program Manager[1  ISO 8583 is the message format used for authorisation messages passed between Visa/Mastercard and Thredd.](#).

All EHI messages in the Token Provisioning flow (TAR/TEN/TCN) are advices only. This means that for all EHI modes you are not able to authorise TAR, TEN or TCN advices. You can use these messages to confirm to the cardholder the tokenisation status. They should never be used for payment authorisation approval or decline decisions.

Figures 12-15 below describe the Visa and Mastercard messages that are received for token provisioning requests. Note that since these are asynchronous messages, it is possible they may arrive out of sequence.

## 7.1 Message flow for Mastercard Token Provisioning (Green Flow)

![](../Resources/Images/Message_flow_MC_green.png)

Figure 13: Mastercard Messages (Green Flow)

1. Mastercard sends an 0100 Token Activation Request (TAR).
2. Thredd returns an Approve response to Mastercard together with the Profile ID (if applicable) so that the token response displays the correct card art and T&Cs on the cardholderâs mobile device screen.   
   Thredd forwards the TAR to the Program Manager, via EHI.
3. Mastercard sends an 0100 Token Complete Notification (TCN).   
   Thredd forward the TCN notification to the Program Manager, via EHI.

## 7.2 Message flow for Mastercard Token Provisioning (Yellow Flow)

![](../Resources/Images/Message_flow_MC_yellow.png)

Figure 14: Mastercard Messages (Yellow Flow)

1. Mastercard sends an 0100 Token Activation Request (TAR).
2. Thredd returns an Approve with Authentication response to Mastercard. The response includes the available cardholder verification methods (e.g., SMS) and the Profile ID (if applicable).  
   Thredd forwards the TAR advice to the Program Manager, via EHI.
3. Mastercard sends an 0100 Activation Code Notification (ACN).   
   Thredd forward the ACN notification (plus the passcode and verification method) to the Program Manager, via EHI.
4. Mastercard sends an 0100 Token Complete Notification (TCN).   
   Thredd forward the TCN notification to the Program Manager, via EHI.

## 7.3 Message flow for Visa Token Provisioning (Green Flow)

![](../Resources/Images/Message_flow_VTS_green_flow.png)

Figure 15: Visa Messages (Green Flow)

1. Visa sends a message to Thredd to check if the PAN is eligible for tokenisation.   
   Thredd returns the Profile ID (if applicable) so that the token response displays the correct card art and T&Cs on the cardholderâs mobile device screen.
2. Visa sends an 0100 Token Activation Request (TAR) to Thredd.
3. Thredd returns an Approve response to Visa.  
   Thredd forwards the TAR to the Program Manager, via EHI.
4. Visa sends an 0620 Token Event Notification (TEN) to Thredd, to indicate the token has been created.   
   Thredd forwards the TEN notification to the Program Manager, via EHI.
5. For a token that is bound to a device, Visa sends an 0620 Token Event: Token Complete Notification (TCN), to indicate the token has been provisioned onto the device.   
   Thredd forwards the TCN notification to the Program Manager, via EHI.

## 7.4 Message flow for Visa Token Provisioning (Yellow Flow)

This flow is only relevant to tokens that are bound to a mobile phone or other device.

![](../Resources/Images/Message_flow_VTS_yellow_flow.png)

Figure 16:  Visa Messages (Yellow Flow)

1. Visa sends a message to Thredd to check if the PAN is eligible for tokenisation.   
   Thredd returns the Profile ID (if applicable) so that the token response displays the correct card art and T&Cs on the cardholderâs mobile device screen.

2. Visa sends an 0100 Token Activation Request (TAR) to Thredd.
3. Thredd returns an Approve with Authentication response to Visa.  
   Thredd forwards the TAR to the Program Manager, via EHI.
4. Visa sends an 0620 Token Event Notification (TEN) to indicate the token has been created (the token is not yet active)
5. Visa uses the Get CVM API to retrieve a list of available cardholder verification methods (CVMs) for this token from Thredd (i.e., methods such as SMS).
6. Visa uses their Send Passcode API to send the passcode and the user-selected cardholder verification method to Thredd.  
   Thredd sends an Activation Code Notification (ACN) to the Program Manager, via EHI. The ACN contains the authentication passcode (One-time password) and user-selected verification method.
7. The OTP is delivered to the cardholder using their chosen verification method. Visa sends an 0620 Token Event: Token Complete Notification (TCN), to indicate the token has been provisioned onto the device.   
   Thredd forward the TCN notification to the Program Manager, via EHI.
8. Visa sends an 0620 Token Event Notification (TEN) to Thredd, to indicate the token authentication was successful. The token is now active. Thredd forwards the TEN notification to the Program Manager, via EHI.

Some Mobile Wallet token requestors require you to confirm to cardholders when the tokenisation process is complete or to follow up with cardholders when tokenisation has not been completed.

The Token Complete Notification (TCN) sent over EHI currently indicates when the device is successfully provisioned. In some cases, later Token Event Notifications (TENs) can arrive once the cardholder is authenticated and Visa has activated the token, which represent the actual end of the token provisioning flow.   
  
The section [When to notify cardholders tokenisation is complete](#_When_to_notify) below describes how you can identify the end of the tokenisation flow.

## 7.5 When to notify your cardholders that Tokenisation is complete

Mastercard sends Thredd a Token Completion Notification (TCN) which identifies when the tokenisation process is complete. We send you the Token Completion Notification (`ProcCode` 350000). You must notify your customers within 30 minutes of successful provisioning and activation of the token (an Apple requirement).

For Visa, currently the Token Completion Notification (`ProcCode` 350000) only represents the end of the tokenisation flow for Green Flow Device Tokenisation.  Visa send a 620 message to indicate that the token is active. Thredd then send a Token Complete Notification (TCN) where the `paymenttoken_creatorStatus` = A (active). For details, see [Visa Tokenisation Messages](../References/Visa_Tokenisation.htm).

## 7.6 Token Requestor Testing

Some Mobile Wallet Token Requestors require completion of testing before go-live.  Please inform your Implementation Manager before this testing has started. Thredd do not receive updated test requirements from Mobile Wallet Token Requestors as we do not have a direct relationship with these parties.

If you become aware of a recent change in the Apple or Android requirements, please contact your Account Manager or Implementation Manager before testing begins so Thredd can review.

## 7.7 Mastercard Provisioning Velocity Limits

Mastercard include provisioning velocity limits for MDES to enable the tackling of reprovisioning fraud in some public transport environments where authorisations are deferred. The provisioning velocity limits apply to a PAN and its associated device tokens.

### How it Works

Mastercard blocks the provisioning if any of the following velocity limits are met:

* 4 provisions per day.
* 5 provisions for 7 days.
* 6 provisions for 30 days.

Velocity limit combinations are managed separately for each device associated with a PAN. For example, if the provisioning velocity limit is 6 provisions for 30 days, the monthly limit is applied to both a smart watch and a phone that is linked to the PAN.

Thredd are not able to amend these limits. The limits are separate to the ones that Thredd manages internally.

### Overriding the Limits

A customer service agent can override an individual provisioning velocity limit for each device and PAN combination for 30 minutes through a customer service portal. Alternatively, provisioning velocity limits can be overriden for a given PAN by adding to a whitelist in MDES Manager.

### Opting in for Velocity Limit Provisioning

You can opt in for velocity limit provisioning by emailing `digital.support@mastercard.com`.

Mastercard may also contact you if you have opted out of token reuse, and/or if fraud is detected on one or more devices.