---
title: "Data enrichment (preview) overview"
description: "Use capabilities from Microsoft and other third-party services to enrich your customer data."
ms.date: 11/15/2022
ms.reviewer: mhart

ms.topic: conceptual
author: jodahlMSFT
ms.author: jodahl
ms.collection: get-started
searchScope: 
  - ci-enrichments
  - ci-enrichment-details
  - ci-enrichment-wizard
  - customerInsights
---

# Data enrichment (preview) overview

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

Use data from sources like Microsoft and other partners to enrich your customer data. Third-party enrichments are configured using [connections](connections.md), which an administrator sets up with credentials and provides consent for data transfers. The connections can be used by administrators and contributors to configure enrichments.  

[!INCLUDE [public-preview-note](includes/public-preview-note.md)]

## Multiple enrichments of the same type

The table to be enriched is specified during the enrichment configuration, which allows you to enrich only a subset of your profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments will have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on each tile on the **Discover** tab of the **Enrichment** page.

## Enrich data sources before unification

You can enrich your customer data before data unification to help increase the quality of a data match. For more information, see [data source enrichment](data-sources-enrichment.md).

## Create an enrichment

You need to have Contributor or Administrator [permissions](permissions.md) to create or edit enrichments.

Go to **Data** > **Enrichment**. The **Discover** tab shows all supported enrichment options.

:::image type="content" source="media/enrichment-hub-page.png" alt-text="Enrichment hub page.":::

# [Individual consumers (B-to-C)](#tab/b2c)

- [AbiliTec Identity](enrichment-liveramp.md) provided by LiveRamp AbiliTec
- [Brands](enrichment-microsoft.md) provided by Microsoft
- [Demographics](enrichment-experian.md) provided by Experian
- [Enhanced addresses](enrichment-enhanced-addresses.md) provided by Microsoft
- [Interests](enrichment-microsoft.md) provided by Microsoft
- [Location data](enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [Location data](enrichment-here.md) provided by HERE Technologies
- [SFTP custom data](enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

# [Business accounts (B-to-B)](#tab/b2b)

- [Account engagement data](enrichment-office.md) provided by Microsoft
- [Company data](enrichment-dnb.md) provided by Dun & Bradstreet
- [Company data](enrichment-leadspace.md) provided by Leadspace
- [Enhanced addresses](enrichment-enhanced-addresses.md) provided by Microsoft
- [Enhanced company data](enrichment-enhanced-company-data.md) provided by Microsoft
- [Location data](enrichment-azure-maps.md) provided by Microsoft Azure Maps
- [Location data](enrichment-here.md) provided by HERE Technologies
- [SFTP custom data](enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP)

---

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

[!INCLUDE [footer-include](includes/footer-banner.md)]
