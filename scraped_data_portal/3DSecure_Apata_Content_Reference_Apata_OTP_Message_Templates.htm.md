# Appendix 2: OTP Message Templates

This section provides examples of the message templates for OTP SMS and OTP Email.

## OTP SMS

If you are customising the text, Thredd recommend you keep your message brief. Otherwise, the message is split into multiple parts, which are sent separately.

#### Default Template (Full)

The template can contain OTP, Card Number (last 4 digits), Currency, Amount and Merchant Name:

[Copy](javascript:void(0);)

```
English:{{OTP}} is the One Time Passcode required for completing a purchase of {{CUR}} {{Amount}} at {{MerchantName}}   
with the last four digits of your card ending in {{CardNumber}}.   
Please use the One Time Passcode to complete the transaction.
```

The *{{CardNumber}}* is the last 4 digits of the card number.

#### Shortened Template

The template can only contain the OTP and card number:

[Copy](javascript:void(0);)

```
{{OTP}} is the 3DS OTP from card ending by {{CardNumber}}.   
Please use the OTP to complete the transaction. 
```

## OTP Email

The OTP Email template requires you to share the following information with Thredd before it can be used:

* A 200 x 70px PNG file of your company logo
* The wording for the email body
* The website for your company

See the following example of the wording for the OTP Email template:

[Copy](javascript:void(0);)

```
Please confirm your payment of {{Currency}} {{Amount} to {Merchant Name} using the code {{OTP}}            
```

Additionally, you need to configure the OTP email to ensure that emails sent to customers are seen as coming from your domain. For information, see [How do we set up OTP email so that the cardholder receives an email from our email domain?](../FAQs_Apata.htm)