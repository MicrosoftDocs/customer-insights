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
- The Customer Match terms of use are accepted.
- [Configured segments](segments.md) in Customer Insights.
- Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Up to 500,000 customer profiles per export to Microsoft Advertising can take up to 10 minutes.
- Exports to Microsoft Advertising is limited to segments.

## Set up the connection to Microsoft Advertising

You must be an [administrator](permissions.md) in Customer Insights to add a connection.

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Microsoft Advertising**.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. The default is administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select **I agree** to confirm the [Data privacy and compliance](#data-privacy-and-compliance).

1. Select **Connect** to initialize the connection.

1. Select **Authenticate with Microsoft Advertising** and provide your admin credentials for Microsoft Advertising.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Microsoft Advertising, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Microsoft Advertising meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to stop use of this functionality.

## Configure an export

To configure this export, you must have [permission](export-destinations.md#set-up-a-new-export) for this connection type.

1. Go to **Data** > **Exports**.

1. Select **Add export**.

1. In the **Connection for export** field, choose a connection from the Microsoft Advertising section. Contact an administrator if one is not available.

1. Enter a name for the export.

1. Select the segments to export. The Customer Match audiences in Microsoft Advertising are automatically created with the name of the segments selected for export. Each segment will result in a separate Customer Match audience.

1. Enter your **Microsoft Advertising Customer ID and Account ID**. You can find the Customer ID (`cid`) and Account ID (`aid`) in the parameters of the URL when you're signed in Microsoft Advertising.

1. In the **Data matching** section, in the **Email** field, select the field with a customer's email address. It's required to export segments to Microsoft Advertising.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). You can also [export data on demand](export-destinations.md#run-exports-on-demand).
