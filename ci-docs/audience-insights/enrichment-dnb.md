---
title: "Enrichment of company profiles with Dun & Bradstreet"
description: "General information about the Dun & Bradstreet third-party enrichment."
ms.date: 04/09/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: skummer
---

# Enrichment of company profiles with Dun & Bradstreet (preview)

Dun & Bradstreet provides commercial data, analytics, and insights for businesses. It enables customers with unified customer profiles for companies to enrich their data. Enrichments include attributes such as DUNS number, company size, location, industry, and more.

## Prerequisites

To configure a Dun & Bradstreet enrichment, the following prerequisites must be met:

- You have an active Dun & Bradstreet license.
- You have [unified customer profiles](customer-profiles.md) for companies.
- A Dun & Bradstreet connection has already been configured by an administrator or you have [administrator](permissions.md#administrator) permissions and the relevant credentials from Dun & Bradstreet Connect. Contact [Dun & Bradstreet](https://www.dnb.com/&lead_source=microsoft_audienceinsights) directly for details about their product.

Click [here](https://www.dnb.com/&lead_source=microsoft_audienceinsights) for information about the data that Dun & Bradstreet provide and information about how to purchase a Dun & Bradstreet license.

Click [here](https://sso.dnb.com/signin/forgot-password&lead_source=microsoft_audienceinsights) to retrieve credentials if you are an existing Dun & Bradstreet customer.

## Setting up your Dun & Bradstreet project

Once you have purchased a Dun & Bradstreet license you can set up a project in Dun & Bradstreet Connect. The first step is to download this [csv file](https://www.dnb.com/&lead_source=microsoft_audienceinsights) that will be used to map the Audience Insights fields to the corresponding Dun & Bradstreet fields. Use this file in the **Upload data** step of the Dun & Bradstreet project creation wizard. 

Click the dots shown below to expose a menu and choose **Get S3 details** when you have successfully created a project

 :::image type="content" source="media/enrichment-dnb-dots.png" alt-text="Screenshot of dots in a Dun & Bradstreet project.":::
 
 :::image type="content" source="media/enrichment-dnb-s3info.png" alt-text="Screenshot of selection of s3 information in a Dun & Bradstreet project.":::

Store this information in a safe place as you will need it for setting up the enrichment in Audience Insights.

<!---  
In Dun & Bradstreet Connect follow these steps:

1. Click *Create new project* and provide a project name.
2. Click next, choose a name for your data, and upload the csv file that you downloaded above.
3. 

--->

## Configure the enrichment

1. In audience insights, go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the Dun & Bradstreet tile and select **Get started**.

   :::image type="content" source="media/enrichment-dnb-tile.png" alt-text="Screenshot of the Dun & Bradstreet tile.":::

1. Select a [connection](connections.md) from the dropdown list. Contact an administrator if no connection is available. If you are an administrator, you can create a connection by selecting **Add connection** and choosing **Dun & Bradstreet**. 

1. Select **Connect to Dun & Bradstreet** to confirm the connection.

1. Select **Next** and choose the **Customer data set** you want to enrich with company data from Dun & Bradstreet. You can select the **Customer** entity to enrich all your customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

1. Select **Next** and define which fields from your unified profiles are used to look for matching company data from Dun & Bradstreet. Either **DUNS number** *or* **Name of company** and **Country** field are required. 

   :::image type="content" source="media/enrichment-dnb-mapping.png" alt-text="Dun & Bradstreet field mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Provide a name for the enrichment and select **Save enrichment** after reviewing your choices.


## Configure a connection for Dun & Bradstreet 

You need to be an administrator to configure connections. Select **Add connection** when configuring an enrichment *or* go to **Admin** > **Connections** and select **Set up** on the Dun & Bradstreet tile.

1. Select **Get Started**. 

1. Enter a name for the connection in the **Display name** box.

1. Provide valid Dun & Bradstreet credentials and Dun & Bradstreet project details *Region, Drop folder path, and Drop folder name*.

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
