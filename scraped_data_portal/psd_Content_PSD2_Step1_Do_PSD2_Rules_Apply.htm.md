## Step 1: Check if PSD2 Rules Apply

PSD2 checks are required for this transaction if all the following are true:

* This an authorisation request (MTID 0100)
* PSD2 compliance is enabled for the Thredd Card product
* The transaction is not set up as an MDES/VDEP payment token or   
  the transaction is set up as an MDES/VDEP payment token, but checks are done by Thredd
* The transaction has not already been declined

If all the above are true, then Thredd tests whether the PSD2 rules apply as shown in the figure below:

![](../Resources/Images/PSD2_Check_Step1.png "PSD2 Checks - Step 1: Exemption Checks")

Figure 4: PSD2 Check Step 1: Exempt from PSD2 Rules

The PSD2 rules do not apply to the following types of transactions:

* The Acquirer is outside of the UK or EEA[1 If the card issuer/BIN is outside of the UK/EEA they would typically disable their Thredd card product for PSD2 checks.](#)
* Account Verification transactions
* Credit transactions
* Mail and Telephone Order (MOTO) transactions
* Special exemptions for cardholder present transactions on specific Merchant Category Codes (MCCs) such as hotel and car rental merchants. (Exemption flags must first be set in the Thredd system.)

If any of these conditions apply to the transaction, then it is treated as out of scope of the PSD2 regulations.

If none apply, then Thredd performs [Step 2: Check for PSD2 Exemptions](Step2_PSD2_Exemptions.htm).