---
title: "Company data enhancement"
description: "Enrich and normalize company data with Microsoft's models."
ms.date: 06/10/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# Enrichment of company profiles with enhanced company data

Use Microsoft’s models and compiled company data to correct, supplement, and standardize your company profiles. We'll use the [Common Data Model format](/common-data-model/schema/core/applicationcommon/account) for better accuracy and insights.

You can also [enhance company data on data sources](data-sources-enrichment.md) to improve the match accuracy in the data unification process.

For public companies in the United States, information such as revenue, stock ticker, industry, and more is available.  

## How we enhance company data

Our model goes through a two-step process to enhance a company profile. First, it normalizes the company name. For example, *Microsft Corp* will be corrected and standardized to *Microsoft Corporation*. It tries to find a match in Microsoft's compiled company data. If a match is found, we enrich the company profile with information from our compiled company data, including the company name.

### Example

Your company information might not follow a standardized format and contain spelling errors. The model tries to fix these issues and create consistent information.

```Input
Microsft
```

```Output
- AccountName: Microsoft Corporation
- MainPhoneNumber: 8006427676
- Website: https://www.microsoft.com/
- Street1: One Microsoft Way
- City: Redmond
- StateOrProvince: Washington
- County: King
- ZipOrPostalCode: 98052
- CountryOrRegion: United States
```

## Limitations

The model doesn't:

- Confirm the identity of the company. We don't verify if the input is an existing organization or that a company uses the output as its standard name.
- Comprehensively cover companies globally. Microsoft’s compiled company data has global coverage, but offers most coverage in Australia, Canada, United Kingdom, and the United States.
- Standardize company addresses globally. We currently support standardizing addresses in these countries or regions: Australia, Canada, France, Germany, Italy, Japan, United Kingdom, and the United States.
- Guarantee accuracy or freshness of data. As business information often changes, we can't guarantee that the enhanced company data provided is always exact or up-to-date.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Enhanced company data** tile.

   :::image type="content" source="media/enhanced-company-data-tile.png" alt-text="Enrichment tile in the enrichment hub for company data.":::

1. Review the overview and then select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich. The *Customer* entity enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Select which type of fields from your company profiles to use for matching with Microsoft’s compiled company data. This selection will affect the mapping fields you have access to in the next step.

1. Select **Next**.

1. Map your company fields to the company data from Microsoft. For higher match accuracy, add more fields.

    :::image type="content" source="media/enhanced-company-data-mapping.png" alt-text="Data-mapping step when configuring a company enrichment.":::

1. Select **Next** to complete the field mapping.

1. Provide a **Name** for the enrichment and the **Output entity**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## Enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

### Overview card

The **Customers changes overview** tile shows details about the coverage of the enrichment

- **Companies processed and changed**: The number of customer company profiles that were successfully enriched.
- **Companies processed and not changed**: The number of customer company profiles that were recognized but not changed. This typically happens when the input data is valid and can't be improved by the enrichment.
- **Companies not processed and not changed**: The number of customer company profiles that weren't recognized. This typically happens for input data that are invalid or not supported by the enrichment.

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
