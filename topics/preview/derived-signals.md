---
title: Create and export refined events
author: ruthaisabokhae
description: How to create and export refined events
ms.author: ruthai
ms.date: 07/31/2020
ms.service: product-insights
ms.topic: conceptual
robots: noindex,nofollow
---

# Create and export refined events

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

A refined event is a virtual view of a base event. It is generally used for reducing the scope of a base event for export or for cleaning up an event that contains properties that aren't necessary for exposure or export.

You can define refined events by removing and adding properties or filtering events based on property values.

## Create a refined event

There are three ways to create a refined event from a base event. Start by navigating to **Admin** > **Data** > **Events**, and then choose one of the following options:

- Select **+ Add events** and choose **Create refined event**.
- Select **...** from the table row containing a base event, and then select **Create refined event** from the drop-down menu.
- Select a base event to open a detailed view, and then select **Create a refined event** from the top menu.

## Modify a refined event

Once created, you are taken to a detailed view of your new refined event. By default, this event has the same properties as your base event.

### Add and remove properties

From the detailed view of your refined event, select **Add and remove properties** to open the **Edit properties** pane. Use the check boxes to indicate the properties that you want to show and the ones you want to hide. Select **Confirm** to apply your selection.

### Rename properties

From the detailed view of your refined event, select the arrow next to a property, and then select **Edit name** from the drop-down menu. Enter a new name and select **Confirm** to apply your changes.

> [!TIP]
> Renaming doesn't change the initial property. It creates a copy with a new name and hides the original from view. You can use the **Add and remove** properties menu to access the original property.

## Filter properties

From the detailed view of your refined event, select the arrow next to a property, and then select **Add filters** from the drop-down menu.

Select **+ Add filter** and choose an operation and a value. If you add multiple filters to an event, they are connected with a logical "AND" operator. Select **Confirm** to apply the filters.

You see a filter icon next to the property's name in the detailed view if filters are successfully added.

## Export a refined event

Events, including refined events, can be exported to an external storage.

From the **Events** page, select **...** next to the event you want to export and select **Export** from the drop-down menu. You are guided through the five steps of export creation:

1. Provide a **Name** for the export.
2. Select an event for export and an export cadence. The cadence informs how often an immutable folder with your event's information is created in Azure Data Lake Storage.
3. Select the format for your export.
4. Specify the Azure Data Lake Storage location and your credentials.
5. Review and confirm your selections.

Once you've set up an export, it can be viewed by navigating to **Admin** > **Data** > **Exports**. Use the **...** selections on the page to edit or delete an existing export.
