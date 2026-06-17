# 6 Troubleshooting

This section provides answers to common troubleshooting issues.

## 6.1 Access

#### Cannot log into CTS

* Check your credentials are correct. You use the same credentials to access CTS as you do Smart Client UAT. Both the username and password are case sensitive.
* If you forget your username or password, contact Thredd by raising a [Thredd JIRA](https://gpsprocessor.atlassian.net/servicedesk/customer/portals) to request your username or a password reset.

#### How do I reset my password?

If you are logged into CTS, you can change your current password using the **Reset Password** option. For more information, see [Resetting your Password](CTS/Resetting_your_Password.htm).

If you are not logged in and need to reset your password, contact Thredd by raising a [Thredd JIRA](https://gpsprocessor.atlassian.net/servicedesk/customer/portals)

#### âThis site canât be reachedâ

If the message âThis site canât be reachedâ appears, this means that your IP address is not on the âallowed listâ on our system. Contact Thredd by raising a [Thredd JIRA](https://gpsprocessor.atlassian.net/servicedesk/customer/portals) to request that your IP address is added to the allowed list.

## 6.2 Test

#### 400 or 500 errors

The CTS system provides you with responses each time a transaction is executed. Depending on the information sent, the transaction is either approved or declined. If the transaction is declined, CTS provides a reason and response code to explain why.

Occasionally, if the system does not get a response within the required time frame, a timeout may occur and a 400 or 500 error is displayed. This shows as aborted in the history screen. If this issue continues, raise a [Thredd JIRA](https://gpsprocessor.atlassian.net/servicedesk/customer/portals) for Ops to investigate further.

For a list of response codes, refer to the [Thredd External Host Interface Guide](https://docs.thredd.ai/EHI_Guide.htm).