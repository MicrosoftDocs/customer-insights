---
title: "LiveRamp identity data enrichment"
description: "Enrich customer profiles with LiveRamp data."
ms.date: 03/02/2022
ms.reviewer: mhart

ms.subservice: audience-insights
ms.topic: how-to
author: kishorem-ms
ms.author: kishorem
manager: shellyha
---

# Enrich customer profiles with identity data from LiveRamp (Preview) 

LiveRamp provides deterministic offline identity resolution and consolidation of customer data. You can map personal identifiers in your customer data to the AbiliTec identity graph and receive AbiliTec IDs. You can then use these IDs for better unification of your customer data. 

## Prerequisites 

To configure the enrichment, the following prerequisites must be met: 

- You have an active LiveRamp subscription. To get a subscription, reach out to your LiveRamp account team or to [dynamics@liveramp.com](mailto:dynamics@liveramp.com) for more information.   

- An active AbiliTec subscription with a client ID and secret to access the API. For more information, see [AbiliTec API Developer Hub](https://developers.liveramp.com/abilitec-api/). 

## Supported countries/regions 

We currently support enriching customer profiles with LiveRamp data in the United States only. 

## Configure the enrichment 

1. Go to **Data** > **Enrichment** and select the **Discover** tab. 

1. Select **Enrich my data** on the **Identity** tile. 

   :::image type="content" source="media/liveramp-tile.png" alt-text="Identity tile in the enrichment overview page. ":::

1. Select a [connection](connections.md) from the dropdown list. Contact an administrator if no connection is available. If you're an administrator, you can create a connection by selecting **Add connection**. Choose **LiveRamp** from the dropdown list. 

1. Select **Next** and choose the **Customer data set** you want to enrich with identity data from LiveRamp. You can select the *Customer* entity to enrich all your customer profiles or select a *segment* entity to enrich only customer profiles contained in that segment. 

1. Select **Next** and define which type of fields from your unified profiles should be used to look for matching identity data from LiveRamp. At least one of the fields **Name and address**, **Phone**, or **E-mail** is required. 

   > [!TIP]
   > The more key identifiers and fields you map, the more likelihood of a higher match rate 

1. Map the fields from your unified *Customer* entity that will be used for matching with LiveRamp’s AbiliTec ID graph. 

   :::image type="content" source="media/liveramp-data-mapping.png" alt-text="Data mapping options for the LiveRamp enrichment.":::

1. Select **Next** to complete the field mapping. 

1. Provide a **Name** for the enrichment and the **Output entity**. 

1. Select **Save enrichment** after reviewing your choices. 

## Configure the connection for LiveRamp 

You need to be an administrator to [configure connections](connections.md). Select **Add connection** when configuring the enrichment or go to **Admin** > **Connections** and select **Set up** on the **LiveRamp** tile. 

:::image type="content" source="media/liveramp-connection.png" alt-text="Configuration pane to set up the connection to the LiveRamp AbiliTec service. ":::

1. For **Display name**, enter the name of the connection. 

1. Provide a valid LiveRamp client ID and a secret. 

1. Review and provide your consent for **Data privacy and compliance** by selecting the **I agree** checkbox. 

1. Select **Verify** to validate the configuration. 

1. To complete the connection, select **Save**. 

## Enrichment results 

To start the enrichment process, select Run from the command bar. You can also let the system run the enrichment automatically as part of a [scheduled refresh](system.md#schedule-tab). The processing time depends on the size of your customer data. 

After the enrichment process is complete, you can review the newly enriched customer profiles data under **My enrichments**. Additionally, you'll find the time of the last update and the number of enriched profiles. 

You can access a detailed view of each enriched profile by selecting **View enriched** data. 

## Next steps

Build on top of your enriched customer data. Use the AbiliTec IDs to consolidate customer profiles into a person-based view. 
[!INCLUDE [next-steps-enrichment](../includes/next-steps-enrichment.md)]

## Data privacy and compliance 

When you enable Dynamics 365 Customer Insights to transmit data to LiveRamp, you allow transfer of data outside of the compliance boundary for Dynamics 365 Customer Insights, including potentially sensitive data such as Personal Data. Microsoft will transfer such data at your instruction, but you're responsible for ensuring that LiveRamp meets any privacy or security obligations you may have. For more information, review the [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?linkid=396732). Your Dynamics 365 Customer Insights Administrator can remove this enrichment at any time to discontinue use of this functionality. 


[!INCLUDE[footer-include](includes/footer-banner.md)]
