# Release Notes for the 28th March

The following change has been made to Cards API:

## Updated Maximum Length for City, State, and AddressLine3 Fields

We have updated the maximum length from 100 to 50 for the following fields in the Create Card and Update Card endpoints:

* City
* State
* AddressLine3

If you attempt to input more than 50 characters for these fields, a 422 error is returned to prevent the card being created or updated.