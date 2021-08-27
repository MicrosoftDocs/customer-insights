---
title: "Export Customer Insights data to Microsoft Advertising"
description: "Learn how to configure the connection and export to Microsoft Advertising."
ms.date: 08/27/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to Microsoft Advertising (preview)

Export Customer Insights segments to Microsoft Advertising to create Customer Match audiences. Use these audiences for your ad campaigns.

## Prerequisites

-	An [Microsoft Advertising account](https://ads.microsoft.com/) and corresponding administrator credentials.
-	You've accepted the Customer Match terms of use. 
-	[Configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field with an email address.

## Known limitations

- You can export up to 500 K profiles per export to Microsoft Advertising.
- Exporting to Microsoft Advertising is limited to segments.
- Exporting up to 500 K profiles to Microsoft Advertising can take up to 10 minutes to complete. 


## Set up the connection to Microsoft Advertising

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Microsoft Advertising** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. The default is administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Microsoft Advertising.

1. Select **Authenticate with Microsoft Advertising** and provide your admin credentials for Microsoft Advertising.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Microsoft Advertising section. If you don't see this section name, there are no connections of this type available to you.

1. Select the segments to export. The Customer Match audiences in Microsoft Advertising are automatically created with the name of the segments selected for export. Each segment will result in a separate Customer Match audience. 

1. Enter your **Microsoft Advertising Customer ID and Account ID**. You can find the Customer ID (`cid`) and Account ID (`aid`) in the parameters of the URL when you're signed in Microsoft Advertising.

1. In the **Data matching** section, in the **Email** field, select the field with a customer's email address. It's required to export segments to Microsoft Advertising.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Microsoft Advertising, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Microsoft Advertising meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to stop use of this functionality.
