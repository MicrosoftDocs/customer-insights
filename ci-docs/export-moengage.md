---
title: "Export Customer Insights data to MoEngage"
description: "Learn how to configure the connection and export to MoEngage."
ms.date: 21/06/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to MoEngage (preview)

Export segments of unified customer profiles to MoEngage and use them for email marketing in MoEngage. 

## Prerequisites for a connection

-	You have an [MoEngage account]((https://www.moengage.com/) and corresponding administrator credentials.
-	You have generated an API key under Settings > API in MoEnage.
-	You have [configured segments](segments.md) in Customer Insights.

## Known limitations

- You can export up to 100'000 customer profiles in total to MoEngage.
- Exporting to MoEngage is limited to segments.
- Exporting up to 100'000 customer profiles to MoEngage can take up to a few hours to complete. 
- The number of customer profiles that you can export to MoEngage is dependent and limited on your contract with MoEngage.

## Set up connection to MoEngage

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **MoEngage** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your [MoEngage Data API ID and API key]([https://autopilot.docs.apiary.io/#](https://developers.moengage.com/hc/en-us/articles/4404674776724-Overview#:~:text=Navigate%20to%20Settings%20%3E%20APIs%20%3E%20DATA,ID%20Password%20%2D%20DATA%20API%20KEY)).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to MoEngage.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add export**.

1. In the **Connection for export** field, choose a connection from the MoEngage section. If you don't see this section name, there are no connections of this type available to you.

1. In the **Data matching** section, in the **Email** field, select the field that represents a customer's email address. Repeat the same steps for other optional fields.

1. Select the segments you want to export. We will create one or more segments with the same name as the selected segments in MoEngage under Segment > Custom Segments. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Autopilot, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Autopilot meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.


[!INCLUDE [footer-include](includes/footer-banner.md)]
