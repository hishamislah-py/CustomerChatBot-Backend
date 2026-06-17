# PSD2 Transaction Checks

The figure below provides a summary of the checks that Thredd runs on an incoming payment [authorisation![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Stage where a merchant requests approval for a card payment by sending a request to the card issuer to check that the card is valid, and that the requested authorisation amount is available on the card. At this stage the funds are not deducted from the card.](#) transaction to determine whether the PSD2 rules apply and to approve or decline the transaction, based on whether Strong Customer Authentication (SCA) has been correctly applied.

![](../Resources/Images/PSD2_Flow.png "Authorisation Transaction Flows under PSD2")

Figure 1: Transaction Checks under PSD2 (for Payment Authorisation)

The numbers in orange in the figure above correspond to the steps described below:

1. Assuming the payment authorisation transaction has passed all other Thredd checks and has not been declined, then Thredd checks for the following conditions:

   * The Thredd Product is not enabled for PSD2.
   * The [Wallet Provider![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) These are providers such as Apple, Android (Google), Samsung etc. who supply the payment apps (also known as Mobile Wallet token requestors).](#) (e.g., Apple Pay) manages the PSD2 checks (i.e., does SCA on their end).

If either condition applies, then Thredd does not need to do PSD2 checks. Thredd can approve the transaction (provided that there is no other reason to decline).

If none of above conditions apply, Thredd continues with the PSD2 SCA checks.

2. If the cardholder's device does the SCA checks, then the transaction can be approved.
3. If the cardholder's device does not do the SCA checks, then Thredd checks whether SCA has been done (see [SCA Checks](SCA_checks.htm)):

   * For e-commerce 3D-secure transactions, we can optionally configure your programme so that Thredd only considers the transaction as SCA if the cardholder is challenged (asked to verify their identity via 3D secure) during an online (e-commerce) transaction.
   * If SCA has been done, then Thredd resets the SCA counters (either e-commerce or contactless) and can approve the transaction.

   If required, you can also manually reset the SCA counters using the Thredd API. For details see [Reset Counters](Reset_Counters.htm).
4. If SCA has not been done, then Thredd continues with some additional checks (as described in [PSD2 Rules and Exemption Checks](PSD2_Checking_Steps.htm); a summary is provided below):

   1. Thredd checks whether the PSD2 rules apply (see [Step 1: Check if PSD2 Rules Apply](Step1_Do_PSD2_Rules_Apply.htm))
   * If PSD2 rules do not apply, then the transaction can be approved (provided that there is no other reason to decline).
   * If PSD2 rules apply, then increment the SCA counters.  
      Thredd continues with the next check.2. Thredd checks whether any PSD2 exemptions apply (see [Step 2: PSD2 Exemption Checks](Step2_PSD2_Exemptions.htm) and [Step 3: PSD2 Acquirer Exemption Checks](Step3_PSD2_Acquirer_Exemptions.htm)).
   3. If an exemption applies, the transaction can be approved (provided that there is no other reason to decline).
   4. If no exemption applies, the transaction is soft declined. See [Soft Declines](Soft_Declines.htm).