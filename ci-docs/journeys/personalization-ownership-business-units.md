---
title: How record ownership and business units affect personalization
description: Learn how Dataverse record ownership, journey ownership inheritance, and business units determine whether personalization placeholders resolve or return empty values in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/13/2026
ms.topic: article
author: alfergus
ms.author: alfergus
ms.service: dynamics-365-customer-insights
ms.subservice: dynamics-365-customer-service-journeys
search.audienceType:
  - admin
  - customizer
  - enduser
---

# How record ownership and business units affect personalization

When a personalization placeholder returns an empty value, or a journey condition or inbound filter behaves as though a value is missing, the data might have been filtered out before evaluation. Preview and journey run-time can produce different results because they apply different rules. At journey run-time, **business unit scoping** is usually the cause. In preview, the likely cause is your Dataverse read access.

This article explains how personalization works in preview and at journey run-time so you can diagnose and resolve these issues. The guidance applies to content placeholders in emails, text messages, and push notifications; journey conditions and branches; inbound journey trigger filters; and dynamic values in record and task creation actions.

For help with other personalization issues, such as field-level security, race conditions, and customizations, see [Troubleshoot personalization](/troubleshoot/dynamics-365/customer-insights/journeys/personalization/troubleshoot-personalization).

## How identity affects personalization data access

To resolve a personalization placeholder, the system queries Dataverse for the value. Dataverse returns only rows that the calling **identity** can read. If that identity can't read a required row, the placeholder returns an empty value, which can affect the resulting content or condition. The identity depends on where the placeholder is evaluated:

- In **preview**, the system impersonates the signed-in user. Dataverse returns only the data that you can read based on your security roles, business unit, and field-level security.
- During **live journey execution**, the system uses the `Cxp Dataverse Datasource Services User` identity. Its `Service Reader` role allows it to read any Dataverse data in the environment. As a result, platform restrictions based on ownership, business unit, and role access levels don't limit run-time evaluation.

Because preview and live journey execution use different identities, personalization results can differ between them. If personalization works in preview but not in a live journey, check the journey's business unit scoping. If it doesn't work in preview, check whether your account has access to all required data.

## Two mechanisms that filter personalization data

An empty placeholder value can result from either of two filtering mechanisms:

1. **Dataverse platform security**: Determines which rows you can read during **preview**, when the system impersonates the signed-in user. Your security roles grant `Read` at one of four access levels: `User`, `Business Unit`, `Parent: Child Business Units`, or `Organization`. These levels follow the platform's business unit hierarchy, so preview can't use data that you can't read. During **live journey execution**, the `Cxp Dataverse Datasource Services User` has the `Service Reader` role and can read any Dataverse data in the environment. Therefore, platform security doesn't restrict live evaluation based on ownership, business unit, or role access level.
1. **Customer Insights - Journeys business unit scoping**: Applies an exact-match filter during **live journey execution**. It's the only ownership or business unit filter that affects live journeys, and it doesn't follow the parent or child business unit hierarchy. The rest of this article focuses on this behavior. For more information, see [Business unit support in real-time journeys](real-time-marketing-business-units.md).

Learn more about the platform model in [Security concepts in Microsoft Dataverse](/power-platform/admin/wp-security-cds) and [Security roles and privileges](/power-platform/admin/security-roles-privileges).

## How business unit scoping filters journey data

Business unit scoping applies only to journeys. It limits both the audience members a journey can process and the data that its personalization bindings can retrieve. When you enable scoping, Customer Insights - Journeys adds one exact-match constraint to the underlying Dataverse query based on the journey's ownership:

- The constraint matches either one **owner** or one **owning business unit**, never both.
- The system compares a single GUID for equality. When it scopes by business unit, it uses the journey's business unit and doesn't include child business units. Unlike Dataverse platform security, journey scoping doesn't traverse the business unit hierarchy.
- The field used for the match depends on the table's ownership type:
  - For **user-owned tables**, the system matches the record's **owner** or **owning business unit**.
  - For **business unit–owned tables**, it matches the record's **business unit**.
  - **Organization-owned tables** aren't filtered because they're shared across the organization.

If a record doesn't match the journey's scope, the system filters it out. The placeholder then returns an empty value, or the condition evaluates to *false*. This outcome applies even when the record belongs to a child business unit or the service user can read it through Dataverse platform security. Journey scoping always uses one exact owner or business unit match.

