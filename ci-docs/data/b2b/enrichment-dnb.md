---
title: "Enrich company profiles with Dun & Bradstreet (preview)"
description: "General information about the Dun & Bradstreet third-party enrichment."
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
ms.custom: bap-template
---

# Enrich company profiles with Dun & Bradstreet (preview)

[!INCLUDE [public-preview-banner](../includes/public-preview-banner.md)]



Dun & Bradstreet provides commercial data, analytics, and insights for businesses. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include attributes such as DUNS number, company size, location, industry, and more.

[!INCLUDE [public-preview-note](../includes/public-preview-note.md)]

## Prerequisites

- An active [Dun & Bradstreet](https://www.dnb.com/marketing/media/give-your-data-a-boost.html?source=microsoft_audience_insights) license.
- [Unified customer profiles](../customer-profiles.md) for companies.
- A Dun & Bradstreet [project](#set-up-your-dun--bradstreet-project) is set up.
- A Dun & Bradstreet [connection](../connections.md) is [configured](#configure-a-connection-for-dun--bradstreet) by an administrator.

## Set up your Dun & Bradstreet project

As a licensed user of Dun & Bradstreet, you can set up a project in [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights).

1. Sign in to [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights). To retrieve credentials, [restore your password](https://sso.dnb.com/signin/forgot-password?lead_source=microsoft_audienceinsights).

1. Download [our csv template file](./ciad-files/DnBCIdatamapping.csv) that will be used to map the Dynamics 365 Customer Insights - Data fields to the corresponding Dun & Bradstreet fields.

1. Upload the file in the **Upload data** step of the Dun & Bradstreet project creation experience.

1. Select the horizontal dots under the relevant **source** in the newly created Dun & Bradstreet project to see the available options.

   :::image type="content" source="media/enrichment-dnb-dots.png" alt-text="Screenshot of dots in a Dun & Bradstreet project.":::

1. Choose **Get S3 details**. Store this information in a safe place. You'll need it to [set up the connection for the enrichment](#configure-a-connection-for-dun--bradstreet).

   :::image type="content" source="media/enrichment-dnb-s3info.png" alt-text="Screenshot of selection of s3 information in a Dun & Bradstreet project.":::

## Configure a connection for Dun & Bradstreet

You must be an [administrator](../user-roles.md#admin) in Customer Insights - Data and have the credentials from Dun & Bradstreet Connect.

1. Select **Add connection** when configuring an enrichment or go to **Settings** > **Connections** and select **Set up** on the Dun & Bradstreet tile.

1. Enter a name for the connection.

1. Provide valid Dun & Bradstreet credentials and Dun & Bradstreet project details *Region, Drop folder path, and Drop folder name*. You [get this information](#set-up-your-dun--bradstreet-project) from the Dun & Bradstreet project.

1. Review the [data privacy and compliance](../connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

   :::image type="content" source="media/enrichment-dnb-connection.png" alt-text="Dun & Bradstreet connection configuration page.":::

## Supported countries or regions

We currently support the following country/region options: Canada (English) or United States (English).

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Company data** for Dun & Bradstreet tile.

   :::image type="content" source="media/enrichment-dnb-tile.png" alt-text="Screenshot of the Dun & Bradstreet tile.":::

1. Review the overview and then select **Next**.

1. Select the connection and confirm. Contact an administrator if no connection is available.

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with company data from Dun & Bradstreet. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Define which type of fields from your unified profiles to use for matching company data from Dun & Bradstreet. At least one of the fields **Name and address**, **Phone**, or **Email** is required.

1. Select **Next**

1. Map your fields to the company data from Dun & Bradstreet. Either **DUNS number** or **Name of company** and **Country** fields are required.

      :::image type="content" source="media/enrichment-dnb-mapping.png" alt-text="Dun & Bradstreet field-mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Provide a **Name** for the enrichment and the **Output table name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](../includes/enrichment-results.md)]

## Next steps

[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]

[!INCLUDE[footer-include](../includes/footer-banner.md)]
