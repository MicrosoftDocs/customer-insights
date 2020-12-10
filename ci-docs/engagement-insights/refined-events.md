---
title: Create and modify refined events
description: How to create and modify refined events.
ms.reviewer: ruthai
ms.author: v-salash
author: pickwick129
ms.date: 12/03/2020
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create and modify refined events

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Events represent user behavior. A *base* event records when a user views a page (view event) or interacts with content (action event). A *refined* event is a virtual view of a base event. You define refined events by removing and adding properties or by filtering events based on property values.

Generally, use refined events to reduce the scope of a base event for [export](export-events.md) or to remove properties that aren't necessary for exposure.

## Create refined events

There are three ways to create a refined event from a base event. 

1. Go to **Admin**> **Data** > **Events** and choose one of the following options:
    - Select **New events** and then select **Create refined events**.
    - Select a base event to open a detailed view and select **Create refined events** from the top menu.
    - Select **...** to open the shortcut menu for a base event. Then select **Create refined events**.
    
    :::image type="content" source="media/create-refined-events-options.png" alt-text="Options to create refined events":::

1. In the events dialog, enter the following information:

- Select an event from the **Base events** dropdown if you're creating a new event.
- Enter a name in the **Refined events display name** box.
- Optionally, update the suggested **Actual name** without using spaces.

3. Select **Create** to apply your settings.

1. In the detailed view of your refined event, select **Add and remove properties** to open the **Edit properties** pane. 

1. Use the check boxes to select the properties that you want to show and the ones you want to hide. 
   :::image type="content" source="media/edit-properties-refined-events.png" alt-text="Edit properties for refined events":::

1. Select **Confirm** to apply your selection.

1. Select **Save** to save the configuration.

## Edit refined events

You can change the properties and the name of refined events.

### Edit event details

1. Go to **Admin**> **Data** > **Events**. 
1. Select **...** for an event and select **Edit details**.
1. Update the display name or the description of the event and select **Save**

### Edit selected properties

1. Go to **Admin**> **Data** > **Events** and select the refined events to open the detailed view.
1. Select **Add and remove properties**. 
1. Edit the selection of the check boxes.
1. Select **Confirm** and then **Save** to apply the changes.

## Manage properties of refined events

You can filter, rename, and remove properties of refined events.

1. Go to **Admin**> **Data** > **Events** and select the refined events to open the detailed view.
1. Select the arrow next to a property name and choose an option from the drop-down menu.
   :::image type="content" source="media/manage-properties-refined-event.png" alt-text="Edit options of refined events":::
1. Select **Save** to apply the changes.

> [!NOTE]
> Renaming doesn't change the initial property. It creates a copy with a new name and hides the original property from the view. Removing a property doens't delete the data, it hides the removed property from the view. Select **Add and remove properties** to access the properties and recover hidden properties.

### Filter property

1. Choose **Add filters** and choose an operation and a value. If you add multiple filters to an event, they're connected with a logical "AND" operator. 
1. Select **Confirm** to apply the filters.

You see a filter icon next to the property's name in the detailed view if filters are successfully added.

### Rename property

1. Choose **Edit name** to change the name of a property.
2. Enter a new name and select **Confirm** to apply your changes.

### Remove property

1. Choose **Remove property** to remove a property from the refined events.
