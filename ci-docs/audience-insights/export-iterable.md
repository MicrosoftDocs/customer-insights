---
title: "Export Customer Insights data to Iterable"
description: "Learn how to configure the connection and export to Iterable."
ms.date: 03/29/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment lists to Iterable (preview)

Export segments of unified customer profiles to Iterable and use them for marketing activities.

## Prerequisites

-	You have an [Iterable account](https://iterable.com/) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Exporting to Iterable is limited to segments.
- Exporting up to 1 million customer profiles to Iterable can take up to 30 minutes to complete. 
- The number of customer profiles that you can export to Iterable is dependent and limited on your contract with Iterable.

## Set up connection to Iterable

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Iterable** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your [Iterable API key](https://support.iterable.com/hc/en-us/articles/360043464871) to continue to sign in. 

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Iterable.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Iterable section. If you don't see this section name, there are no connections of this type available to you.

3. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. It's required to export segments to Iterable.The list created in Iterable will receive the exact same name as your segment name in Dynamics 365 Customer Insights.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Iterable, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Iterable meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
