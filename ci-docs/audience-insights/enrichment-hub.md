---
title: "Enrich unified customer profiles"
description: "Use capabilities to enrich your customer data."
ms.date: 09/30/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
ms.custom: intro-internal
---

# Enrichment for customer profiles (preview)

Use data from sources like Microsoft and other partners to enrich your customer data.

:::image type="content" source="media/enrichment-hub-page.png" alt-text="Enrichment hub page.":::

In audience insights, go to **Data** > **Enrichment** to work with enrichment options.  

You need to have Contributor or Administrator permissions to create or edit enrichments. For more information, see [Permissions](permissions.md).

On the **Discover** tab, you'll find all supported enrichment options.

# [Individual consumers (B2C)](#tab/b2c)

- [Brands](enrichment-microsoft.md) provided by Microsoft
- [Interests](enrichment-microsoft.md) provided by Microsoft
- [Enhanced addresses](enrichment-enhanced-addresses.md) provided by Microsoft 
- [Demographics](enrichment-experian.md) provided by Experian
- [Custom data](enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP) 
- [Azure Maps](enrichment-azure-maps.md) provided by Microsoft

# [Business accounts (B-to-B)](#tab/b2b)

- [Company data](enrichment-leadspace.md) provided by Leadspace
- [Enhanced addresses](enrichment-enhanced-addresses.md) provided by Microsoft 
- [Location data](enrichment-here.md) provided by HERE Technologies 
- [Custom data](enrichment-SFTP-custom-import.md) through Secure File Transfer Protocol (SFTP) 
- [Azure Maps](enrichment-azure-maps.md) provided by Microsoft

---

On the **My enrichments** tab, you can see the enrichments you've configured and edit their properties.

## Manage existing enrichments

Go to the **My enrichments** tab to see all configured enrichments. Each enrichment is represented as a row that includes additional information about the enrichment.

Select the enrichment to see the available options. You can also select the ellipsis (...) on a list item to see the options. If you configured several enrichments, you can use the search box to find it quickly.

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

The entity to be enriched is specified during the enrichment configuration, which allows you to enrich only a subset of your profiles. For example, enrich data only for a specific segment. You can configure several enrichments of the same type and reuse the same connection. Some enrichments will have limits to the number of enrichments of the same type that can be created. The limits and current use can be seen on the **Enrichment** page.

## See the progress of the enrichment process

You can find details about the processing of an enrichment, including it status and potential issues while it's refreshing or after a refresh completed. Understand which processes are involved to refresh an enrichment and how long it took to run the processes. The enrichment status is supported for Experian, Leadspace, HERE Technologies, SFTP Import, and Azure Maps.

To see the status of en enrichment

1. Go to **Data** > **Enrichment**. 
1. In the **My enrichments** tab, select the status of an enrichment to open a side pane. 
1. In the **Progress details** pane, expand the **Enrichments** section. 
1. Under the enrichment you want to see the progress, select **See details**. 
1. In the **Task details** pane, select **Show details** to see the processes that are involved in updating the enrichment and their status. 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
