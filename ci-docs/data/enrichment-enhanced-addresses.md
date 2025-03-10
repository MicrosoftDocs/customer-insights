---
title: "Enrich customer profiles with enhanced addresses"
description: "Enrich and normalize address information of customer profiles with Microsoft's models."
ms.date: 11/15/2022
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
searchScope: 
  - ci-data-sources-enrichment
  - ci-data-sources-enrichment-details
  - ci-enrichments
  - ci-enrichment-wizard
  - customerInsights
---

# Enrich customer profiles with enhanced addresses (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Addresses in your data can be unstructured, incomplete, or incorrect. Use Microsoft's models to normalize and enrich your addresses into the [Common Data Model format](/common-data-model/schema/core/applicationcommon/address) for better accuracy and insights.

You can also [enrich addresses on data sources](data-sources-enrichment.md) to improve the match accuracy in the data unification process. 

## How we enhance addresses

Our model goes through a two-step process to enhance an address. First, it parses the address to identify its components and puts them into a structured format. Then, we use AI to correct, complete, and standardize the values in the address.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=3ff1ab6f-d625-4cc3-a688-a8aa6b866e43]

### Example

Address information might be in a nonstandard format and contain spelling errors. The model can fix these issues and create consistent addresses in unified customer profiles.

```Input
4567 w main stret californa missouri 54321 us
```

```Output
- Street1: 4567 W Main St
- City: California
- StateOrProvince: MO
- ZipOrPostalCode: 54321
- CountryOrRegion: United States of America

- Address: 4567 W Main St, California, MO, 54321, United States of America
```

### Limitations

Enhanced addresses only work with the values that already exist in your ingested address data. The model doesn't:

1. Verify if the address is a valid address.
2. Verify if any of the values, such as ZIP codes or street names, are valid.
3. Change values it doesn't recognize.

The model uses machine learning-based techniques to enhance addresses. As with any machine learning-based model, 100 percent accuracy isn't guaranteed.

## Supported countries or regions

We currently support enriching addresses in these countries or regions:

- Australia
- Canada
- France
- Germany
- Italy
- Japan
- United Kingdom
- United States

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Enhanced addresses** tile.

   :::image type="content" source="media/enhanced-addresses-tile.png" alt-text="Screenshot of the Enhanced addresses tile.":::

1. Review the overview and then select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Select how addresses are formatted in your data set. Choose **Single-attribute address** if addresses in your data use a single field. Choose **Multiple-attribute address** if addresses in your data use more than one data field.

1. Select **Next** and map the address fields from your unified customer table.

    :::image type="content" source="media/enhanced-address-mapping.png" alt-text="Enhanced address field-mapping page.":::

   > [!NOTE]
   > Country/Region is mandatory in both single-attribute and multiple-attribute addresses. Addresses that don't contain valid or supported country/region values won't be enriched.

1. Select **Next** to complete the field mapping.

1. Provide a **Name** for the enrichment and the **Output table**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

The **Number of customers enriched by field** provides a drill-down into the coverage of each enriched field.

### Overview card

The **Customers changes overview** card shows details about the coverage of the enrichment:

- **Addresses processed and changed**: The number of customer profiles with addresses that were successfully enriched.
- **Addresses processed and not changed**: The number of customer profiles with addresses that were recognized but not changed. It typically happens when the input data is valid and can't be improved by the enrichment.
- **Addresses not processed and not changed**: The number of profiles with addresses that weren't recognized. Usually for input data that is invalid or not supported by the enrichment.

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
