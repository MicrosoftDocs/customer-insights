---
title: Create and modify refined events
description: How to create and modify refined events.
ms.reviewer: mhart
ms.author: jeffhar
author: mochimochi016
ms.date: 04/30/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create and modify refined events

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]


An event is data that represents user behavior, like activity on a website.

- A *base* event records when a user views a page (view event) or interacts with content (action event).
- A *refined* event is a virtual view of a base event. You define refined events by removing and adding properties or by filtering events based on property values.

Use refined events to reduce the scope of a base event for [export](export-events.md) or to remove properties that aren't necessary for exposure.

## Create refined events

There are three ways to create a refined event from a base event. 

1. Go to **Data**> **Events** and choose one of the following options:
    - Select **New events** and then select **Create refined events**.
    - Select a base event to open a detailed view and select **Create refined events** from the top menu.
    - Select **More [...]** to open the shortcut menu for a base event. Then select **Create refined events**.
    
    :::image type="content" source="media/create-refined-events-options.png" alt-text="Options to create refined events":::

1. In the **Create refined events** dialog, enter the following information:

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

You can change the name and the properties of a refined event.

### Edit event name

1. Go to **Data** > **Events**. 
1. Select **More [...]** for an event and select **Edit name**.
1. Update the event name and select **Rename**.

### Edit selected properties

1. Go to **Data** > **Events** and select the refined events to open the detailed view.
1. Select **Add and remove properties**. 
1. Edit the selection of the check boxes.
1. Select **Confirm** and then **Save** to apply the changes.

For information about exporting events, see [Export events](export-events.md).
[!INCLUDE[footer-include](../includes/footer-banner.md)]
