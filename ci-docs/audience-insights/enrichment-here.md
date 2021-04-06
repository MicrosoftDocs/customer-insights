---
title: "Enrichment of with the third-party enrichment HERE Technologies"
description: "General information about the HERE Technologies third-party enrichment."
ms.date: 12/10/2020
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of customer profiles with HERE Technologies (preview)

HERE Technologies is a location platform company that provides location-centric data and services. With HERE Technologies' data enrichment services, you can build a more precise location understanding of your customers with address normalization, latitude and longitude extraction, and more.

## Prerequisites

To configure HERE Technologies enrichments, the following prerequisites must be met:

- You have an active HERE Technologies subscription. To get a subscription, you can [sign-up here](https://developer.here.com/sign-up?utm_medium=referral&utm_source=Microsoft-Dynamics-CI&create=Freemium-Basic) or [contact HERE Technologies](https://developer.here.com/help?utm_medium=referral&utm_source=Microsoft-Dynamics-CI#how-can-we-help-you) directly. [Learn more about HERE Technologies Location Enrichment.](https://developer.here.com/location-enrichment?cid=Dev-MicrosoftDynamics-DB-0-Dev-&utm_source=MicrosoftDynamics&utm_medium=referral&utm_campaign=Online_Dev_ReferralMicrosoft)

- There is a HERE [connection](connections.md) available *or* you have [Administrator](permissions.md#administrator) permissions and the HERE Technologies API key.

## Configuration

1. Go to **Data** > **Enrichment**. A wizard flow is initiated that guides you through the configuration steps.

1. Select **Enrich my data** on the HERE Technologies tile and then click **Get started**.

   > [!div class="mx-imgBorder"]
   > ![HERE Technologies tile](media/HERE-tile.png "HERE Technologies tile")

1. Select a [connection](connections.md) from the drop-down. Reach out to an administrator if no connection is available. If you are an administrator you will be able to create a connection by clicking **Add connection** and selecting HERE Technologies from the drop-down, see the section below. 

1. Confirm connection selection by clicking **Connect to HERE Technologies**.

1.	Now, click **Next** and select the **Customer data set** you want to enrich with location data from HERE Technologies. You can select the **Customer** entity to enrich all your customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-HERE-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer data set.":::

1. Choose if you want to map fields to the primary and/or secondary address. You can specify a field mapping for both addresses (for example, a home and a business address) and enrich the profiles for both addresses separately. Select **Next**.

1. Define which fields from your unified profiles should be used to look for matching location data from HERE Technologies. The **Street 1** and **Zip/Postal Code** fields are required for the selected primary and/or secondary address. For a higher match accuracy, more fields can be added.

   > [!div class="mx-imgBorder"]
   > ![HERE Technologies enrichment configuration page](media/enrichment-HERE-configuration.png "HERE Technologies enrichment configuration page")

1. Select **Next** to complete the field mapping.

1. Finally, you provide a name for the enrichment. Save the enrichment by clicking on **Save enrichment** after reviewing your choices.

## Configuring connection for HERE technologies 

You need to be an administrator to be able to configure connections. You can click on **Add connection** in the wizard flow as described above *or* go to **Admin** > **Connections** and select HERE Technologies from the dropdown or click **Set up** on the HERE technologies tile.

1. Enter a name for the connection in the **Display name** box.

1. Provide a valid HERE Technologies API key.

1. Review and provide your consent for Data privacy and compliance by selecting the **I agree** checkbox

1. Click verify to get the configuration verified.

1. Once the verification has completed the connection can be saved by clicking **Save**.

> [!div class="mx-imgBorder"]
   > ![HERE Technologies connection configuration page](media/enrichment-HERE-connection.png "HERE Technologies connection configuration page")

## Enrichment results

To start the enrichment process, select **Run** from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time will depend on the size of your customer data and the API response times from HERE Technologies.

After the enrichment process completes, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md), [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to HERE Technologies, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that HERE Technologies meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
