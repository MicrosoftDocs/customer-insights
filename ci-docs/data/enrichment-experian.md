---
title: Enrich customer profiles with demographics from Experian (preview)
description: Enrich customer profiles with Experian demographics like household size and income to gain deeper customer insights. Learn how to configure this enrichment.
ms.date: 07/13/2026
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: sfi-image-nochange
---

# Enrich customer profiles with demographics from Experian (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Experian is a global leader in consumer and business credit reporting and marketing services. By using Experian’s data enrichment services, you can gain a deeper understanding of your customers by enriching your customer profiles with demographic data such as household size, income, and more.

## Supported countries/regions

You can currently enrich customer profiles in the United States only.

## Prerequisites

- An active Experian subscription. To get a subscription, [contact Experian](https://www.experian.com/marketing-services/contact) directly. [Learn more about Experian Data Enrichment](https://www.experian.com/marketing-services/microsoft?cmpid=ems_web_mci_cdppage).

- An administrator configured an [Experian connection](#configure-the-connection-for-experian). Learn more about [connections](connections.md).

- Experian User ID, Party ID, and Model Number for your SSH-enabled Secure Transport (ST) account that Experian created for you.

## Configure the connection for Experian

You must be an [administrator](user-roles.md#admin) in Customer Insights - Data and have an Experian User ID, Party ID, and Model Number.

1. Select **Add connection** when configuring an enrichment, or go to **Settings** > **Connections** and select **Set up** on the Experian tile.

   :::image type="content" source="media/enrichment-Experian-connection.png" alt-text="Screenshot of the Experian connection configuration pane.":::

1. Enter a name for the connection and a valid User ID, Party ID, and Model Number for your Experian Secure Transport account.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Demographics** from Experian tile.

   :::image type="content" source="media/experian-tile.png" alt-text="Screenshot of the Experian tile in the enrichment overview page.":::

1. Review the overview and then select **Next**.

1. Select the connection. Contact an administrator if no connection is available.

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with demographics data from Experian. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-Experian-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer data set.":::

1. Define which type of fields from your unified profiles to use for matching demographics data from Experian. At least one of the fields **Name and address**, **Phone**, or **Email** is required. For higher match accuracy, add other fields. Select **Next**.

1. Map your fields to the demographic data from Experian.

1. Select **Next** to complete the field mapping.

1. Provide a **Name** for the enrichment and the **Output table name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

The **Number of customers enriched by field** metric shows the coverage for each enriched field.


## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
