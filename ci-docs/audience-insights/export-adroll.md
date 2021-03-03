---
title: "Export Customer Insights data to AdRoll"
description: "Learn how to configure the connection to AdRoll."
ms.date: 02/15/2021
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for AdRoll (preview)

Export segments of unified customer profiles to AdRoll and use them for advertising. 

## Prerequisites

-	You have an [AdRoll account](https://www.adroll.com/) and corresponding administrator credentials.
-	You have [configured segments](segments.md) in audience insights.
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Connect to AdRoll

1. Go to **Admin** > **Export destinations**.

1. Under **AdRoll**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

   :::image type="content" source="media/AdRoll_config.PNG" alt-text="Configuration pane for AdRoll connection.":::

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Select **Connect** to initialize the connection to AdRoll.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

1. Enter your **AdRoll Advertiser ID** [AdRoll Advertisable](https://help.adroll.com/hc/en-us/articles/212011838-Advertiser-Profiles).

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. It's required to export segments to AdRoll.

1. Select the segments you want to export. Select a segment with a least 100 members. You can't export smaller segments. Additionally the maximum size of a segment to export is 250'000 members per export. 

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab).

## Known limitations

- You can export up to 250'000 profiles in per export to AdRoll.
- You can't export segments with fewer than 100 profiles to AdRoll. 
- Exporting to AdRoll is limited to segments.
- Exporting up to 250'000 profiles to AdRoll can take up to 10 minutes to complete. 
- The number of profiles that you can export to AdRoll is dependent and limited on your contract with AdRoll.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to AdRoll, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that AdRoll meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
