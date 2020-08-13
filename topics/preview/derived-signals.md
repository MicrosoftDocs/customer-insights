---
title: Create and export derived events
author: ruthaisabokhae
description: How to create and export derived events
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Create and export derived events

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

A derived event is a virtual view of a base event. These are generally used for scoping down a base event for export, or for cleaning up a event containing properties that aren't necessary for exposure or export.

Users can define derived events by removing and adding properties, as well as filtering events based on property values.

## Create a derived event

There are three ways to create a derived event from a base event. Start by navigating to **Admin** > **Data** > **Events**, then choose any one of the following options:

- Select **+ Add events** and choose **Create derived event**.
- Select **...** from the table row containing a base event, then select **Create derived event** from the dropdown menu.
- Select the a base event to open a detailed view, then select **Create a derived event** from the top menu.

## Modify a derived event

Once created, you'll be taken to a detailed view of your new derived event. This event will have the same properties as your base event by default.

### Add and remove properties

From the detailed view of your derived event, select **Add and remove properties** to open the **Edit properties** pane. Use the checkboxes to indicate which properties you want to show and which ones you want to hide. Select **Confirm** to apply your selection.

### Rename properties

From the detailed view of your derived event, select the arrow next to a property, then select **Edit name** from the dropdown menu. Enter a new name and select **Confirm** to apply your changes.

> [!TIP]
> Renaming doesn't change the initial property. Instead, it creates a copy of the original with a new name, and then hides the original from view. If you want to access the original property, you can find it using the **Add and remove** properties menu.

## Filter properties

From the detailed view of your derived event, select the arrow next to a property, then select **Add filters** from the dropdown menu.

Select **+ Add filter** and choose an operation and a value. If you add multiple filters to a event, they will be connected with a logical "AND" operator. Select **Confirm** to apply the filters.

You'll see a filter icon next to the property's name in the detailed view if filters are successfully added.

## Export a derived event

Events, including derived events, can be exported to an external storage.

From the **Events** page, select **...** next to the event you want to export and select **Export** from the dropdown menu. You will be guided through the five steps of export creation:

1. Provide a **Name** for the export.
2. Select a event for export, and an export cadence. The cadence informs how often an immutable folder with your event's information will be created in Azure Data Lake Storage (ADLS).
3. Select the format for your export
4. Specify the ADLS location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, it can be viewed by navigating to **Admin** > **Data** > **Exports**. Use the **...** selections on this page to edit or delete an existing export as desired.
