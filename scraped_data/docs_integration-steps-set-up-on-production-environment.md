# Set up on Production

When all production readiness activities are complete, Thredd provides you with production credentials and generates a limited number of PAN stock, as approved by your card issuer.

### Production Testing Steps

Additional end-to-end transaction testing is required at this stage. In particular:

* Create card tokens for automated card production.
* Thredd will send a file to the card manufacturer via sFTP. The card manufacturer generates live physical cards and despatches to the relevant parties for testing (Thredd , Program Manager and Card Schemes).

Thredd can provide you with a test script to run tests that cover aspects you should test, such as:

* Test traffic through the BIN tables.
* Test the card chip profile is working in line with how it has been configured (for example, if the card is enabled to draw out money at ATMs and charges a fee for ATM withdrawals, check this works as expected).
* Test to ensure usage groups and velocity limits set up for your products work as expected and return the expected results.
* Make sure you understand any messages returned from the card schemes and card issuers and know how to handle these.
* Test the end-to-end customer experience and confirm that the card and account are operating as expected.