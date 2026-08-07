---
title: Permission changes in the June 2026 release (version 1.2.437.94)
description: The June 2026 release changed permissions for 9 out-of-the-box roles in Customer Insights - Journeys, with breaking changes in 7 of them.
ms.date: 08/05/2026
ms.topic: article
author: vinayd
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Permission changes in the June 2026 release (version 1.2.437.94)

This article details the permission changes introduced in the **June 2026 release (version 1.2.437.94)** for the out-of-the-box roles in Customer Insights - Journeys. For background on how to use this changelist to keep custom roles in sync, see [Permission changes in each release](role-permissions.md). *BU* (used throughout this article) stands for *business unit*.

## Change summary

| **Metric** | **Count** |
|---|---|
| Roles modified | 9 |
| Roles added | 0 |
| Roles deleted | 0 |
| Privileges added | 563 |
| Privileges removed | 222 |
| Privilege level changed | 170 |
| Privilege moved | 578 |
| Breaking changes | Yes (7 roles) |

## Role: Event Administrator

**Role identifier:** {a31a2242-bf8f-e611-80d7-00155d4b201d}

### Changelist-1 Added (Tables and privileges that exist in this release but not in the previous release)

This role doesn't add any tables.

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

This role doesn't update any table privileges.

## Role: Event Administrator (BU level)

**Role identifier:** {07d52deb-3b54-4203-b3cf-35efe4350f82}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

This role doesn't add any tables.

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

### Changelist-3 Updated (Privileges that changed in this release compared to the previous release)

This role doesn't update any table privileges.

## Role: Event Planner (BU level)

**Role identifier:** {9d0bcbb3-75d8-4496-b2fb-62d0a9cb902f}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

This role doesn't add any tables.

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

### Changelist-3 Updated (Privileges that changed in this release compared to the previous release)

This role doesn't update any table privileges.

## Role: Lead Score Modeler

**Role identifier:** {d1fd2176-cee8-e611-80d8-00155d4b205a}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 | Local | Local | Local | Local | Local |
| msdyncrm_leadscoremodel | Global | Global | Local | Global | Global |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

No tables were removed from this role.

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

No table privileges were updated for this role.

## Role: Lead Score Viewer

**Role identifier:** {32e87eb4-c85c-e711-80fe-000d3a297db2}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 | Local |  |  |  |  |
| msdyncrm_leadscoremodel | Local |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

No tables were removed from this role.

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

No table privileges were updated for this role.

## Role: Marketing Manager - Business

