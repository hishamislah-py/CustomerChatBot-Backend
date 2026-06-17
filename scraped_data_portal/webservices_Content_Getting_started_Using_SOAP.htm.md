# Using the API

This section provides tips on how to integrate to Thredd using the [SOAP![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) SOAP (Simple Object Access Protocol) is a messaging protocol for exchanging structured information in the implementation of web services. It uses Extensible Markup Language (XML) for its message format and relies on application layer protocols such as HTTP for message negotiation and transmission.
SOAP allows developers to invoke processes running on disparate operating systems (such as Windows, macOS, and Linux) to authenticate, authorise, and communicate using XML.](#) web services API.

## Using the Web Services

### View the WSDL

You open the following URL in a browser to view the structure of the [WSDL![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Web Service Definition Language (WSDL) is an XML format for describing network services as a set of endpoints operating on messages containing either document-oriented or procedure-oriented information.
WSDL files are central to testing SOAP-based services. SoapUI uses WSDL files to generate test requests, assertions and mock services.](#):

<https://ws-uat.globalprocessing.net:13682/service.asmx?WSDL>

We recommend you always refer to the WSDL for the correct XML tag name spelling and capitalisation, as different web services may sometimes adopt different case and naming conventions.

### Install a SOAP Application

Thredd recommend that you use an API tool that supports SOAP to test out the Thredd web services.

[SOAPUI](https://www.soapui.org/) is an open-source application, which you can download and install on any computer, which enables you to submit test transactions to Thredd.

### Load the SOAP WSDL

You can load the Thredd SOAP test WSDL into your SOAP tool. If you are using SOAPUI, then:

1. Select **File > New SOAP Project**.
2. Enter a project name and then, in the **Initial WSDL** field, paste the following URL:   
   <https://ws-uat.globalprocessing.net:13682/service.asmx?WSDL>
3. Click **OK**.

![](../Resources/Images/new_soap_project.png "Starting a new SOAP project and importing the WSDL")

Figure 8: Starting a new SOAP project and importing the WSDL

## Implementing a SOAP Request

Always follow the instructions provided for [Implementing web service calls](About.htm#Implemen), to ensure that your XML requests are correctly formatted.

You can implement a SOAP call as follows:

1. Select a SOAP service from the left-hand navigation pane. Thredd recommend you start with a check of the status of the web service to make sure you can connect, using `Ws_Check`. See [Check Service Availability](../Web_services_api/Check_Service_Availability.htm).
2. In the centre pane, customise the SOAP details of your transaction. At a minimum, you will need to enter your username, password and Issuer Code (`IssCode`). If you don't have these details, check with you Thredd Implementation Manager.

You can copy and paste examples in this guide into the SOAP window, and customise as required.

3. Click **Submit**.

   The SOAP response should be displayed in the right-hand pane within SOAPUI. A successful request will return an `ActionCode` status of *000* (Normal, approved). See [Action Codes](../Reference/Action_Codes.htm).

![](../Resources/Images/SoapUI.png "Example of the SOAP GUI app")

Figure 9: Example of a SOAP Request in SOAPUI

## Fair Usage Policy

Thredd has a Fair Usage Policy which restricts the maximum number of *[concurrent ![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The number of sessions (concurrent requests) that can be processed by the Thredd server at the same time. This figure may vary, depending on server load and performance, which affects the response time. For example, an average server response time of 0.05ms.](#)*web service connections per client (IP address) to 20.

If you send more than 20 concurrent web service requests to Thredd an HTTP error message 403, sub-status 501 is returned. This can be mitigated by controlling your outbound web server configuration. For further details, please contact your Implementation Manager or Account Manager.

### Additional charges for using some Web Services

Note that in the Production environment additional charges may apply to web services that retrieve the balance on the card from Thredd. Contact your account manager to discuss. You can avoid this charge if you use the EHI data feed to maintain the balance in your own systems. The following web services listed in this guide retrieve the balance on the card: `Ws_Balance_Enquiry`, `Ws_Card_Statement`, `Ws_Enquiry, Ws_Card_BalEnq`, `Ws_Customer_Enquiry`, `Ws_Customer_Enquiry_V2` and  `Ws_Balance_Enquiry_V2`

## Viewing Transactions on Smart Client and Thredd Portal

You can log in to [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's user interface for managing your account on the Thredd Platform. You install Smart Client as a desktop application which requires a secure connection to Thredd systems in order to access your account.](#) or Thredd **Portal** to view the card token and associated activity generated by your web services.

Smart Client must first be installed as a desktop application on your machine. A secure connection to Thredd is required to access Smart Client. Thredd Portal does not require local installation as it is a web application.

For more information on using Smart Client, refer to the [Smart Client User Guide](https://docs.thredd.ai/Smart_Client_Guide.htm). For more information on using Thredd Portal, refer to the [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm).