# 3.1 Overview

When a cardholder uses a card at a merchantâs website or store, the merchant takes payment (enters the payment amount and cardholder details). The merchant may use the services of a payment service provider (PSP) to process the payment (i.e., provide the physical card reader or online payment gateway). The payment is passed to the acquirer, who then connects to the card scheme. The card scheme then passes the authorisation request to the issuer for approval.

For program managers using Thredd as their issuer-processor, Thredd receives the authorisation request directly from the card scheme and provides an authorisation response (approve or decline).  See the figure below.

![](../Resources/Images/Intro_card_payments/Overview.png)

Figure 10: Typical Flow for an Authorisation Request

The Figure above is a simplified view which does not include 3D secure authentication