## Step 3: Check for PSD2 Acquirer Exemptions

In this step Thredd checks for any [PSD2 Acquirer Exemptions](PSD2_Acquirer_Exemptions.htm). Acquirer exemptions include low value transactions, transaction risk analysis and recurring transactions, which enable the acquirer to process as many transactions as possible without Strong Customer Authentication.

![](../Resources/Images/PSD2_Check_Step3.png "PSD2 Checks Step 3: Acquirer Exemptions")

Figure 6: PSD2 Checks Step 3: Acquirer Exemptions

The numbers in orange in the figure above correspond to the steps described below.

The following acquirer exemption checks are made:

1. Is the *[*Acquirer Transaction Risk Analysis Exemption*](PSD2_Settings.htm)* specified in the transaction?

   If no, then the next check is carried out (see step 2 below).

   If yes, then Thredd checks your product's *Acquirer Transaction Risk Analysis Exemption* transaction limit:

   * If this limit is blank (Thredd has not set a limit) for your product, then the transaction is exempt
   * If the transaction value is below or equal to the limit, then the transaction is exempt
   * If the transaction value is above the limit, then the exemption is ignored and the next check is carried out (see step 2 below).
2. Is the *[Acquirer Low-Value Exemption](PSD2_Settings.htm)* set for your product?

   If no, then the next check is carried out (see step 3 below).

   If yes, then Thredd checks your product's *Acquirer Low-Value Exemption* transaction limit:

   * If this limit is blank (Thredd has not set a limit) for your product, then the transaction is exempt
   * If the transaction value is below or equal to the limit, then the transaction is exempt
   * If the transaction value is above the limit, then the exemption is ignored and the next check is carried out (see step 3 below).
3. Are there any other acquirer exemptions? (see [PSD2 Acquirer Exemptions](PSD2_Acquirer_Exemptions.htm))

   * If no, then the transaction is not exempt
   * If yes, then the transaction is exempt

## What happens after exemption checking is complete?

For a transaction that was not strongly authenticated, then after exemption checking is complete:

* If no exemptions apply, then Thredd soft declines the transaction. See [Soft Declines](Soft_Declines.htm).
* If any exemptions apply, then Thredd can approve the transaction (provided there are no other reasons to decline).

For details of the full end-to-end transaction checking process, see [PSD2 Transaction Checks](PSD2_Transaction_Flow.htm).