---
title: Permission changes overview
description: Permission changes overview for out-of-the-box roles in Customer Insights - Journeys are documented by release, so you can keep custom roles up to date.
ms.date: 08/06/2026
ms.topic: article
author: vinayd
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Permission changes overview

This article details permission changes for the out-of-the-box roles in Customer Insights - Journeys. Whether you're an administrator configuring roles or a user checking your access level, use this article as your reference for what each role can do.

> [!NOTE]
> The content and structure of this page changed significantly since April 2026. If you used this page to keep custom roles aligned with out-of-the-box roles, review the entire article to understand what changed and how role updates are now documented.

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

*BU* stands for *business unit*. Roles marked "(BU level)" are scoped to a single business unit rather than the entire organization.

## How to use information in this page

If your organization uses custom roles based on out-of-the-box roles, with specific privileges added, removed, or changed to match your business needs, you need to keep those custom roles in sync as the product evolves. Out-of-the-box roles can change with each release when new capabilities are added or existing capabilities are updated. Review the [Release-wise changes to roles and privileges](#release-wise-changes-to-roles-and-privileges) section regularly and apply the documented changes to your custom roles.

Earlier versions of this article listed every privilege for each role. That format was difficult to maintain and made it hard to identify what changed between releases. Starting with the March 2026 release, this article uses a changelist format that documents only the differences from one release to the next. We're also now documenting privileges for all eight actions (previously, we documented only five actions: Read, Write, Create, Append, AppendTo, Delete).

Here's how the information is organized:

- **[June 2026 release (version 1.2.437.94)](role-permissions-2026-06.md)**: Changelist of differences introduced in the June 2026 release.
- **[May 2026 release (version 1.1.65002.146)](role-permissions-2026-05.md)**: Changelist of differences introduced in the May 2026 release.
- **[April 2026 release (version 1.1.64196.86)](role-permissions-2026-04.md)**: Changelist of differences introduced in the April 2026 release.
- **[March 2026 release (version 1.1.62960.43)](role-permissions-2026-03.md)**: Changelist of differences introduced in the March 2026 release compared to the previously published documentation.
- **[Baseline (pre-March 2026)](role-permissions-baseline.md)**: The last published version of this page, documenting all 11 roles and their privileges for five actions. Use this section as a reference if you need to verify your custom roles against the full privilege set before the changelist format was adopted.

To keep your custom roles in sync, first align them with the documented baseline. Then apply each release's permission changes, up through your current release, to bring your roles up to date. After that, check this page after every release for new changes to apply.

## How to check privileges for any role

For the most accurate and up-to-date privilege information, check roles directly in the application. Follow the steps in [Security roles and privileges for Dataverse](/power-platform/admin/security-roles-privileges) to find configured roles and their privileges.

Dataverse security roles combine an **action** (for example, Read or Write) with an **access scope** that defines how broadly that action applies across your organization.

These scopes are documented as **Basic**, **Local**, **Deep**, and **Global**. In the Power Platform admin center, the same concepts appear with the following labels:

- **User → Basic**: Access only to records the user owns or that are shared with them.
- **Business → Local**: Access to records owned by users in the same business unit.
- **Parent: Child Business Unit → Deep**: Access to records in the user's business unit and all subordinate business units.
- **Organization → Global**: Access to all records across the entire environment, regardless of business unit.

## Release-wise changes to roles and privileges

This section is updated after each release to note changes, if any, to out-of-the-box roles and privileges. Each release is documented on its own page:

- [June 2026 release (version 1.2.437.94)](role-permissions-2026-06.md)
- [May 2026 release (version 1.1.65002.146)](role-permissions-2026-05.md)
- [April 2026 release (version 1.1.64196.86)](role-permissions-2026-04.md)
- [March 2026 release (version 1.1.62960.43)](role-permissions-2026-03.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]
