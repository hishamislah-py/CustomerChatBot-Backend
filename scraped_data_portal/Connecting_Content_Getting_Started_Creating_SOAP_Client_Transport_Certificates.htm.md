# Creating Transport Certificates for SOAP Web Services

This page describes how you create Transport Certificates for accessing Threddâs SOAP Web Services. As Thredd's SOAP Web Services are secured using Mutual Transport Layer Security (MTLS), your *client application* must present a trusted Transport Certificate for authentication.

The instructions for obtaining certificates are the same as those for clients using Thredd's REST APIs.

To obtain certificates, you must first set up a Super Admin user in Thredd Portal, create an application and OAuth Client, and then request certificates for it. See [Requesting certificates for applications using mTLS](requesting-certificates-for-mtls-connections.htm).

### Convert the certificate and key to PKCS#12 syntax

If required, for example you are using Windows services, you can convert the public certificate and private key to the PKCS#12 syntax. For converting, you can use OpenSSL commands. In the PKCS#12 syntax, the files are in the .pfx format. For more details, see [RFC 7292: PKCS #12: Personal Information Exchange Syntax v1.1](https://datatracker.ietf.org/doc/html/rfc7292).