---
title: "Enrichment of company profiles with the third-party enrichment Leadspace"
description: "General information about the Leadspace third-party enrichment."
ms.date: 09/30/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
manager: shellyha
---

# Enrichment of company profiles with Leadspace (preview)

Leadspace is a data science company that provides a B2B Customer Data Platform. It enables environments with unified customer profiles based on accounts to enrich their data. Enrich *Customer profiles* with attributes such as company size, location, or industry. Enrich *Contact profiles* with attributes such as title, persona, or email verification.

## Prerequisites

To configure Leadspace, the following prerequisites must be met:

- You have an active Leadspace license.
- You have [unified customer profiles](customer-profiles.md) based on accounts.
- A Leadspace connection has already been configured by an administrator or you have [administrator](permissions.md#administrator) permissions and the “perpetual key” (referred to as **Leadspace token**). Contact [Leadspace](https://www.leadspace.com/products/leadspace-on-demand/) directly for details about their product.

## Configure the enrichment

1. In audience insights, go to **Data** > **Enrichment**.

1. Select **Enrich my data** on the Leadspace tile and select **Get started**.

   :::image type="content" source="media/leadspace-tile.png" alt-text="Screenshot of the Leadspace tile.":::

1. Select a [connection](connections.md) from the dropdown list. Contact an administrator if no connection is available. If you are an administrator, you can create a connection by selecting **Add connection** and choosing **Leadspace**. 

1. Select **Connect to Leadspace** to confirm the connection.

1. Select **Next** and choose the **Customer data set** you want to enrich with company data from Leadspace. You can select the **Customer** entity to enrich all your customer profiles or select a segment entity to enrich only customer profiles contained in that segment.

    :::image type="content" source="media/enrichment-Leadspace-configuration-customer-data-set.png" alt-text="Screenshot when choosing the customer data set.":::

1. Select **Next** and define which fields from your unified profiles are used to look for matching company data from Leadspace. The **Name of company** field is required. For a higher match accuracy, up to two other fields, **Company website** and **Company location**, can be added.

   :::image type="content" source="media/enrichment-leadspace-mapping.png" alt-text="Leadspace field-mapping pane.":::

1. Select **Next** to complete the field mapping.

1. Select the checkbox if you have *Contact profiles* that you would like to enrich. Audience insights will automatically map the required fields.

   :::image type="content" source="media/enrichment-leadspace-contacts.png" alt-text="Leadspace field-mapping pane.":::
 
1. Provide a name for the enrichment and select **Save enrichment** after reviewing your choices.


## Configure the connection for Leadspace 

You need to be an administrator to configure connections. Select **Add connection** when configuring an enrichment *or* go to **Admin** > **Connections** and select **Set up** on the Leadspace tile.

1. Select **Get Started**. 

1. Enter a name for the connection in the **Display name** box.

1. Provide a valid Leadspace token.

1. Review and provide your consent for **Data privacy and compliance** by selecting **I agree**.

1. Select **Verify** to validate the configuration.

1. After completing the verification, select **Save**.
   
   :::image type="content" source="media/enrichment-Leadspace-connection.png" alt-text="Leadspace connection configuration page.":::

## Enrichment results

After refreshing the enrichment, you can review the newly enriched company data under [My enrichments](enrichment-hub.md). You can find the time of the last update and the number of enriched profiles.

You can access a detailed view of each enriched profile by selecting **View enriched data**.

For more information, see [Leadspace APIs](https://support.leadspace.com/hc/en-us/sections/201997649-API).

## Next steps

Build on top of your enriched customer data. Create [segments](segments.md) and [measures](measures.md), and even [export the data](export-destinations.md) to deliver personalized experiences to your customers.

## Data privacy and compliance

When you enable Dynamics 365 Customer Insights to transmit data to Leadspace, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you are responsible for ensuring that Leadspace meets any privacy or security obligations you may have. For more information, see [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732).
Your Dynamics 365 Customer Insights administrator can remove this enrichment at any time to discontinue use of this functionality.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