## How ownership models affect business unit scoping

How business unit scoping applies to a Dataverse record depends on its ownership model. A personalization path can include records from any of these models:

- **User-owned records.** A single user owns the record, and that user belongs to a business unit. Scoping matches the record's **owner** or **owning business unit**. If the user belongs to a different business unit than the journey, the record is filtered out, even when that business unit is a child of the journey's.
- **Team-owned records.** A team owns the record, and the team belongs to a business unit. Scoping matches the team's owning business unit against the journey's scope. Dataverse platform security can still prevent the signed-in user from reading the record during preview.
- **Organization-owned records.** These records aren't owned by a user or business unit. Journey scoping doesn't filter them because they're shared across the organization. During preview, the signed-in user still needs the table's platform **Read** privilege.

> [!NOTE]
> Changing a record's **owner** can also change its **owning business unit**. If you reassign a record to a user or team in a different business unit, the record might no longer match the journey's scope. Personalization can then stop resolving the record even though the service user still has permission to read it.

## How scoping applies across a personalization path

A personalization placeholder can follow relationships across multiple records to retrieve a value. This sequence is called a **traversal** or **multihop path**. For example: *Contact → parent account → account owner → owner's manager → manager phone number*.

Business unit scoping checks every user-owned or business unit–owned record in the path independently. Each record must match the journey's owner or business unit. If any record doesn't match, the traversal stops at that record and values later in the path resolve as empty.

For example, a contact might match the journey's business unit while its parent account belongs to a different business unit. In that case, the placeholder can't continue past the account. A mismatch can therefore occur several steps after the first record. Organization-owned records are exempt from journey scoping.

> [!IMPORTANT]
> Check every record in the full path, not only the first one. During live journey execution, every user-owned or business unit–owned record must match the journey's scope. During preview, your account must also have permission to read every record.

## Diagnose an ownership or business unit issue

1. **Map the full placeholder path.** List every table, relationship, and record from the starting record to the final column.
1. **Check ownership at every step.** Record the owner and owning business unit of each record in the path. Include records created by the journey, which inherit the journey's ownership.
1. **Identify where the issue occurs.** Preview uses the signed-in user's identity. Live journey execution uses the `Cxp Dataverse Datasource Services User` identity.
1. **Apply the correct check.** For a live journey issue, verify that every applicable record exactly matches the journey's owner or business unit. For a preview issue, verify that your account can read every record. The first record that fails either check is where the path breaks.
1. **Run a controlled live test.** Test with records that you know match the journey's scope. Don't rely only on preview because a placeholder can work there and still fail during live execution.

## Resolve ownership and business unit issues

Choose a mitigation that meets your security and privacy requirements:

- **Align record ownership with the journey's scope.** Ensure that every record the journey needs, including records it creates, has an owner or owning business unit that matches the journey's scope. Increasing platform `Read` access doesn't change this exact-match requirement during live execution.
- **Align the journey owner with the source data.** Assign the journey to a user in the same business unit as the required source records. This alignment keeps the audience members and personalization data within the journey's scope.
- **Review business unit scoping.** If the journey needs data from other business units, confirm that scoping is appropriate for the scenario. Child business units aren't included automatically. For configuration details, see [Business unit support in real-time journeys](real-time-marketing-business-units.md).
- **Set default values.** Add fallback values to personalized elements so messages remain complete when data is unavailable.

> [!NOTE]
> Field-level security is separate from ownership and business unit scoping. A protected column can return *null* even when the record is readable. If one field is empty but the rest of the record resolves, see [Override field-level security attributes](overriding-fls-attributes.md).

## See also

- [Troubleshoot personalization](/troubleshoot/dynamics-365/customer-insights/journeys/personalization/troubleshoot-personalization)
- [Override field-level security attributes](overriding-fls-attributes.md)
- [Business unit support in real-time journeys](real-time-marketing-business-units.md)
- [Customer Insights - Journeys service users](admin-users-licenses-roles.md#customer-insights---journeys-service-users)
- [Security concepts in Microsoft Dataverse](/power-platform/admin/wp-security-cds)
- [Security roles and privileges](/power-platform/admin/security-roles-privileges)
- [Create or edit business units](/power-platform/admin/create-edit-business-units)

[!INCLUDE [footer-include](./includes/footer-banner.md)]