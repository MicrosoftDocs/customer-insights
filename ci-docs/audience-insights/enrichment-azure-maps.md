---
title: "Enrich customer profiles with location data from Azure Maps"
description: "General information about the Azure Maps first-party enrichment."
ms.date: 06/01/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of customer profiles with Azure Maps (preview)

Azure Maps provides location-centric data and services to deliver experiences based on geospatial data with built-in location intelligence. Azure Maps data enrichment services help create a more precise location understanding of your customers. It brings capabilities like address normalization or latitude and longitude extraction to Customer Insights.

## Prerequisites

To configure Azure Maps enrichments, the following prerequisites must be met:

- You have an active Azure Maps subscription. To get a subscription, you can [sign-up or get a free trial](https://azure.microsoft.com/en-us/services/azure-maps/).

- There's an Azure Maps [connection](connections.md) available *or* you have [administrator](permissions.md#administrator) permissions and an active Azure Maps API key.

## Configure the enrichment

1. Go to **Data** > **Enrichment**. 

1. On the **Location** tile, select **Enrich my data**.

   :::image type="content" source="media/azure-maps-tile.png" alt-text="Azure Maps tile":::

1. Select a [connection](connections.md) from the drop-down list. Contact an administrator if no Azure Maps connection is available. If you're an administrator, you can [configure the connection for Azure Maps](#configure-the-connection-for-azure-maps). 

1. Select **Next** to confirm the selection.

1. Choose the **Customer data set** you want to enrich with location data from Azure Maps. You can select the **Customer** entity to enrich all your unified customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-azure-maps-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer data set.":::

1. Choose if you want to map fields to the primary and/or secondary address. You can specify a field mapping for both addresses and enrich the profiles for both addresses separately. For example, if there's a home and a business address. Select **Next**.

1. Define which fields from your unified profiles should be used to look for matching location data from Azure Maps. The **Street 1** and **Zip/Postal Code** fields are required for the selected primary and/or secondary address. For a higher match accuracy, more fields can be added.

   :::image type="content" source="media/enrichment-azure-maps-configuration.png" alt-text="Azure Maps enrichment configuration page":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment. 

1. Select **Save enrichment** after reviewing your choices.

## Configure the connection for Azure Maps

You need to be an administrator in audience insights to configure connections. Select **Add connection** when configuring an enrichment *or* go to **Admin** > **Connections** and select **Set up** on the Azure Maps tile.

1. Enter a name for the connection in the **Display name** box.

1. Provide a valid Azure Maps API key.

1. Review and provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.

:::image type="content" source="media/enrichment-azure-maps-connection.png" alt-text="Azure Maps connection configuration page":::

## Enrichment results

To start the enrichment process, select **Run** from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time will depend on the size of your customer data and the API response times.

After the enrichment process completes, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md), [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

## Data privacy and compliance

<!-- is this section needed for first party services? -->

When you enable Dynamics 365 Customer Insights to transmit data to Azure Maps, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Azure Maps meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
