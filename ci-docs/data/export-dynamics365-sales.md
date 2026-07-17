---
title: Export segments to Dynamics 365 Sales (preview)
description: Export segments to Dynamics 365 Sales to build marketing lists, follow-up workflows, and promotions. Learn how to configure the connection and export.
ms.date: 07/16/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to Dynamics 365 Sales (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Use your customer data to create marketing lists, follow-up workflows, and send promotions by using Dynamics 365 Sales.

## Prerequisites

You must have contact records in Dynamics 365 Sales before you can export a segment from Customer Insights - Data to Sales. For more information, see [Dynamics 365 Sales using Microsoft Dataverse](connect-dataverse.md).

   > [!NOTE]
   > Exporting segments from Customer Insights - Data to Sales doesn't create new contact records in the Sales environments. You must ingest the contact records from Sales into Customer Insights - Data and use them as a data source. You also need to include these contact records in the unified Customer table to map customer IDs to contact IDs before you can export segments.

## Known limitations

Exports to Dynamics 365 Sales are limited to 100,000 contacts per segment. The export process can take up to three hours to complete.

## Set up connection to Sales

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Dynamics 365 Sales**.

1. Enter a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. Choose a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, only administrators can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your organization's Sales URL in the **Server address** field.

1. In the **Server admin account** section, select **Sign in** and choose a Dynamics 365 Sales account.

1. Map a customer ID field to the Dynamics 365 Contact ID.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In **Connection for export**, choose a connection from the Dynamics 365 Sales section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. Select the Contact ID field in the Customer table that matches the Dynamics 365 Contact ID.

1. Select the segments you want to export.

1. Select **Save**

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
