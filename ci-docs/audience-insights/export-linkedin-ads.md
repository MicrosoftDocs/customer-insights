---
title: "Export Customer Insights data to LinkedIn Ads"
description: "Learn how to configure the connection and export to LinkedIn Ads."
ms.date: 08/27/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: pkieffer
ms.author: philk
manager: shellyha
---

# Export segments to LinkedIn Ads (preview)

Export segments of unified customer profiles to LinkedIn Ads to create matched audiences. Use the matched audiences for company targeting and contact targeting.

## Prerequisites

-	You have an [LinkedIn Campaign Manager account](https://business.linkedin.com/marketing-solutions/ads) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Customer profiles in the exported segments contain a field with an email address.

## Known limitations

- You can export up to 100K profiles per export to LinkedIn Ads.
- Exporting to LinkedIn Ads is limited to segments.
- Exporting up to 100K profiles to LinkedIn Ads can take up to 10 minutes to complete. 

## Set up the connection to LinkedIn Ads

1. In audience insights, go to **Admin** > **Connections**.

1. Select **Add connection** and choose **LinkedIn Ads** to configure the connection.

1. Give your connection a recognizable name in the **Display name** field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default is administrators. For more information, see [Allow contributors to use a connection for exports](connections.md#allow-contributors-to-use-a-connection-for-exports).

1. Provide your [LinkedIn Campaign Manager Account ID](https://www.linkedin.com/help/lms/answer/a424270).

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to Campaign Monitor.

1. Select **Authenticate with LinkedIn** and provide your admin credentials for LinkedIn Campaign Manager.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection.

## Configure an export

You can configure an export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to **Data** > **Exports**.

1. To create a new export, select **Add destination**.

1. In the **Connection for export** field, choose a connection from the LinkedIn Ads section. If you don't see this section name, there are no connections of this type available to you.

1. Choose whether you want to export data to do [contact targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/contact-targeting) or [company targeting](https://business.linkedin.com/marketing-solutions/ad-targeting/account-targeting) on LinkedIn. 

1. In the **Data matching** section, select at least one field that represents a customer's email address, Apple Ad ID, Google Ad ID, Google User ID, or First and last names, if you selected to export data to do contact targeting. If you selected to export data to do company targeting, select at least one field that represents a company's name, email domain, LinkedIn page URL, Stock symbol, or Website. Additional fields can be selected to further define your export. 

1. Select the segments you want to export. The matched audiences in LinkedIn Campaign Manager will automatically be created with the name of the segments that you selected to export. Each segment will result in a separate matched audience. 

1. Select **Save**.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-exports-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to LinkedIn Ads, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that LinkedIn Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).

Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to stop the use of this functionality.
