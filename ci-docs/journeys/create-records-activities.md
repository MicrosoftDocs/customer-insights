---
title: Create records and activities from journeys (preview)
description: Dynamics 365 Customer Insights journeys let you create any record or activity automatically from customer actions. Discover how to optimize engagement today.
ms.date: 04/06/2026
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
> The system only displays entities that have a relationship with a contact or lead and that you have permission to create. If you don't see the entity you need, check with your administrator to ensure that the entity has a relationship with contact or lead entities and that you have the necessary permissions to create records for that entity type.

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

### Configure record ownership and assignment

For entities that support ownership (such as phone calls, tasks, leads, and opportunities), specify who should own the created record.

- **Contact/Lead owner**: The owner of the contact or lead flowing through the journey is assigned as an owner of the created entity.
- **Parent account owner**: If the contact or lead flowing through the journey has a relationship with the parent account, the owner of the parent account is assigned as an owner of the created entity. If this option is selected and the value can’t be resolved, the contact or lead owner is assigned instead. 
- **Specific user**: Select a specific static user or team to be assigned as an owner of the created entity.
- **Dynamic value**: Select a dynamic binding to resolve an owner to be assigned to the created entity. If this option is selected and the value can’t be resolved, the contact or lead owner is assigned.

For leads and opportunities, Dynamics 365 Sales assignment rules take precedence over the owner specified in the journey. This precedence ensures that the system routes leads and opportunities according to your sales team's territory assignments and distribution rules.

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

- Ask your administrator to confirm the entity has a relationship to the contact or lead.
- Verify that you have **Create** privileges for the entity (and any related entities required by business rules). Verify that you have the necessary permissions to create records for the type of entity.
- If you’re an administrator, create the required relationship between the entity and the contact or lead, then try again.

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