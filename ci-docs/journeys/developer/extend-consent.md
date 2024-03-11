# Extending consent
## Pre-requisites 
- Basic knowledge on how to [create and debug dataverse plugins](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/write-plug-in?tabs=pluginbase)
- Basic knowledge on how to [create custom api endpoint](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/create-custom-api-solution)
- Consent solution (DynamicsMKT_Consent) with April 2024 update (solution version 1.1.40197.xxx or higher)
- Enabled 'Multi-brand consent and customizable preference centers' in Settings -> Feature switches

## Consent provider entity
Consent provider entity is the main configuration entry describing your consent solution capabilities.
| Property name              |  Description  | Mandatory | Sample  |
| -------------              | ------------- | --------- | ------- |
| msdynmkt_consentproviderid | Unique identifier for your consent provider | Yes | 003f5e82-49ce-4253-947d-8daa11f1ff75 |
| msdynmkt_consentcheckurltemplate | Unique name of custom api that exposes your consent check | Yes | new_contosoconsentcheck |
| msdynmkt_consentproviderexternalformidentifier | reference to systemform (main form on top of new_contosocompliancesetting entity) that will extend compliance profile entity UI if needed | No | 0c0126d4-d0d5-43e1-8d3b-dfa96e87285f |
| msdynmkt_consentproviderexternalentity | reference to entity that will extend compliance profile configuration | No | new_contosocompliancesetting |
| msdynmkt_consentproviderexternalpurposeformidentifier | reference to system form (main form on top of new_contosopurpose entity) that will extend purpose entity UI if needed | No | 4dfb6f18-7a89-48da-86cb-edbb9a56e3d5 |
| msdynmkt_consentproviderexternalpurposeentity | reference to entity that will extend compliance purpose entity | No | new_contosopurpose |
| msdynmkt_consentresolutionmessageoptions | picklist determining how consent for message is resolved (check out External consent resolution options) | Yes | 238550001 |
| msdynmkt_consentresolutiontrackingoptions | picklist determining how consent for tracking is resolved (check out External consent resolution options) | Yes | 238550001 |
| msdynmkt_email_consentresolutionmessageoverride | picklist determing how consent for email message is resolved (check out External consent resolution channel override) | No | 238550000 |
| msdynmkt_email_consentresolutiontrackingoverride | picklist determing how consent for email message tracking is resolved (check out External consent resolution channel override) | No | 238550000 |
| msdynmkt_oneclickunsubscribesupported | boolean, determining whether your consent api supports one-click unsubscribe | Yes | 1 |

Sample configuration entity
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

##  Custom api for consent checks
### Request
| Property name | Type | Description | Sample |
| ------------- | ---- | ----------- | ------ |
| contactpoints | `string[]` | Contact points for which to determine consent | `["john.doe@contoso.com"]` |
| purpose | `EntityReference` | Reference to the `msdymnkt_purpose` entity | 6952ed55-42bb-4549-9f8b-ddf7af3ccc82 |
| topic | `EntityReference` | Reference to the `msdynmkt_topic` entity | 1d7fc107-c915-45e9-99ef-50ad5d5c728f |
| channeltype | `string` | One of `custom`, `email`, `push` or `sms` | `email` |
| complianceprofile | `EntityReference` | Reference to the `msdynmkt_compliancesettings4` entity | 0d923da1-355e-471d-84fa-e30fa198633b |
| owningbusinessunit | `EntityReference` | Reference to the `businessunit` entity | 9a6c0f7f-9a26-4717-bb13-025fb514bc5d |
| unsubscribeurlrequired | `bool` | Whether you should provide unsubscribe url in the response | true |
| oneclickunsubscribeurlrequired | `bool` | Whether you should provide one-click unsubscribe url in the response | true |
| correlationheaders | `Entity` | Contains correlation headers related to journey run - usefull for telemetry | N/A |

### Response
| Property name | Type | Description | 
| ------------- | ---- | ----------- |
| consents | `EntityCollection` | List of consents for given request |

Each entity in `consents` collection should be having following properties
| Property name | Type | Description | Sample |
| ------------- | ---- | ----------- | ------ |
| consentformessage | `bool` | Whether consent to send message is given or not | true |
| contactpoint | `string` | Carbon copy of each entry in contactpoints  | `"john.doe@contoso.com"` |
| unsubscribeurl | `string` | Url pointing to page where customer can manage their consent | `https://contoso.com/manage-email-sending-preferences?for=1253515123` |
| oneclickunsubscribeurl | `string` | Url pointing to page where customer can manage their consent, the url is implementing [RFC 8085](https://datatracker.ietf.org/doc/html/rfc8058) | `https://contoso.com/manage-email-list?for=1253515123` |

# Create your own consent provider solution
 - Create a new blank solution
 - Add there a custom api that is matching the contract of Custom api for consent checks
 - Declare your consent provider entity in the solution (should be located under `unmanaged/msdynmkt_consentproviders/msdynmkt_cpmconsentprovider/new_contosoconsentcheck.xml`)
 - Pack your solution and import it to your dev org
 - Go to Settings -> Compliance Profiles -> New Profile -> With external consent provider -> select your consent provider and save the form
 - Enable plugin trace logs
 - Create email entity, under Settings -> Compliance -> make sure to select the newly create compliance profile
 - Publish email entity - at this point request to your consent provider should be made under the `john.doe@contoso.com` email - if the validation of email entity failed investigate plugin trace logs for errors in your logic
 - If the email went live make sure to also test small journey - create static segment with your testing email address, create a segment-based journey targeting this segment - email should be sent out to give email address, make sure the unsubscribe url in the email and List-Unsubscribe headers (if your consent system supports  1CU) are set correctly
 
   
