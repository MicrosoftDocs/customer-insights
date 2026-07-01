---
title: Create records and activities from journeys (preview)
description: Dynamics 365 Customer Insights journeys let you create any record or activity automatically from customer actions. Discover how to optimize engagement today.
ms.date: 06/30/2026
ms.topic: article
author: cmenesatti-m
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create records and activities from journeys (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Use journeys in Dynamics 365 Customer Insights - Journeys to automatically create Dataverse records in response to customer actions and engagement signals. Create any type of record or activity, including phone calls, tasks, leads, opportunities, and custom entities, directly from the journey canvas to drive timely follow-up and improve conversion rates.

For example, when a high-value lead downloads a whitepaper, you can automatically create a phone call activity assigned to a sales representative with all relevant context. This process ensures sales can follow up while the lead's interest is at its peak.

> [!NOTE]
> This feature currently works when orchestrating journeys on contacts and leads. It doesn't support Customer Insights - Data profiles.
>
> Users can only create records that have a relationship to lead or contact and that they have Create privileges to.
>
> Records related to event planning aren't supported.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Enable creating records and activities from journeys

To turn this feature on or off:

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Enable or disable the **Record creation (preview)** toggle inside the **Journey** section.

> [!NOTE]
> Like any preview feature, this feature is disabled by default. However, given that this is a change to an existing feature, if you previously had the **Lead and opportunity creation (preview)** toggle enabled, that is still respected.

> [!IMPORTANT]
> A new dedicated service role — **Create Record Role Extensible** — is now available for the **Create a record** tile. This role provides more granular control. The entity picker only shows tables and fields where both you (the journey publisher) and this role have the required permissions, so configuration issues surface at setup rather than at runtime.
>
> The **Marketing Service User Extensible** role continues to function. To take advantage of the improved visibility behavior, migrate privileges for any custom tables you previously configured on **Marketing Service User Extensible** to **Create Record Role Extensible**. See [Roles and permissions](#roles-and-permissions) for step-by-step instructions.

## Add a Create a record tile to your journey

To add the capability to create records to your journey:

1. In Customer Insights - Journeys, go to **Engagement** > **Journeys**.
1. Open an existing journey or select **+ New Journey** to create a new one.
1. On the journey canvas, select the plus sign **(+)** where you want to add the record creation step.
1. In the tile gallery, select **Create a record**.

:::image type="content" source="media/create-records-activities-tiles.png" alt-text="Screenshot of Dynamics 365 Add an action panel with Create a record tile highlighted for journey step selection." lightbox="media/create-records-activities-tiles.png":::

### Select the record type

After adding the **Create a record** tile, search for or scroll through the list of available entities and select the record type you want to create (for example, Phone Call, Task, Lead, Opportunity, or any custom entity). Records related to event planning aren't supported.

> [!TIP]
> The system only displays entities where both you (the journey publisher) and the **Create Record Role Extensible** service role have *Create* permission at business unit level or higher. If an entity or field is missing from the list, a message indicates that this is due to missing privileges and links to the documentation.
>
> If you don’t see the entity you need, ask your administrator to grant *Create* permission on that entity to both your security role and the **Create Record Role Extensible** role. To learn more, see [Why can’t I see a table in the list of tables for Create Record?](#why-cant-i-see-a-table-in-the-list-of-tables-for-create-record) below.

### Configure the required fields

After you select the entity type, the **Create a record** pane displays all required fields for that entity. Configure these fields to ensure you create records with essential information:

For each required field, choose whether to set a **Static value** or use **Dynamic content**:

- **Static value**: Enter a fixed value that is the same for all records the tile creates.
- **Dynamic content**: Select data from Dataverse to personalize each record based on the contact, lead, trigger, or related data.

:::image type="content" source="media/create-records-activities-configure.png" alt-text="Screenshot of Dynamics 365 Create a record pane for Phone call, showing required Subject field set with dynamic content." lightbox="media/create-records-activities-configure.png":::

> [!IMPORTANT]
> Required fields are displayed by default. To save and publish the journey, you must fill in all required fields.

### Add optional fields

To configure additional fields beyond the required ones:

1. In the **Create a record** pane, select **+ Add optional fields**.
1. In the searchable field list, find the field you want to add.
1. Select the field to add it to the configuration.
1. Configure the field value by using static content or dynamic content.
1. Repeat for all additional fields you want to configure.

The optional fields list includes all writable fields from the entity, including custom fields. The list excludes system fields (such as *Created On* and *Modified By*) and calculated fields because the system automatically populates them or they're read-only.

> [!NOTE]
> Fields you configure by using **+ Add optional fields** are saved per user, per session, not globally for all users.

> [!TIP]
> If the system can't resolve a dynamic content field at runtime (for example, if a contact doesn't have a phone number), the field is left empty.

> [!IMPORTANT]
> During the preview, when choosing a lead record type, a number of standard attributes such as `First Name` and `Last Name`, `Email`, `Address`, and more are pre-filled from the journey audience. These fields show as pre-filled in the Create a record side pane according to their settings (required versus more info).

### Configure record ownership and assignment

For entities that support ownership (such as phone calls, tasks, leads, and opportunities), specify who should own the created record.

- **Contact/Lead owner**: The owner of the contact or lead flowing through the journey is assigned as an owner of the created entity.
- **Parent account owner**: If the contact or lead flowing through the journey has a relationship with the parent account, the owner of the parent account is assigned as an owner of the created entity. If this option is selected and the value can’t be resolved, the contact or lead owner is assigned instead. 
- **Specific user**: Select a specific static user or team to be assigned as an owner of the created entity.
- **Dynamic value**: Select a dynamic binding to resolve an owner to be assigned to the created entity. If this option is selected and the value can’t be resolved, the contact or lead owner is assigned.

For leads and opportunities, Dynamics 365 Sales assignment rules take precedence over the owner specified in the journey. This precedence ensures that the system routes leads and opportunities according to your sales team's territory assignments and distribution rules.

## Roles and permissions

To create records from a journey using the new **Create Record Role Extensible** role, Dataverse requires permissions from two principals:

- **Journey publisher**: The user who publishes the journey. Their security role must include the required privileges on the target table.
- **Create Record Role Extensible**: The dedicated service role used by the Workflow service when the journey runs. This role must also hold the required privileges.

Record creation only succeeds if *both* principals pass all required permission checks.

### Built-in tables (Lead, Task, Opportunity, Phone Call)

For built-in tables, the **Create Record Role Extensible** role already includes the required privileges. No action is needed for the service role.

The journey publisher must have the following privileges on the target table:

| Privilege | Why it's needed |
|---|---|
| Create | Create and populate fields on the record |
| Append | Set lookup fields on the record |
| AppendTo | Allow other records to reference this record |
| Assign | Set the owner (ownerid) on the record |

Additionally, the journey publisher needs **AppendTo** on any entity referenced by lookup fields configured in the tile (for example, account, contact, transactioncurrency).

### Custom tables

Custom tables aren't included in the default **Create Record Role Extensible** role. You must manually add privileges for both the journey publisher and the service role.

For both the journey publisher’s security role and the **Create Record Role Extensible** role:

1. Go to **Settings** > **Security** > **Security Roles**.
1. Open the role.
1. On the **Custom Entities** tab, locate your custom table.
1. Set the following privileges to at least the business unit level: **Create**, **Append**, **AppendTo**, **Assign**.
1. For every lookup field on the custom table, also add **AppendTo** on the entity the lookup points to.
1. Save.

### Adding a custom lookup field to a built-in table

If you add a custom lookup field that references a table not already covered by the default role (for example, a new custom entity new_project), you must add **AppendTo** on that referenced entity to both the journey publisher’s security role and the **Create Record Role Extensible** role.

No changes are needed if the lookup field points to a standard entity already covered by the default role (such as account, contact, transactioncurrency, lead, task, opportunity, or phone call).

## Example use cases for creating records and activities

### Hand-off high value leads to sales

Create phone call activities for leads who perform high-value actions:

1. Create a trigger-based journey that starts when a lead submits a pricing request form.
1. (Optional) Add an attribute branch to assign phone calls to the appropriate team.
1. Add a **Create a record** tile and select **Phone Call**.
1. Select the appropriate user or team as **Owner**.
1. Set all the required fields and add any optional fields such as Regarding to give more context to sellers.

### View analytics for created records

After the journey is live and begins creating records, you can track its effectiveness through analytics that show created records and allow you to open them directly. If a record creation fails, you can also view details about the failure.

> [!IMPORTANT]
> Journey validation checks many common configuration issues, but it can’t validate all runtime business rules or customer specific customizations. As a result, a journey may publish successfully, but some create record actions can still fail when the journey runs. Publishing a journey doesn’t guarantee that all records will be created. You should test the journey with a sample audience and review execution results before using it with live data.

## Troubleshooting

### The entity I need doesn't appear in the entity list

This can happen for one of the following reasons:

- The entity doesn’t have a relationship with the contact or lead.
- The entity is related to event planning (not supported).
- You don’t have permission to create records for that entity.

**Resolution**:

- Confirm the entity has a relationship with the contact or lead. If not, ask your administrator to create the required relationship and try again.
-	Verify that both your security role and the **Create Record Role Extensible** role have **Create** permission on the entity at business unit level or higher. The entity picker only shows entities where both permission checks pass.
-	If your organization restricts the entity to specific roles, ask your administrator to update both roles accordingly. See [Roles and permissions](#roles-and-permissions) for step-by-step instructions.
-	Confirm that the entity isn't an event planning entity (prefix `msevtmgt`). Event planning entities aren't supported.

### Why can’t I see a table in the list of tables for Create Record?

To use a table in the **Create Record** tile, both you (the journey publisher) and the **Create Record Role Extensible** role must have **Create** permission on that table at business unit level or higher. If either permission is missing, the table is hidden from the picker and the user interface shows a message indicating that the item isn't visible due to missing privileges.

**Resolution**:

1. Open your `Dataverse environment` > **Settings** > **Security** > **Security Roles**.
1. Find the security role assigned to your user account.
1. Locate the table row. It may be under **Core Records**, **Custom Entities**, or another tab.
1. Set the **Create** column to at least the **Business Unit** level (the second filled circle).
1. Repeat the same steps for the **Create Record Role Extensible** role.

### Why can’t I see a lookup field for the selected table?

Lookup fields link the new record to an existing record in another table. To use a lookup field, both you and the **Create Record Role Extensible** role need two additional permissions:

- **Append** permission on the source table (the table you’re creating a record in) at business unit level or higher.
- **AppendTo** permission on the target table (the table the lookup field points to) at business unit level or higher.

If either permission is missing, the lookup field is hidden from the field picker and the user interface shows a message indicating that the field isn't visible due to missing privileges.

**Resolution**

1. Open your `Dataverse environment` > **Settings** > **Security** > **Security Roles**.
1. For both your security role and the **Create Record Role Extensible** role:
    - Find the source table row > set the **Append** column to at least **Business Unit** level.
    - Find the target table row > set the **AppendTo** column to at least **Business Unit** level.
1. Save both roles.

#### Why are Append and AppendTo needed?

In Dataverse, setting a lookup field creates a relationship link between two records. Dataverse requires **Append** permission to attach a child record to a parent, and **AppendTo** permission on the parent to accept the attachment. Without both, record creation fails at runtime when the journey runs.

### Records aren't created

A journey can publish successfully, but the **Create a record** action can still fail at runtime due to permissions, required data, business rules, or customer-specific customizations. Journey validation checks many common configuration issues before publish, but it can’t evaluate every condition enforced at runtime.

For example, validation might not account for:

- Business rules that run only during journey execution, and
- Custom plug-ins, workflows, or other customer-specific customizations.

Because of this, a journey can publish successfully and appear valid, but some records might not be created during execution. To confirm the cause, review journey execution details and validate your entity configuration and data.

**Resolution**:

- Review the journey execution details and logs for the **Create a record** step to see the specific error.
- Confirm required fields are configured and that runtime data exists for any dynamic content used.
- Test with a small audience and verify that the expected records are created before you publish to a production audience.

### Dynamic content fields are empty in created records

This can happen when the selected dynamic content path is incorrect or when the underlying data is blank for some contacts or leads.

**Resolution**:

- Re-check the selected dynamic content field and relationship path to ensure it points to the intended attribute.
- Test with a contact or lead where you know the field has a value, then compare results.
- Add default values or branches to handle contacts and leads with missing data.

## What changed from the *Create sales activities from lead signals* preview

Previously, this capability was limited to four predefined entity types with restricted fields. The enhanced feature provides access to any entity type related to contacts or leads, with full access to all required, optional, and custom fields. This flexibility unlocks countless scenarios that previously required custom development or third-party integrations.

If you previously used the *Create sales activities from lead signals* preview feature, be aware of the following changes:

- **Unified tile**: The four separate tiles (Phone Call, Task, Lead, Opportunity) are replaced by a single **Create a record** tile that supports any entity type.
- **Existing journeys**: Journeys that use the previous tiles continue to run. If you edit them, you must replace the old tiles with the new unified tile.
- **Templates**: Task templates aren't supported anymore. Use journey templates to preserve commonly used field configurations.
- **Branching**: Hardcoded status updates for phone calls and tasks are removed. Use standard if/then branches with Dataverse change detection instead.

## Related information

- [Journeys overview](journeys-overview.md)
- [Add an action in a journey](add-action.md)
- [Journey analytics](real-time-marketing-analytics.md)

[!INCLUDE [footer-include](./includes/footer-banner.md)]