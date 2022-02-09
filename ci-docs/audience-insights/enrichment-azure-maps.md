---
title: "Enrich customer profiles with location data from Azure Maps"
description: "General information about the Azure Maps first-party enrichment."
ms.date: 08/31/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of customer profiles with Azure Maps (preview)

Azure Maps provides location-centric data and services to deliver experiences based on geospatial data with built-in location intelligence. Azure Maps data enrichment services improve the precision of location information about your customers. It brings capabilities like address normalization and latitude and longitude extraction to Dynamics 365 Customer Insights.

## Prerequisites

To configure Azure Maps data enrichment, the following prerequisites must be met:

- You have an active Azure Maps subscription. To get a subscription, you can [sign up or get a free trial](https://azure.microsoft.com/services/azure-maps/).

- An Azure Maps [connection](connections.md) is available, *or* you have [administrator](permissions.md#admin) permissions and an active Azure Maps API key.

## Configure the enrichment

1. Go to **Data** > **Enrichment**. 

1. On the **Location** tile, select **Enrich my data**.

   :::image type="content" source="media/azure-maps-tile.png" alt-text="Azure Maps tile.":::

1. Select a [connection](connections.md) from the dropdown list. Contact an administrator if no Azure Maps connection is available. If you're an administrator, you can [configure the connection for Azure Maps](#configure-the-connection-for-azure-maps). 

1. Select **Next** to confirm the selection.

1. Choose the **Customer dataset** you want to enrich with location data from Azure Maps. You can select the **Customer** entity to enrich all your unified customer profiles, or select a segment entity to enrich only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-azure-maps-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer dataset.":::

1. Choose whether you want to map fields to the primary and/or secondary address. You can specify a field mapping for both addresses and enrich the profiles for both addresses separately&mdash;for example, for a home address and a business address. Select **Next**.

1. Define which fields from your unified profiles to use to look for matching location data from Azure Maps. The **Street 1** and **Zip/Postal Code** fields are required for the selected primary or secondary address. For higher match accuracy, you can add more fields.

   :::image type="content" source="media/enrichment-azure-maps-configuration.png" alt-text="Azure Maps enrichment configuration page.":::

1. Select **Next** to complete the field mapping.

1. Evaluate whether you want to modify **Advanced Settings**. These are provided to give maximum flexibility to handle advanced use cases, but the default values will be adequate in most cases:
   - **Type of addresses**: The default behavior is that the enrichment will return the best address match even if it's incomplete. To get only complete addresses&mdash;for example, addresses that include the house number&mdash;clear all the checkboxes except **Point Addresses**. 
   - **Language**: By default, addresses are returned in the language for the region that the address has been determined to belong to. To apply a standardized address language, select the language from the dropdown menu. For example, selecting **English** will return **Copenhagen, Denmark** instead of **København, Danmark**.

1. Provide a name for the enrichment.

1. Review your choices, and then select **Save enrichment**.

## Configure the connection for Azure Maps

You need to be an administrator in audience insights to configure connections. Select **Add connection** when configuring an enrichment, or go to **Admin** > **Connections** and select **Set up** on the Azure Maps tile.

1. In the **Display name** box, enter a name for the connection.

1. Provide a valid Azure Maps API key.

1. Review and provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.

:::image type="content" source="media/enrichment-azure-maps-connection.png" alt-text="Azure Maps connection configuration page.":::

## Enrichment results

To start the enrichment process, select **Run** from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time will depend on the size of your customer data and the API response times.

After the enrichment process is completed, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Azure Maps, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Azure Maps meets any privacy or security obligations you may have. For more information, go to [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
