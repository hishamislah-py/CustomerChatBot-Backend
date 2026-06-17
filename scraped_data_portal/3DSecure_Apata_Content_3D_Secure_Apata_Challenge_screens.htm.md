## 5.4 Challenge Screens

This section of the product setup form enables you to specify the text to appear on the Challenge screens, which will be presented to the cardholder during an authentication session. Please provide your brand logo to be displayed on the challenge screen if required. The scheme logo will also be displayed. Your logo must be in SVG (Scalable Vector Graphics) format.

Below is an example of the Challenge screens for OTP SMS. The text in the grey fields is customisable.

[![](../Resources/Images/Apata/OTP_Challenge_screen.png "OTP Challenge Screen")](../Resources/Images/Apata/OTP_Challenge_screen.png)

Figure 8: OTP SMS Challenge Screen Customisation

If you do not wish to customise the text, we will use the default English text for your screens.

#### Other text

Other Challenge screen text is common to all Challenge screens and appears in the footer or lower part of the screen. See the example below.

[![](../Resources/Images/Apata/Other_challenge_screen_text.png "Other challenge screen text")](../Resources/Images/Apata/Other_challenge_screen_text.png)

Figure 9: Other Challenge Screen Text Customisation

#### Use of variables

You can specify the use of the following variables on the Challenge screens:

| Variable | Description |
| --- | --- |
| {merchant name} | The merchant name. |
| {CUR} | The transaction currency. |
| {amount} | The transaction amount |

The variable values are taken from the information supplied in the authentication request sent from the card scheme to Apata.

### 5.4.1 Supported Languages

If you support more than one language, make a copy of the Challenge screens tab per language and provide the translated text for each language.

Apata identifies the language in which to display the Authentication screens based on the language settings applied under your products. If you wish to support different languages across your products, please specify which language to use for which product.

The main body of the screen text has a limit of 350 characters. Headers and labels have a limit of 45 characters.