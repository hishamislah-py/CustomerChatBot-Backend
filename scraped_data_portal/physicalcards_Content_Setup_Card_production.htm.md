# 7 Card Production and Testing

This section describes the typical steps in producing, testing and releasing into production the card products for your programme.

## 7.1 Creating White Test Plastics

White test plastics are generic, non-branded cards with test keys on the card and a Chip profile. Your Implementation Manager will work with your card manufacturer to produce test cards. Below are the typical steps in creating your test cards:

1. Create several test cards and provide Thredd with a list of the generated [Public Tokens![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The 9-digit token is a unique reference for the PAN. This is used between and clients to remove the need for clients to hold actual PANs.](#).
2. Thredd produces a card generation file for any test cards that have been created and manually sends the file to the card manufacturer via sFTP.
3. The card manufacturer produces white test plastics in line with the agreed project plan. Test cards are sent to the relevant parties (e.g. the Program Manager and Visa or Mastercard).
4. Testing is undertaken in line with the agreed scope.

## 7.2 Setting up on Production

When all production readiness activities are complete, Thredd provides you with production credentials and generates a limited number of PAN stock, as approved by your card issuer.

### 7.2.1 Production testing steps

Additional end-to-end transaction testing is required at this stage. In particular:

1. Create card tokens for automated card production.

   * Thredd will send a card generation file to the card manufacturer via sFTP. The card manufacturer generates live physical cards and despatches to the relevant parties for testing (Thredd, Programme Manager and Card Schemes).
2. Make sure you understand any messages returned from the card schemes (payment networks) and card issuers and know how to handle them.
3. Thredd can provide you with a test script to run tests that cover aspects you should test, such as:

   * Test traffic through the [BIN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Bank Identification Number (BIN) is the first six to eight numbers on a payment card, which identifies the institution that issues the card.](#) tables (BIN databases held by the card scheme).
   * Test the card chip profile is working in line with how it has been configured (for example, if the card is enabled to draw out money at ATMs and charges a fee for ATM withdrawals, check this works as expected).
   * Test to ensure usage groups and velocity limits set up for your products work as expected and return the expected results.
4. Test the end-to-end customer experience and confirm that the card and account are operating as expected.