---
title: "Enrich customer profiles with data from Microsoft"
description: "Use proprietary data from Microsoft to enrich your customer data with affinities and share of voice."
ms.date: 11/11/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-MS
ms.author: kishorem
manager: shellyha
---

# Enrich customer profiles with affinities and share of voice (preview)

Use Microsoft's proprietary data to enrich your customer data with brand affinities, interest affinities, and share of voice (SoV). These affinities and SoV are based on data from people with demographics similar to your customers. This information helps you to better understand and segment your customers based on their affinities or SoV to specific brands and interests.

In audience insights, go to **Data** > **Enrichment** to [configure and view enrichments](enrichment-hub.md).

To configure brand affinities enrichment, go to the **Discover** tab and select **Enrich my data** on the **Brands** tile.

To configure interest affinities enrichment, go to the **Discover** tab and select **Enrich my data** on the **Interests** tile.

   > [!div class="mx-imgBorder"]
   > ![Brands and Interests tiles.](media/BrandsInterest-tile-Hub.png "Brands and Interest tiles")

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

To select a country or region, open **Brands enrichment** or **Interest enrichment** and select **Change** next to **Country/Region**. In the **Country/Region settings** pane, choose an option and select **Apply**.

### Implications related to country selection

- When [choosing your own brands](#define-your-brands-or-interests), the system provides suggestions based on the selected country or region.

- When [choosing an industry](#define-your-brands-or-interests), you'll get the most relevant brands or interests based on the selected country or region.

- When [enriching profiles](#refresh-enrichment), we'll enrich all customer profiles for which we get data for the selected brands and interests, including profiles that are not in the selected country or region. For example, if you selected Germany, we'll enrich profiles located in the United States if we have data available for the selected brands and interests in the US.

## Configure enrichment

A guided experience helps you through the configuration of the enrichments. 

### Define your brands or interests

Choose up to five brands or interests using one or both of these options:

- **Industry**: Select your industry from the dropdown list and then choose from the top brands or interests for that industry.
- **Choose your own**: Enter a brand or interest that is relevant to your organization and then choose from the matching suggestions. If we don't list a brand or interest you're looking for, send us feedback using the **Suggest** link.

### Review enrichment preferences

Review your default enrichment preferences and update them as needed.

:::image type="content" source="media/affinity-enrichment-preferences.png" alt-text="Screenshot of the enrichment preferences window.":::

### Select entity to enrich

Select **Enriched entity** and choose the data set you want to enrich with data from the Microsoft. You can select the Customer entity to enrich all your customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

### Map your fields

Map fields from your unified customer entity to define the demographic segment you want the system to use for enriching your customer data. Map Country/Region and at least Date of Birth or Gender attributes. Additionally, you must map at least one of City (and State/Province) or Postal code. Select **Edit** to define the mapping of the fields and select **Apply** when you're done. Select **Save** to complete the field mapping.

The following formats and values are supported (values are not case-sensitive):

- **Date of Birth**: We recommend that date of birth is converted to DateTime type during data ingestion. Alternatively, it can be a string in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format "yyyy-MM-dd" or "yyyy-MM-ddTHH:mm:ss".
- **Gender**: Male, Female, Unknown.
- **Postal code**: Five-digit ZIP codes for United States, standard postal code everywhere else.
- **City**: City name in English.
- **State/Province**: Two-letter abbreviation for the US and Canada. Two- or three-letter abbreviation for Australia. Not applicable for France, Germany, or the UK.
- **Country/Region**:

  - US: United States of America, United States, USA, US, America
  - CA: Canada, CA
  - GB: United Kingdom, UK, Great Britain, GB, United Kingdom of Great Britain and Northern Ireland, United Kingdom of Great Britain
  - AU: Australia, AU, Commonwealth of Australia
  - FR: France, FR, French Republic
  - DE: Germany, German, Deutschland, Allemagne, DE, Federal Republic of Germany, Republic of Germany

## Review and name the enrichment

Finally, you get to review the information and provide a name for the enrichment.

:::image type="content" source="media/enrichment-interests-summary.png" alt-text="Interests review and naming page.":::

## Refresh enrichment

Run the enrichment after configuring brands, interests, and the field mapping for demographics. To start the process, select **Run** on the brand or interest configuration page. Additionally, you can let the system run the enrichment automatically as part of a scheduled refresh.

Depending on the size of your customer data, it may take several minutes for an enrichment run to complete.

[!INCLUDE [progress-details-include](../includes/progress-details-pane.md)]

## Enrichment results

After running the enrichment process, go to **My enrichments** to review the total number of enriched customers and a breakdown of brands or interests in the enriched customer profiles.

:::image type="content" source="media/my-enrichments.png" alt-text="Preview of results after running the enrichment process.":::

You'll find a chart with the number of enriched customer profiles over time and previews of the enriched entities. Review the enriched data by selecting **See more** in the **Affinity Level** or **Share of Voice** charts. Enriched data for brands goes to the **BrandAffinityFromMicrosoft** and **BrandShareOfVoiceFromMicrosoft** entities. Data for interests is in the **InterestAffinityFromMicrosoft** and **InterestShareOfVoiceFromMicrosoft** entities. You'll also find these entities listed in the **Enrichment** group in **Data** > **Entities**.

## See enrichment data on the customer card

Brand and interest SoV can also be viewed on individual customer cards. Go to **Customers** and select a customer profile. In the customer card, you'll find charts for the brand or interest SoV based on people in that customer's demographic profile.

:::image type="content" source="media/enrichment-customer-card.png" alt-text="Customer card with enriched data.":::

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]


[!INCLUDE[footer-include](../includes/footer-banner.md)]
