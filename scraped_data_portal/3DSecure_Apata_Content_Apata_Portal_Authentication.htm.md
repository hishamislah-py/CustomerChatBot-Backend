# 22 Managing Authentication Rules

The Authentication menu on the [Apata Portal Dashboard](Apata_dashboard.htm#Apata_Portal_Dashboard) enables you to view your challenge methods, card programs and corresponding BIN ranges, and also create and update your authentication rules. Options include:

* [Viewing Risk profiles](#Viewing)
* [Creating and Editing Risk profiles](#Creating) (administrator-level only)
* [Viewing Challenge methods](#Viewing2)
* [Viewing Cards Programs](#Viewing3)

Thredd provides default authentication rules and profiles for your programme; you can edit or add to these rules and profiles to meet your business requirements. (Before making any changes, we recommend you discuss first with your 3D Secure implementation Manager.)

Only Administrator users can edit these options.

## 22.1 Viewing Risk Profiles

A risk profile defines a set of rules for processing of transaction requests and determining the action the system should take (such as *accept*, *reject* or *challenge*). A Risk profile could be simple, consisting of a single rule, or complex, consisting of multiple rules. You can also define the order in which the rule checks are made.

1. To view a list of risk profiles, select Authentication > Risk Profiles from the left-hand menu.

![](../Resources/Images/Apata/risk_profiles.png "View Risk Profiles")

Figure 19: View Risk Profiles

2. To view details of a risk profile, click the ![](../Resources/Images/Apata/View_details_31x30.png) button.

Below is an example of a simple risk profile rule, configured to allow all (no challenge screens will appear). This might be suitable for low-value prepaid cards or closed loop card programmes.

![](../Resources/Images/Apata/risk_rule_allow_all.png "Risk Rule - Allow")

Figure 20: Risk Profile Rule - Allow All

Below is an example of the opposite risk profile rule, configured to provide challenge screens for all authentication transactions. This might be suitable for cards that are considered very high risk (e.g., issued in higher risk countries).

![](../Resources/Images/Apata/risk_rule_challenge_all.png "Risk rule: challenge all")

Figure 21: Risk Rule - Challenge All

Below is an example of a complex risk profile, consisting of multiple rules, created for a card program in the EU. The risk profile consists of rules to allow frictionless authentication in the following circumstances:

|  |  |
| --- | --- |
| * the merchant is on a trust list * the transaction is within the PSD2 rules for low-value transaction * the transaction is a secure corporate payment * the transaction is merchant-initiated | * the merchant acquirer has requested an exemption from authentication * the transaction is not a payment transaction (e.g., account funding) * the transaction is within the cumulative number for frictionless authentication * the transaction is within the maximum cumulative spend (e.g., â¬100 or Â£100) |

![](../Resources/Images/Apata/risk_rule_eu_program.png "Risk Profile for an EU program")

Figure 22: Example of Risk Profile Details

Each Risk Profile and its associated rules is assigned a unique system ID, which is then assigned to a card program (i.e, grouping of cards of BIN ranges).

* To view further details of the rule, click the ![](../Resources/Images/Apata/down_arrow.png "Down arrow")button next to the rule.   
  The example below shows the configuration for rule 6. In this example, you can select the type of transactions (identified by codes: 04, 05, 06, 07, 08, 09 and 10) that are treated as non-payment transactions and which will be allowed without any Challenge screens.

![](../Resources/Images/Apata/eu_program_rule6.png "Example of a rule")

Figure 23: Example of a rule configuration

## 22.2 Creating and Editing Risk Profiles

To create a new risk profile, in the Risk Profiles screen, click the Create Risk Profile button.

Only administrator users can access this functionality.

To edit an existing risk profile, click the ![](../Resources/Images/Apata/edit_button.png "Edit button") button.

### 22.2.1 Adding a new rule

1. To add a new rule, scroll down to the bottom of the screen and click the ![](../Resources/Images/Apata/Add rule icon.png "Add rule button") button.
2. Select the rule you want to add. For a list of available rules, see [Appendix 1: Apata 3D Secure Rules](../Reference_Apata/Apata_3D_Secure.htm).

### 22.2.2 Adding a Conditional Rule

1. To add a new rule, scroll down to the bottom of the screen and click the ![](../Resources/Images/Apata/Add rule icon.png "Add rule") button.
2. Select the Conditional rule.
3. Select an action for your rule. Options include:

| Rule | Description |
| --- | --- |
| Accept | If rule condition is met, allow frictionless authentication. |
| Reject | If rule condition is met, reject the authentication. |
| Challenge | If rule condition is met, show Challenge screens. |
| Next | If none of the previous rule conditions are met, move on to the next rule. |

4. Configure the conditions which trigger the rule:

   * Click the Add Rule button.
   * Use the operator selector (e.g., AND, OR) to add multiple conditions.
   * Select a Field Name, Operation and Value for the condition. The value that can be selected or entered depends on the field name selected.  
     See the examples below:

| Field Name | Operation | Value | Action Configured |
| --- | --- | --- | --- |
| Risk Score | Is | Low | Accept |
| MCC | Is | 7995 | Reject |
| Amount | Is greater than | 200 | Challenge |

5. If you have multiple rules, you should order your rules in the order in which you want them to be checked. The system will move on to the next rule in the list, provided that the Next rule action has been specified. (If no Next rule action is specified, the final decision is returned (accept, reject or challenge).

   If the transaction does not meet the criteria of any rules in the risk profile created, the transaction will be challenged as a default behaviour.You can also set a SIMPLE rule as the last rule in the risk profile and set desired âActionâ (example: Accept or Reject).
6. To delete a condition, click the ![](../Resources/Images/Apata/Delete_button.png "Delete button") button.
7. To save your changes, click the ![](../Resources/Images/Apata/Update_button.png "Update button") button.

Below is an example of a conditional rule. In this rule the Challenge action is triggered when the following conditions are met: *Amount if greater than 100* and *risk score is HIGH*.

![](../Resources/Images/Apata/risk_conditions.png "Risk conditions")

Figure 24: Example of a Challenge rule configuration

### 22.2.3 Creating a Draft Risk Profile

A draft risk profile lets you add changes to an existing risk profile before applying the change to the Live environment. This enables you to check any changes prior to publishing, ensuring that these are configured correctly to perform the desired actions. The draft risk profile also enables you to run a backtest, which simulates how an updated version of a risk profile performs on transactions before publishing. For information on backtesting, see [Backtesting Risk Profiles](Merchant_Simulator.htm#Backtest).

1. From the dashboard, click on the risk profile that you want to update. For example, you change a rule action from Accept to Challenge.
2. Click the **Drafts** tab.
3. In the displayed box that is labelled **Oops Nothing Here**, click **Add New Draft**.

   ![](../Resources/Images/Apata/draft_risk_profile.png)

   Figure 25: Drafts tab for creating a draft risk profile
4. Add your rules to the draft risk profile.
5. Click **Create Draft**.
6. If you want to include comments, add these to the displayed window and click **Create**.

![](../Resources/Images/Apata/create_draft.png)

Figure 26: Adding comments for a draft risk profile

The created draft risk profile appears under the Details tab.

![](../Resources/Images/Apata/created_draftprofile.png)

Figure 27: Created draft risk profile

Once you have created the draft risk profile, you can edit or publish it, or run a backtest. You can also share the draft risk profile with your colleagues.

Clicking the **Rules** tab from the Details tab, lets you refer back to the live profile.

### 22.2.4 Editing a Draft Risk Profile

You can modify a draft risk profile. For example, you can change a rule action from Challenge to Reject.

1. Open the risk profile by clicking the ![](../Resources/Images/Apata/View_details_31x30.png) button.
2. Click **Edit Draft**.
3. Click **Update Draft**. A message box appears where you can add a comment.
4. Click **Update**.

#### Deleting a Draft Risk Profile

1. Ensure that you risk profile is in Edit mode where you have clicked the **Edit Draft** button.
2. Click the **Delete Draft**. A confirmation message appears.
3. Click the **Delete**.

### 22.2.5 Publishing a Draft Risk Profile

* Click **Publish Live**. Publishing applies the changes from the draft risk profile, and replaces the Live profile.

### 22.2.6 Running a Backtest

* For more details, see [Backtesting Risk Profiles](Merchant_Simulator.htm#Backtest).

## 22.3 Viewing Challenge Methods

The Challenge method defines the type of Challenge options used to authenticate a cardholder during an online 3D Secure session. Examples include OTP SMS, OTP email and biometric. The Apata system provides a number of default Challenge options that can be selected as default for your programme. Please check with your Thredd 3D Secure Implementation Manager to determine which methods can be used with Thredd.

If you require any changes to your configuration including adding new challenge methods, please speak to your Thredd 3D Secure Implementation Manager.

1. To view a list of challenge methods, select Authentication > Challenge Methods from the left-hand menu.

![](../Resources/Images/Apata/challenge_methods.png "Challenge methods")

Figure 28: View Challenge Methods

2. To view details of a challenge method, click the ![](../Resources/Images/Apata/View_details.png) button.

Below is an example of a challenge method, using SMS OTP.

![](../Resources/Images/Apata/challenge_method_sms_otp.png "OTP SMS Challenge Method")

Figure 29: OTP SMS Challenge Method Example

A mock-up view of the Primary challenge screen is displayed in the right-hand pane. For details of how to specify text and logo changes, see [Configuration of 3D Secure Screens](../3D_Secure_Apata/Configuration_of_Screens.htm).

Each challenge method is assigned a unique system ID.

## 22.4 Viewing Card Programs

Apata's options for authentication at card program level enable you to set up different risk profiles, depending on the card BIN range. This is a useful option to enable you to assign different risk profiles to different types of cards, based on BIN range. For example, your issuer (BIN sponsor) may have assigned you with different BINs for Corporate cards versus Consumer cards, or separate BINs (BIN ranges in the EEA) for each of the countries in which you intend to issue cards.

1. To view a list of card programs, select Authentication > Card Programs from the left-hand menu.

![](../Resources/Images/Apata/card_programs.png "Card Programs")

Figure 30: View Card Programs

If the Card Program is set to Default, it will automatically include all card ranges that are not already associated with another Card Program.

To apply any changes to your card program setup, please raise a change request with your Thredd 3D Secure Implementation Manager.

2. To view details of a card program, click the ![](../Resources/Images/Apata/View_details.png) button. Below is an example of a card program.

![](../Resources/Images/Apata/card_program_details.png)

Figure 31: Card Program Example - UK Physical Cards

3. To view the Risk profile associated with the card program, click the ![](../Resources/Images/Apata/View_details.png) button.
4. To view the card BIN ranges, status and other details associated with the card program, click the ![](../Resources/Images/Apata/view_button.png "View button") button.