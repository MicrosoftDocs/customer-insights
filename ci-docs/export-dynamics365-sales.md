---
title: "Export segments to Dynamics 365 Sales (preview)"
description: "Learn how to configure the connection and export to Dynamics 365 Sales."
ms.date: 03/03/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: pkieffer
ms.author: philk
manager: shellyha
searchScope: 
  - ci-export
  - customerInsights
---

# Export segments to Dynamics 365 Sales (preview)

Use your customer data to create marketing lists, follow up workflows, and send out promotions with Dynamics 365 Sales.

## Prerequisites

Contact records must be present in Dynamics 365 Sales before you can export a segment from Customer Insights to Sales. Read more on how to ingest contacts from [Dynamics 365 Sales using Microsoft Dataverse](connect-dataverse-managed-lake.md).

   > [!NOTE]
   > Exporting segments from Customer Insights to Sales will not create new contact records in the Sales instances. The contact records from Sales must be ingested in Customer Insights and used as a data source. They also need to be included in the unified Customer entity to map customer IDs to contact IDs before segments can be exported.

## Known limitations

The maximum members per segment to export to Dynamics 365 Sales is 100,000, which can take up to 3 hours to complete.

## Set up connection to Sales

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Dynamics 365 Sales**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, it's only administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your organization's Sales URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Sales account.

1. Map a customer ID field to the Dynamics 365 Contact ID.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Dynamics 365 Sales section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Choose one or more segments.

1. Select **Save**

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

[!INCLUDE [footer-include](includes/footer-banner.md)]
