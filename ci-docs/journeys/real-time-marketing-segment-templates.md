---
title: Create and use segment templates
description: Create segments from built-in or custom templates in Dynamics 365 Customer Insights - Journeys, and add placeholders to guide users through reusable queries.
ms.date: 10/23/2026
ms.topic: how-to
author: udag
ms.author: udag
search.audienceType:
  - admin
  - customizer
  - enduser
ai-usage: ai-assisted
---

# Create and use segment templates

Segment templates give you a reusable starting point for building audiences in Dynamics 365 Customer Insights - Journeys. Choose a built-in template for a common scenario, or save your own segment query as a custom template. Add placeholders with hint text to show users which values to enter each time they create a segment.

## Turn on segment templates

Check that **Segment templates** is **On** for your environment. If it's **Off**, ask an administrator to enable it.

If the switch is off, an administrator can enable it with these steps:

1. Go to **Settings** > **Overview** > **Feature switches**.
1. Under **Segmentation**, set **Segment templates** to **On**.
1. Select **Save** in the upper-right corner.

> [!div class="mx-imgBorder"]
> :::image type="content" source="media/real-time-marketing-segment-templates-feature-switch.png" alt-text="Screenshot of the Segment templates feature switch turned on and its description.":::

For more information, see [Use feature switches to enable or disable optional and preview features](admin-feature-switches.md).

## Create a segment from a template

Start from the template gallery to create a segment with an existing query.

1. Go to **Audience** > **Segments** and select **New Segment**.
1. In **Create new segment**, choose **Gallery** for built-in templates or **Custom templates** for templates created in your organization.

   > [!div class="mx-imgBorder"]
   > :::image type="content" source="media/real-time-marketing-segment-templates-gallery.png" alt-text="Screenshot of the segment template gallery showing the nine built-in templates in list view.":::

1. Select a template and review its details, including its **Audience**.
1. Select **Select** to open a new, unsaved **Draft** segment. The segment uses the template's name and target audience.
1. Enter a descriptive **Name** for your segment.
1. Complete any blank condition values and adjust the query for your audience.
1. Select **Save**.

The saved segment remains a draft. For more information about reviewing a segment and making it ready to use, see [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md).

## Built-in segment templates

The **Gallery** tab includes the following templates. The **Clicked an email** and **Opened a form but did not submit** templates each have separate contact and lead versions, so the gallery has nine entries for these seven template names.

| Template | Audience | Starting query |
|---|---|---|
| Accounts to primary contacts | Contact | Filter accounts by account attributes, and find the primary contact for each account. |
| Attended a session | Contact | Find contacts who attended a session. |
| Attended an event | Contact | Find contacts with a recorded check-in for the selected event within the configured time window. The default is the last 28 days. |
| Birthday within the next 5 days | Contact | Review the birth date condition before using this template. |
| Clicked an email | Contact or Lead | Find contacts or leads who clicked a link in a marketing email during a specified time frame. |
| Hold a pass for event | Contact | Find contacts who hold a pass for an event. |
| Opened a form but did not submit | Contact or Lead | Find contacts or leads with a recorded visit to the selected form and no recorded submission of that same form within the configured time windows. Both default to the last 28 days. |

When you use **Opened a form but did not submit**, choose the same form in both groups and review both time windows.

## Create a custom segment template

Start with a query-based segment whose conditions you want to reuse. For example, create a contact segment with **Status** set to **Active** and **Address 1: City** set to **Seattle**, using the **Is** operator for both conditions.

> [!NOTE]
> Static member lists aren't supported in segment templates.

1. Go to **Audience** > **Segments** and open the segment.
1. Select the arrow next to **Save**, and then select **Save as template**.

   > [!div class="mx-imgBorder"]
   > :::image type="content" source="media/real-time-marketing-segment-templates-save-menu.png" alt-text="Screenshot of the arrow next to Save expanded to show the Save as template command.":::

1. In **Quick Create: Segment Definition Template**, enter a descriptive **Name**, such as **Regional audience**.
1. Enter a **Description** that explains how to use the template. For example, enter **Active contacts in a city. Choose the city when you create a segment.**
1. Review the required **Owner**, which is filled in by default, and optionally add a **Label**.

   > [!div class="mx-imgBorder"]
   > :::image type="content" source="media/real-time-marketing-segment-templates-details.png" alt-text="Screenshot of the template details form with the Regional audience name, owner, and description.":::

1. Select **Save and Close**.

The custom template is saved, and you return to the original segment. To add placeholders or change the template's query, open it from **Assets** > **Templates** as described in the next section.

## Add placeholders to a custom template

Use hint text to explain what users need to enter in a condition. In the **Regional audience** example, leave the city value blank and add a hint so users can choose a different city for each segment.

> [!IMPORTANT]
> Adding hint text doesn't clear an existing condition value. Clear the value separately if you want the template to leave it blank.

1. Go to **Assets** > **Templates**.
1. Select the **Segment** tile.
1. Select the **Custom templates** tab.
1. Open your template, such as **Regional audience**.
1. In the **Address 1: City** condition, select the ellipsis (**Show options**), and then select **Change hint text**.

   > [!div class="mx-imgBorder"]
   > :::image type="content" source="media/real-time-marketing-segment-templates-placeholder-menu.png" alt-text="Screenshot of the city condition's options menu showing Change hint text.":::

1. In the **Hint text** dialog, enter **Enter the city to target, for example Seattle**.

   > [!div class="mx-imgBorder"]
   > :::image type="content" source="media/real-time-marketing-segment-templates-hint-text.png" alt-text="Screenshot of the Hint text dialog with guidance to enter a city, such as Seattle.":::

1. Select **Save** in the dialog.
1. Clear the existing **Address 1: City** value so that the field is blank.
1. Select **Save** on the template's command bar.

The template keeps **Status** set to **Active** and shows the hint in the blank city field.

> [!div class="mx-imgBorder"]
> :::image type="content" source="media/real-time-marketing-segment-templates-placeholder.png" alt-text="Screenshot of the Regional audience template with Status set to Active and a hint in the blank city field.":::

## Use a custom template with placeholders

Create a segment from your custom template and fill in the values for your audience.

1. Go to **Audience** > **Segments** and select **New Segment**.
1. On the **Custom templates** tab, select **Regional audience**.
1. Select **Select** to open a new draft segment.
1. Change the **Name** to **Seattle contacts**.
1. Enter **Seattle** in the blank **Address 1: City** field identified by the hint. Leave **Status** set to **Active**.
1. Review the query and select **Save**.

The new **Seattle contacts** segment is saved as a draft with the completed query. The **Regional audience** template remains available to create more segments.

> [!div class="mx-imgBorder"]
> :::image type="content" source="media/real-time-marketing-segment-templates-filled.png" alt-text="Screenshot of the Seattle contacts draft with Status set to Active and the city set to Seattle.":::

## Related content

- [Segmentation overview](real-time-marketing-segments.md)
- [Build segments in Customer Insights - Journeys](real-time-marketing-build-segments.md)
- [Improve targeting using interaction data in segments](real-time-marketing-redesigned-segment-builder.md)
