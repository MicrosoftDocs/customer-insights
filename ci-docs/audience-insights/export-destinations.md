---
title: "Exports"
description: "Manage exports to share data."
ms.date: 07/21/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Exports (preview) overview

The **Exports** page shows you all configured exports. Exports share specific data with various business apps and tools, and can include customer profiles or entities and their related schemas and mapping details. Each export needs a connection, set up by an admin, to manage authentication and access.

Go to **Data** > **Exports** to get to this page. All user roles have access to Exports page.


## Set up a new export

To set up or edit an export, you need to have connections available to you. This depends on your [role](permissions.md):
- Administrators have access to all connections. They can also create new connections when setting up an export.
- Contributors can have access to specific connections. They depend on administrators to configure connection to be available to them. [Learn more about sharing connections](connections.md#allow-contributors-to-use-a-connection-for-exports)
- Viewers cannot set up or edit exports.

1. Go to **Data** > **Exports**.

1. Select **Add export** to create a new export destination.

1. In the **Set up export** pane, select which connection to use. Picking a connection will define the type of export you are creating. [Connections](connections.md) are setup by administrators. 

   1. If you are administrator you can choose to create a new connection.

1. Provide the required details and select **Save** to create the export.

### Edit an export

1. Select the vertical ellipsis for the Export destination you want to edit.

1. Select **Edit** from the dropdown menu.

1. Change the values that require update and select **Save**.

## View Exports and export details

After creating export destinations, you'll find them in the list on the Exports page. All user roles have access to this page, so they understand what data is shared and its latest status.

1. Go to **Data** > **Exports**.

1. For user roles who cannot edit a specific export, the first action on each row is called **View** instead of Edit. Select **View** to open a side panel.

1. This side panel displays the set up of this export. You cannot change anything. To get back to the Exports page select **Close**. 

## Run exports on demand

After configuring an export, it will run with every [scheduled refresh](system.md#schedule-tab) as long as it has a connection.

To export data without waiting for a scheduled refresh, go to **Data** > **Exports**. You how two options:

- To run all exports simultaneously select **Run all** in the command bar. 
- To run a single export select the ellipsis (...) on a list item and then choose the **Run** option.

## Remove an Export

To remove an Export, start from the main **Exports** page.

1. Select the vertical ellipsis for the Export you want to remove.

1. Select **Remove** from the dropdown menu.

1. Confirm the removal by selecting **Remove** on the confirmation screen.
