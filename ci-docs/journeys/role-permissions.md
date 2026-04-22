---
title: Permissions for out-of-the-box roles
description: How to manage permissions for out-of-the-box and custom roles in Dynamics 365 Customer Insights - Journeys.
ms.date: 04/21/2026
ms.topic: article
author: vinayd
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Permissions for out-of-the-box roles

This article details permissions for the out-of-the-box roles in Customer Insights - Journeys. Whether you're an administrator configuring roles or a user looking to understand the access levels, these roles serve as a valuable reference.

> [!NOTE]
> The content and structure of this page have changed significantly since April 2026. If you used this page to keep custom roles aligned with out‑of‑the‑box roles, review the entire article to understand what has changed and how role updates are now documented

### List of out-of-the-box roles
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

### How to use information in this page

If your organization uses custom roles based on out-of-the-box roles — with specific privileges added, removed, or changed to match your business needs — you need to keep those custom roles in sync as the product evolves. Out-of-the-box roles can change with each release when new capabilities are added or existing capabilities are updated. Review the #changes-to-roles-and-privileges section on a regular basis and apply the documented changes to your custom roles.

Earlier versions of this article listed every privilege for each role. That format was difficult to maintain and made it hard to identify what changed between releases. Starting with the March 2026 release, this article uses a changelist format that documents only the differences from one release to the next. We are also now documenting privileges for all 8 actions (previously we documented only 5 actions Read, Write, Create, Append, AppendTo, Delete)

Here is how the information is organized:

