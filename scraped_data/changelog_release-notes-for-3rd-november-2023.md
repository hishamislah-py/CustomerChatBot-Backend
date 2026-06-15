# Release Notes for 3rd November 2023

New changes to the Thredd Cards API for the week ending 3rd November 2023.

* [New Get 3DS Configuration endpoint](#new-get-3ds-configuration-endpoint)
* [String cleaning of special character in Create Card and Update Card endpoints](#string-cleaning-of-special-character-in-create-card-and-update-card-endpoints)

## New Get 3DS Configuration endpoint

*Endpoint: cards/\{\{publicToken}}/3ds-configuration*\
A new endpoint has been added that enables customers to view card and 3DS enrolment data from the Alexis Database. This is to support customers using Apata for their 3DS provider.

You can retrieve a card's 3DS configuration by making a GET request to the Get 3DS Configuration endpoint. For example:

```json Example Get 3DS Configuration endpoint
{{base-url}}/cards/{{publicToken}}/3ds-configuration\_
```

A successful response will return an HTTP 200 response code and the 3DS configuration for the card will be in the response. Below is an example response:

```json Example Get 3DS Configuration response
{
	"provider" : "1",
	"programManager" :
	{
		"shortName" : "MABA",
		"ProgramManagerCode" : "FEV"
	},	
	"mobile" : 1234564566,
	"email" : "john.smith@example.com",
	"isActive" : "0",
	"Has3dSecureCredential" : "0",
	"apataConfig": {
	  "cardProgramId" : "ec737f30-0c61-4383-9732-83d7c7b38b49",
	  "challengeProfileId" : "950c886e-8eba-4465-8443-d22f90d269f8",
	  "financialInstitutionId" : "f88458df-20ea-49b7-b890-119c2f5e8c6e",
	  "kbaNumberOfQuestionsToAnswer" : "3",
	  "kbaNumberOfIncorrectPermissible" : "2",
	  "language": "en-EN"
	},
	"Kba": [
	  {
		"question": "What is your mother's maiden name?",
		"answer": "Roundel"
	  },
	  {
		"question": "What was your first car?",
		"answer": "Ford"
	  },
	  ...
	 },
	 "otpsms":
	 {
		"OtpSmsTemplateFullFormat" : "",
		"OtpSmsTemplateDefaultFormat" : ""		
	 },
	 "biometric":
	 {
		"AutoEnrol3dsBiometrics" : "0",
		"AutoEnrol3dsOob" : "0",
		"BiometricUrl" : "https://www.paynetics.com/biometric"
	 }

```

> 👍 Documentation/API Explorer
>
> * For more information on the Get 3DS Configuration endpoint, see [Managind 3DS Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials).
> * To try the Get 3DS Configuration endpoint, see [Get 3DS Configuration](https://cardsapidocs.thredd.com/reference/list-card-enrollment-details) in API Explorer.

## String cleaning of special characters in Create Card and Update Card endpoints

String cleaning will be performed on special characters that are included in the following fields for the Create Card and Update Card endpoints:

* firstName
* middleName
* lastName
* nameOnCard

The following characters will be removed for each of these fields if they are included.

* ;:!?\<>\~#%@\{}|\[]”