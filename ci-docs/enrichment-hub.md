---
title: "Enrich unified customer profiles"
description: "Use capabilities to enrich your customer data."
ms.date: 06/10/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: conceptual
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
ms.custom: intro-internal
searchScope: 
  - ci-enrichments
  - ci-enrichment-details
  - ci-enrichment-wizard
  - customerInsights
---

# Enrichment for customer profiles (preview)

Use data from sources like Microsoft and other partners to enrich your customer data.

:::image type="content" source="media/enrichment-hub-page.png" alt-text="Enrichment hub page.":::

Go to **Data** > **Enrichment** to work with enrichment options.  

You need to have Contributor or Administrator permissions to create or edit enrichments. For more information, see [Permissions](permissions.md).

On the **Discover** tab, you'll find all supported enrichment options.

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

On the **My enrichments** tab, you can see the enrichments you've configured and edit their properties. You also have the option to create [segments](segments.md) or [measures](measures.md) from an enrichment.

## Manage existing enrichments

Go to the **My enrichments** tab to see all configured enrichments. Each enrichment is represented as a row that includes additional information about the enrichment.

Select the enrichment to see the available options. You can also select the vertical ellipsis (&vellip;) on a list item to see the options. If you configured several enrichments, you can use the search box to find it quickly.

:::image type="content" source="media/enrichment-hub-options-run.png" alt-text="Options to manage enrichments in the list of enrichments.":::

- **View** enrichment details with the number of enriched customer profiles.
- **Edit** the enrichment configuration.
- **Run** the enrichment to update customer profiles with the latest data.
- **Deactivate** an existing enrichment to stop it from refreshing automatically with every scheduled refresh. Data from the last successful refresh will continue to be available. **Activate** an inactive enrichment to restart automatic refreshing with every scheduled refresh.
- **Delete** the enrichment.

Run or deactivate multiple enrichments at once by selecting them in the list. View and edit options aren't available as bulk action. They only work for one enrichment at a time.

## Enrichments and connections

Third-party enrichments are configured using [connections](connections.md), which an administrator sets up with credentials and provides consent for data transfers. The connections can be used by administrators and contributors to configure enrichments.  

## Multiple enrichments of the same type

The entity to be enriched is specified during the enrichment configuration, which allows you to enrich only a subset of your profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments will have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on each tile on the **Discover** tab of the **Enrichment** page.

## Enrich data sources before unification

You can enrich your customer data before data unification to help increase the quality of a data match. For more information, see [data source enrichment](data-sources-enrichment.md).

## Run or refresh an enrichment

1. To start the enrichment process, select **Run**. Or, let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time depends on the size of your customer data.

1. Optionally, [see the progress of the enrichment process](#see-the-progress-of-the-enrichment-process).

1. After the enrichment process completes, go to **My enrichments** to review the newly enriched customer profiles data, the time of the last update, and the number of enriched profiles.

1. Select the enrichment to see [enrichment results](#enrichment-results).

### See the progress of the enrichment process

You can find details about the processing of an enrichment, including it status and potential issues while it's refreshing or after a refresh completed. Understand which processes are involved to refresh an enrichment and how long it took to run the processes. The enrichment status is supported for Experian, Leadspace, HERE Technologies, SFTP Import, and Azure Maps.

1. Go to **Data** > **Enrichment**.
1. In the **My enrichments** tab, select the status of an enrichment to open a side pane.
1. In the **Progress details** pane, expand the **Enrichments** section.
1. Under the enrichment you want to see the progress, select **See details**.
1. In the **Task details** pane, select **Show details** to see the processes that are involved in updating the enrichment and their status.

## Enrichment results

After a completed enrichment run, review the enrichment results.

1. Go to **Data** > **Enrichment**.
1. In the **My enrichments** tab, select the enrichment that you want information about.

All enrichments show basic information such as the number of enriched profiles and the number of enriched profiles over time. The **Enriched customers preview** tile shows a sample of the generated enrichment entity. To see a detailed view, select **See more** and select the **Data** tab.

:::image type="content" source="media/enrichments-results.png" alt-text="Enrichments results page.":::

If available, the **Number of customers enriched by field** provides a drill-down into the coverage of each enriched field.

Some enrichments also show information specific to the type of enrichment. Refer to the documentation for the relevant enrichment for more information.

[!INCLUDE [footer-include](includes/footer-banner.md)]
