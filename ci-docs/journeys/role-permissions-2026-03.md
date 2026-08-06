---
title: Permission changes in the March 2026 release (version 1.1.62960.43)
description: Out-of-the-box role permissions added, removed, or updated in the March 2026 release of Customer Insights - Journeys are documented in this changelist.
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

# Permission changes in the March 2026 release (version 1.1.62960.43)

This article details the permission changes introduced in the **March 2026 release (version 1.1.62960.43)** for the out-of-the-box roles in Customer Insights - Journeys. For background on how to use this changelist to keep custom roles in sync, see [Permission changes in each release](role-permissions.md). *BU* (used throughout this article) stands for *business unit*.

This changelist is the first one published for this documentation. It reflects a comparison against the previously published Learn page for roles and permissions, so some entries might be marked as **Added** or **Removed** even when no functional change occurred. An **Added** entry might indicate a permission that already existed but was previously undocumented. Similarly, a **Removed** entry might reflect a correction to earlier documentation rather than an actual removal of a permission.

## Role-wise changes (versus previously published documentation)

---

## Table of contents

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

## Summary of changes

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

## Role: Event Administrator

**Role identifier:** {a31a2242-bf8f-e611-80d7-00155d4b201d}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 5 | 25 |
| Removed | 0 | 0 |
| Updated | 1 | 1 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Global | Global | Global | Global | Global |
| msevtmgt_eventregistrationsettings | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_integrationconfiguration | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_paymentprovider | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_powerpageswebsite | Organization | Organization | Organization | Organization | Organization |

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Workflow |  |  |  |  | (added) → Organization |

---

## Role: Event Administrator (BU level)

**Role identifier:** {07d52deb-3b54-4203-b3cf-35efe4350f82}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 5 | 25 |
| Removed | 0 | 0 |
| Updated | 1 | 1 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_eventregistrationsettings | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_integrationconfiguration | Deep | Deep | Deep | Deep | Deep |
| msevtmgt_paymentprovider | Organization | Organization | Organization | Organization | Organization |
| msevtmgt_powerpageswebsite | Deep | Deep | Deep | Deep | Deep |

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| Workflow |  |  |  |  | (added) → Organization |

---

## Role: Event Planner (BU level)

**Role identifier:** {9d0bcbb3-75d8-4496-b2fb-62d0a9cb902f}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 4 | 17 |
| Removed | 0 | 0 |
| Updated | 45 | 156 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msevtmgt_eventregistrationcustomfield | Local | Local | Local | Local | Local |
| msevtmgt_integrationconfiguration | Local | Local | Local | Local | Local |
| msevtmgt_paymentprovider | Organization |  |  |  | Organization |
| msevtmgt_powerpageswebsite | Local | Local | Local | Local | Local |

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in this release compared to previous documentation)

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

## Role: Lead Score Modeler

**Role identifier:** {d1fd2176-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 0 | 0 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

_None_

### Changelist-2 Removed (Tables and privileges that the previous documentation included but the current release no longer includes)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

_No changes._

---

## Role: Lead Score Modeler (BU level)

**Role identifier:** {3b30e84e-3ec6-4aa2-9417-b569f0d0284d}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 2 | 6 |
| Removed | 6 | 6 |
| Updated | 6 | 24 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_Localleadtoopportunity | Deep | Deep | Deep | Deep | Deep |
| msdynmkt_featureconfiguration | Global |  |  |  |  |

### Changelist-2 Removed (Tables and privileges that the previous documentation included but the current release no longer includes)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| AppModule | Global |  |  |  |  |
| PluginAssembly | Global |  |  |  |  |
| PluginType | Global |  |  |  |  |
| SdkMessage | Global |  |  |  |  |
| SdkMessageProcessingStep | Global |  |  |  |  |
| SdkMessageProcessingStepImage | Global |  |  |  |  |

### Changelist-3 Updated (Privileges that changed in this release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdyncrm_leadscore_v2 |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdyncrm_leadscoremodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entitygradedistribution |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entityscoredistribution |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_entityscoringmodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |
| msdynmkt_leadqualificationmodel |  | (added) → Deep | (added) → Deep | (added) → Deep | (added) → Deep |

---

## Role: Lead Score Viewer

**Role identifier:** {32e87eb4-c85c-e711-80fe-000d3a297db2}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 0 | 0 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

_None_

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

_No changes._

---

## Role: Lead Score Viewer (BU level)

**Role identifier:** {afc2cc8c-a26f-41c1-99a3-4510003a1878}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 1 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| msdynmkt_featureconfiguration | Global |  |  |  |  |

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in this release compared to previous documentation)

_No changes._

---

## Role: Marketing Manager - Business

**Role identifier:** {bf157a3a-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 24 | 57 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

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

### Changelist-2 Removed (Tables and privileges that were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

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

## Role: Marketing Manager (BU level) - Business

**Role identifier:** {dd84f17f-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 8 | 14 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

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

### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

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

## Role: Marketing Professional - Business

**Role identifier:** {ce995e5a-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 19 | 44 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

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

### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

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

## Role: Marketing Professional (BU level) - Business

**Role identifier:** {6d63ebe3-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 13 | 40 |
| Removed | 0 | 0 |
| Updated | 4 | 6 |

### Changelist-1 Added (Tables and privileges that exist in the current release but weren't previously documented)

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

### Changelist-2 Removed (Tables and privileges were previously documented but are no longer in the release)

_None_

### Changelist-3 Updated (Privileges that changed in the current release compared to previous documentation)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** |
|---|---|---|---|---|---|
| WorkflowSession |  |  |  |  | (added) → Local |
| msdynmkt_featureconfiguration | Local → Global |  |  |  |  |
| msdynmkt_marketingform |  |  |  |  | (added) → Local |
| msdynmkt_marketingformtemplate |  | (added) → Local | (added) → Local | (added) → Local |  |

[!INCLUDE [footer-include](./includes/footer-banner.md)]
