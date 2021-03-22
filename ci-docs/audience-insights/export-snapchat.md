---
title: "Export Customer Insights data to Snapchat"
description: "Learn how to configure the connection and export to Snapchat."
ms.date: 03/03/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment lists to Snapchat (preview)

Export segments of unified customer profiles to Snapchat and use them for advertising. 

## Prerequisites for a connection

-	You have a [Snapchat Business account](https://business.snapchat.com/), a [Snapchat Ads account](https://ads.snapchat.com/) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- Exporting to Snapchat is limited to segments.
- Exporting up to 1 million profiles to Snapchat can take up to 15 minutes to complete. 

## Set up connection to Snapchat

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Snapchat** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Snapchat.

1. Select **Authenticate with Snapchat** and provide your Admin credentials for Snapchat. 

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Snapchat section. If you don't see this section name, there are no connections of this type available to you.

1. Enter your [**Snapchat Audience ID**](https://businesshelp.snapchat.com/s/article/custom-audiences?language=en_US).
  - Note: Open a list and you can find the list ID in the URL.

3. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. It's required to export segments to Snapchat.

1. Select the segments you want to export. 

3. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Snapchat, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Snapchat meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
