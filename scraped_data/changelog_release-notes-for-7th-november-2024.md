# Release Notes for 7th November 2024

New changes to the Thredd Cards API coming on the 7th November. These include:

* [New Fields Added to Unblock CVV and Update Card Controls Endpoints](#new-fields-added-to-unblock-cvv-and-update-card-controls-endpoints)
* [General Behaviour Fixes for Tokenisation](#general-behaviour-fixes-for-tokenisation)

## New Fields Added to Unblock CVV and Update Card Controls Endpoints

Two new fields have been added to the Unblock CVV and Update Card Controls endpoints. `updatedBy` and `description`, enabling you to see the changes made to the endpoints and by whom.

```json Example Unblock CVV request
{
  "status": "Unblocked",
  "description": "CVV unblocked on 04/11/2024",
  "updatedBy": "John Bloggs"
}
```

```json Example Update Card Controls request
{
  "controlGroups": {
    "limitsGroup": 10023
  },
  "updatedBy": "John Bloggs",
  "description": "Group updated to 10023 on the 4th November"
}
```

## General Behaviour Fixes for Tokenisation

The following improvements have been made around tokenisation in this release:

* Fixed an issue where replacing a card doesn’t transfer the payment token to the new card.
* A lifecycle update call is now sent to Mastercard Digital Enablement Service (MDES) or Visa Digital Enablement Program (VDEP) when replacing, renewing or updating a card status to 00. This is true even if the card does not have payment token