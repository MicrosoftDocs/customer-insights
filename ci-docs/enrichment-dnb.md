---
title: "Enrichment of company profiles with Dun & Bradstreet"
description: "General information about the Dun & Bradstreet third-party enrichment."
ms.date: 04/26/2022
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of company profiles with Dun & Bradstreet (Preview)

Dun & Bradstreet provides commercial data, analytics, and insights for businesses. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include attributes such as DUNS number, company size, location, industry, and more.

## Prerequisites

- An active [Dun & Bradstreet](https://www.dnb.com/marketing/media/give-your-data-a-boost.html?source=microsoft_audience_insights) license.
- [Unified customer profiles](customer-profiles.md) for companies.
- A Dun & Bradstreet [project](#set-up-your-dun--bradstreet-project) is set up.
- A Dun & Bradstreet [connection](connections.md) is  [configured](#configure-a-connection-for-dun--bradstreet) by an administrator.

## Set up your Dun & Bradstreet project

As a licensed user of Dun & Bradstreet, you can set up a project in [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights).

1. Sign in to [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights). To retrieve credentials, [restore your password](https://sso.dnb.com/signin/forgot-password?lead_source=microsoft_audienceinsights).

1. Download [our csv template file](https://c360devenrichment.blob.core.windows.net/mapping/DnBCIdatamapping.csv) that will be used to map the Customer Insights fields to the corresponding Dun & Bradstreet fields.

1. Upload the file in the **Upload data** step of the Dun & Bradstreet project creation experience.

1. Select the horizontal dots under the relevant **source** in the newly created Dun & Bradstreet project to see the available options.

   :::image type="content" source="media/enrichment-dnb-dots.png" alt-text="Screenshot of dots in a Dun & Bradstreet project.":::

1. Choose **Get S3 details**. Store this information in a safe place. You'll need it to [set up the connection for the enrichment](#configure-a-connection-for-dun--bradstreet) in Customer Insights.

   :::image type="content" source="media/enrichment-dnb-s3info.png" alt-text="Screenshot of selection of s3 information in a Dun & Bradstreet project.":::

## Configure a connection for Dun & Bradstreet

You must be an [administrator](permissions.md#admin)  and have the credentials from Dun & Bradstreet Connect.

1. Select **Add connection** when configuring an enrichment or go to **Admin** > **Connections** and select **Set up** on the Dun & Bradstreet tile.

1. Select **Get Started**.

1. Enter a name for the connection.

1. Provide valid Dun & Bradstreet credentials and Dun & Bradstreet project details *Region, Drop folder path, and Drop folder name*. You [get this information](#set-up-your-dun--bradstreet-project) from the Dun & Bradstreet project.

1. Review and provide your consent for [Data privacy and compliance](#data-privacy-and-compliance) by selecting **I agree**.

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.

   :::image type="content" source="media/enrichment-dnb-connection.png" alt-text="Dun & Bradstreet connection configuration page.":::

### Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Dun & Bradstreet, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you're responsible for ensuring that Dun & Bradstreet meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights administrator can remove this enrichment at any time to discontinue use of this functionality.

## Configure the enrichment

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **Company data** for Dun & Bradstreet tile.

   :::image type="content" source="media/enrichment-dnb-tile.png" alt-text="Screenshot of the Dun & Bradstreet tile.":::

1. Review the overview and then select **Next**.

1. Select the connection and confirm. Contact an administrator if one is not available.

1. Select **Next**.

1. Select the **Customer data set** and choose the profile or segment you want to enrich with company data from Dun & Bradstreet. The *Customer* entity enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Define which type of fields from your unified profiles to use for matching company data from Dun & Bradstreet. At least one of the fields **Name and address**, **Phone**, or **Email** is required.

1. Select **Next**

1. Map your fields to the company data from Dun & Bradstreet. Either **DUNS number** or **Name of company** and **Country** fields are required. The country field supports [two or three letter country codes](https://www.iso.org/iso-3166-country-codes.html), country name in English, country name in native language, and phone prefix. Some common country variants include:

   - US: United States of America, United States, USA, America.
   - CA: Canada.
   - GB: United Kingdom, UK, Great Britain, GB, United Kingdom of Great Britain and Northern Ireland, United Kingdom of Great Britain.
   - AU: Australia, Commonwealth of Australia.
   - FR: France, French Republic.
   - DE: Germany, German, Deutschland, Allemagne, Federal Republic of Germany, Republic of Germany.

      :::image type="content" source="media/enrichment-dnb-mapping.png" alt-text="Dun & Bradstreet field-mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment and select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## Enrichment results

After a completed [enrichment run](enrichment-hub.md#run-or-refresh-an-enrichment), select the enrichment to review the results.

In addition to the standard results, the **Enriched customers preview** tile shows a sample of the enriched data. Select **See more** and select the **Data** tab to access a detailed view of each enriched profile.

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE[footer-include](includes/footer-banner.md)]
