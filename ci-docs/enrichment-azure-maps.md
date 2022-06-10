---
title: "Enrich customer profiles with location data from Azure Maps"
description: "General information about the Azure Maps first-party enrichment."
ms.date: 06/10/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of customer profiles with Azure Maps (preview)

Azure Maps provide location-centric data and services to deliver experiences based on geospatial data with built-in location intelligence. Azure Maps data enrichment services improve the precision of location information about your customers. It brings capabilities like address normalization and latitude and longitude extraction to Dynamics 365 Customer Insights.

## Prerequisites

- An active Azure Maps subscription. To get a subscription, [sign up or get a free trial](https://azure.microsoft.com/services/azure-maps/).

- An Azure Maps [connection](connections.md) is [configured](#configure-the-connection-for-azure-maps) by an administrator.

## Configure the connection for Azure Maps

You must be an [administrator](permissions.md#admin) in Customer Insights and have an active Azure Maps API key.

1. Select **Add connection** when configuring an enrichment, or go to **Admin** > **Connections** and select **Set up** on the Azure Maps tile.

:::image type="content" source="media/enrichment-azure-maps-connection.png" alt-text="Azure Maps connection configuration page.":::

1. Enter a name for the connection and a valid Azure Maps API key.

1. Review and provide your consent for [Data privacy and compliance](#data-privacy-and-compliance) by selecting **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Azure Maps, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you're responsible for ensuring that Azure Maps meet any privacy or security obligations you may have. For more information, go to [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Location** from Microsoft Azure Maps tile.

   :::image type="content" source="media/azure-maps-tile.png" alt-text="Azure Maps tile.":::

1. Review the overview and then select **Next**.

1. Select the connection. Contact an administrator if one is not available.

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with data from Microsoft. The *Customer* entity enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Define which type of fields from your unified profiles to use for matching: the primary and/or secondary address. You can specify a field mapping for both addresses and enrich the profiles for both addresses separately. For example, for a home address and a business address. Select **Next**.

1. Map your fields to the location data from Azure Maps. The **Street 1** and **Zip/Postal Code** fields are required for the selected primary and/or secondary address. For higher match accuracy, add more fields.

   :::image type="content" source="media/enrichment-azure-maps-attributes.png" alt-text="Azure Maps attribute mapping.":::

1. Select **Next** to complete the field mapping.

1. Review **Advanced Settings** which offer maximum flexibility to handle advanced use cases. However, the following default values typically do not need to be changed.

   - **Type of addresses**: Best address match returns even if it's incomplete. To get only complete addresses&mdash;for example, addresses that include the house number&mdash;clear all the checkboxes except **Point Addresses**.
   - **Language**: Addresses return in the language based on the address region. To apply a standardized address language, select the language from the dropdown menu. For example, selecting **English** returns **Copenhagen, Denmark** instead of **København, Danmark**.
   - **Maximum number of results**: Number of results per address.

1. Select **Next**.

1. Provide a **Name** for the enrichment and the **Output entity name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## Enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

The **Number of customers enriched by field** provides a drill-down into the coverage of each enriched field.

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
