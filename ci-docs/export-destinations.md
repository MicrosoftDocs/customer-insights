---
title: "Exports (preview) overview"
description: "Manage exports to share data."
ms.date: 07/25/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: overview
author: pkieffer
ms.author: philk
manager: shellyha
searchScope: 
  - ci-export
  - ci-connections
  - customerInsights
---

# Exports (preview) overview

 Exports allow you to share specific data with various applications. They can include customer profiles, entities, schemas, and mapping details. Each export requires a [connection, set up by an administrator, to manage authentication and access](connections.md). The **Exports** page shows you all configured exports.

## Export types

There are two main types of exports:  

- **Data-out exports**: export any type of entity available in Customer Insights. The entities that you select for export are exported with all data fields, metadata, schemas, and mapping details.
- **Segment exports**: export segment entities from Customer Insights. Segments represent a list of customer profiles. When configuring the export, you select the included data fields, depending on the target system you are exporting data to.

### Export segments

**Exporting segments in environments for business accounts (B-to-B) or individual consumers (B-to-C)**  
Most export options support both types of environments. Exporting segments to various target systems have specific requirements. 

**Segment exports in environments for individual consumers (B-to-C)**  
- Segments in the context of environments for individual customers are built on the *unified customer profile* entity. Every segment that meets the requirements of the target systems (for example, an email address) can get exported.

**Segment exports environments for business accounts (B-to-B)**  
- Segments in the context of environments for business accounts are built on the *account* entity. To export account segments as is, the target system needs to support pure account segments. This is the case for [LinkedIn](export-linkedin-ads.md) when you choose the **company** option while defining the export.
- All other target systems require fields from the contact entity. To ensure account segments can retrieve data from related contacts, your segment definition needs to project attributes of the contact entity. Learn more about how to [configure segments and project attributes](segment-builder.md).

**Limits on segment exports**  
- Third-party target systems may limit the number of customer profiles that you can export. 
- For individual customers, you'll see the actual number of segment members when you select a segment for export. You'll get a warning if a segment is too large. 
- For business accounts, you'll see the number of accounts in a segment; however, the number of contacts that may be projected doesn't show. In some cases, this could lead to the exported segment actually containing more customer profiles than the target system accepts. If the limits of the target system are exceeded, the export is skipped.

## Set up a new export

To set up or edit an export, you need the right connections available to you. Connections depend on your [user role](permissions.md):
- **Administrators** have access to all connections. They can also create new connections when setting up an export.
- **Contributors** can have access to specific connections. They depend on administrators to configure and share connections. The exports list shows contributors whether they can edit or only view an export in the **Your permissions** column. For more information, go to [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).
- **Viewers** can only view existing exports—not create them.

1. Go to **Data** > **Exports**.

1. Select **Add export** to create a new export.

1. In the **Set up export** pane, select which [connection](connections.md) to use.

1. Provide the required details and select **Save** to create the export. For the required details, review the Customer Insights documentation for the specific export.

## Manage existing exports

Go to **Data** > **Exports** to view the exports, their connection name, connection type, and status. All user roles can view configured exports. You can sort the list of exports by any column or use the search box to find the export you want to manage.

Select an export to view available actions.

:::image type="content" source="media/exports_showmore.png" alt-text="Exports page.":::

- **View** or **Edit** the export. Users without edit permissions select **View** instead of **Edit** to see the export details.
- **Run** the export to export the latest data.
- **Create duplicate** of an export.
- **[Schedule](#schedule-and-run-exports)** the export.
- **Detach connection** to remove the connection for this export. Detach does not remove the connection, but deactivates the export. The **Connection used** column displays No Connection.
- **Remove** the export.

## Schedule and run exports

Each export you configure has a refresh schedule. During a refresh, the system looks for new or updated data to include in an export. By default, exports are run as part of every [scheduled system refresh](system.md#schedule-tab). You can customize the refresh schedule or turn it off to run exports manually.

Export schedules depend on the state of your environment. If there are updates in progress on [dependencies](system.md#refresh-processes) when a scheduled export should start, the system will first complete the updates and then run the export. The **Refreshed** column shows when an export was last refreshed.

### Schedule exports

Define custom refresh schedules for individual exports or several exports at once. The currently defined schedule is listed in the **Schedule** column of the export list. The permission to change the schedule is the same as [editing and defining exports](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. Select the export you want to schedule.

1. Select **Schedule**.

1. In the **Schedule export** pane, set the **Schedule run** to **On** to run the export automatically. Set it to **Off** to refresh it manually.

1. For automatically refreshed exports, choose a **Recurrence** value and specify the details for it. The time defined applies to all instances of a recurrence. It's the time when an export should start refreshing.

1. Select **Save**.

When editing the schedule for several exports, make a selection under **Keep or override schedules**:

- **Keep individual schedules**: Keep the previously defined schedule for the selected exports and only disable or enable them.
- **Define new schedule for all selected exports**: Override the existing schedules of the selected exports.

### Run exports on demand

To export data without waiting for a scheduled refresh, go to **Data** > **Exports**.

- To run all exports, select **Run all** in the command bar. Only exports that have an active schedule are run. To run an export that is not active, run a single export.
- To run a single export, select it in the list and select **Run** in the command bar.

[!INCLUDE [progress-details-include](includes/progress-details-pane.md)]


[!INCLUDE [footer-include](includes/footer-banner.md)]
