# 7 Integrating 3D Secure Endpoints

This step includes setting up firewall permissions for IP addresses and integrating the Biometrics/OOB API endpoint.

## 7.1 Setting up Firewall Permissions

Firewall permissions need to be set up in both directions, between Thredd and your systems.

You will need to provide Thredd with a list of IP addresses you will be using, so that we can set up firewall permissions. These include:

* A list of the IP addresses (maximum of 5) you will use to access Thredd systems (in both UAT and Production).
* The IP addresses (maximum of 5) which Thredd will need to contact through the `DelegateSCANotification` API call. These are the resolving IP addresses of the `DelegateSCANotification` endpoint.
* A list of IP address from which you will be accessing the Thredd oAuth server.

The IP addresses should be public and static. Your organisation must own the IP addresses.

You will need to permit access on your systems to Biometric/Out of Band API calls (in both UAT and Production). For details of allowed Thredd endpoints and IP addresses, see [Authorising Thredd IP Addresses](Authorising_IP_Addresses.htm#top).