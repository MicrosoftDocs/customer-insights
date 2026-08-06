---
title: Permission changes in the April 2026 release (version 1.1.64196.86)
description: The April 2026 release of Customer Insights - Journeys added new table permissions to four Marketing roles; review the details in this changelist.
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

# Permission changes in the April 2026 release (version 1.1.64196.86)

This article details the permission changes introduced in the **April 2026 release (version 1.1.64196.86)** for the out-of-the-box roles in Customer Insights - Journeys. For background on how to use this changelist to keep custom roles in sync, see [Permission changes in each release](role-permissions.md). *BU* (used throughout this article) stands for *business unit*.

## Role-wise changes (versus the March 2026 release)

---

## Summary of changes

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

## Role: Marketing Manager - Business

**Role identifier:** {bf157a3a-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Global | Global | Global | Global | Global | Global | Global | Global |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

## Role: Marketing Manager (BU level) - Business

**Role identifier:** {dd84f17f-cde8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Deep | Deep | Deep | Deep | Deep | Deep | Deep | Deep |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

## Role: Marketing Professional - Business

**Role identifier:** {ce995e5a-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Global | Global | Global | Global | Global | Global | Global | Global |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

## Role: Marketing Professional (BU level) - Business

**Role identifier:** {6d63ebe3-cee8-e611-80d8-00155d4b205a}

| Metric | Tables | Privileges |
|---|---|---|
| Added | 1 | 8 |
| Removed | 0 | 0 |
| Updated | 0 | 0 |

### Changelist-1 Added (Tables and privileges that exist in the current release but not in the previous release)

| **Table name** | **Read** | **Write** | **Create** | **Append** | **AppendTo** | **Delete** | **Assign** | **Share** |
|---|---|---|---|---|---|---|---|---|
| msdynmkt_agentsetting | Local | Local | Local | Local | Local | Local | Local | Local |

### Changelist-2 Removed (Tables and privileges in the previous release but no longer in the current release)

_None_

### Changelist-3 Updated (Privileges that have changed in the current release compared to the previous release)

_No changes._

---

[!INCLUDE [footer-include](./includes/footer-banner.md)]
