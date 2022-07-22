---
title: "Export segments to Microsoft Advertising (preview)"
description: "Learn how to configure the connection and export to Microsoft Advertising."
ms.date: 10/08/2021
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Microsoft Advertising (preview)

Export Customer Insights segments to Microsoft Advertising to create Customer Match audiences. Use these audiences for your ad campaigns.

## Prerequisites

- A [Microsoft Advertising account](https://ads.microsoft.com/) and corresponding administrator credentials.
- Microsoft Advertising Customer ID and Account ID. Find the Customer ID (`cid`) and Account ID (`aid`) in the parameters of the URL when you're signed in to Microsoft Advertising.
- The Customer Match terms of use are accepted.
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 500,000 customer profiles per export to Microsoft Advertising, which can take up to 10 minutes.
- Segments only.

## Set up connection to Microsoft Advertising

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Microsoft Advertising**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. The default is administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter the **Microsoft Advertising Customer ID**.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with Microsoft Advertising** and provide your admin credentials for Microsoft Advertising.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Microsoft Advertising section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Select the segments to export. The Customer Match audiences in Microsoft Advertising are automatically created with the name of the segments selected for export. Each segment will result in a separate Customer Match audience.

1. Enter your **Microsoft Advertising Customer ID and Account ID**.

1. In the **Data matching** section, in the **Email** field, select the field with a customer's email address.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).

[!INCLUDE [footer-include](includes/footer-banner.md)]
