# 3.3 More about Message Types

Further details of the main types of card payment messages are provided below.

## 3.3.1 Online Authorisations

An online authorisation transaction is an authorisation message that requires real-time and immediate processing via the card payment network and an immediate response from the issuer. Examples of online authorisations include: 0100, 0101 and 0120 messages.

## 3.3.2 Authorisation Request

An authorisation request is an online authorisation message, processed in real-time, which requires Thredd or the program manager to approve or decline the transaction. If the card scheme does not receive a response from Thredd, they may either decline the transaction or provide fallback approval (if configured for your card programme). 0100 and 0101 are examples of acquirer authorisation request messages.

## 3.3.3 Authorisation Advice

Unlike an authorisation request, which requires Thredd or the program manager to approve or decline, an authorisation advice is used to indicate that an authorisation decision has already been made, and the advice is provided to inform you of the details.

In some instances, Thredd will generate and send you authorisation advices, which require an acknowledgement response to confirm you have received the message. 0120 is an example of acquirer authorisation advice messages.

## 3.3.4 Authorisation Reversal

This includes both authorisation reversal requests (0400) and authorisation reversal advices (0420). An authorisation reversal will partially or fully reverse a previous authorisation request or authorisation advice.

## 3.3.5 Financial Notification Messages

Financial notification messages are provided as part of the daily Visa and Mastercard clearing cycles and are not processed in real-time. Their purpose is to confirm the financial part of the transaction, in which funds are exchanged between acquirers and issuers. Thredd receives clearing files from the card schemes (containing batch records) and generates financial messages for each transaction within the file.

Presentments (1240) and chargebacks (1442) are examples of financial messages.