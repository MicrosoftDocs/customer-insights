---
title: "Enrich customer profiles with HERE Technologies (preview)"
description: "General information about the HERE Technologies third-party enrichment."
ms.date: 06/10/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrich customer profiles with HERE Technologies (preview)

HERE Technologies is a location platform company that provides location-centric data and services. HERE Technologies' data enrichment services improve the precision of location information about your customers. It provides address normalization, latitude and longitude extraction, and more.

## Prerequisites

- An active HERE Technologies subscription. To get a subscription, [sign up here](https://developer.here.com/sign-up?utm_medium=referral&utm_source=Microsoft-Dynamics-CI&create=Freemium-Basic) or [contact HERE Technologies](https://developer.here.com/help?utm_medium=referral&utm_source=Microsoft-Dynamics-CI#how-can-we-help-you) directly. [Learn more about HERE Technologies Location Enrichment.](https://developer.here.com/location-enrichment?cid=Dev-MicrosoftDynamics-DB-0-Dev-&utm_source=MicrosoftDynamics&utm_medium=referral&utm_campaign=Online_Dev_ReferralMicrosoft)

- A HERE [connection](connections.md) is [configured](#configure-the-connection-for-here-technologies) by an administrator.

## Configure the connection for HERE Technologies

You must be an [administrator](permissions.md#admin) in Customer Insights and have an active HERE Technologies API key.

1. Select **Add connection** when configuring an enrichment, or go to **Admin** > **Connections** and select **Set up** on the HERE Technologies tile.

1. Enter a name for the connection and a valid HERE Technologies API key.

1. Review and provide your consent for [Data privacy and compliance](#data-privacy-and-compliance) by selecting **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

   :::image type="content" source="media/enrichment-HERE-connection.png" alt-text="HERE Technologies connection configuration page.":::

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to HERE Technologies, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that HERE Technologies meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights administrator can remove this enrichment at any time to discontinue use of this functionality.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Location** from HERE Technologies tile.

   :::image type="content" source="media/HERE-tile.png" alt-text="HERE Technologies tile.":::

1. Review the overview and then select **Next**.

1. Select the connection. Contact an administrator if no connection is available.

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with data from HERE Technologies. The *Customer* entity enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Define which type of fields from your unified profiles to use for matching: the primary and/or secondary address. You can specify a field mapping for both addresses and enrich the profiles for both addresses separately. For example, for a home address and a business address. Select **Next**.

1. Map your fields to the data from HERE Technologies. The **Street 1** and **Zip/Postal Code** fields are required for the selected primary and/or secondary address. For a higher match accuracy, add more fields.

1. Select **Next** to complete the field mapping.

1. Provide a **Name** for the enrichment and the **Output entity name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

The **Number of customers enriched by field** provides a drill-down into the coverage of each enriched field.

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