- **[April 2026 release (version 1.1.64196.86)](#april-2026-release-version-116419686)** — Changelist of differences introduced in the April 2026 release.
- **[March 2026 release (version 1.1.62960.43)](#march-2026-release-version-1116296043)** — Changelist of differences introduced in the March 2026 release compared to the previously published documentation.
- **[Baseline (pre-March 2026)](#baseline-pre-march-2026)** — The last published version of this page, documenting all 11 roles and their privileges for five actions. Use this section as a reference if you need to verify your custom roles against the full privilege set before the changelist format was adopted.

To keep your custom roles in sync, first align them with the documented baseline. Then, apply the permission changes introduced in each release—up to your current release—to bring your roles up to date. Afterward, review this page after every release to identify new changes that must be applied to remain in sync.


### How to check privileges for any role           
For the most accurate and up-to-date privilege information, check roles directly in the application. Follow the steps in [Security roles and privileges for Dataverse](https://learn.microsoft.com/power-platform/admin/security-roles-privileges) to find configured roles and their privileges.

Dataverse security roles combine an **action** (for example, Read or Write) with an **access scope** that defines how broadly that action applies across your organization.

These scopes are documented as **Basic**, **Local**, **Deep**, and **Global**. In the Power Platform admin center UI, the same concepts appear with the following labels:

- **User → Basic**. Access only to records the user owns or that are shared with them.
- **Business → Local**. Access to records owned by users in the same business unit.
- **Parent: Child Business Unit → Deep**. Access to records in the user's business unit and all subordinate business units.
- **Organization → Global**. Access to all records across the entire environment, regardless of business unit.


# Release-wise changes to roles and privileges

We will update this section after each release to note changes, if any, to out-of-the-box roles and privileges. 

## April 2026 release (version 1.1.64196.86)

### Role wise changes (vs March 2026 release)

---

### Summary of Changes

| Role | Tables Added | Privs Added | Tables Removed | Privs Removed | Tables Updated | Privs Updated | |
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

This is the first changenote published for this documentation and reflects a comparison against previously published learn page for roles and permissions . As a result, **some entries may be marked as Added or Removed even when no functional change has occurred**. An Added entry may indicate a permission that already existed but was previously undocumented. Similarly, a Removed entry may reflect a correction to earlier documentation rather than an actual removal of a permission.

### Role wise changes (vs previously published documentation)

---

### Table of Contents

- [Role: Event Administrator](#role-event-administrator)
- [Role: Event Administrator (BU level)](#role-event-administrator-bu-level)
- [Role: Event Planner (BU level)](#role-event-planner-bu-level)
- [Role: Lead Score Modeler](#role-lead-score-modeler)
- [Role: Lead Score Modeler (BU level)](#role-lead-score-modeler-bu-level)
- [Role: Lead Score Viewer](#role-lead-score-viewer)
- [Role: Lead Score Viewer (BU level)](#role-lead-score-viewer-bu-level)
- [Role: Marketing Manager - Business](#role-marketing-manager-business)
- [Role: Marketing Manager (BU level) - Business](#role-marketing-manager-bu-level-business)
- [Role: Marketing Professional - Business](#role-marketing-professional-business)
- [Role: Marketing Professional (BU level) - Business](#role-marketing-professional-bu-level-business)

---
### Summary of Changes

| Role | Tables Added | Privs Added | Tables Removed | Privs Removed | Tables Updated | Privs Updated | |
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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

#### Changelist-1 Added (Tables and privileges that exist in the current release but were not previously documented)

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

---


## Baseline pre-March 2026
>[!NOTE]
> This section doesn’t reflect the current roles or their privileges. It preserves the last published version of this page, which documented 11 roles and their privileges across five actions. Use it as a historical reference to validate custom roles against the complete privilege set **prior to the adoption of the changelist format**.
>
## Role: Event Administrator

**Role identifier**: a31a2242-bf8f-e611-80d7-00155d4b201d

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| adx_entityform | Global |   |   |   |   |
| Adx_website | Global |   |   |   |   |
| Adx_websitebinding | Global |   |   |   |   |
| AppModule | Global |   |   |   |   |
| AsyncOperation | Global |   |   |   |   |
| Attribute | Global |   |   |   |   |
| AttributeMap | Global |   |   |   |   |
| BusinessUnit | Global |   |   |   |   |
| Contact | Basic | Basic | Basic | Basic | Basic |
| Customization | Global |   |   |   |   |
| Entity | Global |   |   |   |   |
| EntityKey | Global |   |   |   |   |
| EntityMap | Global |   |   |   |   |
| msdyn_PostConfig | Global |   |   |   |   |
| msdyn_tour | Global |   |   |   |   |
| msdyncrm_customerinsightsinfo | Basic |   |   |   |   |
| msdyncrm_defaultmarketingsetting | Global |   |   |   |   |
| msdyncrm_digitalassetsconfiguration | Global |   |   |   |   |
| msdyncrm_featureconfiguration | Global |   |   |   |   |
| msdyncrm_file | Global | Global | Local | Global | Global |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_marketingconfiguration | Global |   |   |   |   |
| msdyncrm_setupdomain | Global | Global | Global | Global | Global |
| msdynmkt_domain | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_marketingfieldsubmission | Global |   |   |   |   |
| msdynmkt_marketingform | Global | Global | Global | Global | Global |
| msdynmkt_marketingformfield | Global |   |   |   |   |
| msdynmkt_marketingformsubmission | Global |   | Global | Global |   |
| msdynmkt_marketingformtemplate | Global |   |   |   | Global |
| msdynmkt_matchingstrategy | Global | Global | Global |   | Global |
| msdynmkt_matchingstrategyattribute | Global |   |   |   |   |
| msdynmkt_trackingcontext | Global |   |   |   |   |
| msdynmkt_virtualdomain | Global |   |   |   |   |
| msevtmgt_AttendeePass | Global | Global | Global | Global | Global |
| msevtmgt_authenticationsettings | Global |   |   |   |   |
| msevtmgt_bpf_9623d46752ae497989f62ac0d11dad99 | Global | Global | Global | Global | Global |
| msevtmgt_Building | Global | Global | Global | Global | Global |
| msevtmgt_CheckIn | Global | Global | Global | Global | Global |
| msevtmgt_customregistrationfield | Global | Global | Global | Global | Global |
| msevtmgt_EntityCounter | Global | Global | Global | Global | Global |
| msevtmgt_Event | Global | Global | Global | Global | Global |
| msevtmgt_eventadministration | Global | Global | Global | Global | Global |
| msevtmgt_eventcustomregistrationfield | Global | Global | Global | Global | Global |
| msevtmgt_eventmanagementconfiguration | Global |   |   |   |   |
| msevtmgt_eventpurchase | Global | Global | Global | Global | Global |
| msevtmgt_eventpurchaseattendee | Global | Global | Global | Global | Global |
| msevtmgt_eventpurchasepass | Global | Global | Global | Global | Global |
| msevtmgt_EventRegistration | Global | Global | Global | Global | Global |
| msevtmgt_EventTeamMember | Global | Global | Global | Global | Global |
| msevtmgt_eventvendor | Global | Global | Global | Global | Global |
| msevtmgt_file | Global | Global | Global | Global | Global |
| msevtmgt_Hotel | Global | Global | Global | Global | Global |
| msevtmgt_HotelRoomAllocation | Global | Global | Global | Global | Global |
| msevtmgt_HotelRoomReservation | Global | Global | Global | Global | Global |
| msevtmgt_Layout | Global | Global | Global | Global | Global |
| msevtmgt_pass | Global | Global | Global | Global | Global |
| msevtmgt_registrationresponse | Global | Global | Global | Global | Global |
| msevtmgt_Room | Global | Global | Global | Global | Global |
| msevtmgt_roomreservation | Global | Global | Global | Global | Global |
| msevtmgt_Session | Global | Global | Global | Global | Global |
| msevtmgt_SessionRegistration | Global | Global | Global | Global | Global |
| msevtmgt_SessionTrack | Global | Global | Global | Global | Global |
| msevtmgt_Speaker | Global | Global | Global | Global | Global |
| msevtmgt_speakerengagement | Global | Global | Global | Global | Global |
| msevtmgt_SponsorableArticle | Global | Global | Global | Global | Global |
| msevtmgt_Sponsorship | Global | Global | Global | Global | Global |
| msevtmgt_Venue | Global | Global | Global | Global | Global |
| msevtmgt_waitlistitem | Global | Global | Global | Global | Global |
| msevtmgt_webapplication | Global | Global | Global | Global | Global |
| msevtmgt_webinarconfiguration | Global | Global | Global | Global | Global |
| msevtmgt_webinarconsent | Global | Global | Global | Global | Global |
| msevtmgt_WebinarProvider | Global | Global |   | Global | Global |
| msevtmgt_WebinarType | Global |   |   | Global | Global |
| msevtmgt_websiteentityconfiguration | Global | Global | Global | Global | Global |
| OptionSet | Global |   |   |   |   |
| Organization | Global |   |   |   |   |
| PluginAssembly | Global |   |   |   |   |
| PluginType | Global |   |   |   |   |
| Query | Global |   |   |   |   |
| Relationship | Global |   |   |   |   |
| Role | Global |   |   |   |   |
| SdkMessage | Global |   |   |   |   |
| SdkMessageProcessingStep | Global |   |   |   |   |
| SdkMessageProcessingStepImage | Global |   |   |   |   |
| SharePointData | Global | Global | Global |   |   |
| SharePointDocument | Global |   |   |   |   |
| Solution | Global |   |   |   |   |
| SystemForm | Global |   |   |   |   |
| User | Global |   |   |   | Global |
| UserEntityUISettings | Basic | Basic | Basic |   |   |
| UserSettings | Global |   |   |   |   |
| WebResource | Global |   |   |   |   |
| Workflow | Global | Basic | Basic | Basic |   |

## Role: Event Administrator (BU level)

**Role identifier**: 07d52deb-3b54-4203-b3cf-35efe4350f82

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| adx_entityform | Global |  |  |  |  |
| Adx_website | Global |  |  |  |  |
| Adx_websitebinding | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Deep |  |  |  |  |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Deep |  |  |  |  |
| Contact | Basic | Basic | Basic | Basic | Basic |
| Customization | Global |  |  |  |  |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_tour | Global |  |  |  |  |
| msdyncrm_customerinsightsinfo | Basic |  |  |  |  |
| msdyncrm_defaultmarketingsetting | Deep |  |  |  |  |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Global |  |  |  |  |
| msdyncrm_file | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_setupdomain | Global | Global | Global | Global | Global |
| msdynmkt_domain | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_marketingfieldsubmission | Deep |  |  |  |  |
| msdynmkt_marketingform | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_marketingformfield | Deep |  |  |  |  |
| msdynmkt_marketingformsubmission | Deep |  | Deep | Deep |  |
| msdynmkt_marketingformtemplate | Deep |  |  |  | Deep |
| msdynmkt_matchingstrategy | Deep | Deep | Deep |  | Deep |
| msdynmkt_matchingstrategyattribute | Deep |  |  |  |  |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msevtmgt_AttendeePass | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_authenticationsettings | Global |  |  |  |  |
| msevtmgt_bpf_9623d46752ae497989f62ac0d11dad99 | Global | Global | Global | Global | Global |
| msevtmgt_Building | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_CheckIn | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_customregistrationfield | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_EntityCounter | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Event | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventadministration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventcustomregistrationfield | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventmanagementconfiguration | Global |  |  |  |  |
| msevtmgt_eventpurchase | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventpurchaseattendee | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventpurchasepass | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_EventRegistration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_EventTeamMember | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventvendor | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_file | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Hotel | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_HotelRoomAllocation | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_HotelRoomReservation | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Layout | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_pass | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_registrationresponse | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Room | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_roomreservation | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Session | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_SessionRegistration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_SessionTrack | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Speaker | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_speakerengagement | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_SponsorableArticle | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Sponsorship | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_Venue | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_waitlistitem | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_webapplication | Global | Global | Global | Global | Global |
| msevtmgt_webinarconfiguration | Global | Global | Global | Global | Global |
| msevtmgt_webinarconsent | Global | Global | Global | Global | Global |
| msevtmgt_WebinarProvider | Global | Global |  | Global | Global |
| msevtmgt_WebinarType | Global |  |  | Global | Global |
| msevtmgt_websiteentityconfiguration | Deep | Deep | Deep | Deep | Deep |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Query | Global |  |  |  |  |
| Relationship | Global |  |  |  |  |
| Role | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| Solution | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| User | Deep |  |  |  | Deep |
| UserEntityUISettings | Basic | Basic | Basic |  |  |
| UserSettings | Global |  |  |  |  |
| WebResource | Global |  |  |  |  |
| Workflow | Global | Basic | Basic | Basic |  |

## Role: Event Planner (BU level)

**Role identifier**: 9d0bcbb3-75d8-4496-b2fb-62d0a9cb902f

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| adx_entityform | Global |  |  |  |  |
| Adx_website | Global |  |  |  |  |
| Adx_websitebinding | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Global |  |  |  |  |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Global |  |  |  |  |
| Contact | Basic | Basic | Basic | Basic | Basic |
| Customization | Global |  |  |  |  |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_tour | Global |  |  |  |  |
| msdyncrm_customerinsightsinfo | Basic |  |  |  |  |
| msdyncrm_defaultmarketingsetting | Global |  |  |  |  |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Global |  |  |  |  |
| msdyncrm_file | Global | Global | Local | Global | Global |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_setupdomain |  | Global |  |  |  |
| msdynmkt_domain | Local | Local | Local | Local | Local |
| msdynmkt_marketingfieldsubmission | Global |  |  |  |  |
| msdynmkt_marketingform | Global | Global | Global | Global | Global |
| msdynmkt_marketingformfield | Global |  |  |  |  |
| msdynmkt_marketingformsubmission | Global |  | Global | Global |  |
| msdynmkt_marketingformtemplate | Global |  |  |  | Global |
| msdynmkt_matchingstrategy | Global | Global | Global |  | Global |
| msdynmkt_matchingstrategyattribute | Global |  |  |  |  |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msevtmgt_AttendeePass | Global | Basic | Global | Global | Global |
| msevtmgt_authenticationsettings | Global |  |  |  |  |
| msevtmgt_bpf_9623d46752ae497989f62ac0d11dad99 | Global | Global | Global | Global | Global |
| msevtmgt_Building | Global | Basic | Global | Global | Global |
| msevtmgt_CheckIn | Global | Basic | Global | Global | Global |
| msevtmgt_customregistrationfield | Global | Basic | Global | Global | Global |
| msevtmgt_EntityCounter | Global | Basic | Global | Global | Global |
| msevtmgt_Event | Global | Basic | Global | Global | Global |
| msevtmgt_eventadministration | Global | Basic | Global | Global | Global |
| msevtmgt_eventcustomregistrationfield | Global | Basic | Global | Global | Global |
| msevtmgt_eventpurchase | Global | Basic | Global | Global | Global |
| msevtmgt_eventpurchaseattendee | Global | Basic | Global | Global | Global |
| msevtmgt_eventpurchasepass | Global | Basic | Global | Global | Global |
| msevtmgt_EventRegistration | Global | Basic | Global | Global | Global |
| msevtmgt_EventTeamMember | Global | Basic | Global | Global | Global |
| msevtmgt_eventvendor | Global | Basic | Global | Global | Global |
| msevtmgt_Hotel | Global | Basic | Global | Global | Global |
| msevtmgt_HotelRoomAllocation | Global | Basic | Global | Global | Global |
| msevtmgt_HotelRoomReservation | Global | Basic | Global | Global | Global |
| msevtmgt_Layout | Global | Basic | Global | Global | Global |
| msevtmgt_pass | Global | Basic | Global | Global | Global |
| msevtmgt_registrationresponse | Global | Basic | Global | Global | Global |
| msevtmgt_Room | Global | Basic | Global | Global | Global |
| msevtmgt_roomreservation | Global | Basic | Global | Global | Global |
| msevtmgt_Session | Global | Basic | Global | Global | Global |
| msevtmgt_SessionRegistration | Global | Basic | Global | Global | Global |
| msevtmgt_SessionTrack | Global | Basic | Global | Global | Global |
| msevtmgt_Speaker | Global | Basic | Global | Global | Global |
| msevtmgt_speakerengagement | Global | Basic | Global | Global | Global |
| msevtmgt_SponsorableArticle | Global | Basic | Global | Global | Global |
| msevtmgt_Sponsorship | Global | Basic | Global | Global | Global |
| msevtmgt_Venue | Global | Basic | Global | Global | Global |
| msevtmgt_waitlistitem | Global | Basic | Global | Global | Global |
| msevtmgt_webinarconfiguration | Global |  |  |  |  |
| msevtmgt_webinarconsent | Global |  |  |  |  |
| msevtmgt_WebinarProvider | Global |  |  | Global | Global |
| msevtmgt_WebinarType | Global |  |  | Global | Global |
| msevtmgt_websiteentityconfiguration | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Query | Global |  |  |  |  |
| Relationship | Global |  |  |  |  |
| Role | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| Solution | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| User | Global |  |  |  | Global |
| UserEntityUISettings | Basic | Basic | Basic |  |  |
| UserSettings | Global |  |  |  |  |
| WebResource | Global |  |  |  |  |
| Workflow | Global | Basic | Basic | Basic |  |

## Role: Lead Score Modeler

**Role identifier**: d1fd2176-cee8-e611-80d8-00155d4b205a

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 | Local | Local | Local | Local | Local |
| msdyncrm_leadscoremodel | Global | Global | Local | Global | Global |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdynmkt_entitygradedistribution | Global | Global | Local | Global | Global |
| msdynmkt_entityscoredistribution | Global | Global | Local | Global | Global |
| msdynmkt_entityscoringmodel | Global | Global | Local | Global | Global |
| msdynmkt_leadqualificationmodel | Global | Global | Local | Global | Global |
| SharePointData | Global | Global | Global |   |   |
| SharePointDocument | Global |   |   |   |   |

## Role: Lead Score Modeler (BU level)

**Role identifier**: 3b30e84e-3ec6-4aa2-9417-b569f0d0284d

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AppModule | Global |   |   |   |   |
| msdyncrm_leadscore_v2 | Deep |   |   |   |   |
| msdyncrm_leadscoremodel | Deep |   |   |   |   |
| msdynmkt_entitygradedistribution | Deep |   |   |   |   |
| msdynmkt_entityscoredistribution | Deep |   |   |   |   |
| msdynmkt_entityscoringmodel | Deep |   |   |   |   |
| msdynmkt_leadqualificationmodel | Deep |   |   |   |   |
| PluginAssembly | Global |   |   |   |   |
| PluginType | Global |   |   |   |   |
| SdkMessage | Global |   |   |   |   |
| SdkMessageProcessingStep | Global |   |   |   |   |
| SdkMessageProcessingStepImage | Global |   |   |   |   |
| SharePointData | Global | Global | Global |   |   |
| SharePointDocument | Global |   |   |   |   |

## Role: Lead Score Viewer

**Role identifier**: 32e87eb4-c85c-e711-80fe-000d3a297db2

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AppModule | Global |   |   |   |   |
| msdyncrm_leadscore_v2 | Local |   |   |   |   |
| msdyncrm_leadscoremodel | Local |   |   |   |   |
| msdynmkt_entitygradedistribution | Local |   |   |   |   |
| msdynmkt_entityscoredistribution | Local |   |   |   |   |
| msdynmkt_entityscoringmodel | Local |   |   |   |   |
| msdynmkt_leadqualificationmodel | Local |   |   |   |   |
| PluginAssembly | Global |   |   |   |   |
| PluginType | Global |   |   |   |   |
| SdkMessage | Global |   |   |   |   |
| SdkMessageProcessingStep | Global |   |   |   |   |
| SdkMessageProcessingStepImage | Global |   |   |   |   |
| SharePointData | Global | Global | Global |   |   |
| SharePointDocument | Global |   |   |   |   |

## Role: Lead Score Viewer (BU level)

**Role identifier**: afc2cc8c-a26f-41c1-99a3-4510003a1878

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AppModule | Global |  |  |  |  |
| msdyncrm_leadscore_v2 | Deep |  |  |  |  |
| msdyncrm_leadscoremodel | Deep |  |  |  |  |
| msdynmkt_entitygradedistribution | Deep |  |  |  |  |
| msdynmkt_entityscoredistribution | Deep |  |  |  |  |
| msdynmkt_entityscoringmodel | Deep |  |  |  |  |
| msdynmkt_leadqualificationmodel | Deep |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |

## Role: Marketing Manager - Business

**Role identifier**: bf157a3a-cde8-e611-80d8-00155d4b205a

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Global | Global | Local | Global | Global |
| ActionCard | Basic | Basic | Basic | Basic | Global |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Global | Local | Local | Local | Local |
| Adx_pagetemplate | Global | Global | Local | Global | Global |
| adx_portallanguage | Global | Global | Local | Global | Global |
| Adx_publishingstate | Global | Global | Global | Global | Global |
| Adx_webpage | Global | Global | Local | Global | Global |
| Adx_website | Global | Global | Local | Global | Global |
| Adx_websiteaccess | Global | Global | Local | Global | Global |
| Adx_websitebinding | Global | Global | Global | Global | Global |
| adx_websitelanguage | Global | Global | Local | Global | Global |
| adx_webtemplate | Global | Global | Global | Global | Global |
| AppConfigMaster | Global |  |  |  |  |
| ApplicationFile | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Local | Local |  |  | Local |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Global |  |  |  | Global |
| Campaign | Global |  |  | Local | Local |
| Catalog | Global |  |  |  |  |
| CatalogAssignment | Global |  |  |  |  |
| ChannelPropertyGroup | Global | Global | Global | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Global | Global | Local | Global | Global |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Global | Global | Local | Global | Global |
| CustomAPI | Global |  |  |  |  |
| CustomerOpportunityRole | Global | Local | Local | Global | Global |
| CustomerRelationship | Global | Local | Local | Global | Global |
| Customization | Global |  |  |  |  |
| DocumentTemplate | Global |  |  |  |  |
| DuplicateRule | Global | Local | Local | Local | Local |
| EmailServerProfile | Global |  |  |  | Global |
| EmailSignature | Global | Global | Local |  |  |
| EmailTemplate | Global | Global | Local | Deep | Global |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| EnvironmentVariableDefinition | Local |  |  |  |  |
| EnvironmentVariableValue | Global |  |  |  |  |
| ExchangeSyncIdMapping | Basic | Basic | Basic |  |  |
| Feedback | Global |  |  | Global | Global |
| FieldSecurityProfile | Global |  |  |  |  |
| GoalRollupQuery | Basic | Basic | Basic | Basic | Basic |
| HierarchyRule | Global |  |  |  |  |
| Import | Local | Local | Local | Local | Local |
| ImportFile | Local | Local | Local | Local | Local |
| ImportMap | Global | Local | Local | Local | Local |
| LanguageLocale | Global |  |  | Global | Global |
| Lead | Global | Global | Local | Global | Global |
| LeadToOpportunitySalesProcess | Global | Global | Global | Global | Global |
| License | Global |  |  |  |  |
| List | Global | Deep | Local | Deep | Deep |
| Mailbox | Basic | Basic |  | Basic |  |
| MailboxTrackingFolder | Basic | Basic | Basic | Basic |  |
| MailMergeTemplate | Basic | Basic | Basic | Basic | Basic |
| MobileOfflineProfile | Global |  |  |  |  |
| msdyn_ChannelDefinition | Global |  |  |  | Global |
| msdyn_channeldefinitionconsent | Global | Global | Global | Global |  |
| msdyn_ChannelDefinitionLocale | Global |  |  |  |  |
| msdyn_ChannelInstance | Global | Global | Global | Global | Global |
| msdyn_ChannelInstanceAccount | Global | Global | Global | Global | Global |
| msdyn_ChannelMessagePart | Global |  |  |  |  |
| msdyn_ConsumingApplication | Global |  |  |  | Global |
| msdyn_dataanalyticsreport_mkt | Global |  |  |  |  |
| msdyn_occommunicationprovidersetting | Deep | Deep | Deep | Deep | Deep |
| msdyn_ocphonenumber | Deep | Deep | Deep | Deep | Deep |
| msdyn_odatav4ds | Global | Global |  | Global | Global |
| msdyn_PostAlbum | Global | Basic | Basic | Basic | Basic |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_PostRuleConfig | Global |  |  |  |  |
| msdyn_wallsavedquery | Global |  |  |  |  |
| msdyn_wallsavedqueryusersettings | Basic | Basic | Basic | Basic | Basic |
| msdynci_alternatekey | Global |  |  |  |  |
| msdynci_customerprofile | Global |  |  |  |  |
| msdyncrm_appointmentactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_appointmentactivitymarketingtemplate | Global | Global | Local | Global | Global |
| msdyncrm_cdnconfiguration | Global |  |  |  |  |
| msdyncrm_cdsaconnectorconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_contentblock | Global | Global | Global | Global | Global |
| msdyncrm_contentsettings | Global | Global | Local | Global | Global |
| msdyncrm_createleadactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerinsightsinfo | Global | Global | Local | Global | Global |
| msdyncrm_customerjourney | Global | Global | Local | Global | Global |
| msdyncrm_customerjourneycustomchannelactivity | Global | Global | Local | Global | Global |
| msdyncrm_customerjourneyiteration | Global | Global | Local | Global | Global |
| msdyncrm_customerjourneyruntimestate | Global | Global | Local | Global | Global |
| msdyncrm_customerjourneytemplate | Global | Global | Local | Global | Global |
| msdyncrm_customerjourneyworkflowlink | Global | Global | Local | Global | Global |
| msdyncrm_defaultmarketingsetting | Global | Global | Local | Global | Global |
| msdyncrm_delaydatetimeactivity | Global | Global | Global |  |  |
| msdyncrm_delaydurationactivity | Global | Global | Global |  |  |
| msdyncrm_deprecatedcustomtileactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedeventactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedformsprosurveyactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedpageactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_designerfeatureavailability | Global | Global | Local | Global | Global |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_emailkeypoint | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_file | Global | Global | Local | Global | Global |
| msdyncrm_formpage | Global | Global | Local | Global | Global |
| msdyncrm_formpagetemplate | Global | Global | Local | Global | Global |
| msdyncrm_geopin | Global | Global | Local | Global | Global |
| msdyncrm_gpt3log | Global |  |  |  |  |
| msdyncrm_gwennolfeatureconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_gwennolspamscoreactivity | Deep |  |  |  |  |
| msdyncrm_gwennolspamscorerequest | Global |  | Global |  |  |
| msdyncrm_keyword | Global | Global | Local | Global | Global |
| msdyncrm_launchworkflowactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_leadscoremodel | Global | Global | Local | Global | Global |
| msdyncrm_leadscoringconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_linkedincampaignactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_listform | Global | Global | Local | Global | Global |
| msdyncrm_liveentitydependency | Global | Global | Global | Global | Global |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_marketingdynamiccontentmetadata | Global | Global | Local | Global | Global |
| msdyncrm_marketingemail | Global | Global | Local | Global | Global |
| msdyncrm_marketingemailactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemaildynamiccontentmetadata | Global | Global | Local | Global | Global |
| msdyncrm_marketingemailtemplate | Global | Global | Local | Global | Global |
| msdyncrm_marketingemailtest | Global |  |  | Global | Global |
| msdyncrm_marketingemailtestattribute | Global |  |  | Global | Global |
| msdyncrm_marketingemailtestsend | Global | Global | Local | Global | Global |
| msdyncrm_marketingfieldsubmission | Global | Global | Local | Global | Global |
| msdyncrm_marketingform | Global | Global | Local | Global | Global |
| msdyncrm_marketingformactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformfield | Global | Global | Local | Global | Global |
| msdyncrm_marketingformformwhitelistrule |  |  |  |  | Global |
| msdyncrm_marketingformsubmission | Global | Global | Local | Global | Global |
| msdyncrm_marketingformtemplate | Global | Global | Local | Global | Global |
| msdyncrm_marketingformwhitelistrule | Global | Global | Global | Global |  |
| msdyncrm_marketingpage | Global | Global | Local | Global | Global |
| msdyncrm_marketingpageconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_marketingpagetemplate | Global | Global | Local | Global | Global |
| msdyncrm_matchingstrategy | Global | Global | Global | Global | Global |
| msdyncrm_matchingstrategyattribute | Global | Global | Global | Global | Global |
| msdyncrm_mktactivity | Global | Global | Local | Global | Global |
| msdyncrm_networkpage | Global | Global | Local | Global | Global |
| msdyncrm_personalizedpage | Global | Global | Local | Global | Global |
| msdyncrm_personalizedpagefield | Global | Global | Local | Global | Global |
| msdyncrm_phonecallactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_phonecallactivitymarketingtemplate | Global | Global | Local | Global | Global |
| msdyncrm_portalsettings | Global | Global | Global | Global | Global |
| msdyncrm_postingishts | Global | Global | Local | Global | Global |
| msdyncrm_quicksendemail | Global | Global | Local | Global | Global |
| msdyncrm_reaction | Global | Global | Local | Global | Global |
| msdyncrm_recordupdateactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_redirecturl | Global | Global | Local | Global | Global |
| msdyncrm_segment | Global | Global | Local | Global | Global |
| msdyncrm_segmentactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_segmenttemplate | Global | Global | Local | Global | Global |
| msdyncrm_setupdomain | Global | Global | Global | Global | Global |
| msdyncrm_socialpost | Global | Global | Local | Global | Global |
| msdyncrm_socialpostingconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_socialpostingconsent | Global | Global | Global | Global | Global |
| msdyncrm_sourceactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_splitteractivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_tag | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_taskactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_taskactivitymarketingtemplate | Global | Global | Local | Global | Global |
| msdyncrm_textstyle | Global |  |  |  |  |
| msdyncrm_triggeractivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_uicconfig | Global | Global | Local | Global | Global |
| msdyncrm_usergeoregion | Global | Global | Local | Global | Global |
| msdyncrm_usersetting | Global | Global | Local | Global | Global |
| msdyncrm_video | Global | Global | Local | Global | Global |
| msdyncrm_website | Global | Global | Local | Global | Global |
| msdynmkt_brandprofile | Global | Global | Global | Global | Global |
| msdynmkt_brandsender | Global | Global | Global | Global | Global |
| msdynmkt_brandtheme | Global | Global | Global | Global | Global |
| msdynmkt_buttonstyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_byoacschannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_byoacschannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_captcha | Global |  |  |  |  |
| msdynmkt_catalogeventstatusconfiguration | Global |  |  |  |  |
| msdynmkt_cmsaddon | Global | Global | Global | Global | Global |
| msdynmkt_commercedatasource | Global |  |  |  |  |
| msdynmkt_compliancesettings | Global | Global |  | Global | Global |
| msdynmkt_compliancesettings3 | Global | Global |  | Global | Global |
| msdynmkt_compliancesettings4 | Global | Global | Global | Global | Global |
| msdynmkt_configuration | Global |  |  |  |  |
| msdynmkt_consent | Global | Global | Global | Global | Global |
| msdynmkt_consentcenterconfiguration | Global | Global | Global | Global | Global |
| msdynmkt_consentsystemconfiguration | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent | Global | Global | Global | Global | Global |
| msdynmkt_contactpointconsent2 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent3 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent4 | Global | Global | Global | Global | Global |
| msdynmkt_contactpointsettings | Global | Global |  |  |  |
| msdynmkt_conversioneventdefinition | Global | Global | Global | Global | Global |
| msdynmkt_createdentitylink | Global |  |  |  |  |
| msdynmkt_customchannelmessage | Global | Global | Global | Global | Global |
| msdynmkt_customerdatamapping | Global | Global | Global | Global | Global |
| msdynmkt_customerdataselection | Global | Global | Global | Global | Global |
| msdynmkt_customgoalcategory | Global | Global | Global | Global | Global |
| msdynmkt_cxpasset | Global | Global | Global |  |  |
| msdynmkt_domain | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_email | Global | Global | Global | Global | Global |
| msdynmkt_emailtemplate | Global | Global | Global | Global | Global |
| msdynmkt_entitygradedistribution | Global | Global | Local | Global | Global |
| msdynmkt_entityscoredistribution | Global | Global | Local | Global | Global |
| msdynmkt_entityscoringmodel | Global | Global | Local | Global | Global |
| msdynmkt_eventmetadata | Global | Global | Global | Global | Global |
| msdynmkt_eventparametermetadata | Global |  |  |  |  |
| msdynmkt_experiment | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_featureconfiguration | Global |  |  |  |  |
| msdynmkt_file | Global |  |  |  |  |
| msdynmkt_fragment | Global | Global | Global | Global | Global |
| msdynmkt_frequencycap | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_gdprrequest | Deep | Deep | Deep | Deep |  |
| msdynmkt_image | Global |  |  |  |  |
| msdynmkt_imagestyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_infobipchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_infobipchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_journey | Global | Global | Global | Global | Global |
| msdynmkt_Journeydependency | Global |  |  |  |  |
| msdynmkt_journeyevent | Global | Global | Global | Global | Global |
| msdynmkt_journeyoptimizationcount | Global |  |  |  |  |
| msdynmkt_journeyrunparameter | Global |  |  |  |  |
| msdynmkt_journeysetting | Global | Global | Local | Global | Global |
| msdynmkt_journeytemplate | Global | Global | Global | Global | Global |
| msdynmkt_JourneyWorkflowMapping | Global | Global | Global | Global | Global |
| msdynmkt_keyword | Global | Global | Global | Global | Global |
| msdynmkt_leadqualificationmodel | Global | Global | Local | Global | Global |
| msdynmkt_linkmobilitychannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_linkmobilitychannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_marketingfieldsubmission | Global |  |  |  |  |
| msdynmkt_marketingform | Global | Global | Global | Global |  |
| msdynmkt_marketingformfield | Global |  |  |  |  |
| msdynmkt_marketingformsubmission | Global |  |  |  |  |
| msdynmkt_marketingformtemplate | Global |  |  |  | Global |
| msdynmkt_matchingstrategy | Global | Global | Global |  | Global |
| msdynmkt_matchingstrategyattribute | Global | Global | Global |  |  |
| msdynmkt_mobileapp | Deep |  |  |  |  |
| msdynmkt_mobileappchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_mobileapplication | Global | Global | Global | Global | Global |
| msdynmkt_mobiledevice | Global | Global | Global | Global | Global |
| msdynmkt_mocksmsproviderchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_mocksmsproviderchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_optimizationcustomercount | Global |  |  |  |  |
| msdynmkt_optimizationdecision | Global |  |  |  |  |
| msdynmkt_predefinedplaceholder | Global | Global | Global | Global | Global |
| msdynmkt_preferencecenter | Global | Global | Global | Global | Global |
| msdynmkt_preferencecenterlink | Global | Global | Global | Global | Global |
| msdynmkt_purpose | Global | Global | Global | Global | Global |
| msdynmkt_pushdeviceregistrationresult | Global | Global | Global | Global | Global |
| msdynmkt_pushmobiledevice | Global | Global | Global | Global | Global |
| msdynmkt_pushnotification | Global | Global | Global | Global | Global |
| msdynmkt_qrcodestyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_quiettimesetting | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_richfragment | Global |  |  |  |  |
| msdynmkt_segment | Global | Global | Local | Global | Global |
| msdynmkt_segmentdefinition | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentexecution | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentusage | Global | Global | Global | Global | Global |
| msdynmkt_sms | Global | Global | Global | Global | Global |
| msdynmkt_smsphonenumber | Global | Global | Global | Global | Global |
| msdynmkt_submitbutton | Global |  |  |  |  |
| msdynmkt_tag | Global | Global | Global | Global | Global |
| msdynmkt_telesignchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_telesignchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_textfragment | Global |  |  |  |  |
| msdynmkt_topic | Global | Global | Global | Global | Global |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_twiliochannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_twiliochannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_utmtracking | Global | Global | Global | Global | Global |
| msdynmkt_vibeschannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_vibeschannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_video | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasource | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasourcev2 | Global |  |  |  |  |
| msdynmkt_virtualsegment | Global |  |  |  |  |
| msdynmkt_virtualsegmentdatasource | Global |  |  |  |  |
| msgdpr_gdprconfiguration | Global | Global | Global |  |  |
| msgdpr_gdprconsentchangerecord | Global |  |  |  |  |
| NewsArticle | Global | Global | Global |  | Global |
| Note | Global | Basic | Local | Local | Local |
| Opportunity | Global | Global | Local | Global | Global |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrganizationSetting | Global |  |  |  |  |
| OrgEmailTemplates |  |  | Global |  |  |
| PersonalDocumentTemplate | Basic | Basic | Basic | Basic | Basic |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Position | Global |  |  |  |  |
| Post | Global |  | Global | Global | Global |
| PostFollow | Global |  | Local | Local |  |
| PrincipalObjectAttributeAccess | Global | Global | Global |  |  |
| Product | Global |  |  |  |  |
| Query | Global | Global | Global |  |  |
| RecommendedDocument | Global |  |  |  |  |
| RecordAuditHistory | Global |  |  |  |  |
| Relationship | Global |  |  |  |  |
| RelationshipRole | Global |  |  |  |  |
| Role | Global |  |  |  |  |
| SavedQueryVisualizations | Global | Global | Global |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Global |  |  |  | Global |
| SocialProfile | Global | Global | Local | Global | Global |
| Solution | Global |  |  |  |  |
| Subject | Global |  |  |  | Global |
| SyncError | Basic | Basic | Basic | Basic | Basic |
| SystemApplicationMetadata | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| SystemUser |  |  |  |  | Global |
| Team | Global | Global | Local | Global | Global |
| TraceLog | Global |  | Global | Global | Global |
| TransactionCurrency | Global |  |  | Global | Global |
| User | Global | Deep | Local | Deep | Deep |
| UserApplicationMetadata | Basic | Basic | Basic |  |  |
| UserEntityInstanceData | Basic | Basic | Basic |  |  |
| UserEntityUISettings | Basic | Basic | Basic |  |  |
| UserForm | Basic | Basic | Basic |  |  |
| UserQuery | Basic | Basic | Basic |  |  |
| UserQueryVisualizations | Basic | Basic | Basic |  |  |
| UserSettings | Global | Local | Local |  | Local |
| WebResource | Global |  |  |  |  |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Local | Local | Local | Global |
| WorkflowSession | Global | Local | Local | Local |  |

## Role: Marketing Manager (BU level) - Business

**Role identifier**: dd84f17f-cde8-e611-80d8-00155d4b205a

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Deep | Deep | Deep | Deep | Deep |
| ActionCard | Deep | Deep | Deep | Deep | Deep |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Deep | Deep | Deep | Deep | Deep |
| Adx_pagetemplate | Deep | Deep | Deep | Deep | Deep |
| adx_portallanguage | Deep | Deep | Deep | Deep | Deep |
| Adx_publishingstate | Deep | Deep | Deep | Deep | Deep |
| Adx_webpage | Deep | Deep | Deep | Deep | Deep |
| Adx_website | Deep | Deep | Deep | Deep | Deep |
| Adx_websiteaccess | Deep | Deep | Deep | Deep | Deep |
| Adx_websitebinding | Global | Global | Global | Global | Global |
| adx_websitelanguage | Deep | Deep | Deep | Deep | Deep |
| adx_webtemplate | Global | Global | Global | Global | Global |
| AppConfigMaster | Global |  |  |  |  |
| ApplicationFile | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Deep | Deep |  |  | Deep |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Deep |  |  |  | Deep |
| Campaign | Deep |  |  | Deep | Deep |
| Catalog | Global |  |  |  |  |
| CatalogAssignment | Global |  |  |  |  |
| ChannelPropertyGroup | Global |  |  | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Deep | Deep | Deep | Deep | Deep |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Deep | Deep | Deep | Deep | Deep |
| CustomAPI | Global |  |  |  |  |
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
| EnvironmentVariableDefinition | Deep |  |  |  |  |
| EnvironmentVariableValue | Global |  |  |  |  |
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
| msdyn_ChannelDefinition | Global |  |  |  | Global |
| msdyn_channeldefinitionconsent | Deep | Deep | Deep | Deep |  |
| msdyn_ChannelDefinitionLocale | Global |  |  |  |  |
| msdyn_ChannelInstance | Deep | Deep | Deep | Deep | Deep |
| msdyn_ChannelInstanceAccount | Deep | Deep | Deep | Deep | Deep |
| msdyn_ChannelMessagePart | Global |  |  |  |  |
| msdyn_ConsumingApplication | Global |  |  |  | Global |
| msdyn_dataanalyticsreport_mkt | Global |  |  |  |  |
| msdyn_occommunicationprovidersetting | Deep | Deep | Deep | Deep | Deep |
| msdyn_ocphonenumber | Deep | Deep | Deep | Deep | Deep |
| msdyn_odatav4ds | Global | Global |  | Global | Global |
| msdyn_PostAlbum | Deep | Deep | Deep | Deep | Deep |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_PostRuleConfig | Global |  |  |  |  |
| msdyn_wallsavedquery | Global |  |  |  |  |
| msdyn_wallsavedqueryusersettings | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_appointmentactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_appointmentactivitymarketingtemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_cdnconfiguration | Deep |  |  |  |  |
| msdyncrm_cdsaconnectorconfiguration | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_contentblock | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_contentsettings | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_createleadactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerinsightsinfo | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourney | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourneycustomchannelactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourneyiteration | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourneyruntimestate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourneytemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_customerjourneyworkflowlink | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_defaultmarketingsetting | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_delaydatetimeactivity | Global | Global | Global |  |  |
| msdyncrm_delaydurationactivity | Global | Global | Global |  |  |
| msdyncrm_deprecatedcustomtileactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedeventactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedformsprosurveyactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_deprecatedpageactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_designerfeatureavailability | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_emailkeypoint | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Deep |  |  |  |  |
| msdyncrm_file | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_formpage | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_formpagetemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_geopin | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_gpt3log | Global |  |  |  |  |
| msdyncrm_gwennolfeatureconfiguration | Global | Deep | Deep | Deep | Deep |
| msdyncrm_gwennolspamscoreactivity | Deep |  |  |  |  |
| msdyncrm_gwennolspamscorerequest | Deep |  | Deep |  |  |
| msdyncrm_keyword | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_launchworkflowactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_leadscoremodel | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_leadscoringconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_linkedincampaignactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_listform | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_liveentitydependency | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_marketingdynamiccontentmetadata | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemail | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemailactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemaildynamiccontentmetadata | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemailtemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingemailtest | Deep |  |  | Deep | Deep |
| msdyncrm_marketingemailtestattribute | Deep |  |  | Deep | Deep |
| msdyncrm_marketingemailtestsend | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingfieldsubmission | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingform | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformfield | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformformwhitelistrule |  |  |  |  | Global |
| msdyncrm_marketingformsubmission | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformtemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingformwhitelistrule | Deep | Deep | Deep | Deep |  |
| msdyncrm_marketingpage | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_marketingpageconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_marketingpagetemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_matchingstrategy | Global | Global | Global | Global | Global |
| msdyncrm_matchingstrategyattribute | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_mktactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_networkpage | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_personalizedpage | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_personalizedpagefield | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_phonecallactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_phonecallactivitymarketingtemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_portalsettings | Global | Global | Global | Global | Global |
| msdyncrm_postingishts | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_quicksendemail | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_reaction | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_recordupdateactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_redirecturl | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_segment | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_segmentactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_segmenttemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_setupdomain | Global | Global | Global | Global | Global |
| msdyncrm_socialpost | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_socialpostingconfiguration | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_socialpostingconsent | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_sourceactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_splitteractivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_tag | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_taskactivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_taskactivitymarketingtemplate | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_textstyle | Global |  |  |  |  |
| msdyncrm_triggeractivity | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_uicconfig | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_usergeoregion | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_usersetting | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_video | Deep | Deep | Deep | Deep | Deep |
| msdyncrm_website | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_brandprofile | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_brandsender | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_brandtheme | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_buttonstyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_byoacschannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_byoacschannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_captcha | Deep |  |  |  |  |
| msdynmkt_catalogeventstatusconfiguration | Global |  |  |  |  |
| msdynmkt_cmsaddon | Global | Global | Global | Global | Global |
| msdynmkt_commercedatasource | Global |  |  |  |  |
| msdynmkt_compliancesettings | Global |  |  | Global | Global |
| msdynmkt_compliancesettings3 | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_compliancesettings4 | Global | Deep | Deep | Global | Global |
| msdynmkt_configuration | Global |  |  |  |  |
| msdynmkt_consent | Global | Global | Global | Global | Global |
| msdynmkt_consentcenterconfiguration | Global | Global | Global | Global | Global |
| msdynmkt_consentsystemconfiguration | Deep | Deep | Deep |  |  |
| msdynmkt_contactpointconsent | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_contactpointconsent2 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent3 | Deep | Deep | Deep |  |  |
| msdynmkt_contactpointconsent4 | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_contactpointsettings | Global |  |  |  |  |
| msdynmkt_conversioneventdefinition | Global | Global | Global | Global | Global |
| msdynmkt_createdentitylink | Deep |  |  |  |  |
| msdynmkt_customchannelmessage | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_customerdatamapping | Global | Global | Global | Global | Global |
| msdynmkt_customerdataselection | Global | Global | Global | Global | Global |
| msdynmkt_customgoalcategory | Global | Global | Global | Global | Global |
| msdynmkt_cxpasset | Global | Global | Global |  |  |
| msdynmkt_domain | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_email | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_emailtemplate | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_entitygradedistribution | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_entityscoredistribution | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_entityscoringmodel | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_eventmetadata | Deep | Deep | Deep | Deep | Global |
| msdynmkt_eventparametermetadata | Deep |  |  |  |  |
| msdynmkt_experiment | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_featureconfiguration | Deep |  |  |  |  |
| msdynmkt_file | Global |  |  |  |  |
| msdynmkt_fragment | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_frequencycap | Deep |  |  |  |  |
| msdynmkt_gdprrequest | Deep | Deep | Deep | Deep |  |
| msdynmkt_image | Global |  |  |  |  |
| msdynmkt_imagestyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_infobipchannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_infobipchannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_journey | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_Journeydependency | Deep |  |  |  |  |
| msdynmkt_journeyevent | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_journeyoptimizationcount | Deep |  |  |  |  |
| msdynmkt_journeyrunparameter | Deep |  |  |  |  |
| msdynmkt_journeysetting | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_journeytemplate | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_JourneyWorkflowMapping | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_keyword | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_leadqualificationmodel | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_linkmobilitychannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_linkmobilitychannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_marketingfieldsubmission | Deep |  |  |  |  |
| msdynmkt_marketingform | Deep | Deep | Deep | Deep |  |
| msdynmkt_marketingformfield | Deep |  |  |  |  |
| msdynmkt_marketingformsubmission | Deep |  |  |  |  |
| msdynmkt_marketingformtemplate | Deep |  |  |  | Deep |
| msdynmkt_matchingstrategy | Deep | Deep | Deep |  | Deep |
| msdynmkt_matchingstrategyattribute | Deep | Deep | Deep | Deep |  |
| msdynmkt_mobileapp | Deep |  |  |  |  |
| msdynmkt_mobileappchannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_mobileapplication | Global | Global | Global | Global | Global |
| msdynmkt_mobiledevice | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_mocksmsproviderchannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_mocksmsproviderchannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_optimizationcustomercount | Global |  |  |  |  |
| msdynmkt_optimizationdecision | Global |  |  |  |  |
| msdynmkt_predefinedplaceholder | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_preferencecenter | Global | Deep | Deep | Global | Global |
| msdynmkt_preferencecenterlink | Global | Global | Global | Global | Global |
| msdynmkt_purpose | Global | Deep | Deep | Global | Global |
| msdynmkt_pushdeviceregistrationresult | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_pushmobiledevice | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_pushnotification | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_qrcodestyle | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_quiettimesetting | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_richfragment | Global |  |  |  |  |
| msdynmkt_segment | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentdefinition | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentexecution | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentusage | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_sms | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_smsphonenumber | Global |  |  | Global | Global |
| msdynmkt_submitbutton | Deep |  |  |  |  |
| msdynmkt_tag | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_telesignchannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_telesignchannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_textfragment | Global |  |  |  |  |
| msdynmkt_topic | Global | Deep | Deep | Global | Global |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_twiliochannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_twiliochannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_utmtracking | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_vibeschannelinstance | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_vibeschannelinstanceaccount | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_video | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasource | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasourcev2 | Global |  |  |  |  |
| msdynmkt_virtualsegment | Global |  |  |  |  |
| msdynmkt_virtualsegmentdatasource | Global |  |  |  |  |
| msgdpr_gdprconfiguration | Global | Global | Global |  |  |
| msgdpr_gdprconsentchangerecord | Global |  |  |  |  |
| NewsArticle | Global |  |  |  |  |
| Note | Deep | Deep | Deep | Deep | Deep |
| Opportunity | Deep | Deep | Deep | Deep | Deep |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrganizationSetting | Global |  |  |  |  |
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
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Deep |  |  |  | Deep |
| SocialProfile | Deep | Deep | Deep | Deep | Deep |
| Solution | Global |  |  |  |  |
| Subject | Global |  |  |  | Global |
| SyncError | Deep | Deep | Deep | Deep | Deep |
| SystemApplicationMetadata | Global |  |  |  |  |
| SystemForm | Global |  |  |  |  |
| SystemUser |  |  |  |  | Global |
| Team | Global |  |  |  |  |
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
| WebResource | Global |  |  |  |  |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Deep | Deep | Deep | Global |
| WorkflowSession | Global | Deep | Deep | Deep |  |

## Role: Marketing Professional - Business

**Role identifier**: ce995e5a-cee8-e611-80d8-00155d4b205a

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Global | Global | Basic | Global | Global |
| ActionCard | Basic | Basic | Basic | Basic | Global |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Global | Local | Basic | Local | Local |
| Adx_pagetemplate | Global | Global | Basic | Global | Global |
| adx_portallanguage | Global | Global | Basic | Global | Global |
| Adx_publishingstate | Global | Global | Global | Global | Global |
| Adx_webpage | Global | Global | Basic | Global | Global |
| Adx_website | Global | Global | Basic | Global | Global |
| Adx_websiteaccess | Global | Global | Basic | Global | Global |
| Adx_websitebinding | Global | Global | Global | Global | Global |
| adx_websitelanguage | Global | Global | Basic | Global | Global |
| adx_webtemplate | Global | Global | Global | Global | Global |
| ApplicationFile | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Basic | Basic |  |  | Basic |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Global |  |  |  | Global |
| Campaign | Global |  |  | Local | Local |
| Catalog | Global |  |  |  |  |
| CatalogAssignment | Global |  |  |  |  |
| ChannelPropertyGroup | Global |  |  | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Global | Global | Basic | Global | Global |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Global | Global | Basic | Global | Global |
| CustomAPI | Global |  |  |  |  |
| CustomerOpportunityRole | Global | Basic | Basic | Global | Global |
| CustomerRelationship | Global | Basic | Basic | Global | Global |
| Customization | Global |  |  |  |  |
| DocumentTemplate | Global |  |  |  |  |
| DuplicateRule | Global |  |  |  |  |
| EmailServerProfile | Global |  |  |  | Global |
| EmailSignature | Global | Basic | Basic |  |  |
| EmailTemplate | Global | Basic | Basic | Local |  |
| Entity | Global |  |  |  |  |
| EntityKey | Global |  |  |  |  |
| EntityMap | Global |  |  |  |  |
| EnvironmentVariableDefinition | Global |  |  |  |  |
| EnvironmentVariableValue | Global |  |  |  |  |
| ExchangeSyncIdMapping | Basic | Basic | Basic |  |  |
| Feedback | Global |  |  | Global | Global |
| GoalRollupQuery | Basic |  |  |  |  |
| HierarchyRule | Global |  |  |  |  |
| Import | Basic | Basic | Basic | Basic | Basic |
| ImportFile | Basic | Basic | Basic | Basic | Basic |
| ImportMap | Global | Local | Local | Local | Local |
| LanguageLocale | Global |  |  | Global | Global |
| Lead | Global | Global | Basic | Global | Global |
| LeadToOpportunitySalesProcess | Global | Global | Global | Global | Global |
| License | Global |  |  |  |  |
| List | Global | Deep | Basic | Deep | Deep |
| Mailbox | Basic | Basic |  | Basic |  |
| MailboxTrackingFolder | Basic | Basic | Basic | Basic |  |
| MailMergeTemplate | Basic | Basic | Basic | Basic | Basic |
| MobileOfflineProfile | Global |  |  |  |  |
| msdyn_ChannelDefinition | Global |  |  |  | Global |
| msdyn_channeldefinitionconsent | Global | Global | Global | Global |  |
| msdyn_ChannelDefinitionLocale | Global |  |  |  |  |
| msdyn_ChannelInstance | Global | Global | Global | Global | Global |
| msdyn_ChannelInstanceAccount | Global | Global | Global | Global | Global |
| msdyn_ChannelMessagePart | Global |  |  |  |  |
| msdyn_ConsumingApplication | Global |  |  |  | Global |
| msdyn_dataanalyticsreport_mkt | Global |  |  |  |  |
| msdyn_occommunicationprovidersetting | Local | Local | Local | Local | Local |
| msdyn_ocphonenumber | Local | Local | Local | Local | Local |
| msdyn_odatav4ds | Global | Global |  | Global | Global |
| msdyn_PostAlbum | Global | Basic | Basic | Basic | Basic |
| msdyn_PostConfig | Global |  |  |  |  |
| msdyn_PostRuleConfig | Global |  |  |  |  |
| msdyn_wallsavedquery | Global |  |  |  |  |
| msdyn_wallsavedqueryusersettings | Basic | Basic | Basic | Basic | Basic |
| msdynci_alternatekey | Global |  |  |  |  |
| msdynci_customerprofile | Global |  |  |  |  |
| msdyncrm_appointmentactivity | Local | Local | Local | Local | Local |
| msdyncrm_appointmentactivitymarketingtemplate | Global | Global | Basic | Global | Global |
| msdyncrm_cdnconfiguration | Global |  |  |  |  |
| msdyncrm_cdsaconnectorconfiguration | Global |  |  |  |  |
| msdyncrm_contentblock | Global | Global | Global | Global | Global |
| msdyncrm_contentsettings | Global | Global | Basic | Global | Global |
| msdyncrm_createleadactivity | Local | Local | Local | Local | Local |
| msdyncrm_customerinsightsinfo | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourney | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourneycustomchannelactivity | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourneyiteration | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourneyruntimestate | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourneytemplate | Global | Global | Basic | Global | Global |
| msdyncrm_customerjourneyworkflowlink | Global | Global | Basic | Global | Global |
| msdyncrm_defaultmarketingsetting | Global | Global | Basic | Global | Global |
| msdyncrm_delaydatetimeactivity | Global | Global | Global |  |  |
| msdyncrm_delaydurationactivity | Global | Global | Global |  |  |
| msdyncrm_deprecatedcustomtileactivity | Local | Local | Local | Local | Local |
| msdyncrm_deprecatedeventactivity | Local | Local | Local | Local | Local |
| msdyncrm_deprecatedformsprosurveyactivity | Local | Local | Local | Local | Local |
| msdyncrm_deprecatedpageactivity | Local | Local | Local | Local | Local |
| msdyncrm_designerfeatureavailability | Global | Global | Basic | Global | Global |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_emailkeypoint | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Global |  |  |  |  |
| msdyncrm_file | Global | Global | Basic | Global | Global |
| msdyncrm_formpage | Global | Global | Basic | Global | Global |
| msdyncrm_formpagetemplate | Global | Global | Basic | Global | Global |
| msdyncrm_geopin | Global | Global | Basic | Global | Global |
| msdyncrm_gpt3log | Global |  |  |  |  |
| msdyncrm_gwennolfeatureconfiguration | Global |  |  |  |  |
| msdyncrm_gwennolspamscoreactivity | Local |  |  |  |  |
| msdyncrm_gwennolspamscorerequest | Global |  | Global |  |  |
| msdyncrm_keyword | Global | Global | Basic | Global | Global |
| msdyncrm_launchworkflowactivity | Local | Local | Local | Local | Local |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_linkedincampaignactivity | Local | Local | Local | Local | Local |
| msdyncrm_listform | Global | Global | Basic | Global | Global |
| msdyncrm_liveentitydependency | Global | Global | Global | Global | Global |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_marketingdynamiccontentmetadata | Global | Global | Basic | Global | Global |
| msdyncrm_marketingemail | Global | Global | Basic | Global | Global |
| msdyncrm_marketingemailactivity | Local | Local | Local | Local | Local |
| msdyncrm_marketingemaildynamiccontentmetadata | Global | Global | Basic | Global | Global |
| msdyncrm_marketingemailtemplate | Global | Global | Basic | Global | Global |
| msdyncrm_marketingemailtest | Global |  |  | Global | Global |
| msdyncrm_marketingemailtestattribute | Global |  |  | Global | Global |
| msdyncrm_marketingemailtestsend | Global | Global | Basic | Global | Global |
| msdyncrm_marketingfieldsubmission | Global | Global | Basic | Global | Global |
| msdyncrm_marketingform | Global | Global | Basic | Global | Global |
| msdyncrm_marketingformactivity | Local | Local | Local | Local | Local |
| msdyncrm_marketingformfield | Global | Global | Basic | Global | Global |
| msdyncrm_marketingformformwhitelistrule |  |  |  |  | Global |
| msdyncrm_marketingformsubmission | Global | Global | Basic | Global | Global |
| msdyncrm_marketingformtemplate | Global | Global | Basic | Global | Global |
| msdyncrm_marketingformwhitelistrule | Global | Global | Global | Global |  |
| msdyncrm_marketingpage | Global | Global | Basic | Global | Global |
| msdyncrm_marketingpageconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_marketingpagetemplate | Global | Global | Basic | Global | Global |
| msdyncrm_matchingstrategy | Global | Global | Global | Global | Global |
| msdyncrm_matchingstrategyattribute | Global | Global | Global | Global | Global |
| msdyncrm_mktactivity | Global | Global | Basic | Global | Global |
| msdyncrm_networkpage | Global | Global | Local | Global | Global |
| msdyncrm_personalizedpage | Global | Global | Local | Global | Global |
| msdyncrm_phonecallactivity | Local | Local | Local | Local | Local |
| msdyncrm_phonecallactivitymarketingtemplate | Global | Global | Basic | Global | Global |
| msdyncrm_portalsettings | Global | Global | Global | Global | Global |
| msdyncrm_postingishts | Global | Global | Local | Global | Global |
| msdyncrm_quicksendemail | Global | Global | Local | Global | Global |
| msdyncrm_reaction | Global | Global | Local | Global | Global |
| msdyncrm_recordupdateactivity | Local | Local | Local | Local | Local |
| msdyncrm_redirecturl | Global | Global | Basic | Global | Global |
| msdyncrm_segment | Global | Global | Basic | Global | Global |
| msdyncrm_segmentactivity | Local | Local | Local | Local | Local |
| msdyncrm_segmenttemplate | Global | Global | Basic | Global | Global |
| msdyncrm_setupdomain | Global | Global |  |  |  |
| msdyncrm_socialpost | Global | Global | Local | Global | Global |
| msdyncrm_socialpostingconfiguration | Global |  |  |  |  |
| msdyncrm_socialpostingconsent | Global |  |  |  |  |
| msdyncrm_sourceactivity | Local | Local | Local | Local | Local |
| msdyncrm_splitteractivity | Local | Local | Local | Local | Local |
| msdyncrm_tag | Local | Local | Local | Local | Local |
| msdyncrm_taskactivity | Local | Local | Local | Local | Local |
| msdyncrm_taskactivitymarketingtemplate | Global | Global | Basic | Global | Global |
| msdyncrm_textstyle | Global |  |  |  |  |
| msdyncrm_triggeractivity | Local | Local | Local | Local | Local |
| msdyncrm_uicconfig | Global | Global | Basic | Global | Global |
| msdyncrm_usergeoregion | Global | Global | Basic | Global | Global |
| msdyncrm_usersetting | Global | Global | Local | Global | Global |
| msdyncrm_video | Global | Global | Local | Global | Global |
| msdyncrm_website | Global | Global | Basic | Global | Global |
| msdynmkt_brandprofile | Global |  |  |  |  |
| msdynmkt_brandsender | Global |  |  |  |  |
| msdynmkt_brandtheme | Global |  |  |  |  |
| msdynmkt_buttonstyle | Local | Local | Local | Local | Local |
| msdynmkt_byoacschannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_byoacschannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_captcha | Global |  |  |  |  |
| msdynmkt_catalogeventstatusconfiguration | Global |  |  |  |  |
| msdynmkt_cmsaddon | Global | Global | Global | Global | Global |
| msdynmkt_commercedatasource | Global |  |  |  |  |
| msdynmkt_compliancesettings | Global |  |  | Global | Global |
| msdynmkt_compliancesettings3 | Global |  |  | Global | Global |
| msdynmkt_compliancesettings4 | Global | Global | Global | Global | Global |
| msdynmkt_configuration | Global |  |  |  |  |
| msdynmkt_consent | Global | Global | Global | Global | Global |
| msdynmkt_consentcenterconfiguration | Global | Global | Global | Global | Global |
| msdynmkt_consentsystemconfiguration | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent | Global | Global | Global | Global | Global |
| msdynmkt_contactpointconsent2 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent3 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent4 | Global | Global | Global | Global | Global |
| msdynmkt_contactpointsettings | Global |  |  |  |  |
| msdynmkt_conversioneventdefinition | Global | Local | Local | Local | Global |
| msdynmkt_createdentitylink | Global |  |  |  |  |
| msdynmkt_customchannelmessage | Global | Global | Global | Global | Global |
| msdynmkt_customerdatamapping | Global | Global | Global | Global | Global |
| msdynmkt_customerdataselection | Global | Global | Global | Global | Global |
| msdynmkt_customgoalcategory | Global | Global | Global | Global | Global |
| msdynmkt_cxpasset | Global | Global | Global |  |  |
| msdynmkt_domain | Local | Local | Local | Local | Local |
| msdynmkt_email | Global | Global | Global | Global | Global |
| msdynmkt_emailtemplate | Global | Global | Global | Global | Global |
| msdynmkt_eventmetadata | Global | Local | Local | Global | Global |
| msdynmkt_eventparametermetadata | Global |  |  |  |  |
| msdynmkt_experiment | Local | Local | Local | Local | Local |
| msdynmkt_featureconfiguration | Global |  |  |  |  |
| msdynmkt_file | Global |  |  |  |  |
| msdynmkt_fragment | Global | Global | Global | Global | Global |
| msdynmkt_frequencycap | Local |  |  |  |  |
| msdynmkt_gdprrequest | Local | Local | Local | Local |  |
| msdynmkt_image | Global |  |  |  |  |
| msdynmkt_imagestyle | Local | Local | Local | Local | Local |
| msdynmkt_infobipchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_infobipchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_journey | Global | Global | Local | Global | Global |
| msdynmkt_Journeydependency | Global |  |  |  |  |
| msdynmkt_journeyevent | Global | Global | Basic | Global | Global |
| msdynmkt_journeyoptimizationcount | Global |  |  |  |  |
| msdynmkt_journeyrunparameter | Global |  |  |  |  |
| msdynmkt_journeysetting | Global | Global | Basic | Global | Global |
| msdynmkt_journeytemplate | Global | Global | Local | Global | Global |
| msdynmkt_JourneyWorkflowMapping | Global | Global | Global | Global | Global |
| msdynmkt_keyword | Global | Global | Global | Global | Global |
| msdynmkt_linkmobilitychannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_linkmobilitychannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_marketingfieldsubmission | Global |  |  |  |  |
| msdynmkt_marketingform | Global | Global | Global | Global |  |
| msdynmkt_marketingformfield | Global |  |  |  |  |
| msdynmkt_marketingformsubmission | Global |  |  |  |  |
| msdynmkt_marketingformtemplate | Global |  |  |  | Global |
| msdynmkt_matchingstrategy | Global | Global | Global |  | Global |
| msdynmkt_matchingstrategyattribute | Global |  |  |  |  |
| msdynmkt_mobileapp | Deep |  |  |  |  |
| msdynmkt_mobileappchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_mobileapplication | Global | Global | Global | Global | Global |
| msdynmkt_mobiledevice | Global | Global | Global | Global | Global |
| msdynmkt_mocksmsproviderchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_mocksmsproviderchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_optimizationcustomercount | Global |  |  |  |  |
| msdynmkt_optimizationdecision | Global |  |  |  |  |
| msdynmkt_predefinedplaceholder | Global | Global | Global | Global | Global |
| msdynmkt_preferencecenter | Global | Global | Global | Global | Global |
| msdynmkt_preferencecenterlink | Global | Global | Global | Global | Global |
| msdynmkt_purpose | Global | Global | Global | Global | Global |
| msdynmkt_pushdeviceregistrationresult | Global | Global | Global | Global | Global |
| msdynmkt_pushmobiledevice | Global | Global | Global | Global | Global |
| msdynmkt_pushnotification | Global | Global | Global | Global | Global |
| msdynmkt_qrcodestyle | Local | Local | Local | Local | Local |
| msdynmkt_quiettimesetting | Local |  |  |  |  |
| msdynmkt_richfragment | Global |  |  |  |  |
| msdynmkt_segment | Global | Global | Basic | Global | Global |
| msdynmkt_segmentdefinition | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentexecution | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_segmentusage | Global | Global | Global | Global | Global |
| msdynmkt_sms | Global | Global | Global | Global | Global |
| msdynmkt_smsphonenumber | Global | Global | Global | Global | Global |
| msdynmkt_submitbutton | Global |  |  |  |  |
| msdynmkt_tag | Global | Global | Global | Global | Global |
| msdynmkt_telesignchannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_telesignchannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_textfragment | Global |  |  |  |  |
| msdynmkt_topic | Global | Global | Global | Global | Global |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_twiliochannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_twiliochannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_utmtracking | Global | Global | Global | Global | Global |
| msdynmkt_vibeschannelinstance | Global | Global | Global | Global | Global |
| msdynmkt_vibeschannelinstanceaccount | Global | Global | Global | Global | Global |
| msdynmkt_video | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasource | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasourcev2 | Global |  |  |  |  |
| msdynmkt_virtualsegment | Global |  |  |  |  |
| msdynmkt_virtualsegmentdatasource | Global |  |  |  |  |
| msgdpr_gdprconfiguration | Global |  |  |  |  |
| msgdpr_gdprconsentchangerecord | Global |  |  |  |  |
| NewsArticle | Global |  |  |  |  |
| Note | Global | Basic | Basic | Local | Local |
| Opportunity | Global | Global | Basic | Global | Global |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrganizationSetting | Global |  |  |  |  |
| OrgEmailTemplates |  |  | Global |  |  |
| PersonalDocumentTemplate | Basic | Basic | Basic | Basic | Basic |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| Position | Global |  |  |  |  |
| Post | Global |  | Global | Global | Global |
| PostFollow | Global |  | Basic | Basic |  |
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
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Global |  |  |  | Global |
| SocialProfile | Global | Global | Basic | Global | Global |
| Solution | Global |  |  |  |  |
| Subject | Global |  |  |  | Global |
| SyncError | Basic | Basic | Basic | Basic | Basic |
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
| WebResource | Global |  |  |  |  |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Basic | Basic | Basic | Global |
| WorkflowSession | Global | Basic | Basic | Basic |  |

## Role: Marketing Professional (BU level) - Business

**Role identifier**: 6d63ebe3-cee8-e611-80d8-00155d4b205a

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Account | Local | Local | Local | Local | Local |
| ActionCard | Local | Local | Local | Local | Local |
| ActionCardUserSettings | Basic | Basic | Basic |  |  |
| Activity | Local | Local | Local | Local | Local |
| Adx_pagetemplate | Local | Local | Local | Local | Local |
| adx_portallanguage | Local | Local | Local | Local | Local |
| Adx_publishingstate | Local | Local | Local | Local | Local |
| Adx_webpage | Local | Local | Local | Local | Local |
| Adx_website | Local | Local | Local | Local | Local |
| Adx_websiteaccess | Local | Local | Local | Local | Local |
| Adx_websitebinding | Global | Global | Global | Global | Global |
| adx_websitelanguage | Local | Local | Local | Local | Local |
| adx_webtemplate | Global | Global | Global | Global | Global |
| ApplicationFile | Global |  |  |  |  |
| AppModule | Global |  |  |  |  |
| AsyncOperation | Local | Local |  |  | Local |
| Attribute | Global |  |  |  |  |
| AttributeMap | Global |  |  |  |  |
| BusinessUnit | Local |  |  |  | Local |
| Campaign | Local |  |  | Local | Local |
| Catalog | Global |  |  |  |  |
| CatalogAssignment | Global |  |  |  |  |
| ChannelPropertyGroup | Global |  |  | Global | Global |
| ComplexControl | Global |  |  |  |  |
| Connection | Local | Local | Local | Local | Local |
| ConnectionRole | Global |  |  |  |  |
| Constraint |  |  |  | Global |  |
| Contact | Local | Local | Local | Local | Local |
| CustomAPI | Global |  |  |  |  |
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
| EnvironmentVariableDefinition | Local |  |  |  |  |
| EnvironmentVariableValue | Global |  |  |  |  |
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
| msdyn_ChannelDefinition | Global |  |  |  | Global |
| msdyn_channeldefinitionconsent | Local | Local | Local | Local |  |
| msdyn_ChannelDefinitionLocale | Global |  |  |  |  |
| msdyn_ChannelInstance | Local | Local | Local | Local | Local |
| msdyn_ChannelInstanceAccount | Local | Local | Local | Local | Local |
| msdyn_ChannelMessagePart | Global |  |  |  |  |
| msdyn_ConsumingApplication | Global |  |  |  | Global |
| msdyn_dataanalyticsreport_mkt | Global |  |  |  |  |
| msdyn_occommunicationprovidersetting | Local | Local | Local | Local | Local |
| msdyn_ocphonenumber | Local | Local | Local | Local | Local |
| msdyncrm_appointmentactivitymarketingtemplate | Local | Local | Local | Local | Local |
| msdyncrm_cdnconfiguration | Local |  |  |  |  |
| msdyncrm_contentblock | Local | Local | Local | Local | Local |
| msdyncrm_contentsettings | Local | Local | Local | Local | Local |
| msdyncrm_customerinsightsinfo | Local | Local | Local | Local | Local |
| msdyncrm_customerjourney | Local | Local | Local | Local | Local |
| msdyncrm_customerjourneycustomchannelactivity | Local | Local | Local | Local | Local |
| msdyncrm_customerjourneyiteration | Local | Local | Local | Local | Local |
| msdyncrm_customerjourneyruntimestate | Local | Local | Local | Local | Local |
| msdyncrm_customerjourneytemplate | Local | Local | Local | Local | Local |
| msdyncrm_customerjourneyworkflowlink | Local | Local | Local | Local | Local |
| msdyncrm_defaultmarketingsetting | Local | Local | Local | Local | Local |
| msdyncrm_designerfeatureavailability | Local | Local | Local | Local | Local |
| msdyncrm_digitalassetsconfiguration | Global |  |  |  |  |
| msdyncrm_featureconfiguration | Local |  |  |  |  |
| msdyncrm_file | Local | Local | Local | Local | Local |
| msdyncrm_formpage | Local | Local | Local | Local | Local |
| msdyncrm_formpagetemplate | Local | Local | Local | Local | Local |
| msdyncrm_geopin | Local | Local | Local | Local | Local |
| msdyncrm_gwennolspamscorerequest | Local |  | Local |  |  |
| msdyncrm_keyword | Local | Local | Local | Local | Local |
| msdyncrm_leadtoopportunity | Global | Global | Global | Global | Global |
| msdyncrm_listform | Local | Local | Local | Local | Local |
| msdyncrm_liveentitydependency | Local | Local | Local | Local | Local |
| msdyncrm_marketingconfiguration | Global |  |  |  |  |
| msdyncrm_marketingdynamiccontentmetadata | Local | Local | Local | Local | Local |
| msdyncrm_marketingemail | Local | Local | Local | Local | Local |
| msdyncrm_marketingemaildynamiccontentmetadata | Local | Local | Local | Local | Local |
| msdyncrm_marketingemailtemplate | Local | Local | Local | Local | Local |
| msdyncrm_marketingemailtest | Local |  |  | Local | Local |
| msdyncrm_marketingemailtestattribute | Local |  |  | Local | Local |
| msdyncrm_marketingemailtestsend | Local | Local | Local | Local | Local |
| msdyncrm_marketingfieldsubmission | Local | Local | Local | Local | Local |
| msdyncrm_marketingform | Local | Local | Local | Local | Local |
| msdyncrm_marketingformfield | Local | Local | Local | Local | Local |
| msdyncrm_marketingformsubmission | Local | Local | Local | Local | Local |
| msdyncrm_marketingformtemplate | Local | Local | Local | Local | Local |
| msdyncrm_marketingformwhitelistrule | Local | Local | Local | Local |  |
| msdyncrm_marketingpage | Local | Local | Local | Local | Local |
| msdyncrm_marketingpageconfiguration | Global | Global | Global | Global | Global |
| msdyncrm_marketingpagetemplate | Local | Local | Local | Local | Local |
| msdyncrm_matchingstrategy | Global | Global | Global | Global | Global |
| msdyncrm_matchingstrategyattribute | Local | Local | Local | Local | Local |
| msdyncrm_mktactivity | Local | Local | Local | Local | Local |
| msdyncrm_networkpage | Local | Local | Local | Local | Local |
| msdyncrm_personalizedpage | Local | Local | Local | Local | Local |
| msdyncrm_phonecallactivitymarketingtemplate | Local | Local | Local | Local | Local |
| msdyncrm_portalsettings | Global | Global | Global | Global | Global |
| msdyncrm_postingishts | Local | Local | Local | Local | Local |
| msdyncrm_quicksendemail | Local | Local | Local | Local | Local |
| msdyncrm_reaction | Local | Local | Local | Local | Local |
| msdyncrm_redirecturl | Local | Local | Local | Local | Local |
| msdyncrm_segment | Local | Local | Local | Local | Local |
| msdyncrm_segmenttemplate | Local | Local | Local | Local | Local |
| msdyncrm_setupdomain | Global | Global |  |  |  |
| msdyncrm_socialpost | Local | Local | Local | Local | Local |
| msdyncrm_socialpostingconfiguration | Local |  |  |  |  |
| msdyncrm_taskactivitymarketingtemplate | Local | Local | Local | Local | Local |
| msdyncrm_uicconfig | Local | Local | Local | Local | Local |
| msdyncrm_usergeoregion | Local | Local | Local | Local | Local |
| msdyncrm_usersetting | Local | Local | Local | Local | Local |
| msdyncrm_video | Local | Local | Local | Local | Local |
| msdyncrm_website | Local | Local | Local | Local | Local |
| msdynmkt_brandprofile | Local |  |  | Local | Local |
| msdynmkt_brandsender | Local |  |  |  | Local |
| msdynmkt_brandtheme | Local |  |  |  |  |
| msdynmkt_buttonstyle | Local | Local | Local | Local | Local |
| msdynmkt_byoacschannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_byoacschannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_captcha | Local |  |  |  |  |
| msdynmkt_catalogeventstatusconfiguration | Global |  |  |  |  |
| msdynmkt_cmsaddon | Global | Global | Global | Global | Global |
| msdynmkt_commercedatasource | Global |  |  |  |  |
| msdynmkt_compliancesettings | Global |  |  | Global | Global |
| msdynmkt_compliancesettings3 | Local | Local | Local | Local | Local |
| msdynmkt_compliancesettings4 | Global | Local | Local | Global | Global |
| msdynmkt_configuration | Global |  |  |  |  |
| msdynmkt_consent | Global | Global | Global | Global | Global |
| msdynmkt_consentcenterconfiguration | Global | Global | Global | Global | Global |
| msdynmkt_consentsystemconfiguration | Local | Local | Local |  |  |
| msdynmkt_contactpointconsent | Local | Local | Local | Local | Local |
| msdynmkt_contactpointconsent2 | Global | Global | Global |  |  |
| msdynmkt_contactpointconsent3 | Local | Local | Local |  |  |
| msdynmkt_contactpointconsent4 | Local | Local | Local | Local | Local |
| msdynmkt_contactpointsettings | Global |  |  |  |  |
| msdynmkt_conversioneventdefinition | Global | Local | Local | Local | Global |
| msdynmkt_createdentitylink | Local |  |  |  |  |
| msdynmkt_customchannelmessage | Local | Local | Local | Local | Local |
| msdynmkt_customerdatamapping | Global | Global | Global | Global | Global |
| msdynmkt_customerdataselection | Global | Global | Global | Global | Global |
| msdynmkt_customgoalcategory | Global | Global | Global | Global | Global |
| msdynmkt_cxpasset | Global | Global | Global |  |  |
| msdynmkt_domain | Local | Local | Local | Local | Local |
| msdynmkt_email | Local | Local | Local | Local | Local |
| msdynmkt_emailtemplate | Local | Local | Local | Local | Local |
| msdynmkt_eventmetadata | Local | Local | Local | Local | Global |
| msdynmkt_eventparametermetadata | Local |  |  |  |  |
| msdynmkt_experiment | Local | Local | Local | Local | Local |
| msdynmkt_featureconfiguration | Local |  |  |  |  |
| msdynmkt_file | Global |  |  |  |  |
| msdynmkt_fragment | Local | Local | Local | Local | Local |
| msdynmkt_frequencycap | Local |  |  |  |  |
| msdynmkt_gdprrequest | Local | Local | Local | Local |  |
| msdynmkt_image | Global |  |  |  |  |
| msdynmkt_imagestyle | Local | Local | Local | Local | Local |
| msdynmkt_infobipchannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_infobipchannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_journey | Local | Local | Local | Local | Local |
| msdynmkt_Journeydependency | Local |  |  |  |  |
| msdynmkt_journeyevent | Local | Local | Local | Local | Local |
| msdynmkt_journeyoptimizationcount | Local |  |  |  |  |
| msdynmkt_journeyrunparameter | Local |  |  |  |  |
| msdynmkt_journeysetting | Local | Local | Local | Local | Local |
| msdynmkt_journeytemplate | Local | Local | Local | Local | Local |
| msdynmkt_JourneyWorkflowMapping | Local | Local | Local | Local | Local |
| msdynmkt_keyword | Local | Local | Local | Local | Local |
| msdynmkt_linkmobilitychannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_linkmobilitychannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_marketingfieldsubmission | Local |  |  |  |  |
| msdynmkt_marketingform | Local | Local | Local | Local |  |
| msdynmkt_marketingformfield | Local |  |  |  |  |
| msdynmkt_marketingformsubmission | Local |  |  |  |  |
| msdynmkt_marketingformtemplate | Local |  |  |  | Local |
| msdynmkt_matchingstrategy | Local | Local | Local |  | Local |
| msdynmkt_matchingstrategyattribute | Local |  |  |  |  |
| msdynmkt_mobileapp | Local |  |  |  |  |
| msdynmkt_mobileappchannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_mobileapplication | Global | Global | Global | Global | Global |
| msdynmkt_mobiledevice | Local | Local | Local | Local | Local |
| msdynmkt_mocksmsproviderchannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_mocksmsproviderchannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_optimizationcustomercount | Global |  |  |  |  |
| msdynmkt_optimizationdecision | Global |  |  |  |  |
| msdynmkt_predefinedplaceholder | Local | Local | Local | Local | Local |
| msdynmkt_preferencecenter | Global | Local | Local | Global | Global |
| msdynmkt_preferencecenterlink | Global | Global | Global | Global | Global |
| msdynmkt_purpose | Global | Local | Local | Global | Global |
| msdynmkt_pushdeviceregistrationresult | Local | Local | Local | Local | Local |
| msdynmkt_pushmobiledevice | Local | Local | Local | Local | Local |
| msdynmkt_pushnotification | Local | Local | Local | Local | Local |
| msdynmkt_qrcodestyle | Local | Local | Local | Local | Local |
| msdynmkt_quiettimesetting | Local |  |  |  |  |
| msdynmkt_richfragment | Global |  |  |  |  |
| msdynmkt_segment | Local | Local | Local | Local | Local |
| msdynmkt_segmentdefinition | Local | Local | Local | Local | Local |
| msdynmkt_segmentexecution | Local | Local | Local | Local | Local |
| msdynmkt_segmentusage | Local | Local | Local | Local | Local |
| msdynmkt_sms | Local | Local | Local | Local | Local |
| msdynmkt_smsphonenumber | Global |  |  | Global | Global |
| msdynmkt_submitbutton | Local |  |  |  |  |
| msdynmkt_tag | Local | Local | Local | Local | Local |
| msdynmkt_telesignchannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_telesignchannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_textfragment | Global |  |  |  |  |
| msdynmkt_topic | Global | Local | Local | Global | Global |
| msdynmkt_trackingcontext | Global |  |  |  |  |
| msdynmkt_twiliochannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_twiliochannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_utmtracking | Local | Local | Local | Local | Local |
| msdynmkt_vibeschannelinstance | Local | Local | Local | Local | Local |
| msdynmkt_vibeschannelinstanceaccount | Local | Local | Local | Local | Local |
| msdynmkt_video | Global |  |  |  |  |
| msdynmkt_virtualdomain | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasource | Global |  |  |  |  |
| msdynmkt_virtualdomaindatasourcev2 | Global |  |  |  |  |
| msdynmkt_virtualsegment | Global |  |  |  |  |
| msdynmkt_virtualsegmentdatasource | Global |  |  |  |  |
| msgdpr_gdprconfiguration | Global |  |  |  |  |
| NewsArticle | Global |  |  |  |  |
| Note | Local | Local | Local | Local | Local |
| Opportunity | Local | Local | Local | Local | Local |
| OpportunitySalesProcess | Global | Global | Global | Global | Global |
| OptionSet | Global |  |  |  |  |
| Organization | Global |  |  |  |  |
| OrganizationSetting | Global |  |  |  |  |
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
| SharePointData | Global | Global | Global |  |  |
| SharePointDocument | Global |  |  |  |  |
| SharePointDocumentLocation | Global | Global | Global | Global | Global |
| SharePointSite | Local |  |  |  | Local |
| SocialProfile | Local | Local | Local | Local | Local |
| Solution | Global |  |  |  |  |
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
| WebResource | Global |  |  |  |  |
| WebWizard | Global |  |  |  |  |
| WizardAccessPrivilege | Global |  |  |  |  |
| WizardPage | Global |  |  |  |  |
| Workflow | Global | Local | Local | Local | Global |
| WorkflowSession | Global | Local | Local | Local |  |
