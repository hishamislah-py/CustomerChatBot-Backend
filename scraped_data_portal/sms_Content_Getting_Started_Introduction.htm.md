# 1 Introduction

This topic introduces the Thredd mobile text messaging (SMS) solution which enables you to communicate better with your customers and enhance the customer experience.

Using this solution, you can send messages to customersâ SMS-enabled devices to provide [Personal Identification Number (PIN)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The 4 to 12 digit value known only to the cardholder, which they may enter at POS or ATM to authenticate themselves.](#) reminders and balance queries, perform card activation, and block and unblock cards.

You can automate SMS messages or initiate them at scheme master level.

You use Thredd Web Services to trigger the SMS messages, using the **SmsBalance** or **Sms\_Required** parameters for API calls such as **Card Activate** (`Ws_Activate`)[1  In Card Activate (Ws\_Activate), the SMS parameter is capitalised as âSMSBalanceâ](#), **Card Activate and Load** (`Ws_Activate_Load`), **Card Load** (`Ws_Load`) etc. For a full list of the calls that provide SMS parameters, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm).

The SMS service is currently only supported via our SOAP-based web services and is not available on the Thredd REST-based Cards API.

Thredd charge a fee for sending SMS messages. Refer to your Thredd contract for details.

If your programme is sending SMS messages to cardholders with a Singapore mobile number (starting +65), contact your account manager or Thredd representative to be advised on specific Singapore regulation.

## 1.1 What are the Benefits?

Using SMS messaging, you can give customers more control over their accounts and improve accessibility for cardholders. The following examples show how you can use SMS messaging in your deployment.

### 1.1.1 Send Customised Messages

Messages can be configured and sent to customers based on an âeventâ such as card activation or a balance enquiry. You can either configure your own messages to use for events or use the default messages provided. For a list of the default messages, see [Appendix A â Default messaging](../Reference/Appendix_A_Default_messaging.htm#_Appendix_A_â).

Messages can be configured using standard variables (denoted by the % symbol) which you substitute with your own data. Messages of up to 150 characters can be sent.

You can also specify when a message is to be sent and the language used. The language of the message is based on the country of residence of the cardholder. For more information about where to find this information on the Card Master screen, see the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).

#### Use Case: Standard Activation Message

You can send a message on card activation; for example: âYour card ending \*\*\*\*%PAN4% is active now. [CVV![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Card Verification Value. A 3-digit number which provides added security.](#) number relating to the card is: %CVV%. Thank youâ, where %PAN4% is substituted with the masked [PAN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The cardâs 16-digit primary account number (PAN) that is typically embossed on a physical card.](#) (containing only the last 4 digits) and %CVV% is the card verification value.

### 1.1.2 Add Security

You can send SMS messages to customers to notify them of when changes are made to key data fields. For example, you can message a cardholder when loads have been made and funds are available.

You do this by sending details of the transaction amount and balance using the **SmsBalance** or **Sms\_Required** parameters for API calls such as **Card Activate** (`Ws_Activate`)[2  In Card Activate (Ws\_Activate), the SMS parameter is capitalised as âSMSBalanceâ](#), **Card Activate and Load** (`Ws_Activate_Load`), **Card Load** (`Ws_Load`) etc.

For a full list of the calls that provide SMS parameters, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm).

#### Use Case: Load Message

You can send a message to notify customers when a load has been made and funds are available: âAn amount of %CURCODE% %AMT% loaded to your Card ending with \*\*\*\*%PAN4%. Your current balance is %CURCODE% %CBAL%. Thank Youâ, where %CURCODE% is the Currency Code, %AMT% is the amount, %CBAL% is the current balance, and %PAN4% is substituted with the masked PAN (containing only the last 4 digits).

### 1.1.3 Send a PIN

You can send an SMS message containing a customerâs PIN using the **Card PIN Control** (`WS_PinControl`) web service, with the **Sms\_Required** field.

For example, you can use this feature when a card PIN has been blocked and needs to be regenerated. This means customers do not need WIFI or to use an application when out and about; instead, they can receive messages direct to their mobile device and continue to access their funds.

#### Use Case: Send PIN

You can send an SMS message to customers containing a PIN number. For example, âDear %FNAME%, your PIN for your card ending %PAN4% is: %NEWPIN%. Kind Regards, %SENDER%â, where %FNAME% is the customerâs name, %PAN4% is substituted with the masked PAN (containing only the last 4 digits), %NEWPIN% is the PIN number, and %SENDER% is your details (the program manager).

### 1.1.4 Comply with PCI Regulations

Information containing a full PAN, either stored or transmitted, is governed by [PCI![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Payment Card Industry. This body sets standards and security requirements for organisations that process debit and credit card transactions.](#) rules. To remain PCI compliant, you can send an SMS message to communicate specific information only to customers.

#### Use Case: Virtual Cards

To avoid the need for your front-end application to be fully PCI compliant, you can communicate the expiry date, CVV and the first 6 and last 4 digits of a virtual card in the card image sent by the application, and then use SMS to send the remainder of the PAN. For more information, see the [Virtual Cards Guide](https://docs.thredd.ai/Virtual_Cards_Guide.htm).

## 1.2 How does the SMS Solution Work?

The Thredd SMS solution is based on [Amazon Pinpoint![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Amazon Pinpoint is a fully managed messaging service which enables you to send notifications directly to your customers.](#). Amazon Pinpoint enables you to send notifications directly to your customersâ SMS-enabled devices. It supports SMS text messaging to over 200 countries, mobile push notifications to Amazon, Android, Apple, Baidu, and Microsoft devices, and also email notifications.

For more information about Amazon Pinpoint, see: [Amazon.com: Pinpoint](https://aws.amazon.com/pinpoint/).

For Thredd to send SMS messages to the cardholder via Amazon Pinpoint, Thredd uses an internal web API called Thredd Messenger. Thredd Messenger processes and forwards the SMS message to Amazon Pinpoint which, in turn, sends it to customers.

The figure below shows the components involved in the Thredd SMS solution.

![Chart

Description automatically generated](../Resources/Images/SMS_solution.png)

Figure 1: Components in the Thredd SMS solution

## 1.3 How do I get the new SMS Service?

To benefit from the new SMS solution, contact your Thredd Business Development Manager or Account Manager.

Thredd will then work with you to configure the SMS solution as follows:

1. Using Smart Client, Thredd configures the SMS provider at program manager level.
2. You select the countries the SMS messages will be sent in. For a list of supported regions and countries see: <https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html>
3. You select the SMS messages you want to send to clients, and Thredd configures these at scheme master level.
4. You test the SMS service in the UAT environment using any token with a mobile telephone number correctly assigned to it.
5. After testing, Thredd will make the solution live.