---
title: "Address enhancement enrichment"
description: "Enrich and normalize address information of customer profiles with Microsoft proprietary data."
ms.date: 04/21/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# Enrichment of customer profiles with enhanced addresses

Addresses in your data can be unstructured, incomplete, or incorrect. Use Microsoft proprietary data and models to normalize and enrich your addresses into the [Common Data Model format](/common-data-model/schema/core/applicationcommon/address) for better accuracy and insights.

## How we enhance addresses

Our model performs a two-step process to enhance an address. First, it parses the address to identify its components puts them into a structured format. Then, we use our Microsoft proprietary data to correct, complete, and standardize the values in the address.

For example, an address might be in a non-standard format and contain spelling errors. For countries/regions that are supported, we can fix these issues and create a consistent way to list addresses in unified customer profiles.

## Supported countries/regions

We currently support enriching addresses in these countries/regions: 

- Australia
- Canada
- United Kingdom
- United States.

Addresses must contain a country/region value. Addresses that don't contain country/region or contain a country/region that’s not supported will not be processed.

## Configure the enrichment

1. Go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the **Enhanced addresses** tile and select **Enrich my data**.

   :::image type="content" source="media/enhanced-addresses-tile.png" alt-text="Screenshot of the Enhanced addresses tile.":::

1. Select the **Customer data set** and choose the entity containing the addresses you want to enrich. You can select the *Customer* entity to enrich addresses in all your customer profiles or select a segment entity to enrich addresses only in customer profiles contained in that segment.

1. Select how addresses are formatted in your data set. Choose **Single-attribute address** if addresses in your data uses a single field. Choose **Multiple-attribute address** if addresses in your data use more than one data field.

1.	Map the address fields from your unified customer entity. The Country/Region field is mandatory for multiple-attribute addresses. 

   :::image type="content" source="media/enhanced-address-mapping.png" alt-text="Enhanced address field mapping page.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment

1. Select **Save enrichment** after reviewing your choices.

## Configure the connection for Leadspace 

You need to be an administrator to configure connections. Select **Add connection** when configuring an enrichment *or* go to **Admin** > **Connections** and select **Set up** on the Leadspace tile.

1. Select **Get Started** 

1. Enter a name for the connection in the **Display name** box.

1. Provide a valid Leadspace token.

1. Review and provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.
   
   :::image type="content" source="media/enrichment-Leadspace-connection.png" alt-text="Leadspace connection configuration page.":::

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
