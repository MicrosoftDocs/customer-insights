---
title: "Export data from Customer Insights"
description: "Manage exports to share data."
ms.date: 10/08/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
ms.custom: intro-internal
---

# Exports (preview) overview

The **Exports** page shows you all configured exports. Exports share specific data with various applications. They can include customer profiles, entities, schemas, and mapping details. Each export requires a [connection, set up by an administrator, to manage authentication and access](connections.md).

Go to **Data** > **Exports** to view the exports page. All user roles can view configured exports. Use the search field in the command bar to find exports by their name, connection name, or connection type.

## Export types

There are two main types of exports:  

- **Data-out exports** let you export any type of entity available in audience insights. The entities that you select for export are exported with all data fields, metadata, schemas, and mapping details. 
- **Segment exports** let you export segment entities from audience insights. Segments represent a list of customer profiles. When configuring the export, you select the included data fields, depending on the target system you are export data to. 

### Export segments

**Exporting segments in environments for business accounts (B-to-B) or individual consumers (B2C)**  
Most export option support both types of environments. Exporting segments to various target systems has specific requirements. Generally speaking, a segment member, the customer profile, contains contact information. While this is usually the case for segments built on individual consumers (B2C), it's not necessarily the case for segments based on business accounts (B-to-B). 

**Segment exports environments for business accounts (B-to-B)**  
- Segments in the context of environments for business accounts are built on the *account* entity. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](export-linkedin-ads.md) when you choose the **company** option while defining the export.
- All other target systems require fields from the contact entity. To ensure account segments can retrieve data from related contacts, your segment definition needs to project attributes of the contact entity. Learn more about how to [configure segments and project attributes](segment-builder.md).

**Segment exports in environments for individual consumers (B2C)**  
- Segments in the context of environments for individual customers are built on the *unified customer profile* entity. Every segment that meets the requirements of the target systems (for example, an email address) can get exported.

**Limits on segment exports**  
- Third-party target systems may limit the number of customer profiles that you can export. 
- For individual customers, you'll see the actual number of segment members when you select a segment for export. You'll get a warning if a segment is too large. 
- For business accounts, you'll see the number of accounts in a segment; however, the number of contacts that may be projected doesn't show. In some cases, this could lead to the exported segment actually containing more customer profiles than the target system accepts. Exceeding the limits of the target systems results will skip the export. 

## Set up a new export  
To set up or edit an export, you need to have connections available to you. Connections depend on your [user role](permissions.md):
- **Administrators** have access to all connections. They can also create new connections when setting up an export.
- **Contributors** can have access to specific connections. They depend on administrators to configure and share connections. The exports list shows contributors whether they can edit or only view an export in the **Your permissions** column. For more information, go to [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).
- **Viewers** can only view existing exports—not create them.

### Define a new export

1. Go to **Data** > **Exports**.

1. Select **Add export** to create a new export.

1. In the **Set up export** pane, select which connection to use. [Connections](connections.md) are managed by administrators. 

1. Provide the required details and select **Save** to create the export.

### Define a new export based on an existing export

1. Go to **Data** > **Exports**.

1. In the list of exports, select the export you want to duplicate.

1. Select **Create duplicate** in the command bar to open the **Set up export** pane with the details of the selected export.

1. Review and adapt the export and select **Save** to create a new export.

### Edit an export

1. Go to **Data** > **Exports**.

1. In the list of exports, select the export you want to edit.

1. Select **Edit** in the command bar.

1. Change the values you want to update and select **Save**.

## View exports and export details

After creating export destinations, they're listed on **Data** > **Exports**. All users can see which data is shared and its latest status.

1. Go to **Data** > **Exports**.

1. Users without edit permissions select **View** instead of **Edit** to see the export details.

1. The side pane shows the configuration of an export. Without edit permissions, you can't change values. Select **Close** to return to the exports page.

## Schedule and run exports

Each export you configure has a refresh schedule. During a refresh, the system looks for new or updated data to include in an export. By default, exports are run as part of every [scheduled system refresh](system.md#schedule-tab). You can customize the refresh schedule or turn it off to run exports manually.

Export schedules depend on the state of your environment. If there are updates in progress on [dependencies](system.md#refresh-policies) when a scheduled export should start, the system will first complete the updates and then run the export. You can see when an export was last refreshed in column **Refreshed**.

### Schedule exports

You can define custom refresh schedules for individual exports or several exports at once. The currently defined schedule is listed in the **Schedule** column of the export list. The permission to change the schedule is the same as for [editing and defining exports](export-destinations.md#set-up-a-new-export). 

1. Go to **Data** > **Exports**.

1. Select the export you want to schedule.

1. Select **Schedule** in the command bar.

1. In the **Schedule export** pane, set the **Schedule run** to **On** to run the export automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed exports, choose a **Recurrence** value and specify the details for it. The time defined applies to all instances of a recurrence. It's the time when an export should start refreshing.

1. Apply and activate your changes by selecting **Save**.

When editing the schedule for several exports, you need to make a selection under **Keep or override schedules**:
- **Keep individual schedules**: Persist the previously defined schedule for the selected exports and only disable or enable them.
- **Define new schedule for all selected exports**: Override the existing schedules of the selected exports.

### Run exports on demand

To export data without waiting for a scheduled refresh, go to **Data** > **Exports**.

- To run all exports, select **Run all** in the command bar. This action will only run exports that have an active schedule.
- To run a single export, select it in the list and select **Run** in the command bar. That's how you run exports with no active schedule. 

## Remove an Export

1. Go to **Data** > **Exports**.

1. Select the export you want to remove.

1. Select **Remove** in the command bar.

1. Confirm the removal by selecting **Remove** on the confirmation screen.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
