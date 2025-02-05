---
title: Extend and customize consent
description: Learn how to extend and customize consent capabilities in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/10/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
---

# Extend and customize consent

## Prerequisites

- Basic knowledge on how to [create and debug Dataverse plugins](/power-apps/developer/data-platform/write-plug-in?tabs=pluginbase)
- Basic knowledge on how to [create custom API endpoints](/power-apps/developer/data-platform/create-custom-api-solution)
- A consent solution (DynamicsMKT_Consent) with the April 2024 update (solution version 1.1.40197.xxx or higher)
- Enabled "Multi-brand consent and customizable preference centers" in **Settings** > **Feature switches**

## Consent provider entity

The consent provider entity is the main configuration entry describing your consent solution capabilities.

| Property name              |  Description  | Mandatory | Sample  |
| -------------              | ------------- | --------- | ------- |
| msdynmkt_consentproviderid | Unique identifier for your consent provider | Yes | 003f5e82-49ce-4253-947d-8daa11f1ff75 |
| msdynmkt_consentcheckurltemplate | Unique name of the custom API that exposes your consent check | Yes | new_contosoconsentcheck |
| msdynmkt_consentproviderexternalformidentifier | Reference to the `systemform` (main form on top of the `new_contosocompliancesetting` entity) that extends the compliance profile entity UI if needed | No | 0c0126d4-d0d5-43e1-8d3b-dfa96e87285f |
| msdynmkt_consentproviderexternalentity | Reference to the entity that extends the compliance profile configuration | No | new_contosocompliancesetting |
| msdynmkt_consentproviderexternalpurposeformidentifier | Reference to the system form (main form on top of the `new_contosopurpose` entity) that extends the purpose entity user interface if needed | No | 4dfb6f18-7a89-48da-86cb-edbb9a56e3d5 |
| msdynmkt_consentproviderexternalpurposeentity | Reference to the entity that extends the compliance purpose entity | No | new_contosopurpose |
| msdynmkt_consentresolutionmessageoptions | Picklist determining how consent for the message is resolved (check out external consent resolution options) | Yes | 238550001 |
| msdynmkt_consentresolutiontrackingoptions | Picklist determining how consent for tracking is resolved (check out external consent resolution options) | Yes | 238550001 |
| msdynmkt_email_consentresolutionmessageoverride | Picklist determining how consent for the email message is resolved (check out external consent resolution channel override) | No | 238550000 |
| msdynmkt_email_consentresolutiontrackingoverride | Picklist determining how consent for the email message tracking is resolved (check out external consent resolution channel override) | No | 238550000 |
| msdynmkt_oneclickunsubscribesupported | Boolean determining whether your consent API supports one-click unsubscribe | Yes | 1 |

### Sample configuration entity

```
<?xml version="1.0" encoding="utf-8"?>
<msdynmkt_consentprovider msdynmkt_name="new_contosoconsentcheck">
  <msdynmkt_consentproviderid>003f5e82-49ce-4253-947d-8daa11f1ff75</msdynmkt_consentproviderid>
  <msdynmkt_consentcheckurltemplate>new_contosocompliancesetting</msdynmkt_consentcheckurltemplate>
  <msdynmkt_consentproviderexternalformidentifier>0c0126d4-d0d5-43e1-8d3b-dfa96e87285f</msdynmkt_consentproviderexternalformidentifier>
  <msdynmkt_consentproviderexternalentity>new_contosocompliancesetting</msdynmkt_consentproviderexternalentity>
  <msdynmkt_consentproviderexternalpurposeformidentifier>4dfb6f18-7a89-48da-86cb-edbb9a56e3d5</msdynmkt_consentproviderexternalpurposeformidentifier>
  <msdynmkt_consentproviderexternalpurposeentity>new_contosopurpose</msdynmkt_consentproviderexternalpurposeentity>
  <msdynmkt_consentresolutionmessageoptions>238550001</msdynmkt_consentresolutionmessageoptions>
  <msdynmkt_consentresolutiontrackingoptions>238550001</msdynmkt_consentresolutiontrackingoptions>
  <msdynmkt_email_consentresolutionmessageoverride>238550000</msdynmkt_email_consentresolutionmessageoverride>
  <msdynmkt_email_consentresolutiontrackingoverride>238550000</msdynmkt_email_consentresolutiontrackingoverride>
  <msdynmkt_oneclickunsubscribesupported>1</msdynmkt_oneclickunsubscribesupported>
</msdynmkt_consentprovider>
```

