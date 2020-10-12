---
title: Created and modify refined events
description: How to create and modify refined events
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 10/12/2020
ms.service: product-insights
ms.topic: conceptual
ms.manager: shellyha
---

# Create and modify refined events

[!INCLUDE [cc-beta-prerelease-disclaimer]( ../includes/cc-beta-prerelease-disclaimer.md)]

A refined event is a virtual view of a base event. Generally, use refined events to reduce the scope of a base event for export or to remove properties that aren't necessary for exposure or export.

You can define refined events by removing and adding properties or by filtering events based on property values.

## Create a refined event

There are three ways to create a refined event from a base event. Select **Admin**> **Data** > **Events** and choose one of the following options:

- Select **+ Add events** and choose **Create refined event**.
- Select **...** from the table row containing a base event, and then select **Create refined event** from the drop-down menu.
- Select a base event to open a detailed view, and then select **Create a refined event** from the top menu.

## Modify a refined event

Once created, you're taken to a detailed view of your new refined event. By default, this event has the same properties as your base event.

### Add and remove properties

1. From the detailed view of your refined event, select **Add and remove properties** to open the **Edit properties** pane. 
2. Use the check boxes to select the properties that you want to show and the ones you want to hide. 
3. Select **Confirm** to apply your selection.

### Rename properties

1. From the detailed view of your refined event, select the arrow next to a property, and then select **Edit name** from the drop-down menu. 
2. Enter a new name and select **Confirm** to apply your changes.

> [!TIP]
> Renaming doesn't change the initial property. It creates a copy with a new name and hides the original from view. You can use the **Add and remove** properties menu to access the original property.

## Filter properties

1. From the detailed view of your refined event, select the arrow next to a property, and then select **Add filters** from the drop-down menu.
2. Select **+ Add filter** and choose an operation and a value. If you add multiple filters to an event, they're connected with a logical "AND" operator. 
3. Select **Confirm** to apply the filters.

You see a filter icon next to the property's name in the detailed view if filters are successfully added.
