# Using PANFinder

## Starting PANFinder

1. To start PANFinder, double-click the **PANFinder** desktop icon.

   ![](../Resources/Images/PANFinder/PANFinder_login.png "PANFinder login box")
2. When prompted, enter the username and password you received from Thredd. This will be the same login credentials as you use to log in to Smart Client.
3. Click **Login**.   
   The OTP window appears.
4. Using multi-factor authentication, enter the OTP sent to the email address assigned to your account.

   ![](../Resources/Images/OTPPrompt.png)

   A user has a total of six attempts to log in successfully to Smart Client. When all attempts to log in have been exhausted, the user account is locked and you will need to contact Thredd support to unlock the account.

   If you do not receive an email with the OTP code, click Resend OTP to send the email again. This button is greyed out for the first 60 seconds after Thredd sends an email. You are allowed to press the button three times before the functionality to send the OTP is disabled. A message on the window displays how many attempts for resending an OTP are left.
5. Click **Validate**. If the OTP entered is correct, the PANFinder screen appears.

## Displaying the PAN

1. From the PANFinder top main menu, select **View PAN**.  
   The following screen appears:

   ![](../Resources/Images/PANFinder/PANFinder.png "PANFinder")
2. Enter the **ThreddToken** (you can enter either the 9 digit or 16 digit token).
3. Click **List**.  
   The **PAN** field displays the full PAN.

## Displaying the Thredd token

If you already know the PAN, you can use the PANFinder app to find the linked Thredd token.

1. From the top main menu, select **View PAN**.
2. Enter the **PAN**.
3. Click **List**.  
   The  **ThreddToken (9 digit)** and **ThreddToken (16 digit)** fields display the Thredd token.

## Troubleshooting PAN Display

Refer to the table below for common issues and how to resolve.

| Issue | How to resolve |
| --- | --- |
| Unauthorised to access PANFinder | Only users set up with sufficient user permissions (**Management + PANFinder** access level) in Smart Client are able to access the PANFinder application. To request access, please raise a Jira with Thredd. |
| Forgot user credentials | Please reset or request your login credentials via your Thredd Smart Client account. |
| 16 digit or 9 digit token token not found | You have entered an invalid Thredd token or the token is not available. Please check to ensure you have entered a valid token. |
| PAN not found | You have entered an invalid PAN or the PAN is not available. Please check to ensure you have entered a valid PAN. |
| You do not have the permission to view the PAN | You have entered the PAN of a card that belongs to the account of another Institution. You should ensure that the access rights for that particular institution is enabled in your Smart Client account, and then log in to PANFinder using the user account credentials set up for that institution. |