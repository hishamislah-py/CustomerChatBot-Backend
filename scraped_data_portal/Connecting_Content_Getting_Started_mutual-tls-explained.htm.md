# Mutual TLS explained

Mutual Transport Layer Security (Mutual TLS, mTLS) is an enhanced security protocol that requires a Client and Server to verify each otherâs identity before establishing a secure communication channel. This digital handshake requires both parties to provide their official identity.

## What is Transport Layer Security (TLS) and how is mTLS different?

*Transport Layer Security* (TLS) is the standard internet protocol that ensures private, secure communication. For example, it enables HTTPS, where HTTP essentially runs over TLS, to secure the websites that people visit daily. TLS uses one-way authentication, where only the Server presents a certificate to the Client to prove its identity.

With *Mutual TLS* (mTLS), this process is reciprocal, as the 'Mutual' part of its name implies. mTLS requires two-way authentication, which means that both the Client and the Server must present a valid digital certificate that allows them to verify each other's identities.

| Feature | TLS (one-way) | Mutual TLS (two-way) |
| --- | --- | --- |
| Server Authentication | Required (the Server proves its identity to the Client) | Required |
| Client Authentication | Optional (usually none) | Required (the Client proves its identity to the Server) |
| Verification method | The Server uses a Server Certificate | The Client and the Server use Certificates |

### How mTLS works using a two-way verification process

The mTLS process involves four key steps:

1. Client request: A Client (your application) attempts to connect to the Server.
2. Server challenge and authentication: The Server sends its digital certificate to the Client and simultaneously requests the Client's Transport Certificate.
3. Client certificate presentation: The Client sends its unique Transport Certificate and a digital signature back to the Server.
4. Mutual verification:

   1. The Client verifies the Server's certificate.
   2. The Server verifies the Client's Transport Certificate, checking its validity, issuing authority, and integrity.
   3. If both checks pass, the Server and Client establish a TLS connection. If a check fails, the connection is immediately terminated.

### Key benefits

By implementing mTLS, Thredd provides a significantly higher level of assurance and security for clients, and their data and services:

* Zero Trust Architecture (ZTA): mTLS is foundational to a Zero Trust security model. It ensures that no device or application is trusted by default, regardless of its location (inside or outside the network).
* Stronger authentication: It eliminates reliance on API keys alone. Your Transport Certificate is a unique, cryptographically-secured identity that is much harder to forge or steal.
* Protection against Man-In-The-Middle (MITM) attacks: The mutual verification process makes it virtually impossible for an unauthorised third party to impersonate either the client or the server to intercept data.

### Transport Certificates to connect to REST APIs via mTLS

For Thredd's systems to securely authenticate your application, you must provide a valid Transport Certificate when using mTLS. This certificate is issued by Thredd's internal Certificate Authority and acts as the digital passport for your client application.

The Transport Certificate is mandatory for mTLS and is used solely for establishing the secure connection. Without a valid, signed Transport Certificate, your application is unable to connect to Thredd's secure endpoints. You will also require a Signing Certificate.

To learn more, see [Requesting certificates for applications using mTLS.](requesting-certificates-for-mtls-connections.htm)

### Using the EHI with mTLS

In an EHIm (External Host Interface and mTLS) setup, your role of your organisation is reversed. Instead, your organisation acts as the *Server* and Thredd is the *Client*. To configure an EHIm setup, you must download and install Thredd's Trust Chain on your EHI server. You do not need to request a Transport Certificate from Thredd, but you do need to obtain a Server certificate from a Certificate of Authority vendor, such as Verizon or Digicert or Amazon Web Services.

To learn more, see [Setting up EHI for mTLS connections.](setting-up-ehi-for-mtls.htm)