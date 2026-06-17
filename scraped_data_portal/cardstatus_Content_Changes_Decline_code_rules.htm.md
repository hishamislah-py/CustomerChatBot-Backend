# 1 Rules for Decline Response Codes

Visa and Mastercard implemented rules in October and November 2021 which required issuers (BIN sponsors) and acquirers to properly use and manage declined transaction response codes, eliminate excessive reattempts and ensure data consistency in authorisation transactions. The schemes enforce penalty fees to increase compliance with these rules. These rules apply to issuers in Europe, AP, Canada and CEMEA.

To support the scheme rules, Thredd provides suitable card status codes and response fields to use in your EHI response messages where you decline an authorisation request.

Your systems should return appropriate response codes when you decline transaction authorisation requests (relevant if you are using EHI modes 1, 2 and 4).

## 1.1 Mastercard Rules

* AN 4536 - Effective 2nd November 2021[1  Refer to the Mastercard document: Revised Standards for the Decline Reason Code Service for Card-Not-Present Transactions.](#): No more than 5% of card-not-present declines should use the â05â (do not honour) response code[2  Scheme penalty fees for non-compliance are charged directly to the Issuer, who may pass these charges on to you.](#). In your EHI response, you should return an appropriate response code to reflect the reason for the decline and reduce the use of the generic 05 code. For details, see [Decline Response Code Categories](EHI_Response_Codes.htm#_Decline_Response_Code).
* AN 4536 / AN 4811 - Effective 1st October 2021: Thredd returns a Merchant Advice Code (MAC) field in our authorisation response to Mastercard, which provides more information to the merchant on the reason for a decline. In your EHI response, you can return an optional MerchantAdvice field to set the value of this response field. If not used, Thredd will return a default response. For details, see [EHI Field MerchantAdvice](EHI_Response_Codes.htm#_New_EHI_Field).
* *AN 6409 - Effective 1st July 2025*: No more than 1% of Refund Declines should use the '57' (Transaction not permitted to issuer/cardholder) response code. In your EHI response, you should return an appropriate response code to reflect the reason for the decline. For details, see the Decline Response Code Categories. Thredd is no longer using 57 Refund Declines. For details, see [EHI Response Codes](EHI_Response_Codes.htm#top).

Issuers should now use Response Code 58 for refund declines. Thredd systems have been updated to use Response Code 58.

## 1.2 Visa Rules

* Article 5.1 - Effective 1st October 2021[3  Refer to the Visa document: October 2021 and January 2022 VisaNet Business Enhancements: VisaNet Global Technical Letter and Implementation Guide](#): Avoid using generic decline codes (such as 05 â do not honour), for both card-present and card-not-present declines. For a list of suitable codes to use, see [Decline Response Codes](Card_Status_Codes.htm#_Decline_Response_Codes)
* You must use a suitable response code for refund request approvals and declines. See [Response Codes for Refund Requests](EHI_Response_Codes.htm#_Response_Codes_for).
* Response codes 12 and 15 are Visa-only codes effective from 12 April 2025. If an Issuer uses these codes incorrectly, then Visa will convert the response and send it to the Acquirer as a generic response code decline. See [EHI Response Codes](EHI_Response_Codes.htm).
* Visa have stipulated that response codes 04, 07, 14, 41, 43, and 46 are only used for listing permanently closed or invalid accounts. If these codes are used for an account that is subsequently reopened, a new PAN should be issued.
* Effective 18 October 2025: Visa have stated that Response Code 57 (Transaction not permitted to cardholder) cannot be used for individual PANs to generically decline a transaction. Please note:

  + Response code 57 can still be used if the decline condition applies to all PANs for the same product.
  + If code 57 is used for individual PANs after 18th October, Visa will convert it to a generic response code decline. You should be aware that excessive use of generic response codes above Visaâs thresholds will result in system integrity fees.
  + Note that any decline fees set up for response code 57 (using the Thredd Fees service) will no longer apply.
* Do not use Response Code 57 for Refund Declines.

  You must use Response Code 58. Thredd systems have been updated to use Response Code 58.

Thredd recommends that these rules are respected in authorisation responses.

## 1.3 Thredd Status Codes

Thredd provides a number of card status codes which you can use to set the status of your cards to support decline response reporting. See [Card Status Codes](Card_Status_Codes.htm#_Changes_to_Card).