**Role identifier:** {bf157a3a-cde8-e611-80d8-00155d4b205a}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_compliancesettings3 |  |  | Deep |  |  |
| msdynmkt_matchingstrategyattribute |  |  |  | Deep |  |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| Adx_pagetemplate |
| Adx_publishingstate |
| Adx_webpage |
| Adx_website |
| Adx_websiteaccess |
| Adx_websitebinding |
| ChannelPropertyGroup |
| DuplicateRule |
| EmailTemplate |
| GoalRollupQuery |
| NewsArticle |
| PrincipalObjectAttributeAccess |
| User |
| adx_portallanguage |
| adx_websitelanguage |
| adx_webtemplate |
| msdyncrm_appointmentactivity |
| msdyncrm_appointmentactivitymarketingtemplate |
| msdyncrm_cdnconfiguration |
| msdyncrm_cdsaconnectorconfiguration |
| msdyncrm_contentblock |
| msdyncrm_contentsettings |
| msdyncrm_createleadactivity |
| msdyncrm_customerinsightsinfo |
| msdyncrm_customerjourney |
| msdyncrm_customerjourneycustomchannelactivity |
| msdyncrm_customerjourneyiteration |
| msdyncrm_customerjourneyruntimestate |
| msdyncrm_customerjourneytemplate |
| msdyncrm_customerjourneyworkflowlink |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_delaydatetimeactivity |
| msdyncrm_delaydurationactivity |
| msdyncrm_deprecatedcustomtileactivity |
| msdyncrm_deprecatedeventactivity |
| msdyncrm_deprecatedformsprosurveyactivity |
| msdyncrm_deprecatedpageactivity |
| msdyncrm_designerfeatureavailability |
| msdyncrm_formpage |
| msdyncrm_formpagetemplate |
| msdyncrm_geopin |
| msdyncrm_gwennolfeatureconfiguration |
| msdyncrm_gwennolspamscoreactivity |
| msdyncrm_gwennolspamscorerequest |
| msdyncrm_launchworkflowactivity |
| msdyncrm_leadscoringconfiguration |
| msdyncrm_leadtoopportunity |
| msdyncrm_linkedincampaignactivity |
| msdyncrm_listform |
| msdyncrm_liveentitydependency |
| msdyncrm_marketingconfiguration |
| msdyncrm_marketingdynamiccontentmetadata |
| msdyncrm_marketingemail |
| msdyncrm_marketingemailactivity |
| msdyncrm_marketingemaildynamiccontentmetadata |
| msdyncrm_marketingemailtemplate |
| msdyncrm_marketingemailtest |
| msdyncrm_marketingemailtestattribute |
| msdyncrm_marketingemailtestsend |
| msdyncrm_marketingfieldsubmission |
| msdyncrm_marketingform |
| msdyncrm_marketingformactivity |
| msdyncrm_marketingformfield |
| msdyncrm_marketingformformwhitelistrule |
| msdyncrm_marketingformsubmission |
| msdyncrm_marketingformtemplate |
| msdyncrm_marketingformwhitelistrule |
| msdyncrm_marketingpage |
| msdyncrm_marketingpageconfiguration |
| msdyncrm_marketingpagetemplate |
| msdyncrm_matchingstrategy |
| msdyncrm_matchingstrategyattribute |
| msdyncrm_mktactivity |
| msdyncrm_networkpage |
| msdyncrm_personalizedpage |
| msdyncrm_personalizedpagefield |
| msdyncrm_phonecallactivity |
| msdyncrm_phonecallactivitymarketingtemplate |
| msdyncrm_portalsettings |
| msdyncrm_postingishts |
| msdyncrm_quicksendemail |
| msdyncrm_reaction |
| msdyncrm_recordupdateactivity |
| msdyncrm_redirecturl |
| msdyncrm_segment |
| msdyncrm_segmentactivity |
| msdyncrm_segmenttemplate |
| msdyncrm_socialpost |
| msdyncrm_socialpostingconfiguration |
| msdyncrm_socialpostingconsent |
| msdyncrm_sourceactivity |
| msdyncrm_splitteractivity |
| msdyncrm_tag |
| msdyncrm_taskactivity |
| msdyncrm_taskactivitymarketingtemplate |
| msdyncrm_triggeractivity |
| msdyncrm_uicconfig |
| msdyncrm_usergeoregion |
| msdyncrm_usersetting |
| msdyncrm_website |
| msgdpr_gdprconfiguration |
| msgdpr_gdprconsentchangerecord |

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| ActionCard | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep | Global → Deep |
| Activity | Global → Deep | Local → Deep | Local → Deep | Local → Deep | Local → Deep |
| CustomerOpportunityRole | Global → Deep | Local → Deep | Local → Deep | Global → Deep | Global → Deep |
| CustomerRelationship | Global → Deep | Local → Deep | Local → Deep | Global → Deep | Global → Deep |
| DuplicateRule | Global → Deep |  |  |  |  |
| EmailSignature | Global → Deep | Global → Deep | Local → Deep |  |  |
| EmailTemplate | Global → Deep | Global → Deep | Local → Deep |  |  |
| Feedback | Global → Deep |  |  | Global → Deep | Global → Deep |
| GoalRollupQuery | Basic → Deep |  |  |  |  |
| Import | Local → Deep | Local → Deep | Local → Deep | Local → Deep | Local → Deep |
| ImportFile | Local → Deep | Local → Deep | Local → Deep | Local → Deep | Local → Deep |
| ImportMap | Global → Deep | Local → Deep | Local → Deep | Local → Deep | Local → Deep |
| Mailbox | Basic → Deep | Basic → Deep |  | Basic → Deep |  |
| MailboxTrackingFolder | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep |  |
| MailMergeTemplate | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep |
| msdyn_PostAlbum | Global → Deep | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep |
| msdyn_wallsavedqueryusersettings | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep |
| msdyncrm_leadscoremodel | Global → Deep | Global → Deep | Local → Deep | Global → Deep | Global → Deep |
| Note | Global → Deep | Basic → Deep | Local → Deep | Local → Deep | Local → Deep |
| PostFollow | Global → Deep |  | Local → Deep | Local → Deep |  |
| SharePointSite | Global → Deep |  |  |  | Global → Deep |
| SocialProfile | Global → Deep | Global → Deep | Local → Deep | Global → Deep | Global → Deep |
| SyncError | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep | Basic → Deep |
| WorkflowSession |  | Local → Deep | Local → Deep | Local → Deep | Local → Deep |

