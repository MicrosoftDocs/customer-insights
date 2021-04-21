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

Our model goes through a two-step process to enhance an address. First, it parses the address to identify its components puts them into a structured format. Then, we use our Microsoft proprietary data to correct, complete, and standardize the values in the address.

### Example

Address information might be in a non-standard format and contain spelling errors. The model can fix these issues and create consistent addresses in unified customer profiles.

**Input**

```
4567 w main stret californa missouri 54321 us
```


**Output**

```
- Street1: 4567 W Main St
- City: California
- StateOrProvince: MO
- ZipOrPostalCode: 54321
- CountryOrRegion: United States of America

- Address: 4567 W Main St, California, MO, 54321, United States of America
```


## Supported countries or regions

We currently support enriching addresses in these countries or regions: 

- Australia
- Canada
- United Kingdom
- United States.

Addresses must contain a country/region value. We don't process addresses for countries or regions that aren't supported and addresses that have no country or region provided.

## Configure the enrichment

1. Go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the **Enhanced addresses** tile and select **Enrich my data**.

   :::image type="content" source="media/enhanced-addresses-tile.png" alt-text="Screenshot of the Enhanced addresses tile.":::

1. Select the **Customer data set** and choose the entity containing the addresses you want to enrich. You can select the *Customer* entity to enrich addresses in all your customer profiles or select a segment entity to enrich addresses only in customer profiles contained in that segment.

1. Select how addresses are formatted in your data set. Choose **Single-attribute address** if addresses in your data use a single field. Choose **Multiple-attribute address** if addresses in your data use more than one data field.

1.	Map the address fields from your unified customer entity. The Country/Region field is mandatory for multiple-attribute addresses. 

    :::image type="content" source="media/enhanced-address-mapping.png" alt-text="Enhanced address field-mapping page.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment

1. Select **Save enrichment** after reviewing your choices.

## Enrichment results

To start the enrichment process, select **Run** from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time depends on the size of your customer data.

After the enrichment process completes, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md), [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
