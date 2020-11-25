---
title: "Export Customer Insights data to Google Ads"
description: "Learn how to configure the connection to Google Ads."
ms.date: 11/18/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Google Ads (preview)

Export segments of unified customer profiles to Google Ads audience list and use them to advertise on Google Search, Gmail, YouTube, and Google Display Network. 

## Prerequisites

-	You have a [Google Ads account](https://ads.google.com/) and corresponding administrator credentials.
-	There are existing audiences in Google Ads and the corresponding IDs. For more information, see [Google Ads audiences](https://support.google.com/google-ads/answer/7558048?hl=en#:~:text=Audience%20lists%20is%20a%20section,Display%20Network%20through%20remarketing%20campaigns.).
-	You have [configured segments](segments.md)
-	Unified customer profiles in the exported segments contain fields representing an email address, first name, and last name

## Connect to Google Ads

1. Go to **Admin** > **Export destinations**.

1. Under **Google Ads**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your **[Google Ads customer ID](https://support.google.com/google-ads/answer/1704344)**.

1. Enter your **[Google Ads approved developer token](https://developers.google.com/google-ads/api/docs/first-call/dev-token)**.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Enter your **[Google Ads audience ID](https://support.google.com/google-ads/answer/7558048?hl=en#:~:text=Audience%20lists%20is%20a%20section,Display%20Network%20through%20remarketing%20campaigns.)** and select **Connect** to initialize the connection to Google Ads.

1. Select **Authenticate with Google Ads** and provide your Google Ads credentials.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

   :::image type="content" source="media/export-segments-googleads.PNG" alt-text="Export screenshot for Google Ads connection":::

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. Repeat the same steps for **First name" and **Last name** fields.

1. Select the segments you want to export. You can export up to 1 million customer profiles in total to Google Ads.

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab). In Google Ads, you can now find your segments under [Google Ads audiences](https://support.google.com/google-ads/answer/7558048?hl=en/).

## Known limitations

- Up to 1 million profiles per export to Google Ads.
- Exporting to Google Ads is limited to segments.
- Exporting segments with a total of 1 million profiles can take up to 5 minutes because of limitations on the provider side. 
- The matching in Google Ads can take up to 48 hours.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Google Ads, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Google Ads meet any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
