---
title: View and create dimensions
description: How to create, edit, and delete dimensions.
ms.reviewer: mhart
ms.author: jusali
author: jusali
ms.date: 06/02/2021
ms.service: customer-insights
ms.subservice: engagement-insights 
ms.topic: how-to
ms.manager: shellyha 
---

# View and create dimensions

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

A dimension is an attribute of an event that can describe, filter, or group data. If you're running a marketing promotion on your website, you can use dimensions to sort visitors by new and returning users.  

Engagement insights includes out-of-the-box dimensions for event properties. Examples include:

- Browser name
- Page name
- Device model
- Operating system
- Country

## View dimensions

Dimensions are based on existing event properties. When you use the tracking code for engagement insights, system dimensions are automatically created.

1. Go to **Data** in the left navigation pane. 
1. Select **Dimensions** to see a list of all the dimensions in the workspace. 
   > [!NOTE]
   > System-generated dimensions are read-only. You can’t edit them. You can only create and edit custom dimensions.

## Create a dimension

In addition to system-generated dimensions, environment and workspace admins can create custom dimensions. Custom dimensions are based on default properties of base events or they can use [custom properties of an event](advanced-SDK-implementation.md).

1. Go to **Data** > **Dimensions**.
1. Select **Add a dimension**.

   :::image type="content" source="media/add-dimension.png" alt-text="Add a dimension to an event":::

1. In the **Create a dimension** pane, select a property to base the dimension on. The properties list will show all the properties in the workspace not assigned to a dimension.
1. Enter a name in the **Display name** box. Optionally, you can add a description.
1. Select **Create** to save the dimension. It can take up to one minute before you can use the dimension in a [custom report](custom-reports.md) or [segment](segments.md). 

## Edit a dimension

You can change the name and description of a dimension.

1. Go to **Data** > **Dimensions**.
1. Select the dimension you want to delete.
1. In the **Edit dimension** pane, update the dimension.
1. Select **Apply** to save your changes.

## Delete a dimension

You can only delete user-created dimensions but you can't remove system dimensions.

Deleting a dimension is permanent. Reports and segments that use a deleted dimension will no longer work. 

1. Go to **Data** > **Dimensions**.
1. Select the dimension you want to delete.
1. In the **Edit dimension** pane, select **Delete dimension**.

   :::image type="content" source="media/delete-dimension.png" alt-text="Delete a dimension to an event":::

1. Enter **CONFIRM DELETE** (in all caps) to confirm the deletion. 
1. Select **Delete**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]