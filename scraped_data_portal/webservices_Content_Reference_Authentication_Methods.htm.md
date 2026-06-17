# Authentication Methods

See the table below for a list of cardholder authentication methods, which are used within the `<AuthType>` tag. In most cases an Authorisation type of 1 is sufficient, since there is separate SOAP header authentication to validate the user of the web service.

| Auth Type | Description |
| --- | --- |
| 1 | Card number (PAN) or public token |
| 2 | Card number/public token & cardholderâs date of birth |
| 3 | Card number/public token & CVC2 |
| 4 | Card number/public token & access code |
| 5 | Login ID â DO NOT USE |
| 6 | Card number and cardholderâs date of birth and cardholderâs last name |
| 7 | Full Track2 |
| 8 | Card number & security data â DO NOT USE |

If you suspect your SOAP login details may have been compromised, contact Thredd immediately