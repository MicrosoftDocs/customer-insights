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
> Until March 2021, exports created a connection to the corresponding service automatically. Exports now require a [connection, created and shared by an administrator](connections.md) before you can create them.

Go to **Data** > **Exports** to view the exports page. All user roles have access to view configured exports. Use of the search field in the command bar to find exports by their name, connection name, or connection type.

## Set up a new export

To set up or edit an export, you need to have connections available to you. Connections depend on your [user role](permissions.md):
- Administrators have access to all connections. They can also create new connections when setting up an export.
- Contributors can have access to specific connections. They depend on administrators to configure and share connections. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).
- Viewers can only view existing exports but not create them.


### To define a new export:

1. Go to **Data** > **Exports**.

1. Select **Add export** to create a new export.

1. In the **Set up export** pane, select which connection to use. [Connections](connections.md) are managed by administrators. 

1. Provide the required details and select **Save** to create the export.


### To define a new export based on an existing one:

1. Select the export you want to base the new on on by activating it in the list of exports.

1. Select **Create duplicate** action. This opens the panel to define a new export with the same setup as the export you activated it on.

1. Review and adapt the export and select **Save** to create the export.


### Edit an export

1. Select the vertical ellipsis for the export destination you want to edit.

1. Select **Edit** from the drop-down menu.

1. Change the values you want to update and select **Save**.

## View Exports and export details

After creating export destinations, they are listed on **Data** > **Exports**. All users can see which data is shared and its latest status.

1. Go to **Data** > **Exports**.

1. Users without edit permissions select **View** instead of **Edit** see the export details.

1. This side pane shows the set up of this export. Without edit permissions, you can't change values. Select **Close** to return to the exports page.

## Schedule and run exports

Each export you configure has a schedule. By default exports are run as part of the system every [scheduled refresh](system.md#schedule-tab). You can customize the schedule when this export should be run. If turned off, the export will only run if activated manually.

### Schedule exports
You can choose custom schedules for your exports. You can define this for individual or a several exports at once. The exports page shows the current schedule in the column **Schedule**. The permission to change the schedule is the same as for [editing and defining exports](export-destinations.md#set-up-a-new-export). 

Note that schedules for exports depend on the state of your instance. If there are [dependencies](system.md#refresh-policies) being updated for scheduled exports when schedule should start, the system will wait until these have finished, then run the export. You can see when an export was last refreshed in column **Refreshed**.

1. Go to **Data** > **Exports**.

1. Select the export you want to schedule in the list.

1. Select **Schedule** from the commandbar or the dropdown menu.

1. Within the panel that opened choose between having this export run automatically or only manually with the toggle control "Schedule run". When toggle is set to off, this export will only be run if triggered by a user. Your previously defined schedule will remain stored. It only has an effect if the toggle is set to on.

1. When editing a schedule choose recurrence type, then define details for it. The time defined applies to all instances of a recurrence. This time reflects when that export should start.

1. When done with defining a schedule save it by activating **Save**.

When editing the schedule for several exports, you need to make an additional choice in control **Keep or override schedules**:
- If you only want to disable or enable if these exports should run on schedule, then choose **Keep individual schedules** option. This will preserve the previously definied schedule for each export.
- If you want to define a new schedule for all selected exports, which will override existing schedules, then choose **Define new schedule for all selected** option. You will then see the same form as for single export.


### Run exports manually
To export data without waiting for a scheduled refresh, go to **Data** > **Exports**. You have two options:

- To run all exports, select **Run all** in the command bar. This will only run exports which have an active schedule.
- To run a single export, select it in the list, then active **Run**, which is available in the command bar at the top of the page or through the ellipsis (...) on a list item.

## Remove an Export

1. Go to **Data** > **Exports**.

1. Select the vertical ellipsis for the Export you want to remove.

1. Select **Remove** from the dropdown menu.

1. Confirm the removal by selecting **Remove** on the confirmation screen.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
