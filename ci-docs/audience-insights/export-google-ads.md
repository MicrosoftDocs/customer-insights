---
title: "Export Customer Insights data to Google Ads"
description: "Learn how to configure the connection and export to Google Ads."
ms.date: 11/18/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Export segment lists to Google Ads (preview)

Export segments of unified customer profiles to Google Ads audience list and use them to advertise on Google Search, Gmail, YouTube, and Google Display Network. 

## Prerequisites for connection

-	You have a [Google Ads account](https://ads.google.com/) and corresponding administrator credentials.
-	There are existing audiences in Google Ads and the corresponding IDs. For more information, see [Google Ads audiences](https://support.google.com/google-ads/answer/7558048?hl=en#:~:text=Audience%20lists%20is%20a%20section,Display%20Network%20through%20remarketing%20campaigns.).
-	You have [configured segments](segments.md)
-	Unified customer profiles in the exported segments contain fields representing an email address, first name, and last name

## Known limitations

- Up to 1 million profiles per export to Google Ads.
- Exporting to Google Ads is limited to segments.
- Exporting segments with a total of 1 million profiles can take up to 5 minutes because of limitations on the provider side. 
- The matching in Google Ads can take up to 48 hours.

## Setup connection to Google Ads

1. Go to **Admin** > **Connections**.

1. Select **Add connection** and choose **Google Ads** to configure the connection.

1. Give your connection a recognizable name in the Display name field. The name and the type of the connection describe this connection. We recommend choosing a name that explains the purpose and target of the connection.

1. Choose who can use this connection. If you take no action, the default will be Administrators. For more information, see [Allow contributors to use a connection for exports](connection.md#allow-contributors-to-use-a-connection-for-exports).

1. Enter your **[Google Ads customer ID](https://support.google.com/google-ads/answer/1704344)**.

1. Enter your **[Google Ads approved developer token](https://developers.google.com/google-ads/api/docs/first-call/dev-token)**.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Authenticate with Google Ads** and provide your Google Ads credentials.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Select **Save** to complete the connection. 

## Configure an export

You can configure this export if you have access to a connection of this type. For more information, see [Permissions needed to configure an export](export-destinations.md#set-up-a-new-export).

1. Go to Data > Exports.

1. To create a new export, select Add destination.

1. In Connection for export choose a connection from the Google Ads section. If you don't see this section name, there are no connections of this type available to you.

1. Enter your **[Google Ads audience ID](https://support.google.com/google-ads/answer/7558048?hl=en#:~:text=Audience%20lists%20is%20a%20section,Display%20Network%20through%20remarketing%20campaigns.)** and select **Connect** to initialize the connection to Google Ads.

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. Repeat the same steps for **First name" and **Last name** fields.

1. Select the segments you want to export. You can export up to 1 million customer profiles in total to Google Ads.

Saving an export doesn't run the export immediately.

The export runs with every [scheduled refresh](system.md#schedule-tab). 
You can also [export data on demand](export-destinations.md#run-export-on-demand). 


## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Google Ads, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Google Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
