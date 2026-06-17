# 5.5 Security and Fraud Management

Managing risk is always a trade-off. You can only make your cards 100% secure by not allowing any transactions. The risk of fraud needs to be balanced against the flexibility and ease of use you want to enable for your customers. Thredd offers a number of products and services to help you reduce the incidents of fraud.

## 5.5.1 Cardholder Verification Checks

These are checks that merchants can use to verify the identity of the cardholder:

* **Signature**: A manual check by the merchant that the signature matches the one on the back of the card.
* **PIN verification**: Typically a 4-6 digit personal identification number (PIN) is entered by the customer at a POS terminal or ATM and verified by Thredd or the chip card. PINs are blocked after three incorrect attempts. You can change card PINs and unblock PINs using the Thredd Web Services.
* **Address Verification Service (AVS)**: An AVS check compares the billing address used in the transaction with the issuing bankâs address information on file for that cardholder. Depending on whether they match fully, partially, or not at all, the merchant can use that information in their decision on whether to accept an order. AVS is one of the most widely used fraud prevention tools in card-not-present transactions. The usage of AVS varies, depending on the country.
* **3D Secure authentication**: 3D Secure (3-domain structure), also known as Payer Authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa, Mastercard and Discover. For more information on Thredd support for 3D Secure, see [Thredd Docs Portal: Cardholder Authentication (3D Secure)](https://docs.thredd.ai/More_Information/Cardholder_Authentication.htm).

## 5.5.2 Card Verification and Security Checks

When the card is used, there are a number of card verification and security checks that can be performed at the point of sale, to validate that the card is a genuine card:

* **Card Verification Value/Code 1 (CVV1 or CVC1**): A 3-digit number which is located on the cardâs magnetic stripe tracks 1 and 2. It is used to help prevent fake magnetic stripe transactions, but is vulnerable to copying if someone can see the original magnetic stripe data.
* **Card Verification Value/Code 2 (CVV2 or CVC2)**: A 3-digit number which is located on the card, which is entered by the customer in an e-commerce transaction. It is used to help prevent fraud in card-not-present transactions, since only the cardholder should be able to see this number.

## 5.5.3 Fraud Transaction Monitoring

Using adaptive behavioural analytics and machine learning, Fraud Transaction Monitoring adapts to new fraud types and identifies unknown threats by detecting unexpected changes (anomalies) in real-time data. This improves transaction monitoring, identifies fraud and reduces the number of occurrences where legitimate transactions are flagged as suspicious, payments are stopped or accounts locked. For more information, see [Thredd Docs Portal: Fraud Transaction Monitoring](https://docs.thredd.ai/More_Information/Fraud_Monitoring.htm).

## 5.5.4 Card Control Groups

Thredd provides a number of options to enable you to manage the risks associated with card payments. For example:

* **Limit groups**: Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded.
* **Usage groups**: Group that controls where a card can be used. For example: Point of Sale (POS) or ATM.

Card control groups are set up at the time when you first implement your card program through Thredd. The control groups linked to a card can be changed dynamically using the Thredd web services or cards API (which you use via your customer app to enable your cardholders to control their card spending limits and card usage).

## 5.5.5 Permission Lists

You can configure allow and disallow lists which determine where a card can be used, based on the Merchant ID or Merchant Category Code (MCC).

## 5.5.6 Cardholder Authentication (3D Secure)

Cardholder authentication, also known as Payer Authentication, is a security process that protects both cardholders and merchants by verifying the cardholder's identity during an online transaction. Examples of cardholder authentication programs are Verified by Visa and Mastercard Identity Check, which are both implementations of 3D Secure.

The latest 3D Secure solutions support 2-factor authentication and Strong Customer Authentication (SCA), through means such as biometric identification.

Thredd offers a fully integrated 3D Secure service for both Mastercard and Visa cards. For more information, see [Thredd Docs Portal: Cardholder Authentication (3D Secure)](https://docs.thredd.ai/More_Information/Cardholder_Authentication.htm).