---
title: "Export Customer Insights data to Mailchimp"
description: "Learn how to configure the connection to Mailchimp."
ms.date: 10/26/2020
ms.reviewer: philk
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Connector for Mailchimp (preview)

Export segments of unified customer profiles to Mailchimp to create newsletters and email campaigns.

## Prerequisites

-	You have a [Mailchimp account](https://mailchimp.com/) and corresponding administrator credentials.
-	There are existing audiences in Mailchimp and the corresponding IDs. For more information, see [Mailchimp audiences](https://mailchimp.com/help/create-audience/).
-	You have [configured segments](segments.md)
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Connect to Mailchimp

1. Go to **Admin** > **Export destinations**.

1. Under **Mailchimp**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Select **I agree** to confirm the **Data privacy and compliance**.

1. Enter your **[Mailchimp audience ID](https://mailchimp.com/help/find-audience-id/)** and select **Connect** to initialize the connection to Mailchimp.

1. Select **Authenticate with Mailchimp** and provide your Mailchimp credentials.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

   :::image type="content" source="media/export-connect-mailchimp.png" alt-text="Export screenshot for Mailchimp connection":::

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that representes a customer's email address. 

1. Optionally, you can export **First name** and **Last name** as additional fields to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export. You can export up to 1 million customer profiles in total to Mailchimp.

   :::image type="content" source="media/export-segments-mailchimp.png" alt-text="Select fields and segments to export to Mailchimp":::

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab). In Mailchimp, you can now find your segments under [Mailchimp audiences](https://mailchimp.com/help/create-audience/).

## Known limitations

- Up to 1 million profiles per export to Mailchimp.
- Exporting to Mailchimp is limited to segments.
- Exporting a segment or several segments with a total of 1 million profiles can take up to three hours due to limitations on the provider side. 
- The amount of profiles that you can export to Mailchimp is dependent and limited on your contract with Mailchimp.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Mailchimp, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Mailchimp meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.
