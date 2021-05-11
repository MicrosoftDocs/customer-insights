---
title: "Export Customer Insights data to LinkedIn Ads"
description: "Learn how to configure the connection and export to LinkedIn Ads."
ms.date: 03/03/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segment lists to LinkedIn Ads (preview)

Export segments of unified customer profiles to LinkedIn Ads to create Matched Audiences, and use the audiences to target contacts and companies.

## Prerequisites

-	You have an [LinkedIn Campaign Manager account](https://business.linkedin.com/marketing-solutions/ads) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Known limitations

- You can export up to 1ook million profiles per export to LinkedIn Ads.
- Exporting to LinkdedIn Ads is limited to segments.
- Exporting up to 1ook million profiles to LinkedIn Ads can take up to 20 minutes to complete. 


## Set up connection to LinkedIn Ads

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **LinkedIn Ads** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your [LinkedIn Campaign Manager Account ID](https://www.linkedin.com/help/lms/answer/a424270)

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Campaign Monitor.

1. Select **Authenticate with LinkedIn** and provide your admin credentials for LinkedIn Campaign Manager.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the LinkedIn Ads section. If you don't see this section name, there are no connections of this type available to you.

1.Choose whether you want to export data to do [Contact Targeting or Company Targeting on LinkedIn](https://business.linkedin.com/marketing-solutions/blog/linkedin-b2b-marketing/2017/how-to-use-linkedin-matched-audiences). 

3. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. It's required to export segments to LinkedIn Ads.

1. Select the segments you want to export. The Matched Audiences in LinkedIn campagain manager will automatically be created with the name of the segments that you selected to export. Each segment will result in an individual Matched Audience. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to LinkedIn Ads, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that LinkedIn Ads meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
