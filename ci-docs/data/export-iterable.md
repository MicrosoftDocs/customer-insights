---
title: Export segments to Iterable (preview)
description: Export segments to Iterable to power your marketing activities. Learn how to configure the connection and export unified customer profiles.
ms.date: 07/16/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
---

# Export segments to Iterable (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Export segments of unified customer profiles to Iterable and use them for marketing activities.

## Prerequisites

- An [Iterable account](https://iterable.com/) and corresponding administrator credentials.
- An [Iterable API key](https://support.iterable.com/hc/en-us/articles/360043464871)
- [Configured segments](segments.md).
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- You can export up to 1 million customer profiles to Iterable, which can take up to 30 minutes to complete. The number of customer profiles that you can export to Iterable depends on your contract with Iterable.
- You can only export segments.

## Set up connection to Iterable

[!INCLUDE [export-connection-include](includes/export-connection-admn.md)]

1. Go to **Settings** > **Connections**.

1. Select **Add connection** and choose **Iterable**.

1. Enter a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. Choose a name that explains the purpose and target of the connection.

1. Choose who can use this connection. By default, only administrators can use it. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your Iterable API key to continue to sign in.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Add yourself as export user** and provide your Dynamics 365 Customer Insights - Data credentials.

1. Select **Save** to complete the connection.

## Configure an export

[!INCLUDE [export-permission-include](includes/export-permission.md)]

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In **Connection for export**, choose a connection from the Iterable section. Contact an administrator if no connection is available.

1. Enter a name for the export.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. The list you create in Iterable has the same name as your segment name in Customer Insights - Data.

1. Select the segments you want to export.

1. Select **Save**.

[!INCLUDE [export-saving-include](includes/export-saving.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
