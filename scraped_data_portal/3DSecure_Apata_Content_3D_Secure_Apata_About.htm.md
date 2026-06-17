# About This Document

This document describes the 3D Secure (Apata) service and how to integrate this service with Thredd.

The information provided in this document refers to integrating with Apata as your 3D Secure provider. If you are integrating with Cardinal, refer to the Cardinal guide.

## Target Audience

This document is intended for Thredd clients (Program Managers) who are interested in integrating the 3D Secure service into their program. It is aimed at Business Analysts, and Project Leaders and developer users with an understanding of how to implement Thredd API to connect to Thredd.

## Whatâs Changed?

If you want to find out what's changed since the previous release, see the [Document History](Document_History_Apata.htm).

## How to use this Guide

If you are new to the 3D Secure service and want to understand how it works, see the [Introduction](Introduction.htm).

To find out about the steps involved in implementing the 3D Secure project, including details of the 3D Secure service configuration options, see [Steps in a 3D Secure Project](Steps_in_a_3D_Secure_project.htm#_Steps_in_a). For information on the 3D Secure API, see [Using the 3D Secure API.](Using_the_3D_Secure_API.htm)

## Related Documents

Refer to the table below for other documents which should be used in conjunction with this guide.

| Document | Description |
| --- | --- |
| [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm) | Provides details of the Thredd SOAP-based Web Services and includes a section on 3D Secure web services. |
| [Cards API Website](https://cardsapidocs.thredd.com/) | Provides details of the Thredd REST-based Cards API and includes a section on 3D Secure API. |
| [EHI Guide](https://docs.thredd.ai/EHI_Guide.htm) | Provides details of the Thredd External Host Interface (EHI). |
| [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm) | Describes how to use the Thredd Smart Client to manage your account. |
| [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm) | Describes how to use the Thredd Portal to manage card and transactions. |

## Other Guides

Refer to the table below for other relevant documents.

| Document | Description |
| --- | --- |
| EMVÂ® 3-D Secure Protocol and Core Functions Specification | You can download the latest 3D Secure protocol specification from the [EMVCo website](https://www.emvco.com/). This document provides the latest 3D Secure specifications for anyone implementing a 3D Secure project and includes information not covered in the Thredd guides, such as authentication message flows between issuer (BIN sponsor), ACS provider and merchant (PReq, PRes, AReq, ARes), and specific internal message fields that may be passed or validated (e.g., CAVV/ AAV). |
| Mastercard Identity Check Program Guide | Guide providing details of the Mastercard 3D Secure implementation. Provides details on internal Mastercard message fields (such as `acsInfoInd` and `RequestorAppUrl`). Please check on [Mastercard Connect](https://www.mastercardconnect.com/) for the latest version of this guide, which is available to Issuers (BIN sponsors). |
| Visa EMV 3D Secure 3DS User Experience Guidelines | Provides information on the Visa 3DSecure service. See <https://developer.visa.com/pages/visa-3d-secure>. |