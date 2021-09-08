---
title: "Export Customer Insights data to Klaviyo"
description: "Learn how to configure the connection and export to Klaviyo."
ms.date: 08/13/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment lists to Klaviyo (preview)

Export segments of unified customer profiles to Klaviyo and use them for marketing activities.

## Prerequisites

-	You have an [Klaviyo account](https://www.klaviyo.com/) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- You can export up to 100'000 profiles per export to Klaviyo.
- Exporting to Klaviyo is limited to segments.
- Exporting up to 1 million profiles to Klaviyo can take up to 20 minutes to complete. 
- The number of profiles that you can export to Klaviyo is dependent and limited on your contract with Klaviyo.

## Set up connection to Klaviyo

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Klaviyo** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your [Klaviyo API key](https://help.klaviyo.com/hc/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys) to continue to sign in. 

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Klaviyo.

1. Select **Authenticate with Klaviyo** and provide your admin credentials for Klaviyo.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the Klaviyo section. If you don't see this section name, there are no connections of this type available to you.

1. Enter your [**Klaviyo List ID**](https://help.klaviyo.com/hc/articles/115005078647-How-to-Find-a-List-ID).     

3. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. It's required to export segments to Klaviyo.

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Klaviyo, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Klaviyo meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
