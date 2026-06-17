# 11 Authorising Thredd IP Addresses

The following URLs must be allowed on your firewall to enable oAuth and RDX API communication to support Biometric/In-App authentication:

#### UAT Environment (RDX.API)

| Endpoint | Server name | Inbound IP | Outbound IP | Components |
| --- | --- | --- | --- | --- |
| *https://vcasuat.globalprocessing.net* | GPS-UAT-RDX-01 | 3.10.135.193 | 3.10.135.193  3.9.27.216 | GPS.VCAS.RDX.API |
| *https://oauthuat.globalprocessing.net* | GPS-UAT-RDX-01 | 3.10.135.193 | 3.10.135.193  3.9.27.216 | GPS.Identity.Api |

#### PRDZ Cloud Production Environment

| Endpoint | Inbound IP | Outbound IP | Components |
| --- | --- | --- | --- |
| *https://p0ivcas.globalprocessing.net* | 3.10.200.197  3.10.133.128 | 3.10.200.197  3.10.133.128 | GPS.VCAS.RDX.API |
| *https://p1ists.globalprocessing.net* | 3.10.200.197  3.10.133.128 | 3.10.200.197  3.10.133.128 | GPS.Identity.Api |

#### PRD1 Cloud Production Environment

For secure RDX API communication between Thredd and your systems when using one of our cloud-based production environments, please allow the following public IP address on your firewall: 91.194.25.213 and 91.194.25.212.

PRD1 is for Thredd clients using the Cloud Europe Instance of Thredd platform.

Your firewall also allows the following additional IP addresses:

| Endpoint | Environment | Server name | IP | Components |
| --- | --- | --- | --- | --- |
| p1ivcas.globalprocessing.net | PRD1 | P1B-I2-RDX01  P1A-I2-RDX01 | 18.156.16.255 | GPS.VCAS.RDX.API |
| p1ists.globalprocessing.net | PRD1 | P1B-I2-RDX01  P1A-I2-RDX01 | 3.123.216.247 | GPS.Identity.Api |

#### PRD2 - Cloud Production Environment

For secure RDX API communication between Thredd and your systems when using one of our cloud-based production environments, please allow the following public IP address on your firewall: 91.194.104.212 and 91.194.104.213.

PRD2 is for Thredd clients using the Cloud Asia Pacific Instance of Thredd platform.

Your firewall also allows the following additional IP addresses:

| Endpoint | Environment | Server name | IP | Components |
| --- | --- | --- | --- | --- |
| p2ivcas.globalprocessing.net | PRD2 | P2B-I2-RDX01  P2A-I2-RDX01 | 3.1.92.70 | GPS.VCAS.RDX.API |
| p1ists.globalprocessing.net | PRD2 | P2B-I2-RDX01  P2A-I2-RDX01 | 3.1.92.70 | GPS.Identity.Api |