# 1.2 EHI Version Control

The currently supported EHI versions are 3.x, 4.x and 5.x.

Thredd creates new EHI versions for new functionality as required by scheme and regulatory changes and/or client enhancements. These are available to all customers.

We distinguish between the following versions:

* *Major versions*: add significant functionality (e.g. MDES). Examples of major version numbers are: 3.0, 4.0, 5.0, and so on.
* *Minor versions*: add minimal functionality (e.g. new field). Examples of minor version numbers are: 4.1, 4.2, 4.3, 5.1. and so on.
* *Document versions*: reflect guide update. Examples of document version numbers are: 4.0.1, 4.0.2, 4.0.3. and so on.

We send notifications out to you whenever there is a new release. To [upgrade your EHI version](#Upgradin), contact your Thredd account manager or Thredd implementation manager.

## 1.2.1 Adding New Fields

When Thredd needs to add new fields, we increase the minor version.  We keep a record of which EHI version requires which fields. When you connect to the EHI, the system looks up your current EHI version and sends you only the fields that are associated with that version.

If we add new values to an existing field, you receive the new values (that is, the EHI version protects which fields you receive, not the values inside existing fields.)

For a list of EHI fields available with each of the supported EHI versions, see [EHI Versions](../Appendices/EHI_Versions.htm).

## 1.2.2 Upgrading your EHI Version

Thredd recommends that you upgrade your EHI version to one of the currently supported versions. Versions 3 onwards provide access to ThreddNet, with enhanced EHI features such as load balancing, a streamlined service architecture, support for multiple external host endpoints, faster response times and reduced connection timeouts.

### Decommissioning of old EHI Versions

If you are on an older version of EHI, prior to 3.x, we recommend you upgrade. Older versions that are no longer supported may be decommissioned in the future.

## 1.2.3 Best Practise for Customer Implementations

* Regularly upgrade to ensure you are on a supported EHI version. You should develop EHI integration with an awareness that older, unsupported versions are no longer being tested.
* Ignore all fields you are not expecting, and do not treat this as an error. This will mean that you can upgrade to a new EHI version, without making any changes on your side.
* In order to use any new EHI fields and functionality you may need to update your systems. For details of new fields that have been added to a release, see [EHI Versions](../Appendices/EHI_Versions.htm). For details of additional changes, see the [Documentation History](../Document_history.htm).