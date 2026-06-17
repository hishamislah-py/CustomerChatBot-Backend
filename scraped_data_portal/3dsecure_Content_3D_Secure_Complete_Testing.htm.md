# 9 Completing Staging/UAT Testing

Once the authentication screens are configured, Thredd and Cardinal release the project into the Staging environment for you to test.

## 9.1 Set up Rules in the Cardinal Portal

Thredd will set up your account and provide you with your user credentials to access the Cardinal Portal.

Access is only via permitted IP addresses. Please send Thredd a list of IP addresses you want to add to the authorised access list in Cardinal.

### 9.1.1 How to Access the Cardinal Portal

You can log in at:

<https://identifiportalstaging.cardinalcommerce.com/home/dashboard>

See the example below:

![](../Resources/Images/Cardinal/Cardinal_Portal.png)

Figure 11:  Cardinal Portal

In the Cardinal Portal, create your 3D Secure policy and set up the rules required to trigger Success, Fail/Reject or Challenge outcomes. You should complete rules for both 3DS 1.0 and 3DS 2.0. For details, see [Appendix 1: Cardinal 3D Secure Rules](../Reference/Cardinal_3D_Secure.htm).

For more information on how to use the Cardinal Portal, including arranging training sessions, please contact your 3DS project manager.

### 9.1.2 Using the Cardinal Test Simulator

You can start testing in Staging using the Cardinal Test Simulator:

1. Log in to the Cardinal Portal and in the **VCAS Test Store** box, click **Launch**.

   ![](../Resources/Images/VCAST_Test_Score_1.png)
2. This opens the VCAS Test Store web form, where you can submit test transactions. See the example below:

![](../Resources/Images/VCAST_Test_Score.png)

Figure 12: VCAS Test Store

You can use the **Test Setup** and **Additional Fields** sections to configure the test details (such as IP address, merchant country and merchant category code).

We recommend you test different use case scenarios, based on the Policy rules you have set up in Cardinal, to trigger Success, Reject/Fail/Fail with feedback or Challenge outcomes. For example, test different amounts, merchant categories, IP addresses, countries and account types.

When testing using the simulator, the authentication screens for OTP and Biometric are displayed and you will be able to complete the simulation of the OTP and Biometric authentication.

### 9.1.3 Viewing 3D Secure Transactions and Unblocking Cards

The Cardinal Portal enables you to view 3D Secure transactions processed on the system and unblock any blocked cards (e.g., cards blocked due to too many failed 3D Secure attempts).

You must be [PCI Compliant![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organisations that handle credit cards from the major Card Schemes (payment networks). All merchants who handle customer card data must be compliant with this standard. See: https://www.pcisecuritystandards.org/pci\_security](#) in order to view the full card PAN,