## Role: Marketing Manager (BU level) - Business

**Role identifier:** {dd84f17f-cde8-e611-80d8-00155d4b205a}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Deep | Deep | Deep | Deep | Deep |
| ActionCard | Deep | Deep | Deep | Deep | Deep |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Deep | Deep | Deep | Deep | Deep |
| AppConfigMaster | Global |  |  |  |  |
| ApplicationFile | Global |  |  |  |  |
| AsyncOperation | Deep | Deep |  |  | Deep |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Deep |  |  |  | Deep |
| Campaign | Deep |  |  | Deep | Deep |
| ChannelPropertyGroup | Global |  |  | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Deep | Deep | Deep | Deep | Deep |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Deep | Deep | Deep | Deep | Deep |
| CustomerOpportunityRole | Deep | Deep | Deep | Deep | Deep |
| CustomerRelationship | Deep | Deep | Deep | Deep | Deep |
| Customization | Global |  |  |  |  |
| DocumentTemplate | Global |  |  |  |  |
| DuplicateRule | Deep |  |  |  |  |
| EmailServerProfile | Global |  |  |  | Global |
| EmailSignature | Deep | Deep | Deep |  |  |
| EmailTemplate | Deep | Deep | Deep | Deep |  |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| ExchangeSyncIdMapping | Basic | Basic | Basic |  |  |
| Feedback | Deep |  |  | Deep | Deep |
| FieldSecurityProfile | Global |  |  |  |  |
| GoalRollupQuery | Deep |  |  |  |  |
| HierarchyRule | Global |  |  |  |  |
| Import | Deep | Deep | Deep | Deep | Deep |
| ImportFile | Deep | Deep | Deep | Deep | Deep |
| ImportMap | Deep | Deep | Deep | Deep | Deep |
| LanguageLocale | Global |  |  | Global | Global |
| Lead | Deep | Deep | Deep | Deep | Deep |
| LeadToOpportunitySalesProcess | Global | Global | Global | Global | Global |
| License | Global |  |  |  |  |
| List | Deep | Deep | Deep | Deep | Deep |
| Mailbox | Deep | Deep |  | Deep |  |
| MailboxTrackingFolder | Deep | Deep | Deep | Deep |  |
| MailMergeTemplate | Deep | Deep | Deep | Deep | Deep |
| MobileOfflineProfile | Global |  |  |  |  |
| msdyn_odatav4ds | Global | Global |  | Global | Global |
| msdyn_PostAlbum | Deep | Deep | Deep | Deep | Deep |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_PostRuleConfig | Global |  |  |  |  |
| msdyn_wallsavedquery | Global |  |  |  |  |
| msdyn_wallsavedqueryusersettings | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_emailkeypoint | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Deep | Global | Global | Global | Global |
| msdyncrm_gpt3log | Global |  |  |  |  |
| msdyncrm_leadscoremodel | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_textstyle | Global |  |  |  |  |
| msdynmkt_compliancesettings |  | Global |  |  |  |
| msdynmkt_contactpointsettings |  | Global |  |  |  |
| msdynmkt_frequencycap |  | Global | Global | Global | Global |
| msdynmkt_smsphonenumber |  | Global | Global |  |  |
| NewsArticle | Global |  |  |  |  |
| Note | Deep | Deep | Deep | Deep | Deep |
| Opportunity | Deep | Deep | Deep | Deep | Deep |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrgEmailTemplates |  |  | Global |  |  |
| PersonalDocumentTemplate | Basic | Basic | Basic | Basic | Basic |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Position | Global |  |  |  |  |
| Post | Global |  | Global | Global | Global |
| PostFollow | Deep |  | Deep | Deep |  |
| Product | Global |  |  |  |  |
| Query | Global | Global | Global |  |  |
| RecommendedDocument | Global |  |  |  |  |
| RecordAuditHistory | Global |  |  |  |  |
| Relationship | Global |  |  |  |  |
| RelationshipRole | Global |  |  |  |  |
| Role | Local |  |  |  |  |
| SavedQueryVisualizations | Global | Global | Global |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Deep |  |  |  | Deep |
| SocialProfile | Deep | Deep | Deep | Deep | Deep |
| Subject | Global |  |  |  | Global |
| SyncError | Deep | Deep | Deep | Deep | Deep |
| SystemApplicationMetadata | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| SystemUser |  |  |  |  | Global |
| Team | Global | Global | Local | Global | Global |
| TraceLog | Global |  | Global | Global | Global |
| TransactionCurrency | Global |  |  | Global | Global |
| User | Global |  |  | Deep | Deep |
| UserApplicationMetadata | Basic | Basic | Basic |  |  |
| UserEntityInstanceData | Basic | Basic | Basic |  |  |
| UserEntityUISettings | Basic | Basic | Basic |  |  |
| UserForm | Basic | Basic | Basic |  |  |
| UserQuery | Basic | Basic | Basic |  |  |
| UserQueryVisualizations | Basic | Basic | Basic |  |  |
| UserSettings | Global | Local | Local |  | Local |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Deep | Deep | Deep | Global |
| WorkflowSession | Global | Deep | Deep | Deep | Deep |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| msdyncrm_gwennolfeatureconfiguration |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |
| msdyncrm_segment |
| msgdpr_gdprconfiguration |

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

