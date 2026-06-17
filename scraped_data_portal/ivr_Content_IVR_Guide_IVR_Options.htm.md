# 2 IVR Options

This section describes the options available in the Thredd Thredd service, and provides details of how each option can be set up. Each option can have the wording changed as required for your programme.

The IVR template call flows shown below are examples, and the elements are configurable. For example, in a flow where a cardholder is prompted to input a passcode following the [PAN![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The cardâs 16-digit primary account number (PAN) that is typically embossed on a physical card.](#), this is a suggested flow.

## 2.1 Activate Card

The activate card IVR option enables the cardholder to activate a new card that they have received.

After the cardholder has navigated the menu and selected the Activate Card option, they are asked to enter the PAN and passcode that has been sent to them. The IVR solution receives these details, forwards to Thredd, and the Thredd database checks if the card is already active. If it isnât then the card is activated in the Thredd database and a success message is read back to the cardholder.

The template flow for the activate card option is shown below:

![](../Resources/Images/IVR_Activate_Card.png)

Figure 2: Activate Card Example Flow Diagram

## 2.2 Check Balance

The check balance IVR option enables the cardholder to call and find out what the current balance is for their card.

After the cardholder has navigated the menu and selected the Activate Card option, they are asked to enter the PAN and passcode that has been sent to them. The IVR solution receives these details, forwards to Thredd, and the Thredd database retrieves the cardâs balance and then reads it back out to the cardholder.

A template flow for the check balance option is shown below:

![](../Resources/Images/IVR_Check_Balance.png)

Figure 3: Check Balance Example Flow Diagram

## 2.3 Report Lost/Stolen Card

The report lost or stolen card IVR option enables the cardholder to call and report to you that their card has been lost or stolen, so that it can be made inactive.

After the cardholder has navigated the menu and selected the Report Card Lost/Stolen option, they are required to either enter the PAN and passcode that has been sent to them, or alternatively press a number on the phone to speak to a customer advisor.

If they enter the PAN and passcode, they are asked if they want to replace their card with a new one. The IVR solution receives the answer, forwards to Thredd, and the Thredd database updates the card status. The cardâs Lost/Stolen status is confirmed to the cardholder.

A template flow for the Report Lost/Stolen Card option is shown below:

![](../Resources/Images/IVR_Lost_stolen.png)

Figure 4: Report Lost/Stolen Card Example Flow Diagram

## 2.4 Unblock PIN

The unblock [Personal Identification Number (PIN)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The 4 to 12 digit value known only to the cardholder, which they may enter at POS or ATM to authenticate themselves.](#) IVR option enables the cardholder to unblock the PIN on their card.

After the cardholder has navigated the menu and selected the Unblock PIN option, they are asked to enter the PAN and [passcode![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) A 6-digit access code that is provided to the cardholder, and Thredd, when creating a card.](#) that has been sent to them. The IVR solution receives these details, forwards to Thredd, and the PIN status is unblocked in the Thredd database. The PIN Status is confirmed as unblocked to the customer.

A template flow for the Unblock PIN option is shown below:

![](../Resources/Images/IVR_Unblock_PIN.png)

Figure 5: Unblock PIN Example Flow Diagram

## 2.5 Get PIN

The Get PIN IVR option enables the cardholder to listen to the PIN for their card.

After the cardholder has navigated the menu and selected the Get PIN option, are asked to enter the PAN and passcode that has been sent to them. The IVR solution receives these details, forwards to Thredd, and the PIN is retrieved from the Thredd database. The PIN is then read out to the customer.

A template flow for the Get PIN option is shown below:

![](../Resources/Images/IVR_Get_PIN.png)

Figure 6: Get PIN Example Flow Diagram

## 2.6 Hear Terms and Conditions

The Hear Terms and Conditions IVR option enables the cardholder to have the terms and conditions read to them.

After the cardholder has navigated the menu and selected the Hear Terms and Conditions option, the Terms and Conditions are read out to them. Alternatively, they can be instructed to visit a website where the terms and conditions are displayed.

A template flow for the Terms and Conditions option is shown below:

![](../Resources/Images/IVR_Hear_terms.png)

Figure 7: Terms and Conditions Example Data Flow

## 2.7 Speak with a Customer Advisor

The Speak with a Customer Advisor IVR option enables the cardholder to exit the IVR menu and speak to a customer advisor.

After the cardholder has navigated the menu and selected the Speak to a Customer Advisor option, they are taken out of the menu and put through to the next available customer advisor.

A template flow for the Speak with a Customer Advisor option is shown below:

![](../Resources/Images/IVR_Speak_Advisor.png)

Figure 8: Speak with a Customer Advisor