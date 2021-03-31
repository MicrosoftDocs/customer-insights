---
title: "Export data from Customer Insights"
description: "Manage exports to share data."
ms.date: 03/25/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: phkieffer
ms.author: philk
manager: shellyha
---

# Exports (preview) overview

The **Exports** page shows you all configured exports. Exports share specific data with various applications. They can include customer profiles or entities, schemas, and mapping details. Each export requires a [connection, set up by an administrator, to manage authentication and access](connections.md).

> [!NOTE]
> Until March 2021, exports created a connection to the corresponding service automatically. Exports now require a [connection, created and shared by an administrator](connections.md) before you can create them. Read on for additinal details.

Go to **Data** > **Exports** to view the exports page. All user roles have access to view configured exports. Use of the search field in the command bar to find exports by their name, connection name, or connection type.

## Set up a new export

To set up or edit an export, you need to have connections available to you. Connections depend on your [user role](permissions.md):
- Administrators have access to all connections. They can also create new connections when setting up an export.
- Contributors can have access to specific connections. They depend on administrators to configure and share connections. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).
- Viewers can only view existing exports but not create them.

1. Go to **Data** > **Exports**.

1. Select **Add export** to create a new export destination.

1. In the **Set up export** pane, select which connection to use. [Connections](connections.md) are managed by administrators. 

1. Provide the required details and select **Save** to create the export.

### Edit an export

1. Select the vertical ellipsis for the export destination you want to edit.

1. Select **Edit** from the drop-down menu.

1. Change the values you want to update and select **Save**.

## View Exports and export details

After creating export destinations, they are listed on **Data** > **Exports**. All users can see which data is shared and its latest status.

1. Go to **Data** > **Exports**.

1. Users without edit permissions select **View** instead of **Edit** see the export details.

1. This side pane shows the set up of this export. Without edit permissions, you can't change values. Select **Close** to return to the exports page.

## Run exports on demand

After configuring an export, it will run with every [scheduled refresh](system.md#schedule-tab) as long as it has a working connection.

To export data without waiting for a scheduled refresh, go to **Data** > **Exports**. You have two options:

- To run all exports, select **Run all** in the command bar. 
- To run a single export, select the ellipsis (...) on a list item and then choose **Run**.

## Remove an Export

1. Go to **Data** > **Exports**.

1. Select the vertical ellipsis for the Export you want to remove.

1. Select **Remove** from the dropdown menu.

1. Confirm the removal by selecting **Remove** on the confirmation screen.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
