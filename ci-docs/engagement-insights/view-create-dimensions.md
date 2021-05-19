---
title: View and create dimensions
description: How to create, edit, and delete dimensions.
ms.reviewer: jusali
ms.author: v-salash
author: pickwick129
ms.date: 05/18/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create dimensions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A dimension is an attribute of an [event](refined-events.md) that can describe, filter, or group data. If you're running a marketing promotion on your website, you can use dimensions to sort visitors by new and returning users. You could filter visitors by country or use dimensions to separate purchases by type on a chart. 

Engagement insights include out-of-the-box dimensions for web and mobile events. Examples include:

- Browser name
- Page name
- Device model
- Operating system
- Country

## View dimensions

Dimensions are based on existing event properties. When you use the engagement insights web SDK to define user information, dimensions are automatically included with events.

1. Go to **Data** in the left navigation pane. 
1. Select **Dimensions** to see a list of all the dimensions in the workspace. 
   > [!NOTE]
   > System-generated dimensions are read-only. You can’t edit them. You can only create and edit custom dimensions.

## Create a custom dimension

In addition to system-generated dimensions, Event and Workspace admins can create custom dimensions. First, you must have [specified custom properties](advanced-SDK-implementation.md) to be sent with the event.

1. Go to **Data** and then select **Dimensions**.
1. Select **Add a dimension**.

   :::image type="content" source="media/add-dimension.png" alt-text="Add a dimension to an event":::

1. In the **Dimensions** pane, select a property to base the dimension on. The properties list will show all the properties in the workspace not assigned to a dimension.
1. Enter a name in the **Display name** box. Optionally, you can add a description.
1. Select **Save** to create the dimension. It can take up to one minute before you can use the dimension in a report or segment. 

## Delete a custom dimension

System dimensions cannot be deleted but you can delete any custom dimension.

Deleting a dimension is permanent. The reports and segments that use the dimension will no longer render. 

1. To delete a  dimension, go to **Data** and then select **Dimension**.
1. Select the dimension you want to delete and in the **Edit dimension** pane, select **Delete dimension**.

   :::image type="content" source="media/delete-dimension.png" alt-text="Delete a dimension to an event":::

1. Enter **CONFIRM DELETE** to confirm the deletion. 
1. Enter **Delete**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]