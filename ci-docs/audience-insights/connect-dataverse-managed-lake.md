---
title: "Connect to tables in Microsoft Dataverse"
description: "Import data from a Microsoft Dataverse managed data lake."
ms.date: 12/06/2021
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
manager: shellyha
ms.reviewer: mhart
---

# Connect to data in a Microsoft Dataverse managed data lake



This article provides information on how Dataverse users can quickly connect to analytical entities in a Microsoft Dataverse managed lake. 

> [!NOTE]
> You must be an admin on the Dataverse organization to proceed and view the list of entities available in the managed lake.

## Important considerations

Data stored in online services, such as Azure Data Lake Storage, may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Connect to a Dataverse managed lake

1. In audience insights, go to **Data** > **Data sources**.

2. Select **Add data source**.

3. Select **Microsoft Dataverse** and select **Next**.

4. Enter a **Name** for the data source and select **Next**. 

5. Provide the **Server address** for the Dataverse organization, and select **Sign in**.

   :::image type="content" source="media/ingest-dataverse-server-address.png" alt-text="Screen in data ingestion step where a user can enter the Dataverse environment URL.":::

6. Select the tables you want to ingest as entities to audience insights from the available list.    

   > [!NOTE]
   > If some tables are already selected, they might be used by other Dynamics 365 applications (such as Dynamics 365 Sales Insights or Customer Service Insights). You can't change the selection. These tables will be available as entities once the data source is created.

   :::image type="content" source="media/select-dataverse-entities.png" alt-text="Dialog box showing a list of entities in the Dataverse environment.":::

7. Save your selection to start syncing the selected tables from Dataverse. You'll find the newly added connection on the **Data sources** page. It will be queued for refresh and show the entity count as 0 until all the selected tables are synced.

Only one data source of an environment can simultaneously use the same Dataverse managed lake.

## Edit a Dataverse managed lake data source

You only edit the entity selection after creating the data source. For example, if additional entities were added to Dataverse and you want to import them too.    
To connect to a different Dataverse data lake, [create a new data source](#connect-to-a-dataverse-managed-lake).

1. In audience insights, go to **Data** > **Data sources**.

2. Next to the data source you'd like to update, select the ellipsis.

3. Select the **Edit** option from the list.

4. Select additional entities from the available list of entities and select **Save**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
