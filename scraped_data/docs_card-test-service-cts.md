# Card Transaction System (CTS)

The Card Transaction System (CTS) enables you to test your system’s integration before you move into a production environment. CTS allows you to submit card transactions and validate your External Host Interface (EHI) setup within a test (UAT) environment. A simple dashboard provides built-in standard test cases and a transaction history screen.

## Pre-requisites

To access CTS, you need the following:

* Your public IP address(es) added to the Thredd ‘allowed’ list
* Your bespoke Programme configuration, including EHI setup (refer to your Product Setup Form)
* A unique username and password for each user, your own setup in the UAT environment, and a username and password. You will also need your EHI set up at product level.

To submit test transactions, you will use Thredd Web Services to create and activate test cards. If you are using Cooperative Processing (Mode 2) or Full Service Processing (Mode 3), you will also need to load funds onto the test cards. You will need the 9-digit token, CVV2, and Expiry Date (provided in the Ws\_CreateCard Web Service response). For the PIN, Thredd recommends setting this in the Ws\_CreateCard request, otherwise you will need to use Ws\_PINControl to retrieve the generated PIN.

For more information about deploying CTS in your environment, contact your Account Manager.

## Logging into CTS

You can access CTS at:  [https://cts-uat.globalprocessing.net:54340/](https://cts-uat.globalprocessing.net:54340/)\
For more information, see the *CTS User Guide*.

> 👍 Documentation
>
> For more information on CTS, refer to the [Card Transaction System (CTS) Guide](https://docs.thredd.com/cts/Content/Home.htm).