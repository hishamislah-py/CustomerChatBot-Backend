# 7 Integrating RDX Endpoints

This step includes setting up firewall permissions for IP addresses and integrating the Biometrics API endpoint.

## 7.1 Setting up Firewall Permissions

Firewall permissions need to be set up in both directions, between Thredd and your systems.

You must provide Thredd with a list of IP addresses you will be using, so that we can set up firewall permissions. This includes:

* A list of the IP addresses you will use to access Thredd systems (in both UAT staging and Production).
* The IP addresses you will use for sending API messages to Thredd (in both UAT staging and Production).
* The IP addresses you will use for oAuth (in both UAT staging and Production) to be authorised at Thredd.

You will need to permit access on your systems to [Thredd oAuth](Using_Oauth.htm#_Authorising_GPS_IP) and [3D Secure RDX API](Using_Card_Enrolment_API.htm) calls (in both UAT staging and Production). For details of the Thredd IP addresses to allow, see [Authorising IP Addresses](Authorising_IP_Addresses.htm) (Your Thredd 3DS project manager will provide you with details of any additional Thredd IP addresses that may be needed.)

## 7.2 Implementing the Biometrics API

Please provide Thredd with the `NotifyInitiateAction` API endpoints we should use to send Biometric verification requests to your systems (one for UAT staging and one for Production). You should provide these details on your 3DS Product Setup Form. See the section [Client Information](Completing_the_PSF.htm#_Client_Information) .

When your systems receive a request at this endpoint, they should initiate a Biometric or In-App session as described in the section [Using the Biometric/In-App Authentication API](Using_Biometric_API.htm).

Once completed, your systems should return the result to Thredd, using the `NotifyValidate` API. See [Notifying Thredd of the Result of the Biometric Session](Using_Biometric_API.htm#_Notifying_Thredd_of).

## 7.3 Implementing oAuth Access

You must authenticate against the Thredd oAuth server before you can use the 3D Secure RDX API services. The oAuth server provides you with a token that you must include in your API requests to access the RDX API services. You can also use the oAuth server to validate the Token in the `NotifyInitiateAction` API requests received from Thredd.

For details, see [Using the Thredd oAuth Server](Using_Oauth.htm).