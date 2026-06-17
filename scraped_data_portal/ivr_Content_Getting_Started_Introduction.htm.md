# 1 Introduction

This topic introduces the Thredd Interactive Voice Response (IVR) service which enables customers to call a phone number to perform various actions for their card.

Using this service, you can work with Thredd to set up the following actions that customers can use in IVR:

* Activate their Card
* Check their Available Balance
* Report their card Lost or Stolen
* Unblock / Get PIN
* Hear Terms and Conditions

## 1.1 What are the Benefits?

Using IVR, you can give cardholders a different way of performing actions for their card.

A major benefit of offering an IVR service is that many customer queries can be covered by an automatic service, without involving customer support.

The cardholder receives benefits too. They can get support on queries without needing to spend long periods of time in a queue and waiting to speak to a real person.

## 1.2 How does the IVR solution work?

The Thredd IVR service is based on Amazon Web Services Connect (AWS Connect). When a customer calls your designated phone number, the selection process is completed in AWS Connect. When the appropriate option has been selected by the cardholder, AWS sends a Web Service request to Thredd to perform the relevant action.

For more information about Amazon Connect, see: [Amazon Connect](https://docs.aws.amazon.com/connect/?id=docs_gateway).

When Thredd has performed the necessary action, it passes the results back to the cardholder via AWS.

![Chart

Description automatically generated](../Resources/Images/Overview.png)

Figure 1: Components in the Thredd IVR solution

The Thredd IVR service is configured at [Program Manager![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A Thredd customer who manages a card program. The program manager can create branded cards, load funds and provide other card or banking services to their end customers.](#) level (and will be available to all cards in your programme). To discuss initial IVR costs, speak to the Implementation team and then work with them to complete the IVR builder template.