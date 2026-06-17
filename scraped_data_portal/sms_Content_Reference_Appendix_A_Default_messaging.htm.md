# Appendix A â Default messaging

This section lists the default messages available in the Thredd SMS solution for each âeventâ such as card activation or balance enquiry. These defaults are used if you do not specify your own message for a particular event.

You can substitute the variables denoted by the % symbol with your own data. These variables are shown below.

## Default Messages

| Response code | Event | Default message text |
| --- | --- | --- |
| 1 | Activation | Your card ending \*\*\*\*%PAN4% is active now. CVV number relating to the card is: %CVV%. Thank you |
| 2 | Balance Enquiry | Your Card balance is %CURCODE% %CBAL% |
| 3 | Card Creation | Your card ending \*\*\*\*%PAN4% is created. CVV number relating to the card is: %CVV%. Thank You |
| 4 | Card Renewal | CVV number relating to your card ending \*\*\*\*%PAN4% is: %CVV%. Thank You |
| 5 | Card Replacement | Your card ending with \*\*\*\*%OLDPAN4% is replaced by card ending with \*\*\*\*%PAN4%. New card CVV is: %CVV%. Thank You |
| 6 | Load | An amount of %CURCODE% %AMT% loaded to your Card ending with \*\*\*\*%PAN4%. Your current balance is %CURCODE% %CBAL%. Thank You |
| 7 | PIN Retrieval | Dear %FNAME%, your PIN for your card ending %PAN4% is: %NEWPIN%. Kind Regards, %SENDER% |
| 8 | Status Change | Your card ending \*\*\*\*%PAN4% is now blocked/unblocked. Thank You |
| 9 | Card Image Regeneration | CVV number relating to your card ending \*\*\*\*%PAN4% is: %CVV%. Thank You |
| 10 | Card Conversion | Your virtual card ending \*\*\*\*%PAN4% is successfully converted in to physical. Thank You |
| 11 | Activation and Load | Your card ending \*\*\*\*%PAN4% is active now. An amount of %CURCODE% %AMT% is loaded. Your current balance is %CURCODE% %CBAL%. Thank You |
| 12 | Balance Adjustment | An amount of %CURCODE% %AMT% is %DEBORCRED% your card ending \*\*\*\*%PAN4%. Thank You |
| 13 | Balance Transfer | An amount of %CURCODE% %AMT% is transferred from your card ending \*\*\*\*%PAN4% to card ending \*\*\*\*%NEWPAN4%. Your current balance is %CURCODE% %CBAL% |
| 14 | Change Groups | Settings is changed for your card ending \*\*\*\*%PAN4%. Thank You |
| 15 | Extend Expiry | Thredd expiry of your card ending \*\*\*\*%PAN4% is extended to %GPSEXP%. Thank You |
| 16 | Unload | An amount of %CURCODE% %AMT% is debited from your card ending \*\*\*\*%PAN4%. Thank You |
| 17 | Unload and Status Change | Your card ending \*\*\*\*%PAN4% is now blocked/unblocked and an amount of %CURCODE% %AMT% is debited. Thank You |
| 18 | Update Cardholder | Card holder details of your card ending \*\*\*\*%PAN4% is updated. Thank You |
| 19 | **Mobile wallets only**  Send Mobile Activation code to Cardholder | %MOB\_ACTIVATION\_CODE% is your %WALLET% verification code for card ending \*\*\*\*%PAN4%. Please enter it when prompted |
| 20 | **Mobile wallets only**  Notification of Tokenisation | Your card ending \*\*\*\*%PAN4% has been successfully registered with %WALLET% |
| 21 | CVC2 Unblock | Message from %SENDER%. The CVC2 counter for your card ending \*\*\*\*%PAN4% has been unblocked. Thank you |

## Standard Variables

| Variable | Description |
| --- | --- |
| %FNAME% | Name |
| %AMT% | Amount |
| %CURCODE% | Currency Code |
| %CBAL% | Current Balance |
| %PAN4% | Masked PAN, showing last 4 digits |
| %NEWPIN% | PIN number |
| %CVV% | CVV (card verification value) |
| %SENDER% | Program manager, SMS message detail on product master screen |

## Mobile Wallet Variables

| Variable | Description |
| --- | --- |
| %MOB\_ACTIVATION\_CODE% | Represents the activation code in Payment\_Token.activation\_code |
| %MOB\_ACTIVATION\_EXP\_GMT% | Represents the expiry date/time of the activation code in Payment\_Token.activation\_code\_Expdate (this is date and time in GMT) |
| %MOB\_ACTIVATION\_EXP\_LOCAL% | Represents the expiry date/time of the activation code in Payment\_Token.activation\_code\_Expdate but expressed in the timezone of CARDDETAILS.country country |
| %MOB\_ACTIVATION\_MINUTES% | Represents the number of minutes from now that the activation code will still be valid for (subtract Payment\_Token.activation\_code\_Expdate GMT value from current GMT value and convert into whole minutes) |
| %MOB\_ACTIVATION\_LAST4\_TEL% | Represents the last 4 digits of the phone number to digitise (PAYMENT\_TOKEN.device\_tel\_num) |
| %WALLET% | Represents the wallet being used; for example, Google Pay, Apple Pay |