---
title: Permission changes in each release
description: Permission changes in each release track updates to out-of-the-box roles in Customer Insights - Journeys. Review the changelists and keep your custom roles in sync.
ms.date: 07/28/2026
ms.topic: article
author: vinayd
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Permission changes in each release

This article details permissions for the out-of-the-box roles in Customer Insights - Journeys. Whether you're an administrator configuring roles or a user looking to understand the access levels, these roles serve as a valuable reference.

> [!NOTE]
> The content and structure of this page have changed significantly since April 2026. If you used this page to keep custom roles aligned with out‑of‑the‑box roles, review the entire article to understand what has changed and how role updates are now documented.

## List of out-of-the-box roles

1. Event Administrator
1. Event Administrator (BU level)
1. Event Planner (BU level)
1. Lead Score Modeler
1. Lead Score Modeler (BU level)
1. Lead Score Viewer
1. Lead Score Viewer (BU level)
1. Marketing Manager - Business
1. Marketing Manager (BU level) - Business
1. Marketing Professional - Business
1. Marketing Professional (BU level) - Business

## How to use information in this page

If your organization uses custom roles based on out-of-the-box roles, with specific privileges added, removed, or changed to match your business needs, you need to keep those custom roles in sync as the product evolves. Out-of-the-box roles can change with each release when new capabilities are added or existing capabilities are updated. Review the [Release-wise changes to roles and privileges](#release-wise-changes-to-roles-and-privileges) section regularly and apply the documented changes to your custom roles.

Earlier versions of this article listed every privilege for each role. That format was difficult to maintain and made it hard to identify what changed between releases. Starting with the March 2026 release, this article uses a changelist format that documents only the differences from one release to the next. We're also now documenting privileges for all eight actions (previously, we documented only five actions: Read, Write, Create, Append, AppendTo, Delete).

Here's how the information is organized:

- **[June 2026 release (version 1.2.437.94)](#june-2026-release-version-1243794)**: Changelist of differences introduced in the June 2026 release.
- **[May 2026 release (version 1.1.65002.146)](#may-2026-release-version-1165002146)**: Changelist of differences introduced in the May 2026 release.
- **[April 2026 release (version 1.1.64196.86)](#april-2026-release-version-116419686)**: Changelist of differences introduced in the April 2026 release.
- **[March 2026 release (version 1.1.62960.43)](#march-2026-release-version-116296043)**: Changelist of differences introduced in the March 2026 release compared to the previously published documentation.
- **[Baseline (pre-March 2026)](role-permissions-baseline.md)**: The last published version of this page, documenting all 11 roles and their privileges for five actions. Use this section as a reference if you need to verify your custom roles against the full privilege set before the changelist format was adopted.

To keep your custom roles in sync, first align them with the documented baseline. Then, apply the permission changes introduced in each release, up to your current release, to bring your roles up to date. Afterward, review this page after every release to identify new changes that must be applied to remain in sync.

## How to check privileges for any role

For the most accurate and up-to-date privilege information, check roles directly in the application. Follow the steps in [Security roles and privileges for Dataverse](/power-platform/admin/security-roles-privileges) to find configured roles and their privileges.

Dataverse security roles combine an **action** (for example, Read or Write) with an **access scope** that defines how broadly that action applies across your organization.

These scopes are documented as **Basic**, **Local**, **Deep**, and **Global**. In the Power Platform admin center, the same concepts appear with the following labels:

- **User → Basic**: Access only to records the user owns or that are shared with them.
- **Business → Local**: Access to records owned by users in the same business unit.
- **Parent: Child Business Unit → Deep**: Access to records in the user's business unit and all subordinate business units.
- **Organization → Global**: Access to all records across the entire environment, regardless of business unit.

## Release-wise changes to roles and privileges

We'll update this section after each release to note changes, if any, to out-of-the-box roles and privileges.

## June 2026 release (version 1.2.437.94)

### Change summary

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

### Role: Event Administrator

**Role identifier**: a31a2242-bf8f-e611-80d7-00155d4b201d

#### Changelist 1 - Additions

This role doesn't add any tables.

#### Changelist 2 - Removed

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

#### Changelist 3 - Updated

This role doesn't update any table privileges.

### Role: Event Administrator (BU level)

**Role identifier**: 07d52deb-3b54-4203-b3cf-35efe4350f82

#### Changelist 1 - Additions

This role doesn't add any tables.

#### Changelist 2 - Removed

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

#### Changelist 3 - Updated

This role doesn't update any table privileges.

### Role: Event Planner (BU level)

**Role identifier**: 9d0bcbb3-75d8-4496-b2fb-62d0a9cb902f

#### Changelist 1 - Additions

This role doesn't add any tables.

#### Changelist 2 - Removed

| **Table name** |
|---|
| msdyncrm_customerinsightsinfo |
| msdyncrm_defaultmarketingsetting |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |

#### Changelist 3 - Updated

This role doesn't update any table privileges.

### Role: Lead Score Modeler

**Role identifier**: d1fd2176-cee8-e611-80d8-00155d4b205a

#### Changelist 1 - Additions

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 | Local | Local | Local | Local | Local |
| msdyncrm_leadscoremodel | Global | Global | Local | Global | Global |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |

#### Changelist 2 - Removed

No tables were removed from this role.

#### Changelist 3 - Updated

No table privileges were updated for this role.

### Role: Lead Score Viewer

**Role identifier**: 32e87eb4-c85c-e711-80fe-000d3a297db2

#### Changelist 1 - Additions

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

#### Changelist 2 - Removed

No tables were removed from this role.

#### Changelist 3 - updated

No table privileges were updated for this role.

### Role: Marketing Manager - Business

**Role identifier**: bf157a3a-cde8-e611-80d8-00155d4b205a

#### Changelist 1 - Additions

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_compliancesettings3 |  |  | Deep |  |  |
| msdynmkt_matchingstrategyattribute |  |  |  | Deep |  |

#### Changelist 2 - Removed

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

#### Changelist 3 - updated

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

### Role: Marketing Manager (BU level) - Business

**Role identifier**: dd84f17f-cde8-e611-80d8-00155d4b205a

#### Changelist 1 - Additions

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

#### Changelist 2 - removed

| **Table name** |
|---|
| msdyncrm_gwennolfeatureconfiguration |
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |
| msdyncrm_segment |
| msgdpr_gdprconfiguration |

#### Changelist 3 - updated

No table privileges were updated for this role.

### Role: Marketing Professional - Business

**Role identifier**: ce995e5a-cee8-e611-80d8-00155d4b205a

#### Changelist 1 - Additions

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_compliancesettings3 |  | Local | Local |  |  |

#### Changelist 2 - removed

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

#### Changelist 3 - updated

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

### Role: Marketing Professional (BU level) - Business

**Role identifier**: 6d63ebe3-cee8-e611-80d8-00155d4b205a

#### Changelist 1 - Additions

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

#### Changelist 2 - removed

| **Table name** |
|---|
| msdyncrm_leadtoopportunity |
| msdyncrm_marketingconfiguration |
| msdyncrm_segment |
| msgdpr_gdprconfiguration |

#### Changelist 3 - updated

No table privileges were updated for this role.

## May 2026 release (version 1.1.65002.146)

This month's release did not change any roles or privileges.

## April 2026 release (version 1.1.64196.86)

### Role-wise changes (versus the March 2026 release)

---

### Summary of changes

| Role | Tables Added | Privs Added | Tables Removed | Privs Removed | Tables Updated | Privs Updated | Change alert |
|---|---|---|---|---|---|---|---|
| Event Administrator | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Event Administrator (BU level) | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Event Planner (BU level) | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Modeler | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Modeler (BU level) | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Viewer | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Viewer (BU level) | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Marketing Manager - Business | 1 | 8 | 0 | 0 | 0 | 0 | ⚠ |
| Marketing Manager (BU level) - Business | 1 | 8 | 0 | 0 | 0 | 0 | ⚠ |
| Marketing Professional - Business | 1 | 8 | 0 | 0 | 0 | 0 | ⚠ |
| Marketing Professional (BU level) - Business | 1 | 8 | 0 | 0 | 0 | 0 | ⚠ |

---

### Role: Marketing Manager - Business

**Role identifier:** {bf157a3a-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Global | Global | Global | Global | Global | Global | Global | Global |

#### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

### Role: Marketing Manager (BU level) - Business

**Role identifier:** {dd84f17f-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Deep | Deep | Deep | Deep | Deep | Deep | Deep | Deep |

#### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

### Role: Marketing Professional - Business

**Role identifier:** {ce995e5a-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Global | Global | Global | Global | Global | Global | Global | Global |

#### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

### Role: Marketing Professional (BU level) - Business

**Role identifier:** {6d63ebe3-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Local | Local | Local | Local | Local | Local | Local | Local |

#### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

## March 2026 release (version 1.1.62960.43)

This is the first changenote published for this documentation and reflects a comparison against previously published learn page for roles and permissions. As a result, some entries may be marked as **Added** or **Removed** even when no functional change has occurred. An **Added** entry may indicate a permission that already existed but was previously undocumented. Similarly, a **Removed** entry may reflect a correction to earlier documentation rather than an actual removal of a permission.

### Role wise changes (versus previously published documentation)

---

### Table of contents

- [Role: Event Administrator](#role-event-administrator)
- [Role: Event Administrator (BU level)](#role-event-administrator-bu-level)
- [Role: Event Planner (BU level)](#role-event-planner-bu-level)
- [Role: Lead Score Modeler](#role-lead-score-modeler)
- [Role: Lead Score Modeler (BU level)](#role-lead-score-modeler-bu-level)
- [Role: Lead Score Viewer](#role-lead-score-viewer)
- [Role: Lead Score Viewer (BU level)](#role-lead-score-viewer-bu-level)
- [Role: Marketing Manager - Business](#role-marketing-manager---business)
- [Role: Marketing Manager (BU level) - Business](#role-marketing-manager-bu-level---business)
- [Role: Marketing Professional - Business](#role-marketing-professional---business)
- [Role: Marketing Professional (BU level) - Business](#role-marketing-professional-bu-level---business)

---

### Summary of changes

| Role | Tables Added | Privs Added | Tables Removed | Privs Removed | Tables Updated | Privs Updated | Change alert |
|---|---|---|---|---|---|---|---|
| Event Administrator | 5 | 25 | 0 | 0 | 1 | 1 | ⚠ |
| Event Administrator (BU level) | 5 | 25 | 0 | 0 | 1 | 1 | ⚠ |
| Event Planner (BU level) | 4 | 17 | 0 | 0 | 45 | 156 | ⚠ |
| Lead Score Modeler | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Modeler (BU level) | 2 | 6 | 6 | 6 | 6 | 24 | ⚠ |
| Lead Score Viewer | 0 | 0 | 0 | 0 | 0 | 0 |  |
| Lead Score Viewer (BU level) | 1 | 1 | 0 | 0 | 0 | 0 | ⚠ |
| Marketing Manager - Business | 13 | 40 | 0 | 0 | 24 | 57 | ⚠ |
| Marketing Manager (BU level) - Business | 13 | 40 | 0 | 0 | 8 | 14 | ⚠ |
| Marketing Professional - Business | 13 | 40 | 0 | 0 | 19 | 44 | ⚠ |
| Marketing Professional (BU level) - Business | 13 | 40 | 0 | 0 | 4 | 6 | ⚠ |

---

### Role: Event Administrator

**Role identifier:** {a31a2242-bf8f-e611-80d7-00155d4b201d}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 5 | 25 |
| Removed | 0 | 0 |
| Updated | 1 | 1 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Global | Global | Global | Global | Global |
| msevtmgt_eventregistrationsettings | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_integrationconfiguration | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_paymentprovider | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_powerpageswebsite | Organization | Organization | Organization | Organization | Organization |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Workflow |  |  |  |  | (added) → Organization |

---

### Role: Event Administrator (BU level)

**Role identifier:** {07d52deb-3b54-4203-b3cf-35efe4350f82}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 5 | 25 |
| Removed | 0 | 0 |
| Updated | 1 | 1 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventregistrationsettings | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_integrationconfiguration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_paymentprovider | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_powerpageswebsite | Deep | Deep | Deep | Deep | Deep |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Workflow |  |  |  |  | (added) → Organization |

---

### Role: Event Planner (BU level)

**Role identifier:** {9d0bcbb3-75d8-4496-b2fb-62d0a9cb902f}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 4 | 17 |
| Removed | 0 | 0 |
| Updated | 45 | 156 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Local | Local | Local | Local | Local |
| msevtmgt_integrationconfiguration | Local | Local | Local | Local | Local |
| msevtmgt_paymentprovider | Organization |  |  |  | Organization |
| msevtmgt_powerpageswebsite | Local | Local | Local | Local | Local |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AsyncOperation | Organization → Local |  |  |  |  |
| BusinessUnit | Organization → Local |  |  |  |  |
| User | Organization → Local |  |  |  | Organization → Local |
| Workflow |  |  |  |  | (added) → Organization |
| msdyncrm_defaultmarketingsetting | Organization → Deep |  |  |  |  |
| msdyncrm_file | Organization → Local | Organization → Local |  | Organization → Local | Organization → Local |
| msdynmkt_marketingfieldsubmission | Organization → Local |  |  |  |  |
| msdynmkt_marketingform | Organization → Local | Organization → Local | Organization → Local | Organization → Local | Organization → Local |
| msdynmkt_marketingformfield | Organization → Local |  |  |  |  |
| msdynmkt_marketingformsubmission | Organization → Local |  | Organization → Local | Organization → Local |  |
| msdynmkt_marketingformtemplate | Organization → Local |  |  |  | Organization → Local |
| msdynmkt_matchingstrategy | Organization → Local | Organization → Local | Organization → Local |  | Organization → Local |
| msdynmkt_matchingstrategyattribute | Organization → Local |  |  |  |  |
| msevtmgt_AttendeePass | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Building | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_CheckIn | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_EntityCounter | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Event | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_EventRegistration | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_EventTeamMember | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Hotel | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_HotelRoomAllocation | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_HotelRoomReservation | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Layout | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Room | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Session | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_SessionRegistration | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_SessionTrack | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Speaker | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_SponsorableArticle | Organization → Local |  | Organization → Local | Organization → Local | Organization → Local |
| msevtmgt_Sponsorship | Organization → Local |  | Organization → Local | Organization → Local | Global → Local |
| msevtmgt_Venue | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_customregistrationfield | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventadministration | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventcustomregistrationfield | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventpurchase | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventpurchaseattendee | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventpurchasepass | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_eventvendor | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_pass | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_registrationresponse | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_roomreservation | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_speakerengagement | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_waitlistitem | Global → Local |  | Global → Local | Global → Local | Global → Local |
| msevtmgt_websiteentityconfiguration | Global → Local | Global → Local | Global → Local | Global → Local | Global → Local |

---

### Role: Lead Score Modeler

**Role identifier:** {d1fd2176-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 0 | 0 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

_None_

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

_No changes._

---

### Role: Lead Score Modeler (BU level)

**Role identifier:** {3b30e84e-3ec6-4aa2-9417-b569f0d0284d}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 2 | 6 |
| Removed | 6 | 6 |
| Updated | 6 | 24 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_Localleadtoopportunity | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_featureconfiguration | Global |  |  |  |  |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AppModule | Global |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdyncrm_leadscoremodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entitygradedistribution |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entityscoredistribution |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entityscoringmodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_leadqualificationmodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |

---

### Role: Lead Score Viewer

**Role identifier:** {32e87eb4-c85c-e711-80fe-000d3a297db2}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 0 | 0 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

_None_

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

_No changes._

---

### Role: Lead Score Viewer (BU level)

**Role identifier:** {afc2cc8c-a26f-41c1-99a3-4510003a1878}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 1 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_featureconfiguration | Global |  |  |  |  |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

_No changes._

---

### Role: Marketing Manager - Business

**Role identifier:** {bf157a3a-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 24 | 57 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_browser | Global |  |  |  |  |
| msdynmkt_consentprovider | Global |  |  |  |  |
| msdynmkt_consentsubmitbutton | Global |  |  |  |  |
| msdynmkt_devicetype | Global |  |  |  |  |
| msdynmkt_emailclient | Global |  |  |  |  |
| msdynmkt_formsetting | Global | Global | Global | Global | Global |
| msdynmkt_formtargetaudience | Global | Global | Global | Global | Global |
| msdynmkt_operatingsystem | Global |  |  |  |  |
| msdynmkt_savedformfield | Global | Global | Global | Global |  |
| msdynmkt_segmentationcsvupload | Global | Global | Global | Global | Global |
| msevtmgt_eventregistrationcustomfield | Global | Global | Global | Global | Global |
| msevtmgt_integrationconfiguration | Global | Global | Global | Global | Global |
| msevtmgt_powerpageswebsite | Global | Global | Global | Global | Global |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| WorkflowSession |  |  |  |  | (added) → Local |
| msdyn_ChannelDefinition |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdyn_ConsumingApplication |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdyncrm_customerjourney |  |  | Local → Global |  |  |
| msdyncrm_file |  |  | Local → Global |  |  |
| msdyncrm_keyword |  |  | Local → Global |  |  |
| msdyncrm_video |  |  | Local → Global |  |  |
| msdynmkt_domain | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_entitygradedistribution |  |  | Local → Global |  |  |
| msdynmkt_entityscoredistribution |  |  | Local → Global |  |  |
| msdynmkt_entityscoringmodel |  |  | Local → Global |  |  |
| msdynmkt_experiment | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_frequencycap | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_gdprrequest | Deep → Global | Deep → Global | Deep → Global | Deep → Global |  |
| msdynmkt_journeysetting |  |  | Local → Global |  |  |
| msdynmkt_leadqualificationmodel |  |  | Local → Global |  |  |
| msdynmkt_marketingform |  |  |  |  | (added) → Global |
| msdynmkt_marketingformtemplate |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdynmkt_matchingstrategy |  |  |  | (added) → Global |  |
| msdynmkt_mobileapp | Deep → Global |  |  |  |  |
| msdynmkt_quiettimesetting | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_segment |  |  | Local → Global |  |  |
| msdynmkt_segmentdefinition | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_segmentexecution | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |

---

### Role: Marketing Manager (BU level) - Business

**Role identifier:** {dd84f17f-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 8 | 14 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_browser | Global |  |  |  |  |
| msdynmkt_consentprovider | Global |  |  |  |  |
| msdynmkt_consentsubmitbutton | Deep |  |  |  |  |
| msdynmkt_devicetype | Global |  |  |  |  |
| msdynmkt_emailclient | Global |  |  |  |  |
| msdynmkt_formsetting | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_formtargetaudience | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_operatingsystem | Global |  |  |  |  |
| msdynmkt_savedformfield | Deep | Deep | Deep | Deep |  |
| msdynmkt_segmentationcsvupload | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventregistrationcustomfield | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_integrationconfiguration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_powerpageswebsite | Deep | Deep | Deep | Deep | Deep |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| WorkflowSession |  |  |  |  | (added) → Deep |
| msdyn_ChannelDefinition |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdyn_ConsumingApplication |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdyncrm_gwennolfeatureconfiguration | Global → Deep |  |  |  |  |
| msdynmkt_featureconfiguration | Deep → Global |  |  |  |  |
| msdynmkt_marketingform |  |  |  |  | (added) → Deep |
| msdynmkt_marketingformtemplate |  | (added) → Deep | (added) → Deep | (added) → Deep |  |
| msdynmkt_matchingstrategy |  |  |  | (added) → Deep |  |

---

### Role: Marketing Professional - Business

**Role identifier:** {ce995e5a-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 19 | 44 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_browser | Global |  |  |  |  |
| msdynmkt_consentprovider | Global |  |  |  |  |
| msdynmkt_consentsubmitbutton | Global |  |  |  |  |
| msdynmkt_devicetype | Global |  |  |  |  |
| msdynmkt_emailclient | Global |  |  |  |  |
| msdynmkt_formsetting | Global | Global | Global | Global | Global |
| msdynmkt_formtargetaudience | Global | Global | Global | Global | Global |
| msdynmkt_operatingsystem | Global |  |  |  |  |
| msdynmkt_savedformfield | Global | Global | Global | Global |  |
| msdynmkt_segmentationcsvupload | Global | Global | Global | Global | Global |
| msevtmgt_eventregistrationcustomfield | Global | Global | Basic | Global | Global |
| msevtmgt_integrationconfiguration | Global | Global | Basic | Global | Global |
| msevtmgt_powerpageswebsite | Global | Global | Basic | Global | Global |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| WorkflowSession |  |  |  |  | (added) → Basic |
| msdyncrm_customerjourney |  |  | Basic → Global |  |  |
| msdyncrm_video |  |  | Local → Global |  |  |
| msdynmkt_brandprofile |  |  |  | (added) → Global | (added) → Global |
| msdynmkt_brandsender |  |  |  |  | (added) → Global |
| msdynmkt_conversioneventdefinition |  | Local → Global | Local → Global | Local → Global |  |
| msdynmkt_domain | Local → Global | Local → Global | Local → Global | Local → Global | Local → Global |
| msdynmkt_eventmetadata |  | Local → Global | Local → Global |  |  |
| msdynmkt_experiment | Local → Global | Local → Global | Local → Global | Local → Global | Local → Global |
| msdynmkt_frequencycap | Local → Global |  |  |  |  |
| msdynmkt_gdprrequest | Local → Global | Local → Global | Local → Global | Local → Global |  |
| msdynmkt_journey |  |  | Local → Global |  |  |
| msdynmkt_journeytemplate |  |  | Local → Global |  |  |
| msdynmkt_marketingform |  |  |  |  | (added) → Global |
| msdynmkt_marketingformtemplate |  | (added) → Global | (added) → Global | (added) → Global |  |
| msdynmkt_mobileapp | Deep → Global |  |  |  |  |
| msdynmkt_quiettimesetting | Local → Global |  |  |  |  |
| msdynmkt_segmentdefinition | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |
| msdynmkt_segmentexecution | Deep → Global | Deep → Global | Deep → Global | Deep → Global | Deep → Global |

---

### Role: Marketing Professional (BU level) - Business

**Role identifier:** {6d63ebe3-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 4 | 6 |

#### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_browser | Global |  |  |  |  |
| msdynmkt_consentprovider | Global |  |  |  |  |
| msdynmkt_consentsubmitbutton | Local |  |  |  |  |
| msdynmkt_devicetype | Global |  |  |  |  |
| msdynmkt_emailclient | Global |  |  |  |  |
| msdynmkt_formsetting | Local | Local | Local | Local | Local |
| msdynmkt_formtargetaudience | Local | Local | Local | Local | Local |
| msdynmkt_operatingsystem | Global |  |  |  |  |
| msdynmkt_savedformfield | Local | Local | Local | Local |  |
| msdynmkt_segmentationcsvupload | Local | Local | Local | Local | Local |
| msevtmgt_eventregistrationcustomfield | Local | Local | Local | Local | Local |
| msevtmgt_integrationconfiguration | Local | Local | Local | Local | Local |
| msevtmgt_powerpageswebsite | Local | Local | Local | Local | Local |

#### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

#### Changelist-3 Updated (Privileges that have changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| WorkflowSession |  |  |  |  | (added) → Local |
| msdynmkt_featureconfiguration | Local → Global |  |  |  |  |
| msdynmkt_marketingform |  |  |  |  | (added) → Local |
| msdynmkt_marketingformtemplate |  | (added) → Local | (added) → Local | (added) → Local |  |

[!INCLUDE [footer-include](./includes/footer-banner.md)]