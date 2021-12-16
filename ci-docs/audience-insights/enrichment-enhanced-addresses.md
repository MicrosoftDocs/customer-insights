---
title: "Address enhancement enrichment (Video)"
description: "Enrich and normalize address information of customer profiles with Microsoft's models."
ms.date: 12/16/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# Enrichment of customer profiles with enhanced addresses

Addresses in your data can be unstructured, incomplete, or incorrect. Use Microsoft's models to normalize and enrich your addresses into the [Common Data Model format](/common-data-model/schema/core/applicationcommon/address) for better accuracy and insights.

## How we enhance addresses

Our model goes through a two-step process to enhance an address. First, it parses the address to identify its components and puts them into a structured format. Then, we use AI to correct, complete, and standardize the values in the address.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWNewo]

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

Enhanced addresses only works with the values that already exist in your ingested address data. The model doesn't: 

1. Verify if the address is a valid address.
2. Verify if any of the values, such as ZIP codes or street names, are valid.
3. Change values it doesn't recognize.

The model uses machine learning-based techniques to enhance addresses. While we apply a high confidence threshold for when the model changes an input value, as with any machine learning-based model, 100 percent accuracy is not guaranteed.

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

Addresses must contain a country/region value. We don't process addresses for countries or regions that aren't supported and addresses that have no country or region provided.

## Configure the enrichment

1. Go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the **Enhanced addresses** tile.

   :::image type="content" source="media/enhanced-addresses-tile.png" alt-text="Screenshot of the Enhanced addresses tile.":::

1. Select the **Customer data set** and choose the entity containing the addresses you want to enrich. You can select the *Customer* entity to enrich addresses in all your customer profiles or select a segment entity to enrich addresses only in customer profiles contained in that segment.

1. Select how addresses are formatted in your data set. Choose **Single-attribute address** if addresses in your data use a single field. Choose **Multiple-attribute address** if addresses in your data use more than one data field.

   > [!NOTE]
   > Country/Region is mandatory in both single-attribute and multiple-attribute addresses. Addresses that don't contain valid or supported country/region values won't be enriched.

1.	Map the address fields from your unified customer entity.

    :::image type="content" source="media/enhanced-address-mapping.png" alt-text="Enhanced address field-mapping page.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment and the output entity.

1. Select **Save enrichment** after reviewing your choices.

## Enrichment results

To start the enrichment process, select **Run** from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time depends on the size of your customer data.

After the enrichment process completes, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

### Overview card

The overview card shows details about the coverage of the enrichment. 

* **Customers processed and changed**: The number of customer profiles that were succesfully enriched.

* **Customers processed and not changed**: The number of customer profiles that were recognized but not changed. It typically happens when the input data is valid and can't be improved by the enrichment.

* **Customers not processed and not changed**: The number of profiles that were not recognized. Usually for input data that is invalid or not supported by the enrichment.

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]

[!INCLUDE[footer-include](../includes/footer-banner.md)]
