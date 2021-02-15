---
title: "Enrichment of company profiles with the third-party enrichment Leadspace"
description: "General information about the Leadspace third-party enrichment."
ms.date: 11/24/2020
ms.reviewer: kishorem
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Enrichment of company profiles with Leadspace (preview)

Leadspace is a data science company that provides a B2B Customer Data Platform. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include additional attributes such as company size, location, industry, and more.

## Prerequisites

To configure Leadspace, the following prerequisites must be met:

- You have an active Leadspace license and the “perpetual key” (referred to as **Leadspace token**). Contact directly [Leadspace](https://www.leadspace.com/products/leadspace-on-demand/) for details about their product.
- You have [Administrator](permissions.md#administrator) permissions.
- You have [unified customer profiles](customer-profiles.md) for companies.

## Configuration

1. In audience insights, go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the Leadspace tile.

   :::image type="content" source="media/leadspace-tile.png" alt-text="Screenshot of the Leadspace tile.":::

1. Select **Get Started** and then enter an active **Leadspace token** (perpetual key). Review and provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox. Confirm both inputs by selecting **Connect to Leadspace**.

1. Select **Map data** and choose the data set you want to enrich with company data from Leadspace. You can select the *Customer* entity to enrich all your customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

   :::image type="content" source="media/enrichment-leadspace-select-segment.png" alt-text="Choose between customer profile and segment enrichment.":::

1. Click **Next** and define which fields from your unified profiles should be used to look for matching company data from Leadspace. The **Name of company** field is required. For a higher match accuracy, up to two other fields, **Company website** and **Company location**, can be added.

   :::image type="content" source="media/enrichment-leadspace-mapping.png" alt-text="Leadspace field mapping pane.":::
   
1. Select **Apply** to complete the field mapping.

1. Select **Run** to enrich the company profiles. How long an enrichment takes depends on the number of unified customer profiles.

## Enrichment results

After refreshing the enrichment, you can review the newly enriched company data under [My enrichments](enrichment-hub.md). You can find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

For more information, see [Leadspace APIs](https://support.leadspace.com/hc/en-us/sections/201997649-API).

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md), [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Leadspace, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Leadspace meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]