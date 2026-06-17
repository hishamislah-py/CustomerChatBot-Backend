# Troubleshooting FAQs

This section provides answers to common troubleshooting issues.

## General Issues

#### Cannot Download or Install Smart Client

* Solution 1: Ensure that your Popup-blocker/Antivirus allows you to launch the software.
* Solution 2: Use Internet Explorer or Microsoft Edge, as there are multiple software settings and software versions that can cause conflicts and prevent a successful installation. Currently, you cannot download and install Smart Client on Apple OSX.

#### Smart Client does not start

* Solution: Uninstall Smart Client and then reinstall it. For more information, see [Installing the Smart Client application](Installing_SC.htm).

#### Forgotten username and/or password

If you forget your username or password, use the links in the Thredd Smart Client Login screen to retrieve and reset these.

##### Forgotten Password?

1. Click **Forgotten password?** to go to the reset screen.
2. Provide the email address configured for Thredd Smart Client and your Thredd Smart Client username.   
   Provided the credentials are valid a One-Time Temporary Password (OTP) is automatically sent to your email.
3. After logging in with the OTP, change your password immediately before proceeding.

##### Forgotten Username?

1. Click **Forgotten Username?** to go to the reset screen.
2. Provide the email address configured for Thredd Smart Client.

Provided the email address is valid, a username reminder is sent automatically to your email.

If you have been restricted from using the application due to multiple incorrect login attempts, email the Thredd Operations Command Centre at [occ@thredd.com](mailto:occ@thredd.com) (operational 24 hours a day, 7 days a week).

#### Cannot log into Smart Client

* Solution 1: Check that your credentials are correct. Please raise a JIRA ticket or email the Thredd Operations Command Centre at [occ@thredd.com](mailto:occ@thredd.com).
* Solution 2: For security reasons, Smart Client will not run two instances of the program at the same time on one machine, nor will it run on two machines that share the same computer name. Refer to your Microsoft Windows documentation for information about how to check the name of your computer or rename it.

* Solution 1: Check that your credentials are correct. Please raise a JIRA ticket or email the Thredd Operations Command Centre at [occ@thredd.com](mailto:occ@thredd.com).
* Solution 2: Check that the application is connected securely to Thredd. See the [Connecting to Thredd Guide.](https://docs.thredd.ai/Connecting_to_Thredd_Guide.htm)
* Solution 3: For security reasons, Smart Client will not run two instances of the program at the same time on one machine, nor will it run on two machines that share the same computer name. Refer to your Microsoft Windows documentation for information about how to check the name of your computer or rename it.

#### Card declined due to failed AVS check although address details appear correct

If only a delivery (Card Purchaser) address is specified during card creation and not a cardholder address, the transaction may be declined if the customer attempts to use it for ecommerce and telephone transactions where the merchant performs an address check. This is because the address (AVS) check is performed on the cardholder address which is blank.

Typically, you will spot this in the View Cards screen where the address is blank, and the post code is 0 (zero). This indicates Thredd does not hold a cardholder address, and as a result, will be unable to conduct an AVS Check (Address Verification Service).

To fix the issue for an affected card, you can use the Thredd Web Services API to update the cardholder address (`Ws_Update_Cardholder_Details`). For more information, see the *Web Services Guide*.

To fix the issue for an affected card using Smart Client, the customer needs to have made a transaction which will enable you to access the **Edit Card Details** option where you can update the address.

If the customer has yet to make a transaction, use Web Services to update the cardholder address or contact Thredd Support.

1. Right-click the transaction, choose **Actions** > **Edit Card Details**. The **Card Master** screen appears.
2. Click anywhere on the **Card Holder** pane, and then click **Save**. The Cardholder address is automatically populated with the purchaser (delivery) address, and the card will immediately be updated for AVS checks.

If there is a requirement to later amend the Cardholder address, you can repeat this process.

**Tip!** To prevent similar issues from occurring, ensure Thredd is always provided with a cardholder address during the card creation process.

## Known Issues

For a list of known issues, contact your Implementation Manager.