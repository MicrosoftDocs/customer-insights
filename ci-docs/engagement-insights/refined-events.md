---
title: Create and modify events
description: How to create and modify events.
ms.reviewer: mhart
ms.author: jefhar
author: mochimochi016
ms.date: 10/01/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha
---

# Create and modify events

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

An event is data that represents user behavior, like activity on a website.

- A *base* event records when a user views a page (view event) or interacts with content (action event).
- A *refined* event is a virtual view of a base event. You define refined events by removing and adding properties or by filtering events based on property values.

## Prerequisites

In order to see events, your website data needs to first be conneceted to engagement insights with a code snippet. For more information, see [Install the web SDK on a website](instrument-website.md). 

    :::image type="content" source="media/new-events-connect-data.png" alt-text="Connect your data first.":::

## Create refined events

Use refined events to reduce the scope of a base event for [export](export-events.md) or to remove properties that aren't necessary for exposure.

> [!NOTE]
> Once you add the web SDK to your website, you can view your base events and create refined events. 

To view your base events:

1. Go to **Data** in the left navigation pane.

1. Select **Events** to see a list of all the events in the workspace.

    :::image type="content" source="media/data-events.png" alt-text="View events.":::

Create a refined event from a base event: 

1. Go to **Data**> **Events** and select **+ New events** at the top of the screen.

1. In the **New events** dialog, select **Create refined events** and then click **Next**.
   
     :::image type="content" source="media/new-events-wizard.png" alt-text="New events wizard.":::
     
1. In the **New events** dialog, enter the following information:

   - Select an event from the **Base events** dropdown.
   - Enter a name in the **Refined events display name** box.
   - Optionally, update the suggested **Actual name** without using spaces.

1. Select **Create** to apply your settings.

The refined event now appears in your **Events** list.

### Edit event name

You can change the name and the properties of a base or refined event.

1. Go to **Data** > **Events**. 

1. Select **More [...]** for an event and select **Edit name**.
    
     :::image type="content" source="media/create-refined-events-options.png" alt-text="Options to create refined events.":::

3. Update the event name and select **Rename**.

### View the details of a refined event:

1. In the **Event** list, click your base or refined event. 

1. Select **Add and remove properties** at the top of the screen to open the **Edit properties** pane. 

     :::image type="content" source="media/add-remove-properties.png" alt-text="Add and remove properties.":::

1. Use the check boxes to select the properties that you want to show and the ones you want to hide. 

   :::image type="content" source="media/edit-properties-refined-events.png" alt-text="Edit properties for refined events.":::

1. Select **Confirm** to apply your selection, and then click **Save**.


### Edit selected properties for a refined event

1. Go to **Data** > **Events** and select the refined events to open the detailed view.
1. Select **Add and remove properties**. 
1. Edit the selection of the check boxes.
1. Select **Confirm** and then **Save** to apply the changes.

For information about exporting events, see [Export events](export-events.md).
[!INCLUDE[footer-include](../includes/footer-banner.md)]