No table privileges were updated for this role.

## Role: Marketing Professional - Business

**Role identifier:** {ce995e5a-cee8-e611-80d8-00155d4b205a}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_compliancesettings3 |  | Local | Local |  |  |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| Adx_pagetemplate |
| Adx_publishingstate |
| Adx_webpage |
| Adx_website |
| Adx_websiteaccess |
| Adx_websitebinding |
| adx_portallanguage |
| adx_websitelanguage |
| adx_webtemplate |
| msdyn_PostAlbum |
| msdyn_PostConfig |
| msdyn_PostRuleConfig |
| msdyn_odatav4ds |
| msdyn_wallsavedquery |
| msdyn_wallsavedqueryusersettings |
| msdyncrm_appointmentactivity |
| msdyncrm_appointmentactivitymarketingtemplate |
| msdyncrm_cdnconfiguration |
| msdyncrm_cdsaconnectorconfiguration |
| msdyncrm_contentblock |
| msdyncrm_contentsettings |
| msdyncrm_createleadactivity |
| msdyncrm_customerinsightsinfo |
| msdyncrm_customerjourney |
| msdyncrm_customerjourneycustomchannelactivity |
| msdyncrm_customerjourneyiteration |
| msdyncrm_customerjourneyruntimestate |
| msdyncrm_customerjourneytemplate |
| msdyncrm_customerjourneyworkflowlink |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_delaydatetimeactivity |
| msdyncrm_delaydurationactivity |
| msdyncrm_deprecatedcustomtileactivity |
| msdyncrm_deprecatedeventactivity |
| msdyncrm_deprecatedformsprosurveyactivity |
| msdyncrm_deprecatedpageactivity |
| msdyncrm_designerfeatureavailability |
| msdyncrm_formpage |
| msdyncrm_formpagetemplate |
| msdyncrm_geopin |
| msdyncrm_gwennolfeatureconfiguration |
| msdyncrm_gwennolspamscoreactivity |
| msdyncrm_gwennolspamscorerequest |
| msdyncrm_launchworkflowactivity |
| msdyncrm_leadtoopportunity |
| msdyncrm_linkedincampaignactivity |
| msdyncrm_listform |
| msdyncrm_liveentitydependency |
| msdyncrm_marketingconfiguration |
| msdyncrm_marketingdynamiccontentmetadata |
| msdyncrm_marketingemail |
| msdyncrm_marketingemailactivity |
| msdyncrm_marketingemaildynamiccontentmetadata |
| msdyncrm_marketingemailtemplate |
| msdyncrm_marketingemailtest |
| msdyncrm_marketingemailtestattribute |
| msdyncrm_marketingemailtestsend |
| msdyncrm_marketingfieldsubmission |
| msdyncrm_marketingform |
| msdyncrm_marketingformactivity |
| msdyncrm_marketingformfield |
| msdyncrm_marketingformformwhitelistrule |
| msdyncrm_marketingformsubmission |
| msdyncrm_marketingformtemplate |
| msdyncrm_marketingformwhitelistrule |
| msdyncrm_marketingpage |
| msdyncrm_marketingpageconfiguration |
| msdyncrm_marketingpagetemplate |
| msdyncrm_matchingstrategy |
| msdyncrm_matchingstrategyattribute |
| msdyncrm_mktactivity |
| msdyncrm_networkpage |
| msdyncrm_personalizedpage |
| msdyncrm_phonecallactivity |
| msdyncrm_phonecallactivitymarketingtemplate |
| msdyncrm_portalsettings |
| msdyncrm_postingishts |
| msdyncrm_quicksendemail |
| msdyncrm_reaction |
| msdyncrm_recordupdateactivity |
| msdyncrm_redirecturl |
| msdyncrm_segment |
| msdyncrm_segmentactivity |
| msdyncrm_segmenttemplate |
| msdyncrm_socialpost |
| msdyncrm_socialpostingconfiguration |
| msdyncrm_socialpostingconsent |
| msdyncrm_sourceactivity |
| msdyncrm_splitteractivity |
| msdyncrm_tag |
| msdyncrm_taskactivity |
| msdyncrm_taskactivitymarketingtemplate |
| msdyncrm_triggeractivity |
| msdyncrm_uicconfig |
| msdyncrm_usergeoregion |
| msdyncrm_usersetting |
| msdyncrm_website |
| msgdpr_gdprconfiguration |
| msgdpr_gdprconsentchangerecord |

