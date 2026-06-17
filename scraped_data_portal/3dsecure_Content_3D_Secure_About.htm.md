# About This Document

This document describes the 3D Secure (Cardinal) authentication service and integrating this service with Thredd.

The information provided in this document refers to integrating with Cardinal as your 3D Secure provider. If you are integrating with Apata, refer to the Apata guide.

## Target Audience

This document is intended for Thredd clients (Program Managers) who are interested in integrating the 3D Secure (Cardinal) service with OTP, Biometric, In-App or KBA authentication into their program. It is aimed at developer users, with an understanding of how to implement the Thredd API to connect to Thredd.

## Whatâs Changed?

If you want to find out what's changed since the previous release, see the [Document History](../Document_History.htm).

## How to use this Guide

If you are new to the 3D Secure service and want to understand how it works, see the [Introduction](Introduction.htm).

To find out about the steps involved in implementing the 3D Secure project, including details of the 3D Secure service configuration options, see [Steps in a 3D Secure Biometric/In-app Project](Steps_in_a_3D_Secure_Biometric.htm#_Steps_in_a).

For information on the 3D Secure API, see [Using the 3D Secure API](Using_the_3D_Secure_API.htm)

## Related Documents

Refer to the table below for other documents which should be used in conjunction with this guide.

| Document | Description |
| --- | --- |
| [Web Service Guide (SOAP)](https://docs.thredd.ai/Web_Services_Guide.htm) | Provides details of the Thredd API and includes a section on 3D Secure web services. |
| [Cards API Website (REST)](https://cardsapidocs.thredd.com/) | Provides details of the Thredd REST-based Cards API and includes a section on 3D Secure API. |
| [EHI Guide](https://docs.thredd.ai/EHI_Guide.htm) | Provides details of the Thredd External Host Interface (EHI). |
| [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm) | Describes how to use the legacy Thredd Smart Client application to manage your account. |
| [Thredd Portal Guide](https://docs.thredd.ai/Thredd_Portal_Guide.htm) | Describes how to use the new Thredd Portal, the new online user interface, to manage your account. |

## Other Guides

Refer to the table below for other relevant documents.

| Document | Description |
| --- | --- |
| EMV 3DS Global Consumer Screen Template Guide | A PDF guide for configuration of the 3D Secure Authentication Service screens shown to cardholders during a 3D Secure session. This guide contains editable fields and you should work with your Thredd 3DS project manager to review this guide and complete these fields. |
| Cardinal Guides | Cardinal provides several guides related to their service. You should refer to these guide when setting up your 3D Secure rules and managing your service on the Cardinal Portal.   | Guide | Description | | --- | --- | | Customer Service Application: Portal User Guide | This document provides users step-by-step instructions for using the Customer Service application in the VCAS Portal. | | EMV 3DS Reporting Suite: Portal User Guide | This guide outlines how to use the EMV 3DS Reporting Suite application within the VCAS Portal to effectively monitor and control authentication performance. | | EMV 3DS Rules Application : Portal User Guide | This document includes information on how to create, edit, test, and publish rules and policies as well as how to generate lists for use in rules. | | User Management Application: Portal User Guide | This document provides users step-by-step instructions for using the User Management application in the VCAS Portal. | | VCAS Compliance Manager Portal User Guide | This guide provides an overview of how the Compliance Manager application works and outlines how to manage the features of the Compliance Manager application. | | VCAS Test Store Guide | This guide provides an overview of how the test store application works and provides instructions on how to run test transactions in the test store application. |   For the latest versions, please check with your 3DS project manager  Thredd also provide training on how to use the Cardinal Portal. For details, please contact your Thredd 3DS project manager. |
| EMVÂ® 3-D Secure Protocol and Core Functions Specification | You can download the latest 3D Secure protocol specification from the [EMVCo website](https://www.emvco.com/). This document provides the latest 3D Secure specifications for anyone implementing a 3D Secure project and includes information not covered in the Thredd guides, such as authentication message flows between issuer (BIN sponsor), ACS provider and merchant (PReq, PRes, AReq, ARes), and specific internal message fields that may be passed or validated (e.g., CAVV/ AAV). |
| Mastercard Identity Check Program Guide | Guide providing details of the Mastercard 3D Secure implementation. Provides details on internal Mastercard message fields (such as `acsInfoInd` and `RequestorAppUrl`). Please check on [Mastercard Connect](https://www.mastercardconnect.com/) for the latest version of this guide which is available to Issuers (BIN sponsors). |
| Visa EMV 3D Secure 3DS User Experience Guidelines | Provides information on the Visa 3DSecure service. See <https://developer.visa.com/pages/visa-3d-secure>. |

For the latest technical documentation, see the [Documentation Portal](https://docs.thredd.ai).