##  Custom API for consent checks

### Request

| Property name | Type | Description | Sample |
| ------------- | ---- | ----------- | ------ |
| contactpoints | `string[]` | Contact points to determine consent | `["john.doe@contoso.com"]` |
| purpose | `EntityReference` | Reference to the `msdymnkt_purpose` entity | 6952ed55-42bb-4549-9f8b-ddf7af3ccc82 |
| topic | `EntityReference` | Reference to the `msdynmkt_topic` entity | 1d7fc107-c915-45e9-99ef-50ad5d5c728f |
| channeltype | `string` | One of `custom`, `email`, `push` or `sms` | `email` |
| complianceprofile | `EntityReference` | Reference to the `msdynmkt_compliancesettings4` entity | 0d923da1-355e-471d-84fa-e30fa198633b |
| owningbusinessunit | `EntityReference` | Reference to the `businessunit` entity | 9a6c0f7f-9a26-4717-bb13-025fb514bc5d |
| unsubscribeurlrequired | `bool` | Whether you should provide unsubscribe URL in the response | true |
| oneclickunsubscribeurlrequired | `bool` | Whether you should provide one-click unsubscribe URL in the response | true |
| correlationheaders | `Entity` | Contains correlation headers related to journey run, useful for telemetry | N/A |

### Response

| Property name | Type | Description | 
| ------------- | ---- | ----------- |
| consents | `EntityCollection` | List of consents for given request |

Each entity in the `consents` collection should have the following properties:

| Property name | Type | Description | Sample |
| ------------- | ---- | ----------- | ------ |
| consentformessage | `bool` | Whether consent to send message is given or not | true |
| contactpoint | `string` | Carbon copy of each entry in `contactpoints`  | `"john.doe@contoso.com"` |
| unsubscribeurl | `string` | URL pointing to page where customers can manage their consent | `https://contoso.com/manage-email-sending-preferences?for=1253515123` |
| oneclickunsubscribeurl | `string` | URL pointing to page where customers can manage their consent; the URL implements [RFC 8085](https://datatracker.ietf.org/doc/html/rfc8058) | `https://contoso.com/manage-email-list?for=1253515123` |

## Create your own consent provider solution

1. Create a new blank solution.
1. Add a custom API that matches the contract of the custom API for consent checks.
1. Declare your consent provider entity in the solution (should be located under `unmanaged/msdynmkt_consentproviders/msdynmkt_cpmconsentprovider/new_contosoconsentcheck.xml`).
1. Pack your solution and import it into your dev org.
1. Go to **Settings** > **Compliance profiles** > **New profile** > **With external consent provider**, select your consent provider and save the form.
1. Enable plugin trace logs.
1. Create an email entity under **Settings** > **Compliance**. Make sure to select the newly created compliance profile.
1. Publish the email entity. At this point, the request to your consent provider should be made under the `john.doe@contoso.com` email.
    1. If the email entity validation failed, investigate the plugin trace logs for errors in your logic.
    2. If the email went live, make sure to also test a small journey. Create a static segment with your testing email address and create a segment-based journey targeting this segment. The email should be sent out to the given email address. Make sure the unsubscribe URL in the email and the `List-Unsubscribe` headers (if your consent system supports one-click unsubscribe) are set correctly.

### Sample consent provider solution

[Sample consent provider solution](https://download.microsoft.com/download/7/0/3/703e096a-c89c-4dbd-8a08-f2b43cd4edd9/ConsentProviderSample.zip)

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