### Changelist-3 Updated (Privileges that changed in the current release compared to the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| ActionCard | Basic → Local | Basic → Local | Basic → Local | Basic → Local | Global → Local |
| Activity | Global → Local |  | Basic → Local |  |  |
| CustomerOpportunityRole | Global → Local | Basic → Local | Basic → Local | Global → Local | Global → Local |
| CustomerRelationship | Global → Local | Basic → Local | Basic → Local | Global → Local | Global → Local |
| DuplicateRule | Global → Local |  |  |  |  |
| EmailSignature | Global → Local | Basic → Local | Basic → Local |  |  |
| EmailTemplate | Global → Local | Basic → Local | Basic → Local |  |  |
| Feedback | Global → Local |  |  | Global → Local | Global → Local |
| GoalRollupQuery | Basic → Local |  |  |  |  |
| Import | Basic → Local | Basic → Local | Basic → Local | Basic → Local | Basic → Local |
| ImportFile | Basic → Local | Basic → Local | Basic → Local | Basic → Local | Basic → Local |
| ImportMap | Global → Local |  |  |  |  |
| Mailbox | Basic → Local | Basic → Local |  | Basic → Local |  |
| MailboxTrackingFolder | Basic → Local | Basic → Local | Basic → Local | Basic → Local |  |
| MailMergeTemplate | Basic → Local | Basic → Local | Basic → Local | Basic → Local | Basic → Local |
| Note | Global → Local | Basic → Local | Basic → Local |  |  |
| PostFollow | Global → Local |  | Basic → Local | Basic → Local |  |
| SharePointSite | Global → Local |  |  |  | Global → Local |
| SocialProfile | Global → Local | Global → Local | Basic → Local | Global → Local | Global → Local |
| SyncError | Basic → Local | Basic → Local | Basic → Local | Basic → Local | Basic → Local |
| WorkflowSession |  | Basic → Local | Basic → Local | Basic → Local | Basic → Local |

## Role: Marketing Professional (BU level) - Business

