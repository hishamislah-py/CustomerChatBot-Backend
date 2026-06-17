# PSD2 Rules and Exemption Checks

The figure below provides a summary of the key checks that Thredd performs on an incoming payment authorisation transaction, to determine whether the PSD2 rules apply and if there are any exemptions from the PSD2 rules.

These checks are done as part of the full [PSD2 Transaction Checks](PSD2_Transaction_Flow.htm).

![](../Resources/Images/PSD2_Exemption_Checking_Summary.png)

Figure 3: PSD 2 Checks Performed by Thredd - Summary View

For a more detailed process flow which breaks down steps 1-3 above, see [Detailed Thredd PSD2 Exemption Checks Workflow](PSD2_Checking_Details.htm).

There are three main exemption checks which are applied to the transaction:

* [Step 1: Check if PSD2 Rules Apply](Step1_Do_PSD2_Rules_Apply.htm)
* [Step 2: Check for PSD2 Exemptions](Step2_PSD2_Exemptions.htm)
* [Step 3: Check for PSD2 Acquirer Exemptions](Step3_PSD2_Acquirer_Exemptions.htm)