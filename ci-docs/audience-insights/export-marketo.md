---
title: "Export Customer Insights data to Marketo"
description: "Learn how to configure the connection to Marketo."
ms.date: 11/12/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: phkieffer
ms.author: philk
manager: shellyha
---

# Connector for Marketo (preview)

Export segments of unified customer profiles to generate campaigns, provide email marketing and use specific groups of customers with Marketo.

## Prerequisites

-	You have a [Marketo account](https://login.marketo.com/) and corresponding administrator credentials.
-	There are existing lists in Marketo and the corresponding IDs. For more information, see [Marketo lists](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists).
-	You have [configured segments](segments.md).
-	Unified customer profiles in the exported segments contain a field representing an email address.

## Connect to Marketo

1. Go to **Admin** > **Export destinations**.

1. Under **Marketo**, select **Set up**.

1. Give your export destination a recognizable name in the **Display name** field.

1. Enter your **[Marketo client ID, Client secret and REST Endpoint Hostname](https://developers.marketo.com/rest-api/authentication/)**.

1. Enter your **[Marketo list ID](https://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists)** 

1. Select **I agree** to confirm the **Data privacy and compliance** and select **Connect** to initialize the connection to Marketo.

1. Select **Add yourself as export user** and provide your Customer Insights credentials.

   :::image type="content" source="media/export-connect-marketo.png" alt-text="Export screenshot for Marketo connection":::

1. Select **Next** to configure the export.

## Configure the connector

1. In the **Data matching** section, in the **Email** field, select the field in your unified customer profile that represents a customer's email address. 

1. Optionally, you can export **First name**, **Last name**, **City**, **State**, and **Country/Region**  as additional fields to create more personalized emails. Select **Add attribute** to map these fields.

1. Select the segments you want to export. You can export up to 1 million customer profiles in total to Marketo.

   :::image type="content" source="media/export-segment-marketo.png" alt-text="Select fields and segments to export to Marketo":::

1. Select **Save**.

## Export the data

You can [export data on demand](export-destinations.md). The export will also run with every [scheduled refresh](system.md#schedule-tab). In Marketo, you can now find your segments under [Marketo lists](ttps://docs.marketo.com/display/public/DOCS/Understanding+Static+Lists).

## Known limitations

- Up to 1 million profiles per export to Marketo.
- Exporting to Marketo is limited to segments.
- Exporting segments with a total of 1 million profiles can take up to 3 hours. 
- The number of profiles that you can export to Marketo is dependent and limited on your contract with Marketo.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Marketo, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Marketo meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this export destination at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]