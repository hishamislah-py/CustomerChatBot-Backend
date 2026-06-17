# 8 Enroling your cards in 3D Secure

You can enrol your cards in 3D Secure using either the Thredd 3D Secure Enrolment Thredd API (using SOAP) or the Cards API (using REST). Your request must include the Thredd public token and the authentication type to use during authentication for this card (e.g., BIOMETRIC) and the value. For OTP SMS, you need to provide the mobile number as the value. For the Biometric authentication, the value is for your reference only. See [Using the Card Enrolment API](Using_Card_Enrolment_API.htm#_Using_the_Card_Enrolrement_API).

Thredd also provides an auto-enrolment option, which can be triggered either as a bulk update on all your existing cards not yet enroled or can be triggered at the time when you create a new card. See [Card Auto Enrolment](#_Card_Auto_Enrolment).

Thredd saves the card enrolment record in our database.

## 8.1 Card Auto Enrolment

If you are upgrading existing cards to 3D Secure, Thredd can automatically enrol all your cards[1 auto-enrolment includes cards created (in active, non-active or temporary blocked status), but excluded cards that are expired or permanently blocked.](#) in the Apata 3D Secure service: you can request auto-enrolment by specifying the authorisation types to auto-enrol on your 3DS Product Setup Form (PSF). See [Completing your 3DS Product Setup Form](Completing_the_PSF.htm).

Auto-enrol options include:

* None â there is no auto-enrolment. You will need to do this using either Thredd API or Cards API; see [Using the Card Enrolment API](Using_Card_Enrolment_API.htm).
* Initial load â Thredd creates the authentication type credentials (e.g., OTP SMS or BIOMETRIC) for all existing cards. For OTP SMS, Thredd uses the phone number linked to the card (i.e., the phone number supplied when the card was created or updated). This is done as a single bulk update; adding credentials for any future new cards or applying any changes to credentials for existing cards must be done using using either Thredd APIs or Cards API; see [Using the Card Enrolment API](Using_Card_Enrolment_API.htm)
* Continuous â same as Initial load, however any future cards created (using the Card Create Thredd API or Card Create Cards API) will also have their credentials automatically registered for 3D Secure in the same way. Applying any changes to credentials for existing cards must be done using using either Thredd APIs or Cards API; see [Using the Card Enrolment API.](Using_Card_Enrolment_API.htm)

Auto-enrolment enrols all live and active cards. It is not recommended if you wish to exclude some cardholders from enrolment.

Thredd auto-enrols the cards in the default main and fallback authentication methods. Auto-enrolment is available for OTP SMS, OTP Email, Out of Band (OOB) and Biometric authentication methods. Where a fallback method is not in use, the cards are enroled to the default method only.

For OTP SMS, Thredd auto-enrols using the mobile number linked to the card as the number for sending the SMS message to the cardholder during an SMS OTP authentication session.

To use this option, you must first have set up the default main and fallback authentication types on your 3DS Product Setup Form. See [Completing your 3DS Product Setup Form](Completing_the_PSF.htm).

## 8.2 Card Unenrolment

For cards which have been enroled manually or auto-enroled, you can un-enrol the card if required by deleting the credentials linked to the card using Thredd's 3DS Webservice or the Card Enrolment API.. If using continuous auto-enrolment, note that cards cannot be un-enroled if the card status is still live and active. The Program Manager needs to disable Auto0enrolment and switch to using the Card Enrolment API before unenroling cards. To disable Auto-enrolment on your products, speak to your Thredd Implementation Manager or Customer Support Specialist.

Thredd does not automatically unenrol cards on behalf of Program Managers. If the status of the card changes to statuses such as Destroyed, Lost, or Stolen, the Program Manager needs to unenrol the respective cards using the 3DS webservice, `Ws_AddUpDelCredentials` (SOAP), or the 3DS credentials API (REST).