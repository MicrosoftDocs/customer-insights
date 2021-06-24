---
title: "Export Customer Insights data to AdRoll"
description: "Learn how to configure the connection and export to AdRoll."
ms.date: 03/03/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to AdRoll (preview)

Export segments of unified customer profiles to AdRoll and use them for advertising. 

## Prerequisites for a connection

-	You have an [AdRoll account](https://www.adroll.com/) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- You can export up to 250,000 profiles at a time to AdRoll.
- You can't export segments with fewer than 100 profiles to AdRoll. 
- Exporting to AdRoll is limited to segments.
- Exporting up to 250,000 profiles to AdRoll can take up to 10 minutes to complete. 
- The number of profiles that you can export to AdRoll is dependent on your contract with AdRoll.

## Set up connection to AdRoll

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **AdRoll** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to AdRoll.

1. Select **Authenticate with AdRoll** and provide your admin credentials for AdRoll. 

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the AdRoll section. If you don't see this section name, then no connections of this type are available to you.

1. Enter your **AdRoll Advertiser ID**. For more information, see [AdRoll Advertiser Profiles](https://help.adroll.com/hc/articles/212011838-Advertiser-Profiles).

3. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. It's required to export segments to AdRoll.

1. Select the segments you want to export. Select a segment with a least 100 members. You can't export smaller segments. Additionally the maximum size of a segment to export is 250,000 members per export. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 

You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to AdRoll, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that AdRoll meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights administrator can remove this export destination at any time to discontinue use of this functionality.
