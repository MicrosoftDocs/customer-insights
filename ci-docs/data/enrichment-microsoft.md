---
title: "Enrich customer profiles with brands and interests data from Microsoft (preview)"
description: "Use proprietary data from Microsoft to enrich your customer data with affinities and share of voice."
ms.date: 11/15/2022
ms.reviewer: mhart
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
searchScope: 
  - ci-enrichments
  - ci-enrichment-wizard
  - customerInsights
---

# Enrich customer profiles with brands and interests data from Microsoft (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Use Microsoft's proprietary data to enrich your customer data with brand affinities, interest affinities, and share of voice (SoV). These affinities and SoV are based on data from people with demographics similar to your customers. This information helps you to better understand and segment your customers based on their affinities or SoV to specific brands and interests.

## How we determine affinities and SoV

We use Microsoft’s online search data to find affinities and SoV for brands and interests across various demographic segments (defined by age, gender, or location). The online search volume for a brand or interest forms the basis for determining the affinity or SoV. However, each provides a different perspective to understanding your customers.

- Affinity is a comparative across demographic segments. You can use this information to identify demographic segments that have the highest affinity for a given brand or interest, compared to other segments.

- Share of voice is a comparative across your selected brands or interests. You can use this information to identify which brand or interest has the highest share-of-voice for a given demographic segment, compared to other brands or interests you selected.

## Affinity level and score

On every enriched customer profile, we provide two related values: affinity level and affinity score. These values help you determine how strong the affinity is for that profile’s demographic segment, for a brand or interest, as compared to other demographic segments.

*Affinity level* consists of four levels and *affinity score* is calculated on a 100-point scale that maps to the affinity levels.

|Affinity level |Affinity score  |
|---------|---------|
|Very high     | 85-100       |
|High     | 70-84        |
|Medium     | 35-69        |
|Low     | 1-34        |

Depending on the granularity you would like for measuring the affinity, you can use either affinity level or score. Affinity score gives you more precise control.

## Share of voice (SoV)

We calculate SoV on a 100-point scale. The total SoV across all brands or interests for every enriched customer profile adds up to 100. Unlike affinities, SoV is relative to the brands and interests you select. For example, the SoV values for 'Microsoft' can be different if the selected brands are ('Microsoft', 'GitHub') versus ('Microsoft', 'LinkedIn').

## Supported countries/regions

We currently support the following country/region options: Australia, Canada (English), France, Germany, United Kingdom, or United States (English).

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

   - To configure brand affinities and SoV enrichment, select **Enrich my data** on the **Brands** tile.

   - To configure interest affinities and SoV enrichment, select **Enrich my data** on the **Interests** tile.

   > [!div class="mx-imgBorder"]
   > ![Brands and Interests tiles.](media/BrandsInterest-tile-Hub.png "Brands and Interest tiles")

1. Review the overview and then select **Next**.

1. To change your country or region, select **Change** next to **Country/Region**. In the **Country/Region settings** pane, choose a [supported country/region](#supported-countriesregions) and select **Apply**.

   > [!NOTE]
   > When choosing your own brands, the system provides suggestions based on the selected country or region. When choosing an industry, you'll get the most relevant brands or interests based on the selected country or region.

1. Choose up to five brands or interests using one or both of these options:

   - **Industry**: Select your industry from the dropdown list and then choose from the top brands or interests for that industry.
   - **Choose your own**: Enter a brand or interest that is relevant to your organization and then choose from the matching suggestions. If we don't list a brand or interest you're looking for, send us feedback using the **Suggest** link.

1. Select **Next** and review your default enrichment preferences and update them as needed.

   :::image type="content" source="media/affinity-enrichment-preferences.png" alt-text="Screenshot of the enrichment preferences window.":::

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with data from Microsoft. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Select **Next**.

1. Map your fields from your unified customer table to the Microsoft data.

   > [!NOTE]
   > At least Date of Birth or Gender attributes are required. Country/Region and at least City (and State/Province) or Postal code are required. We recommend that date of birth is converted to DateTime type during data ingestion. Alternatively, it can be a string in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format "yyyy-MM-dd" or "yyyy-MM-ddTHH:mm:ss".

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment. The **Output table name** is automatically selected.

   :::image type="content" source="media/enrichment-interests-summary.png" alt-text="Interests review and naming page.":::

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

   When enriching profiles, we'll enrich all customer profiles for which we get data for the selected brands and interests, including profiles that are not in the selected country or region. For example, if you selected Germany, we'll enrich profiles located in the United States if we have data available for the selected brands and interests in the US.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

:::image type="content" source="media/my-enrichments.png" alt-text="Preview of results after running the enrichment process.":::

The results include **Affinity Level** or **Share of Voice** charts.

The tables created from the enrichments are listed under the **Enrichment** group in **Data** > **Tables** > **Output**. Enriched data for brands goes to the **BrandAffinityFromMicrosoft** and **BrandShareOfVoiceFromMicrosoft** tables. Data for interests is in the **InterestAffinityFromMicrosoft** and **InterestShareOfVoiceFromMicrosoft** tables.

## See enrichment data on the customer card

Brand and interest SoV can also be viewed on individual customer cards. Go to **Customers** and select a customer profile. In the customer card, you'll find charts for the brand or interest SoV based on people in that customer's demographic profile.

:::image type="content" source="media/enrichment-customer-card.png" alt-text="Customer card with enriched data.":::

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]


[!INCLUDE [footer-include](includes/footer-banner.md)]
