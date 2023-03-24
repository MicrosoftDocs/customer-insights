---
title: "Enrich company profiles with Leadspace (preview)"
description: "General information about the Leadspace third-party enrichment."
ms.date: 11/15/2022
ms.reviewer: mhart

ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
---

# Enrich company profiles with Leadspace (preview)

Leadspace is a data science company that provides a B-to-B Customer Data Platform. It enables environments with unified customer profiles based on accounts to enrich their data. Enrich *Customer profiles* with attributes such as company size, location, or industry. Enrich *Contact profiles* with attributes such as title, persona, or email verification.

## Prerequisites

- An active Leadspace license.
- [Unified customer profiles](customer-profiles.md) based on accounts.
- A Leadspace [connection](connections.md) is [configured](#configure-the-connection-for-leadspace) by an administrator. Contact [Leadspace](https://www.leadspace.com/leadspace-microsoft-dynamics-365/) directly for details about their product.

## Configure the connection for Leadspace

You must be an [administrator](permissions.md#admin) in Customer Insights and have the “perpetual key” (referred to as **Leadspace token**).

1. Select **Add connection** when configuring an enrichment or go to **Settings** > **Connections** and select **Set up** on the Leadspace tile.

   :::image type="content" source="media/enrichment-Leadspace-connection.png" alt-text="Leadspace connection configuration page.":::

1. Enter a name for the connection and a valid Leadspace token.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Company data** from Leadspace tile.

   :::image type="content" source="media/leadspace-tile.png" alt-text="Screenshot of the Leadspace tile.":::

1. Review the overview and then select **Next**.

1. Select the connection. Contact an administrator if no connection is available.

1. Select **Next**.

1. Select the **Customer data set**  and choose the profile or segment you want to enrich with company data from Leadspace. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-Leadspace-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer data set.":::

1. Define which type of fields from your unified profiles to use for matching: the primary and/or secondary address. You can specify a field mapping for both addresses and enrich the profiles for both addresses separately. For example, for a home address and a business address. Select **Next**.

1. Map your fields to the company data from Leadspace. The **Name of company** field is required. For a higher match accuracy, up to two other fields, **Company website** and **Company location**, can be added.

   :::image type="content" source="media/enrichment-leadspace-mapping.png" alt-text="Leadspace field-mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Select the checkbox if you have *Contact profiles* that you would like to enrich. Customer Insights will automatically map the required fields.

   :::image type="content" source="media/enrichment-leadspace-contacts.png" alt-text="Leadspace contact records enrichment.":::

1. Select **Next**.

1. Provide a **Name** for the enrichment and the **Output table name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

For more information, see [Leadspace APIs](https://support.leadspace.com/hc/en-us/sections/201997649-API).

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
