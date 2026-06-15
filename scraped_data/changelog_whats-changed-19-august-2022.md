# Release Notes for 19 August 2022

New changes to the GPS Cards API for the week ending 19th August 2022.

* [New Transaction Type added to Load and Unload Card endpoints](#new-transaction-type-added-to-load-and-unload-card-endpoints)
* [Middle name field added to multiple endpoints](#middle-name-field-added-to-multiple-endpoints)
* [New fields added to Create Card endpoint](#new-fields-added-to-create-card-endpoint)
* [New fields added to Update Card endpoint](#new-fields-added-to-update-card-endpoint)
* [New fields added to Create Card response](#new-fields-added-to-create-card-response)

## New Transaction Type added to Load and Unload Card endpoints

A Fee transaction type has been added to the Load/Unload Card endpoint. This change also includes two new properties for the request:

* FeeType is the processing code associated with the fee applied to the card
* FeeAmount is the amount charged to the card

These fields are mandatory if Fee is set as the TransactionType value. Additionally, the Amount property should not be included where the TransactionType value is set to Fee.

The below is an example body for a Load transaction where FeeType and FeeAmount are used.

```json
{
     "transactionType": "Fee",
     "feeType": "RecurringFee",
     "feeAmount": 200,
     "currencyCode": "GBP"
}
'
```

## Middle name field added to multiple endpoints

The Middle Name (MiddleName) field has been added to the following endpoints:

* Get Cardholder Details
* Retrieve a Card

This field enables you to capture and retrieve the middle name for the cardholder associated with your card.

## New fields added to Create Card endpoint

The following fields have been added to the Create Card endpoint:

* Cardholder.MiddleName
* Address.State
* Fulfillment.State
* ManufacturingDetails.Language

## New fields added to Update Card endpoint

The following fields have been added to the Update Card endpoint:

* Cardholder.MiddleName
* Address.State
* Fulfillment.State

## New fields added to Create Card response

The following fields have been added to the Create Card response:

* CustomerReference
* EmbossName
* MaskedPAN
* StartDate
* ExpiryDate

```json Updated response to Create Card response
{
  "PublicToken": "12345678910",
  "CustomerReference": "string",
  "EmbossName": "string",
  "MaskedPAN": "string",    
  "StartDate": "string",
  "ExpiryDate": "string"
}
```