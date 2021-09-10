---
title: "Enrichment of company profiles with Dun & Bradstreet"
description: "General information about the Dun & Bradstreet third-party enrichment."
ms.date: 09/30/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of company profiles with Dun & Bradstreet (preview)

Dun & Bradstreet provides commercial data, analytics, and insights for businesses. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include attributes such as DUNS number, company size, location, industry, and more.

## Prerequisites

To configure a Dun & Bradstreet enrichment, the following prerequisites must be met:

- You have an active [Dun & Bradstreet](https://www.dnb.com/) license.
- You have [unified customer profiles](customer-profiles.md) for companies.
- A Dun & Bradstreet [connection](connections.md) has already been configured by an administrator or you have [administrator](permissions.md#administrator) permissions and the relevant credentials from Dun & Bradstreet Connect. 

## Setting up your Dun & Bradstreet project

As a licensed user of Dun & Bradstreet, you can set up a project in [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights). 


1. Sign in to [Dun & Bradstreet Connect](https://connect.dnb.com?lead_source=microsoft_audienceinsights). To retrieve credentials, [restore your password](https://sso.dnb.com/signin/forgot-password&lead_source=microsoft_audienceinsights).
1. Download [our csv template file](tbd.md) that will be used to map the audience insights fields to the corresponding Dun & Bradstreet fields. 
1. Upload the file in the **Upload data** step of the Dun & Bradstreet project creation experience. 
1. When you have successfully created the project, select the horizontal dots in the Dun & Bradstreet project to see the available options.
   :::image type="content" source="media/enrichment-dnb-dots.png" alt-text="Screenshot of dots in a Dun & Bradstreet project.":::
1. Choose **Get S3 details**. Store this information in a safe place You'll it to [set up the connection for the enrichment](#configure-a-connection-for-dun--bradstreet) in audience insights. 
   :::image type="content" source="media/enrichment-dnb-s3info.png" alt-text="Screenshot of selection of s3 information in a Dun & Bradstreet project.":::



## Configure the enrichment

1. In audience insights, go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the Dun & Bradstreet tile and select **Get started**.

   :::image type="content" source="media/enrichment-dnb-tile.png" alt-text="Screenshot of the Dun & Bradstreet tile.":::

1. Select a [connection](connections.md) from the dropdown list. Contact an administrator if no connection is available. If you are an administrator, you can create a connection by selecting **Add connection** and choosing **Dun & Bradstreet**. 

1. Select **Connect to Dun & Bradstreet** to confirm the connection.

1. Select **Next** and choose the **Customer data set** you want to enrich with company data from Dun & Bradstreet. You can select the **Customer** entity to enrich all your customer profiles or select a segment entity to enrich only unified customer profiles contained in that segment.

1. Select **Next** and define which fields from your unified profiles are used to look for matching company data from Dun & Bradstreet. Either **DUNS number** or **Name of company** and **Country** field are required. 

   :::image type="content" source="media/enrichment-dnb-mapping.png" alt-text="Dun & Bradstreet field mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment and select **Save enrichment** after reviewing your choices.


## Configure a connection for Dun & Bradstreet 

You need to be an administrator to configure connections. Select **Add connection** when configuring an enrichment *or* go to **Admin** > **Connections** and select **Set up** on the Dun & Bradstreet tile.

1. Select **Get Started**. 

1. Enter a name for the connection in the **Display name** box.

1. Provide valid Dun & Bradstreet credentials and Dun & Bradstreet project details *Region, Drop folder path, and Drop folder name*. You [get this information](#setting-up-your-dun--bradstreet-project) from the Dun & Bradstreet project.

1. Review and provide your consent for **Data privacy and compliance** by selecting **I agree**.

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.
   
   :::image type="content" source="media/enrichment-dnb-connection.png" alt-text="Dun & Bradstreet connection configuration page.":::

## Enrichment results

After refreshing the enrichment, you can review the newly enriched company data under [My enrichments](enrichment-hub.md). You can find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md) and [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Dun & Bradstreet, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Dun & Bradstreet meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights administrator can remove this enrichment at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
