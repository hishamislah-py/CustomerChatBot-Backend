# Connecting with AWS and VPN

Here, you can learn how to access the Thredd AWS environments if you will connect to Thredd this way. Thredd services are hosted in AWS.

Only refer to this information Thredd has confirmed that you will use it; otherwise, you can ignore this information.

There are three supported integration options for clients:

* **IPSec Site-to-Site VPN** for clients using AWS and other Cloud and on-premise infrastructure.
* **AWS Transit Gateway Peering** for clients that host their Infrastructure in AWS.
* **Mutual TLS (mTLS)** for certificate-based authentication.

For a VPN setup, Thredd provides implementation guides for connecting to Thredd. For AWS, refer to the [AWS documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-3-1.html).

See the following diagram of the flow for each option.

![](../Resources/Images/AWS_VPN_Flow.png)

## Connecting using VPN

It is the responsibility of the client to ensure that any local changes are communicated to Thredd to maintain connectivity.

Internet Protocol Security (IPsec) VPN connections take place over public networks, but the data exchanged over the VPN is still private because it is encrypted. VPNs make it possible to securely access and exchange confidential data over shared network infrastructure. In this instance, the public Internet.

IPsec is a framework of open standards to ensure private and secure communications over Internet Protocol (IP) networks. Encapsulating Security Payload (ESP) and Authentication Header (AH) are the two IPsec security protocols used to provide these security services.

### Thredd VPN Setup Information

Thredd enables a private connection from AWS for each client that sets up two VPNs per site. You must complete the Thredd VPN Connectivity Setup Form and share it with Thredd. When Thredd has received this, it sends you a configuration template for your VPN product.

Thredd typically only supports static routing for VPNs. However, in certain circumstances, Border Gateway Protocol (BGP) routing can be implemented. For AWS configurations, Thredd provides Transit Gateway (TGW) peering to allow you to connect directly to our environment and minimise latency. You must include the TGW ID when completing the Thredd VPN Connectivity Setup Form.

When a subnet has been provided, Thredd confirms that it is available. Note the following:

* An EHI endpoint must be a subnet.
* The maximum subnet is /22. Thredd recommends using /24.
* Subnet /20 is not permitted by Thredd.
* All services run through the same Thredd tunnel.

Where two VPNs are required for production access, you must split them as follows:

* Web Services and EHI
* Thredd Portal

## Connecting using AWS

It is the responsibility of the client to ensure that any local changes are communicated to Thredd to maintain connectivity.

**AWS Transit Gateway Peering**is for clients that host their Infrastructure in Amazon Web Services (AWS). Internet Protocol Security (IPsec) is a framework of open standards to ensure private and secure communications over Internet Protocol (IP) networks. Encapsulating Security Payload (ESP) and Authentication Header (AH) are the two IPsec security protocols used to provide these security services.

IPsec VPN connections take place over public networks, but the data exchanged over the VPN is still private because it is encrypted. VPNs make it possible to securely access and exchange confidential data over shared network infrastructure. In this instance, the public Internet.

### Thredd AWS Setup Information

Thredd enables a private connection from AWS for each client and sets up a transit gateway attachment per site. You must complete the Thredd VPN Connectivity Setup Form and share it with Thredd. When Thredd has received this, Thredd sends you a configuration template for your VPN product.

Thredd only supports static routing for AWS Transit Gateway (TGW) attachments. When a subnet has been provided, Thredd confirms that it is available. Note the following:

* An EHI endpoint must be a subnet.
* The maximum subnet is /22. Thredd recommends using /24.
* Subnet /20 is not permitted by Thredd.
* All services run through the same Thredd tunnel.

Where two attachments are required for production access you must split them as follows:

* Web Services and EHI
* Thredd Portal