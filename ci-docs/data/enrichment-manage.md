---
title: "Enrich unified data (preview)"
description: "Use capabilities from Microsoft and other third-party services to enrich your unified customer data."
ms.date: 10/05/2023
ms.reviewer: mhart
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
ms.collection: get-started
ms.custom: sfi-image-nochange
---

# Enrich unified data (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Use enrichments to enhance your unified customer data. Create the connections for the specific enrichments so that administrators and contributors can configure the enrichments.

To help increase the quality of a data match, [enrich data sources before unification](data-sources-enrichment.md).

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Create an enrichment

You need to have Contributor or Administrator [permissions](user-roles.md) to create or edit enrichments.

Go to **Data** > **Enrichment**. The **Discover** tab shows all supported enrichment options.

:::image type="content" source="media/enrichment-hub-page.png" alt-text="Enrichment hub page.":::

- [AbiliTec Identity](enrichment-liveramp.md) provided by LiveRamp AbiliTec
- [Brands](enrichment-microsoft.md) provided by Microsoft
- [Demographics](enrichment-experian.md) provided by Experian
- [Enhanced addresses](enrichment-enhanced-addresses.md) provided by Microsoft
- [Interests](enrichment-microsoft.md) provided by Microsoft
- [Location data](enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [SFTP custom data](enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

## Manage existing enrichments

Go to **Data** > **Enrichment**. On the **My enrichments** tab, view the configured enrichments, their status, number of enriched customers, and the last time the data was refreshed. You can sort the list of enrichments by any column or use the search box to find the enrichment you want to manage.

Select the enrichment to view available actions.

:::image type="content" source="media/enrichment-hub-options-run.png" alt-text="Options to manage enrichments in the list of enrichments.":::

- **View** enrichment details with the number of enriched customer profiles.
- **Edit** the enrichment configuration.
- [**Run**](#run-or-refresh-enrichments) the enrichment to update customer profiles with the latest data. Run multiple enrichments at once by selecting them in the list.
- **Activate** or **Deactivate** an enrichment. Inactive enrichments won't get refreshed during a [scheduled refresh](schedule-refresh.md).
- **Delete** the enrichment.

You can also create [segments](segments.md) or [measures](measures.md) from enrichments.

## Run or refresh enrichments

Once run, enrichments can be refreshed on an automatic schedule or refreshed manually on demand.

1. To manually refresh one or more enrichments, select them and choose **Run**. To [schedule an automatic refresh](schedule-refresh.md), go to **Settings** > **System** > **Schedule**. The processing time depends on the size of your customer data.

1. Optionally, [see the progress of the enrichment process](#see-the-progress-of-the-enrichment-process).

1. After the enrichment process completes, go to **My enrichments** to review the newly enriched customer profiles data, the time of the last update, and the number of enriched profiles.

1. Select the enrichment to see [enrichment results](#view-enrichment-results).

### See the progress of the enrichment process

You can find details about the processing of an enrichment, including its status and potential issues while it's refreshing or after a refresh completed. Understand which processes are involved to refresh an enrichment and how long it took to run the processes. The enrichment status is supported for Experian, Leadspace, HERE Technologies, SFTP Import, and Azure Maps.

1. Go to **Data** > **Enrichment**.
1. In the **My enrichments** tab, select the status of the enrichment to open a side pane.
1. In the **Progress details** pane, expand the **Enrichments** section.
1. Under the enrichment you want to see the progress, select **See details**.
1. In the **Task details** pane, select **Show details** to see the processes that are involved in updating the enrichment and their status.

[!INCLUDE [progress-details-pane](includes/progress-details-pane.md)]

## View enrichment results

After a completed enrichment run, review the enrichment results.

1. Go to **Data** > **Enrichment**.
1. In the **My enrichments** tab, select the enrichment that you want to view.

All enrichments show basic information such as the number of enriched profiles and the number of enriched profiles over time. The **Enriched customers preview** tile shows a sample of the generated enrichment table. To see a detailed view, select **See more** and select the **Data** tab.

:::image type="content" source="media/enrichments-results.png" alt-text="Enrichments results page.":::

If available, the **Number of customers enriched by field** provides a drill-down into the coverage of each enriched field.

Some enrichments also show information specific to the type of enrichment. For more information, see the related documentation.
