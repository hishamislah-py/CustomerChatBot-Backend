# Troubleshooting FAQs

This section provides answers to common integration issues.

## Connection Issues

#### Why am I unable to connect to Thredd?

To confirm if you can connect to Thredd, you should use a web service such as [Check Service Availability](Web_services_api/Check_Service_Availability.htm): `Ws_Check`. This should return a response with an [Action Code](Reference/Action_Codes.htm) of 000.

If you still cannot connect, check to confirm the following:

* You are using the correct API endpoint and environment (test or production)
* The credentials (username and password) you are using are correct for the environment
* Thredd has enabled your IP address to use this service
* You will need a secure connection to Thredd.
* The ports on your firewall have been configured to allow traffic from Thredd
* You have enabled the Thredd IP address to use this service in the test environment

For further details, contact your Implementation Manager.

## Web Service Issues

#### Why has my web service request failed?

When submitting a web service request to an API endpoint, Thredd responds with an [Action Code](Reference/Action_Codes.htm) to indicate the status of the request.

Below are common reasons for API request failures:

* Incorrect username and password (Action Code 999) or issuer code ( Action Code 801).
* The value provided in the `<WSID>` tag is not unique. A unique `<WSID>` must be provided for most web services.
* Mandatory fields required in the request have not been supplied. Check the relevant web service description in this guide for details of mandatory fields.
* The requested object you want to query or update, for example, existing card, does not exist. Make sure you have provided the correct reference to the object you want to update.
* The format or type of value provided in an XML tag is incorrect. Check the relevant web service description in this guide for details of the allowed formats and expected values.
* If you change the default `xmlns` attributes (XML namespaces) in the SOAP request, this causes an error.
* Check that there are no spaces in xml tags, as this causes an error.
* XML tag spelling or case is incorrect. Each web service implements its own naming convention standard and tag names, so these cannot be copied across different web services. If in doubt, always check the [WSDL![Closed](../Skins/Default/Stylesheets/Images/transparent.gif) Web Service Definition Language (WSDL) is an XML format for describing network services as a set of endpoints operating on messages containing either document-oriented or procedure-oriented information.
  WSDL files are central to testing SOAP-based services. SoapUI uses WSDL files to generate test requests, assertions and mock services.](#) for the correct XML tag name. See [Using the API](Getting_started/Using_SOAP.htm).

## 3D Secure Issues

#### Why am I unable to enrol or edit a cardholder in 3D Secure?

If you are using the Cardinal Batch Interface (legacy service), your changes may take up to two hours to implement, since Thredd send updates in an hourly batch file at 20 past the hour. You should wait two hours between batch file web services to ensure they are all processed by both Thredd and Cardinal, before sending any follow-up requests.

For an improved service, we recommend you upgrade to using the real-time data exchange 3D Secure Interface. See [3D Secure Credentials (Cardinal and Apata)](Web_services_api/3D_Secure_RDX_Credentials.htm): `Ws_AddUpDelCredentials`

For further details of Thredd support for 3D Secure, see our [3D Secure FAQs](FAQs.htm#3D).

## Known Issues

For a list of known issues, contact your Implementation Manager.