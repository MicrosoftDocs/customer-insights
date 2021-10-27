---
title: "Enrich customer profiles with data from Microsoft Office 365"
description: "Use proprietary data from Microsoft Office to enrich your customer profiles with engagement data."
ms.date: 10/27/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahl-MS
ms.author: jodahl
manager: skummer
---

# Enrich customer profiles with engagement data (preview)

Use proprietary data from Microsoft Office to enrich your customer profiles with engagement data. The engagement data consists of email and meeting activity aggregated to the account level. This enrichment is available in the following regions: UK, Europe, North America.

## Prerequisites

To configure engagement data, the following prerequisites must be met:

- You have an active Office 365 *cloud* license.
- You have [unified customer profiles](customer-profiles.md) based on accounts.
- You have [administrator](permissions.md#administrator) permissions.
- You have Office 365 tenant administrator permissions or can get consent to use aggregated Office data in CI from a Office 365 tenant administrator.

# Configure the enrichment

1. In audience insights, go to **Data** > **Enrichment**.

1. Go to the **Discover** tab and select **Enrich my data** on the **Account Engagement** tile.

## Office 365 administrator consent

## Running the Account Engagement enrichment for the first time



To configure interest affinities enrichment, go to the **Discover** tab and select **Enrich my data** on the **Interests** tile.

   > [!div class="mx-imgBorder"]
   > ![Brands and Interests tiles.](media/BrandsInterest-tile-Hub.png "Brands and Interest tiles")

## How the engagement data are aggregated



## Refresh enrichment

Run the enrichment after configuring brands, interests, and the field mapping for demographics. To start the process, select **Run** on the brand or interest configuration page. Additionally, you can let the system run the enrichment automatically as part of a scheduled refresh.

Depending on the size of your customer data, it may take several minutes for an enrichment run to complete.

> [!TIP]
> There are [six types of status](system.md#status-types) for tasks/processes. Additionally, most processes [depend on other downstream processes](system.md#refresh-policies). You can select the status of a process to see details on the progress of the entire job. After selecting **See details** for one of the job's tasks, you'll find additional information: processing time, the last processing date, and all errors and warnings associated with the task.

## Enrichment results

After running the enrichment process, go to **My enrichments** to review the total number of enriched customers and a breakdown of brands or interests in the enriched customer profiles.

:::image type="content" source="media/my-enrichments.png" alt-text="Preview of results after running the enrichment process.":::

Review the enriched data by selecting **View enriched data** in the chart. Enriched data for brands goes to the **BrandAffinityFromMicrosoft** entity. Data for interests is in the **InterestAffinityFromMicrosoft** entity. You'll also find these entities listed in the **Enrichment** group in **Data** > **Entities**.

You will see a chart with the number of enriched customer profiles over time and a preview of the enriched entity. Select **Show more** in the preview tile to open the enriched entity.

## See enrichment data on the customer card

Brand and interest affinities can also be viewed on individual customer cards. Go to **Customers** and select a customer profile. In the customer card, you'll find charts for the brands or interests that people in that customer's demographic profile have affinity for.

:::image type="content" source="media/enrichment-customer-card.png" alt-text="Customer card with enriched data.":::

## Create segments and measures based on the enriched data

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]


[!INCLUDE[footer-include](../includes/footer-banner.md)]
