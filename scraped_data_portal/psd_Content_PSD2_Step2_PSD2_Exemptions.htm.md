## Step 2: Check for PSD2 Exemptions

In this step Thredd checks for the following PSD2 transaction exemptions:

![](../Resources/Images/PSD2_Check_Step2.png "PSD2 Check: Step 2 - Determine if PSD2 Exemptions Apply")

Figure 5: PSD2 Check Step 2 : Determine if any PSD2 Exemptions Apply

The following exemption checks are made:

* Exempt Merchant Category Codes (MCC)[1 Thredd only applies the MCC exemption where the cardholder is present (we ignore the terminal unattended status, as this is often incorrectly set by the acquirer).](#) - for example, Commuter Transport and Parking which are exempt from PSD2 for cardholder-present transactions at unattended terminals[2 We can optionally configure your programme to apply MCC exemptions to the following: Hotel merchants and Car rental merchants doing PAN key entry or manual or manual, cardholder present (or unknown) transactions.](#). For details, see [Which Merchant Category Codes are Exempt from SCA?](../FAQs.htm#Q.)
* Transaction is Contactless and the transaction value is under the Thredd Contactless limits
* Transaction is e-commerce and the transaction value is under the Thredd e-commerce limits
* Transaction is a Recurring Payment or instalment payment[3 We can optionally configure your programme to check that the original payment was SCA before applying the exemption.](#)

If none of these exemptions apply, then Thredd performs [Step 3: Check for PSD2 Acquirer Exemptions](Step3_PSD2_Acquirer_Exemptions.htm).