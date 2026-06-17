# Appendix 1: Cardinal 3D Secure Rules

You can use the Cardinal Portal to create rules to trigger a success, reject/fail or challenge outcome on the Cardinal system, based on factors such as the transaction amount, the type of transaction, the merchant category code (MCC), the merchant country, IP address, IP country, Risk score and shipping method. The process is as follows:

1. Create rules for processing of 3D Secure transactions in Cardinal. See [Creating Rules](#_Creating_Rules).
2. Create a policy and add the required rules. See [Creating Policies](#_Creating_Policies_1).
3. Save your policy and select the card BIN ranges the policy applies to.
4. Repeat steps 1 and 3 for any additional rule in the policy.
5. Repeat step 3 for any additional sub-BIN/BIN ranges.
6. If you are using Compliance Manager, then set up any additional rules required for [PSD2![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#) and [SCA![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Authentication which is a combination of two factors of identification at checkout. Examples include something they know (such as a password or PIN), something they get (such as an OTP in a mobile phone or other device) or something they are (such as their fingerprint).](#). See [Creating Policies in Compliance Manager](#Setting).

## Creating Rules

To create a rule:

1. On the Cardinal Portal dashboard, in the **EMV 3DS Rules Manager** box, click **Launch**.
2. From the menu, select **Rules > Write New Rule**.

   Provide a name and configure your rule. Your rule should include the conditions which trigger a specific authentication outcome. See [Rule Outcomes](#_Rule_Outcomes).

   The example below shows a simple rule to approve transactions for less than 30 USD where the country is UK:

   ![](../Resources/Images/Cardinal/Cardinal_Rule_Editor.png)

   Figure 13: Cardinal Rule Editor
3. Click **Save Rule**.
4. Create the additional rules you require to trigger other outcomes.

   You need to save the rule and publish it before adding it to the policy and saving the policy.

### Rule Outcomes

Rule outcomes can be one of the following:

| Field | Description |
| --- | --- |
| Success | The authentication request is Approved. [Frictionless authenticationClosed When a transaction is approved without requiring any manual input from the cardholder.](#) approval is provided, and the card can proceed to payment authorisation. |
| Rejected | The authentication request is rejected. In this case Cardinal will show the status you configured for a rejected transaction. See [Authentication Status.](#_Authentication_Status) |
| Challenge | Cardinal do cardholder authentication, based on the authentication types the card is enrolled for. |
| Fail | The authentication request fails. The merchant can attempt payment using a different method. |
| Fail with Feedback | The authentication request fails with feedback. The response provides the reason for the failure. The message provided depends on what you have filled in the Fail with Feedback screen template in the 3DS Product Setup Form (PSF). |

### Authentication Status

Cardinal can display the following status values for the result or authentication transaction:

| Status | Description |
| --- | --- |
| Y | Successful Authentication |
| N | Failed Authentication |
| NF | Not Authenticated with Feedback |
| A | Attempts |
| MC | Merchant Cancelled |
| CC | Cardholder Cancelled |
| I | Incomplete |
| U | Unavailable |

## Creating Policies

Your rules should now be added to a 3D Secure policy.

To create a new policy:

1. From the menu, select **Policies > Build New Policy**.
2. In the **Policy Editor** screen, click **Add Rule**.

   ![](../Resources/Images/Cardinal/Cardinal_Policy_Editor.png)

   Figure 14: Cardinal Policy Editor
3. Add the rules you previously configured.
4. If you have more than one rule, to change the order of a rules, select the order and click **Change Order**. Then drag and drop the rule in the required order.
5. When you are finished, click **Save Changes**.
6. To publish the policy and link it to a Sub-BIN/BIN range (depending on what have you requested to be configured in Cardinal), click **Publish**.
7. Under **Available BIN Ranges**, select the BINs if they are not already selected.

8. Click **Publish** and **Yes Publish**.

## Creating Policies in Compliance Manager

Compliance Manager is a Cardinal application which provides tools to identify transactions that require [Strong Customer Authentication (SCA)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Authentication which is a combination of two factors of identification at checkout. Examples include something they know (such as a password or PIN), something they get (such as an OTP in a mobile phone or other device) or something they are (such as their fingerprint).](#), and enables you to configure rules for handling these transactions. This option is mainly relevant to Issuers (BIN sponsors) in the European Economic Area (EEA) and in other regions who want to conform to the [Second Payment Services Directive (PSD2)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) PSD2 is a European regulation for electronic payment services. It seeks to make payments more secure, boost innovation and help banking services adapt to new technologies. The regulations are available here: https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366\_en](#). For more information, refer to the *VCAS Compliance Manager Portal User Guide*.

You will need to request access to the Compliance Manager application as this is only relevant to PSD2 customers and is not provided automatically.

To create a new Compliance Manager policy:

1. From the Cardinal Portal dashboard, in the **Compliance Manager** box, click **Launch**.
2. In the Compliance Manager screen, click **Create a New Policy**.
3. Enter a name for this policy and click **Assign Card Ranges**. Then enter the card ranges that apply to this policy.
4. Switch on the rules which you want to apply to the policy and click **Save Policy**. See [Compliance Manager Rules](#Complian).

### Compliance Manager Rules

Refer to the table below for details of available rules.

| Rule | Description |
| --- | --- |
| Smart detection | If enabled, then Cardinal will use the origin of the issuing card and location of the merchant acquirer to determine whether is out of scope for Strong Customer Authentication (SCA), thereby providing a frictionless experience for 'one-leg-out' transactions. |
| Acquirer transaction risk analysis | If enabled, then any merchants that the Acquirer has flagged as exempt from SCA will not be included in the Cardinal SCA checks. You can also configure rules to customise this exemption, using criteria you define, such as for specific transaction amount thresholds or specific Merchant Category Codes that you want to apply. |
| Issuer transaction risk analysis | If enabled, enables you to set thresholds below which Cardinal will not apply SCA checks, based on transaction amount and risk score. |

![](../Resources/Images/Cardinal/Compliance_manager.png "Compliance Manager screen")

Figure 15: Compliance Manager Screen