**Role identifier:** {6d63ebe3-cee8-e611-80d8-00155d4b205a}

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Local | Local | Local | Local | Local |
| ActionCard | Local | Local | Local | Local | Local |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Local | Local | Local | Local | Local |
| ApplicationFile | Global |  |  |  |  |
| AsyncOperation | Local | Local |  |  | Local |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Local |  |  |  | Local |
| Campaign | Local |  |  | Local | Local |
| ChannelPropertyGroup | Global |  |  | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Local | Local | Local | Local | Local |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Local | Local | Local | Local | Local |
| CustomerOpportunityRole | Local | Local | Local | Local | Local |
| CustomerRelationship | Local | Local | Local | Local | Local |
| Customization | Global |  |  |  |  |
| DocumentTemplate | Global |  |  |  |  |
| DuplicateRule | Local |  |  |  |  |
| EmailServerProfile | Global |  |  |  | Global |
| EmailSignature | Local | Local | Local |  |  |
| EmailTemplate | Local | Local | Local | Local |  |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| ExchangeSyncIdMapping | Basic | Basic | Basic |  |  |
| Feedback | Local |  |  | Local | Local |
| GoalRollupQuery | Local |  |  |  |  |
| HierarchyRule | Global |  |  |  |  |
| Import | Local | Local | Local | Local | Local |
| ImportFile | Local | Local | Local | Local | Local |
| ImportMap | Local | Local | Local | Local | Local |
| LanguageLocale | Global |  |  | Global | Global |
| Lead | Local | Local | Local | Local | Local |
| LeadToOpportunitySalesProcess | Global | Global | Global | Global | Global |
| License | Global |  |  |  |  |
| List | Local | Local | Local | Local | Local |
| Mailbox | Local | Local |  | Local |  |
| MailboxTrackingFolder | Local | Local | Local | Local |  |
| MailMergeTemplate | Local | Local | Local | Local | Local |
| MobileOfflineProfile | Global |  |  |  |  |
| msdyncrm_emailkeypoint | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Local |  |  |  |  |
| msdyncrm_gpt3log | Global |  |  |  |  |
| msdyncrm_setupdomain | Global |  |  |  |  |
| msdyncrm_textstyle | Global |  |  |  |  |
| msdynmkt_smsphonenumber |  | Global | Global |  |  |
| NewsArticle | Global |  |  |  |  |
| Note | Local | Local | Local | Local | Local |
| Opportunity | Local | Local | Local | Local | Local |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrgEmailTemplates |  |  | Global |  |  |
| PersonalDocumentTemplate | Basic | Basic | Basic | Basic | Basic |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Position | Global |  |  |  |  |
| Post | Global |  | Global | Global | Global |
| PostFollow | Local |  | Local | Local |  |
| Product | Global |  |  |  |  |
| Query | Global | Global | Global |  |  |
| RecommendedDocument | Global |  |  |  |  |
| Relationship | Global |  |  |  |  |
| RelationshipRole | Global |  |  |  |  |
| Role | Local |  |  |  |  |
| SavedQueryVisualizations | Global | Global | Global |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Local |  |  |  | Local |
| SocialProfile | Local | Local | Local | Local | Local |
| Subject | Global |  |  |  | Global |
| SyncError | Local | Local | Local | Local | Local |
| SystemApplicationMetadata | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| SystemUser |  |  |  |  | Global |
| Team | Global |  |  |  |  |
| TraceLog | Global |  | Global | Global | Global |
| TransactionCurrency | Global |  |  | Global | Global |
| User | Global |  |  | Local | Local |
| UserApplicationMetadata | Basic | Basic | Basic |  |  |
| UserEntityInstanceData | Basic | Basic | Basic |  |  |
| UserEntityUISettings | Basic | Basic | Basic |  |  |
| UserForm | Basic | Basic | Basic |  |  |
| UserQuery | Basic | Basic | Basic |  |  |
| UserQueryVisualizations | Basic | Basic | Basic |  |  |
| UserSettings | Global | Local | Local |  | Local |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Local | Local | Local | Global |
| WorkflowSession | Global | Local | Local | Local | Local |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in this release)

| **Table name** |
|---|
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |
| msdyncrm_segment |
| msgdpr_gdprconfiguration |

### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

No table privileges were updated for this role.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
